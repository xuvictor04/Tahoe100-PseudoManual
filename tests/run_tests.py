#!/usr/bin/env python3
"""run_tests.py - the whole tahoemap pipeline on synthetic Tahoe-100M data with planted answers.

    python3 tests/run_tests.py [--workdir DIR] [--seed 0] [--regen] [--only STAGE,...] [--keep-going]

1. Makes (or reuses) a synthetic download with make_synthetic_tahoe.py: 7 plates (one unreliable mixed-dose plate),
   18 real cell lines, 94 real drugs, 1,200 genes, planted drug effects, gene modules (including pairs of modules
   that move in opposite directions), and every artifact the method corrects (ground_truth.json says what).
2. Runs `python -m tahoemap run` on it (offline: the reference stage needs the network and is skipped), in
   --workdir/out_seedN. An output made from other synthetic data (an older generator) is removed first: the build
   keeps a plate it has summed before while the plate's file list is unchanged, and the synthetic files keep their
   names when the data are made again, so it would sum the old counts even with --redo (see fresh_out).
3. Checks each stage against the planted truth. Every check prints PASS / FAIL / WARN with its numbers; the exit
   code is 1 if anything FAILs. Thresholds are set inside what seed 0 (the default) gives, so a FAIL there means a
   regression. Other seeds draw other data, and with 18 lines a few planted effects sit near what can be detected:
   seeds 1 and 2 each fail a few such checks (on both: CDKN1A rising in one TP53-mutant line, and TP53 -> cells
   under the DNA-damaging drugs significant only within the TP53 group).
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import traceback


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# the default work folder: /tmp/tahoemap_test, or on Windows the system temp folder (not C:\tmp)
DEFAULT_WORKDIR = "/tmp/tahoemap_test" if os.name != "nt" else os.path.join(tempfile.gettempdir(), "tahoemap_test")
sys.path.insert(0, REPO)

RESULTS = []


def check(stage, name, fn):
    try:
        ok, detail = fn()
        status = "WARN" if isinstance(ok, str) and ok == "warn" else ("PASS" if bool(ok) else "FAIL")
    except Exception as e:  # noqa: BLE001
        status, detail = "FAIL", f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=3)}"
    RESULTS.append({"stage": stage, "check": name, "status": status, "detail": str(detail)})
    print(f"  [{status}] {stage}: {name} -- {detail}", flush=True)


def ensure_data(work, seed, regen):
    data = os.path.join(work, f"data_seed{seed}")
    gen = os.path.join(HERE, "make_synthetic_tahoe.py")
    h = hashlib.sha1()
    for f in (gen, os.path.join(HERE, "tahoe_meta_snapshot.py")):
        h.update(open(f, "rb").read().replace(b"\r\n", b"\n"))
    key = f"{h.hexdigest()}-{seed}"
    stamp = os.path.join(data, "generator.key")
    made = regen or not (os.path.exists(stamp) and open(stamp, encoding="utf-8").read() == key)
    if made:
        print(f"Generating synthetic data (seed {seed}) in {data} ...", flush=True)
        subprocess.run([sys.executable, gen, data, "--seed", str(seed)], check=True)
        with open(stamp, "w", encoding="utf-8") as fh:
            fh.write(key)
    return data, key, made


# what a tahoemap output folder holds (fresh_out removes a folder only if it looks like one)
OUTPUT_MARKS = ("atlas", "stages", "run.log", "pipeline_console.log")


def fresh_out(out, key, made):
    """Make sure the output folder was made from these data (generator key `key`), else remove it first.

    The build keeps a plate it has summed before when the plate's file list is unchanged (atlas_core._build_group,
    verbatim: how a stopped build resumes), even with --redo. The synthetic files keep their names when the data are
    made again (a new generator draws the same cells into the same 39 files), so an output from earlier data would
    keep the old counts while ground_truth.json describes the new ones: the plants a newer generator adds would be
    missing. So the key of the data an output was made from is kept next to it (OUT.data.key, outside the folder the
    pipeline and the export own); an output without it, with another key, or older than data made now is removed."""
    stamp = out + ".data.key"
    old = open(stamp, encoding="utf-8").read() if os.path.exists(stamp) else None
    if os.path.isdir(out) and os.listdir(out) and (made or old != key):
        if not any(os.path.exists(os.path.join(out, m)) for m in OUTPUT_MARKS):
            sys.exit(f"{out} is not a tahoemap output (none of {', '.join(OUTPUT_MARKS)} in it); it is left as it is. "
                     "Give another --workdir.")
        why = "the data were made again" if made else ("it was made from other synthetic data" if old else
                                                       "its synthetic data are not recorded")
        print(f"Removing the earlier output {out} ({why}): the build would reuse its plates.", flush=True)
        try:
            shutil.rmtree(out)
        except OSError as e:
            sys.exit(f"Could not remove {out} ({type(e).__name__}: {e}). Close what has a file of it open, or "
                     "remove it yourself, and run again.")
    os.makedirs(out, exist_ok=True)
    with open(stamp, "w", encoding="utf-8") as fh:
        fh.write(key)


def run_pipeline(data, out, extra=()):
    cmd = [sys.executable, "-m", "tahoemap", "run", "--data", data, "--out", out, "--min-cells", "10",
           "--offline", "--dims", "32", "--truth", os.path.join(data, "ground_truth.json"), *extra]
    print("Running:", " ".join(cmd), flush=True)
    t0 = time.time()
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    with open(os.path.join(out, "pipeline_console.log"), "w", encoding="utf-8") as fh:
        fh.write(r.stdout + "\n" + r.stderr)
    print(f"  pipeline exit code {r.returncode} in {(time.time() - t0) / 60:.1f} min "
          f"(log: {os.path.join(out, 'run.log')})", flush=True)
    if r.returncode != 0:
        print(r.stdout[-3000:], r.stderr[-3000:])
    return r.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", default=os.environ.get("TAHOE_TEST_DIR", DEFAULT_WORKDIR))
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--regen", action="store_true")
    ap.add_argument("--reuse", action="store_true", help="do not rerun the pipeline if its output exists")
    a = ap.parse_args()
    os.makedirs(a.workdir, exist_ok=True)
    data, key, made = ensure_data(a.workdir, a.seed, a.regen)
    out = os.path.join(a.workdir, f"out_seed{a.seed}")
    fresh_out(out, key, made)
    if not (a.reuse and os.path.exists(os.path.join(out, "stages", "map.json"))):
        rc = run_pipeline(data, out, ("--redo",))
        check("run", "pipeline finishes", lambda: (rc == 0, f"exit code {rc}"))
    truth = json.load(open(os.path.join(data, "ground_truth.json"), encoding="utf-8"))
    from tests import checks                                # noqa: E402  (the per-stage checks)
    checks.run_all(out, data, truth, check)
    n = {s: sum(r["status"] == s for r in RESULTS) for s in ("PASS", "WARN", "FAIL")}
    with open(os.path.join(a.workdir, "test_results.json"), "w", encoding="utf-8") as fh:
        json.dump({"counts": n, "results": RESULTS}, fh, indent=1)
    print(f"\n{n['PASS']} passed, {n['WARN']} warnings, {n['FAIL']} failed  "
          f"(details: {os.path.join(a.workdir, 'test_results.json')})")
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()

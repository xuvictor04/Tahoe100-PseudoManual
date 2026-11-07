#!/usr/bin/env python3
"""run_tests.py - the whole tahoemap pipeline on synthetic Tahoe-100M data with planted answers.

    python3 tests/run_tests.py [--workdir DIR] [--seed 0] [--regen] [--only STAGE,...] [--keep-going]

1. Makes (or reuses) a synthetic download with make_synthetic_tahoe.py: 7 plates (one unreliable mixed-dose plate),
   18 real cell lines, 94 real drugs, 1,200 genes, planted drug effects, gene modules (including pairs of modules
   that move in opposite directions), and every artifact the method corrects (ground_truth.json says what).
2. Runs `python -m tahoemap run` on it (offline: the reference stage needs the network and is skipped).
3. Checks each stage against the planted truth. Every check prints PASS / FAIL / WARN with its numbers; the exit
   code is 1 if anything FAILs. Thresholds are set well inside what seeds 0-2 give, so a FAIL means a regression.
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
import traceback


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
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
    if regen or not (os.path.exists(stamp) and open(stamp, encoding="utf-8").read() == key):
        print(f"Generating synthetic data (seed {seed}) in {data} ...", flush=True)
        subprocess.run([sys.executable, gen, data, "--seed", str(seed)], check=True)
        with open(stamp, "w", encoding="utf-8") as fh:
            fh.write(key)
    return data


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
    ap.add_argument("--workdir", default=os.environ.get("TAHOE_TEST_DIR", "/tmp/tahoemap_test"))
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--regen", action="store_true")
    ap.add_argument("--reuse", action="store_true", help="do not rerun the pipeline if its output exists")
    a = ap.parse_args()
    os.makedirs(a.workdir, exist_ok=True)
    data = ensure_data(a.workdir, a.seed, a.regen)
    out = os.path.join(a.workdir, f"out_seed{a.seed}")
    os.makedirs(out, exist_ok=True)
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

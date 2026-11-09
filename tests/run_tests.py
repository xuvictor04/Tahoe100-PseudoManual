#!/usr/bin/env python3
"""run_tests.py - the whole tahoemap pipeline on synthetic Tahoe-100M data with planted answers.

    python3 tests/run_tests.py [--workdir DIR] [--seed 0] [--regen] [--reuse]

--regen makes the synthetic data again; --reuse checks the output already in --workdir without running the pipeline
(when it finished: stages/explorer.json).

1. Makes (or reuses) a synthetic download with make_synthetic_tahoe.py: 7 plates (one unreliable mixed-dose plate),
   18 real cell lines, 94 real drugs, 1,200 genes, planted drug effects, gene modules (including pairs of modules
   that move in opposite directions), and every artifact the method corrects (ground_truth.json says what).
2. Runs `python -m tahoemap run --redo` on it (offline: the reference stage needs the network and is skipped), in
   --workdir/out_seedN; every stage runs, the explorer last. An output made from other synthetic data (an older
   generator) is removed first: a build keeps a plate it has summed before while the plate's file list is unchanged,
   and the synthetic files keep their names when the data are made again (see fresh_out; --redo now also removes
   the finished plates before the build).
3. Checks each stage against the planted truth (tests/checks.py), then the checks of tests/test_direction.py,
   tests/test_surfaces.py and tests/test_explorer.py on the same output, and the explorer's browser test
   (tests/test_explorer_browser.py) when that file is there and Playwright is installed (else a WARN: skipped).
   Every check prints PASS / FAIL / WARN with its numbers; the exit code is 1 if anything FAILs. Thresholds are
   set inside what seed 0 (the default) gives, so a FAIL there means a regression. Other seeds draw other data, and
   with 18 lines a few planted effects sit near what can be detected: seeds 1 and 2 each fail a few such checks (on
   both: CDKN1A rising in one TP53-mutant line, and TP53 -> cells under the DNA-damaging drugs significant only
   within the TP53 group).
"""

import argparse
import hashlib
import importlib
import inspect
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


BROWSER_TEST = os.path.join(HERE, "test_explorer_browser.py")
PLAYWRIGHT_HINT = ("pip install playwright, then python -m playwright install chromium")


def _status(ok):
    """A package check's result as run_tests' (True / False / 'warn'); also 'PASS' / 'FAIL' / 'WARN' strings."""
    if isinstance(ok, str):
        u = ok.strip().upper()
        return "warn" if u == "WARN" else u == "PASS"
    return bool(ok)


def browser_checks(out, data):
    """The explorer in a headless browser (tests/test_explorer_browser.py): its check(out, data, report=check) (each
    result one check; without a report argument its returned results are reported here), else the file run as a
    script (--out, --data; exit code 0 = pass). Skipped with a WARN when the file is not there or Playwright is not
    installed."""
    name = "pages in a headless browser (tests/test_explorer_browser.py)"
    if not os.path.exists(BROWSER_TEST):
        check("explorer", name, lambda: ("warn", "tests/test_explorer_browser.py is not in this code: skipped"))
        return
    try:
        importlib.import_module("playwright.sync_api")
    except ImportError:
        check("explorer", name, lambda: ("warn", f"Playwright not installed: skipped ({PLAYWRIGHT_HINT})"))
        return
    try:
        sys.path.insert(0, HERE)
        mod = importlib.import_module("test_explorer_browser")
    except Exception as e:  # noqa: BLE001
        check("explorer", name, lambda e=e: (False, f"cannot import it: {type(e).__name__}: {e}"))
        return
    if callable(getattr(mod, "check", None)) and "report" in inspect.signature(mod.check).parameters:
        try:                               # it reports each result itself, through check (its own stage name)
            res = mod.check(out, data, report=check)
        except Exception as e:  # noqa: BLE001
            check("explorer", name, lambda e=e: (False, f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=4)}"))
            return
        if not res:
            check("explorer", name, lambda: (False, "its check(out, data) reported no result"))
        return
    if callable(getattr(mod, "check", None)):
        try:
            res = mod.check(out, data)
        except Exception as e:  # noqa: BLE001
            check("explorer", name, lambda e=e: (False, f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=4)}"))
            return
        for r in res or []:
            nm, ok, detail = (list(r) + ["", ""])[:3]
            check("explorer", f"browser: {nm}", lambda ok=ok, detail=detail: (_status(ok) if _status(ok) != "warn"
                                                                              else "warn", detail))
        if not res:
            check("explorer", name, lambda: (False, "its check(out, data) returned no results"))
        return
    t0 = time.time()
    r = subprocess.run([sys.executable, BROWSER_TEST, "--out", out, "--data", data], cwd=REPO, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    tail = " | ".join((r.stdout + r.stderr).strip().splitlines()[-6:])
    check("explorer", name, lambda: (r.returncode == 0, f"exit code {r.returncode} in {time.time() - t0:.0f} s: "
                                                        f"{tail[-900:]}"))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--workdir", default=os.environ.get("TAHOE_TEST_DIR", DEFAULT_WORKDIR))
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--regen", action="store_true")
    ap.add_argument("--reuse", action="store_true", help="do not rerun the pipeline if its output exists (every "
                                                         "stage finished: stages/explorer.json)")
    a = ap.parse_args()
    os.makedirs(a.workdir, exist_ok=True)
    data, key, made = ensure_data(a.workdir, a.seed, a.regen)
    out = os.path.join(a.workdir, f"out_seed{a.seed}")
    fresh_out(out, key, made)
    if not (a.reuse and os.path.exists(os.path.join(out, "stages", "explorer.json"))):
        rc = run_pipeline(data, out, ("--redo",))
        check("run", "pipeline finishes", lambda: (rc == 0, f"exit code {rc}"))
    truth = json.load(open(os.path.join(data, "ground_truth.json"), encoding="utf-8"))
    from tests import checks                                # noqa: E402  (the per-stage checks)
    checks.run_all(out, data, truth, check)
    browser_checks(out, data)
    n = {s: sum(r["status"] == s for r in RESULTS) for s in ("PASS", "WARN", "FAIL")}
    with open(os.path.join(a.workdir, "test_results.json"), "w", encoding="utf-8") as fh:
        json.dump({"counts": n, "results": RESULTS}, fh, indent=1)
    print(f"\n{n['PASS']} passed, {n['WARN']} warnings, {n['FAIL']} failed  "
          f"(details: {os.path.join(a.workdir, 'test_results.json')})")
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()

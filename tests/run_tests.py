#!/usr/bin/env python3
"""run_tests.py - the whole tahoemap pipeline on synthetic Tahoe-100M data with planted answers.

    python3 tests/run_tests.py [--workdir DIR] [--seed 0] [--regen] [--reuse]

--regen makes the synthetic data again; --reuse checks the output already in --workdir without running the pipeline
(when it finished: stages/explorer.json).

1. Makes (or reuses) a synthetic download with make_synthetic_tahoe.py: 7 plates (one unreliable mixed-dose plate),
   18 real cell lines, 94 real drugs, 1,200 genes, planted drug effects, gene modules (including pairs of modules
   that move in opposite directions), and every artifact the method corrects (ground_truth.json says what). The
   newer plants (ground_truth.json): a neighbouring-well copy (an artifact and a top-dose tier), a translation
   inhibitor, TOP2 poisons, a promiscuous glucocorticoid gene, KRAS codon-12 and one-dose selectivity, an expression
   programme, a lineage-restricted set and its broad twin, and a p53 target that falls.
2. Copies the offline reference fixture (tests/fixtures/reference_cache: the ChEMBL records of the 94 synthetic
   drugs and the Ensembl r112 GTF genes of the panel and of the lines' driver genes) afresh to
   --workdir/reference_cache_seedN (the reference stage writes files next to the GTF, so the fixture itself is never
   used in place). Then runs `python -m tahoemap run --redo --offline --reference-cache <that copy>` on the data, in
   --workdir/out_seedN; every stage runs, reference right after tensor and the explorer last. Offline, the reference
   stage reads the GTF and the ChEMBL records from the fixture (drug annotations, mechanism classes, gene
   coordinates); HGNC, the gene sets and the Compara paralogues are not in it, so those parts say 'not loaded'. An
   output made from other synthetic data (an older generator) is removed first: a build keeps a plate it has summed
   before while the plate's file list is unchanged, and the synthetic files keep their names when the data are made
   again (see fresh_out; --redo also removes the finished plates before the build).
3. Checks each stage against the planted truth (tests/checks.py), then the checks of tests/test_direction.py,
   tests/test_surfaces.py and tests/test_explorer.py on the same output, the explorer's browser test
   (tests/test_explorer_browser.py) when that file is there and Playwright is installed (else a WARN: skipped), and
   the offline unit scripts (tests/test_mechanisms.py, test_tables_rules.py, test_relations_rules.py,
   test_validate_rules.py: one check each, exit code 0 = PASS); tests/checks.py also runs tests/test_fix_back.py (its
   unit checks on toy inputs and its checks of this output). Every check prints PASS / FAIL / WARN with its
   numbers; the exit code is 1 if anything FAILs. Thresholds are set inside what seed 0 (the default) gives, so a
   FAIL there means a regression. One planted effect is below what its rule can call on seed 0 and is a WARN that
   says so: the 'lowered by mTOR' module label (a stronger planted fall makes the ribosome genes join the proteasome
   genes' module, which the curated proteasome set then names). The direction edges of a version N output (N >= 5)
   are compared with tests/fixtures/direction_v<VERSION>_seed0.tsv (now v6; test_direction.py --write-fixture; other
   seeds are not compared). Other seeds draw other data, and with 18 lines a few planted effects sit near what can be
   detected: seed 1 fails three such checks (CDKN1A rising in one TP53-mutant line, NCI-H1299; TP53 -> cells under the
   DNA-damaging drugs significant only within the TP53 group; the map's HDAC arms parting by 0.7 arm spreads, under
   the 1.5 asked) and warns that the one-dose plant gave no selectivity arrow there. The planted natural knockout and
   the failed well are read from ground_truth.json (and atlas/effects/failed_wells.csv), so no check names seed 0's.
"""

import argparse
import hashlib
import importlib
import inspect
import json
import os
import shutil
import stat
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


FIXTURES = os.path.join(HERE, "fixtures", "reference_cache")
# the offline unit scripts run after the checks of the output (each one check: exit code 0 = PASS)
UNIT_SCRIPTS = ("test_mechanisms.py", "test_tables_rules.py", "test_relations_rules.py", "test_validate_rules.py")


def _writable_again(func, path, _exc):
    """shutil.rmtree's error handler: a read-only file (Windows refuses to remove one) is made writable and removed."""
    os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
    func(path)


def remove_tree(path):
    """shutil.rmtree that also removes read-only files (on Windows a read-only file stops a plain rmtree)."""
    if sys.version_info >= (3, 12):
        shutil.rmtree(path, onexc=_writable_again)
    else:
        shutil.rmtree(path, onerror=_writable_again)


def fresh_cache(work, seed):
    """WORK/reference_cache_seedN: a fresh copy of tests/fixtures/reference_cache (the reference stage writes parquet
    files next to the GTF, so the fixture itself is never used in place); an earlier copy is removed first, read-only
    files included. None when the fixture is not there."""
    if not os.path.isdir(FIXTURES):
        return None
    dst = os.path.join(work, f"reference_cache_seed{seed}")
    if os.path.isdir(dst):
        remove_tree(dst)
    shutil.copytree(FIXTURES, dst)
    return dst


def unit_scripts():
    """Each offline unit script as one check (exit code 0 = PASS; the last lines of its output are the detail)."""
    for name in UNIT_SCRIPTS:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            check("unit", f"tests/{name}", lambda name=name: (False, f"tests/{name} is not in this code"))
            continue
        t0 = time.time()
        r = subprocess.run([sys.executable, path], cwd=REPO, capture_output=True, text=True, encoding="utf-8",
                           errors="replace")
        out = (r.stdout + r.stderr).strip().splitlines()
        fails = [ln.strip() for ln in out if ln.lstrip().startswith(("FAIL", "[FAIL]"))]
        tail = " | ".join(out[-2:])
        check("unit", f"tests/{name}", lambda r=r, t0=t0, fails=fails, tail=tail: (
            r.returncode == 0, f"exit code {r.returncode} in {time.time() - t0:.0f} s; {tail[-400:]}"
                               + (f"; failed: {' | '.join(fails[:4])[-600:]}" if fails else "")))


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
        cache = fresh_cache(a.workdir, a.seed)
        rc = run_pipeline(data, out, ("--redo",) + (("--reference-cache", cache) if cache else ()))
        check("run", "pipeline finishes", lambda: (rc == 0, f"exit code {rc}"))
    truth = json.load(open(os.path.join(data, "ground_truth.json"), encoding="utf-8"))
    from tests import checks                                # noqa: E402  (the per-stage checks)
    checks.run_all(out, data, truth, check)
    browser_checks(out, data)
    unit_scripts()
    n = {s: sum(r["status"] == s for r in RESULTS) for s in ("PASS", "WARN", "FAIL")}
    with open(os.path.join(a.workdir, "test_results.json"), "w", encoding="utf-8") as fh:
        json.dump({"counts": n, "results": RESULTS}, fh, indent=1)
    print(f"\n{n['PASS']} passed, {n['WARN']} warnings, {n['FAIL']} failed  "
          f"(details: {os.path.join(a.workdir, 'test_results.json')})")
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()

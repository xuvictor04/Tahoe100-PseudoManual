#!/usr/bin/env python3
"""pipeline_with_fixtures.py - the pipeline on the synthetic data with the offline reference fixtures.

    python tests/pipeline_with_fixtures.py --workdir W [--seed 0] [--from STAGE] [--to STAGE] [--checks]

A helper for working on one part of the pipeline (until tests/run_tests.py passes the fixtures itself):
1. Makes or reuses the synthetic data and the output folder exactly as tests/run_tests.py does (its ensure_data and
   fresh_out): W/data_seedN and W/out_seedN.
2. Copies tests/fixtures/reference_cache afresh to W/reference_cache_seedN: the ChEMBL records of the synthetic drugs
   (chembl_drugs.json) and the Ensembl r112 GTF cut to the synthetic genes, so the reference stage has drug
   annotations, mechanism classes and gene coordinates offline.
3. Runs `python -m tahoemap run --data D --out O --min-cells 10 --offline --dims 32 --truth D/ground_truth.json
   --reference-cache W/reference_cache_seedN`, with --redo unless --from is given, and with --from / --to.
4. --checks: runs every check of tests/checks.py (run_all, with run_tests.check) on the output and prints the counts of
   PASS, WARN and FAIL and every FAIL. The checks of stages that did not run (after --to) fail: read them as 'not
   run'. The exit code is 1 when the pipeline or a check fails.
"""

import argparse
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)
sys.path.insert(0, HERE)

from tests import run_tests as RT  # noqa: E402

FIXTURES = os.path.join(HERE, "fixtures", "reference_cache")
STAGES = ["build", "effects", "tensor", "reference", "tables", "embed", "relations", "graph", "direction",
          "validate", "vault", "map", "explorer"]
try:                                                  # the package's own order, when it can be imported
    from tahoemap.common import STAGES  # noqa: E402,F811
except Exception:  # noqa: BLE001
    pass


def fresh_cache(work, seed):
    """W/reference_cache_seedN: a fresh copy of tests/fixtures/reference_cache (the reference stage writes parquet
    files next to the GTF, so the fixtures themselves are never used in place)."""
    dst = os.path.join(work, f"reference_cache_seed{seed}")
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(FIXTURES, dst)
    return dst


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--from", dest="start", choices=STAGES, default=None)
    ap.add_argument("--to", dest="stop", choices=STAGES, default=None)
    ap.add_argument("--checks", action="store_true", help="run tests/checks.py on the output afterwards")
    a = ap.parse_args()
    work = os.path.abspath(a.workdir)
    os.makedirs(work, exist_ok=True)
    data, key, made = RT.ensure_data(work, a.seed, False)
    out = os.path.join(work, f"out_seed{a.seed}")
    had = os.path.exists(os.path.join(out, "stages"))
    RT.fresh_out(out, key, made)
    start = a.start
    if start and (made or not had or not os.path.exists(os.path.join(out, "stages"))):
        print(f"--from {start}: the output folder is new (or was made from other data), so every stage runs.",
              flush=True)
        start = None
    cache = fresh_cache(work, a.seed)
    extra = ["--reference-cache", cache]
    extra += ["--from", start] if start else ["--redo"]
    if a.stop:
        extra += ["--to", a.stop]
    rc = RT.run_pipeline(data, out, extra)
    RT.check("run", "pipeline finishes", lambda: (rc == 0, f"exit code {rc}"))
    if a.checks:
        with open(os.path.join(data, "ground_truth.json"), encoding="utf-8") as fh:
            truth = json.load(fh)
        from tests import checks                    # noqa: E402  (the per-stage checks)
        try:
            checks.run_all(out, data, truth, RT.check)
        except Exception as e:  # noqa: BLE001  (a stage that did not run: its files are missing)
            RT.check("run", "tests/checks.py run_all", lambda e=e: (False, f"{type(e).__name__}: {e}"))
    n = {s: sum(r["status"] == s for r in RT.RESULTS) for s in ("PASS", "WARN", "FAIL")}
    with open(os.path.join(work, "pipeline_with_fixtures_results.json"), "w", encoding="utf-8") as fh:
        json.dump({"counts": n, "results": RT.RESULTS}, fh, indent=1)
    print(f"\n{n['PASS']} passed, {n['WARN']} warnings, {n['FAIL']} failed"
          + (f" (the checks of stages after --to {a.stop} did not run: they fail)" if a.stop and a.checks else ""))
    for r in RT.RESULTS:
        if r["status"] == "FAIL":
            print(f"  FAIL {r['stage']}: {r['check']} -- {r['detail'][:600]}")
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()

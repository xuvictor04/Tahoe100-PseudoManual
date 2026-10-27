#!/usr/bin/env python3
"""Compare a run's MG53 tables with the ones committed in this repository (the last step of mg53_setup.sh).

    python3 mg53_p53/setup/compare_with_repo.py --out ~/Tahoe-100M/mg53_p53

Compared: every CSV of each step's tables/ folder (mg53_p53/<step>/tables, single_cell_all/adjusted_ATF3/tables), the
summary tables (mg53_p53/summary) and the idarubicin per-line tables (trim72_idarubicin/corrected vs
<out>/trim72_idarubicin). A table is 'identical' when its rows, columns and text match and every number agrees to
1e-6 (relative); 'close' when numbers differ by less than 1e-3 (relative; e.g. another numpy / BLAS); else 'differs'.
Folder paths inside text are compared by their last part only. Writes <out>/compare_with_repo.txt.
"""
import argparse
import glob
import os
import re
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
MG53 = os.path.dirname(HERE)
REPO = os.path.dirname(MG53)
PATH = re.compile(r"(?:[A-Za-z]:)?(?:[/\\][^\s;,()'\"/\\]+)+[/\\]([^\s;,()'\"/\\]+)")


def pairs(out):
    """(label, repo folder, run folder) for every table folder the repository holds."""
    for d in sorted(glob.glob(os.path.join(MG53, "**", "tables"), recursive=True)):
        rel = os.path.relpath(d, MG53)
        if "verify" in rel.split(os.sep):
            continue
        yield rel, d, os.path.join(out, rel)
    yield "summary", os.path.join(MG53, "summary"), os.path.join(out, "summary")
    yield "trim72_idarubicin", os.path.join(REPO, "trim72_idarubicin", "corrected"), os.path.join(out, "trim72_idarubicin")


def text(s):
    return s.fillna("").astype(str).map(lambda v: PATH.sub(r"\1", v))


def compare(a, b):
    x, y = pd.read_csv(a, low_memory=False), pd.read_csv(b, low_memory=False)
    if list(x.columns) != list(y.columns):
        return "differs", f"columns differ ({len(x.columns)} vs {len(y.columns)})"
    if len(x) != len(y):
        return "differs", f"rows {len(x)} (repository) vs {len(y)} (this run)"
    num = [c for c in x.columns if pd.api.types.is_numeric_dtype(x[c]) and pd.api.types.is_numeric_dtype(y[c])]
    txt = [c for c in x.columns if c not in num and not text(x[c]).equals(text(y[c]))]
    if txt:
        return "differs", "text differs in " + ", ".join(txt[:5])
    if not num:
        return "identical", ""
    u, v = x[num].to_numpy(float), y[num].to_numpy(float)
    nan = int((np.isnan(u) != np.isnan(v)).sum())
    if nan:
        return "differs", f"{nan} values missing in one run only"
    with np.errstate(invalid="ignore"):
        ok = np.isfinite(u) & np.isfinite(v)
        rel = np.abs(u - v)[ok] / np.maximum(np.maximum(np.abs(u), np.abs(v))[ok], 1e-12)
        inf = int(((u != v) & ~ok & ~np.isnan(u)).sum())
    worst = float(rel.max()) if rel.size else 0.0
    if inf:
        return "differs", f"{inf} infinite values differ"
    if worst <= 1e-6:
        return "identical", ""
    return ("close" if worst <= 1e-3 else "differs"), f"largest relative difference {worst:.2g}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="the run's output folder (run_mg53_p53.py --out; default "
                                                 "<data>/mg53_p53)")
    a = ap.parse_args()
    out = os.path.abspath(os.path.expanduser(a.out))
    lines, counts = [], {"identical": 0, "close": 0, "differs": 0, "missing": 0}
    for label, rd, od in pairs(out):
        files = sorted(os.path.basename(f) for f in glob.glob(os.path.join(rd, "*.csv")))
        res = {"identical": 0, "close": 0, "differs": 0, "missing": 0}
        notes = []
        for f in files:
            b = os.path.join(od, f)
            if not os.path.exists(b):
                res["missing"] += 1
                notes.append(f"  missing  {f}")
                continue
            try:
                verdict, why = compare(os.path.join(rd, f), b)
            except Exception as e:  # noqa: BLE001
                verdict, why = "differs", f"unreadable: {e!r}"
            res[verdict] += 1
            if verdict != "identical":
                notes.append(f"  {verdict:8s} {f}: {why}")
        for k in counts:
            counts[k] += res[k]
        lines.append(f"{label}: {len(files)} tables: " + ", ".join(f"{v} {k}" for k, v in res.items() if v))
        lines += notes
    total = sum(counts.values())
    head = (f"{total} tables compared with the repository ({REPO}): " + ", ".join(f"{v} {k}" for k, v in counts.items())
            + ("\nAll identical: this run reproduces the committed tables." if counts["identical"] == total else
               "\n'close' = numbers agree to 1e-3 (another numpy / BLAS version can do that); 'differs' and 'missing'"
               " need a look (the run log is <out>/run_mg53_p53.log)."))
    report = head + "\n\n" + "\n".join(lines) + "\n"
    with open(os.path.join(out, "compare_with_repo.txt"), "w", encoding="utf-8") as fh:
        fh.write(report)
    print(report)


if __name__ == "__main__":
    sys.exit(main())

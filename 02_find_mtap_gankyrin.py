#!/usr/bin/env python3
"""
Find everything in Tahoe-100M that mentions MTAP or Gankyrin (PSMD10), table by table.

    cd ~/Tahoe-100M
    python3 02_find_mtap_gankyrin.py           # or: python3 02_find_mtap_gankyrin.py /path/to/Tahoe-100M

Writes to ./mtap_search/:
  search_summary.txt                every table, its size, and how many rows mention MTAP / PSMD10 / Gankyrin
  <table>_hits.csv                  matching rows from each small table (gene, cell line, drug, sample metadata)
  pseudobulk_MTAP_PSMD10_raw.csv    every published DE test for the two genes (one row per drug x dose x
                                    cell line x plate). UNCORRECTED: the plate-DMSO and well-position artifacts
                                    are still in these numbers; use tahoe_mtap_gankyrin.py for corrected results.
The pseudobulk scan reads only one column of ~4 billion rows: a few minutes.
"""
import glob
import os
import re
import sys

import pandas as pd
import pyarrow.parquet as pq

data = sys.argv[1] if len(sys.argv) > 1 else "."
OUT = "mtap_search"
GENES = ("MTAP", "PSMD10")
PAT = re.compile(r"\b(MTAP|PSMD10|GANKYRIN)\b", re.I)


def is_output(path, root=os.path.abspath(data), _cache={}):
    """True for files inside a folder made by tahoe_mtap_gankyrin.py (it holds file_index.json)."""
    d = os.path.dirname(os.path.abspath(path))
    while d.startswith(root) and d not in _cache:
        if os.path.exists(os.path.join(d, "file_index.json")):
            _cache[d] = True
            break
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    return any(os.path.abspath(path).startswith(k + os.sep) for k, v in _cache.items() if v)


os.makedirs(OUT, exist_ok=True)
files = sorted(f for f in glob.glob(os.path.join(data, "**", "*.parquet"), recursive=True) if not is_output(f))
if not files:
    sys.exit(f"No parquet files found under {os.path.abspath(data)}")
info = {}
for f in files:
    pf = pq.ParquetFile(f)
    info[f] = (pf.schema_arrow, pf.metadata.num_rows)

# group sharded files into tables, e.g. ".../train-00012-of-00400.parquet" -> ".../train"
groups = {}
for f in files:
    key = re.sub(r"[-_]?\d{3,}[^/]*\.parquet$", "", os.path.relpath(f, data))
    key = re.sub(r"\.parquet$", "", key)
    groups.setdefault(key, []).append(f)

summary = [f"Parquet files: {len(files)}, tables: {len(groups)}", ""]
for key, fs in sorted(groups.items()):
    total = sum(info[f][1] for f in fs)
    schema = info[fs[0]][0]
    names = schema.names
    label = f"{key}  ({len(fs)} files, {total:,} rows)"
    outname = re.sub(r"\W+", "_", key).strip("_")

    if {"gene_name", "log2FoldChange"} <= set(names):          # pseudobulk differential expression
        import duckdb
        out = os.path.join(OUT, "pseudobulk_MTAP_PSMD10_raw.csv")
        flist = "[" + ",".join("'" + f.replace("'", "''") + "'" for f in fs) + "]"
        duckdb.sql(f"COPY (SELECT * FROM read_parquet({flist}) WHERE gene_name IN {GENES}) "
                   f"TO '{out}' (HEADER)")
        n = duckdb.sql(f"SELECT gene_name, count(*) FROM read_csv_auto('{out}') GROUP BY 1").fetchall()
        summary.append(f"{label}\n  -> DE tests written to {out}: " + ", ".join(f"{g} {c:,}" for g, c in n))
        continue
    if {"genes", "expressions"} <= set(names):                  # per-cell expression: too big to text-search
        summary.append(f"{label}\n  per-cell expression data (use tahoe_mtap_gankyrin.py to extract the genes)")
        continue
    if total > 200_000:
        summary.append(f"{label}\n  large table, not text-searched (columns: {names})")
        continue

    df = pd.concat([pd.read_parquet(f) for f in fs], ignore_index=True)
    hits = df[df.astype(str).apply(lambda s: s.str.contains(PAT)).any(axis=1)]
    line = f"{label}\n  -> {len(hits)} rows mention MTAP / PSMD10 / Gankyrin"
    if len(hits):
        out = os.path.join(OUT, f"{outname}_hits.csv")
        hits.to_csv(out, index=False)
        line += f", written to {out}"
    summary.append(line)

with open(os.path.join(OUT, "search_summary.txt"), "w") as fh:
    fh.write("\n".join(summary) + "\n")
print("\n".join(summary))

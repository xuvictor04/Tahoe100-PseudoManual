#!/usr/bin/env python3
"""
Write a readable preview of one Tahoe-100M expression parquet file.

    cd ~/Tahoe-100M
    python3 01_preview_parquet.py              # or: python3 01_preview_parquet.py /path/to/Tahoe-100M

Writes, in the current folder:
  tahoe_preview.txt  schema, row counts, and the top 50 genes (by name) of the first cell
  tahoe_preview.csv  100 cells: metadata, genes detected, total counts, top 10 genes by name
Reads only the first 100 rows, so it takes seconds.
"""
import glob
import os
import sys

import pandas as pd
import pyarrow.parquet as pq

data = sys.argv[1] if len(sys.argv) > 1 else "."


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


files = sorted(f for f in glob.glob(os.path.join(data, "**", "*.parquet"), recursive=True) if not is_output(f))
if not files:
    sys.exit(f"No parquet files found under {os.path.abspath(data)}")


def cols(f):
    return set(pq.read_schema(f).names)


expr = next((f for f in files if {"genes", "expressions"} <= cols(f)), None)
if expr is None:
    sys.exit("No expression file (with 'genes' and 'expressions' columns) found")
gene_cands = [f for f in files if "gene" in os.path.basename(f).lower()] or files
gmeta = next((f for f in gene_cands if {"token_id", "gene_symbol"} <= cols(f)), None)
if gmeta is None:
    gmeta = next((f for f in files if {"token_id", "gene_symbol"} <= cols(f)), None)

pf = pq.ParquetFile(expr)
df = next(pf.iter_batches(batch_size=100)).to_pandas()

id2sym = {}
if gmeta:
    g = pd.read_parquet(gmeta, columns=["token_id", "gene_symbol"])
    id2sym = dict(zip(g.token_id, g.gene_symbol))


def ranked(row):
    # skip the first entry (a marker token), then sort genes by count
    pairs = zip(row["genes"][1:], row["expressions"][1:])
    return sorted(pairs, key=lambda x: -x[1])


def top_str(row, n=10):
    return "; ".join(f"{id2sym.get(gid, gid)}:{int(c)}" for gid, c in ranked(row)[:n])


meta_cols = [c for c in df.columns if c not in ("genes", "expressions")]
out = df[meta_cols].copy()
out["n_genes_detected"] = df["genes"].apply(lambda x: len(x) - 1)
out["total_counts"] = df["expressions"].apply(lambda x: int(sum(x[1:])))
out["top10_genes"] = df.apply(top_str, axis=1)
out.to_csv("tahoe_preview.csv", index=False)

with open("tahoe_preview.txt", "w") as fh:
    fh.write(f"Parquet files in folder: {len(files)}\n")
    fh.write(f"Expression file:         {expr}\n")
    fh.write(f"Gene metadata file:      {gmeta}\n")
    fh.write(f"Rows in this file:       {pf.metadata.num_rows:,}\n")
    fh.write(f"Row groups:              {pf.metadata.num_row_groups}\n\n")
    fh.write("SCHEMA\n------\n" + str(pf.schema_arrow) + "\n\n")
    first = df.iloc[0]
    fh.write("FIRST CELL\n----------\n")
    for c in meta_cols:
        fh.write(f"{c:20s} {first[c]}\n")
    fh.write(f"{'n_genes_detected':20s} {len(first['genes']) - 1}\n\n")
    fh.write("Top 50 genes (symbol, raw count)\n")
    for gid, c in ranked(first)[:50]:
        fh.write(f"  {str(id2sym.get(gid, gid)):15s} {int(c)}\n")

print("Wrote tahoe_preview.txt and tahoe_preview.csv in", os.getcwd())

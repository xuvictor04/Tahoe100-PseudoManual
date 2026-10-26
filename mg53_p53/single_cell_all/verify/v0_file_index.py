"""Verifier: per cell file, which (sample, cell_line_id) groups it holds and how many cells (own code)."""
import glob, os, sys, time
import numpy as np, pandas as pd, pyarrow.parquet as pq
data = sys.argv[1]; out = sys.argv[2]
files = sorted(glob.glob(os.path.join(data, "gene_panel", "cells", "*.parquet")))
rows = []
t0 = time.time()
for fi, f in enumerate(files):
    t = pq.read_table(f, columns=["sample", "cell_line_id"]).to_pandas()
    c = t.groupby(["sample", "cell_line_id"], observed=True).size().reset_index(name="n")
    c["fi"] = fi
    rows.append(c)
    if fi % 500 == 0:
        print(fi, time.time() - t0, flush=True)
df = pd.concat(rows, ignore_index=True)
df["sample"] = df["sample"].astype(str); df["cell_line_id"] = df["cell_line_id"].astype(str)
df.to_parquet(out, index=False)
print("files", len(files), "cells", df["n"].sum(), "rows", len(df), time.time() - t0)

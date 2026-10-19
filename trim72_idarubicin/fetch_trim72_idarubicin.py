"""Pull TRIM72 rows for idarubicin from Tahoe-100M's pseudobulk DE table on Hugging Face,
reading only the parquet footers and the row groups whose drug statistics match."""
import sys, concurrent.futures as cf
import fsspec, pyarrow.parquet as pq, pandas as pd

BASE = "https://huggingface.co/datasets/tahoebio/Tahoe-100M/resolve/main/metadata/pseudobulk_differential_expression/"
N, DRUG, GENE = 1026, "Idarubicin (hydrochloride)", "TRIM72"
fs = fsspec.filesystem("https", block_size=1 << 20)

def scan(i):
    url = f"{BASE}train-{i:05d}-of-{N:05d}.parquet"
    for attempt in range(4):
        try:
            with fs.open(url, "rb") as fh:
                pf = pq.ParquetFile(fh)
                md = pf.metadata
                di = md.schema.to_arrow_schema().names.index("drug")
                rgs = [g for g in range(md.num_row_groups)
                       if (s := md.row_group(g).column(di).statistics) and s.min <= DRUG <= s.max]
                if not rgs:
                    return None
                t = pf.read_row_groups(rgs).to_pandas()
                return t[(t.drug == DRUG) & (t.gene_name == GENE)].assign(source_file=i)
        except Exception as e:
            err = e
    print(f"file {i} failed: {err}", file=sys.stderr)
    return None

out = []
with cf.ThreadPoolExecutor(16) as ex:
    for k, r in enumerate(ex.map(scan, range(N))):
        if r is not None and len(r):
            out.append(r)
        if k % 100 == 0:
            print(k, sum(map(len, out)), flush=True)
df = pd.concat(out) if out else pd.DataFrame()
df.to_csv(sys.argv[1], index=False)
print("rows:", len(df))

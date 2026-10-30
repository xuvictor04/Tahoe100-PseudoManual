#!/usr/bin/env python3
"""Any genes' rows from the export's gene store (all_genes/, or <export>/.cache/store when all_genes was left out),
as CSV (or Parquet), with the full per-profile column set of the export (cpm, log2cpm and composition_shift added
back). Needs only numpy, pandas and pyarrow; reads only the genes asked for (one Parquet row group per gene).

    python3 export_genes.py --export <data>/mg53_p53/export --genes TRIM72,FUS,ATF3 --out genes.csv
    python3 export_genes.py --export DIR --set upstream --level drugdose_line --out up.csv.gz
    python3 export_genes.py --export DIR --genes CDKN1A --level drugdose          # to the terminal

--level profile        one row per (gene, plate, well, drug, concentration, cell line), DMSO wells included (default)
        drugdose_line  per (gene, drug-dose, cell line): means over the drug-dose's used wells with a value
        drugdose       per (gene, drug-dose): the atlas's DD values and the uncorrected medians over lines
        baselines      per (gene, plate, cell line): the drug-median and pooled-DMSO baselines of u_drugmedian / u_dmso
--set upstream|downstream adds that folder's genes (its genes.csv). Gene names: atlas symbols or labels.
The columns are defined in <export>/README.md.
"""
import argparse
import gzip
import os
import sys

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

PROFILE_ORDER = ["gene", "plate", "well", "slot", "sample", "drug", "concentration_uM", "is_dmso", "well_used",
                 "drug_dose_row", "unreliable_plate", "cell_line_id", "cell_name", "tp53_group", "n_cells",
                 "umi_count", "total_umi", "cpm", "log2cpm", "usable", "expressed", "u_dmso", "u_drugmedian",
                 "composition_shift", "position_effect", "posunc", "r2", "correction_path"]


def store_dir(export):
    for d in (os.path.join(export, "all_genes"), os.path.join(export, ".cache", "store")):
        if os.path.exists(os.path.join(d, "genes.csv")):
            return d
    sys.exit(f"no gene store under {export} (all_genes/genes.csv or .cache/store/genes.csv): run the export step")


class Store:
    def __init__(self, sdir):
        self.d = sdir
        self.idx = pd.read_csv(os.path.join(sdir, "genes.csv"))
        self.by = {}
        for col in ("gene", "symbol"):
            for r in self.idx.itertuples():
                self.by.setdefault(str(getattr(r, col)), r)
        self.prof = pq.read_table(os.path.join(sdir, "profiles.parquet")).to_pandas()
        self._pf = {}

    def _file(self, rel):
        if rel not in self._pf:
            self._pf[rel] = pq.ParquetFile(os.path.join(self.d, rel))
        return self._pf[rel]

    def read(self, g, kind):
        r = self.by[g]
        rel = {"profile": r.file, "drugdose": r.drugdose_file, "baselines": r.baselines_file}[kind]
        return self._file(rel).read_row_group(int(r.row_group)).to_pandas()


NULL_TYPES = {"posunc": pa.bool_(), "DD_posunc": pa.bool_()}


def no_null_types(tb):
    """All-null columns (e.g. posunc of an extra gene) typed as the other genes' (bool), so that every gene's rows share
    one Parquet schema whichever gene comes first."""
    for i, f in enumerate(tb.schema):
        if pa.types.is_null(f.type):
            ty = NULL_TYPES.get(f.name, pa.string())
            tb = tb.set_column(i, pa.field(f.name, ty), pa.nulls(tb.num_rows, ty))
    return tb


def strs(df):
    for c in df.columns:
        if isinstance(df[c].dtype, pd.CategoricalDtype):
            df[c] = df[c].astype(str)
    return df


def profile_rows(st, g):
    """The export's (2) columns for one gene: the store's rows + the profile columns + cpm / log2cpm."""
    t = strs(st.read(g, "profile"))
    p = st.prof
    if len(t) != len(p):
        sys.exit(f"{g}: {len(t)} rows, profiles.parquet has {len(p)}: the store is inconsistent")
    for c in ("slot", "sample", "drug_dose_row", "unreliable_plate", "cell_name", "tp53_group", "composition_shift"):
        t[c] = p[c].astype(str).to_numpy() if isinstance(p[c].dtype, pd.CategoricalDtype) else p[c].to_numpy()
    cnt = t["umi_count"].to_numpy(np.float64)
    tot = t["total_umi"].to_numpy(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        t["cpm"] = np.where(tot > 0, cnt / tot * 1e6, np.nan)
        t["log2cpm"] = np.where(tot > 0, np.log2((cnt + 0.5) / (tot + 1.0) * 1e6), np.nan).astype(np.float32)
    t["correction_path"] = str(st.by[g].correction_path)
    return t[[c for c in PROFILE_ORDER if c in t.columns]]


def drugdose_line_rows(st, g):
    """Per (drug-dose, line): means over the used wells, sums over the used wells (as the export's per_drugdose_line
    tables): r2_mean, u_drugmedian_mean_r2wells, composition_shift_mean and position_effect_mean over the wells with an
    r2 value (n_wells_r2), u_drugmedian_mean over the wells with a u_drugmedian value (n_wells_u), u_dmso_mean over the
    wells with a u_dmso value (n_wells_u_dmso)."""
    t = profile_rows(st, g)
    for c in ("r2", "u_drugmedian", "u_dmso", "composition_shift", "position_effect"):
        t[c] = t[c].astype(np.float64)                         # means in float64, as the export's tables
    u = t[t["well_used"] & (t["drug_dose_row"] >= 0)].copy()
    r2w = u["r2"].notna()
    for c, nm in (("u_drugmedian", "_udm_r2"), ("composition_shift", "_cs_r2"), ("position_effect", "_pe_r2")):
        u[nm] = u[c].where(r2w)
    k = ["drug_dose_row", "drug", "concentration_uM", "cell_line_id", "cell_name", "tp53_group"]
    agg = u.groupby(k, sort=True, observed=True).agg(
        expressed=("expressed", "first"), n_wells_r2=("r2", "count"), r2_mean=("r2", "mean"),
        u_drugmedian_mean_r2wells=("_udm_r2", "mean"), composition_shift_mean=("_cs_r2", "mean"),
        position_effect_mean=("_pe_r2", "mean"), n_wells_u=("u_drugmedian", "count"),
        u_drugmedian_mean=("u_drugmedian", "mean"), n_wells_u_dmso=("u_dmso", "count"),
        u_dmso_mean=("u_dmso", "mean"),
        umi_count_sum=("umi_count", "sum"), total_umi_sum=("total_umi", "sum"), n_cells_sum=("n_cells", "sum"))
    agg = agg.reset_index()
    agg.insert(0, "gene", t["gene"].iloc[0] if len(t) else g)
    agg.insert(agg.columns.get_loc("r2_mean") + 1, "fold_change", 2.0 ** agg["r2_mean"])
    with np.errstate(divide="ignore", invalid="ignore"):
        agg["cpm_pooled"] = np.where(agg["total_umi_sum"] > 0, agg["umi_count_sum"] / agg["total_umi_sum"] * 1e6,
                                     np.nan)
    return agg


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--export", required=True, help="the export folder (<data>/mg53_p53/export)")
    ap.add_argument("--genes", default="", help="comma list of genes (symbols or labels)")
    ap.add_argument("--set", choices=["upstream", "downstream"], action="append", default=[],
                    help="add the genes of upstream/genes.csv or downstream/genes.csv (repeatable)")
    ap.add_argument("--level", choices=["profile", "drugdose_line", "drugdose", "baselines"], default="profile")
    ap.add_argument("--out", default="-", help="output file (.csv, .csv.gz or .parquet; default: the terminal)")
    a = ap.parse_args()
    st = Store(store_dir(os.path.abspath(a.export)))
    genes = [g.strip() for g in a.genes.split(",") if g.strip()]
    for s in a.set:
        p = os.path.join(a.export, s, "genes.csv")
        if not os.path.exists(p):
            sys.exit(f"{p} not found (that part of the export has not been written)")
        genes += pd.read_csv(p)["gene"].astype(str).tolist()
    genes = list(dict.fromkeys(genes))
    if not genes:
        sys.exit("name genes with --genes and / or --set")
    miss = [g for g in genes if g not in st.by]
    if miss:
        sys.exit(f"not in the gene store ({st.d}): {', '.join(miss[:20])}"
                 + (" (all_genes was left out: only the selected genes are stored)" if ".cache" in st.d else ""))
    pq_out = a.out.endswith(".parquet")
    fh = writer = None
    if a.out == "-":
        fh = sys.stdout
    elif not pq_out:
        fh = gzip.open(a.out + ".tmp", "wt", encoding="utf-8", newline="") if a.out.endswith(".gz") else \
            open(a.out + ".tmp", "w", encoding="utf-8", newline="")
    first = True
    try:
        for g in genes:                     # one gene at a time: memory stays at one gene's rows (~70k on real data)
            if a.level == "profile":
                t = profile_rows(st, g)
            elif a.level == "drugdose_line":
                t = drugdose_line_rows(st, g)
            else:
                t = strs(st.read(g, a.level))
            if pq_out:
                tb = no_null_types(pa.Table.from_pandas(t, preserve_index=False).replace_schema_metadata(None))
                if writer is None:
                    writer = pq.ParquetWriter(a.out + ".tmp", tb.schema, compression="zstd")
                writer.write_table(tb.cast(writer.schema), row_group_size=max(1, tb.num_rows))
            else:
                t.to_csv(fh, index=False, header=first, lineterminator="\n")
            first = False
    except BrokenPipeError:                 # the terminal output was cut (e.g. '| head'): stop quietly
        if a.out == "-":
            os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
            sys.exit(0)
        raise
    if writer is not None:
        writer.close()
    elif fh is not None and a.out != "-":
        fh.close()
    if a.out != "-":
        os.replace(a.out + ".tmp", a.out)
        print(f"{len(genes)} genes ({a.level}) -> {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()

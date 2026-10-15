#!/usr/bin/env python3
r"""
SUPERSEDED - kept only to reproduce the original, UNCORRECTED drug lists for comparison.

This ranks drugs straight from the published pseudobulk DE table. Its top hits turned out to be artifacts:
  - well position (every drug in well H1 looks like an MTAP inducer, every drug in D10 like a Gankyrin inducer)
  - plate 2's DMSO control (every drug on plate 2 looks like a Gankyrin inducer)
  - p-values that understate well-to-well noise
  - drugs tested on two plates counted twice
Use tahoe_mtap_gankyrin.py for corrected results (it also reports these uncorrected values side by side).

    python3 old_drug_effect_uncorrected.py MTAP mtap_old
    python3 old_drug_effect_uncorrected.py PSMD10 gankyrin_old
    C:\tahoe\.venv\Scripts\python.exe old_drug_effect_uncorrected.py MTAP mtap_old   # Windows (PowerShell)
"""
import glob
import os
import sys

import duckdb
import pyarrow.parquet as pq

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(0 if sys.argv[1:2] in (["-h"], ["--help"]) else 2)
GENE, OUT = sys.argv[1], sys.argv[2]
PADJ = 0.05      # significance cutoff
LFC = 0.5        # log2 fold change cutoff (0.5 ~ 1.4x, 1.0 = 2x)

os.makedirs(OUT, exist_ok=True)
files = [f for f in sorted(glob.glob("**/*.parquet", recursive=True))
         if {"gene_name", "log2FoldChange"} <= set(pq.read_schema(f).names)]
assert files, "No pseudobulk parquet files found - run this from the Tahoe-100M folder"
print(f"{GENE}: scanning {len(files)} pseudobulk files (a few minutes)...")

flist = "[" + ",".join("'" + f.replace("'", "''") + "'" for f in files) + "]"
con = duckdb.connect()
con.execute(f"CREATE TABLE de AS SELECT * FROM read_parquet({flist}) WHERE gene_name = '{GENE}'")
n = con.execute("SELECT count(*) FROM de").fetchone()[0]
assert n, f"No rows for {GENE} - check the gene symbol"
con.execute(f"COPY de TO '{OUT}/{GENE}_DE_all_tests.csv' (HEADER)")

con.execute(f"""
  CREATE TABLE by_dose AS
  SELECT drug, concentration, concentration_unit,
         count(*)                                   AS n_tests,
         count(DISTINCT Cell_ID_Cellosaur)          AS n_cell_lines,
         sum(CASE WHEN padj < {PADJ} AND log2FoldChange >  {LFC} THEN 1 ELSE 0 END) AS n_up,
         sum(CASE WHEN padj < {PADJ} AND log2FoldChange < -{LFC} THEN 1 ELSE 0 END) AS n_down,
         round(median(log2FoldChange), 3)           AS median_lfc,
         round(avg(log2FoldChange), 3)              AS mean_lfc,
         round(max(log2FoldChange), 3)              AS max_lfc,
         round(median(baseMean), 1)                 AS median_baseMean
  FROM de WHERE NOT isnan(log2FoldChange)
  GROUP BY drug, concentration, concentration_unit
""")
con.execute("ALTER TABLE by_dose ADD COLUMN frac_up DOUBLE")
con.execute("UPDATE by_dose SET frac_up = round(n_up / n_tests, 3)")
con.execute(f"COPY (SELECT * FROM by_dose ORDER BY n_up DESC, median_lfc DESC) "
            f"TO '{OUT}/{GENE}_by_drug_and_dose.csv' (HEADER)")
con.execute(f"""
  COPY (
    SELECT * FROM by_dose
    QUALIFY row_number() OVER (PARTITION BY drug ORDER BY n_up DESC, median_lfc DESC) = 1
    ORDER BY n_up DESC, median_lfc DESC
  ) TO '{OUT}/{GENE}_top_drugs.csv' (HEADER)
""")
print(f"\nTop 15 drugs increasing {GENE} ({n:,} tests) - UNCORRECTED:")
print(con.execute(f"""SELECT drug, concentration, n_cell_lines, n_up, frac_up, median_lfc, max_lfc
                      FROM read_csv_auto('{OUT}/{GENE}_top_drugs.csv') LIMIT 15""").fetchdf().to_string(index=False))
print(f"Files written to ./{OUT}/")

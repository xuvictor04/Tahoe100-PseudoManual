# Synthetic Tahoe-100M data and smoke tests

`tests/` holds a generator for a small synthetic Tahoe-100M download with known, planted effects, and a smoke test
that runs every script of this repo on it and checks that the planted effects come back out.

| File | What it is |
|---|---|
| `make_synthetic_tahoe.py` | Writes the synthetic download (about 250,000 cells, 250 MB) plus `ground_truth.json`. |
| `run_smoke.py` | Generates the data once, runs every script on it, checks the results: PASS/FAIL per check. |
| `tahoe_meta_snapshot.py` | The real metadata rows the generator copies (18 cell lines, 94 drugs, 244 gene symbols). |

You need Python 3.10+ with numpy, pandas, pyarrow and duckdb, the same packages the scripts use. For the atlas
`check` step, `claude-agent-sdk` is optional. No API key is used: the agents step runs with `--dry-run`, and
the API-key variables are removed from the environment of every command the smoke test starts.

## Run the smoke test

Linux / macOS, from the repo folder:
```bash
python3 tests/run_smoke.py                         # data + all stages; outputs in /tmp/tahoe_smoke
python3 tests/run_smoke.py --workdir ~/tahoe_smoke --only mtap,atlas
python3 tests/run_smoke.py --regen                 # force new data (otherwise reused)
```
Windows (PowerShell), from the repo folder:
```powershell
C:\tahoe\.venv\Scripts\python.exe tests\run_smoke.py --workdir C:\tahoe\smoke
C:\tahoe\.venv\Scripts\python.exe tests\run_smoke.py --workdir C:\tahoe\smoke --only atlas
```
Options:
- `--workdir DIR`: where the data and outputs go. The default is `$TAHOE_SMOKE_DIR`, or else
  `<system temp>/tahoe_smoke`.
- `--only small,mtap,atlas,panel`: run only these stages.
- `--workers 2`: passed to the scripts.
- `--seed N`: generator seed. The data are regenerated when the seed changes.
- `--regen`: regenerate the data.

Exit code 0 means no check failed, and 1 means at least one check failed. A WARN line is reported but does not
fail the run: it marks a known weakness whose outcome depends on chance in these small data.

What ends up in DIR:

| Path | Contents |
|---|---|
| `synthetic_tahoe/` | The generated download. It is regenerated automatically when `make_synthetic_tahoe.py` changes, because its sha1 is stored in `ground_truth.json`. |
| `small/` | Outputs of `01_preview_parquet.py`, `02_find_mtap_gankyrin.py` and `old_drug_effect_uncorrected.py`. |
| `mtap_gankyrin/` | Output of `tahoe_mtap_gankyrin.py all` and `coreg`. |
| `atlas/` | Output of `tahoe_atlas.py` `check`, `compute`, `lookup` x4, `agents --dry-run` and `bundle`. |
| `gene_panel/` | Output of `tahoe_gene_panel.py`, once that script exists. Until then the `panel` stage is skipped. |
| `logs/<stage>_<step>.log` | The full output of every command. |
| `smoke_results.json` | Every check (stage, name, PASS/FAIL/WARN/SKIP, detail) and every command (argv, exit code, seconds, log). |

Each stage starts from an empty output folder. The scripts run from `DIR/scratch` with the Python that runs
`run_smoke.py`. There is one exception: `old_drug_effect_uncorrected.py` has no data argument and globs
`**/*.parquet` from its working folder, so it runs inside `synthetic_tahoe/` and writes to an absolute path in
`small/`.

**Runtime** (4 CPUs, `--workers 2`):

| Step | Time |
|---|---|
| Generating the data | ~45 s, < 1 GB RAM |
| small | ~3 s |
| mtap | ~11 s |
| atlas | ~25 s |
| Whole run | ~1.5 min |

**Adding a stage:** write one function decorated with `@stage("name")` in `run_smoke.py`, using
`ctx.run_ok(...)` for commands and `ctx.check(name, fn)` for checks. `stage_panel` is the template for the future
`tahoe_gene_panel.py` (`extract` and `analyze` into `DIR/gene_panel`). Its ground-truth checks can read `ctx.gt`.

## Generate the data only

```bash
python3 tests/make_synthetic_tahoe.py /path/to/synth [--seed 0] [--plates 6] [--lines 18] [--cells 35] [--genes 1200]
```
```powershell
C:\tahoe\.venv\Scripts\python.exe tests\make_synthetic_tahoe.py C:\tahoe\synth
```
The scripts then run on it as on a real download, for example
`python3 tahoe_atlas.py compute --data /path/to/synth --out /path/to/atlas`.
The output is deterministic for a given seed.

## Layout: like a real download

- `data/train-00000-of-000NN.parquet`: one plate per file, about 8,000 cells per file, rows grouped by sample
  (sublibrary, then well, then barcode). A plate spans several files, and a sample can continue into the next file.
- `metadata/{cell_line,drug,gene,sample}_metadata.parquet`
- `metadata/pseudobulk_differential_expression/train-00000-of-00001.parquet`
- `ground_truth.json`

Every table has the real column names and dtypes. They were checked against the real files with
`pyarrow.Schema.equals`:
- `genes` is `list<element: int64>`, starting with marker token 1. `expressions` is `list<element: float>` (float32
  counts), starting with -2.0. Genes are sorted.
- `pubchem_cid` is a string (`"2554.0"`) in the expression files and a double in drug_metadata.
- Barcodes look like `WW_RRR_RRR-lib_NNNN`, where WW is the sample's well 01..96, numbered row-major. Barcodes are
  unique within a well, two sublibraries per plate.
- Samples are `smp_1495`... (plate1 starts at 1495, as in the real data). Plates are `plate1`...
- DMSO is `DMSO_TF`, in H11 and H12 of every plate.
- `drugname_drugconc` looks like `[('Name', 0.5, 'uM')]`. Erdafitinib keeps its real trailing space.
- The DE table has float32 statistics, plate `'1'`..`'6'`, int64 cell counts, and `Cell_Name_Vevo`.

The design:
- 6 plates of 96 wells. Plates 1-2 are at 0.05 uM, 3-4 at 0.5 uM and 5-6 at 5 uM.
- 94 drugs plus 2 DMSO wells per plate. Every drug sits on every plate, at a different position each time, so each
  drug-dose sits on 2 plates at 2 positions.
- 18 real cell lines are pooled in every well, at different abundances: about 10-40 cells per line per well
  (average ~25).
- Library size is log-normal, about 1,000 UMIs per cell.
- Each cell has a G1, S or G2/M state.
- Counts are Poisson. Each cell also gets 8-14% of its counts from the well-average profile (ambient RNA), so a
  deleted gene reads about 9% of the median line.
- Every gene has log-normal well noise: sigma 0.08 shared by the well, 0.05 per line.
- There are plate offsets.
- Effects are planted at the top dose. 0.5 uM gets 40% of the log effect and 0.05 uM gets 5%.

The gene universe holds 1,200 genes:
- 244 named genes with their real symbols and Ensembl ids:
  - the 37 panel genes, the anchors MTAP/PSMD10/CDKN2A/CDKN2B and the context gene sets of the gene-panel spec;
  - the S, G2/M and proteasome genes of `tahoe_mtap_gankyrin.py`.
- `SYNTH0001`... filler genes (Ensembl ids `ENSG9...`).
- Token ids are compact: 3...1202.

The levels of the named genes keep their real order (FTL/FTH1/BAX high, NLRP3/CASP5/AIM2 about 1 CPM, TRIM72
zero), but their range is compressed. The reason is size: a synthetic profile of ~25 cells holds ~25k UMIs, where
a real one has ~2.8M, so genes need more counts per million to be measurable. For the same reason the filler levels
are kept narrow. A gene below ~100 CPM in these data sits at the pseudocount floor, where a real gene above 2 CPM
would not.

## What is planted (everything is listed in `ground_truth.json`)

| Planted | Detail |
|---|---|
| Doxorubicin, Topotecan, 5-FU | P53 activity genes 2x (CDKN1A 3x, MDM2 2.5x) in TP53-wild-type lines (no TP53 row in cell_line_metadata), 1.1x in TP53-altered lines. Cell numbers x0.6 (WT) and x0.9 (altered). Doxorubicin 5 uM: all cells ~0.4x. |
| Dimethyl fumarate | NRF2 core 2x, HMOX1 4x, SLC7A11 2.5x. |
| Auranofin | NRF2 core 1.8x, HMOX1 3x, SLC7A11 2x, CHAC1 2.5x, ISR 1.8x. |
| Artesunate | PTGS2 2x, CHAC1 2x, TFRC 1.5x, no ISR change. High-ACSL4 lines are depleted more (same -1.8 slope). |
| Ciclopirox | TFRC 2.5x, FTH1/FTL 0.7x, NCOA4 1.3x. |
| Decitabine, 5-Azacytidine | IFN genes 1.6x. GSDME about 4x in the 5 GSDME-silenced lines. |
| Bortezomib | Proteasome subunits 1.8x, heat shock 3x, HMOX1 3x, ISR 2x, CHAC1 2x. 5 uM: cells 0.3x, UMIs/cell 0.6x. |
| Paclitaxel | G2/M genes 1.8x. |
| Pemetrexed | MTAP-null lines (A549, MCF-7, PANC-1, MIA PaCa-2, BxPC-3) depleted: 0.5x at 5 uM, 0.75x at 0.5 uM. |
| Ixazomib | High-PSMD10 lines depleted more (log2 cells -1.8 x the line's PSMD10 rank fraction at 5 uM). |
| Imiquimod (maleate) | NFKB genes 2x, IL1B 3x in the 2 IL1B-expressing lines, CASP4 1.5x. |
| Rimonabant | NAPEPLD 1.6x. |
| Dinaciclib | UMIs/cell 0.65x (the spec says ~0.7x; 0.65x clears the scripts' 0.707x flag threshold), MDM2 0.5x. |
| Celecoxib | PTGS2 1.5x. |
| Well positions (every drug well) | H1: MTAP 1.6x. D10: PSMD10 1.5x. A12: CHAC1 1.5x. |
| Plate 2 DMSO wells | PSMD10 0.6x, CDKN1A 0.65x. The spec says 0.7x/0.75x; it was made stronger because an offset estimated from 2 DMSO wells of ~25-cell profiles has ~0.11 log2 noise. |
| Failed well | Allantoin 0.5 uM on plate 3 recovered 3% of the usual cells. |
| Expression facts | TRIM72 0 everywhere. NLRP3/CASP5/AIM2 about 1 CPM. IL1B in 2 lines. CASP1 absent in 6 lines. GSDME silenced in 5 lines. MTAP 0 in the MTAP-null lines. CDKN2A/CDKN2B 0 in the lines with deletion rows. TP53 0 in NCI-H1299 and Calu-1. |
| Extra, not in the panel spec | HDAC inhibitors share a SYNTH signature; Carbamazepine, labelled HDAC, is the inert outlier. mTOR inhibitors lower a SYNTH ribosome set and proteasome subunits (0.85x). Glucocorticoids and statins share SYNTH sets. CDK4/6 inhibitors put S/G2M genes at 0.6x. 22 other drugs have private SYNTH signatures. PSMD10 is 1.25x in G2/M cells. |

`ground_truth.json` also holds the full plate layout (sample, plate, well, drug, dose) and the measured level of
the key genes in every line (`measured_expression`).

## What the smoke test checks

| Stage | Checks |
|---|---|
| small | All three scripts exit 0 and write their files. The raw DE extract has both genes. The uncorrected MTAP lists show the H1 artifact. |
| mtap | H1 is in the top 3 MTAP positions and D10 in the top 3 PSMD10 positions. Plate 2 has the top PSMD10 DMSO offset. The MTAP-null calls equal the planted lines. Pemetrexed is in the top 3 MTAP-null-selective drugs. Ixazomib is in the top 3 "high-Gankyrin lines depleted more". The failed well is excluded. summary.txt has sections 1-9. Bortezomib 5 uM is flagged toxic with a transcription drop. Bortezomib leads the PROTEASOME module. The plate-2 DMSO offset inflates the uncorrected PSMD10 values and not the corrected ones. PSMD10 is higher in G2/M cells. coreg runs and fills its tables. |
| atlas | `check` passes. `compute` runs and no angle logs an error. Every angle has brief.md, including focus_MTAP and focus_PSMD10. H1 and D10 carry the largest single-gene position shifts (top 3). MTAP/PSMD10/CHAC1 are the top genes at H1/D10/A12 and map back to them in position_sensitive_genes. H1 and D10 are in the first 10 rows of position_effects.csv: WARN only, because that file is sorted by the number of shifted genes, and chance alone gives each position 0-6 of them. Dimethyl fumarate is the top HMOX1 inducer. Bortezomib 5 uM is toxic. "MTAP not expressed" equals the planted lines, with Pemetrexed in its top 3. The failed well is excluded. Plate 2 DMSO reads low for PSMD10/CDKN1A. Dinaciclib shows a transcription drop. Paclitaxel shows a G2/M build-up. Ciclopirox/TFRC, Rimonabant/NAPEPLD, Bortezomib/HSPA1A and DNMT inhibitors/ISG15 each come out as top inducers. Ixazomib leads focus_PSMD10/level_vs_growth. Pemetrexed leads focus_MTAP/loss_selective_drugs. The MTAP expression-loss group equals the planted lines. ACSL4 and PSMD10 are biomarkers for Artesunate and Ixazomib. The HDAC class is coherent with Carbamazepine as its outlier. The look-ups print the expected cards. `agents --dry-run` writes a prompt per angle. atlas_bundle.zip lists `computation/` files. |
| panel | Skipped until `tahoe_gene_panel.py` exists. |

Rankings are checked as top-k (k = 2-3, or 10 for long lists), never as exact values.

## Known limits of the synthetic data

| Synthetic data | Real data |
|---|---|
| 18 lines, ~25 cells per line per well | ~50 lines, ~1,400 cells per line per well |
| 1,200 genes | 62,710 genes |
| Naive pseudobulk DE table (vs pooled plate DMSO; not DESeq2) | DESeq2 table |

- Counting noise per profile is far higher than in real data, so genes below ~100 CPM behave like zero-count genes.
- The DE table only has to be plausible for the scripts that read it.
- In expression files the DMSO rows have empty `moa-fine`, `canonical_smiles` and `pubchem_cid`. This is an
  assumption: DMSO_TF is not in drug_metadata, so a join leaves them empty.
- Doses act only through the fixed 5% / 40% / 100% scaling of the log effect.

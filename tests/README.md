# Synthetic Tahoe-100M data and smoke tests

`tests/` holds a generator for a small synthetic Tahoe-100M download with known, planted effects, and a smoke test
that runs every script of this repo on it and checks that the planted effects come back out.

| File | What it is |
|---|---|
| `make_synthetic_tahoe.py` | Writes the synthetic download (about 290,000 cells, 290 MB) plus `ground_truth.json`. |
| `run_smoke.py` | Generates the data once, runs every script on it, checks the results: PASS/FAIL per check. |
| `tahoe_meta_snapshot.py` | The real metadata rows the generator copies (18 cell lines, 94 drugs, 244 gene symbols). |

You need Python 3.10+ with numpy, pandas, pyarrow and duckdb, the same packages the scripts use. For the atlas
`check` step, `claude-agent-sdk` is optional. No API key is used: the agents step runs with `--dry-run`, and
the API-key variables are removed from the environment of every command the smoke test starts.

## Run the smoke test

Linux / macOS, from the repo folder:
```bash
python3 tests/run_smoke.py                         # data + all stages; outputs in /tmp/tahoe_smoke
python3 tests/run_smoke.py --workdir ~/tahoe_smoke --only atlas,mtap
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
- `--only small,atlas,mtap,panel,wrapper`: run only these stages (they always run in this order).
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
| `synthetic_tahoe/atlas/` | Output of `tahoe_atlas.py` `check`, `compute --min-cells 10`, `lookup` x4, `agents --dry-run` and `bundle`. It sits in `<data>/atlas`, as on a real download, because `tahoe_mtap_gankyrin.py` and the gene panel look for the atlas there (composition shifts, plate factors, 'wells disagree'). It is a script output folder (`file_index.json`), so no script reads it as data. |
| `mtap_gankyrin/` | Output of `tahoe_mtap_gankyrin.py all` and `coreg` (after the atlas: it uses the atlas's composition shifts). |
| `gene_panel/` | Output of `tahoe_gene_panel.py` `check`, `all` (extract + analyze + bundle; it reads `mtap_gankyrin/` as the earlier run and the atlas), `agents --dry-run`, `analyze` once more with `--prior none` (the no-prior cross-links) and `bundle`. |
| `scratch/older_tahoe_mtap_gankyrin/` | A copy of `tahoe_gene_panel.py` next to a `tahoe_mtap_gankyrin.py` with `METHOD_VERSION = 2`: the panel must refuse it. |
| `wrapper_state/` | The `wrapper` stage: `tahoe_status.py status`, `next` and `facts` on the outputs above (both runs done, `Next: tahoe bundle`, every line within 80 columns; then once with the atlas's and once with the panel's method stamp set to 2: 'done, but outdated', `Next: tahoe run`; the stamps are restored), then `bash -n tahoe` and `tahoe help` (all commands, 80 columns; skipped without bash). It needs the atlas and panel stages. |
| `logs/<stage>_<step>.log` | The full output of every command. |
| `smoke_results.json` | Every check (stage, name, PASS/FAIL/WARN/SKIP, detail) and every command (argv, exit code, seconds, log). |

Each stage starts from an empty output folder. The scripts run from `DIR/scratch` with the Python that runs
`run_smoke.py`. There is one exception: `old_drug_effect_uncorrected.py` has no data argument and globs
`**/*.parquet` from its working folder, so it runs inside `synthetic_tahoe/` and writes to an absolute path in
`small/`.

**Runtime** (4 CPUs, `--workers 2`; the first column on an idle machine, before plate13 was added; the second
measured with method v3 (its traps in the data and its code) on a 4-CPU VM, where the version before v3 took
72 / 3 / 21 / 56 / 195 / 1 s, 347 s in all):

| Step | Time (earlier, idle) | Time (method v3) |
|---|---|---|
| Generating the data | ~45 s, < 1 GB RAM | ~75 s, < 1 GB RAM |
| small | ~3 s | ~4 s |
| atlas | ~30 s | ~43 s |
| mtap | ~11 s | ~19 s |
| panel | ~100 s (two analyze runs) | ~230 s |
| wrapper | ~1 s | ~2 s |
| Whole run | ~3 min | ~5 min with the data reused, ~6 min with new data |

**Adding a stage:** write one function decorated with `@stage("name")` in `run_smoke.py`, using
`ctx.run_ok(...)` for commands and `ctx.check(name, fn)` for checks; ground-truth checks read `ctx.gt` (see
`stage_panel`). The `panel` stage needs the `mtap` stage's output for its reproduction checks: with
`--only panel` it reuses `DIR/mtap_gankyrin` from an earlier run, and skips those checks when it is missing. The
same holds for the atlas: the panel's atlas comparisons (MTAP/PSMD10 agreement, imported plate factors and
composition shifts) are skipped without a method-v3 atlas in `DIR/synthetic_tahoe/atlas`. The method-v3 checks
(named `v3: ...`) live in the functions `v3_atlas`, `v3_mtap`, `v3_panel`, `v3_noprior`, `v3_panel_guard` and
`v3_outdated`; they are skipped (SKIP) on data from a generator without the `method_v3` ground truth.

## Generate the data only

```bash
python3 tests/make_synthetic_tahoe.py /path/to/synth [--seed 0] [--plates 6] [--lines 18] [--cells 35] [--genes 1200]
```
```powershell
C:\tahoe\.venv\Scripts\python.exe tests\make_synthetic_tahoe.py C:\tahoe\synth
```
The scripts then run on it as on a real download, for example
`python3 tahoe_atlas.py compute --data /path/to/synth --out /path/to/atlas`.
The output is deterministic for a given seed. `--plates` (3-12) sets the regular plates; plate13 always comes on top.

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
- Samples are `smp_1495`... (plate1 starts at 1495, as in the real data). Plates are `plate1`... and `plate13`.
- DMSO is `DMSO_TF`, in H11 and H12 of every plate except plate13 (B11 and B12, as in the real data).
- `drugname_drugconc` looks like `[('Name', 0.5, 'uM')]`. Erdafitinib keeps its real trailing space.
- The DE table has float32 statistics, plate `'1'`..`'6'` and `'13'`, int64 cell counts, and `Cell_Name_Vevo`.

The design:
- 6 regular plates of 96 wells. Plates 1-2 are at 0.05 uM, 3-4 at 0.5 uM and 5-6 at 5 uM. On top, `plate13`: a
  mixed-dose plate (dose by row: A, B, E, H 0.05 uM; D, G 0.5 uM; C, F 5 uM), as the real plate 13.
- 94 drugs plus 2 DMSO wells per plate. Every drug sits on every regular plate, at a different position each time,
  so each drug-dose sits on 2 plates at 2 positions, with these exceptions (the method-v3 traps, below): the
  reference drug Bestatin sits at 0.05 uM in H10 of every regular plate (6 wells, one position) and its 0.5 and 5 uM
  only on plate13; Dinaciclib and Pyridoxine take turns in B11 and B12 (one on odd plates, the other on even ones);
  the 12 inert drugs of plate5 row E have their 5 uM dose on plate5 only, and on plate6 their positions hold a
  second well of 12 other inert drugs. plate13 holds the 22 private-signature drugs at all three doses, the
  reference drug's 0.5 and 5 uM and inert fillers, so 92 drug-doses get a third well there.
- 18 real cell lines are pooled in every well, at different abundances: about 10-40 cells per line per well
  (average ~25).
- Library size is log-normal, about 1,000 UMIs per cell.
- Each cell has a G1, S or G2/M state.
- Counts are Poisson. Each cell also gets 8-14% of its counts from the well-average profile (ambient RNA), so a
  deleted gene reads about 9% of the median line.
- Every gene has log-normal well noise: sigma 0.08 shared by the well, 0.05 per line (3x both on plate6).
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
| Decitabine, 5-Azacytidine | IFN genes 1.6x. GSDME in the 5 GSDME-silenced lines about 6x (Decitabine, the more potent DNMT inhibitor) and 3.5x (5-Azacytidine). |
| Bortezomib | Proteasome subunits 1.8x, heat shock 3x, HMOX1 3x, ISR 2x, CHAC1 2x. 5 uM: cells 0.3x, UMIs/cell 0.6x. |
| Paclitaxel | G2/M genes 1.8x. |
| Pemetrexed | MTAP-null lines (A549, MCF-7, PANC-1, MIA PaCa-2, BxPC-3) depleted: 0.5x at 5 uM, 0.75x at 0.5 uM. |
| Ixazomib | High-PSMD10 lines depleted more (log2 cells -1.8 x the line's PSMD10 rank fraction at 5 uM). |
| Imiquimod (maleate) | NFKB genes 2x, IL1B 3x in the 2 IL1B-expressing lines, CASP4 1.5x. |
| Rimonabant | NAPEPLD 2x (the spec says 1.6x; with one of its two 5 uM wells on the noisy plate6, 1.6x on a gene with ~0.17 log2 well noise was within chance of the top noise drug-doses). |
| Dinaciclib | UMIs/cell 0.65x (the spec says ~0.7x; 0.65x clears the scripts' 0.707x flag threshold), MDM2 0.5x; for the co-location trap also TFRC 0.35x and 24 SYNTH genes (14 at 0.35x, 10 at 2.5x). |
| Celecoxib | PTGS2 1.5x. |
| Well positions (every drug well) | H1: MTAP 1.6x. D10: PSMD10 1.5x. A12: CHAC1 1.5x. |
| Plate 2 DMSO wells | PSMD10 0.6x, CDKN1A 0.65x. The spec says 0.7x/0.75x; it was made stronger because an offset estimated from 2 DMSO wells of ~25-cell profiles has ~0.11 log2 noise. |
| Failed well | Allantoin 0.5 uM on plate 3 recovered 3% of the usual cells. |
| Expression facts | TRIM72 0 everywhere. NLRP3/CASP5/AIM2 about 1 CPM. IL1B in 2 lines. CASP1 absent in 6 lines. GSDME silenced in 5 lines: they keep 8% of the median line, so in DMSO they read ~2x the ambient-RNA floor (silenced, not deleted; method v3 calls a rise in lines that read ambient only 'not interpretable'). MTAP 0 in the MTAP-null lines. CDKN2A/CDKN2B 0 in the lines with deletion rows. TP53 0 in NCI-H1299 and Calu-1. |
| Extra, not in the panel spec | HDAC inhibitors share a SYNTH signature; Carbamazepine, labelled HDAC, is the inert outlier. mTOR inhibitors lower a SYNTH ribosome set and proteasome subunits (0.85x). Glucocorticoids and statins share SYNTH sets. CDK4/6 inhibitors put S/G2M genes at 0.6x. 22 other drugs have private SYNTH signatures. PSMD10 is 1.25x in G2/M cells. |

The traps that method v3 fixes, as found in the real data (`ground_truth.json` `method_v3`, with what v3 should
make of each):

| Trap (spec 10) | Planted | v3 should give |
|---|---|---|
| a. noisy plate | plate6 (5 uM) has 3x the per-well expression noise, so its W2 spread is ~2x that of its peer plate5 (counting noise stays). | `plate_scale.csv` factor ~2 for plate6, 1 for plate5 (never narrowed); the 5 uM drug-doses `plate_scale` ~1.5 and 'noisy plate (z scaled)'; inert drugs no longer gain significant genes at 5 uM; the planted 5 uM effects still found. |
| b. unreliable plate | `plate13`: mixed doses by row, DMSO in B11/B12; every drug well carries another drug's planted biology (labels shuffled; `layout` entries have a `biology` key). Bestatin 0.5 and 5 uM exist only there. | Left out of every drug-dose that has a reliable well (n_wells, mean W2, Stouffer z); Bestatin 0.5 / 5 'unreliable plate only'; replicate pairs with plate13 agree less than the others (`pair_type` 'unreliable plate'). |
| c. co-location | Dinaciclib (strong) and Pyridoxine (inert) take turns in B11/B12 on every regular plate: each one's only position donors are the other's three doses. | Before v3, Pyridoxine reads minus Dinaciclib's 0.5 uM effect (TFRC ~1.5x up, the SYNTH genes mirrored, at every dose). v3: ~0, 'position correction uncertain' (`DD_posunc.npy`); Dinaciclib's own effect kept. |
| c2. co-location, clean donors | (No well moves.) At a well position where a 5 uM plate and a lower-dose plate hold inert fillers, the 5 uM filler becomes a strong drug (its own 22 SYNTH genes, 0.3x / 3x; put on its wells' counts from a separate random stream, so the rest of the data is the draw before) and the other is the test drug: its well has 6 donors of 6 drugs, one of them the strong 5 uM well (as sodium salicylate next to dinaciclib in the real data). | The clean-donor pass drops the strong well and corrects the test well with the median of the other donors (recomputed exactly from W1 and the pass-1 z): ~0 on the strong drug's genes, NOT 'position correction uncertain'. |
| d. uncorrectable position | Bestatin 0.05 uM in H10 of every regular plate, whatever the plate's dose (as Adagrasib in the real data); one plate13 drug there. | 'position not correctable', `position_not_correctable`; the 0.05 uM well on a 0.5 / 5 uM plate joins that plate's group for the plate factor. |
| e. composition shift | 8-Hydroxyquinoline 5 uM raises the 4 most abundant SYNTH genes 30x: every other gene reads ~0.59 log2 lower in CPM. | `composition_shift.parquet`, `composition_shift_log2` ~ -0.59, 'composition shift'; its other genes ~0 after the normalisation; the panel and `tahoe_mtap_gankyrin.py` use the atlas's shifts. |
| f. cell loss | plate5 row E lost 2/3 of its cells (-1.6 log2: a well's cell number varies by ~0.22 log2, so the spec's ~60% would leave some drug-doses above the -1 cut); its 12 inert drugs have their 5 uM dose there only (one well each, as on the real plates 1-3), and their plate6 positions hold second wells of 12 other inert drugs (`same_plate_replicates`: pair_type 'same plate'). Ranolazine 0.05 uM 0.35x cells in both wells, its higher doses fine. | 'low cells (technical?)' (+ 'plate-row cell shift' for the row), not 'toxic'; Bortezomib 5 and Doxorubicin 5 stay 'toxic'. |
| g. no earlier run | (smoke test) the panel's second `analyze` runs with `--prior none`. | crosslinks brief without `prior/` or 'reproducibility vs the earlier run'; summary.txt "this run's MTAP / PSMD10 lists", no 'two runs'. |

`ground_truth.json` also holds the full plate layout (sample, plate, well, drug, dose) and the measured level of
the key genes in every line (`measured_expression`).

## What the smoke test checks

| Stage | Checks |
|---|---|
| small | All three scripts exit 0 and write their files. The raw DE extract has both genes. The uncorrected MTAP lists show the H1 artifact. |
| atlas | `check` passes. `compute` runs and no angle logs an error. Every angle has brief.md, including focus_MTAP and focus_PSMD10. H1 and D10 carry the largest single-gene position shifts (top 3 of the positions with >= 3 drug wells: plate13's drug wells in H11/H12, DMSO positions elsewhere, are one drug each, not a position artifact). MTAP/PSMD10/CHAC1 are the top genes at H1/D10/A12 and map back to them in position_sensitive_genes (same restriction). H1 and D10 are in the first 10 rows of position_effects.csv: WARN only, because that file is sorted by the number of shifted genes, and chance alone gives each position 0-6 of them. Dimethyl fumarate is the top HMOX1 inducer. Bortezomib 5 uM is toxic. "MTAP not expressed" equals the planted lines, with Pemetrexed in its top 3. The failed well is excluded. Plate 2 DMSO reads low for PSMD10/CDKN1A. Dinaciclib shows a transcription drop. Paclitaxel shows a G2/M build-up. Ciclopirox/TFRC, Rimonabant/NAPEPLD, Bortezomib/HSPA1A and DNMT inhibitors/ISG15 each come out as top inducers. Ixazomib leads focus_PSMD10/level_vs_growth. Pemetrexed leads focus_MTAP/loss_selective_drugs. The MTAP expression-loss group equals the planted lines. ACSL4 and PSMD10 are biomarkers for Artesunate and Ixazomib. The HDAC class is coherent with Carbamazepine as its outlier. The look-ups print the expected cards (v3: the TFRC card counts the drug-doses whose position correction is uncertain, from `DD_posunc.npy`). `agents --dry-run` writes a prompt per angle. atlas_bundle.zip lists `computation/` files. |
| mtap | H1 is in the top 3 MTAP positions and D10 in the top 3 PSMD10 positions. Plate 2 has the top PSMD10 DMSO offset. The MTAP-null calls equal the planted lines. Pemetrexed is in the top 3 MTAP-null-selective drugs. Ixazomib is in the top 3 "high-Gankyrin lines depleted more". The failed well is excluded. summary.txt has sections 1-9. Bortezomib 5 uM is flagged toxic with a transcription drop. Bortezomib leads the PROTEASOME module. The plate-2 DMSO offset inflates the uncorrected PSMD10 values and not the corrected ones. PSMD10 is higher in G2/M cells. coreg runs and fills its tables. |
| panel | `check` passes; `all` runs with `--min-cells 10 --prior DIR/mtap_gankyrin` and no step logs a failure. Doxorubicin, Topotecan and 5-FU are the top 3 of the p53 WT-vs-altered screen (all three in the top 6). p53 responsiveness separates TP53-WT from TP53-altered lines (AUC >= 0.9, recomputed from `p53_functional_status.csv`). Dimethyl fumarate tops the NRF2 score and the HMOX1 inducers. FERRO_MARKERS rise at 5 uM (z >= 3, FDR < 0.1) under Artesunate with ISR z < 3 and under Auranofin with ISR z >= 3, and both get a reading. Ciclopirox is the top TFRC inducer; Rimonabant is in the top 3 NAPEPLD inducers. Decitabine leads, and 5-Azacytidine is in the top 3 of, GSDME inducers in the GSDME-silenced lines; the GSDME loss group equals the planted lines. The deleted CDKN2A/CDKN2B get no 're-expression' reading, and Decitabine tops the GSDME 're-expression' readings (its 5 uM is the drug's strongest dose; the lower doses' noise does not make that 'inconsistent'). IL1B counts as expressed (above ambient RNA) only in the 2 planted IL1B lines. TRIM72 is 'not expressed'; NLRP3/CASP5/AIM2 are not testable. ACSL4 and PSMD10 levels predict Artesunate and Ixazomib depletion (top 3, rho < 0). Pemetrexed is in the top 3 MTAP-null-selective drugs. Bortezomib 5 uM is toxic with HEAT_SHOCK and PROTEASOME context. CHAC1's top position is A12, no CHAC1 call comes from an A12 well, and unplanted CHAC1 up calls are within what an FDR of 10% allows (see the known limits). Plate 2 tops the CDKN1A and PSMD10 DMSO offsets, inflates the uncorrected CDKN1A values and gives no corrected call. The failed well is excluded. Every planted positive control is 'clear', and `positive_controls.csv` marks each one robust or uncertain at 24 h (DNMT inhibitors uncertain). 100% of wells and the MTAP-null calls agree with the earlier run. The MTAP-null screen (z_selective, depletion) and the Gankyrin level screen (rho, rho_partial_G2M, z) reproduce `tahoe_mtap_gankyrin.py`'s files within 1e-6. summary.txt has sections 1-9 and no failed step; every angle has brief.md; `agents --dry-run` writes a prompt per angle and `gene_panel/agents.log`. A second `analyze` (with `--prior none`) moves the earlier results to `results/previous_run/`, removes old tables from the angle folders and keeps the agents' own scripts. The bundle holds the summary, the positive controls and both logs, and leaves out a report older than the analysis. |
| atlas, v3 | `effects/complete.json` version 3 and `EFFECTS_VERSION` 3. a: `plate_scale.csv` gives plate6 a factor ~2 (1.5-2.8), its peer plate5 1 (raw < 0.85: never narrowed), the others <= 1.25, one group per regular plate (the reference well and the DMSO wells join it: their rows carry its factor) and 3 on plate13; drugdose.csv `plate_scale` = the mean factor of the used wells, 'noisy plate (z scaled)' exactly when > 1.2; inert drugs at 5 uM have at most 2x + 10 the significant genes of 0.5 uM. b: exactly the plate13-only drug-doses are 'unreliable plate only'; drug-doses with a plate13 well count only their reliable wells (`n_wells`) and `DD_lfc` is the mean W2 of those; `replicates.csv` has the four `pair_type`s and plate13 pairs agree less (median r over drug-doses with >= 10 genes) than pairs at a different position; summary.json reports per pair type and holds the same-position null next to the random-pair null. c: Pyridoxine's median abs log2FC on Dinaciclib's 26 genes < 0.15, `DD_posunc.npy` set there (>= 80%; <= 10% on its other genes, <= 20% for Dinaciclib), Dinaciclib's own 5 uM down genes still <= -1 log2. d: only Bestatin 0.05 is 'position not correctable' (`position_not_correctable`), its H10 wells have < 3 donors, wells.csv has a clean-donor column. e: `composition_shift.parquet`; the 8-Hydroxyquinoline 5 uM wells read the planted shift (within 0.2), other wells ~0, the drug-dose <= -0.3 and 'composition shift' (at most 3 drug-doses flagged), its other genes ~0 after the normalisation, its 4 genes >= 8x. f: the row-loss drugs 'low cells (technical?)' and 'plate-row cell shift' (>= 10 of 12), none 'toxic'; Ranolazine 0.05 'low cells (technical?)'; Bortezomib 5 and Doxorubicin 5 'toxic'. 'cell-cycle shift' follows the v3 rule; 'wells disagree' follows `replicate_r`. Focus tables count only expressing lines, carry the new flags, and their briefs the 'inconclusive' context (no bentamapimod); no q < 0.1 in level_vs_growth / proliferation_dependent_drugs from a drug without a planted growth effect; selective_drugs.csv lists 'replicated' first; feature_response `small_group`; the lowest_active_dose rule; <= 25 genes per best drug-dose and no noise-class RNAs in the inducible / repressible lists; a plate x dose calibration table; METHODS / RULEBOOK name plate6, plate13, B11, the new flags and the real gene count; every script path in a brief exists; `--help` lists `--unreliable-plates`; atlas_bundle.zip holds briefs/<angle>.md. |
| mtap, v3 | `METHOD_VERSION` 3; in MTAP_drug_effects_by_dose.csv Bestatin 0.05 'position not correctable', Bestatin 0.5 / 5 'unreliable plate only', no 'plate DMSO offset' flag (column kept), `n_plates` counts the reliable wells, the cell-loss flags as above, the drug-doses with a plate6 well 'noisy plate (z scaled)'; with the atlas present summary.txt does not say 'composition normalisation not applied' and the composition drug is flagged (without it, it says so); `--help` lists `--unreliable-plates`. |
| panel, v3 | `results/run_info.json` method_version 3. The atlas focus_MTAP / focus_PSMD10 drug_effects.csv and the panel's by-dose tables agree on every drug-dose (both leave out a well with < 5 measured lines, MIN_LINES; a drug-dose without a value must lack it in both): log2FC within 1e-3 for >= 98% (max 0.02), z within 0.05 + 3%, calls (<= 2 differ), the shared flags (<= 3% differ); `plate_scale` equal to the atlas's on every drug-dose; `well_effects.csv.gz` composition shifts equal to the atlas's (0.02) and the composition drug's panel genes ~0 (their median within 0.1 of 0, their median abs log2FC at most max(0.15, 1.3x that of the other 5 uM drug-doses, whose wells also sit on plate5 and the noisy plate6)). TFRC: Pyridoxine ~0, 'position correction uncertain', no call, at every dose; Dinaciclib 5 uM still 'down'. The trap flags of MTAP / TFRC (d, b), `n_plates`, the noisy-plate flag, the cell-loss flags (drug_context_by_dose.csv), the cell-cycle rule, no 'plate DMSO offset' flag anywhere; p53 `pattern` follows its rule (DNA-damage drugs 'WT induction', printed in summary.txt); every 're-expression' reading has >= 2 lines up; summary.txt section 4 names the dose-level FDR and prints the GSDME readout; the cross-links' shared-drug count is compared with an expectation matched for drug activity (the atlas's significant genes); `well_effects.csv.gz` columns; the briefs name plate6 / plate13 / B11 / the new flags / composition, MG53 protein, the IL1B lines, and the script; `--help` lists `--unreliable-plates`; next to a `tahoe_mtap_gankyrin.py` with METHOD_VERSION 2 the panel stops. After `analyze --prior none`: no prior/, no 'reproducibility vs the earlier run', no 'two runs', "this run's MTAP / PSMD10 lists" in summary.txt. The bundle holds briefs/<pathway>.md, run_info.json and well_effects.csv.gz. |
| wrapper, v3 | With the atlas's effects stamped version 2, then the panel's results method_version 2 (restored afterwards, with their times), status reads 'done, but outdated' and Next: tahoe run. With three briefs older than the effects (an interrupted `angles`), the atlas is not ready and `tahoe run` plans `angles`. `tahoe_status.py briefcheck` (the 'tahoe agents' preflight) is silent on the smoke run's briefs and names a deleted copy of tahoe_atlas.py that a brief still names (the brief is restored afterwards; no agent runs). |
| review fixes (v3) | Atlas: 'toxic' re-derived from the columns for every drug-dose (the plate row subtracted only when it is itself shifted > 0.8 log2; with several used wells the best one < -0.5 too; no higher dose >= -1); trap c2; `plate_scale_gene.npy` = max(group factor, the gene's own spread ratio / 1.3), recomputed from W2, and `quality/calibration_by_plate_gene.csv`; replicate agreement counts each drug-dose once (summary.json `drug_doses` per type; pairs with a well without position correction apart) and the scaled plate groups leave out joined control wells; focus per-line columns only where the fold change has a value; calibration shares over the measured z; the briefs: 'low cells (technical?)' is 'not confirmed' (no 'recovery artifact'), how well two wells agree on cell loss (from the data), replicates per drug-dose, sequencing depth in the focus briefs; `angles/complete.json`; the bundle holds `effects/genes.csv` and `README_effects.md`. Unit checks on crafted inputs: the 'toxic' rule in both scripts, one `--unreliable-plates` parser, the stale-brief guard on a quoted path with a space, the noise-RNA classes (H1-*, RPL13AP5), one salt-form helper, the per-gene factor. Panel: 'toxic' re-derived in drug_context_by_dose.csv and MTAP_drug_effects_by_dose.csv; CASP1 rows with z >= 3 read 'lost lines read ambient only' (no deleted line), GSDME Decitabine 5 uM stays 're-expression'; `plate_scale_by_gene.csv` follows its definition and equals the atlas's for MTAP / PSMD10; a gene in 6 lines, 2 of them sparse (as the real CASP5), keeps a value in >= 90% of drug wells; `position_wells_used` means the same in both scripts; `well_effects.csv.gz` has the uncorrected value and the position state; Bortezomib's HMOX1 / CHAC1 called at >= 1 dose and >= 1.5x at 5 uM; no brief says 'do not rely on its expression changes'; the crosslinks heading names no earlier analysis. |

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
- A well that lost most of its cells keeps few profiles with >= 10 cells here (real wells keep hundreds of cells per
  line). The atlas and `tahoe_mtap_gankyrin.py` both leave a well with < 5 measured lines out (MIN_LINES, also as a
  position donor; the panel's effects within the lines that lost a gene need one), so this changes no agreement.
- Chance: at an FDR of 10% a few false calls are expected. The CHAC1 check allows unplanted up calls up to what
  that FDR allows (ceil(10% of the calls); method-independent): the current draw (seed 0) gives one, Bentamapimod
  0.5 uM (q ~0.1; the method before v3 calls it too, q 0.086, with Pimitespib 5 uM). The draws that the v3 traps
  first made each moved another chance-bound check (p53 AUC 0.89, the GSDME top 3, the empirical-null zero), so the
  traps added since (c2) consume no random number of the main draw.
- Bortezomib 5 uM keeps ~7 cells per line and well (0.3x) and one of its two wells sits on the noisy plate6 (z
  divided by ~2): its planted HMOX1 / CHAC1 rise shows (>= 1.5x) but is not called; the 0.5 uM dose is.

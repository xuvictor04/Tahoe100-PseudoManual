# tables/ - the fold-change tables

Written by `tahoemap tables` (tahoemap/tables.py). Keys: `col` = gene column (0 .. genes-1, the order of atlas/effects/genes.csv), `dd` = drug-dose row (atlas/effects/drugdose.csv), `line` = cell-line index (atlas/effects/lines.csv), `w` = well row (atlas/effects/wells.csv). Join on these, not on names: symbols can repeat.

**Baseline of every fold change**: the same cell line's median over the plate's *drug* wells (the typical treated well; most drugs leave most genes alone), **not DMSO**. For each line and well the atlas takes log2 CPM minus that line's plate median, minus the profile's composition (library-size) shift, minus the well-position effect. Pooled values (`lfc`, `z`, `q_*`, `pooled_*`) take the median over lines per well and then the mean (lfc) or Stouffer sum (z) over the drug-dose's used wells; per-line values (tensor DDL_lfc / DDL_z) keep each line. `lfc` is log2; `fold` = 2**lfc (1 = no change, 2 = doubled, 0.5 = halved). z is a robust z (median / 1.4826 MAD of the drug wells), widened on noisy plates.

**Significant** (as the atlas): q_up < 0.1 and fold >= 1.2 (up), q_down < 0.1 and fold <= 1/1.2 (down); q = Benjamini-Hochberg within each gene over all drug-doses. **Clean** = no artifact flag (toxic, transcription drop, cell-cycle shift, unreliable plate only, position not correctable, position correction uncertain, wells disagree) in the drug-dose's flags plus the gene's own flags (a cell-cycle shift counts only where it is the explanation of the gene's change: see below). Soft caveats that do not make a value unclean: low cells (technical?), plate-row cell shift, composition shift, noisy plate (z scaled), position effect removed. **Flagged values are kept**: every table lists flagged drug-doses in their ranked place with their flags (and `clean` = False); only estimates (the per-line |z| calibration, response_sd, the cell-cycle slopes) leave artifact-flagged drug-doses out.

Missing values: NaN / null = not measured (line not expressing, too few cells or counts) or no candidate; -1 in an index or count column = none / not measured.

**Pooled vs per line**: the pooled values are the atlas's *median over the measured lines*, so a response seen in fewer than about half of the measured lines (e.g. a p53 response in the TP53-wild-type lines only) does not appear in drug_effects or in the n_dd_* / best_* columns of genes.parquet. Such responses are in line_effects (per gene x line) and drug_line_top (each gene's strongest drug-dose x line cells).

**Per-line significance** (line_effects n_dd_up / n_dd_down / best_*, drug_line_top): per-line |z| >= **8.45** (`line_z_threshold` in tables/info.json; fold >= 1.5 for line_effects). A per-line z rests on one or two wells and its tails are heavier than a normal's, so the cut is calibrated on this run: among (gene, clean drug-dose) pairs whose pooled |z| < 2 (the null), P(|per-line z| >= 3) = 0.0099, >= 4: 0.003, >= 5: 0.001, >= 6: 0.00039. t is the smallest value >= 4 at which the expected number of chance passes per (gene, line) over the 1026 clean drug-doses is <= 0.05; at t it is 0.049 (`line_z_expected_chance`; over all drug-doses, as line_effects' *_all counts: 0.054, `line_z_expected_chance_all`). The 'lines up / down' of drug_effects and genes.parquet (per-line z >= 2 and fold >= 1.2, given a pooled call) are descriptive: they say where the pooled effect shows up, and a line with no effect reaches z >= 2 at a rate of 0.012 and z <= -2 at 0.032 (`lines_up_chance_rate`, `lines_down_chance_rate`; the null's tails per direction are `line_z_null_tail_up` / `_down`: low counts make the lower tail heavier).

**Lines that do not express a gene** (line_effects `expressed` = False) have no per-line values: below 0.25 x the gene's pooled level a line reads only the wells' ambient RNA (the average of all the well's cells), whose 'responses' are other lines' (tensor/line_measured.npy). Profiles with < 2 expected counts of the gene (few cells or a low level) are not measured either. So re-expression of a gene a line does not make is not detected here.

**Cell-cycle shift** (decided per gene): the atlas flags a drug-dose 'cell-cycle shift' when its cells moved into or out of S or G2/M (the S_PHASE or G2M_PHASE module's pooled log2 fold change beyond 0.5, or beyond 0.25 at |z| >= 4). That is a property of the drug-dose; whether it explains a given gene's change depends on how much the gene goes with the cell cycle, and that is measured here: per gene, a robust regression (OLS, then one Huber reweighting at 2.5 robust SDs) of its pooled lfc on the two modules' pooled lfc, lfc ~ a + bS x S + bG x G, over the 1,062 drug-doses with no other artifact flag (genes.parquet cc_slope_S / cc_slope_G2M; >= 20 drug-doses with a value for the gene). At a flagged drug-dose the shift predicts bS x S + bG x G of the gene's change, with the slopes fitted again without that drug-dose when it is among the fitted ones (leave-one-out: the drug-doses being judged have the largest module changes, so a strong change of the gene's own there would otherwise pull the slopes toward explaining it), and `cc_share` (drug_effects, drug_line_top) is that part's share of the observed change (0 when it points the other way). Fitted slopes are attenuated by measurement noise (the modules' lfc are measured with error too), so the rule doubles them to be safe: the plain artifact flag 'cell-cycle shift' stays unless 2 x cc_share < 0.5 and the change left after the doubled prediction, |lfc| x (1 - 2 x cc_share), is at least the 1.2x floor; then the gene's flags read 'cell-cycle shift (explains ~N% here)', which is no artifact flag, and the value is clean unless another flag says otherwise (other artifact flags of the drug-dose still apply). This run: 54 drug-doses carry the flag, 46 of them no other artifact flag; there the rule clears 135,718 of 193,346 significant changes (165,641 with the slopes as fitted). Check, the genes of the atlas's cell-cycle modules at every flagged drug-dose (the shift is what moves them, so few should be cleared): significant changes cleared S_PHASE: 130 of 1,168 (43 genes); G2M_PHASE: 186 of 1,448 (54 genes).

Example from the full Tahoe-100M run: TRIM72 (MG53) has slopes bS +0.50, bG +0.47. Idarubicin 5 uM raises it 12.2x (z +15.9, in 37 of 37 lines) and its cell-cycle shift would explain ~4% of that; homoharringtonine 5 uM ~18%, 0.5 uM ~8%; epirubicin 5 uM ~14%: all cleared (clean). At panobinostat 0.5 uM (~87%) and TAK-901 5 uM (~75%) the flag stays. Classic cell-cycle genes have large slopes (PCNA bS +1.50, CCNE2 bS +1.55, TOP2A bG +1.51, CCNB1 bG +1.38), so at a real shift the flag stays for them. Over the 46 drug-doses whose only artifact flag is the shift, the rule clears 131,683 of 193,346 significant changes (163,786 with the slopes as fitted).

## genes.parquet

One row per gene (gene columns of atlas/effects/genes.csv; the S_PHASE, G2M_PHASE and PROTEASOME module columns are not here). 'Clean' = the drug-dose's flags plus this gene's flags hold none of: toxic, transcription drop, cell-cycle shift (only where the shift is the explanation of this gene's change: see 'Cell-cycle shift'), unreliable plate only, position not correctable, position correction uncertain, wells disagree. n_dd_up / n_dd_down and best_up_* / best_down_* count and rank every drug-dose (flagged ones included: their flags are in best_*_flags); the *_clean columns the clean ones only.

| column | meaning |
|---|---|
| `col` | gene column: row key of genes.csv and column of every gene matrix (0 .. genes-1). Key genes by col |
| `symbol` | gene symbol (can repeat between columns) |
| `label` | unique label: the symbol, or 'SYM (ENSG...)' for repeated symbols |
| `ensembl_id` | Ensembl gene id from the Tahoe gene metadata (joined on token; '' when missing) |
| `token` | Tahoe gene token id |
| `pooled_cpm` | level over all wells and lines (counts per million) |
| `median_line_cpm` | median over cell lines of the line's level (CPM) |
| `n_lines_expressing` | lines that truly express the gene (line_effects 'expressed', tensor/line_measured.npy): level >= 25% of the median line's (the atlas's expr_mask) AND >= 25% of the gene's pooled level (otherwise the line reads only ambient RNA); atlas/effects/genes.csv keeps the atlas's count |
| `noise_rna` | True for noise-class RNAs (atlas NOISE_RNA_RE on the symbol: 7SK, snoRNA, snRNA, mitochondrial, ribosomal-protein pseudogenes, replication histones, ENSG-only names): read their drug responses with care |
| `corr_with_S` | Pearson r over all drug wells (pairwise complete) of the gene's corrected well effect (W2) with the S-phase module's: near 1 = the gene moves with the S-phase share of cells |
| `corr_with_G2M` | the same with the G2/M module |
| `n_dd_up` | drug-doses that raise the gene significantly (q_up < 0.10 and fold >= 1.2) |
| `n_dd_down` | drug-doses that lower it significantly (q_down < 0.10 and fold <= 1/1.2) |
| `n_dd_up_clean` | n_dd_up among clean drug-doses (no artifact flag for this gene) |
| `n_dd_down_clean` | n_dd_down among clean drug-doses |
| `best_up_dd` | highest pooled z over all drug-doses (flagged ones included; may be non-significant: check q): drug-dose row (-1 = none) |
| `best_up_drug` | highest pooled z over all drug-doses (flagged ones included; may be non-significant: check q): drug |
| `best_up_dose` | highest pooled z over all drug-doses (flagged ones included; may be non-significant: check q): dose key (uM) |
| `best_up_fold` | highest pooled z over all drug-doses (flagged ones included; may be non-significant: check q): pooled fold change (linear; 2**lfc; log2 fold change vs the same cell line's median over the plate's drug wells (not DMSO), after the composition shift and the well-position effect are removed) |
| `best_up_z` | highest pooled z over all drug-doses (flagged ones included; may be non-significant: check q): pooled z (DD_z) |
| `best_up_q` | highest pooled z over all drug-doses (flagged ones included; may be non-significant: check q): BH q-value of the atlas in that direction (q_up for up, q_down for down; within the gene over all drug-doses) |
| `best_up_flags` | highest pooled z over all drug-doses (flagged ones included; may be non-significant: check q): drug-dose flags + this gene's flags (atlas_core.gene_flags), '; '-joined; 'cell-cycle shift (explains ~N% here)' where the drug-dose's shift is not the explanation of this gene's change (no artifact flag; see 'Cell-cycle shift') |
| `best_down_dd` | lowest pooled z over all drug-doses (flagged ones included): drug-dose row (-1 = none) |
| `best_down_drug` | lowest pooled z over all drug-doses (flagged ones included): drug |
| `best_down_dose` | lowest pooled z over all drug-doses (flagged ones included): dose key (uM) |
| `best_down_fold` | lowest pooled z over all drug-doses (flagged ones included): pooled fold change (linear; 2**lfc; log2 fold change vs the same cell line's median over the plate's drug wells (not DMSO), after the composition shift and the well-position effect are removed) |
| `best_down_z` | lowest pooled z over all drug-doses (flagged ones included): pooled z (DD_z) |
| `best_down_q` | lowest pooled z over all drug-doses (flagged ones included): BH q-value of the atlas in that direction (q_up for up, q_down for down; within the gene over all drug-doses) |
| `best_down_flags` | lowest pooled z over all drug-doses (flagged ones included): drug-dose flags + this gene's flags (atlas_core.gene_flags), '; '-joined; 'cell-cycle shift (explains ~N% here)' where the drug-dose's shift is not the explanation of this gene's change (no artifact flag; see 'Cell-cycle shift') |
| `best_clean_up_dd` | highest pooled z over the clean drug-doses for this gene: drug-dose row (-1 = none) |
| `best_clean_up_drug` | highest pooled z over the clean drug-doses for this gene: drug |
| `best_clean_up_dose` | highest pooled z over the clean drug-doses for this gene: dose key (uM) |
| `best_clean_up_fold` | highest pooled z over the clean drug-doses for this gene: pooled fold change (linear; 2**lfc; log2 fold change vs the same cell line's median over the plate's drug wells (not DMSO), after the composition shift and the well-position effect are removed) |
| `best_clean_up_z` | highest pooled z over the clean drug-doses for this gene: pooled z (DD_z) |
| `best_clean_up_q` | highest pooled z over the clean drug-doses for this gene: BH q-value of the atlas in that direction (q_up for up, q_down for down; within the gene over all drug-doses) |
| `best_clean_up_flags` | highest pooled z over the clean drug-doses for this gene: drug-dose flags + this gene's flags (atlas_core.gene_flags), '; '-joined; 'cell-cycle shift (explains ~N% here)' where the drug-dose's shift is not the explanation of this gene's change (no artifact flag; see 'Cell-cycle shift') |
| `best_clean_up_n_lines_up` | best clean drug-dose up: lines with per-line z >= 2 and fold >= 1.2 (tensor DDL_z / DDL_lfc; descriptive, not a per-line test: see drug_effects n_lines_up); -1 = no clean drug-dose |
| `best_clean_up_pattern` | dose pattern of that drug for this gene (atlas dose_shape over its doses' pooled z) |
| `best_clean_down_dd` | lowest pooled z over the clean drug-doses for this gene: drug-dose row (-1 = none) |
| `best_clean_down_drug` | lowest pooled z over the clean drug-doses for this gene: drug |
| `best_clean_down_dose` | lowest pooled z over the clean drug-doses for this gene: dose key (uM) |
| `best_clean_down_fold` | lowest pooled z over the clean drug-doses for this gene: pooled fold change (linear; 2**lfc; log2 fold change vs the same cell line's median over the plate's drug wells (not DMSO), after the composition shift and the well-position effect are removed) |
| `best_clean_down_z` | lowest pooled z over the clean drug-doses for this gene: pooled z (DD_z) |
| `best_clean_down_q` | lowest pooled z over the clean drug-doses for this gene: BH q-value of the atlas in that direction (q_up for up, q_down for down; within the gene over all drug-doses) |
| `best_clean_down_flags` | lowest pooled z over the clean drug-doses for this gene: drug-dose flags + this gene's flags (atlas_core.gene_flags), '; '-joined; 'cell-cycle shift (explains ~N% here)' where the drug-dose's shift is not the explanation of this gene's change (no artifact flag; see 'Cell-cycle shift') |
| `best_clean_down_n_lines_down` | best clean drug-dose down: lines with per-line z <= -2 and fold <= 1/1.2 (descriptive); -1 = none |
| `best_clean_down_pattern` | the same for the decrease (z negated) |
| `up_specificity_z_gap` | best clean z up minus the best clean z up of any OTHER compound (salt forms merged): large = one compound stands out; NaN with < 2 compounds |
| `down_specificity_z_gap` | the same for decreases (in units of -z) |
| `cc_slope_S` | the gene's slope bS on the S-phase module's pooled log2 fold change (robust regression of its pooled lfc on the S_PHASE and G2M_PHASE modules' pooled lfc over the drug-doses without another artifact flag; see 'Cell-cycle shift'): how much of a cell-cycle shift reaches the gene (~1: it moves like the module; ~0: unaffected); NaN with < 20 fitted drug-doses |
| `cc_slope_G2M` | the same slope bG on the G2/M module's pooled log2 fold change |

## drug_effects.parquet

Fold change relative to each drug: one row per gene x drug-dose with |pooled z| >= 3 or q_up < 0.10 or q_down < 0.10 (sorted by col, then z from high to low). Pooled = over the cell lines (median per well, mean over the drug-dose's used wells), so a response seen in fewer than about half of the measured lines is not here: look in line_effects / drug_line_top. Per-line values come from the tensor (DDL_z, DDL_lfc). The line counts (n_lines_up / n_lines_down / lines_*) are descriptive: per-line z >= 2 is not a per-line test (see 'Per-line significance' above).

| column | meaning |
|---|---|
| `col` | gene column |
| `symbol` | gene symbol |
| `dd` | drug-dose row: row of atlas/effects/drugdose.csv and of every DD_* / DDL_* matrix |
| `drug` | drug name as in Tahoe (salt forms are separate drugs; see salt_base) |
| `dose` | dose key (text): the concentration formatted with %.6g, in the unit of the sample metadata (uM) |
| `conc` | concentration (uM) |
| `lfc` | pooled log2 fold change vs the same cell line's median over the plate's drug wells (not DMSO), after the composition shift and the well-position effect are removed (DD_lfc) |
| `fold` | 2**lfc (linear fold change; 1 = no change) |
| `z` | pooled z (DD_z: Stouffer over the used wells of the robust z of the corrected well effect, divided by the gene's plate factor) |
| `q_up` | BH q-value for an increase (within the gene, over all drug-doses) |
| `q_down` | BH q-value for a decrease |
| `flags` | drug-dose flags + this gene's flags ('noisy plate (z scaled)' from its own plate factor, 'position correction uncertain', 'position effect removed'), '; '-joined, the exact strings of the atlas, except that a drug-dose's 'cell-cycle shift' reads 'cell-cycle shift (explains ~N% here)' where the shift is not the explanation of this gene's change (N = round(100 x cc_share); no artifact flag) |
| `clean` | True when flags hold no artifact flag (atlas_core.has_artifact; see genes.parquet). Rows that are not clean are kept: read them with their flags |
| `n_lines_measured` | lines with a per-line value (truly expressing the gene, enough cells in the wells, >= 2 expected counts) |
| `n_lines_up` | lines with per-line z >= 2 and fold >= 1.2: where the pooled effect shows up (descriptive; at z >= 2 a line also passes by chance, at the rate lines_up_chance_rate of tables/info.json) |
| `n_lines_down` | lines with per-line z <= -2 and fold <= 1/1.2 (descriptive, as n_lines_up) |
| `lines_up` | cell names of those lines, strongest per-line z first, at most 12, ', '-joined |
| `lines_down` | cell names of the lines counted in n_lines_down, most negative per-line z first, at most 12 |
| `pattern_up` | how the increase behaves over the drug's doses (atlas dose_shape over the pooled z by ascending dose; the same for every dose of the drug): none / single dose / all doses, stronger at high dose / all doses, flat / top dose only / rises with dose / two highest doses / inconsistent across doses |
| `pattern_down` | the same for the decrease (z negated) |
| `cc_share` | at a drug-dose whose flags include 'cell-cycle shift': the share of this gene's change that the shift would explain, /bS x S + bG x G/ / /lfc/ with the gene's slopes (genes.parquet cc_slope_S, cc_slope_G2M, here fitted again without this drug-dose when it is in the fit: leave-one-out) and the drug-dose's S_PHASE_lfc / G2M_PHASE_lfc; 0 when that predicted part goes the other way; at most 1. NaN for drug-doses without the flag (or genes without slopes). The flag stays an artifact flag unless 2 x cc_share < 0.5 and /lfc/ x (1 - 2 x cc_share) >= log2 1.2 (see 'Cell-cycle shift') |

## line_effects.parquet

Fold change relative to each cell line: one row per gene x cell line (all genes x all lines). Counts and bests without a suffix use the clean drug-doses for the gene, those ending in '_all' every drug-dose (flagged ones included, with their flags in best_*_flags_all); both use the per-line tensor values (DDL_z, DDL_lfc): a per-line fold change is the mean over the drug-dose's used wells of that line's log2 fold change vs the same cell line's median over the plate's drug wells (not DMSO), after the composition shift and the well-position effect are removed; per-line z = Stouffer over those wells of (value - line centre) / line scale / plate factor.

| column | meaning |
|---|---|
| `col` | gene column |
| `symbol` | gene symbol |
| `line` | line index (row of lines.parquet / atlas lines.csv, last axis of the tensor) |
| `cell_line_id` | Cellosaurus id |
| `cell_name` | cell line name |
| `baseline_cpm` | the line's level of the gene over all its wells (CPM; atlas line_cpm) |
| `expressed` | the line truly expresses the gene (tensor/line_measured.npy): the atlas's expr_mask (level >= 25% of the median line's) AND level >= 25% of the gene's pooled level; below that the line reads only the wells' ambient RNA, and its per-line values are NaN |
| `response_sd` | 1.4826 x MAD over the clean drug-doses of the line's per-line log2 fold change: the typical spread of this gene's responses in this line (log2; NaN with < 10 measured clean drug-doses) |
| `n_dd_up` | clean drug-doses with per-line z >= line_z_threshold (calibrated; tables/info.json) and fold >= 1.5 in this line |
| `n_dd_down` | clean drug-doses with per-line z <= -line_z_threshold and fold <= 1/1.5 |
| `best_up_dd` | the drug-dose counted in n_dd_up with the highest per-line z in this line (-1 = none passes) |
| `best_up_drug` | its drug |
| `best_up_dose` | its dose key (uM) |
| `best_up_lfc` | its per-line log2 fold change |
| `best_up_z` | its per-line z |
| `best_down_dd` | the drug-dose counted in n_dd_down with the lowest per-line z (-1 = none passes) |
| `best_down_drug` | its drug |
| `best_down_dose` | its dose key (uM) |
| `best_down_lfc` | its per-line log2 fold change |
| `best_down_z` | its per-line z |
| `n_dd_up_all` | n_dd_up over all drug-doses (flagged ones included). Chance passes grow with the number of drug-doses: line_z_expected_chance_all of tables/info.json |
| `n_dd_down_all` | n_dd_down over all drug-doses (flagged ones included) |
| `best_up_dd_all` | the drug-dose counted in n_dd_up_all with the highest per-line z in this line, flagged or not (-1 = none passes); equal to best_up_dd when that one is clean |
| `best_up_drug_all` | its drug |
| `best_up_dose_all` | its dose key (uM) |
| `best_up_lfc_all` | its per-line log2 fold change |
| `best_up_z_all` | its per-line z |
| `best_up_flags_all` | its flags for this gene (as drug_effects flags; null = none passes) |
| `best_up_clean_all` | True when those flags hold no artifact flag (False when none passes) |
| `best_up_cc_share_all` | its cc_share for this gene (as drug_effects; NaN without the cell-cycle flag) |
| `best_down_dd_all` | the drug-dose counted in n_dd_down_all with the lowest per-line z in this line, flagged or not (-1 = none passes) |
| `best_down_drug_all` | its drug |
| `best_down_dose_all` | its dose key (uM) |
| `best_down_lfc_all` | its per-line log2 fold change |
| `best_down_z_all` | its per-line z |
| `best_down_flags_all` | its flags for this gene (null = none passes) |
| `best_down_clean_all` | True when those flags hold no artifact flag (False when none passes) |
| `best_down_cc_share_all` | its cc_share for this gene (NaN without the cell-cycle flag) |

## drug_line_top.parquet

Per gene and direction, the 15 strongest (drug-dose, cell line) cells over ALL drug-doses (flagged ones included, with their flags) with per-line |z| >= line_z_threshold (calibrated; tables/info.json; no fold condition), plus any of the 15 strongest among the clean drug-doses for the gene that fall outside them, so that flagged cells never push the clean ones out: at most 30 rows per gene and direction, fewer when fewer qualify. Responses confined to a few lines, which the pooled tables miss, show up here.

| column | meaning |
|---|---|
| `col` | gene column |
| `symbol` | gene symbol |
| `direction` | up / down |
| `rank` | rank of the cell's per-line z in that direction among all the gene's qualifying cells, flagged or not (1 = strongest; a clean cell kept beyond the 15 strongest has its rank over all, > 15) |
| `dd` | drug-dose row: row of atlas/effects/drugdose.csv and of every DD_* / DDL_* matrix |
| `drug` | drug name as in Tahoe (salt forms are separate drugs; see salt_base) |
| `dose` | dose key (text): the concentration formatted with %.6g, in the unit of the sample metadata (uM) |
| `line` | line index |
| `cell_name` | cell line name |
| `lfc` | per-line log2 fold change vs the same cell line's median over the plate's drug wells (not DMSO), after the composition shift and the well-position effect are removed (DDL_lfc) |
| `z` | per-line z (DDL_z) |
| `pooled_lfc` | the drug-dose's pooled log2 fold change for the gene (DD_lfc) |
| `pooled_z` | the drug-dose's pooled z (DD_z) |
| `flags` | the drug-dose's flags for this gene (as drug_effects flags) |
| `clean` | True when flags hold no artifact flag; False = read the cell with its flags |
| `cc_share` | the share of the gene's pooled change the drug-dose's cell-cycle shift would explain (as drug_effects; NaN without the flag) |

## drugdoses.parquet

atlas/effects/drugdose.csv (one row per drug and dose) plus dd, salt_base, top_up and top_down.

| column | meaning |
|---|---|
| `dd` | drug-dose row: row of atlas/effects/drugdose.csv and of every DD_* / DDL_* matrix |
| `drug` | drug name as in Tahoe (salt forms are separate drugs; see salt_base) |
| `dose` | dose key (text): the concentration formatted with %.6g, in the unit of the sample metadata (uM) |
| `salt_base` | drug name without the trailing salt / form in brackets (tlib.salt_base): salt forms of one compound share it |
| `conc` | concentration (uM) |
| `n_wells` | used wells (those on reliable plates; all of them when the drug-dose sits only on unreliable plates) |
| `n_wells_all` | all its wells |
| `wells` | well names of the used wells |
| `plates` | plates of the used wells |
| `wells_left_out` | plate:well of wells left out (on unreliable plates) |
| `unreliable_plate_only` | True when every well is on an unreliable plate |
| `cells_log2_vs_plate` | cells per well, log2 vs the plate's median drug well (mean over used wells) |
| `umi_per_cell_log2_vs_plate` | UMIs per cell, log2 vs the plate's median drug well |
| `genes_per_cell_log2_vs_plate` | genes detected per cell, log2 vs the plate's median drug well |
| `row_cells_log2` | the same as cells_log2_vs_plate for the other drug wells in the same plate row (median; mean over the used wells) |
| `row_umi_per_cell_log2` | the same for UMIs per cell |
| `row_genes_per_cell_log2` | the same for genes per cell |
| `composition_shift_log2` | median over the wells' lines of the profile's composition (library-size) shift (log2) |
| `cells_log2_best_well` | the largest cells_log2_beyond_row of the used wells ('toxic' needs it < -0.5) |
| `plate_scale` | mean plate factor (z divisor) of the used wells |
| `position_wells_used` | mean number of other-drug wells at the same position used for the position correction |
| `position_not_correctable` | True when a used well had < 3 other-drug wells at its position |
| `S_PHASE_lfc` | S-phase module log2 fold change |
| `S_PHASE_z` | S-phase module z |
| `G2M_PHASE_lfc` | G2/M module log2 fold change |
| `G2M_PHASE_z` | G2/M module z |
| `PROTEASOME_lfc` | proteasome module log2 fold change |
| `PROTEASOME_z` | proteasome module z |
| `cells_log2_best_higher_dose` | best cells_log2_vs_plate of the same drug at a higher dose (NaN: none) |
| `flags` | drug-dose flags, '; '-joined (artifacts: toxic, transcription drop, cell-cycle shift, unreliable plate only, position not correctable, wells disagree; caveats: low cells (technical?), plate-row cell shift, composition shift, noisy plate (z scaled)) |
| `n_genes_up` | genes raised significantly (q_up < 0.10, fold >= 1.2) |
| `n_genes_down` | genes lowered significantly |
| `n_sig_genes` | n_genes_up + n_genes_down |
| `replicate_r` | mean pairwise r of the used wells' z over the top 500 genes (wells agree?) |
| `targets` | drug targets (Tahoe drug metadata) |
| `moa_fine` | mechanism of action, fine |
| `moa_broad` | mechanism of action, broad |
| `approved` | human-approved (Tahoe drug metadata) |
| `top_up` | up to 15 significantly raised genes, highest z first: 'LABEL (fold x)' |
| `top_down` | up to 15 significantly lowered genes, lowest z first: 'LABEL (fold x)' |

## drugs.parquet

One row per drug (all its doses).

| column | meaning |
|---|---|
| `drug` | drug name as in Tahoe (salt forms are separate drugs; see salt_base) |
| `salt_base` | drug name without the trailing salt / form in brackets (tlib.salt_base): salt forms of one compound share it |
| `targets` | drug targets |
| `moa_fine` | mechanism of action, fine |
| `moa_broad` | mechanism of action, broad |
| `approved` | human-approved |
| `n_doses` | number of doses |
| `doses` | dose keys by ascending concentration (uM), ' / '-joined |
| `n_sig_by_dose` | significant genes (n_sig_genes) per dose, same order |
| `max_sig` | the largest of them |
| `best_dose` | the dose with the most significant genes (tie -> the higher dose) |
| `best_dd` | its drug-dose row |
| `lowest_active_dose` | the lowest dose such that it and every higher dose have >= 10 significant genes; 'low dose only (noise?)' when only lower doses do; '' when no dose does |
| `flags_by_dose` | each dose's flags ('-' = none), ' / '-joined by ascending dose |
| `signature_r_between_doses` | cosine similarity of the pooled z signatures (genes significant in >= 3 drug-doses) of consecutive doses (low-mid / mid-high): near 1 = the same response growing with dose |

## lines.parquet

atlas/effects/lines.csv (one row per cell line, in the order of the line axis) plus line, tp53_status, n_dd_depleted, n_dd_depleted_clean, median_response.

| column | meaning |
|---|---|
| `line` | line index (last axis of the tensor) |
| `cell_line_id` | Cellosaurus id |
| `n_cells_total` | cells of the line over all wells |
| `cell_name` | cell line name |
| `Cell_ID_DepMap` | DepMap id |
| `Organ` | organ of origin |
| `drivers` | driver genes (variant type) from the Tahoe cell-line metadata |
| `driver_changes` | driver protein changes |
| `in_growth_analysis` | True when the line has enough cells for the relative-abundance (growth) analysis |
| `wells_usable` | wells with >= min_cells cells of the line (usable expression) |
| `pct_wells_usable` | the same as % of all wells |
| `tp53_status` | altered (a TP53 row in the cell-line metadata) / wild type (the line is in the metadata without one) / unknown |
| `n_dd_depleted` | drug-doses that deplete the line: relative-abundance z (DD_Az) <= -3, leaving out only drug-doses whose cell counts are untrustworthy (unreliable plate only, position not correctable, wells disagree); toxic, transcription drop and cell-cycle shift drug-doses count (depletion is what makes them toxic). -1 = not measured: the line is not in the growth analysis (too few cells) |
| `n_dd_depleted_clean` | the same among clean drug-doses only (no artifact flag at all); -1 = not measured |
| `median_response` | median over drug-doses of the line's response strength (DD_beta: slope of the line's changes on the drug-dose's consensus over its significant genes; 1 = a typical line, 0 = no response; only drug-doses with >= 20 significant genes) |

## plates.parquet

One row per plate (atlas plate order).

| column | meaning |
|---|---|
| `plate` | plate |
| `n_wells` | wells analysed (drug + DMSO; failed wells excluded) |
| `n_drug_wells` | drug wells |
| `doses` | dose keys of the drug wells (uM), ' / '-joined |
| `unreliable` | True for plates named unreliable (kept out of pooled drug-doses, centres and plate-factor peers) |
| `plate_factor` | largest plate-group factor of the plate (z divisor; 1 = as noisy as its peers) |
| `dmso_wells` | DMSO well names |
| `n_dmso_wells` | number of DMSO wells |
| `failed_wells` | well names excluded as technical failures (< 1/8 of the plate's typical cells while the drug did fine elsewhere) |
| `n_failed_wells` | number of them |
| `median_cells_per_well` | median cells per analysed well (all lines) |

## wells.parquet

atlas/effects/wells.csv (one row per analysed well, the row order of W1/W2/Z and of the tensor's well axis) plus w and umi_total. Per-gene raw counts per well are in tensor/well_counts.npy (wells x genes, UMI summed over the well's lines), not here.

| column | meaning |
|---|---|
| `w` | well row (axis of W1/W2/Z, tensor R and well_counts) |
| `sample` | Tahoe sample id |
| `plate` | plate |
| `drug` | drug (DMSO_TF for vehicle) |
| `n_cells` | cells in the well (all lines) |
| `is_dmso` | vehicle well |
| `plate_num` | plate number |
| `conc` | concentration (uM; 0 for DMSO) |
| `unit` | concentration unit |
| `mean_gene_count` | mean genes per cell (Tahoe sample metadata) |
| `mean_tscp_count` | mean transcripts per cell (Tahoe sample metadata) |
| `mean_pcnt_mito` | mean mitochondrial fraction (Tahoe sample metadata) |
| `slot` | well position 1-96 (A1 = 1, row-major) |
| `slot_purity` | share of the well's cells whose barcode gives that position |
| `well` | well name (A1 ... H12) |
| `dose` | dose key (uM) |
| `cells` | cells of the analysed lines in the well |
| `umi_per_cell` | UMIs per cell |
| `genes_per_cell` | genes per cell |
| `cells_log2_vs_plate` | cells, log2 vs the plate's median drug well |
| `umi_per_cell_log2_vs_plate` | UMIs per cell, log2 vs the plate's median drug well |
| `genes_per_cell_log2_vs_plate` | genes per cell, log2 vs the plate's median drug well |
| `row_cells_log2` | median cells_log2_vs_plate of the other drug wells in the same plate row |
| `row_umi_per_cell_log2` | the same for UMIs per cell |
| `row_genes_per_cell_log2` | the same for genes per cell |
| `cells_log2_beyond_row` | cell loss beyond the plate row where the row itself moved > 0.8 log2, else cells_log2_vs_plate |
| `composition_shift_log2` | median over the well's lines of the composition shift (log2) |
| `unreliable_plate` | well on an unreliable plate |
| `position_wells_used` | other-drug wells at the same position (position correction donors) |
| `position_clean_donors_median` | median over genes of the clean donors used |
| `position_not_correctable` | < 3 donors: no position correction |
| `plate_scale_group` | plate-and-dose group of the plate factor |
| `plate_scale_group_id` | row of atlas plate_scale_gene.npy (-1: none) |
| `plate_scale_pass1` | the group's plate factor, pass 1 |
| `plate_scale` | the group's plate factor (z divisor) |
| `drugdose_row` | drug-dose row (dd; -1 = DMSO) |
| `used_in_drugdose` | the well counts in its drug-dose |
| `umi_total` | total UMIs of the well over its analysed lines (tensor well_umi) |

The gene x gene table ('relative to each gene') is relations/gene_relations.parquet.

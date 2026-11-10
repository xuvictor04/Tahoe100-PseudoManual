# tahoemap — design and module contracts

This is the engineering contract between the modules of `tahoemap/`. User-facing documentation is in `README.md`
and the other files of `docs/`. Every module reads only the files listed as its inputs and writes only its own
folder under the output root `OUT` (default `<data>/tahoemap`).

## Goal

One command (`tahoe run`) turns Tahoe-100M (50 cell lines × 379 drugs × 3 doses, 14 plates × 96 wells, ~96M cells)
into, for every gene: which drugs raise or lower it, in which cell lines, which other genes move with it or opposite
to it, and which genes probably act on it or are acted on by it (probable direction, from the cell lines); vectors
for genes, drugs, drug-doses and cell lines in one space; a 2D nodal map; an Obsidian vault with a note per gene,
drug, cell line, plate and module; an interactive HTML map; a validation report that separates known from
previously unreported gene relations; and the explorer, searchable web pages over every result of the run with every
value exact (nothing capped, nothing left out for a flag), publishable on GitHub Pages.

## Stages (in order; each writes `OUT/stages/<stage>.json` when it finishes)

| Stage | Module | Reads | Writes |
|---|---|---|---|
| build | `atlas_core.cmd_build` / `stream.build` | Tahoe parquet (local or streamed) | `OUT/atlas/pseudobulk/`, `sample_map.csv`, `build_info.json` |
| effects | `atlas_core.cmd_effects` (verbatim port, method v3) | build | `OUT/atlas/effects/` |
| tensor | `tensor.run` | build, effects | `OUT/tensor/` |
| tables | `tables.run` | effects, tensor, gene metadata | `OUT/tables/` |
| embed | `embed.run` | effects, tensor, tables | `OUT/embed/` |
| reference | `reference.run` (network; cached; optional) | effects/genes.csv, gene metadata | `OUT/reference/` |
| relations | `relations.run` | embed, tables, reference (optional) | `OUT/relations/` |
| graph | `graph.run` | embed, relations | `OUT/graph/` |
| direction | `direction.run` | tensor (DDL_z, DDL_lfc, line_measured), effects (genes, drugdose, lines, line_cpm, DD_z / DD_qup / DD_qdn / DD_lfc, DD_A / DD_Az), the cell-line metadata, relations and tables/drugdoses (optional) | `OUT/direction/` |
| validate | `validate.run` | everything above | `OUT/validation/` |
| vault | `vault.run` | everything above | `OUT/vault/` |
| map | `html_map.run` | tables, embed, relations, graph, direction | `OUT/map/gene_map.html` |
| explorer | `explorer.run` | everything above (atlas/effects, tensor and every table; the map; `vault/.tahoemap-paths.json`) | `OUT/explorer/{web,data[,data_dd]}`, `OUT/explorer/manifest.json` |

Every `run(out, **opts)` function: takes the output root, logs with `common.log`, writes atomically
(`common.write_parquet/write_csv/write_json/save_npy` write a `.tmp` then `os.replace`), ends with
`common.stamp_stage(out, "<stage>", VERSION, info_dict)` and returns the info dict. Use `np.errstate` / `warnings`
to silence all-NaN warnings. Never use Python's `hash()` for seeds: use `common.stable_seed(...)`.
Dependencies allowed: numpy, pandas, pyarrow, scipy, scikit-learn, networkx (pure Python). Nothing else.
Console text goes through `common.printable(text)`: on a console or redirect whose encoding lacks a sign (a Windows
code page), ⚠ becomes '!', → '->', ≥ '>=' (`common.ASCII_FALLBACK`). A capped list keeps its items by
`common.cap_keep(alert, n)`: the n strongest and any of the n strongest without an alert beyond them.

## Indices (shared by every stage)

From `OUT/atlas/effects/` (read with `common.read_effects_index(fxd)` → dict of DataFrames):
- `genes.csv`: K rows = gK gene columns (`kind == "gene"`, rows 0..gK-1) then 3 module columns (S_PHASE,
  G2M_PHASE, PROTEASOME). Key a gene by `col` (0..gK-1), never by symbol: symbols can repeat; `label` is unique
  (`"SYM (ENSG…)"` for repeats). Columns: col, kind, token, symbol, label, pooled_cpm, median_line_cpm,
  n_lines_expressing.
- `wells.csv`: N rows (wells, plate order). Columns include sample, plate, well, slot, drug, conc, dose (str), is_dmso,
  unreliable_plate, used_in_drugdose, drugdose_row, cells_log2_vs_plate, plate_scale, position_not_correctable.
- `drugdose.csv`: Dn rows (drug-doses). Columns include drug, dose (str), conc, n_wells, wells, plates, flags
  (`"; "`-joined, exact strings of docs/method.md), n_genes_up, n_genes_down, n_sig_genes, replicate_r, targets,
  moa_fine, moa_broad, approved, S_PHASE_lfc/z, G2M_PHASE_lfc/z, PROTEASOME_lfc/z, cells_log2_vs_plate,
  unreliable_plate_only, position_not_correctable.
- `lines.csv`: L rows. cell_line_id, cell_name, Cell_ID_DepMap, Organ, drivers, driver_changes, n_cells_total,
  in_growth_analysis, wells_usable, pct_wells_usable.
- Matrices (load with `np.load(path, mmap_mode="r")`): `DD_lfc, DD_z, DD_qup, DD_qdn, DD_poseff` (Dn × K f32),
  `DD_posunc` (Dn × K bool), `W1, W2, Z` (N × K), `line_cpm, expr_mask` (L × K), `plate_scale_gene` (groups × K),
  `DD_A, DD_Az, DD_beta` (Dn × L).
- Artifact flags (`atlas_core.ARTIFACT_FLAGS`, `has_artifact(flags)`): toxic, transcription drop, cell-cycle shift,
  unreliable plate only, position not correctable, position correction uncertain, wells disagree. Soft caveats that
  are NOT artifacts: low cells (technical?), plate-row cell shift, composition shift, noisy plate (z scaled),
  position effect removed. `atlas_core.gene_flags(base, posunc, poseff, notcorr, pscale)` adds the per-gene ones.
- Significance (as the atlas): up = q_up < 0.10 and lfc ≥ log2(1.2); down symmetric.

From `OUT/tensor/` (gene-major, `np.load(..., mmap_mode="r")`):
- `DDL_lfc.npy`, `DDL_z.npy`: gK × Dn × L float16; NaN = line not measured / not expressing.
- `R.npy`: gK × N × L (corrected log2 per well × line). `line_center.npy`, `line_scale.npy`: gK × L.
- `plate_base.npy`: P × L × gK (each line's baseline log2 CPM per plate). `well_counts.npy`: N × gK raw UMI summed over
  lines; `well_umi.npy`: N; `well_line_cells.npy`, `well_line_umi.npy`: N × L.

Gene metadata (Ensembl ids): `OUT/atlas/file_index.json` → key `"gene"` lists the gene_metadata parquet
(`token_id, gene_symbol, ensembl_id`); join on `token`.

## tables (OUT/tables/) — the fold-change tables

All parquet. `README.md` in the folder documents every column. "Clean" = the gene-level flags string (drug-dose flags
plus the gene's own) contains no artifact flag (`atlas_core.has_artifact`). Flagged rows are kept: every list below
holds them in their ranked place with their flags; the readers (vault, map, look-ups, review dossiers) show them with
an alert ('⚠' + the flags in plain words) and count them, and never leave them out.

The cell-cycle shift is judged gene by gene. Per gene, a robust regression (OLS, then one Huber reweighting at 2.5
robust SDs) of its pooled lfc on the drug-doses' S-phase and G2/M module lfc, over the drug-doses whose artifact flags
are at most 'cell-cycle shift' (the gene's 'position correction uncertain' cells left out; ≥ 20 drug-doses), gives
slopes bS, bG (`genes.parquet` cc_slope_S, cc_slope_G2M). At a drug-dose flagged 'cell-cycle shift', pred = bS·S +
bG·G, with the slopes fitted again without that drug-dose when it is among the fitted ones (leave-one-out: a rank-1
downdate of the weighted fit, so the change being judged does not pull the slopes toward explaining itself), and
cc_share = |pred| / |lfc| when pred has the sign of lfc (else 0; at most 1). The shift is not the
explanation when 2·cc_share < 0.5 and |lfc|·(1 − 2·cc_share) ≥ log2 1.2 (the slopes doubled against attenuation by
noise, `tables.CC_SAFETY`): then the gene's flags read 'cell-cycle shift (explains ~N% here)', which is no artifact
flag, and the row can be clean. Otherwise the plain artifact token 'cell-cycle shift' stays and readers say e.g.
'⚠ cell-cycle shift, explains ~60% of this change'. `tables/info.json` cell_cycle_rule records the counts.
1. `genes.parquet` — one row per gene col: col, symbol, label, ensembl_id, token, pooled_cpm, median_line_cpm,
   n_lines_expressing, noise_rna (atlas NOISE_RNA_RE), corr_with_S, corr_with_G2M (Pearson over drug wells of W2),
   n_dd_up, n_dd_down, n_dd_up_clean, n_dd_down_clean, best_up_{drug,dose,fold,z,q,flags} (over all drug-doses),
   best_down_{…}, best_clean_up_{drug,dose,fold,z,q,flags,n_lines_up,pattern}, best_clean_down_{…},
   up_specificity_z_gap, down_specificity_z_gap (z gap to the next different drug among clean drug-doses),
   cc_slope_S, cc_slope_G2M (the cell-cycle slopes above).
2. `drug_effects.parquet` — "fold change relative to each drug": gene × drug-dose rows with |z| ≥ 3 or q_up < 0.1 or
   q_down < 0.1: col, symbol, dd (row), drug, dose, conc, lfc, fold, z, q_up, q_down, flags (drug-dose + gene flags),
   clean, n_lines_measured, n_lines_up, n_lines_down (per-line z ≥ 2 and |lfc| ≥ log2 1.2), lines_up, lines_down
   (cell names, strongest first, ≤ 12), pattern_up, pattern_down (atlas dose_shape over the drug's doses), cc_share
   (at a drug-dose flagged 'cell-cycle shift': the share of this change the shift would explain; else NaN).
3. `line_effects.parquet` — "fold change relative to each cell line": gene × line: col, symbol, cell_line_id,
   cell_name, baseline_cpm (line_cpm), expressed, response_sd (1.4826·MAD over clean drug-doses of DDL_lfc),
   n_dd_up, n_dd_down (clean drug-doses with per-line |z| ≥ the calibrated cut and fold ≥ 1.5 / ≤ 1/1.5),
   best_up_{drug,dose,lfc,z}, best_down_{…}; the same over ALL drug-doses with the suffix `_all`: n_dd_up_all,
   n_dd_down_all, best_{up,down}_{dd,drug,dose,lfc,z,flags,clean,cc_share}_all.
4. `drug_line_top.parquet` — per gene and direction, the 15 strongest (drug-dose, line) cells over ALL drug-doses at
   per-line |z| ≥ the calibrated cut, plus any of the 15 strongest clean cells beyond them (≤ 30): col, symbol,
   direction, rank (over all), drug, dose, cell_name, lfc, z, pooled_lfc, pooled_z, flags, clean, cc_share.
5. `drugdoses.parquet` — drugdose.csv + dd (row), salt_base, top_up, top_down (≤ 15 significant genes by z,
   "SYM (fold)").
6. `drugs.parquet` — per drug: drug, salt_base, targets, moa_fine, moa_broad, approved, doses, n_sig_by_dose,
   best_dose (most significant genes; tie → higher), lowest_active_dose, flags_by_dose, signature_r_between_doses.
7. `lines.parquet` — lines.csv + tp53_status (altered / wild type / unknown, from the cell-line metadata drivers),
   n_dd_depleted (DD_Az ≤ -3 on the drug-doses whose abundance is trusted: artifact flags such as toxic included,
   the untrusted ones not), n_dd_depleted_clean (the same on clean drug-doses), median_response (median DD_beta).
8. `plates.parquet` — plate, n_wells, doses, unreliable, plate_factor (max group factor), dmso_wells,
   failed_wells, median cells per well.
9. `wells.parquet` — wells.csv + umi_total, cpm columns are NOT here (they are `tensor/well_counts.npy`).
The gene × gene table ("relative to each gene") is `OUT/relations/gene_relations.parquet`.

## embed (OUT/embed/) — the vector space

Contexts = (drug-dose, line) pairs of *active, trustworthy* drug-doses: not `unreliable plate only`,
`position not correctable` or `wells disagree`, and either n_sig_genes ≥ `--min-active` (default 10) or
≥ `--min-active` genes at per-line |z| ≥ 5 in ≥ 2 lines. Value = DDL_z clipped to ±8, NaN → 0. Genes included = not
noise RNA, |z| ≥ 3 in ≥ `--min-responsive` (default 5) contexts, AND a significant pooled drug-dose (q < 0.1,
≥ 1.2×; one with an artifact flag counts too) or per-line |z| ≥ max(5, tables `line_z_threshold`) in ≥ 2 lines of one
trustworthy drug-dose; either counts with an artifact flag for the gene too. A gene whose evidence, pooled and
per-line, is all at drug-doses with an artifact flag for that gene (`tables/drug_effects.parquet` clean; for rows it
does not hold, the drug-dose's own flags and the gene's atlas `DD_posunc`) is in the space with
`evidence_flagged_only` = True, and every reader shows it with an alert. The three technically untrustworthy flags
still keep their drug-doses out of the fit (computing, not showing): `info.json` lists each one left out with the
reason, `drugdoses.parquet` has `fit_status`.
1. Rows centred and scaled by max(own SD, median SD). Broad components: among the first 3 components, one whose
   gene-component correlation is |r| ≥ 0.3 for ≥ max(200, 5% of genes) genes is removed (atlas programs rule).
   Logged in `broad_components.csv`.
2. Truncated randomized SVD (k = `--dims`, default 64; seed from `stable_seed`): X ≈ U S Vᵀ. Gene vector
   g = U S (principal coordinates; cosine = correlation of denoised profiles); context vector c = V; X[g, j] ≈ g · c.
3. Drug-dose vector for every drug-dose: d = S⁻¹ Uᵀ x, x = its pooled DD_z column standardised like X, over included
   genes (g · d ≈ its z). Drug vector (for drug–drug cosine) = Uᵀ x of its best trustworthy dose.
4. Line vectors: response sensitivity s_lk = slope (through 0) of the line's context vectors on the drug-doses' mean
   over lines (1 = typical, 0 = no response); baseline vector = projection of the line's log2 baseline (line_cpm vs
   the median line).
5. Split halves: compounds (salt forms merged by `tlib.salt_base`) are dealt into two halves by
   `stable_seed("half", salt_base) % 2`; steps 1-2 are repeated on each half's contexts → unit vectors per half.
Files: `gene_vectors.npy` (gK × k; NaN rows for excluded genes), `gene_unit.npy`, `gene_unit_half1/2.npy`,
`genes.parquet` (col, symbol, included, n_responsive_contexts, vector_norm, represented_fraction, n_sig_drugdoses,
n_sig_drugdoses_clean, line_evidence, line_evidence_clean, evidence_flagged_only),
`contexts.parquet`, `context_vectors.npy`, `drugdose_vectors.npy` (Dn × k), `drug_vectors.npy` + `drugs.parquet`
(trusted), `line_response_vectors.npy`, `line_baseline_vectors.npy`, `components.parquet`, `gene_row_mean/scale.npy`,
`included_cols.npy`, `singular_values.npy`, `info.json`.

## reference (OUT/reference/) — public annotations, cached, optional

Downloads (each optional; failures are logged, never fatal; `--offline` skips them): HGNC complete set
(storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt), Ensembl GRCh38 release 112 GTF
genes (ftp.ensembl.org), UniProt reviewed human function (rest.uniprot.org stream), NCBI gene_summary (human rows),
Reactome pathways GMT (reactome.org), MSigDB Hallmark GMT (data.broadinstitute.org), STRING v12 human links ≥ 400
(+ protein.info for names). Writes `annotations.parquet` (one row per gene col: col, symbol, ensembl_id, hgnc_id,
name, locus_group, locus_type, location, chrom, start, end, strand, biotype, aliases, prev_symbols, gene_groups,
entrez_id, uniprot, protein_name, function, ncbi_summary, matched_by), `gene_sets.parquet` (source, set, col,
symbol), `string_pairs.parquet` (col_a < col_b, score), `sources.json` (url, date, n rows per source).
Match Tahoe genes by Ensembl id first, then symbol, then previous symbol; alias-only matches are flagged.

## relations (OUT/relations/) — gene × gene, "relative to each gene"

Signed cosine of unit gene vectors (blockwise). For each included gene, the top 100 partners by |cos| with: cos,
abs_cos, rank, z_gene (robust z of cos over all partners of that gene), cos_half1, cos_half2, fdr (sign-concordance:
pairs selected in one half's space are scored in the other half; FDR(t) = (#disagreeing + 1) / #agreeing with
|other-half cos| ≥ t, both directions pooled, monotone; a pair's fdr is read at t = min(|cos_half1|, |cos_half2|)),
evidence ("both halves" = same sign in all three, min |half cos| ≥ 0.2 and fdr ≤ 0.10 — `reproducible`; "one half" =
|cos| ≥ 0.5 in one random half only; else "not reproduced"), genomic flags (coords_known, same_chrom, distance_bp,
same_strand, locus = ≤ 50 kb, readthrough_risk = same strand ≤ 20 kb with the 5′ gene ≥ 8× more expressed), known
flags (shared_gene_group, shared_pathway (Reactome set ≤ 300 genes or Hallmark), string_score), known (any),
both_annotated, novel_candidate (reproducible, fdr ≤ 0.05, |cos| ≥ 0.5, not known, not locus, both annotated and
placed, and only when HGNC, Ensembl, STRING and Hallmark or Reactome loaded). Files: `gene_relations.parquet`,
`fdr_curve.csv`, `info.json` (novel_assessed, novel_blocked_by). `gene_relations.parquet` also has `alert`: '' or
'⚠ ' + every reason to doubt the pair in plain words (one half only, not reproduced, read-through risk, same locus, a
gene in the space only through flagged drug-doses); every pair stays in its ranked place.

## graph (OUT/graph/) — the nodal map

Undirected kNN graph: each gene's 15 strongest partners by |cos| ≥ 0.3 with evidence "both halves", or "one half"
with |cos| ≥ 0.5 (weight |cos|, sign kept). Communities = Louvain (networkx, seed fixed, resolution 1.0); < 5 genes →
module 0 (unassigned). Arms: the sign of each member's projection on the module's first principal direction; a "−"
arm is kept only with ≥ 5 members and a mean cosine between the sides ≤ −0.2 (`arms_opposite`), else all members are
"+". Layouts: `x, y` = nodal map = t-SNE (sklearn, precomputed sparse top-90 |cos| neighbour distances 1 − |cos|,
PCA-based init) — genes doing opposite things in one pathway land together; `xs, ys` = signed map = the same on the
top-90 by signed cos (1 − cos) — opposite genes land apart. Module scores = mean z of the + arm minus the − arm.
Modules over 300 genes, or with a mean |cos| < 0.3, are split again (Louvain on their own subgraph, up to 4 levels).
Spread layouts: `xm, ym` (nodal) and `xsm, ysm` (signed; each arm of a two-armed module its own group) keep each
module's t-SNE arrangement as one block (islands of a module packed together), place the blocks by the modules'
directions in the full vector space (1 − |cos| nodal, 1 − cos signed between module directions; classical MDS refined
by SMACOF), push overlapping blocks apart, and move each gene without a module rigidly with one module (among the
modules of its 5 nearest module genes on the t-SNE map, the one it is most alike in the vector space; its offset from
the nearest of them kept); no random draws (`info.json` spread records the mixing of the grouped genes before / after,
and free_sim_tsne / free_sim_spread, the mean |cos| or cos of the genes without a module to their 5 nearest module
genes on each layout).
Files: `nodes.parquet` (col, symbol, module, arm, axis_proj, x, y, xs, ys, xm, ym, xsm, ysm, degree), `edges.parquet`,
`modules.parquet` (module, n_genes, n_plus, n_minus, top_plus, top_minus (15 per arm by |projection|, capped the same
way; a member in the vector space only through flagged drug-doses reads "SYMBOL ⚠"), centroids, drugs_up/down
(capped: the strongest plus any of the strongest without an alert beyond them; a flagged drug-dose reads "(⚠
flags)"),
responsive_lines, mean_cos_within_plus/minus, mean_cos_between_arms, arms_opposite), `module_scores.npy`
(modules × drug-doses × lines), `module_pooled_z.npy` (modules × drug-doses), `info.json`.

## direction (OUT/direction/) — probable direction

Directed edges SOURCE → TARGET from the cell lines; the method is the module docstring of `tahoemap/direction.py`,
the user-facing explanation `docs/direction.md`. Every edge comes from a test with p and a BH q (a pair without q <
0.10 in its family is no edge), has a grade (A, B, C), a sign (+1 / −1 / 0: the effect of the SOURCE's activity on
the target) and `alerts` ('' or '⚠ ' + every reason, '; '-joined); nothing that passes is dropped for doubt.
Kinds: `genotype_response`, `genotype_baseline`, `genotype_sensitivity` (recorded LoF / GoF / 'altered (any record)'
vs 'not recorded'; per driver gene with ≥ 3 lines each side; 200 label permutations, within organs when they allow
≥ 100 arrangements; q over every group of the kind, q_group within the group; written when q_group < 0.10, grade A /
B need q < 0.10 too); `null_response`, `null_baseline`, `null_sensitivity` (lines that do not express the source:
natural knockouts; towards the source's relations partners); `level`, `level_sensitivity` (the source's
lineage-adjusted natural level; grade C; `direction_clear` when |r| > |r_reverse| beyond what selecting the edge
for its strength gives: a null of two equally strong directions with the forward drawn conditional on passing the
same BH cut, the largest p over the common strength); `drug_target` (compounds of one mechanism class that target
the source, one molecule counted once under all its names; hypergeometric; grade B). Grades: A needs no co-occurrence
alert either way (another gene's altered lines on the same side, or on the other side); a tissue-confounded genotype
edge is C. The sign of a response kind is how strongly the target responds in its own direction ('strengthens' /
'weakens'; for a falling target, a deeper fall). Sensitivity kinds have target
`cells under DRUG DOSE` with `target_dd` = the drug-dose row (`drugdose.csv`), `target_col` −1.
Files: `edges.parquet` (source, source_col, target, target_col, target_dd, target_type, kind, grade, sign, reading,
group, mechanism, n_altered, n_intact, n_lines, contrast, D_raw, retained_fraction, raw_share, baseline_log2_diff, r,
r_reverse, direction_clear, p_direction, n_compounds, n_supporting, background_rate, compounds, compounds_supporting,
drug_effect, T, p, q, q_group, alerts, top_drugdoses, n_alerts), `groups.parquet` (every genotype, expression-null
and pseudo group: lines, organs, stratified, alerts, edges per kind), `controls.json` (positive: TP53 → p53 targets
with ranks, TP53 → cells under DNA-damaging drugs, KEAP1 → NRF2 targets; negative: 60 random pseudo-genotype groups
counted at the real BH cut, permuted levels; `expected_false_edges` per kind with a 95% Poisson upper bound),
`info.json` (`peak_rss_mb`: the stage's own peak, `peak_rss_how` says how it was measured), `README.md` (every
column). The stage streams the per-line tensor in gene chunks (`--mem-gb`, default 1; plain reads, no memory map);
estimated 6–7 min and 1.3–1.8 GB at 16,643 genes on 4 CPUs (`tests/test_direction.py`, generated outputs of the full
size). `cli` passes `data` = the `--data` folder (a streamed build: `OUT/hf`), else `atlas/file_index.json` names the
metadata; no result-changing option is exposed through `python -m tahoemap direction`.

**`direction_view.py` is the only reader.** The vault, the map, the look-ups, validate and the review dossiers read
the edges through `direction_view.load(out)` (None without the stage: every reader says so in one sentence and goes
on), so they show the same rows in the same order with the same words:
- `rows`: the display rows = the edges, with one test for several sources merged into one row naming them all
  (drug_target edges with the same target, compounds, mechanism, effect and result; null edges of genes absent from
  exactly the same lines); `members` = their edge ids, `sources`, `n_sources`, `has_alert`, `order`, `effect`,
  `target_drug` / `target_dose`. `edges` = edges.parquet + edge_id, has_alert, target_drug, target_dose.
- `ORDER`: grade A, B, C, then q ascending, then |contrast| descending, then p, kind, source, target.
- Look-ups (gene = col or symbol): `upstream(gene)`, `downstream(gene)` (gene targets), `cells(gene)` (sensitivity
  rows), `for_drugdose(dd)`, `sensitivity(drug)`, `drug_targets(drug)`, `for_drug(drug)`, `gene_counts(gene)`,
  `group(row)`, `counts()`; `collapse=False` gives edges.
- The cap rule: `cap(rows, n)` → (shown, n_more, n_more_alert); `more_text`, `counts_text`.
- Wording: `edge_line(row)` ('TP53 → CDKN1A  [B]  TP53 activity strengthens CDKN1A's drug response (mutation:
  response; q 0.025)  ⚠ ...'), `sign_text`, `sign_word(sign, kind)` (raises / lowers; strengthens / weakens for the
  `RESPONSE` kinds, `SIGN_RESPONSE_NOTE`), `kind_text`, `q_text`, `alert_short` (a short label per reason) /
  `alert_long`, `GRADE_WORDS`, `KIND_SHORT`, `CAVEAT`, `caveat_lines()`, `expected_text` / `CONTROLS_CAVEAT`;
  `ascii=True` forms for consoles.
Edge cap per surface: vault 12 per gene list and 15 per drug / line list, map 8 per side-panel list (3 in a hover
tooltip; 3,000 pairs in the neighbourhood view), look-ups 10 per list (`--top N` when given), all by the cap rule.

## validate (OUT/validation/)

Built-in control sets in `tahoemap/data/control_sets.json` (curated, no network: p53 induction arm + repression
(DREAM) arm, proteasome, cholesterol synthesis, UPR, heat shock, NRF2, MAPK output, interferon, histones,
ribosome biogenesis, G2/M, immediate-early), plus Hallmark/Reactome when reference ran. Per set: within-set mean
signed cosine, AUROC (within-set pairs vs random pairs of included genes) on cos and on |cos|, share of members in
the set's top module. Opposite-arm test (p53 up vs DREAM down): mean cross-arm cosine (expect < 0) and the share of
cross-arm pairs in the same module (expect high). Module enrichment (hypergeometric, BH) → module labels. Drug
check: AUROC of drug-vector cosine for same-moa_fine pairs (`drug_moa.csv` names every drug of a class; validate
version 5). Novel candidates: (a) top `novel_candidate` edges;
(b) guilt by association: genes in a module enriched for a set (q < 0.01) that are not annotated to it, ranked by
cosine to the module's annotated members. Direction (report.md section 8, metrics.json `direction`): the positive
controls with their ranks, per kind the edges written against the false edges the controls expect (⚠ when about half
or more may be false), the counts by grade, and with `--truth` the planted direction answers; on an output without
the stage, one sentence saying so (metrics `direction`: null). Files: `report.md`, `metrics.json`, `module_labels.csv`, `module_enrichment.csv`, `control_sets.csv`,
`novel_edges.csv`, `novel_members.csv`.

## vault (OUT/vault/) — Obsidian

Notes: `Genes/<chrom>/<SYMBOL>.md` (every gene col; symbol repeats → label), `Genes/<chrom>/<SYMBOL> — plates.md`
(per-plate 8×12 grids of the raw pooled CPM and of the corrected well effect W2), `Drugs/<drug> (drug).md`,
`Cell lines/<name> (line).md`, `Plates/Plate NN.md`, `Modules/Module NNN.md` + `Modules/Module NNN.canvas`,
`Indexes/…` (genes by letter, by module, drugs by mechanism, lines by organ, genes below the detection limit),
`Home.md`, `How to read this vault.md`, written notes from `tahoemap/vault_seed/`. Frontmatter emitted with
`json.dumps` values. Wikilinks bare `[[Note name]]`; drugs suffixed ` (drug)`, lines ` (line)`; unique basenames.
`.obsidian/app.json`, `graph.json` (filtered), `types.json`. Written fragments `vault_seed/genes/<SYMBOL>.md` are
spliced under the title. Direction (direction_view): every gene note has a section `## Direction (probable)` with the
tables *Upstream of this gene* and *Downstream of this gene* (gene and cells targets together; 12 per table by the cap
rule; columns for the short labels of the alerts, notes and support), a sentence in At a glance when it has arrows, and frontmatter `direction_upstream`, `direction_downstream`
(null without the stage); drug notes list the sensitivity rows at the drug's doses and its drug-target rows; line
notes list the genotype groups and natural-knockout line sets that include the line (`groups.parquet`); the generated
`Concepts/Probable direction.md` (kinds with this run's counts, grades, sign, alert, note and support labels,
controls, caveats) is
linked from Home, How to read this vault and every direction section.

## map (OUT/map/gene_map.html)

One self-contained HTML (no network): tabs nodal map / signed vector map (each with a Spread slider from the t-SNE
layout to the modules-apart layout), a k-D tour of the genes' unit vectors (a grand tour, or axis i against axis j),
three physics simulations (neighbourhood to depth 1-4, a module, all genes) and the help; colour by module, search,
click a gene → its top partners (green = same direction, red = opposite), its drug-doses up/down, lines (each line
row names the strongest drug-dose up and the strongest down). Every list keeps flagged items in their ranked place
with '⚠' + the reason and says how many carry an alert; a list capped at N adds any of the N strongest without an
alert that fall below the cut. Every preview list says "k of N shown · all N in the explorer ↗" and links into the
explorer (the JSON key `explorer_base`: the site URL; the explorer's own copy of the map rewrites it to `../`).
Probable direction (direction_view): the side panel's Upstream, Downstream and Cells lists (8 each, cap rule, show
all; the kind caveats stated once per list, notes counted); arrows between the genes shown on the neighbourhood tab
(Direction: off / arrows / + its genes) and the selected gene's arrows on the two maps; the `dir` block holds every
display row that touches a gene of the page. Nothing is dropped to fit a size (html_map VERSION 7): the stage logs
the page's size and warns above 25 MB (about 26 MB on the real data). Function snippets are 110 characters and end
in '…' when cut, with a link to the full text. Data embedded as JSON (details: `docs/DESIGN-review-and-physics.md`).

## explorer (OUT/explorer/) — searchable pages with every value

`explorer.run(out, site_url, data_url, line_dd=False, pages_max_mb=905, pooled_r=False)` writes three volumes of
static files (format and catalogue: `docs/explorer-data.md`; front end: `tahoemap/explorer_app/`):

- `web/`: the pages (`index.html`, `app.js` joined from `explorer_app/js/*.js`, `app.css`) and their data `d/`
  (core, flags, hosts, search, the gene buckets `g/`, lines `l/`, modules `m/`, direction groups `dg/`, drugs
  `dr/`, ...) and a copy of the map. Published as the branch `site` (GitHub Pages). About 0.67 GB on the real data.
- `data/`: `x/` one file per gene (per-line lfc and z, per-well values and raw counts, plate baselines) and `p/` one
  per drug-dose (every gene's pooled values). Published as the repository `<repo>-data`. About 5.2 GB.
- `data_dd/` (optional, `--with-line-dd`): `y/` per drug-dose, every gene's per-line values. About 4.3 GB.

Every data file is one line `TAHOE_SHARD("<id>","<base64 of zlib(TSF1)>");`, read by `<script>` from the same site
or the sibling folder, or by `fetch` of the text from raw.githubusercontent.com. Values are the stored bytes
(float32 pooled, float16 per line); flags are the tables stage's own strings (`tables.flag_strings`). The stage
stops, leaving the previous explorer in place, unless every `tables/drug_effects` row is reproduced exactly, every
source table's rows are all in each of its views (counts in the stamp), the self-check decodes and matches, and
every file is at most 95 MiB, every folder at most 1,000 entries and every path at most 80 characters. Above
`--pages-max-mb` the size guard moves parts from `web` to `data` (`w/`), never drops them; if moving is not enough
the stage stops. It writes `OUT/explorer.tmp` and swaps it in through `common.replace_file` (on Windows a folder
that cannot be moved is named in the message; nothing is lost). The stamp records the run id (sha256 of the other
stamps), `assets_sha` (sha256 of `tahoemap/explorer_app/**`), bytes and files per volume, the row counts, the
checks, the moves, step times and peak memory. When only `explorer_app` changed, `run` copies only the page files
(`explorer.refresh_assets`, seconds). `explorer.INVENTORY` maps every OUT file pattern to where the explorer shows
it (or why not).

Links: `tahoemap/links.py` builds the explorer's addresses for every surface (`#/gene/<label>[/<tab>]`, `#/drug/…`,
`#/dd/…`, `#/line/…`, `#/module/…`, `#/group/…`, `#/pair/A/B`); segments are percent-encoded (`links.q`). The site
URL defaults to `https://<owner>.github.io/<repo>/` of the code's `origin` remote, the data URL to
`https://raw.githubusercontent.com/<owner>/<repo>-data/main/`; `--site-url none` means no site (links name the
local files).

## CLI

`python -m tahoemap <command>`; the `tahoe` shell wrapper calls it. Commands: run, status, the stage names (build,
effects, tensor, tables, embed, reference, relations, graph, direction, validate, vault, map, explorer), the look-ups
gene, drug, line, pair, module, and review, duplicate, export (they read a finished output). `run` executes every
stage that is missing or out of date: a stage is out of date when its code VERSION changed, an earlier stage was
redone, a result-changing option differs from the one stamped (options given once are remembered in
`OUT/run_options.json`), or (reference) a source failed to load on a run with network. A stage that is new to an
output (direction or explorer, on an output finished before it existed) is missing, so `run` does it and the stages
after it, nothing earlier. `--from` / `--to` / `--redo` override the plan; `--allow-partial`, `--refresh-reference`,
`--well-tensor` / `--no-well-tensor`, `--reuse-atlas DIR` (an old tahoe_atlas.py build; recorded in
`atlas/reused_from.json`). `--redo` also removes the finished plates of `atlas/pseudobulk` before the build (the
verbatim build keeps a plate whose file list is unchanged, which is how a stopped build resumes; data files replaced
under the same names would otherwise keep the old sums). Explorer options: `--site-url` (vault, map and explorer:
they link to it; a result option of the three), `--data-url`, `--with-line-dd` / `--no-line-dd`, `--with-pooled-r` /
`--no-pooled-r` (result options of the explorer), `--pages-max-mb` (recorded; it only moves parts between the
volumes). `status` prints the explorer's bytes per volume, its row-count checks, its self-check and the size guard's
moves. `--top all` (or 0) gives every row of a look-up. `duplicate` hard-links the arrays and tables of atlas,
tensor, tables, embed, relations, graph and direction; `export` copies vault, map, tables, validation, direction,
graph, relations, embed and stages (its README names the explorer's address and data repository). `export DEST
--explorer` makes the explorer ready to publish: `DEST/site` (the web volume, as copies), `DEST/data` (hard links when on the
same disk, else copies checked against the stage's sha256), `DEST/batches/data_N.txt` (upload lists of at most 1.5
GB: one commit and one push each), `publish.ps1` / `publish.sh` (fixed refspecs: `HEAD:refs/heads/main` to
`<repo>-data`, then `export DEST --pin-data <commit>` rewrites `site/d/hosts.js` and its MANIFEST line, then
`HEAD:refs/heads/site` to the code repository; never `results`, `finalized` or the default branch), `PUBLISH.md` (the
one-time GitHub steps), `RELEASE_ASSETS.txt` and `EXPLORER_EXPORT.json`. Before writing it checks that the explorer
is current (run id, assets_sha), the pages are at most 905 MiB (0.949 GB), every file at most 95 MiB and the free
space (the copies, and the git copies the upload makes: about 0.8 x the bytes it uploads, kept loose with gc.auto 0
so no repack needs the space twice); it never runs git push.

The look-ups read the direction through `direction_view` too: `gene X` has a PROBABLE DIRECTION section (upstream,
downstream, cells under drugs), `line X` its recorded alterations and natural knockouts, `drug X` its sensitivity and
drug-target rows, `pair A B` any edge between the two (and the genes with an edge to both, by the cap rule); a name
that is no measured gene but the source of edges (a drug target such as NR3C1) gets its own arrows from `gene`, and
`pair NR3C1 GENE` gives the edges between them with every alert in full (the review dossiers' `tahoe_lookup` does the
same); every line printed through `common.printable`.

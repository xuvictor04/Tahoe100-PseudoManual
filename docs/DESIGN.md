# tahoemap — design and module contracts

This is the engineering contract between the modules of `tahoemap/`. User-facing documentation is in `README.md`
and the other files of `docs/`. Every module reads only the files listed as its inputs and writes only its own
folder under the output root `OUT` (default `<data>/tahoemap`).

## Goal

One command (`tahoe run`) turns Tahoe-100M (50 cell lines × 379 drugs × 3 doses, 14 plates × 96 wells, ~96M cells)
into, for every gene: which drugs raise or lower it, in which cell lines, which other genes move with it or opposite
to it; vectors for genes, drugs, drug-doses and cell lines in one space; a 2D nodal map; an Obsidian vault with a
note per gene, drug, cell line, plate and module; an interactive HTML map; and a validation report that separates
known from previously unreported gene relations.

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
| validate | `validate.run` | everything above | `OUT/validation/` |
| vault | `vault.run` | everything above | `OUT/vault/` |
| map | `html_map.run` | tables, embed, relations, graph | `OUT/map/gene_map.html` |

Every `run(out, **opts)` function: takes the output root, logs with `common.log`, writes atomically
(`common.write_parquet/write_csv/write_json/save_npy` write a `.tmp` then `os.replace`), ends with
`common.stamp_stage(out, "<stage>", VERSION, info_dict)` and returns the info dict. Use `np.errstate` / `warnings`
to silence all-NaN warnings. Never use Python's `hash()` for seeds: use `common.stable_seed(...)`.
Dependencies allowed: numpy, pandas, pyarrow, scipy, scikit-learn, networkx (pure Python). Nothing else.

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
`evidence_flagged_only` = True, and every reader shows it with an alert. The three technically untrustworthy flags still keep their drug-doses out of the fit (computing,
not showing): `info.json` lists each one left out with the reason, `drugdoses.parquet` has `fit_status`.
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
way; a member in the vector space only through flagged drug-doses reads "SYMBOL ⚠"), centroids, drugs_up/down (capped: the
strongest plus any of the strongest without an alert beyond them; a flagged drug-dose reads "(⚠ flags)"),
responsive_lines, mean_cos_within_plus/minus, mean_cos_between_arms, arms_opposite), `module_scores.npy`
(modules × drug-doses × lines), `module_pooled_z.npy` (modules × drug-doses), `info.json`.

## validate (OUT/validation/)

Built-in control sets in `tahoemap/data/control_sets.json` (curated, no network: p53 induction arm + repression
(DREAM) arm, proteasome, cholesterol synthesis, UPR, heat shock, NRF2, MAPK output, interferon, histones,
ribosome biogenesis, G2/M, immediate-early), plus Hallmark/Reactome when reference ran. Per set: within-set mean
signed cosine, AUROC (within-set pairs vs random pairs of included genes) on cos and on |cos|, share of members in
the set's top module. Opposite-arm test (p53 up vs DREAM down): mean cross-arm cosine (expect < 0) and the share of
cross-arm pairs in the same module (expect high). Module enrichment (hypergeometric, BH) → module labels. Drug
check: AUROC of drug-vector cosine for same-moa_fine pairs. Novel candidates: (a) top `novel_candidate` edges;
(b) guilt by association: genes in a module enriched for a set (q < 0.01) that are not annotated to it, ranked by
cosine to the module's annotated members. Files: `report.md`, `metrics.json`, `module_labels.csv`,
`module_enrichment.csv`, `control_sets.csv`, `novel_edges.csv`, `novel_members.csv`.

## vault (OUT/vault/) — Obsidian

Notes: `Genes/<chrom>/<SYMBOL>.md` (every gene col; symbol repeats → label), `Genes/<chrom>/<SYMBOL> — plates.md`
(per-plate 8×12 grids of the raw pooled CPM and of the corrected well effect W2), `Drugs/<drug> (drug).md`,
`Cell lines/<name> (line).md`, `Plates/Plate NN.md`, `Modules/Module NNN.md` + `Modules/Module NNN.canvas`,
`Indexes/…` (genes by letter, by module, drugs by mechanism, lines by organ, genes below the detection limit),
`Home.md`, `How to read this vault.md`, written notes from `tahoemap/vault_seed/`. Frontmatter emitted with
`json.dumps` values. Wikilinks bare `[[Note name]]`; drugs suffixed ` (drug)`, lines ` (line)`; unique basenames.
`.obsidian/app.json`, `graph.json` (filtered), `types.json`. Written fragments `vault_seed/genes/<SYMBOL>.md` are
spliced under the title.

## map (OUT/map/gene_map.html)

One self-contained HTML (no network): tabs nodal map / signed vector map (each with a Spread slider from the t-SNE
layout to the modules-apart layout), a k-D tour of the genes' unit vectors (a grand tour, or axis i against axis j),
three physics simulations (neighbourhood to depth 1-4, a module, all genes) and the help; colour by module, search,
click a gene → its top partners (green = same direction, red = opposite), its drug-doses up/down, lines. Every list
keeps flagged items in their ranked place with '⚠' + the reason and says how many carry an alert; a list capped at N
adds any of the N strongest without an alert that fall below the cut. Data embedded as JSON
(details: `docs/DESIGN-review-and-physics.md`).

## CLI

`python -m tahoemap <command>`; the `tahoe` shell wrapper calls it. Commands: run, status, the stage names (build,
effects, tensor, tables, embed, reference, relations, graph, validate, vault, map) and the look-ups gene, drug, line,
pair, module. `run` executes every stage that is missing or out of date: a stage is out of date when its code
VERSION changed, an earlier stage was redone, a result-changing option differs from the one stamped (options given
once are remembered in `OUT/run_options.json`), or (reference) a source failed to load on a run with network.
`--from` / `--to` / `--redo` override the plan; `--allow-partial`, `--refresh-reference`, `--well-tensor` /
`--no-well-tensor`, `--reuse-atlas DIR` (an old tahoe_atlas.py build; recorded in `atlas/reused_from.json`).

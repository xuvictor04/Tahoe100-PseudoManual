# Method v3: what changed and why


The first full run on the real data (95.6M cells, 1,344 wells, 50 lines) was checked line by line before any agent
ran. The bookkeeping and the arithmetic were exact, and the effects agree with Tahoe's own DESeq2 table (median
per-gene Spearman 0.63 / Pearson 0.83 on the plates compared, 0.84 / 0.90 with our position correction added back;
93% of effects >= 1.2x have the same sign). But the data have technical structure the method did not remove, and it
would have misled the agents. Version 3 of the method fixes it in all three scripts (one definition each, used
identically by the atlas and the gene panel / MTAP trial).

**Plates 2 and 3 were too noisy.** They hold the 0.5 and 5 uM doses of the plate 1-3 layout (about 16% of the
drug-doses). Their z-scores were about 1.4x and 2x too wide (18% and 36% of drug wells beyond |z| 1.96, against
5-12% on the other plates), because whole plate rows lost cells or sequencing depth. As a result they gave 49% of the
panel's calls and 43% of the atlas's significant gene calls. *Fix:* a plate factor per plate and dose: the group's
spread over that of the same dose on the other reliable plates, median over genes. Every expression z on that plate
(genes, modules, pathway scores, the p53 contrast) is divided by it; the growth (relative abundance) z are not.
A gene that is noisier on a plate than that plate's median gene (its own spread ratio > 1.3x the factor; in the
first run's numbers PSMD10 and several panel genes were 2-3x their peers on plate 2, the median panel gene ~1.45x)
gets its own, larger factor (ratio / 1.3); it never gets a smaller one. Whether the growth z need a factor too,
the quality angle's `calibration_growth_by_plate.csv` shows. The factor only ever widens (never below 1), so a
quiet plate is never sharpened; part of plate 3's spread may be real activity of its targeted-oncology drugs. The
fold changes are unchanged. Flag: `noisy plate (z scaled)` (factor > 1.2). The factors are in
`effects/plate_scale.csv` and the panel's `results/plate_scale.csv`.

**Plate 13 does not reproduce.** It is a mixed-dose rescue plate (all three doses, plus re-runs of plate 1's failed
wells; DMSO at B11/B12, not H11/H12). Its replicate pairs agree at median r -0.06, against +0.30 for pairs on two
other plates (strong drug-doses: +0.58, none negative). Topotecan 5 uM on plate 9 vs plate 13: r -0.19. Ribociclib,
which sits only there, shows no G1 arrest (S-phase z +0.31 at 5 uM; palbociclib 0.5 uM: -8.9). *Fix:* plate 13 is an
unreliable plate by default (`--unreliable-plates plate13`, or `none`, or another list, on every script). Its wells
are still computed and listed, but they stay out of the reference spread and the plate-factor peers. A drug-dose
that also has a well on a reliable plate uses only those wells; one that sits only on plate 13 keeps it and is
flagged `unreliable plate only`.

**Strong neighbours leaked into the position correction.** The plates share four layouts, so 361 of 367 drugs sit
at the same well position at every dose. A drug's position correction is the median of the other drugs' wells at
that position (about 11 wells of about 4 drugs). When one of those drugs is strong, its effect is subtracted as if
it were positional. Example: sodium salicylate appeared to lower TFRC to 0.64x at all three doses, a mirror image
of dinaciclib, which shares its well position. The same layout also means that dose consistency does not rule out a
position artifact; agreement at a different position is the stronger test. *Fix:* a second pass uses only the clean
donors for each gene (wells whose first-pass |z| < 3). With fewer than 3 clean donors that gene is not corrected in
that well and is flagged `position correction uncertain`.

**Some wells could not be corrected at all.** 15 drug wells had fewer than 3 other-drug wells at their position:
Adagrasib 0.05 uM sits at H10 on 13 plates (221 significant genes at 50 nM, none at 0.5 uM; CASP3 0.85x with
z -12.9), and on plate 13 carbidopa and ribociclib 0.05 uM sit at H11/H12. *Fix:* flag `position not correctable`.

**Library composition.** Effects are CPM ratios: when a few genes take a large share of a well's reads, all others
read lower. TAK-901 5 uM read about 0.5 log2 lower than Tahoe's DESeq2 table for nearly all genes (Ouabain 5 uM
about 0.25). *Fix:* a median-of-ratios shift per well and cell line (the median residual of the genes the line
expresses at >= 10 CPM, as in DESeq2), subtracted from every gene, is saved as `effects/composition_shift.parquet`.
The gene panel and the MTAP trial take it from the computed atlas (`<data>/atlas`; `--atlas DIR` for another one,
`--atlas none` for none), so run the atlas first; without it they say `composition normalisation not applied`. Flag
`composition shift` when a drug-dose's shift is >= 0.2 log2: its effects are relative to the median gene, and a raw
CPM view would differ.

**The 'toxic' flag was mostly noise.** It meant "the well kept less than half the plate's cells". Replicate wells of
one drug-dose did not agree on it (Spearman -0.19; of 14 pairs with one well below that line, none had the other
below). Whole plate rows lost cells (plate 2 row D: all 12 wells, 17 of the 49 'toxic' drug-doses were on plate 2).
*Fix:* `toxic` now means cell loss that no higher dose of the same drug recovers from, judged against the plate row
where that row is itself shifted (> 0.8 log2; a row of toxic 5 uM neighbours is no reason to subtract their loss,
which had relabelled e.g. bortezomib and topotecan 5 uM), and, when the drug-dose has several used wells, seen in
its best well too (selinexor 5 uM: one well -2.5, the other +0.3: not toxic). At the top dose there is no higher
dose to check and most drug-doses have one well, so `toxic` there still rests on one well's cell count; duplicate
wells (plates 6 and 14) agree poorly on cell loss, so treat it as weak evidence alone. Other cell loss is flagged
`low cells (technical?)` (not confirmed, not necessarily technical: antimitotics kill more at a lower dose), and a
shifted plate row `plate-row cell shift`.
`transcription drop` is judged against the plate row too, and `cell-cycle shift` looks at both S and G2/M. The p53
reference doses and the re-expression gating use the new `toxic`.

**Statistics that were too optimistic.**
- Atlas `level_vs_growth` and `proliferation_dependent_drugs` drew 'hits' from inert drug-doses (170 PSMD10
  level-vs-growth hits at q < 0.1, mostly single wells). They now use an empirical null: the robust centre and
  spread of the statistic over the reliable drug-doses.
- Biomarkers: an inert drug-dose could reach more than 3,000 'marker' genes (Aliskiren 0.5 uM: 18 significant genes,
  3,397 markers). Each gene's correlation is now calibrated against its own spread over drug-doses (markers need
  calibrated |z| >= 3). A `replicated` column (the growth pattern agrees between doses or wells, r >= 0.3) ranks
  `selective_drugs` first.
- `feature_response`: a Welch t on 3-line groups gave q ~1e-16 for tiny differences. The group variance is now
  floored at the rest's, and `small_group` marks groups of <= 4 lines.
- Replicates are reported by pair type (`same position, other plate`, `different position`, `same plate`,
  `unreliable plate`), with a same-position null, each drug-dose counted once (Adagrasib 0.05 uM's 16 wells gave
  78 of the 170 same-position pairs); pairs with a well that had no position correction are reported apart. The
  single median r 0.18 had pooled these. Few drug-doses have a replicate at a different position on reliable
  plates (on the real layout 9 drug-doses of Afatinib, Binimetinib and Trametinib), and the briefs name them.
- `lowest_active_dose` needs every higher dose to be active too; otherwise it reads `low dose only (noise?)`
  (18 drugs were 'active' only at 0.05 uM).
- The genes angle's inducible / repressible lists hold at most 25 genes per drug-dose and no noise RNAs. Before,
  Idarubicin 5 uM and TAK-901 5 uM filled 378 and 375 of the 500 rows.
- Gene panel: the p53 WT-vs-altered table has a `pattern` column. `WT induction` needs the WT lines to rise >= 1.2x
  and the all-line P53 score to go up; otherwise it is `relative (altered lines fall)` (read it from the run's
  `p53_wt_vs_altered.csv`: the composition normalisation moves exactly the drug-doses whose altered lines seemed to
  fall). Re-expression is compared with the lines deleted for the gene in the same wells (pure ambient RNA; the
  expressing lines when fewer than 2 are deleted): it needs >= 2 lines up and a dose pattern, and reads
  `lost lines read ambient only: not interpretable` when the lost lines' untreated level is at the ambient floor
  (whether or not any line is deleted for the gene). Pathway scores average the members' z, each on its own noise
  scale, so 6-line CASP5 no longer drives INFLAMMASOME. The crosslinks' shared-drug count is compared with an
  expectation stratified by drug activity: 38 shared drugs had looked like ~3x the ~12 'expected', but strong drugs
  are in every list, and the stratified expectation is about 34.
- The `plate DMSO offset` flag is gone (it was on 28% of best-dose rows and never changed a value). The
  `plate_dmso_offset` column stays.

**Briefs.** The briefs now state the facts above from the data. They list the plates with a factor > 1.2 and the
unreliable plates with their replicate r. They say where DMSO sits, which drug-doses have no data (their only well
failed), which lines have usable expression in < 25% of wells, that ~20 drugs appear twice as salt forms, that
cytostatic drugs deplete lines only weakly at 24 h, and how wide the gap behind the MTAP-null cut is. The focus
briefs no longer assert earlier findings: they say the earlier MTAP / Gankyrin analysis was inconclusive and ask
the agent to test every candidate rise against its dose pattern, flags, cell cycle and the whole proteasome. Both
bundles include the briefs.

**What changes in the numbers.** Every z, FDR, call and flag can move compared with earlier runs. Expect plates 2 and
3 to lose many calls, drug-doses with a plate-13 well to rest on their other wells, position-corrected values to
change where a strong drug shares the position, composition-shift drug-doses to move by up to ~0.5 log2 for all
genes, and `toxic` to become rarer. Unchanged: the build and extract (the cells are not read again), failed wells,
`--min-cells`, the expression rules, the MTAP-null call and the TP53 annotation. **MTAP / Gankyrin:** the
conclusion is expected to stay that there is no clean inducer. MTAP had no convincing inducer (its one call,
clobetasol 0.05 uM 1.30x, is inconsistent across doses). PSMD10 mRNA does rise 1.3-2.2x with about 15 drug-doses
(dinaciclib 5 uM, NG25 5 uM, XRK3F2 0.5 uM, ...), and Tahoe's own table ranks the same drug-doses on top, but nearly
all of them come with toxicity, a transcription drop or the whole proteasome. Read the v3 tables before restating it.

**Flags** (the `flags` column of every drug-dose table; the strings are exact, one definition in both scripts):

| Flag | Means | What to do |
|---|---|---|
| `toxic` | < -1 log2 cells vs the plate (and after subtracting the plate row's median where the row itself moved > 0.8 log2), the best used well < -0.5 too, and no higher dose of the drug recovering to >= -1 | Cytotoxicity: effects partly reflect dying or stressed cells. At the top dose it rests on one well's cell count (duplicate wells agree poorly): weak evidence alone |
| `low cells (technical?)` | < half the plate's cells, but not confirmed as dose-consistent loss beyond its row | Not confirmed: a row that lost cells, a non-monotonic dose response (antimitotics), toxic neighbours, or a well that did not replicate. Do not call the drug toxic from it alone; a drug-dose with many significant genes is still active: read its effects with the cell-loss caveat |
| `plate-row cell shift` | The other drug wells of its plate row are shifted together (cells by > 0.8 log2 either way, or UMI per cell < -0.4 log2) | Technical: confirm on another plate |
| `transcription drop` | Genes or UMIs per cell fall vs the plate and its row (< -0.3 / < -0.5 log2) | Global shutdown: many genes fall together |
| `cell-cycle shift` | S or G2/M module moved > 0.5 log2 (or > 0.25 with \|z\| >= 4) | Cycle genes follow the cell-cycle mix |
| `composition shift` | The drug-dose's composition shift is >= 0.2 log2 | Effects are relative to the median gene |
| `noisy plate (z scaled)` | Plate factor > 1.2 (the group's, or the gene's own where it is noisier there): its z were divided by it | Fold changes are unchanged; prefer agreement on another plate |
| `unreliable plate only` | Only wells on an unreliable plate (default plate 13) | Unconfirmed |
| `position correction uncertain` | (per gene) < 3 clean other-drug wells at the position: not corrected | Could be positional |
| `position not correctable` | < 3 other-drug wells at the position at all | No position correction: unconfirmed |
| `position effect removed` | (per gene) the correction moved it by > 0.2 log2 | Check that the corrected value still holds |
| `wells disagree` | >= 2 wells whose z over the top 500 genes correlate at r < 0.1, with >= 100 significant genes | Not replicated |
| `whole proteasome up/down` | (gene panel, PSMD10) the whole proteasome moves with it | Not Gankyrin-specific |

**New columns and files.**
- Atlas `effects/`: `composition_shift.parquet` (sample, cell_line_id, shift_log2), `plate_scale.csv` (plate, dose,
  n_wells, factor_raw, factor, group), `posunc.npy` / `DD_posunc.npy` (position correction uncertain per well /
  drug-dose x gene), `DD_poseff.npy` (position effect removed), `plate_scale_gene.npy` (each gene's z divisor per
  plate group). `wells.csv` adds `composition_shift_log2`, `unreliable_plate`, `plate_scale` / `plate_scale_group_id`,
  the plate-row medians (`row_cells_log2`, `row_umi_per_cell_log2`, `row_genes_per_cell_log2`),
  `cells_log2_beyond_row`, `position_clean_donors_median` and `position_not_correctable`. `drugdose.csv` adds
  `composition_shift_log2`, `plate_scale`, `unreliable_plate_only`, `position_not_correctable`, `replicate_r`,
  `n_wells_all` / `wells_left_out`, `cells_log2_best_well` and `cells_log2_best_higher_dose`. `complete.json` says
  version 3; `angles/complete.json` is written when `angles` finishes (`tahoe status` needs it).
- Atlas angles: `quality/calibration_by_plate.csv` (% of the measured |z| > 1.96 and > 3 per plate and dose, before
  and after the factors), `quality/calibration_by_plate_gene.csv` (the focus genes and the genes widened most beyond
  their plate's factor), `quality/replicate_by_plate_pair.csv`, `quality/replicates.csv` with `pair_type`,
  `quality/composition_shifts.csv`, `quality/position_not_correctable_wells.csv`; `small_group` in
  `line_response/feature_response_top.csv`; `replicated` in the biomarker tables; `plate_scale_gene` in the focus
  tables.
- Gene panel `results/`: `run_info.json` (method_version 3 and the run's settings; written last, read by
  `tahoe status`), `plate_scale.csv`, `plate_scale_by_gene.csv`, `replicate_pairs.csv`, `well_effects.csv.gz` (per
  well: unreliable plate, plate factor, composition shift, and every gene's and score's log2FC and z, the value
  before the position correction and its position state), `pattern` in `p53_wt_vs_altered.csv`. The MTAP trial
  writes `run_info.json`, `plate_scale.csv` and `plate_scale_by_gene.csv` too.
- Every drug-dose table: `plate_scale_gene` (the gene's own z divisor) and `cells_log2_best_well` (the input of
  `toxic`). A gene measured in fewer than 5 lines in a typical well (real CASP5: 4 colorectal lines in nearly every
  well) is computed from the lines it has; other genes need >= 5 measured lines per well, as in the atlas.
- `README_effects.md` (atlas) and `results/README_columns.txt` (panel) describe every column.


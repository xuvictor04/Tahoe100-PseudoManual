---
symbol: "GAL"
type: "gene"
col: 919
ensembl_id: "ENSG00000069482"
name: "galanin and GMAP prepropeptide"
location: "11q13.2"
module: 152
arm: "+"
pooled_cpm: 4.26
n_lines_expressing: 23
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# GAL

*galanin and GMAP prepropeptide* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.54× (z +12.1, q 3e-31, up in 11 of 12 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +4.6, q 4e-04, up in 9 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.103×; ⚠ cell-cycle shift, explains ~82% of this change).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02476]] (+0.52, fdr 3e-04), [[MAGEA3-DT]] (+0.49, fdr 1e-04), [[EIF5AL1]] (+0.48, fdr 4e-05); moves opposite to [[LINC00649]] (-0.40, fdr 2e-04), [[CREBL2]] (-0.40, fdr 1e-04), [[ABHD4]] (-0.39, fdr 1e-04).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[P2RX5]] → it (grade B ⚠); 3 go from it, the strongest it → [[P2RX5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **8.54×** | +12.1 | 3e-31 | 11/12 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.26×** | +11.5 | 4e-28 | 7/7 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.62×** | +8.0 | 2e-13 | 7/8 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.00×** | +6.2 | 7e-08 | 11/18 (SW480, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.86×** | +5.7 | 1e-06 | 12/14 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **2.04×** | +5.7 | 1e-06 | 9/21 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **2.35×** | +4.8 | 1e-04 | 9/14 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +4.6 | 4e-04 | 9/20 (NCI-H2347, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **2.22×** | +4.3 | 9e-04 | 9/16 (LoVo, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +4.3 | 0.001 | 6/20 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.045 | 2/21 (PANC-1, NCI-H2347) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.3 | 0.048 | 4/17 (NCI-H2347, SW480, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.95×** | +3.2 | 0.061 | 3/9 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.74×** | +3.1 | 0.075 | 10/21 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.71×** | +3.0 | 0.087 | 9/21 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.087 | 7/21 (PANC-1, BT-474, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.103×; ⚠ cell-cycle shift, explains ~82% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.44 | 4 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 29.7× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -10.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[NCI-H1792 (line)]] | alt | 8.96 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +8.9) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[SW480 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.66× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.424 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02476]] | +0.52 | +0.26 / +0.48 | both halves | 3e-04 |  |
| [[MAGEA3-DT]] | +0.49 | +0.32 / +0.52 | both halves | 1e-04 |  |
| [[EIF5AL1]] | +0.48 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[SLC25A19]] | +0.48 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[CENPV]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[EPOP]] | +0.48 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[SLC1A1]] | +0.47 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[NPTX2]] | +0.47 | +0.33 / +0.39 | both halves | 1e-04 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[FABP5]] | +0.47 | +0.48 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[DUSP2]] | +0.46 | +0.46 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[FAR2]] | +0.46 | +0.32 / +0.35 | both halves | 2e-04 |  |
| [[MDGA2]] | +0.46 | +0.41 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00649]] | -0.40 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[CREBL2]] | -0.40 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[ABHD4]] | -0.39 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[EFCAB7]] | -0.39 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[EPHX2]] | -0.37 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[LPIN3]] | -0.37 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[JAKMIP2-AS1]] | -0.37 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[ATF6B]] | -0.37 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[HSD17B7P2]] | -0.37 | -0.37 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RX5]] | B | P2RX5 activity raises GAL's level | lines that do not express P2RX5 (15) vs lines expressing it (35) | 2.51× lower at baseline in the lines without P2RX5 | 0.007 | ⚠ within organs, on part of the lines; also absent: C1orf115, LIMS2, PALM |
| [[C1orf21]] | B | C1orf21 activity lowers GAL's level | lines that do not express C1orf21 (9) vs lines expressing it (41) | 1.94× higher at baseline in the lines without C1orf21 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, GALNT8 |
| [[GPR63]] | B | GPR63 activity raises GAL's level | lines that do not express GPR63 (10) vs lines expressing it (40) | 2.31× lower at baseline in the lines without GPR63 | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF618, BEX3, OLFM2 |
| [[SLC1A1]] | B | SLC1A1 activity lowers GAL's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 2.54× higher at baseline in the lines without SLC1A1 | 0.075 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[IKZF3]] | C | IKZF3 activity raises GAL's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.81× lower at baseline in the lines without IKZF3 | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RX5]] | B | GAL activity raises P2RX5's level | lines that do not express GAL (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without GAL | 0.003 | ⚠ within organs, on part of the lines; also absent: HEYL, ACP7, SEC14L4 |
| [[AGMAT]] | B | GAL activity raises AGMAT's level | lines that do not express GAL (27) vs lines expressing it (23) | 1.38× lower at baseline in the lines without GAL | 0.052 | ⚠ within organs, on part of the lines; also absent: HEYL, ACP7, SEC14L4 |
| [[PRR16]] | B | GAL activity lowers PRR16's level | lines that do not express GAL (27) vs lines expressing it (23) | 2.08× higher at baseline in the lines without GAL | 0.083 | ⚠ within organs, on part of the lines; also absent: HEYL, ACP7, SEC14L4 |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.405). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.2, 26.6); signed map (33.0, 45.4). **Vector** length 38.2, 8.50% of its response variance represented; |z| ≥ 3 in 368 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.6 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.9 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.8 | +1.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | galanin and GMAP prepropeptide |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:68,683,779-68,691,175 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GMAP, GAL-GMAP, GLNN; previously GALN |
| Gene groups (HGNC) | Neuropeptides |
| Hallmark sets | UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P22466](https://www.uniprot.org/uniprotkb/P22466) (Galanin peptides):

> Endocrine hormone of the central and peripheral nervous systems that binds and activates the G protein-coupled receptors GALR1, GALR2, and GALR3. This small neuropeptide may regulate diverse physiologic functions including contraction of smooth muscle of the gastrointestinal and genitourinary tract, growth hormone and insulin release and adrenal secretion.

**Summary**, from NCBI Gene [51083](https://www.ncbi.nlm.nih.gov/gene/51083):

> This gene encodes a neuroendocrine peptide that is widely expressed in the central and peripheral nervous systems and also the gastrointestinal tract, pancreas, adrenal gland and urogenital tract. The encoded protein is a precursor that is proteolytically processed to generate two mature peptides: galanin and galanin message-associated peptide (GMAP). Galanin has diverse physiological functions including nociception, feeding and energy homeostasis, osmotic regulation and water balance. GMAP has …

**Accessions** — [HGNC:4114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4114) · Entrez [51083](https://www.ncbi.nlm.nih.gov/gene/51083) · UniProt [P22466](https://www.uniprot.org/uniprotkb/P22466) · Ensembl [ENSG00000069482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069482)

## Data

Gene col 919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 919); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 919]; `tensor/DDL_lfc|DDL_z.npy` [919]; `embed/gene_vectors.npy` [919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 919 or target_col == 919). Every well: [[GAL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

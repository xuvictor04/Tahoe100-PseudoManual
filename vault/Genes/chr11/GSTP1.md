---
symbol: "GSTP1"
type: "gene"
col: 1397
ensembl_id: "ENSG00000084207"
name: "glutathione S-transferase pi 1"
location: "11q13.2"
module: 48
arm: "+"
pooled_cpm: 87.44
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# GSTP1

*glutathione S-transferase pi 1* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.94× (z +7.9, q 2e-12, up in 42 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +5.4, q 2e-05, up in 37 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 11.4×, NCI-H1573 12.5×, MIA PaCa-2 6.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 8.04×, MIA PaCa-2 5.89×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 5.15×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCRQ]] (+0.59, fdr 1e-05, ⚠ UQCRQ in the vector space only through flagged drug-doses), [[ATP5MF]] (+0.59, fdr 7e-06), [[NDUFA4]] (+0.59, fdr 4e-05), [[COX8A]] (+0.58, fdr 3e-05); moves opposite to [[INO80E]] (-0.54, fdr 1e-04), [[DCTD]] (-0.50, fdr 1e-04), [[CDC16]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → cells under [[Imiquimod (hydrochloride) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1397.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 11.4×, NCI-H1573 12.5×, MIA PaCa-2 6.65×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 8.04×, MIA PaCa-2 5.89×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 5.15×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **4.94×** | +7.9 | 2e-12 | 42/44 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **4.00×** | +7.3 | 6e-11 | 38/38 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.4 | 2e-05 | 37/44 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.83×** | +5.3 | 2e-05 | 38/40 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **2.10×** | +4.1 | 0.005 | 40/43 (SW 900, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.5 | 0.039 | 33/42 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.89×** | +3.5 | 0.039 | 34/43 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.79× | +3.1 | 0.15 | 29/45 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.304× | -3.4 | 0.20 | 40/44 (SHP-77, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.309× | -3.4 | 0.20 | 38/44 (SK-MEL-2, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 60.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.89× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 118 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.4× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A549 (line)]] | wt | 85.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.5× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 225 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 123 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 85.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRQ]] ⚠ | +0.59 | +0.51 / +0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MF]] | +0.59 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[NDUFA4]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 | pathway: Cellular response to chemical stress |
| [[COX8A]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 | pathway: Cellular response to chemical stress |
| [[MIF]] | +0.56 | +0.37 / +0.59 | both halves | 9e-05 |  |
| [[ATP5F1E]] | +0.54 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[NDUFB11]] ⚠ | +0.53 | +0.49 / +0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.52 | +0.37 / +0.58 | both halves | 9e-05 |  |
| [[UQCR10]] ⚠ | +0.52 | +0.50 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX7B]] | +0.51 | +0.47 / +0.54 | both halves | 2e-05 | pathway: Cellular response to chemical stress |
| [[COX7C]] | +0.51 | +0.35 / +0.55 | both halves | 1e-04 | pathway: Cellular response to chemical stress |
| [[B2M]] | +0.51 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[NDUFA1]] | +0.50 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[SRP14]] | +0.50 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TPI1]] | +0.50 | +0.34 / +0.59 | both halves | 1e-04 | STRING 427 |

## Genes that move opposite

*47 of its nearest partners move opposite, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80E]] | -0.54 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[DCTD]] | -0.50 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[CDC16]] | -0.50 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[ZNF783]] ⚠ | -0.49 | -0.33 / -0.47 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MAPKAPK3]] | -0.49 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[MDM4]] | -0.48 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[MTG1]] | -0.48 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[ZNF598]] | -0.48 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[CPSF1]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[BRD9]] | -0.47 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[UVSSA]] | -0.47 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[DDX51]] | -0.47 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[PDCD2]] | -0.47 | -0.27 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Imiquimod (hydrochloride) (drug)]] 5 µM | C | GSTP1 activity raises the cells' numbers under Imiquimod (hydrochloride) 5 µM (protects the cells) | lines that do not express GSTP1 (5) vs lines expressing it (43) | the lines without GSTP1: 0.71× the cells of the other lines | 0.012 | ⚠ tissue-confounded; across organs; also absent: MARVELD1 |
| cells under [[Glycyrrhizic acid (drug)]] 0.5 µM | C | GSTP1 activity raises the cells' numbers under Glycyrrhizic acid 0.5 µM (protects the cells) | lines that do not express GSTP1 (5) vs lines expressing it (43) | the lines without GSTP1: 0.75× the cells of the other lines | 0.039 | ⚠ tissue-confounded; across organs; also absent: MARVELD1 |
| cells under [[Mozavaptan (drug)]] 0.5 µM | C | GSTP1 activity raises the cells' numbers under Mozavaptan 0.5 µM (protects the cells) | lines that do not express GSTP1 (5) vs lines expressing it (43) | the lines without GSTP1: 0.75× the cells of the other lines | 0.043 | ⚠ tissue-confounded; across organs; also absent: MARVELD1 |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM | C | GSTP1 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (protects the cells) | lines that do not express GSTP1 (5) vs lines expressing it (43) | the lines without GSTP1: 0.71× the cells of the other lines | 0.058 | ⚠ tissue-confounded; across organs; also absent: MARVELD1 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 5 µM | C | GSTP1 activity lowers the cells' numbers under Irinotecan (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express GSTP1 (5) vs lines expressing it (43) | the lines without GSTP1: 1.22× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; also absent: MARVELD1 |
| cells under [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM | C | GSTP1 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express GSTP1 (5) vs lines expressing it (43) | the lines without GSTP1: 0.86× the cells of the other lines | 0.091 | ⚠ tissue-confounded; across organs; also absent: MARVELD1 |

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.7, -22.4); signed map (-35.5, 10.5). **Vector** length 53.3, 20.1% of its response variance represented; |z| ≥ 3 in 485 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | +1.8 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +0.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.5 | +0.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -5.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -5.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -4.9 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | +0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase pi 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,583,742-67,586,656 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GSTP; previously FAEES3, GST3 |
| Gene groups (HGNC) | Soluble glutathione S-transferases |
| Reactome | 11 pathways, smallest: Paracetamol ADME; Glutathione conjugation; Detoxification of Reactive Oxygen Species |
| Matched by | ensembl_id |

**Function**, from UniProt [P09211](https://www.uniprot.org/uniprotkb/P09211) (Glutathione S-transferase P):

> Catalyzes conjugation of reduced glutathione to a wide number of exogenous and endogenous hydrophobic electrophiles. Involved in the formation of glutathione conjugates of both prostaglandin A2 (PGA2) and prostaglandin J2 (PGJ2). Participates in the formation of novel hepoxilin regioisomers. Acts as a negative regulator of ferroptosis by mediating glutathione conjugation and detoxification of 4-hydroxynonenal (4-HNE) reactive aldehyde. Negatively regulates CDK5 activity via p25/p35 …

**Summary**, from NCBI Gene [2950](https://www.ncbi.nlm.nih.gov/gene/2950):

> Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene encoding active, functionally different GSTP1 variant proteins that are thought to function in …

**Accessions** — [HGNC:4638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4638) · Entrez [2950](https://www.ncbi.nlm.nih.gov/gene/2950) · UniProt [P09211](https://www.uniprot.org/uniprotkb/P09211) · Ensembl [ENSG00000084207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084207)

## Data

Gene col 1397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1397); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1397]; `tensor/DDL_lfc|DDL_z.npy` [1397]; `embed/gene_vectors.npy` [1397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1397 or target_col == 1397). Every well: [[GSTP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

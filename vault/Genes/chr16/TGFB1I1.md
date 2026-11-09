---
symbol: "TGFB1I1"
type: "gene"
col: 6441
ensembl_id: "ENSG00000140682"
name: "transforming growth factor beta 1 induced transcript 1"
location: "16p11.2"
module: 13
arm: "+"
pooled_cpm: 4.9
n_lines_expressing: 37
n_dd_up: 5
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# TGFB1I1

*transforming growth factor beta 1 induced transcript 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.54× (z +8.0, q 5e-13, up in 9 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.77× (z +3.5, q 0.059, up in 6 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.220× (z -13.5, q 5e-39, down in 32 of 33 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.353× (z -13.2, q 3e-37, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSPG4]] (+0.55, fdr 1e-05), [[COL6A3]] (+0.54, fdr 3e-05), [[LIMD2]] (+0.54, fdr 1e-05); moves opposite to [[TMTC2]] (-0.47, fdr 6e-05), [[BCL2L14]] (-0.47, fdr 2e-04), [[NCK1-DT]] (-0.47, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GPR173]] → it (grade B ⚠); 7 go from it, the strongest it → [[PLP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.0 | 5e-13 | 9/12 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.25×** | +6.9 | 1e-09 | 17/35 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +4.9 | 1e-04 | 8/19 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.77×** | +3.5 | 0.059 | 6/28 (RKO, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.72×** | +3.3 | 0.094 | 6/21 (J82, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.42× | +3.2 | 0.14 | 5/22 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.40× | +3.0 | 0.19 | 8/27 (HS-578T, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.220×** | -13.5 | 5e-39 | 32/33 (J82, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.353×** | -13.2 | 3e-37 | 28/31 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.234×** | -13.0 | 3e-36 | 28/32 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.290×** | -11.1 | 2e-26 | 30/33 (J82, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.321×** | -10.2 | 4e-22 | 27/33 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.485×** | -9.1 | 6e-18 | 24/29 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.365×** | -9.0 | 2e-17 | 28/34 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -7.2 | 4e-11 | 22/26 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.456×** | -7.0 | 2e-10 | 21/27 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.234×** | -6.8 | 6e-10 | 25/31 (RKO, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -6.7 | 1e-09 | 18/32 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -6.7 | 1e-09 | 21/32 (H4, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.594×** | -6.6 | 2e-09 | 20/33 (HOP62, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.490×** | -6.4 | 7e-09 | 20/28 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.499×** | -6.0 | 9e-08 | 19/29 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.505×** | -5.9 | 2e-07 | 18/32 (RKO, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.561×** | -5.2 | 9e-06 | 21/32 (HS-578T, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.351×** | -4.9 | 3e-05 | 14/31 (HOP62, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.685×** | -4.8 | 5e-05 | 17/34 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.69 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 8.84 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0643× (z -14.1) |
| [[J82 (line)]] | alt | 11.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -13.8) |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -10.1) |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.153× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.169× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 6.68 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0864× (z -10.0) |
| [[A-172 (line)]] | wt | 15.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -11.1) |
| [[H4 (line)]] | wt | 10.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0340× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -9.0) |
| [[PANC-1 (line)]] | alt | 4.56 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0980× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 9.47 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0709× (z -10.5) |
| [[A549 (line)]] | wt | 7.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 6.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0462× (z -16.0) |
| [[C32 (line)]] | wt | 4.53 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0751× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 8.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0744× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -11.4) |
| [[SW48 (line)]] | wt | 4.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -8.5) |
| [[A-427 (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSPG4]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[COL6A3]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[LIMD2]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 | same gene group |
| [[PLSCR3]] | +0.52 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[KCTD10]] | +0.49 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[UCK1]] | +0.49 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[HECTD3]] | +0.49 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[DYNC1I2]] | +0.48 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[NELFE]] | +0.48 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[PWP1]] | +0.48 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[DLST]] | +0.47 | +0.61 / +0.32 | both halves | 2e-04 |  |
| [[ACTR8]] | +0.47 | +0.33 / +0.37 | both halves | 1e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC2]] | -0.47 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[BCL2L14]] | -0.47 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[NCK1-DT]] | -0.47 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CCSER1]] | -0.45 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[ITGB6]] | -0.43 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[COX7B]] | -0.42 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[MICOS10]] | -0.42 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[RBM47]] | -0.41 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[ATP1B1]] | -0.41 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[SSTR2]] | -0.41 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[PTMA]] | -0.40 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[SLC2A1-DT]] | -0.40 | -0.42 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR173]] | B | GPR173 activity raises TGFB1I1's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 2.53× lower at baseline in the lines without GPR173 | 0.026 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2 |
| [[COL6A1]] | B | COL6A1 activity raises TGFB1I1's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 2.35× lower at baseline in the lines without COL6A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[TOP2A]] | B | TOP2A activity raises TGFB1I1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SSTR2]] | B | SSTR2 activity raises TGFB1I1's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 2.07× lower at baseline in the lines without SSTR2 | 0.041 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[COL5A1]] | B | COL5A1 activity raises TGFB1I1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.50× lower at baseline in the lines without COL5A1 | 0.053 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[COL6A2]] | B | COL6A2 activity raises TGFB1I1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 2.12× lower at baseline in the lines without COL6A2 | 0.059 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLP2]] | B | TGFB1I1 activity raises PLP2's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without TGFB1I1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[GPSM1]] | B | TGFB1I1 activity raises GPSM1's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without TGFB1I1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[TTLL11]] | B | TGFB1I1 activity raises TTLL11's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without TGFB1I1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[TMEM43]] | B | TGFB1I1 activity raises TMEM43's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without TGFB1I1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[PRXL2C]] | B | TGFB1I1 activity raises PRXL2C's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 1.54× lower at baseline in the lines without TGFB1I1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[ZNF275]] | B | TGFB1I1 activity raises ZNF275's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without TGFB1I1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[GPR173]] | B | TGFB1I1 activity raises GPR173's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 4.40× lower at baseline in the lines without TGFB1I1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.342). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.8, -1.1); signed map (10.9, 56.2). **Vector** length 53.4, 9.80% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.7 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.2 | -0.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | -7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -6.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor beta 1 induced transcript 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,471,585-31,477,960 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hic-5, TSC-5, ARA55, HIC-5 |
| Gene groups (HGNC) | LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43294](https://www.uniprot.org/uniprotkb/O43294) (Transforming growth factor beta-1-induced transcript 1 protein):

> Functions as a molecular adapter coordinating multiple protein-protein interactions at the focal adhesion complex and in the nucleus. Links various intracellular signaling modules to plasma membrane receptors and regulates the Wnt and TGFB signaling pathways. May also regulate SLC6A3 and SLC6A4 targeting to the plasma membrane hence regulating their activity. In the nucleus, functions as a nuclear receptor coactivator regulating glucocorticoid, androgen, mineralocorticoid and progesterone …

**Summary**, from NCBI Gene [7041](https://www.ncbi.nlm.nih.gov/gene/7041):

> This gene encodes a coactivator of the androgen receptor, a transcription factor which is activated by androgen and has a key role in male sexual differentiation. The encoded protein is thought to regulate androgen receptor activity and may have a role to play in the treatment of prostate cancer. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:11767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11767) · Entrez [7041](https://www.ncbi.nlm.nih.gov/gene/7041) · UniProt [O43294](https://www.uniprot.org/uniprotkb/O43294) · Ensembl [ENSG00000140682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140682)

## Data

Gene col 6441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6441); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6441]; `tensor/DDL_lfc|DDL_z.npy` [6441]; `embed/gene_vectors.npy` [6441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6441 or target_col == 6441). Every well: [[TGFB1I1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFB1I1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

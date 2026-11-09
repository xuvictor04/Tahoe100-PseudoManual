---
symbol: "CCDC80"
type: "gene"
col: 1682
ensembl_id: "ENSG00000091986"
name: "coiled-coil domain containing 80"
location: "3q13.2"
module: 66
arm: "+"
pooled_cpm: 30.62
n_lines_expressing: 29
n_dd_up: 30
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# CCDC80

*coiled-coil domain containing 80* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.15× (z +20.6, q 0e+00, up in 24 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +14.8, q 0e+00, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.646× (z -5.0, q 4e-04, down in 15 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR1B1]] (+0.64, fdr 1e-05), [[MATN2]] (+0.62, fdr 7e-06), [[CHRDL1]] (+0.58, fdr 1e-05); moves opposite to [[ARMC10]] (-0.50, fdr 3e-05), [[ZNF749]] (-0.50, fdr 4e-05), [[WRN]] (-0.49, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[CALD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.15×** | +20.6 | 0e+00 | 24/24 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.35×** | +20.1 | 0e+00 | 20/20 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +14.8 | 0e+00 | 22/26 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.76×** | +13.9 | 1e-41 | 21/22 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.24×** | +12.9 | 4e-36 | 17/26 (A498, SW1417, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +8.0 | 2e-13 | 12/27 (SW1417, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.99×** | +7.5 | 7e-12 | 20/26 (A498, A-172, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.88×** | +7.1 | 8e-11 | 14/27 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.68×** | +5.9 | 3e-07 | 11/27 (NCI-H2030, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.6 | 1e-06 | 13/27 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.51×** | +5.3 | 6e-06 | 19/27 (HS-578T, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.3 | 7e-06 | 15/25 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.0 | 2e-05 | 13/27 (HOP62, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.51×** | +5.0 | 2e-05 | 16/27 (HS-578T, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +4.9 | 4e-05 | 16/26 (LOX-IMVI, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.006 | 14/27 (HS-578T, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.019 | 12/27 (HOP62, A498, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.037 | 13/27 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.064 | 11/27 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.064 | 12/27 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.074 | 10/27 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.43×** | +2.9 | 0.074 | 8/27 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1682.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.646×** | -5.0 | 4e-04 | 15/27 (NCI-H1792, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.664×** | -4.7 | 9e-04 | 15/26 (SW 900, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.672×** | -4.5 | 0.001 | 19/27 (NCI-H1792, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.646×** | -3.5 | 0.056 | 11/27 (HS-578T, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 206 | 9 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.4) | — |
| [[A498 (line)]] | wt | 64.4 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 23.9 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 66.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 16.2 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.6× (z +20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.8) | — |
| [[A-172 (line)]] | wt | 74.1 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 8.63 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.1× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.79× (z +13.5) | — |
| [[A549 (line)]] | wt | 23.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +15.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 98.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 130 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +12.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 39.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.68× (z +10.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 11.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.0× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 15.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.7) | — |
| [[C32 (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +10.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 8.65 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.97× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 129 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 3.69× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.35 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.53× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 6.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1B1]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[MATN2]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CHRDL1]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LUM]] | +0.57 | +0.48 / +0.65 | both halves | 2e-05 | STRING 443 |
| [[COL12A1]] | +0.57 | +0.44 / +0.67 | both halves | 3e-05 | STRING 457 |
| [[PRECSIT]] | +0.57 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[CALD1]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SULF1]] | +0.55 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[GFRA1]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[FILIP1L]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SSPN]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC10]] | -0.50 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ZNF749]] | -0.50 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[WRN]] | -0.49 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ZMYND19]] | -0.48 | -0.45 / -0.43 | both halves | 4e-05 |  |
| [[ZNF549]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[VKORC1L1]] | -0.48 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[LSM7]] | -0.46 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ZBED4]] | -0.46 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[ASB13]] | -0.46 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[MRPL52]] | -0.45 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[LSM11]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[GSTO1]] | -0.44 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC80's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSG5]] | B | PSG5 activity raises CCDC80's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 4.88× lower at baseline in the lines without PSG5 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486 |
| [[EDIL3]] | B | EDIL3 activity raises CCDC80's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without EDIL3 | 0.085 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[ABCC9]] | C | ABCC9 activity raises CCDC80's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 4.96× lower at baseline in the lines without ABCC9 | 0.003 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises CCDC80's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 5.28× lower at baseline in the lines without ALPK2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises CCDC80's level | lines that do not express POSTN (38) vs lines expressing it (12) | 4.70× lower at baseline in the lines without POSTN | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[DPYSL3]] | C | DPYSL3 activity raises CCDC80's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 4.13× lower at baseline in the lines without DPYSL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1; co-absent with the target |
| [[MSC]] | C | MSC activity raises CCDC80's level | lines that do not express MSC (34) vs lines expressing it (16) | 4.35× lower at baseline in the lines without MSC | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALD1]] | B | CCDC80 activity raises CALD1's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 3.66× lower at baseline in the lines without CCDC80 | 0.008 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | CCDC80 activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express CCDC80 (21) vs lines expressing it (27) | the lines without CCDC80: 0.84× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[EDIL3]] | B | CCDC80 activity raises EDIL3's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 3.51× lower at baseline in the lines without CCDC80 | 0.051 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| cells under [[Sodium Salicylate (drug)]] 5 µM | B | CCDC80 activity lowers the cells' numbers under Sodium Salicylate 5 µM (makes them more sensitive) | lines that do not express CCDC80 (21) vs lines expressing it (27) | the lines without CCDC80: 1.11× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[MAP1A]] | B | CCDC80 activity raises MAP1A's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 2.51× lower at baseline in the lines without CCDC80 | 0.070 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[GLIPR1]] | B | CCDC80 activity raises GLIPR1's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 2.70× lower at baseline in the lines without CCDC80 | 0.074 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[AKR1B1]] | B | CCDC80 activity raises AKR1B1's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 3.05× lower at baseline in the lines without CCDC80 | 0.074 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[COL1A1]] | B | CCDC80 activity raises COL1A1's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 3.46× lower at baseline in the lines without CCDC80 | 0.082 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| cells under [[Sodium Salicylate (drug)]] 0.5 µM | B | CCDC80 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express CCDC80 (21) vs lines expressing it (27) | the lines without CCDC80: 1.15× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| cells under [[Apalutamide (drug)]] 0.5 µM | B | CCDC80 activity raises the cells' numbers under Apalutamide 0.5 µM (protects the cells) | lines that do not express CCDC80 (21) vs lines expressing it (27) | the lines without CCDC80: 0.86× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[ABCC9]] | C | CCDC80 activity raises ABCC9's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 1.96× lower at baseline in the lines without CCDC80 | 0.073 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2; co-absent with the target |
| [[PTN]] | C | CCDC80 activity raises PTN's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 3.23× lower at baseline in the lines without CCDC80 | 0.091 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.4, 20.1); signed map (44.0, 20.4). **Vector** length 84.1, 23.5% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +20.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.7 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +13.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +8.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -1.9 | +3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.8 | +0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 80 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:112,596,797-112,649,530 (-) |
| Ensembl biotype | protein_coding |
| Also known as | URB, SSG1, DRO1, CL2, TCONS_00006930; previously LINC01279 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76M96](https://www.uniprot.org/uniprotkb/Q76M96) (Coiled-coil domain-containing protein 80):

> Promotes cell adhesion and matrix assembly.

**Summary**, from NCBI Gene [151887](https://www.ncbi.nlm.nih.gov/gene/151887):

> Predicted to enable fibronectin binding activity and heparin binding activity. Predicted to be involved in extracellular matrix organization and positive regulation of cell-substrate adhesion. Predicted to act upstream of or within response to bacterium. Predicted to be located in interstitial matrix. Predicted to be active in basement membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30649) · Entrez [151887](https://www.ncbi.nlm.nih.gov/gene/151887) · UniProt [Q76M96](https://www.uniprot.org/uniprotkb/Q76M96) · Ensembl [ENSG00000091986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091986)

## Data

Gene col 1682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1682); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1682]; `tensor/DDL_lfc|DDL_z.npy` [1682]; `embed/gene_vectors.npy` [1682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1682 or target_col == 1682). Every well: [[CCDC80 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC80.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

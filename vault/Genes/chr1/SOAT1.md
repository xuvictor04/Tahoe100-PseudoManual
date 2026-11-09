---
symbol: "SOAT1"
type: "gene"
col: 645
ensembl_id: "ENSG00000057252"
name: "sterol O-acyltransferase 1"
location: "1q25.2"
module: 23
arm: "-"
pooled_cpm: 42.08
n_lines_expressing: 47
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SOAT1

*sterol O-acyltransferase 1* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.21× (z +23.3, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.793× (z -6.6, q 3e-08, down in 26 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LoVo 0.400×, SW 900 0.457×, RKO 0.435×, CHP-212 0.201×, …); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.281×; ⚠ cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.0939×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAK1]] (+0.64, fdr 1e-05), [[MTMR8]] (+0.62, fdr 1e-05), [[PRKAR2B]] (+0.61, fdr 1e-05); moves opposite to [[RECQL5]] (-0.67, fdr 7e-06), [[NMNAT1]] (-0.66, fdr 1e-05), [[TRIM39]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SH3RF2]] → it (grade B ⚠); 11 go from it, the strongest it → [[HDHD3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.21×** | +23.3 | 0e+00 | 45/45 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.96×** | +21.7 | 0e+00 | 45/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.77×** | +20.4 | 0e+00 | 45/45 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +13.4 | 1e-38 | 35/44 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +12.9 | 6e-36 | 40/45 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +11.1 | 9e-27 | 36/44 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +10.5 | 6e-24 | 39/45 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +10.4 | 3e-23 | 33/43 (H4, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +10.3 | 4e-23 | 35/45 (J82, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +9.6 | 7e-20 | 34/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.34×** | +8.9 | 3e-17 | 36/45 (A498, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +8.9 | 3e-17 | 34/45 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +8.9 | 3e-17 | 28/38 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +8.3 | 4e-15 | 26/45 (H4, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +7.5 | 3e-12 | 30/45 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.6 | 1e-09 | 25/45 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.6 | 2e-09 | 27/45 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +6.3 | 8e-09 | 27/45 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +6.2 | 2e-08 | 23/45 (A-172, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 645.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LoVo 0.400×, SW 900 0.457×, RKO 0.435×, CHP-212 0.201×, …); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.281×; ⚠ cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.0939×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -6.6 | 3e-08 | 26/45 (LoVo, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.876× | -3.8 | 0.046 | 16/45 (Hs 766T, SW480, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.714×** | -3.5 | 0.080 | 16/45 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.28 | 13/44 (SNU-423, AN3 CA, …) | inconsistent across doses | low cells (technical?) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.860× | -3.0 | 0.28 | 10/45 (NCI-H460, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 66.4 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 28.2 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.47× (z +14.9) | — |
| [[H4 (line)]] | wt | 39.8 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.09× (z +11.1) | — |
| [[LoVo (line)]] | wt | 24.7 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.10× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -11.8) |
| [[PANC-1 (line)]] | alt | 43.7 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 58.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.28× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 39.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.96× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 47.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.52× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 28.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 5.73× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -8.6) |
| [[SW480 (line)]] | alt | 23.9 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +13.3) | — |
| [[A549 (line)]] | wt | 33.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 15.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.58× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.65× (z +14.6) | — |
| [[HEC-1-A (line)]] | alt | 31.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.16× (z +12.4) | — |
| [[J82 (line)]] | alt | 90.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 57.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 33.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 89.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +12.1) | — |
| [[A-427 (line)]] | wt | 58.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 40.6 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.0939× (z -9.8) |
| [[HS-578T (line)]] | alt | 24.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.58× (z +8.6) | — |
| [[KATO III (line)]] | alt | 18.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +9.6) | — |
| [[RKO (line)]] | wt | 69.2 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.8) |
| [[SNU-423 (line)]] | alt | 78.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.3) | — |
| [[A-172 (line)]] | wt | 95.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.3) | — |
| [[HCT15 (line)]] | alt | 33.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.42× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 53.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 89.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.9) |
| [[AN3 CA (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK1]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[MTMR8]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PRKAR2B]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[HPSE]] | +0.59 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[CYRIB]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[HDAC1]] | +0.58 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[PRKCI]] | +0.57 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[FDX1]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.56 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[NXPE3]] | +0.56 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[SYTL4]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CERS6]] | +0.56 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL5]] | -0.67 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[NMNAT1]] | -0.66 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[TRIM39]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CFAP53]] | -0.61 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[KIAA0753]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[PPP1R14B-AS1]] | -0.59 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ZNF335]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[TMEM187]] | -0.58 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[IKZF4]] | -0.57 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[GPANK1]] | -0.57 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ARMC5]] | -0.57 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[BOLA1]] | -0.57 | -0.36 / -0.49 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3RF2]] | B | SH3RF2 activity strengthens SOAT1's drug response | lines that do not express SH3RF2 (16) vs lines expressing it (29) | the lines without SH3RF2 respond 0.72× as strongly (z diff +1.15); strongest at Belinostat 5 µM: 2.30x vs 3.12x (z diff +2.1) | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TMOD2]] | B | TMOD2 activity raises SOAT1's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without TMOD2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |
| [[CD24]] | B | CD24 activity lowers SOAT1's level | lines that do not express CD24 (24) vs lines expressing it (26) | 1.60× higher at baseline in the lines without CD24 | 0.089 | ⚠ within organs, on part of the lines; also absent: FOXQ1, RNF223, SPNS2 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDHD3]] | C | SOAT1 activity lowers HDHD3's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 3.39× higher at baseline in the lines without SOAT1 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |
| [[PLBD2]] | C | SOAT1 activity raises PLBD2's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without SOAT1 | 0.024 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |
| [[RCBTB1]] | C | SOAT1 activity weakens RCBTB1's drug response | lines that do not express SOAT1 (3) vs lines expressing it (45) | the lines without SOAT1 respond 2.14× as strongly (z diff -3.20); strongest at Belinostat 5 µM: 4.16x vs 2.08x (z diff -4.0) | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2; target measured in part of the lines; artifact flags |
| [[SH3RF2]] | C | SOAT1 activity strengthens SH3RF2's drug response | lines that do not express SOAT1 (3) vs lines expressing it (29) | the lines without SOAT1 respond 0.23× as strongly (z diff +2.57); strongest at Panobinostat 5 µM: 0.51x vs 1.92x (z diff +8.2) | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2; target measured in part of the lines; artifact flags |
| cells under [[MK-3903 (drug)]] 5 µM | C | SOAT1 activity raises the cells' numbers under MK-3903 5 µM (protects the cells) | lines that do not express SOAT1 (3) vs lines expressing it (45) | the lines without SOAT1: 0.65× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |
| [[BLMH]] | C | SOAT1 activity raises BLMH's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 3.04× lower at baseline in the lines without SOAT1 | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |
| cells under [[Afatinib (drug)]] 0.05 µM | C | SOAT1 activity raises the cells' numbers under Afatinib 0.05 µM (protects the cells) | lines that do not express SOAT1 (3) vs lines expressing it (45) | the lines without SOAT1: 0.82× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |
| [[CPT1A]] | C | SOAT1 activity strengthens CPT1A's drug response | lines that do not express SOAT1 (3) vs lines expressing it (45) | the lines without SOAT1 respond 0.57× as strongly (z diff +2.13); strongest at Dinaciclib 5 µM: 0.92x vs 2.09x (z diff +6.1) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2; target measured in part of the lines; artifact flags |
| [[IRF3]] | C | SOAT1 activity lowers IRF3's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 1.83× higher at baseline in the lines without SOAT1 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |
| [[SLC23A2]] | C | SOAT1 activity raises SLC23A2's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without SOAT1 | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |
| [[HDAC1]] | C | SOAT1 activity lowers HDAC1's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 1.82× higher at baseline in the lines without SOAT1 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.453). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-3.1, 35.9); signed map (-18.0, 37.0). **Vector** length 106, 29.0% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +7.9 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +8.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +7.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -0.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | sterol O-acyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:179,293,714-179,358,680 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACAT, ACAT1; previously SOAT, STAT |
| Gene groups (HGNC) | Membrane bound O-acyltransferase family |
| Reactome | 4 pathways, smallest: LDL clearance; Plasma lipoprotein clearance; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [P35610](https://www.uniprot.org/uniprotkb/P35610) (Sterol O-acyltransferase 1):

> Catalyzes the formation of fatty acid-cholesterol esters, which are less soluble in membranes than cholesterol. Plays a role in lipoprotein assembly and dietary cholesterol absorption. Preferentially utilizes oleoyl-CoA ((9Z)-octadecenoyl-CoA) as a substrate: shows a higher activity towards an acyl-CoA substrate with a double bond at the delta-9 position (9Z) than towards saturated acyl-CoA or an unsaturated acyl-CoA with a double bond at the delta-7 (7Z) or delta-11 (11Z) positions.

**Summary**, from NCBI Gene [6646](https://www.ncbi.nlm.nih.gov/gene/6646):

> The protein encoded by this gene belongs to the acyltransferase family. It is located in the endoplasmic reticulum, and catalyzes the formation of fatty acid-cholesterol esters. This gene has been implicated in the formation of beta-amyloid and atherosclerotic plaques by controlling the equilibrium between free cholesterol and cytoplasmic cholesteryl esters. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:11177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11177) · Entrez [6646](https://www.ncbi.nlm.nih.gov/gene/6646) · UniProt [P35610](https://www.uniprot.org/uniprotkb/P35610) · Ensembl [ENSG00000057252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057252)

## Data

Gene col 645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 645); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 645]; `tensor/DDL_lfc|DDL_z.npy` [645]; `embed/gene_vectors.npy` [645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 645 or target_col == 645). Every well: [[SOAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "DBNDD1"
type: "gene"
col: 31
ensembl_id: "ENSG00000003249"
name: "dysbindin domain containing 1"
location: "16q24.3"
module: 102
arm: "+"
pooled_cpm: 6.4
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# DBNDD1

*dysbindin domain containing 1* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.83× (z +12.7, q 5e-34, up in 32 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.470× (z -8.9, q 5e-16, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASGEF1C]] (+0.53, fdr 4e-05), [[KIF1A]] (+0.50, fdr 4e-05), [[MSI1]] (+0.49, fdr 3e-05); moves opposite to [[COX8A]] (-0.41, fdr 2e-04), [[S100A1]] (-0.38, fdr 9e-04, ⚠ not reproduced), [[TPCN1]] (-0.38, fdr 1e-04), [[WNT5A]] (-0.38, fdr 7e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[WNT5A]] → it (grade B ⚠); 2 go from it, the strongest it → [[GAS8]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 31.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +12.7 | 5e-34 | 32/41 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +9.3 | 5e-18 | 7/11 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +8.9 | 8e-17 | 15/24 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +5.8 | 9e-07 | 10/17 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.0 | 5e-05 | 12/29 (CFPAC-1, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.67×** | +4.5 | 8e-04 | 6/25 (RKO, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 0.001 | 11/36 (MIA PaCa-2, LS 180, …) | two highest doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.087 | 5/36 (C32, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.2 | 0.087 | 5/45 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.087 | 4/42 (BT-474, HT-29, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 31.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.470×** | -8.9 | 5e-16 | 25/41 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -8.2 | 7e-14 | 25/44 (SK-MEL-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.632×** | -7.9 | 5e-13 | 22/39 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.535×** | -7.6 | 3e-12 | 25/42 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.594×** | -6.4 | 2e-08 | 20/36 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.596×** | -6.3 | 2e-08 | 23/44 (C32, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.618×** | -5.9 | 3e-07 | 18/41 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.668×** | -4.9 | 6e-05 | 11/40 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -4.9 | 7e-05 | 16/39 (SW48, SW 900, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.475×** | -4.7 | 1e-04 | 13/34 (RKO, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.679×** | -4.7 | 1e-04 | 18/44 (SK-MEL-2, MIA PaCa-2, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.480×** | -4.7 | 1e-04 | 15/41 (Panc 03.27, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.483×** | -4.6 | 2e-04 | 14/34 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.699×** | -4.4 | 5e-04 | 19/43 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.762×** | -3.3 | 0.033 | 10/43 (A-172, SW 1271, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.765×** | -3.3 | 0.036 | 7/44 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.768×** | -3.2 | 0.038 | 16/35 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 31. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -16.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0333× (z -15.9) |
| [[C32 (line)]] | wt | 16.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -12.5) |
| [[A-172 (line)]] | wt | 7.35 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0600× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0607× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.2) |
| [[A-427 (line)]] | wt | 13.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.138× (z -11.0) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.184× (z -9.1) |
| [[J82 (line)]] | alt | 5.50 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0625× (z -11.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Menadione (drug)]] 5 µM 0.0629× (z -11.3) |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 5.98 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0587× (z -11.1) |
| [[SW48 (line)]] | wt | 14.9 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.0735× (z -10.9) |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.121× (z -8.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 9.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0693× (z -9.4) |
| [[KATO III (line)]] | alt | 9.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -8.8) |
| [[LoVo (line)]] | wt | 9.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 7.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 1.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +9.4) | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0973× (z -10.3) |
| [[SW480 (line)]] | alt | 5.81 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.61× (z +13.0) | — |
| [[A498 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.720 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 31), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASGEF1C]] | +0.53 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[KIF1A]] | +0.50 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[MSI1]] | +0.49 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[SHANK3]] | +0.48 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[ANKRD6]] | +0.47 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[ST6GAL1]] | +0.47 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[DEF8]] | +0.46 | +0.30 / +0.51 | both halves | 2e-04 | STRING 675; ⚠ same locus (36.8 kb: neighbours can correlate without regulation) |
| [[LINC00839]] | +0.46 | +0.30 / +0.47 | both halves | 2e-04 |  |
| [[ZNF114]] | +0.45 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[KBTBD11]] | +0.45 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[HAGLR]] | +0.45 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[SYT17]] | +0.45 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[STOX2]] | +0.45 | +0.48 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX8A]] | -0.41 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[S100A1]] | -0.38 | -0.18 / -0.26 | ⚠ not reproduced | 9e-04 |  |
| [[TPCN1]] | -0.38 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[WNT5A]] | -0.38 | -0.44 / -0.21 | both halves | 7e-04 |  |
| [[ETFB]] | -0.38 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[SORBS2]] | -0.38 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[ARHGAP24]] | -0.38 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT5A]] | B | WNT5A activity lowers DBNDD1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.08× higher at baseline in the lines without WNT5A | 0.002 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[MSI1]] | B | MSI1 activity raises DBNDD1's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without MSI1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[B4GALNT3]] | B | B4GALNT3 activity strengthens DBNDD1's drug response | lines that do not express B4GALNT3 (14) vs lines expressing it (30) | the lines without B4GALNT3 respond 0.46× as strongly (z diff +1.77); strongest at Homoharringtonine 5 µM: 1.41x vs 0.40x (z diff +7.0) | 0.033 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6; target measured in part of the lines; artifact flags |
| [[DPYSL5]] | B | DPYSL5 activity raises DBNDD1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without DPYSL5 | 0.057 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[PRKCZ]] | B | PRKCZ activity raises DBNDD1's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without PRKCZ | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C; its own permutation p |
| [[WNT5A]] | B | WNT5A activity weakens DBNDD1's drug response | lines that do not express WNT5A (28) vs lines expressing it (16) | the lines without WNT5A respond 1.90× as strongly (z diff -1.84); strongest at Homoharringtonine 5 µM: 0.48x vs 0.99x (z diff -4.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; target measured in part of the lines; artifact flags |
| [[STOX2]] | B | STOX2 activity raises DBNDD1's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 1.29× lower at baseline in the lines without STOX2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[FRMD3]] | B | FRMD3 activity lowers DBNDD1's level | lines that do not express FRMD3 (5) vs lines expressing it (45) | 2.17× higher at baseline in the lines without FRMD3 | 0.093 | ⚠ within organs, on part of the lines; also absent: SSUH2, CACNG2, ZMIZ1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAS8]] | C | DBNDD1 activity raises GAS8's level | lines that do not express DBNDD1 (3) vs lines expressing it (47) | 2.50× lower at baseline in the lines without DBNDD1 | 0.009 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, RHBDF2, EIF4E3 |
| cells under [[Radotinib (drug)]] 5 µM | C | DBNDD1 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express DBNDD1 (3) vs lines expressing it (45) | the lines without DBNDD1: 0.83× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, RHBDF2, EIF4E3 |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.489). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.9, 41.6); signed map (25.1, 27.8). **Vector** length 67.9, 11.1% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +8.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +4.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.8 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -8.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -7.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -4.6 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.0 | -0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | dysbindin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:90,004,871-90,019,890 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3101, FLJ12582 |
| Matched by | ensembl_id |

UniProt [Q9H9R9](https://www.uniprot.org/uniprotkb/Q9H9R9) carries no function annotation.

**Summary**, from NCBI Gene [79007](https://www.ncbi.nlm.nih.gov/gene/79007):

> Predicted to be involved in regulation of signal transduction. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28455) · Entrez [79007](https://www.ncbi.nlm.nih.gov/gene/79007) · UniProt [Q9H9R9](https://www.uniprot.org/uniprotkb/Q9H9R9) · Ensembl [ENSG00000003249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003249)

## Data

Gene col 31: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 31); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 31, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 31]; `tensor/DDL_lfc|DDL_z.npy` [31]; `embed/gene_vectors.npy` [31]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 31 or target_col == 31). Every well: [[DBNDD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBNDD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

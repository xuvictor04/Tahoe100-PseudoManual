---
symbol: "PPP1R3C"
type: "gene"
col: 4139
ensembl_id: "ENSG00000119938"
name: "protein phosphatase 1 regulatory subunit 3C"
location: "10q23.32"
module: 79
arm: "+"
pooled_cpm: 24.14
n_lines_expressing: 28
n_dd_up: 34
n_dd_down: 20
n_dd_up_clean: 32
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# PPP1R3C

*protein phosphatase 1 regulatory subunit 3C* — 10q23.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.14× (z +10.0, q 6e-21, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.648× (z -5.7, q 4e-06, down in 19 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RYBP]] (+0.62, fdr 2e-05), [[ARL4D]] (+0.62, fdr 1e-05), [[DIXDC1]] (+0.60, fdr 1e-05); moves opposite to [[PBX3]] (-0.53, fdr 4e-05), [[NR2C2]] (-0.52, fdr 3e-05), [[ANXA2R-OT1]] (-0.51, fdr 3e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLIN2]] → it (grade B ⚠); 8 go from it, the strongest it → [[TMEM9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 2 with an alert ⚠; shown: the 15 strongest. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.14×** | +10.0 | 6e-21 | 26/26 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +7.4 | 3e-11 | 20/26 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.95×** | +6.7 | 3e-09 | 21/27 (NCI-H460, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +6.7 | 3e-09 | 19/26 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +6.6 | 6e-09 | 23/26 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +5.9 | 3e-07 | 17/26 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +5.9 | 4e-07 | 19/26 (A549, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.62×** | +5.0 | 5e-05 | 15/27 (HOP62, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.56×** | +4.7 | 2e-04 | 16/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +4.6 | 2e-04 | 20/25 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.5 | 3e-04 | 16/26 (C32, SNU-423, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.65×** | +4.5 | 3e-04 | 14/26 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +4.4 | 5e-04 | 13/26 (HOP62, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.57×** | +4.2 | 9e-04 | 15/27 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.63×** | +4.2 | 1e-03 | 13/25 (A549, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4139.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -5.7 | 4e-06 | 19/26 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.544×** | -5.7 | 4e-06 | 16/25 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.537×** | -5.6 | 5e-06 | 16/23 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.563×** | -5.3 | 1e-05 | 20/26 (AN3 CA, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.611×** | -4.6 | 5e-04 | 16/26 (A-172, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.630×** | -4.3 | 0.002 | 12/26 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.622×** | -4.2 | 0.003 | 11/26 (CFPAC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.646×** | -4.1 | 0.003 | 14/25 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.644×** | -3.9 | 0.005 | 12/25 (HepG2/C3A, CFPAC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.662×** | -3.8 | 0.007 | 17/26 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.752×** | -3.7 | 0.010 | 14/26 (CFPAC-1, HepG2/C3A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.673×** | -3.7 | 0.011 | 12/26 (HS-578T, AN3 CA, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **0.681×** | -3.6 | 0.016 | 12/26 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.683×** | -3.5 | 0.016 | 13/26 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.693×** | -3.4 | 0.026 | 12/27 (A-172, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.694×** | -3.2 | 0.048 | 10/25 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.519×** | -3.2 | 0.048 | 6/26 (Panc 03.27, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.720×** | -3.0 | 0.074 | 11/26 (A-172, CFPAC-1, …) | all doses, flat |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.794×** | -3.0 | 0.076 | 6/26 (A-172, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.2 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.93× (z +10.2) | — |
| [[A-172 (line)]] | wt | 78.4 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.81× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.0450× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 17.2 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 9.00× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 35.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.95× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 212 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.79× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -17.8) |
| [[A498 (line)]] | wt | 8.01 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.0) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.58× (z +8.9) | — |
| [[C32 (line)]] | wt | 81.4 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.75× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 34.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -15.9) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 21.2 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.86× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.0829× (z -9.0) |
| [[HOP62 (line)]] | alt | 34.3 | 2 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +10.7) ⚠ position not correctable · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.19× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 26.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.39× (z +9.5) | — |
| [[H4 (line)]] | wt | 54.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -12.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[Hs 766T (line)]] | wt | 33.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -12.3) |
| [[J82 (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +9.8) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[SNU-423 (line)]] | alt | 38.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.25× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYBP]] | +0.62 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ARL4D]] | +0.62 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[DIXDC1]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[RAB20]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[RNF150]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ZNF292]] | +0.59 | +0.60 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA |
| [[THAP8]] | +0.57 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[LRCH2]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PLEKHA2]] | +0.56 | +0.49 / +0.37 | both halves | 7e-05 |  |
| [[RAB30]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[BNIP3]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ADM]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX3]] | -0.53 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[NR2C2]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ANXA2R-OT1]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ANKMY1]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[KCTD13]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[MSANTD2]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ARIH2]] | -0.49 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[TTL]] | -0.48 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[MIATNB]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[VKORC1L1]] | -0.48 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.48 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[CDR2]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLIN2]] | B | PLIN2 activity raises PPP1R3C's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 2.42× lower at baseline in the lines without PLIN2 | 0.066 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[SLFN11]] | C | SLFN11 activity raises PPP1R3C's level | lines that do not express SLFN11 (28) vs lines expressing it (22) | 4.40× lower at baseline in the lines without SLFN11 | 0.023 | ⚠ within organs, on part of the lines; also absent: IGF2BP1, INSYN2B, DPY19L2; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM9]] | B | PPP1R3C activity raises TMEM9's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without PPP1R3C | 0.030 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[HILPDA]] | B | PPP1R3C activity raises HILPDA's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without PPP1R3C | 0.043 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[NR2C2]] | B | PPP1R3C activity lowers NR2C2's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.13× higher at baseline in the lines without PPP1R3C | 0.062 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[RAB20]] | B | PPP1R3C activity raises RAB20's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.17× lower at baseline in the lines without PPP1R3C | 0.067 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[BNIP3]] | B | PPP1R3C activity raises BNIP3's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 3.34× lower at baseline in the lines without PPP1R3C | 0.069 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[MLLT3]] | B | PPP1R3C activity raises MLLT3's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.20× lower at baseline in the lines without PPP1R3C | 0.077 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[DDIT4]] | B | PPP1R3C activity raises DDIT4's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.35× lower at baseline in the lines without PPP1R3C | 0.083 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[SLFN11]] | C | PPP1R3C activity raises SLFN11's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 4.39× lower at baseline in the lines without PPP1R3C | 0.050 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1; co-absent with the target |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, -12.1); signed map (-8.1, 16.3). **Vector** length 95.1, 28.7% of its response variance represented; |z| ≥ 3 in 764 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -5.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.32 — chr10:91,628,442-91,633,071 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTG; previously PPP1R5 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | MYOGENESIS, HYPOXIA |
| Reactome | 7 pathways, smallest: Myoclonic epilepsy of Lafora; Glycogen synthesis; Glycogen storage diseases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQK1](https://www.uniprot.org/uniprotkb/Q9UQK1) (Protein phosphatase 1 regulatory subunit 3C):

> Acts as a glycogen-targeting subunit for PP1 and regulates its activity. Activates glycogen synthase, reduces glycogen phosphorylase activity and limits glycogen breakdown. Dramatically increases basal and insulin-stimulated glycogen synthesis upon overexpression in a variety of cell types.

**Summary**, from NCBI Gene [5507](https://www.ncbi.nlm.nih.gov/gene/5507):

> This gene encodes a carbohydrate binding protein that is a subunit of the protein phosphatase 1 (PP1) complex. PP1 catalyzes reversible protein phosphorylation, which is important in a wide range of cellular activities. The encoded protein affects glycogen biosynthesis by activating glycogen synthase and limiting glycogen breakdown by reducing glycogen phosphorylase activity. DNA hypermethylation of this gene has been found in colorectal cancer patients. The encoded protein also interacts with …

**Accessions** — [HGNC:9293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9293) · Entrez [5507](https://www.ncbi.nlm.nih.gov/gene/5507) · UniProt [Q9UQK1](https://www.uniprot.org/uniprotkb/Q9UQK1) · Ensembl [ENSG00000119938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119938)

## Data

Gene col 4139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4139); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4139]; `tensor/DDL_lfc|DDL_z.npy` [4139]; `embed/gene_vectors.npy` [4139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4139 or target_col == 4139). Every well: [[PPP1R3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

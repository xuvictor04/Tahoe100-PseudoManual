---
symbol: "ADGRG1"
type: "gene"
col: 12968
ensembl_id: "ENSG00000205336"
name: "adhesion G protein-coupled receptor G1"
location: "16q21"
module: 14
arm: "+"
pooled_cpm: 41.69
n_lines_expressing: 38
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 10
direction_downstream: 23
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ADGRG1

*adhesion G protein-coupled receptor G1* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +9.8, q 9e-20, up in 19 of 36 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.01× (z +8.9, q 2e-16, up in 24 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.588× (z -9.8, q 5e-20, down in 27 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL16A1]] (+0.71, fdr 7e-06), [[CD70]] (+0.63, fdr 1e-05), [[CGNL1]] (+0.60, fdr 1e-05); moves opposite to [[RNF217]] (-0.53, fdr 3e-05), [[GRPEL1]] (-0.50, fdr 4e-05), [[NUP133]] (-0.49, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ANO9]] → it (grade B ⚠); 23 go from it, the strongest it → [[CXXC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.70×** | +9.8 | 9e-20 | 19/36 (A549, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +8.9 | 2e-16 | 24/36 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +8.2 | 5e-14 | 30/36 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +6.6 | 6e-09 | 27/36 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.2 | 8e-08 | 17/34 (A498, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.52×** | +5.5 | 3e-06 | 16/36 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.45×** | +4.9 | 8e-05 | 18/36 (HT-29, SW1417, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +4.8 | 1e-04 | 16/36 (C32, NCI-H1573, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.5 | 4e-04 | 18/33 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +4.4 | 6e-04 | 18/34 (CFPAC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +4.1 | 0.002 | 15/31 (SK-MEL-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.002 | 19/36 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +4.0 | 0.003 | 17/36 (A549, A498, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.63×** | +3.9 | 0.003 | 16/35 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.008 | 15/36 (SW480, BT-474, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.018 | 16/36 (C32, HEC-1-A, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.026 | 10/34 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.030 | 8/34 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12968.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -9.8 | 5e-20 | 27/35 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.588×** | -7.1 | 5e-10 | 26/36 (HT-29, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.621×** | -6.3 | 5e-08 | 23/36 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.702×** | -4.7 | 4e-04 | 16/36 (SNU-423, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.712×** | -4.3 | 0.002 | 20/36 (J82, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.727×** | -4.2 | 0.002 | 18/35 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.722×** | -4.2 | 0.002 | 19/36 (SW1417, C32, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -4.1 | 0.002 | 16/35 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -4.0 | 0.003 | 17/36 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.574×** | -3.9 | 0.007 | 16/37 (SW480, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.755×** | -3.7 | 0.009 | 15/36 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.030 | 12/36 (J82, CFPAC-1, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.761×** | -3.4 | 0.035 | 17/35 (A549, CHP-212, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.790×** | -3.1 | 0.064 | 16/36 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.636×** | -3.1 | 0.064 | 14/36 (Hs 766T, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.795×** | -3.0 | 0.081 | 13/36 (NCI-H460, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 66.5 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -14.3) |
| [[HepG2_C3A (line)]] | wt | 92.3 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Belinostat (drug)]] 5 µM 0.213× (z -10.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[J82 (line)]] | alt | 36.9 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.08× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -12.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -9.0) |
| [[A-172 (line)]] | wt | 58.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.63× (z +10.2) | — |
| [[A498 (line)]] | wt | 157 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +14.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.35× (z +10.4) | [[Bortezomib (drug)]] 5 µM 0.151× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 29.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.56× (z +18.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.81× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 19.3 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.35× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 59.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 21.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.64× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 40.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.3) |
| [[COLO 205 (line)]] | alt | 67.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 36.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +14.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.22× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 38.3 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 4.35× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -11.8) |
| [[SNU-423 (line)]] | alt | 60.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +13.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.99× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 19.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.40× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RPMI-7951 (line)]] | alt | 41.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 92.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.02× (z +10.3) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 93.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.392× (z -9.5) |
| [[A-427 (line)]] | wt | 9.35 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.09 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.61 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 35.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL16A1]] | +0.71 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[CD70]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[CGNL1]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ANO9]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[TPPP]] | +0.58 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[REPIN1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TEF]] | +0.57 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[PIM3]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[RRAD]] | +0.57 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[CYRIA]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TUBB2B]] | +0.56 | +0.50 / +0.65 | both halves | 1e-05 | STRING 418 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF217]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[GRPEL1]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[NUP133]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO9]] | B | ANO9 activity raises ADGRG1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.20× lower at baseline in the lines without ANO9 | 0.012 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises ADGRG1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without ELF3-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[CX3CL1]] | B | CX3CL1 activity raises ADGRG1's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 2.88× lower at baseline in the lines without CX3CL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[NEURL3]] | B | NEURL3 activity raises ADGRG1's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.64× lower at baseline in the lines without NEURL3 | 0.051 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[TNFAIP2]] | B | TNFAIP2 activity raises ADGRG1's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.73× lower at baseline in the lines without TNFAIP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[ILDR1]] | B | ILDR1 activity raises ADGRG1's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without ILDR1 | 0.055 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1 |
| [[COL16A1]] | B | COL16A1 activity raises ADGRG1's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.83× lower at baseline in the lines without COL16A1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[COL22A1]] | B | COL22A1 activity raises ADGRG1's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without COL22A1 | 0.081 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2 |
| [[LGALS3]] | C | LGALS3 activity raises ADGRG1's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 4.96× lower at baseline in the lines without LGALS3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1; co-absent with the target |
| [[STAT5A]] | C | STAT5A activity raises ADGRG1's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.86× lower at baseline in the lines without STAT5A | 0.005 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 22, C 1. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXXC5]] | B | ADGRG1 activity raises CXXC5's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 3.60× lower at baseline in the lines without ADGRG1 | 0.003 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[SLC7A8]] | B | ADGRG1 activity raises SLC7A8's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.00× lower at baseline in the lines without ADGRG1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[CX3CL1]] | B | ADGRG1 activity raises CX3CL1's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without ADGRG1 | 0.021 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[SYTL1]] | B | ADGRG1 activity raises SYTL1's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.00× lower at baseline in the lines without ADGRG1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[TNFAIP2]] | B | ADGRG1 activity raises TNFAIP2's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 3.19× lower at baseline in the lines without ADGRG1 | 0.026 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[PIM3]] | B | ADGRG1 activity raises PIM3's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without ADGRG1 | 0.026 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[TEF]] | B | ADGRG1 activity raises TEF's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without ADGRG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[LRIG1]] | B | ADGRG1 activity raises LRIG1's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.63× lower at baseline in the lines without ADGRG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[ELF3-AS1]] | B | ADGRG1 activity raises ELF3-AS1's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.00× lower at baseline in the lines without ADGRG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[CBX4]] | B | ADGRG1 activity raises CBX4's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without ADGRG1 | 0.046 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[ANO9]] | B | ADGRG1 activity raises ANO9's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.24× lower at baseline in the lines without ADGRG1 | 0.049 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[TEF]] | B | ADGRG1 activity strengthens TEF's drug response | lines that do not express ADGRG1 (12) vs lines expressing it (36) | the lines without ADGRG1 respond 0.48× as strongly (z diff +1.67); rises at some drug-doses, falls at others (32% from rises): Megestrol 5 µM: 0.75x vs 0.49x (z diff +2.7); Edoxaban (tosylate monohydrate) 5 µM: 0.47x vs 0.29x (z diff +2.5); Homoharringtonine 5 µM: 4.59x vs 5.06x (z diff +2.0) | 0.054 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526; target measured in part of the lines; rises at some drug-doses, falls at others; line-wide correction only; artifact flags |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.6, 2.1); signed map (45.7, 9.2). **Vector** length 107, 28.2% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +8.9 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.3 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | +4.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.5 | -0.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor G1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,610,652-57,665,580 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TM7LN4, TM7XN1; previously GPR56 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily G |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y653](https://www.uniprot.org/uniprotkb/Q9Y653) (Adhesion G protein-coupled receptor G1):

> Adhesion G protein-coupled receptor (aGPCR) for steroid hormone 17alpha-hydroxypregnenolone (17-OH), which is involved in cell adhesion and cell-cell interactions. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as RhoA pathway. ADGRG1 is coupled to G(12) and/or G(13) G proteins (GNA12 and GNA13, respectively) and mediates the activation Rho small GTPases. Acts as a …

**Summary**, from NCBI Gene [9289](https://www.ncbi.nlm.nih.gov/gene/9289):

> This gene encodes a member of the G protein-coupled receptor family and regulates brain cortical patterning. The encoded protein binds specifically to transglutaminase 2, a component of tissue and tumor stroma implicated as an inhibitor of tumor progression. Mutations in this gene are associated with a brain malformation known as bilateral frontoparietal polymicrogyria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:4512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4512) · Entrez [9289](https://www.ncbi.nlm.nih.gov/gene/9289) · UniProt [Q9Y653](https://www.uniprot.org/uniprotkb/Q9Y653) · Ensembl [ENSG00000205336](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205336)

## Data

Gene col 12968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12968); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12968]; `tensor/DDL_lfc|DDL_z.npy` [12968]; `embed/gene_vectors.npy` [12968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12968 or target_col == 12968). Every well: [[ADGRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

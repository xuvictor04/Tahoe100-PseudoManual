---
symbol: "RAB11FIP1"
type: "gene"
col: 8005
ensembl_id: "ENSG00000156675"
name: "RAB11 family interacting protein 1"
location: "8p11.23"
module: 194
arm: "-"
pooled_cpm: 116.92
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 23
direction_downstream: 22
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# RAB11FIP1

*RAB11 family interacting protein 1* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.84× (z +19.7, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.695× (z -6.6, q 2e-08, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[F11R]] (+0.70, fdr 1e-05), [[WASF2]] (+0.70, fdr 4e-05), [[CNNM4]] (+0.68, fdr 7e-06); moves opposite to [[ST7L]] (-0.64, fdr 1e-05), [[ALG8]] (-0.63, fdr 1e-05), [[DNAJC11]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[CDH1]] → it (grade B ⚠); 22 go from it, the strongest it → cells under [[Carbamazepine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.84×** | +19.7 | 0e+00 | 42/45 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.74×** | +19.0 | 0e+00 | 42/45 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.52×** | +17.5 | 0e+00 | 41/45 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +12.6 | 2e-34 | 39/45 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +9.6 | 7e-20 | 38/45 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +7.2 | 8e-11 | 31/46 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +5.9 | 4e-07 | 34/46 (A-172, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 2e-05 | 27/45 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.003 | 20/46 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 20/45 (LS 180, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.9 | 0.004 | 16/45 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.004 | 21/45 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.097 | 18/45 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +3.0 | 0.097 | 17/45 (LoVo, Panc 03.27, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8005.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.695×** | -6.6 | 2e-08 | 25/45 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.616×** | -4.8 | 5e-04 | 23/46 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -4.5 | 0.001 | 24/45 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.784×** | -4.4 | 0.001 | 24/41 (NCI-H23, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -4.4 | 0.001 | 22/45 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.816×** | -3.8 | 0.011 | 17/45 (HT-29, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.011 | 20/45 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.805×** | -3.8 | 0.011 | 25/43 (CFPAC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.690×** | -3.7 | 0.015 | 21/45 (RKO, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.4 | 0.034 | 19/45 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.843× | -3.2 | 0.066 | 18/45 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.071 | 14/44 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -3.2 | 0.071 | 0/47 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -3.1 | 0.080 | 18/45 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -3.1 | 0.080 | 15/45 (CFPAC-1, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 291 | 2 | 12 (8 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.09× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -20.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -11.3) |
| [[LoVo (line)]] | wt | 157 | 8 (2 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +14.0) | [[Harringtonine (drug)]] 5 µM 0.386× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 4 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.451× (z -9.1) |
| [[A498 (line)]] | wt | 126 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.12× (z +14.0) | — |
| [[J82 (line)]] | alt | 54.0 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.49× (z +16.6) | — |
| [[LOX-IMVI (line)]] | wt | 44.4 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 8.42× (z +19.2) | — |
| [[Panc 03.27 (line)]] | alt | 452 | 3 | 3 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.90× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 52.6 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.77× (z +14.4) | — |
| [[A-427 (line)]] | wt | 73.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.45× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 89.3 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 56.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.25× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 85.9 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.08× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 257 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +13.4) | — |
| [[HOP62 (line)]] | alt | 64.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.56× (z +12.7) | — |
| [[KATO III (line)]] | alt | 227 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 49.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 62.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -16.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 87.9 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 60.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.23× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 148 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 71.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.68× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 62.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.09× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 581 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -15.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 46.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +16.1) | — |
| [[PANC-1 (line)]] | alt | 30.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +14.1) | — |
| [[RKO (line)]] | wt | 62.6 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +10.6) | [[PH-797804 (drug)]] 5 µM 0.126× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 39.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.36× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 85.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.1) | — |
| [[SW480 (line)]] | alt | 102 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +15.5) | — |
| [[LS 180 (line)]] | wt | 215 | 1 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.62× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -14.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 51.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.11× (z +10.4) | — |
| [[SW48 (line)]] | wt | 96.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.12× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 291 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 64.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.46× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 124 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 336 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F11R]] | +0.70 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[WASF2]] | +0.70 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[CNNM4]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MGST3]] | +0.68 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[FHIP1A]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[RHPN2]] | +0.65 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[KLC3]] | +0.65 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[CARHSP1]] | +0.63 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[GPR160]] | +0.62 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.61 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[TSPAN33]] | +0.60 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[MBOAT2]] | +0.60 | +0.55 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | -0.64 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ALG8]] | -0.63 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.63 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.62 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CSTF3]] | -0.62 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MSANTD2]] | -0.62 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[ZFP91]] | -0.62 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[TSTD2]] | -0.62 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | -0.60 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[TMEM147-AS1]] | -0.60 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[DPH5-DT]] | -0.60 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[ANAPC7]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH1]] | B | CDH1 activity raises RAB11FIP1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without CDH1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[GRB7]] | B | GRB7 activity raises RAB11FIP1's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without GRB7 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[PRSS8]] | B | PRSS8 activity raises RAB11FIP1's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 3.01× lower at baseline in the lines without PRSS8 | 0.004 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[CLDN4]] | B | CLDN4 activity raises RAB11FIP1's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without CLDN4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[IRF6]] | B | IRF6 activity raises RAB11FIP1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.78× lower at baseline in the lines without IRF6 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[RNF39]] | B | RNF39 activity raises RAB11FIP1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without RNF39 | 0.009 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[BARX2]] | B | BARX2 activity raises RAB11FIP1's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.35× lower at baseline in the lines without BARX2 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[MPZL3]] | B | MPZL3 activity raises RAB11FIP1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 2.22× lower at baseline in the lines without MPZL3 | 0.018 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[FA2H]] | B | FA2H activity raises RAB11FIP1's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.50× lower at baseline in the lines without FA2H | 0.026 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[IFNLR1]] | B | IFNLR1 activity raises RAB11FIP1's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without IFNLR1 | 0.045 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[CLU]] | B | CLU activity lowers RAB11FIP1's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.93× higher at baseline in the lines without CLU | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPR160]] | B | GPR160 activity raises RAB11FIP1's level | lines that do not express GPR160 (8) vs lines expressing it (42) | 3.07× lower at baseline in the lines without GPR160 | 0.050 | ⚠ within organs, on part of the lines; also absent: PNPLA4, PRKCZ; maybe low, not absent |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 0, C 22. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Carbamazepine (drug)]] 0.5 µM | C | RAB11FIP1 activity raises the cells' numbers under Carbamazepine 0.5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.63× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[Pemetrexed (drug)]] 5 µM | C | RAB11FIP1 activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.65× the cells of the other lines | 0.014 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[Futibatinib (drug)]] 0.5 µM | C | RAB11FIP1 activity raises the cells' numbers under Futibatinib 0.5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.70× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| [[EPB41L5]] | C | RAB11FIP1 activity raises EPB41L5's level | lines that do not express RAB11FIP1 (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without RAB11FIP1 | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[Elimusertib hydrochloride (drug)]] 0.5 µM | C | RAB11FIP1 activity raises the cells' numbers under Elimusertib hydrochloride 0.5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.66× the cells of the other lines | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[Malotilate (drug)]] 0.05 µM | C | RAB11FIP1 activity lowers the cells' numbers under Malotilate 0.05 µM (makes them more sensitive) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 1.39× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[Imiquimod (maleate) (drug)]] 0.5 µM | C | RAB11FIP1 activity raises the cells' numbers under Imiquimod (maleate) 0.5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.70× the cells of the other lines | 0.051 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[Clopidogrel (drug)]] 0.05 µM | C | RAB11FIP1 activity lowers the cells' numbers under Clopidogrel 0.05 µM (makes them more sensitive) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 1.56× the cells of the other lines | 0.054 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[Ferulic acid (drug)]] 0.5 µM | C | RAB11FIP1 activity raises the cells' numbers under Ferulic acid 0.5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.60× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[Penfluridol (drug)]] 0.5 µM | C | RAB11FIP1 activity raises the cells' numbers under Penfluridol 0.5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.60× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[9-ING-41 (drug)]] 0.05 µM | C | RAB11FIP1 activity lowers the cells' numbers under 9-ING-41 0.05 µM (makes them more sensitive) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 1.35× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| cells under [[vincristine (drug)]] 5 µM | C | RAB11FIP1 activity raises the cells' numbers under vincristine 5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.53× the cells of the other lines | 0.068 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **-** arm (projection on the module's main direction -0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (10.8, -0.4); signed map (-25.5, 19.5). **Vector** length 140, 43.3% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.8 | +19.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.0 | +19.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.0 | +17.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.6 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +5.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.5 | +2.6 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -5.0 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -3.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB11 family interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:37,858,618-37,899,497 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RCP, FLJ22622, FLJ22524, Rab11-FIP1 |
| Gene groups (HGNC) | C2 domain containing; RAB11 binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6WKZ4](https://www.uniprot.org/uniprotkb/Q6WKZ4) (Rab11 family-interacting protein 1):

> A Rab11 effector protein involved in the endosomal recycling process. Also involved in controlling membrane trafficking along the phagocytic pathway and in phagocytosis. Interaction with RAB14 may function in the process of neurite formation.

**Summary**, from NCBI Gene [80223](https://www.ncbi.nlm.nih.gov/gene/80223):

> This gene encodes one of the Rab11-family interacting proteins (Rab11-FIPs), which play a role in the Rab-11 mediated recycling of vesicles. The encoded protein may be involved in endocytic sorting, trafficking of proteins including integrin subunits and epidermal growth factor receptor (EGFR), and transport between the recycling endosome and the trans-Golgi network. Alternative splicing results in multiple transcript variants. A pseudogene is described on the X chromosome. [provided by RefSeq, …

**Accessions** — [HGNC:30265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30265) · Entrez [80223](https://www.ncbi.nlm.nih.gov/gene/80223) · UniProt [Q6WKZ4](https://www.uniprot.org/uniprotkb/Q6WKZ4) · Ensembl [ENSG00000156675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156675)

## Data

Gene col 8005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8005); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8005]; `tensor/DDL_lfc|DDL_z.npy` [8005]; `embed/gene_vectors.npy` [8005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8005 or target_col == 8005). Every well: [[RAB11FIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB11FIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

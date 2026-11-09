---
symbol: "ALDH1A3"
type: "gene"
col: 11510
ensembl_id: "ENSG00000184254"
name: "aldehyde dehydrogenase 1 family member A3"
location: "15q26.3"
module: 78
arm: "+"
pooled_cpm: 36.12
n_lines_expressing: 30
n_dd_up: 25
n_dd_down: 38
n_dd_up_clean: 18
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ALDH1A3

*aldehyde dehydrogenase 1 family member A3* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.21× (z +18.6, q 0e+00, up in 23 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Menadione (drug)]] 5 µM: 1.73× (z +6.8, q 1e-09, up in 21 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.411× (z -11.5, q 7e-28, down in 24 of 27 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCND1]] (+0.59, fdr 1e-05), [[LTBP2]] (+0.58, fdr 1e-05), [[VIM-AS1]] (+0.54, fdr 5e-05); moves opposite to [[PEX11A]] (-0.49, fdr 1e-04), [[SAP30]] (-0.48, fdr 7e-05), [[GYS1]] (-0.48, fdr 6e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ITGA3]] → it (grade B ⚠); 5 go from it, the strongest it → [[ALDH1A3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.21×** | +18.6 | 0e+00 | 23/25 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.92×** | +17.0 | 0e+00 | 21/23 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +10.7 | 2e-24 | 17/24 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Menadione (drug)]] 5 µM |  | **1.73×** | +6.8 | 1e-09 | 21/27 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.40×** | +5.8 | 7e-07 | 20/28 (Panc 03.27, HOP62, …) | all doses, flat |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.56×** | +5.8 | 7e-07 | 16/28 (SW480, HT-29, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 5 µM |  | **1.71×** | +5.1 | 2e-05 | 16/28 (LOX-IMVI, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.2 | 0.002 | 14/27 (C32, Hs 766T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.82×** | +4.0 | 0.004 | 13/27 (AsPC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.007 | 10/28 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Anastrozole (drug)]] 5 µM |  | **1.72×** | +3.6 | 0.014 | 11/27 (Panc 03.27, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +3.5 | 0.021 | 14/27 (HT-29, SW480, …) | rises with dose |  |
| [[Pimitespib (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.024 | 6/28 (SW 900, BT-474, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.034 | 11/28 (SW 900, SW1417, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.035 | 5/28 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[LY2090314 (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.035 | 12/28 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Menadione (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.043 | 7/27 (H4, Hs 766T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.043 | 11/28 (LoVo, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.047 | 6/27 (SW 900, Hs 766T, …) | rises with dose |  |
| [[AZD1390 (drug)]] 5 µM |  | **1.58×** | +3.1 | 0.054 | 7/27 (LoVo, HT-29, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.411×** | -11.5 | 7e-28 | 24/27 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.437×** | -10.0 | 4e-21 | 25/28 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -9.4 | 9e-19 | 19/28 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.530×** | -8.2 | 3e-14 | 18/28 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.558×** | -7.5 | 5e-12 | 21/28 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.567×** | -7.1 | 2e-10 | 16/27 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.599×** | -6.6 | 3e-09 | 17/27 (HOP62, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.702×** | -6.5 | 7e-09 | 17/28 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.631×** | -5.9 | 2e-07 | 17/28 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.643×** | -5.7 | 6e-07 | 16/27 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -5.6 | 1e-06 | 19/27 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -5.6 | 1e-06 | 19/27 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.644×** | -5.3 | 5e-06 | 17/27 (HOP62, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -5.2 | 8e-06 | 18/28 (HS-578T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.662×** | -5.0 | 2e-05 | 15/27 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -4.7 | 9e-05 | 14/27 (Panc 03.27, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.683×** | -4.6 | 1e-04 | 12/27 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 176 | 0 | 20 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.480× (z -22.0) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.0997× (z -20.0) |
| [[SW480 (line)]] | alt | 25.4 | 2 (2 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.28× (z +10.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.162× (z -11.7) |
| [[HOP62 (line)]] | alt | 120 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.93× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 118 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -16.9) |
| [[LoVo (line)]] | wt | 34.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.6) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 32.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.132× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 22.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -12.9) |
| [[Hs 766T (line)]] | wt | 120 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 116 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +10.7) ⚠ toxic; transcription drop | [[Adagrasib (drug)]] 0.05 µM 0.608× (z -10.2) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 41.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -15.0) |
| [[SNU-423 (line)]] | alt | 10.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.50× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 84.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -10.2) |
| [[A549 (line)]] | wt | 9.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -8.8) |
| [[C32 (line)]] | wt | 9.42 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.9× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.63× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.27 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.88 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.46 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.60 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCND1]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[LTBP2]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[VIM-AS1]] | +0.54 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[ME3]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CMTM6]] | +0.50 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[ELFN2]] | +0.49 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[DOCK2]] | +0.49 | +0.43 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[SMAD3]] | +0.48 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[NFE2L3]] | +0.47 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[PLAU]] | +0.46 | +0.38 / +0.49 | both halves | 7e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[MFNG]] | +0.46 | +0.46 / +0.39 | both halves | 6e-05 |  |
| [[ITGA3]] | +0.46 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX11A]] | -0.49 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[SAP30]] | -0.48 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[GYS1]] | -0.48 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[MBD4]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TSC22D3]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[DDIT4]] | -0.44 | -0.29 / -0.37 | both halves | 3e-04 |  |
| [[PPP1R3C]] | -0.44 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[FUT11]] | -0.43 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[SMIM26]] ⚠ | -0.43 | -0.25 / -0.42 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[AVPI1]] | -0.43 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[TRADD]] | -0.43 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[ATP5MJ]] | -0.43 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[CHCHD1]] | -0.43 | -0.27 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA3]] | B | ITGA3 activity raises ALDH1A3's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 4.57× lower at baseline in the lines without ITGA3 | 0.015 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity raises ALDH1A3's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 3.42× lower at baseline in the lines without SMAD3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[TRBC2]] | B | TRBC2 activity raises ALDH1A3's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 3.07× lower at baseline in the lines without TRBC2 | 0.059 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[MANCR]] | B | MANCR activity raises ALDH1A3's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.68× lower at baseline in the lines without MANCR | 0.076 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[F2RL1]] | B | F2RL1 activity raises ALDH1A3's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without F2RL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[ELFN2]] | C | ELFN2 activity raises ALDH1A3's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 4.07× lower at baseline in the lines without ELFN2 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92; co-absent with the target |
| [[SHROOM4]] | C | SHROOM4 activity raises ALDH1A3's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 3.17× lower at baseline in the lines without SHROOM4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH1A3-AS1]] | B | ALDH1A3 activity raises ALDH1A3-AS1's level | lines that do not express ALDH1A3 (20) vs lines expressing it (30) | 1.36× lower at baseline in the lines without ALDH1A3 | 0.002 | ⚠ within organs, on part of the lines; also absent: SHROOM4, ENSG00000232386, ADAMTS16 |
| [[ITGA3]] | B | ALDH1A3 activity raises ITGA3's level | lines that do not express ALDH1A3 (20) vs lines expressing it (30) | 2.67× lower at baseline in the lines without ALDH1A3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SHROOM4, ENSG00000232386, ADAMTS16 |
| [[ELFN2]] | C | ALDH1A3 activity raises ELFN2's level | lines that do not express ALDH1A3 (20) vs lines expressing it (30) | 2.27× lower at baseline in the lines without ALDH1A3 | 0.013 | ⚠ within organs, on part of the lines; also absent: SHROOM4, ENSG00000232386, ADAMTS16; co-absent with the target |
| [[SHROOM4]] | C | ALDH1A3 activity raises SHROOM4's level | lines that do not express ALDH1A3 (20) vs lines expressing it (30) | 2.97× lower at baseline in the lines without ALDH1A3 | 0.047 | ⚠ within organs, on part of the lines; also absent: SHROOM4, ENSG00000232386, ADAMTS16; co-absent with the target |
| [[LINC00973]] | C | ALDH1A3 activity raises LINC00973's level | lines that do not express ALDH1A3 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without ALDH1A3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SHROOM4, ENSG00000232386, ADAMTS16; co-absent with the target |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.6, 10.1); signed map (13.2, 44.9). **Vector** length 89.4, 22.9% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.5 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.9 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.8 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.7 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +2.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -7.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -5.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -4.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 1 family member A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:100,877,714-100,916,626 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RALDH3; previously ALDH6 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | ANDROGEN_RESPONSE, KRAS_SIGNALING_UP |
| Reactome | 3 pathways, smallest: RA biosynthesis pathway; Signaling by Retinoic Acid; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P47895](https://www.uniprot.org/uniprotkb/P47895) (Retinaldehyde dehydrogenase 3):

> Catalyzes the NAD-dependent oxidation of aldehyde substrates, such as all-trans-retinal and all-trans-13,14-dihydroretinal, to their corresponding carboxylic acids, all-trans-retinoate and all-trans-13,14-dihydroretinoate, respectively (By similarity). High specificity for all-trans-retinal as substrate, can also accept acetaldehyde as substrate in vitro but with lower affinity. Required for the biosynthesis of normal levels of retinoate in the embryonic ocular and nasal regions; a critical …

**Summary**, from NCBI Gene [220](https://www.ncbi.nlm.nih.gov/gene/220):

> This gene encodes an aldehyde dehydrogenase enzyme that uses retinal as a substrate. Mutations in this gene have been associated with microphthalmia, isolated 8, and expression changes have also been detected in tumor cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:409](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:409) · Entrez [220](https://www.ncbi.nlm.nih.gov/gene/220) · UniProt [P47895](https://www.uniprot.org/uniprotkb/P47895) · Ensembl [ENSG00000184254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184254)

## Data

Gene col 11510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11510); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11510]; `tensor/DDL_lfc|DDL_z.npy` [11510]; `embed/gene_vectors.npy` [11510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11510 or target_col == 11510). Every well: [[ALDH1A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH1A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

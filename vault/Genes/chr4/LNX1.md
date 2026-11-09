---
symbol: "LNX1"
type: "gene"
col: 1012
ensembl_id: "ENSG00000072201"
name: "ligand of numb-protein X 1"
location: "4q12"
module: 8
arm: "+"
pooled_cpm: 20.6
n_lines_expressing: 30
n_dd_up: 24
n_dd_down: 15
n_dd_up_clean: 21
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 48
direction_downstream: 48
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# LNX1

*ligand of numb-protein X 1* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +19.7, q 0e+00, up in 23 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.668× (z -7.3, q 1e-10, down in 15 of 27 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 0.674× (z -6.9, q 2e-09, down in 11 of 26 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FMO5]] (+0.64, fdr 1e-05), [[ZNF608]] (+0.63, fdr 1e-05), [[RASSF6]] (+0.62, fdr 3e-05); moves opposite to [[CCM2]] (-0.53, fdr 1e-05), [[FBH1]] (-0.48, fdr 5e-05), [[MROH1]] (-0.48, fdr 8e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 48 arrows point to it, the strongest [[FAAH2]] → it (grade B ⚠); 48 go from it, the strongest it → [[RASGEF1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +19.7 | 0e+00 | 23/27 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.46×** | +16.5 | 0e+00 | 12/26 (HOP62, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +12.8 | 4e-35 | 21/27 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +9.5 | 2e-19 | 2/18 (A-172, HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +9.0 | 3e-17 | 15/26 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +8.8 | 1e-16 | 17/26 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.6 | 7e-16 | 6/27 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +8.6 | 7e-16 | 15/26 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.9 | 4e-10 | 1/22 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.8 | 7e-10 | 2/15 (NCI-H1792, HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.9 | 2e-07 | 11/28 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 2e-05 | 10/26 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +4.6 | 2e-04 | 9/27 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.003 | 4/26 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.009 | 5/28 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.009 | 0/25 | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.013 | 8/26 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.017 | 0/24 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.668×** | -7.3 | 1e-10 | 15/27 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.674×** | -6.9 | 2e-09 | 11/26 (LS 180, RPMI-7951, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.578×** | -5.2 | 3e-05 | 9/26 (SW1417, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.753×** | -5.2 | 3e-05 | 11/26 (HT-29, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.818×** | -5.1 | 3e-05 | 14/27 (LS 180, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.582×** | -5.1 | 3e-05 | 10/26 (SW1417, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.757×** | -5.1 | 3e-05 | 5/26 (NCI-H1792, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.767×** | -4.8 | 1e-04 | 13/26 (LS 180, BT-474, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.607×** | -4.8 | 1e-04 | 10/24 (SW1417, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.613×** | -4.7 | 2e-04 | 9/21 (LS 180, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.648×** | -4.1 | 0.002 | 12/26 (SW1417, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.677×** | -3.7 | 0.010 | 12/26 (SW1417, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.770×** | -3.4 | 0.032 | 14/26 (LS 180, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.831×** | -3.3 | 0.033 | 10/26 (HT-29, LS 180, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.833×** | -3.2 | 0.056 | 6/28 (HCT15, CFPAC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.075 | 11/26 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.849× | -3.0 | 0.093 | 1/26 (SW 900) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 83.3 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.161× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 46.4 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 39.4 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.203× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 149 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0936× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.272× (z -9.2) |
| [[LoVo (line)]] | wt | 12.1 | 5 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.93× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 86.3 | 1 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.25× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 24.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +19.2) | — |
| [[CFPAC-1 (line)]] | alt | 50.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 37.9 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.110× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 34.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -12.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 220 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0325× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.4) |
| [[HOP62 (line)]] | alt | 5.77 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.50× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -9.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 8.36 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.0671× (z -10.4) |
| [[SHP-77 (line)]] | alt | 6.43 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0908× (z -8.6) |
| [[A-172 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMO5]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[RASSF6]] | +0.62 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[PPARGC1A]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.59 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[TRIM31]] | +0.59 | +0.35 / +0.68 | both halves | 1e-04 | same gene group |
| [[ARHGEF38]] | +0.59 | +0.24 / +0.70 | both halves | 5e-04 |  |
| [[FRMD4B]] | +0.58 | +0.36 / +0.67 | both halves | 9e-05 |  |
| [[FRK]] | +0.58 | +0.32 / +0.68 | both halves | 2e-04 |  |
| [[FAAH2]] | +0.57 | +0.29 / +0.69 | both halves | 3e-04 |  |
| [[SUGT1P3-1]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PLAC8]] | +0.55 | +0.25 / +0.58 | both halves | 4e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCM2]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[FBH1]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[MROH1]] | -0.48 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[DPP9]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[DIP2A]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MAD1L1]] | -0.47 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[VPS53]] | -0.47 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[PACS2]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[LIMK1]] | -0.45 | -0.43 / -0.42 | both halves | 4e-05 | same gene group |
| [[CROCCP3-1]] | -0.45 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[PAM16]] | -0.45 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[SRD5A1]] | -0.45 | -0.43 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 38, C 10. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAAH2]] | B | FAAH2 activity raises LNX1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 4.26× lower at baseline in the lines without FAAH2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[AGR3]] | B | AGR3 activity raises LNX1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 9.45× lower at baseline in the lines without AGR3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[TJP3]] | B | TJP3 activity raises LNX1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 4.40× lower at baseline in the lines without TJP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[RNF183]] | B | RNF183 activity raises LNX1's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 4.58× lower at baseline in the lines without RNF183 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |
| [[SYNPR-AS1]] | B | SYNPR-AS1 activity raises LNX1's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 3.92× lower at baseline in the lines without SYNPR-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[ELF3]] | B | ELF3 activity raises LNX1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.50× lower at baseline in the lines without ELF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[CST6]] | B | CST6 activity raises LNX1's level | lines that do not express CST6 (42) vs lines expressing it (8) | 5.12× lower at baseline in the lines without CST6 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546 |
| [[BCAS1]] | B | BCAS1 activity raises LNX1's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 3.69× lower at baseline in the lines without BCAS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[FRMD4B]] | B | FRMD4B activity raises LNX1's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 3.56× lower at baseline in the lines without FRMD4B | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[PLEKHG6]] | B | PLEKHG6 activity raises LNX1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.95× lower at baseline in the lines without PLEKHG6 | 0.010 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[CYP4F12]] | B | CYP4F12 activity raises LNX1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.75× lower at baseline in the lines without CYP4F12 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[SLC40A1]] | B | SLC40A1 activity raises LNX1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.59× lower at baseline in the lines without SLC40A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 38, C 10. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1B]] | B | LNX1 activity raises RASGEF1B's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.56× lower at baseline in the lines without LNX1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[ATP8B1]] | B | LNX1 activity raises ATP8B1's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without LNX1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[FAAH2]] | B | LNX1 activity raises FAAH2's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.85× lower at baseline in the lines without LNX1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[EPS8]] | B | LNX1 activity raises EPS8's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without LNX1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[PAM16]] | B | LNX1 activity lowers PAM16's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.36× higher at baseline in the lines without LNX1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[MAPRE2]] | B | LNX1 activity raises MAPRE2's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without LNX1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | B | LNX1 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LNX1 (20) vs lines expressing it (28) | the lines without LNX1: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[HNMT]] | B | LNX1 activity raises HNMT's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.36× lower at baseline in the lines without LNX1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[ELF3]] | B | LNX1 activity raises ELF3's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 3.07× lower at baseline in the lines without LNX1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[ATP1B1]] | B | LNX1 activity raises ATP1B1's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.48× lower at baseline in the lines without LNX1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[TUFT1]] | B | LNX1 activity raises TUFT1's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without LNX1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[PPP1R3B]] | B | LNX1 activity raises PPP1R3B's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.85× lower at baseline in the lines without LNX1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.8, 50.1); signed map (57.9, 3.4). **Vector** length 71.8, 17.2% of its response variance represented; |z| ≥ 3 in 703 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +19.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +9.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -1.9 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | ligand of numb-protein X 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:53,459,301-53,701,405 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MPDZ, PDZRN2; previously LNX |
| Gene groups (HGNC) | Ring finger proteins; PDZ domain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBB1](https://www.uniprot.org/uniprotkb/Q8TBB1) (E3 ubiquitin-protein ligase LNX):

> E3 ubiquitin-protein ligase that mediates ubiquitination and subsequent proteasomal degradation of NUMB. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Mediates ubiquitination of isoform p66 and isoform p72 of NUMB, but not that of isoform p71 or isoform p65.; Isoform 2 provides an endocytic scaffold for IGSF5/JAM4.

**Summary**, from NCBI Gene [84708](https://www.ncbi.nlm.nih.gov/gene/84708):

> This gene encodes a membrane-bound protein that is involved in signal transduction and protein interactions. The encoded product is an E3 ubiquitin-protein ligase, which mediates ubiquitination and subsequent proteasomal degradation of proteins containing phosphotyrosine binding (PTB) domains. This protein may play an important role in tumorogenesis. Alternatively spliced transcript variants encoding distinct isoforms have been described. A pseudogene, which is located on chromosome 17, has …

**Accessions** — [HGNC:6657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6657) · Entrez [84708](https://www.ncbi.nlm.nih.gov/gene/84708) · UniProt [Q8TBB1](https://www.uniprot.org/uniprotkb/Q8TBB1) · Ensembl [ENSG00000072201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072201)

## Data

Gene col 1012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1012); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1012]; `tensor/DDL_lfc|DDL_z.npy` [1012]; `embed/gene_vectors.npy` [1012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1012 or target_col == 1012). Every well: [[LNX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LNX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

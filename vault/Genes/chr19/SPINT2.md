---
symbol: "SPINT2"
type: "gene"
col: 9508
ensembl_id: "ENSG00000167642"
name: "serine peptidase inhibitor, Kunitz type 2"
location: "19q13.2"
module: 44
arm: "+"
pooled_cpm: 83.12
n_lines_expressing: 26
n_dd_up: 13
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 11
direction_downstream: 16
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# SPINT2

*serine peptidase inhibitor, Kunitz type 2* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.76× (z +15.9, q 0e+00, up in 24 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +6.8, q 1e-09, up in 10 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.562× (z -13.7, q 3e-40, down in 24 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPCAM]] (+0.62, fdr 2e-05), [[RAB11A]] (+0.59, fdr 3e-05), [[MSLN]] (+0.59, fdr 8e-06); moves opposite to [[RPAP1]] (-0.54, fdr 3e-05), [[SCMH1]] (-0.53, fdr 5e-05), [[ZC3HC1]] (-0.52, fdr 9e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[F11R]] → it (grade B ⚠); 16 go from it, the strongest it → [[F11R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +15.9 | 0e+00 | 24/25 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +14.5 | 1e-45 | 22/22 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +12.3 | 3e-32 | 21/23 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.8 | 1e-09 | 10/25 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.38×** | +5.5 | 5e-06 | 21/24 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +5.2 | 2e-05 | 21/24 (PANC-1, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.0 | 6e-05 | 10/18 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.4 | 8e-04 | 9/26 (A-427, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.27×** | +4.0 | 0.005 | 9/24 (LS 180, PANC-1, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.015 | 17/24 (NCI-H2347, SW 900, …) | two highest doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.4 | 0.031 | 12/24 (PANC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.035 | 7/24 (LS 180, Panc 03.27, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.044 | 13/24 (LoVo, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9508.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.562×** | -13.7 | 3e-40 | 24/24 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.471×** | -12.7 | 2e-34 | 24/24 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.554×** | -9.6 | 2e-19 | 21/24 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -5.6 | 3e-06 | 19/24 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -5.0 | 6e-05 | 19/24 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.743×** | -5.0 | 6e-05 | 15/24 (SW 900, A549, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.770×** | -4.4 | 9e-04 | 13/24 (COLO 205, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.770×** | -4.4 | 9e-04 | 20/24 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.757×** | -4.3 | 0.001 | 19/24 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.781×** | -4.2 | 0.002 | 16/24 (SW 900, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.776×** | -4.1 | 0.002 | 21/25 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.633×** | -4.0 | 0.003 | 20/23 (SW48, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.776×** | -4.0 | 0.003 | 12/23 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.641×** | -3.9 | 0.004 | 15/25 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.796×** | -3.8 | 0.005 | 10/24 (Panc 03.27, AsPC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.016 | 7/24 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.825×** | -3.0 | 0.083 | 4/24 (HEC-1-A, PANC-1, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.782×** | -2.9 | 0.092 | 2/24 (A549, HCT15) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 105 | 1 (1 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -20.4) |
| [[Panc 03.27 (line)]] | alt | 128 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.7) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.383× (z -11.6) |
| [[KATO III (line)]] | alt | 236 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 73.0 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 172 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -20.9) |
| [[SW480 (line)]] | alt | 101 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 175 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -15.3) |
| [[LS 180 (line)]] | wt | 169 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -12.2) |
| [[PANC-1 (line)]] | alt | 164 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -11.9) |
| [[HCT15 (line)]] | alt | 187 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -14.3) |
| [[HT-29 (line)]] | alt | 331 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -21.8) |
| [[LoVo (line)]] | wt | 108 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 30.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 4.07× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -23.4) |
| [[A-427 (line)]] | wt | 66.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 254 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 87.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -21.2) |
| [[SW48 (line)]] | wt | 94.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.5) |
| [[A549 (line)]] | wt | 119 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 152 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -13.6) |
| [[COLO 205 (line)]] | alt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.2) |
| [[SW1417 (line)]] | alt | 136 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.471× (z -9.6) |
| [[A-172 (line)]] | wt | 6.13 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.49 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.88 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.40 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.39 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.91 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.92 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.60 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.18 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.83 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPCAM]] | +0.62 | +0.47 / +0.72 | both halves | 2e-05 | STRING 880 |
| [[RAB11A]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[MSLN]] | +0.59 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[KLK7]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.58 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CD46]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[KLK6]] | +0.56 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[LYZ]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[TSPAN1]] | +0.54 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[KLK11]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 | STRING 446 |
| [[CLDN7]] | +0.54 | +0.56 / +0.49 | both halves | 1e-05 | STRING 468 |
| [[MAL2]] | +0.53 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP1]] | -0.54 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SCMH1]] | -0.53 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[ZC3HC1]] | -0.52 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[TMEM70]] | -0.52 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[RPL7L1]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[EIF2B5]] | -0.51 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[THADA]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[MRFAP1]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MAPK1IP1L]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[NSRP1]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[THAP5]] | -0.50 | -0.57 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11R]] | B | F11R activity raises SPINT2's level | lines that do not express F11R (10) vs lines expressing it (40) | 4.41× lower at baseline in the lines without F11R | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[PRR36]] | B | PRR36 activity raises SPINT2's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 3.16× lower at baseline in the lines without PRR36 | 0.054 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[TMEM54]] | B | TMEM54 activity raises SPINT2's level | lines that do not express TMEM54 (6) vs lines expressing it (44) | 5.20× lower at baseline in the lines without TMEM54 | 0.072 | ⚠ within organs, on part of the lines; also absent: RNF135, PDP1, ENSG00000291063; maybe low, not absent |
| [[CLDN7]] | C | CLDN7 activity raises SPINT2's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 10.03× lower at baseline in the lines without CLDN7 | 1e-04 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14; co-absent with the target |
| [[TFCP2L1]] | C | TFCP2L1 activity raises SPINT2's level | lines that do not express TFCP2L1 (22) vs lines expressing it (28) | 8.96× lower at baseline in the lines without TFCP2L1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, OCLN, SPINT2; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises SPINT2's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 6.91× lower at baseline in the lines without RAB25 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises SPINT2's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 7.19× lower at baseline in the lines without EPCAM | 0.006 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises SPINT2's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 6.10× lower at baseline in the lines without MAL2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[SPINT1]] | C | SPINT1 activity raises SPINT2's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 6.14× lower at baseline in the lines without SPINT1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises SPINT2's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 5.55× lower at baseline in the lines without CEACAM6 | 0.059 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[KLK6]] | C | KLK6 activity raises SPINT2's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 5.40× lower at baseline in the lines without KLK6 | 0.092 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 8, C 8. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11R]] | B | SPINT2 activity raises F11R's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 3.97× lower at baseline in the lines without SPINT2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[ERCC6L2]] | B | SPINT2 activity lowers ERCC6L2's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 1.39× higher at baseline in the lines without SPINT2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[RHOF]] | B | SPINT2 activity raises RHOF's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without SPINT2 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[ERCC6]] | B | SPINT2 activity strengthens ERCC6's drug response | lines that do not express SPINT2 (24) vs lines expressing it (25) | the lines without SPINT2 respond 0.74× as strongly (z diff +0.87); strongest at Homoharringtonine 5 µM: 1.15x vs 1.66x (z diff +4.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2; target measured in part of the lines; both ways; artifact flags |
| [[IMPA2]] | B | SPINT2 activity raises IMPA2's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 1.86× lower at baseline in the lines without SPINT2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[KRTCAP3]] | B | SPINT2 activity raises KRTCAP3's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without SPINT2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[CD46]] | B | SPINT2 activity raises CD46's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 1.49× lower at baseline in the lines without SPINT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[TMBIM6]] | B | SPINT2 activity raises TMBIM6's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without SPINT2 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[EPCAM]] | C | SPINT2 activity raises EPCAM's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 7.48× lower at baseline in the lines without SPINT2 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2; co-absent with the target |
| [[SPINT1]] | C | SPINT2 activity raises SPINT1's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 7.35× lower at baseline in the lines without SPINT2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2; co-absent with the target |
| [[MAL2]] | C | SPINT2 activity raises MAL2's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 5.74× lower at baseline in the lines without SPINT2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2; co-absent with the target |
| [[RAB25]] | C | SPINT2 activity raises RAB25's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 4.07× lower at baseline in the lines without SPINT2 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.392). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.6, 60.0); signed map (67.3, 4.8). **Vector** length 71.8, 22.7% of its response variance represented; |z| ≥ 3 in 549 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +15.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +14.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | -2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -12.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | serine peptidase inhibitor, Kunitz type 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,244,035-38,292,615 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kop, HAI-2, HAI2 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 4 pathways, smallest: Signaling by MST1; MET Receptor Activation; Signaling by MET |
| Matched by | ensembl_id |

**Function**, from UniProt [O43291](https://www.uniprot.org/uniprotkb/O43291) (Kunitz-type protease inhibitor 2):

> Inhibitor of HGFAC. Also inhibits plasmin, and plasma and tissue kallikrein. Inhibits serine protease activity of TMPRSS13. Inhibits serine protease activity of ST14/matriptase and PRSS8/prostasin in vitro.

**Summary**, from NCBI Gene [10653](https://www.ncbi.nlm.nih.gov/gene/10653):

> This gene encodes a transmembrane protein with two extracellular Kunitz domains that inhibits a variety of serine proteases. The protein inhibits HGF activator which prevents the formation of active hepatocyte growth factor. This gene is a putative tumor suppressor, and mutations in this gene result in congenital sodium diarrhea. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:11247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11247) · Entrez [10653](https://www.ncbi.nlm.nih.gov/gene/10653) · UniProt [O43291](https://www.uniprot.org/uniprotkb/O43291) · Ensembl [ENSG00000167642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167642)

## Data

Gene col 9508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9508); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9508]; `tensor/DDL_lfc|DDL_z.npy` [9508]; `embed/gene_vectors.npy` [9508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9508 or target_col == 9508). Every well: [[SPINT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPINT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

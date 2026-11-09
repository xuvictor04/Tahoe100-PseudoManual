---
symbol: "EIF3D"
type: "gene"
col: 1937
ensembl_id: "ENSG00000100353"
name: "eukaryotic translation initiation factor 3 subunit D"
location: "22q12.3"
module: 1
arm: "+"
pooled_cpm: 109.99
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# EIF3D

*eukaryotic translation initiation factor 3 subunit D* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.55× (z +13.8, q 9e-41, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.794× (z -4.6, q 0.002, down in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.619×; ⚠ cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.534×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PES1]] (+0.78, fdr 7e-06), [[MAK16]] (+0.67, fdr 7e-06), [[RSL1D1]] (+0.65, fdr 7e-06); moves opposite to [[MPC2]] (-0.60, fdr 1e-05), [[MAGI3]] (-0.57, fdr 1e-05), [[NAA38]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +13.8 | 9e-41 | 47/49 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.25×** | +12.9 | 2e-35 | 45/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +8.8 | 4e-16 | 37/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +7.9 | 3e-13 | 0/50 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.1 | 1e-10 | 31/49 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.8 | 1e-09 | 31/48 (A498, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.7 | 1e-09 | 39/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.5 | 6e-09 | 30/44 (A-427, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.5 | 3e-06 | 29/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.62×** | +5.3 | 8e-06 | 36/48 (KATO III, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.5 | 3e-04 | 26/48 (Hs 766T, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 3e-04 | 30/48 (CFPAC-1, A498, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.010 | 28/48 (KATO III, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.016 | 20/48 (Hs 766T, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.020 | 25/48 (C32, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.026 | 7/49 (A498, CFPAC-1, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.2 | 0.039 | 14/48 (KATO III, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.059 | 13/47 (HT-29, MIA PaCa-2, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +3.0 | 0.069 | 13/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1937.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.619×; ⚠ cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.534×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.794×** | -4.6 | 0.002 | 29/47 (RKO, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.855× | -4.5 | 0.002 | 17/48 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.866× | -4.2 | 0.005 | 15/48 (A-427, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.6 | 0.043 | 22/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.843× | -3.6 | 0.043 | 17/47 (HT-29, RKO, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.844× | -3.4 | 0.054 | 16/47 (AsPC-1, J82, …) | rises with dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.842× | -3.4 | 0.054 | 20/48 (LoVo, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.892× | -3.4 | 0.054 | 15/49 (LoVo, SW480, …) | top dose only |  |
| [[Trimetrexate (drug)]] 0.5 µM |  | 0.863× | -3.1 | 0.12 | 12/48 (Hs 766T, LS 180, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.862× | -3.0 | 0.12 | 12/50 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Olanzapine (drug)]] 5 µM |  | 0.902× | -3.0 | 0.12 | 1/48 (C-33 A) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | 0.759× | -3.0 | 0.12 | 19/49 (NCI-H23, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 127 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 78.2 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +11.1) | — |
| [[LoVo (line)]] | wt | 111 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.93× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -9.4) ⚠ cell-cycle shift, explains ~10% of this change |
| [[A-172 (line)]] | wt | 57.3 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 5.29× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 71.9 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 113 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.47× (z +10.8) | — |
| [[SW480 (line)]] | alt | 144 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 3.75× (z +10.9) | — |
| [[C-33 A (line)]] | alt | 118 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.05× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 132 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.08× (z +9.2) | — |
| [[KATO III (line)]] | alt | 141 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 3.42× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 107 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.54× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 125 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.89× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 81.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 123 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 3.36× (z +9.4) | — |
| [[RKO (line)]] | wt | 168 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.93× (z +10.7) | — |
| [[A-427 (line)]] | wt | 84.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +10.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 97.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 88.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 86.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +10.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 147 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.50× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 99.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.39× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 92.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.04× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 184 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PES1]] | +0.78 | +0.81 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MAK16]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[RSL1D1]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ZNF202]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[DDX31]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[KARS1]] | +0.63 | +0.70 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 776 |
| [[BYSL]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[IMP4]] | +0.62 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[UTP14A]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[MORC2]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[EIF4B]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 666 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[MAGI3]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[NAA38]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.0, -35.2); signed map (-1.3, -44.2). **Vector** length 97.5, 26.5% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +13.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.3 | +12.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.9 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.8 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:36,510,855-36,529,184 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eIF3-p66, eIF3-zeta; previously EIF3S7 |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 3 complex subunits; Armadillo like helical domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION, MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15371](https://www.uniprot.org/uniprotkb/O15371) (Eukaryotic translation initiation factor 3 subunit D):

> mRNA cap-binding component of the eukaryotic translation initiation factor 3 (eIF-3) complex, a complex required for several steps in the initiation of protein synthesis of a specialized repertoire of mRNAs. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG …

**Summary**, from NCBI Gene [8664](https://www.ncbi.nlm.nih.gov/gene/8664):

> Eukaryotic translation initiation factor-3 (eIF3), the largest of the eIFs, is a multiprotein complex composed of at least ten nonidentical subunits. The complex binds to the 40S ribosome and helps maintain the 40S and 60S ribosomal subunits in a dissociated state. It is also thought to play a role in the formation of the 40S initiation complex by interacting with the ternary complex of eIF2/GTP/methionyl-tRNA, and by promoting mRNA binding. The protein encoded by this gene is the major RNA …

**Accessions** — [HGNC:3278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3278) · Entrez [8664](https://www.ncbi.nlm.nih.gov/gene/8664) · UniProt [O15371](https://www.uniprot.org/uniprotkb/O15371) · Ensembl [ENSG00000100353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100353)

## Data

Gene col 1937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1937); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1937]; `tensor/DDL_lfc|DDL_z.npy` [1937]; `embed/gene_vectors.npy` [1937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1937 or target_col == 1937). Every well: [[EIF3D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

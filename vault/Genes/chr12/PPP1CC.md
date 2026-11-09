---
symbol: "PPP1CC"
type: "gene"
col: 11801
ensembl_id: "ENSG00000186298"
name: "protein phosphatase 1 catalytic subunit gamma"
location: "12q24.11"
module: 35
arm: "-"
pooled_cpm: 114.58
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PPP1CC

*protein phosphatase 1 catalytic subunit gamma* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.96× (z +11.3, q 4e-27, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +6.1, q 8e-08, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.671× (z -9.5, q 1e-18, down in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (LoVo 0.402×, NCI-H460 0.505×, SW48 0.427×, AsPC-1 0.481×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.417×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH3A2]] (+0.63, fdr 1e-05), [[CDCA7L]] (+0.61, fdr 3e-05), [[RALGAPA2]] (+0.60, fdr 4e-05); moves opposite to [[ZFHX2-AS1]] (-0.62, fdr 7e-05), [[GSK3B-DT]] (-0.62, fdr 5e-05), [[AP4S1]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CLCF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.96×** | +11.3 | 4e-27 | 44/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.86×** | +10.5 | 4e-23 | 46/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.82×** | +10.2 | 5e-22 | 45/48 (A-172, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.77×** | +9.7 | 4e-20 | 47/48 (A-172, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.63×** | +8.2 | 2e-14 | 43/48 (KATO III, NCI-H460, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.62×** | +8.2 | 3e-14 | 36/49 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.55×** | +6.5 | 8e-09 | 27/44 (A-172, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.3 | 2e-08 | 2/50 (MIA PaCa-2, SW 1088) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +6.3 | 3e-08 | 44/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.1 | 8e-08 | 33/48 (LoVo, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.42×** | +6.0 | 1e-07 | 39/48 (BT-474, NCI-H460, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.38×** | +5.4 | 3e-06 | 31/48 (A-172, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.36×** | +5.2 | 7e-06 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.40×** | +5.0 | 3e-05 | 34/47 (LoVo, C32, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.73×** | +4.8 | 5e-05 | 41/48 (NCI-H2347, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.028 | 24/49 (A-172, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.082 | 17/48 (CFPAC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.086 | 16/47 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11801.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (LoVo 0.402×, NCI-H460 0.505×, SW48 0.427×, AsPC-1 0.481×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.417×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -9.5 | 1e-18 | 36/49 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.5 µM |  | 0.764× | -3.2 | 0.34 | 23/49 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.835× | -3.0 | 0.44 | 15/47 (SK-MEL-2, SW48, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 60.4 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[HOP62 (line)]] | alt | 82.5 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[NCI-H1792 (line)]] | alt | 86.4 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 119 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -11.5) |
| [[LoVo (line)]] | wt | 193 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -14.4) |
| [[SW480 (line)]] | alt | 131 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -9.3) |
| [[BT-474 (line)]] | alt | 93.1 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -9.0) |
| [[KATO III (line)]] | alt | 87.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +14.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 171 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +10.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.7) |
| [[PANC-1 (line)]] | alt | 144 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[SNU-423 (line)]] | alt | 90.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[A-427 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -15.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -10.5) |
| [[HCT15 (line)]] | alt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 131 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.46× (z +9.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[Hs 766T (line)]] | wt | 72.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 94.5 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.32× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 187 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 131 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[NCI-H23 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[RKO (line)]] | wt | 139 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.22× (z +8.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW1417 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW48 (line)]] | wt | 184 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.4) |
| [[A498 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 150 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 86.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH3A2]] | +0.63 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CDCA7L]] | +0.61 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[RALGAPA2]] | +0.60 | +0.48 / +0.40 | both halves | 4e-05 |  |
| [[PLA2G12A]] | +0.60 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[CXADR]] | +0.59 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[CREG1]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.58 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[ENPP4]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PABPC1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 | STRING 579 |
| [[RAB4A]] | +0.58 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[MPP1]] | +0.57 | +0.27 / +0.58 | both halves | 3e-04 |  |
| [[GDE1]] | +0.57 | +0.37 / +0.48 | both halves | 8e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFHX2-AS1]] | -0.62 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[GSK3B-DT]] | -0.62 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[AP4S1]] | -0.62 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[ZNF425]] | -0.62 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[LINC01829]] | -0.61 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ATXN7L3-AS1]] | -0.59 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[LTO1]] | -0.59 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TRIM39]] | -0.58 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ATE1OSP]] | -0.58 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[DENND6A-AS1]] | -0.58 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[CIBAR1-DT]] | -0.58 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[PLEKHN1]] | -0.57 | -0.51 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCF1]] | B | CLCF1 activity lowers PPP1CC's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.33× higher at baseline in the lines without CLCF1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers PPP1CC's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.42× higher at baseline in the lines without ZNF341-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **-** arm (projection on the module's main direction -0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.1, 10.5); signed map (-32.4, -35.6). **Vector** length 122, 41.3% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.0 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.9 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.5 | +10.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.6 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +2.6 | +2.3 |
|  | [[Aliskiren (drug)]] 0.5 µM |  | +2.5 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 catalytic subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,719,680-110,742,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP1C, PP1gamma |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits |
| Reactome | 39 pathways, smallest: Gain-of-function MRAS complexes activate RAF signaling; SHOC2 M1731 mutant abolishes MRAS complex function; Signaling by MRAS-complex mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P36873](https://www.uniprot.org/uniprotkb/P36873) (Serine/threonine-protein phosphatase PP1-gamma catalytic subunit):

> Protein phosphatase that associates with over 200 regulatory proteins to form highly specific holoenzymes which dephosphorylate hundreds of biological targets. Protein phosphatase 1 (PP1) is essential for cell division, and participates in the regulation of glycogen metabolism, muscle contractility and protein synthesis. Dephosphorylates RPS6KB1. Involved in regulation of ionic conductances and long-term synaptic plasticity. May play an important role in dephosphorylating substrates such as the …

**Summary**, from NCBI Gene [5501](https://www.ncbi.nlm.nih.gov/gene/5501):

> The protein encoded by this gene belongs to the protein phosphatase family, PP1 subfamily. PP1 is an ubiquitous serine/threonine phosphatase that regulates many cellular processes, including cell division. It is expressed in mammalian cells as three closely related isoforms, alpha, beta/delta and gamma, which have distinct localization patterns. This gene encodes the gamma isozyme. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:9283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9283) · Entrez [5501](https://www.ncbi.nlm.nih.gov/gene/5501) · UniProt [P36873](https://www.uniprot.org/uniprotkb/P36873) · Ensembl [ENSG00000186298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186298)

## Data

Gene col 11801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11801); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11801]; `tensor/DDL_lfc|DDL_z.npy` [11801]; `embed/gene_vectors.npy` [11801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11801 or target_col == 11801). Every well: [[PPP1CC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1CC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

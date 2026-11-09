---
symbol: "SF3B3"
type: "gene"
col: 12089
ensembl_id: "ENSG00000189091"
name: "splicing factor 3b subunit 3"
location: "16q22.1"
module: 1
arm: "+"
pooled_cpm: 107.9
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SF3B3

*splicing factor 3b subunit 3* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.77× (z +17.2, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.842× (z -4.7, q 0.001, down in 22 of 49 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.831× (z -3.6, q 0.078, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.143×, Panc 03.27 0.414×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.573×, LoVo 0.614×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.569×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATIC]] (+0.79, fdr 7e-06), [[PFAS]] (+0.74, fdr 7e-06), [[NOL11]] (+0.74, fdr 7e-06); moves opposite to [[ULK1]] (-0.72, fdr 7e-06), [[PHF1]] (-0.71, fdr 7e-06), [[SELENOK]] (-0.70, fdr 9e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.77×** | +17.2 | 0e+00 | 48/49 (SW480, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.71×** | +14.6 | 0e+00 | 47/48 (HOP62, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +14.4 | 1e-44 | 41/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +11.5 | 2e-28 | 43/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +11.1 | 1e-26 | 44/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +8.5 | 2e-15 | 42/48 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.5 | 2e-15 | 43/48 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +7.3 | 2e-11 | 36/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 7e-06 | 30/48 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +5.3 | 8e-06 | 32/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.28×** | +4.7 | 1e-04 | 28/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.025 | 21/48 (NCI-H1792, A498, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | 1.20× | +3.3 | 0.044 | 18/47 (LoVo, NCI-H1573, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.073 | 19/48 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | 1.18× | +3.1 | 0.073 | 22/48 (NCI-H1573, COLO 205, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.085 | 22/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12089.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.143×, Panc 03.27 0.414×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.573×, LoVo 0.614×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.569×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.7 | 0.001 | 22/49 (A498, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.831×** | -3.6 | 0.078 | 22/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.833×** | -3.5 | 0.078 | 21/47 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.3 | 0.15 | 21/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.2 | 0.18 | 21/48 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.856× | -3.0 | 0.22 | 18/48 (SK-MEL-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 66.4 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +16.5) | — |
| [[A549 (line)]] | wt | 105 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +19.2) | — |
| [[LOX-IMVI (line)]] | wt | 96.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 81.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.6) | — |
| [[LoVo (line)]] | wt | 91.3 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.5× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 97.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +16.1) | — |
| [[Panc 03.27 (line)]] | alt | 65.0 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.15× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 90.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.3) | — |
| [[A498 (line)]] | wt | 128 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 73.5 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 22.1× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 96.4 | 4 | 0 | [[PH-797804 (drug)]] 5 µM 11.0× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 61.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 124 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +15.0) | — |
| [[A-172 (line)]] | wt | 100.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.9) | — |
| [[A-427 (line)]] | wt | 116 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.65× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.569× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 46.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 54.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 70.1 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 50.2 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.32× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 90.5 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.37× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 68.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 100 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 8.24× (z +13.2) | — |
| [[J82 (line)]] | alt | 97.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.04× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 89.7 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.12× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 197 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.59× (z +10.1) | — |
| [[RKO (line)]] | wt | 206 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 6.93× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 172 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.45× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 106 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.96× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 74.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +9.6) | — |
| [[SW480 (line)]] | alt | 258 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +13.8) | — |
| [[BT-474 (line)]] | alt | 108 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.10× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 126 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.47× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 73.0 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.80× (z +8.6) | — |
| [[KATO III (line)]] | alt | 115 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.07× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 135 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.04× (z +10.6) | — |
| [[SNU-1 (line)]] | wt | 133 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.51× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 138 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | +0.79 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[PFAS]] | +0.74 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[NOL11]] | +0.74 | +0.75 / +0.74 | both halves | 7e-06 | same gene group |
| [[UTP15]] | +0.74 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PRRC2A]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 | same gene group |
| [[ABCE1]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[FARSB]] | +0.71 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[MRRF]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[MGA]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[GUF1]] | +0.70 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TASOR]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ULK1]] | -0.72 | -0.67 / -0.70 | both halves | 7e-06 |  |
| [[PHF1]] | -0.71 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.70 | -0.57 / -0.74 | both halves | 9e-06 |  |
| [[GABARAPL2]] | -0.70 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[FTL]] | -0.68 | -0.60 / -0.71 | both halves | 7e-06 |  |
| [[IFT20]] | -0.66 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[MACO1]] | -0.66 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[MED31]] | -0.65 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[MXD4]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[PNPLA8]] | -0.64 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[SLC25A29]] | -0.64 | -0.53 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises SF3B3's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without TERT | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity lowers SF3B3's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.55× higher at baseline in the lines without HLA-F-AS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[FTCDNL1]] | B | FTCDNL1 activity raises SF3B3's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without FTCDNL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[FAM216A]] | B | FAM216A activity raises SF3B3's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without FAM216A | 0.099 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.770). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.6, -35.5); signed map (2.5, -40.2). **Vector** length 123, 39.6% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.52 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.8 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.5 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +11.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.3 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -3.5 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 3b subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:70,523,791-70,577,670 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAP130, SF3b130, RSE1, KIAA0017 |
| Gene groups (HGNC) | SF3b complex; Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: mRNA Splicing - Minor Pathway; CHD1 and CHD2 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15393](https://www.uniprot.org/uniprotkb/Q15393) (Splicing factor 3B subunit 3):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, SF3B3 is part of the SF3B subcomplex, which is …

**Summary**, from NCBI Gene [23450](https://www.ncbi.nlm.nih.gov/gene/23450):

> This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also a component of the minor U12-type spliceosome. Subunit 3 has also been identified as a component …

**Accessions** — [HGNC:10770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10770) · Entrez [23450](https://www.ncbi.nlm.nih.gov/gene/23450) · UniProt [Q15393](https://www.uniprot.org/uniprotkb/Q15393) · Ensembl [ENSG00000189091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189091)

## Data

Gene col 12089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12089); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12089]; `tensor/DDL_lfc|DDL_z.npy` [12089]; `embed/gene_vectors.npy` [12089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12089 or target_col == 12089). Every well: [[SF3B3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF3B3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

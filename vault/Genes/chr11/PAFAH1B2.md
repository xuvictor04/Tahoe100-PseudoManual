---
symbol: "PAFAH1B2"
type: "gene"
col: 9598
ensembl_id: "ENSG00000168092"
name: "platelet activating factor acetylhydrolase 1b catalytic subunit 2"
location: "11q23.3"
module: 199
arm: "+"
pooled_cpm: 115.54
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# PAFAH1B2

*platelet activating factor acetylhydrolase 1b catalytic subunit 2* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.67× (z +13.3, q 1e-37, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.631× (z -16.9, q 0e+00, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (AsPC-1 0.418×, HOP62 0.431×, hTERT-HPNE 0.317×, PANC-1 0.568×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.527×, H4 0.399×, HepG2/C3A 0.475×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.118×, SHP-77 0.352×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG5]] (+0.72, fdr 7e-06), [[RNF216P1]] (+0.66, fdr 2e-05), [[LRFN3]] (+0.64, fdr 1e-05); moves opposite to [[UNK]] (-0.64, fdr 3e-05), [[STAP2]] (-0.64, fdr 1e-05), [[CDK3]] (-0.62, fdr 2e-05).
> It is in [[Module 199]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.67×** | +13.3 | 1e-37 | 45/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +13.3 | 1e-37 | 45/49 (SW480, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +6.7 | 5e-09 | 25/48 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +5.8 | 8e-07 | 26/48 (SW480, KATO III, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +5.0 | 8e-05 | 25/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 5e-04 | 22/49 (LoVo, SNU-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **1.21×** | +4.5 | 5e-04 | 23/45 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +4.5 | 6e-04 | 21/48 (SNU-1, COLO 205, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.19× | +4.4 | 6e-04 | 23/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.4 | 7e-04 | 20/48 (SW480, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.0 | 0.003 | 10/49 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.003 | 18/48 (SW480, KATO III, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +4.0 | 0.003 | 12/47 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 1.16× | +3.6 | 0.014 | 21/47 (LoVo, HepG2/C3A, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.4 | 0.022 | 17/38 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.13× | +3.0 | 0.091 | 5/48 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9598.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (AsPC-1 0.418×, HOP62 0.431×, hTERT-HPNE 0.317×, PANC-1 0.568×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.527×, H4 0.399×, HepG2/C3A 0.475×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.118×, SHP-77 0.352×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.631×** | -16.9 | 0e+00 | 39/48 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -12.9 | 8e-36 | 38/49 (AsPC-1, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.5 | 0.002 | 21/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.3 | 0.002 | 20/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.870× | -4.3 | 0.002 | 11/48 (AsPC-1, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.888× | -3.4 | 0.074 | 12/49 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.915× | -3.3 | 0.077 | 3/49 (Hs 766T, J82, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.912× | -3.3 | 0.077 | 8/49 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | 0.883× | -3.1 | 0.11 | 14/47 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.966× | -3.0 | 0.12 | 1/50 (NCI-H2122) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 177 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 114 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.90× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 1.88× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.7) |
| [[SW480 (line)]] | alt | 151 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 4.51× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -10.9) |
| [[A-172 (line)]] | wt | 76.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -12.6) |
| [[KATO III (line)]] | alt | 181 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.61× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 105 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 4.36× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 127 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 3.37× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -11.4) |
| [[HOP62 (line)]] | alt | 84.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -16.9) |
| [[HS-578T (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -11.9) |
| [[J82 (line)]] | alt | 80.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.8) |
| [[LoVo (line)]] | wt | 100.0 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.63× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 76.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -12.7) |
| [[PANC-1 (line)]] | alt | 170 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 2.70× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -15.1) |
| [[SK-MEL-2 (line)]] | alt | 67.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.589× (z -8.5) |
| [[SW1417 (line)]] | alt | 155 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.99× (z +10.7) | — |
| [[A498 (line)]] | wt | 93.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -10.0) |
| [[A549 (line)]] | wt | 88.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -10.9) |
| [[AN3 CA (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 123 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.355× (z -10.5) |
| [[H4 (line)]] | wt | 99.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.6) |
| [[Hs 766T (line)]] | wt | 145 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.636× (z -8.7) |
| [[HT-29 (line)]] | alt | 150 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.75× (z +12.9) | — |
| [[hTERT-HPNE (line)]] | wt | 90.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 56.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 83.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 205 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 126 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.79× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 134 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.609× (z -10.5) |
| [[RKO (line)]] | wt | 131 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.83× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 73.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -9.0) |
| [[SW 900 (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -14.5) |
| [[SW48 (line)]] | wt | 104 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.19× (z +10.0) | — |
| [[A-427 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG5]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[RNF216P1]] | +0.66 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[LRFN3]] | +0.64 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[FBXW2]] | +0.64 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[CDK9]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[MINPP1]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[NAPG]] | +0.61 | +0.69 / +0.34 | both halves | 1e-04 | pathway: Golgi-to-ER retrograde transport |
| [[TSFM]] | +0.61 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[POMGNT2]] | +0.59 | +0.65 / +0.35 | both halves | 1e-04 |  |
| [[CDC42BPB]] | +0.59 | +0.71 / +0.40 | both halves | 5e-05 |  |
| [[PAPSS1]] | +0.58 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[CAMSAP1]] | +0.58 | +0.66 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNK]] | -0.64 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[STAP2]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CDK3]] | -0.62 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[RFX1]] | -0.61 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[NFKBIB]] | -0.61 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[OFD1]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 | STRING 445 |
| [[ATF5]] | -0.60 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[KMT2E-AS1]] | -0.60 | -0.67 / -0.35 | both halves | 1e-04 |  |
| [[KRBOX5]] | -0.59 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.59 | -0.70 / -0.28 | both halves | 3e-04 |  |
| [[TAPBPL]] | -0.58 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.58 | -0.65 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.5, -1.4); signed map (-38.9, -7.9). **Vector** length 125, 36.0% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +7.7 | +13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +13.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.5 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +5.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.8 | -16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -12.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.6 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | platelet activating factor acetylhydrolase 1b catalytic subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:117,144,284-117,176,894 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 7 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [P68402](https://www.uniprot.org/uniprotkb/P68402) (Platelet-activating factor acetylhydrolase IB subunit alpha2):

> Alpha2 catalytic subunit of the cytosolic type I platelet-activating factor (PAF) acetylhydrolase (PAF-AH (I)) heterotetrameric enzyme that catalyzes the hydrolyze of the acetyl group at the sn-2 position of PAF and its analogs and modulates the action of PAF. The activity and substrate specificity of PAF-AH (I) are affected by its subunit composition. The alpha2/alpha2 homodimer (PAFAH1B2/PAFAH1B2 homodimer) hydrolyzes PAF and 1-O-alkyl-2-acetyl-sn-glycero-3-phosphorylethanolamine (AAGPE) more …

**Summary**, from NCBI Gene [5049](https://www.ncbi.nlm.nih.gov/gene/5049):

> Platelet-activating factor acetylhydrolase (PAFAH) inactivates platelet-activating factor (PAF) into acetate and LYSO-PAF. This gene encodes the beta subunit of PAFAH, the other subunits are alpha and gamma. Multiple alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:8575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8575) · Entrez [5049](https://www.ncbi.nlm.nih.gov/gene/5049) · UniProt [P68402](https://www.uniprot.org/uniprotkb/P68402) · Ensembl [ENSG00000168092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168092)

## Data

Gene col 9598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9598); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9598]; `tensor/DDL_lfc|DDL_z.npy` [9598]; `embed/gene_vectors.npy` [9598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9598 or target_col == 9598). Every well: [[PAFAH1B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAFAH1B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

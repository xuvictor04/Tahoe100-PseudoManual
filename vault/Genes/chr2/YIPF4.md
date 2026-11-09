---
symbol: "YIPF4"
type: "gene"
col: 4124
ensembl_id: "ENSG00000119820"
name: "Yip1 domain family member 4"
location: "2p22.3"
module: 74
arm: "+"
pooled_cpm: 63.97
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# YIPF4

*Yip1 domain family member 4* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.25× (z +5.4, q 4e-05, up in 24 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.13× (z +4.6, q 9e-04, up in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2030 2.42×, A-427 1.97×, MIA PaCa-2 1.80×, C-33 A 1.94×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 2.41×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.442× (z -20.5, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.416× (z -11.5, q 4e-28, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLU7]] (+0.68, fdr 1e-05), [[NBR1]] (+0.67, fdr 1e-05), [[MAU2]] (+0.67, fdr 7e-06); moves opposite to [[PPAT]] (-0.62, fdr 1e-05), [[NT5DC3]] (-0.54, fdr 2e-05), [[SLC29A1]] (-0.53, fdr 5e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4124.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2030 2.42×, A-427 1.97×, MIA PaCa-2 1.80×, C-33 A 1.94×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 2.41×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +5.4 | 4e-05 | 24/47 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +5.0 | 1e-04 | 17/48 (NCI-H2030, A-427, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.6 | 9e-04 | 15/48 (A-427, A498, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.007 | 9/49 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +4.0 | 0.009 | 14/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.012 | 11/48 (H4, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.8 | 0.014 | 5/48 (SHP-77, NCI-H2030, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.041 | 13/48 (Hs 766T, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.041 | 19/43 (SK-MEL-2, HepG2/C3A, …) | rises with dose | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.12 | 9/48 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.14 | 10/49 (C-33 A, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.442×** | -20.5 | 0e+00 | 48/48 (HT-29, NCI-H460, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.416×** | -11.5 | 4e-28 | 44/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.448×** | -10.5 | 1e-23 | 45/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.463×** | -10.1 | 7e-22 | 41/48 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.480×** | -9.6 | 7e-20 | 44/48 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.489×** | -9.4 | 6e-19 | 41/48 (AsPC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.658×** | -7.5 | 6e-12 | 42/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.752×** | -6.7 | 1e-09 | 35/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -6.7 | 1e-09 | 30/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.732×** | -5.6 | 2e-06 | 34/49 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.860× | -5.3 | 7e-06 | 17/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.675×** | -5.1 | 1e-05 | 26/37 (NCI-H1573, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.827×** | -4.7 | 9e-05 | 22/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.797×** | -4.0 | 0.002 | 18/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.745×** | -3.8 | 0.005 | 18/48 (SNU-1, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.750×** | -3.8 | 0.006 | 18/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.819×** | -3.5 | 0.013 | 14/48 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.917× | -3.0 | 0.073 | 2/49 (HS-578T, HCT15) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 72.6 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -16.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.303× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 58.5 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.320× (z -15.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.274× (z -9.2) |
| [[KATO III (line)]] | alt | 104 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.340× (z -11.8) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 60.0 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -14.6) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 57.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.454× (z -9.1) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 89.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 67.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.320× (z -15.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.451× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 57.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.357× (z -11.1) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 68.5 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.388× (z -12.1) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 59.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.262× (z -10.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 71.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.505× (z -8.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 59.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 68.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.430× (z -11.6) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 62.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 47.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.385× (z -11.6) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.392× (z -9.7) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -17.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 69.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.483× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 64.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 85.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.450× (z -10.0) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.332× (z -11.8) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.447× (z -11.7) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 70.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.356× (z -11.3) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 59.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 73.1 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0513× (z -10.3) |
| [[SW1417 (line)]] | alt | 73.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.407× (z -10.9) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 85.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.402× (z -14.6) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLU7]] | +0.68 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[NBR1]] | +0.67 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[MAU2]] | +0.67 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[TSG101]] | +0.66 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[NPIPB2]] | +0.65 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[BOD1L1]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[N4BP2L2]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[RB1CC1]] | +0.60 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[WDR48]] | +0.60 | +0.21 / +0.75 | both halves | 6e-04 |  |
| [[C11orf58]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.60 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[EAPP]] | +0.59 | +0.49 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPAT]] | -0.62 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[NT5DC3]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SLC29A1]] | -0.53 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[COLGALT1]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[FAM234B]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[TUBB]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TFRC]] | -0.49 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PAICS]] | -0.49 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[CCDC88C]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SLC25A22]] | -0.48 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[METAP1]] | -0.48 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[ST6GALNAC4]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.2, -46.5); signed map (2.3, -13.7). **Vector** length 114, 28.6% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +0.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.4 | -20.5 |
|  | [[EX229 (drug)]] 5 µM |  | -8.7 | -11.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.4 | -10.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.0 | -9.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.9 | -9.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.8 | -10.1 |

## What is on record

|  |  |
|---|---|
| Name | Yip1 domain family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:32,277,904-32,316,594 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11061, FinGER4, YIPFalpha2 |
| Gene groups (HGNC) | Yip1 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSR8](https://www.uniprot.org/uniprotkb/Q9BSR8) (Protein YIPF4):

> Involved in the maintenance of the Golgi structure.

**Summary**, from NCBI Gene [84272](https://www.ncbi.nlm.nih.gov/gene/84272):

> Predicted to be involved in endoplasmic reticulum to Golgi vesicle-mediated transport and vesicle fusion with Golgi apparatus. Located in Golgi apparatus and endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28145) · Entrez [84272](https://www.ncbi.nlm.nih.gov/gene/84272) · UniProt [Q9BSR8](https://www.uniprot.org/uniprotkb/Q9BSR8) · Ensembl [ENSG00000119820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119820)

## Data

Gene col 4124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4124); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4124]; `tensor/DDL_lfc|DDL_z.npy` [4124]; `embed/gene_vectors.npy` [4124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4124 or target_col == 4124). Every well: [[YIPF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YIPF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

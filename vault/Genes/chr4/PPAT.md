---
symbol: "PPAT"
type: "gene"
col: 4860
ensembl_id: "ENSG00000128059"
name: "phosphoribosyl pyrophosphate amidotransferase"
location: "4q12"
module: 18
arm: "+"
pooled_cpm: 51.73
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PPAT

*phosphoribosyl pyrophosphate amidotransferase* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.45× (z +19.4, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.85× (z +9.6, q 6e-20, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.767× (z -4.2, q 0.016, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METAP1]] (+0.72, fdr 7e-06), [[PODXL2]] (+0.67, fdr 2e-05), [[PAICS]] (+0.67, fdr 7e-06, ⚠ same locus), [[CCDC88C]] (+0.66, fdr 1e-05); moves opposite to [[PIN4]] (-0.63, fdr 1e-05), [[YIPF4]] (-0.62, fdr 1e-05), [[ANKRD49]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.45×** | +19.4 | 0e+00 | 48/48 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.95×** | +16.9 | 0e+00 | 48/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.56×** | +14.7 | 0e+00 | 48/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.87×** | +13.8 | 3e-41 | 38/48 (NCI-H1573, HT-29, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.05×** | +11.2 | 5e-27 | 43/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.98×** | +10.7 | 1e-24 | 39/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +9.6 | 6e-20 | 43/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.81×** | +9.3 | 1e-18 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +8.9 | 3e-17 | 37/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +8.0 | 5e-14 | 41/48 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +7.6 | 1e-12 | 35/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +7.4 | 5e-12 | 38/48 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.60×** | +7.1 | 5e-11 | 34/47 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.56×** | +7.0 | 1e-10 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.4 | 6e-09 | 30/48 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +6.0 | 8e-08 | 36/48 (NCI-H460, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.8 | 3e-07 | 29/48 (NCI-H460, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.88×** | +5.2 | 8e-06 | 32/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.87×** | +5.1 | 1e-05 | 35/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.0 | 2e-05 | 27/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 2e-04 | 24/48 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.73×** | +4.4 | 2e-04 | 27/48 (SK-MEL-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 6e-04 | 24/48 (NCI-H23, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.32×** | +4.1 | 9e-04 | 24/48 (LoVo, A498, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.002 | 19/48 (NCI-H2347, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4860.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.767×** | -4.2 | 0.016 | 27/47 (SK-MEL-2, LoVo, …) | two highest doses | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.786×** | -3.8 | 0.041 | 21/48 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.789×** | -3.6 | 0.047 | 16/47 (LoVo, A-427, …) | two highest doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.797×** | -3.6 | 0.047 | 17/48 (PANC-1, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | 0.861× | -3.4 | 0.091 | 15/48 (SK-MEL-2, A-427, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.865× | -3.3 | 0.10 | 16/48 (A-427, SHP-77, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.816× | -3.2 | 0.10 | 17/48 (SW 1088, NCI-H23, …) | rises with dose |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.870× | -3.1 | 0.11 | 9/49 (NCI-H2347, LOX-IMVI, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.758× | -3.1 | 0.11 | 17/47 (C-33 A, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.815× | -3.1 | 0.11 | 14/49 (HT-29, SNU-423, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.0 | 12 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 41.1 | 7 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.64× (z +12.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 76.5 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.80× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 30.1 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.41× (z +12.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 35.2 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +12.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.00× (z +8.8) | — |
| [[RKO (line)]] | wt | 116 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -15.2) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW1417 (line)]] | alt | 48.8 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 42.3 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +14.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1573 (line)]] | alt | 26.6 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.65× (z +14.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 37.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +12.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 32.9 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.44× (z +13.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 68.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 17.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +11.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 39.8 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 5.35× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.268× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 34.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 62.6 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.25× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 48.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 26.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 31.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 30.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 26.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.52× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HepG2_C3A (line)]] | wt | 32.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 34.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.79× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 40.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 60.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW 900 (line)]] | alt | 53.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 63.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 73.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 59.4 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.75× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 27.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 98.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.46× (z +8.9) ⚠ unreliable plate only | — |
| [[SW48 (line)]] | wt | 83.1 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.70× (z +9.6) | — |
| [[A498 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 126 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | +0.72 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[PODXL2]] | +0.67 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[PAICS]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 | same gene group; pathway: Metabolism of nucleotides; STRING 999; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[CCDC88C]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NT5DC3]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[L2HGDH]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PALS2]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[GGCT]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[UTP18]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SKP2]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[WDR36]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[POLR3G]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[EBPL]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIN4]] | -0.63 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[YIPF4]] | -0.62 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ANKRD49]] | -0.62 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SUPT7L]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.60 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PPP3CB-AS1]] | -0.59 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[CHMP4A]] | -0.59 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[ATE1OSP]] | -0.59 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ZDHHC1]] | -0.59 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[NBR1]] | -0.59 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[TSG101]] | -0.58 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[ZNF189]] | -0.58 | -0.49 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises PPAT's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without PODXL2 | 0.005 | ⚠ within organs, on part of the lines |
| [[TMEM131L]] | C | TMEM131L activity raises PPAT's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; its own permutation p |
| [[GPD1L]] | C | GPD1L activity raises PPAT's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.66× lower at baseline in the lines without GPD1L | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.0, -39.8); signed map (-7.8, -56.0). **Vector** length 93.8, 29.1% of its response variance represented; |z| ≥ 3 in 1,293 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +8.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +9.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +16.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +6.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +4.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -6.4 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.7 | +13.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.6 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +2.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphoribosyl pyrophosphate amidotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,393,362-56,435,615 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPAT, PRAT |
| Gene groups (HGNC) | Purinosome; Phosphoribosyltransferases |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 3 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06203](https://www.uniprot.org/uniprotkb/Q06203) (Amidophosphoribosyltransferase):

> Catalyzes the formation of phosphoribosylamine from phosphoribosylpyrophosphate (PRPP) and glutamine.

**Summary**, from NCBI Gene [5471](https://www.ncbi.nlm.nih.gov/gene/5471):

> The protein encoded by this gene is a member of the purine/pyrimidine phosphoribosyltransferase family. It is a regulatory allosteric enzyme that catalyzes the first step of de novo purine nucleotide biosythetic pathway. This gene and PAICS/AIRC gene, a bifunctional enzyme catalyzing steps six and seven of this pathway, are located in close proximity on chromosome 4, and divergently transcribed from an intergenic region. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:9238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9238) · Entrez [5471](https://www.ncbi.nlm.nih.gov/gene/5471) · UniProt [Q06203](https://www.uniprot.org/uniprotkb/Q06203) · Ensembl [ENSG00000128059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128059)

## Data

Gene col 4860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4860); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4860]; `tensor/DDL_lfc|DDL_z.npy` [4860]; `embed/gene_vectors.npy` [4860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4860 or target_col == 4860). Every well: [[PPAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

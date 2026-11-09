---
symbol: "NOL11"
type: "gene"
col: 5145
ensembl_id: "ENSG00000130935"
name: "nucleolar protein 11"
location: "17q24.2"
module: 1
arm: "+"
pooled_cpm: 38.63
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NOL11

*nucleolar protein 11* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +23.1, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.731× (z -7.1, q 8e-10, down in 26 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.326×, SW480 0.351×, CHP-212 0.154×, LS 180 0.345×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.143×, SW48 0.178×, SW480 0.428×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.104×; ⚠ toxic); [[CP21R7 (drug)]] 5 µM in 1 line (Hs 766T 0.0592×); [[Pimitespib (drug)]] 5 µM in 1 line (HCT15 0.0793×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT5]] (+0.77, fdr 7e-06), [[SMARCAD1]] (+0.77, fdr 7e-06), [[BYSL]] (+0.76, fdr 7e-06); moves opposite to [[TMEM50B]] (-0.67, fdr 7e-06), [[PHF1]] (-0.66, fdr 7e-06), [[ULK1]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +23.1 | 0e+00 | 46/47 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.47×** | +19.4 | 0e+00 | 47/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +17.1 | 0e+00 | 43/47 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.04×** | +16.0 | 0e+00 | 46/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.64×** | +15.1 | 0e+00 | 45/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.95×** | +12.7 | 1e-34 | 40/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.69×** | +11.8 | 6e-30 | 41/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +9.9 | 2e-21 | 38/48 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +9.0 | 2e-17 | 35/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +8.4 | 2e-15 | 36/47 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.42×** | +7.9 | 2e-13 | 28/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +7.5 | 3e-12 | 28/47 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +7.5 | 4e-12 | 27/48 (NCI-H2347, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +7.3 | 2e-11 | 33/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.38×** | +7.2 | 2e-11 | 29/47 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +6.2 | 2e-08 | 23/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.2 | 6e-06 | 24/48 (HT-29, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.6 | 9e-05 | 18/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 2e-04 | 19/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.3 | 4e-04 | 20/48 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.44×** | +4.3 | 4e-04 | 17/48 (MIA PaCa-2, A498, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5145.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.326×, SW480 0.351×, CHP-212 0.154×, LS 180 0.345×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.143×, SW48 0.178×, SW480 0.428×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (HEC-1-A 0.104×; ⚠ toxic); [[CP21R7 (drug)]] 5 µM in 1 line (Hs 766T 0.0592×); [[Pimitespib (drug)]] 5 µM in 1 line (HCT15 0.0793×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.731×** | -7.1 | 8e-10 | 26/46 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.782×** | -5.3 | 3e-05 | 19/40 (NCI-H2030, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -5.0 | 1e-04 | 14/48 (A498, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.812×** | -4.5 | 0.001 | 19/48 (LS 180, CHP-212, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.816×** | -4.4 | 0.001 | 20/47 (NCI-H460, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.847× | -4.0 | 0.006 | 16/48 (SK-MEL-2, SW 1088, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.844× | -3.9 | 0.009 | 14/47 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.864× | -3.7 | 0.018 | 13/48 (A-427, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.873× | -3.5 | 0.025 | 15/48 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.897× | -3.4 | 0.038 | 8/48 (SW480, A-427, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.862× | -3.4 | 0.038 | 16/47 (PANC-1, LoVo, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.864× | -3.3 | 0.040 | 11/47 (HOP62, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.901× | -3.3 | 0.040 | 9/48 (NCI-H2030, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.869× | -3.1 | 0.082 | 11/47 (A-427, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 52.0 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.9) | [[Lonafarnib (drug)]] 5 µM 0.104× (z -13.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 31.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.1) | — |
| [[A549 (line)]] | wt | 47.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +18.4) | — |
| [[SW480 (line)]] | alt | 67.8 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.59× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -12.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +18.2) | — |
| [[LOX-IMVI (line)]] | wt | 35.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 30.5 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 5.40× (z +13.6) | — |
| [[PANC-1 (line)]] | alt | 33.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +16.7) | — |
| [[HS-578T (line)]] | alt | 25.7 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 4.99× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 31.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.2) | — |
| [[A-172 (line)]] | wt | 28.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 35.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 35.1 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.80× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 40.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.83× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 29.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +9.8) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 24.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 33.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -11.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 27.5 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.78× (z +8.6) | [[AZD2858 (drug)]] 5 µM 0.0780× (z -9.0) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.6) | — |
| [[C32 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 94.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -12.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 38.7 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0793× (z -9.0) |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 1 | — | [[CP21R7 (drug)]] 5 µM 0.0592× (z -9.1) |
| [[J82 (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 62.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 28.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.50× (z +8.6) | — |
| [[SW48 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT5]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[SMARCAD1]] | +0.77 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[BYSL]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 847 |
| [[DDX20]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[UTP20]] | +0.75 | +0.79 / +0.74 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 979 |
| [[FASTKD2]] | +0.74 | +0.64 / +0.77 | both halves | 7e-06 | pathway: rRNA processing; STRING 458 |
| [[MAK16]] | +0.74 | +0.77 / +0.73 | both halves | 7e-06 | STRING 469 |
| [[SF3B3]] | +0.74 | +0.75 / +0.74 | both halves | 7e-06 | same gene group |
| [[QTRT2]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[NIP7]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 608 |
| [[MGA]] | +0.73 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50B]] | -0.67 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[PHF1]] | -0.66 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[ULK1]] | -0.65 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.64 | -0.74 / -0.62 | both halves | 7e-06 |  |
| [[GTF2IP4]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[GRHL1]] | -0.62 | -0.42 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.796). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-35.9, 13.1); signed map (2.2, -40.3). **Vector** length 94.9, 24.3% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.55 to 10); *Mitochondrial mRNA modification* (reactome, mean cos +0.58 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +16.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +19.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +17.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +12.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +4.5 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.3 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.7 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:67,717,931-67,744,531 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586L0724 |
| Gene groups (HGNC) | UTPa subcomplex; Small nucleolar RNA protein coding host genes |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8H0](https://www.uniprot.org/uniprotkb/Q9H8H0) (Nucleolar protein 11):

> Ribosome biogenesis factor. May be required for both optimal rDNA transcription and small subunit (SSU) pre-rRNA processing at sites A', A0, 1 and 2b.

**Summary**, from NCBI Gene [25926](https://www.ncbi.nlm.nih.gov/gene/25926):

> Enables RNA binding activity. Involved in maturation of SSU-rRNA and positive regulation of transcription of nucleolar large rRNA by RNA polymerase I. Located in nucleolus. Part of t-UTP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24557) · Entrez [25926](https://www.ncbi.nlm.nih.gov/gene/25926) · UniProt [Q9H8H0](https://www.uniprot.org/uniprotkb/Q9H8H0) · Ensembl [ENSG00000130935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130935)

## Data

Gene col 5145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5145); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5145]; `tensor/DDL_lfc|DDL_z.npy` [5145]; `embed/gene_vectors.npy` [5145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5145 or target_col == 5145). Every well: [[NOL11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOL11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "DISP1"
type: "gene"
col: 7797
ensembl_id: "ENSG00000154309"
name: "dispatched RND transporter family member 1"
location: "1q41"
module: 54
arm: "+"
pooled_cpm: 60.65
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 15
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# DISP1

*dispatched RND transporter family member 1* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.14× (z +13.1, q 1e-36, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.545× (z -10.5, q 6e-23, down in 36 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.586× (z -4.8, q 6e-05, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.136×, A498 0.288×, COLO 205 0.223×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.110×, MIA PaCa-2 0.0997×, SK-MEL-2 0.192×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.258×, SW480 0.249×, NCI-H460 0.212×; ⚠ cell-cycle shift, explains ~33% of this change); [[Entecavir (monohydrate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0670×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.404×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM170A]] (+0.54, fdr 9e-05), [[JOSD2]] (+0.52, fdr 4e-04), [[RNF13]] (+0.51, fdr 4e-05); moves opposite to [[CYB5D1]] (-0.53, fdr 3e-04), [[FBXO41]] (-0.51, fdr 6e-05), [[NID1]] (-0.50, fdr 7e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.14×** | +13.1 | 1e-36 | 42/48 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +11.2 | 1e-26 | 42/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +10.3 | 1e-22 | 42/48 (J82, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +10.1 | 7e-22 | 39/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +8.1 | 4e-14 | 36/48 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +8.0 | 1e-13 | 34/48 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.32×** | +6.9 | 5e-10 | 29/48 (NCI-H2347, LS 180, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +6.8 | 5e-10 | 37/48 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.43×** | +6.2 | 5e-08 | 32/48 (LS 180, CFPAC-1, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +5.6 | 2e-06 | 33/49 (HT-29, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.0 | 3e-05 | 23/48 (SW480, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.36×** | +4.8 | 6e-05 | 24/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +4.8 | 6e-05 | 26/48 (SW480, HT-29, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.33×** | +4.6 | 2e-04 | 24/50 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.29×** | +4.4 | 3e-04 | 24/49 (PANC-1, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +4.3 | 5e-04 | 20/48 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 6e-04 | 25/48 (J82, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +4.0 | 0.002 | 20/49 (NCI-H460, HEC-1-A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.002 | 20/47 (NCI-H460, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7797.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.136×, A498 0.288×, COLO 205 0.223×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.110×, MIA PaCa-2 0.0997×, SK-MEL-2 0.192×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.258×, SW480 0.249×, NCI-H460 0.212×; ⚠ cell-cycle shift, explains ~33% of this change); [[Entecavir (monohydrate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0670×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.404×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.545×** | -10.5 | 6e-23 | 36/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.555×** | -10.2 | 9e-22 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -9.9 | 7e-21 | 30/42 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.584×** | -9.3 | 3e-18 | 40/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.630×** | -7.4 | 2e-11 | 26/44 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.749×** | -7.0 | 2e-10 | 30/48 (NCI-H460, A549, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **0.697×** | -6.2 | 3e-08 | 32/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.676×** | -6.2 | 3e-08 | 33/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -6.2 | 3e-08 | 29/47 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.699×** | -5.7 | 8e-07 | 26/48 (A549, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.709×** | -5.5 | 2e-06 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.575×** | -5.0 | 3e-05 | 29/49 (A549, NCI-H460, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.586×** | -4.8 | 6e-05 | 24/48 (SW 900, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.816×** | -3.5 | 0.022 | 20/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.826×** | -3.0 | 0.094 | 17/48 (NCI-H460, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 284 | 2 | 17 (16 ⚠) | [[Trametinib (drug)]] 0.05 µM 1.88× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -21.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.404× (z -8.9) |
| [[PANC-1 (line)]] | alt | 55.7 | 0 | 8 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -16.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 51.6 | 2 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 54.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -17.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 95.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -14.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 110 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -14.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 39.6 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -16.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 106 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -13.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 70.7 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 22.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +9.8) | — |
| [[KATO III (line)]] | alt | 38.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -17.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 71.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.311× (z -10.0) ⚠ cell-cycle shift, explains ~76% of this change |
| [[NCI-H23 (line)]] | alt | 60.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.27× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 61.3 | 0 | 2 (1 ⚠) | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0670× (z -9.0) |
| [[A-172 (line)]] | wt | 63.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.0) | — |
| [[A-427 (line)]] | wt | 58.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 55.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 21.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -11.4) ⚠ toxic |
| [[H4 (line)]] | wt | 56.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0837× (z -8.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 51.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 63.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -10.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -15.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 62.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -10.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM170A]] | +0.54 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[JOSD2]] | +0.52 | +0.25 / +0.45 | both halves | 4e-04 |  |
| [[RNF13]] | +0.51 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[NDUFB4]] | +0.51 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[BLVRA]] | +0.51 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[TRAPPC2]] | +0.49 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[APC]] | +0.48 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[AP3S2]] | +0.48 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[CCDC127]] | +0.48 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[PSMB4]] | +0.47 | +0.48 / +0.28 | both halves | 3e-04 |  |
| [[EYA3]] | +0.46 | +0.30 / +0.42 | both halves | 2e-04 |  |
| [[JKAMP]] | +0.46 | +0.33 / +0.41 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D1]] | -0.53 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[FBXO41]] | -0.51 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[NID1]] | -0.50 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[MYO1C]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[THOC6]] | -0.48 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[ATN1]] | -0.47 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[RGL2]] | -0.44 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[BAHCC1]] | -0.43 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[EGR3]] | -0.42 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[HNRNPUL1]] | -0.42 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[ABR]] | -0.42 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[PLEKHG2]] | -0.42 | -0.46 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers DISP1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-4.6, 0.9); signed map (-18.5, -4.3). **Vector** length 75.9, 17.7% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.4 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~93% of this change | +4.3 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +6.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.9 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.0 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.6 | -10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Roxadustat (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | dispatched RND transporter family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:222,815,022-223,005,995 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DISPA, MGC13130, DKFZP434I0428, MGC16796 |
| Gene groups (HGNC) | Dispatched RND transporter family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96F81](https://www.uniprot.org/uniprotkb/Q96F81) (Protein dispatched homolog 1):

> Functions in hedgehog (Hh) signaling. Regulates the release and extracellular accumulation of cholesterol-modified hedgehog proteins and is hence required for effective production of the Hh signal (By similarity). Synergizes with SCUBE2 to cause an increase in SHH secretion.

**Summary**, from NCBI Gene [84976](https://www.ncbi.nlm.nih.gov/gene/84976):

> The pattern of cellular proliferation and differentiation that leads to normal development of embryonic structures often depends upon the localized production of secreted protein signals. Cells surrounding the source of a particular signal respond in a graded manner according to the effective concentration of the signal, and this response produces the pattern of cell types constituting the mature structure. A novel segment-polarity gene known as dispatched has been identified in Drosophila and …

**Accessions** — [HGNC:19711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19711) · Entrez [84976](https://www.ncbi.nlm.nih.gov/gene/84976) · UniProt [Q96F81](https://www.uniprot.org/uniprotkb/Q96F81) · Ensembl [ENSG00000154309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154309)

## Data

Gene col 7797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7797); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7797]; `tensor/DDL_lfc|DDL_z.npy` [7797]; `embed/gene_vectors.npy` [7797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7797 or target_col == 7797). Every well: [[DISP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DISP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

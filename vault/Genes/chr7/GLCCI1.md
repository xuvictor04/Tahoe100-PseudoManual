---
symbol: "GLCCI1"
type: "gene"
col: 2759
ensembl_id: "ENSG00000106415"
name: "glucocorticoid induced 1"
location: "7p21.3"
module: 18
arm: "-"
pooled_cpm: 114.23
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 29
n_dd_up_clean: 12
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GLCCI1

*glucocorticoid induced 1* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +9.0, q 1e-16, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.395× (z -14.9, q 0e+00, down in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.486× (z -12.0, q 6e-31, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX7A2]] (+0.56, fdr 1e-05, ⚠ COX7A2 in the vector space only through flagged drug-doses), [[LINC00685]] (+0.53, fdr 1e-05), [[AHCYL1]] (+0.53, fdr 3e-05), [[TESK2]] (+0.52, fdr 3e-05); moves opposite to [[LZTR1]] (-0.53, fdr 5e-05), [[AIMP2]] (-0.52, fdr 1e-04), [[PPP5C]] (-0.51, fdr 1e-05).
> It sits in the **-** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +9.0 | 1e-16 | 32/49 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +6.7 | 6e-09 | 28/48 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.47×** | +6.4 | 3e-08 | 34/49 (NCI-H23, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.9 | 5e-07 | 32/48 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.3 | 1e-05 | 27/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +5.1 | 4e-05 | 27/48 (SW1417, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.74×** | +4.8 | 1e-04 | 30/48 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +4.4 | 8e-04 | 26/47 (SW480, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.20×** | +4.4 | 8e-04 | 25/48 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.006 | 23/48 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.009 | 20/50 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.015 | 18/49 (A-427, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2759.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.395×** | -14.9 | 0e+00 | 36/43 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.486×** | -12.0 | 6e-31 | 41/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.544×** | -10.2 | 6e-22 | 31/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -9.9 | 5e-21 | 38/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.562×** | -8.9 | 6e-17 | 27/43 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -8.8 | 2e-16 | 36/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.684×** | -6.3 | 2e-08 | 34/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -6.1 | 8e-08 | 33/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.700×** | -6.0 | 2e-07 | 35/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.525×** | -5.6 | 1e-06 | 32/49 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.717×** | -5.6 | 1e-06 | 28/48 (NCI-H1792, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.741×** | -5.0 | 3e-05 | 26/48 (PANC-1, BT-474, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.735×** | -4.9 | 3e-05 | 26/47 (HepG2/C3A, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.746×** | -4.9 | 4e-05 | 33/48 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -4.8 | 7e-05 | 30/47 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.584×** | -4.7 | 9e-05 | 29/48 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.755×** | -4.7 | 9e-05 | 28/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -4.7 | 1e-04 | 27/48 (PANC-1, LOX-IMVI, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.752×** | -4.6 | 1e-04 | 28/48 (SW480, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.623×** | -4.1 | 1e-03 | 25/48 (SW 900, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.625×** | -4.1 | 0.001 | 25/49 (PANC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.633×** | -4.0 | 0.002 | 26/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.717×** | -4.0 | 0.002 | 21/48 (SW 900, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.799×** | -3.8 | 0.004 | 21/48 (BT-474, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 223 | 0 | 15 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.401× (z -13.7) |
| [[BT-474 (line)]] | alt | 210 | 0 | 11 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.184× (z -11.6) |
| [[SW480 (line)]] | alt | 96.7 | 4 | 4 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.404× (z -12.0) |
| [[A-172 (line)]] | wt | 152 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.289× (z -12.4) |
| [[A498 (line)]] | wt | 98.4 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.356× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 72.7 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.0) | [[Harringtonine (drug)]] 0.5 µM 0.308× (z -12.9) |
| [[KATO III (line)]] | alt | 121 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -15.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 108 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -25.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 87.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 75.3 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.408× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.406× (z -8.9) |
| [[SNU-423 (line)]] | alt | 81.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.358× (z -10.0) |
| [[C-33 A (line)]] | alt | 116 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -9.3) |
| [[H4 (line)]] | wt | 238 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -17.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 90.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.0950× (z -19.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 90.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.332× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 603 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -11.1) |
| [[SW1417 (line)]] | alt | 54.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.5) | — |
| [[C32 (line)]] | wt | 89.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.5) | [[Harringtonine (drug)]] 0.5 µM 0.359× (z -8.6) |
| [[HT-29 (line)]] | alt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 219 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 68.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.327× (z -9.4) |
| [[SHP-77 (line)]] | alt | 235 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 68.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +10.0) | — |
| [[A549 (line)]] | wt | 44.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.338× (z -8.8) |
| [[CHP-212 (line)]] | wt | 246 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0796× (z -11.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 105 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.348× (z -8.6) |
| [[HS-578T (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 77.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -19.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 47.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 94.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -9.4) |
| [[RKO (line)]] | wt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +8.8) | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -13.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 10 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX7A2]] ⚠ | +0.56 | +0.53 / +0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC00685]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[AHCYL1]] | +0.53 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[TESK2]] | +0.52 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[CCDC65]] | +0.51 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[COX4I1]] ⚠ | +0.51 | +0.47 / +0.51 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMTC2]] | +0.51 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[ANKHD1]] | +0.49 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[NDUFB11]] ⚠ | +0.49 | +0.39 / +0.53 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NR2F1]] | +0.49 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[PP2D1]] | +0.48 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[FANK1]] | +0.48 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[NDUFA2]] | +0.47 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[UXT]] | +0.47 | +0.29 / +0.45 | both halves | 2e-04 |  |
| [[COX6B1]] | +0.47 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZTR1]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[AIMP2]] | -0.52 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[PPP5C]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ARFRP1]] | -0.50 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[TRAF5]] | -0.49 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[DAGLA]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[DLST]] | -0.49 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[GTF2H3]] | -0.49 | -0.16 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[SGPL1]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PARP3]] | -0.48 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[ZFP62]] | -0.48 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[CHST3]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[FAM136A]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GLCCI1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **-** arm (projection on the module's main direction -0.268). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-21.7, -36.7); signed map (-37.3, 33.2). **Vector** length 96.1, 26.8% of its response variance represented; |z| ≥ 3 in 1,446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.6 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.0 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -6.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.0 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | glucocorticoid induced 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:7,968,796-8,094,272 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GIG18, FAM117C, TSSN1 |
| Matched by | ensembl_id |

UniProt [Q86VQ1](https://www.uniprot.org/uniprotkb/Q86VQ1) carries no function annotation.

**Summary**, from NCBI Gene [113263](https://www.ncbi.nlm.nih.gov/gene/113263):

> This gene encodes a protein of unknown function. Expression of this gene is induced by glucocorticoids and may be an early marker for glucocorticoid-induced apoptosis. Single nucleotide polymorphisms in this gene are associated with a decreased response to inhaled glucocorticoids in asthmatic patients. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:18713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18713) · Entrez [113263](https://www.ncbi.nlm.nih.gov/gene/113263) · UniProt [Q86VQ1](https://www.uniprot.org/uniprotkb/Q86VQ1) · Ensembl [ENSG00000106415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106415)

## Data

Gene col 2759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2759); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2759]; `tensor/DDL_lfc|DDL_z.npy` [2759]; `embed/gene_vectors.npy` [2759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2759 or target_col == 2759). Every well: [[GLCCI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLCCI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

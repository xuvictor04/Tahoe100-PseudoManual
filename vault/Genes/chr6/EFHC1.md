---
symbol: "EFHC1"
type: "gene"
col: 1764
ensembl_id: "ENSG00000096093"
name: "EF-hand domain containing 1"
location: "6p12.2"
module: 135
arm: "-"
pooled_cpm: 63.7
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 31
n_dd_up_clean: 5
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# EFHC1

*EF-hand domain containing 1* — 6p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.28× (z +18.4, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.522× (z -14.4, q 2e-44, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFX2]] (+0.75, fdr 7e-06), [[TMEM67]] (+0.69, fdr 7e-06), [[IFT172]] (+0.64, fdr 1e-05); moves opposite to [[ZSCAN29]] (-0.69, fdr 1e-05), [[FBXO30]] (-0.67, fdr 1e-05), [[RNF6]] (-0.66, fdr 3e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +18.4 | 0e+00 | 46/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +16.7 | 0e+00 | 45/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +15.7 | 0e+00 | 47/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +10.4 | 2e-23 | 40/47 (HT-29, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +6.8 | 1e-09 | 35/48 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.3 | 0.002 | 17/47 (A549, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.1 | 0.003 | 20/47 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.008 | 18/47 (HEC-1-A, KATO III, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.045 | 11/48 (NCI-H1573, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.067 | 12/47 (KATO III, HT-29, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.071 | 6/46 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.12 | 5/49 (C32, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1764.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.522×** | -14.4 | 2e-44 | 40/47 (A-172, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.562×** | -12.3 | 4e-32 | 37/46 (HCT15, H4, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -11.6 | 1e-28 | 36/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.612×** | -10.9 | 2e-25 | 34/47 (SNU-423, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -10.7 | 8e-25 | 39/47 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.669×** | -8.9 | 5e-17 | 29/47 (NCI-H23, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.667×** | -8.6 | 5e-16 | 29/47 (SNU-423, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.706×** | -7.7 | 1e-12 | 31/47 (NCI-H460, A498, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.715×** | -7.4 | 7e-12 | 35/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.724×** | -7.1 | 5e-11 | 32/47 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.714×** | -7.0 | 1e-10 | 30/47 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.743×** | -6.6 | 2e-09 | 27/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.727×** | -6.5 | 3e-09 | 26/42 (NCI-H23, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.751×** | -6.3 | 1e-08 | 26/47 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.823×** | -6.1 | 5e-08 | 24/47 (HEC-1-A, COLO 205, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -6.0 | 7e-08 | 27/47 (HOP62, HS-578T, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.780×** | -5.5 | 1e-06 | 24/46 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -5.2 | 5e-06 | 18/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.791×** | -5.2 | 7e-06 | 26/47 (SW 1088, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.806×** | -4.6 | 1e-04 | 23/46 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.681×** | -4.4 | 2e-04 | 25/47 (COLO 205, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.690×** | -4.3 | 4e-04 | 19/47 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.696×** | -4.2 | 6e-04 | 21/47 (Hs 766T, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.713×** | -3.9 | 0.002 | 18/47 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.2 | 3 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +12.2) | [[Harringtonine (drug)]] 0.5 µM 0.467× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 109 | 2 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0750× (z -31.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -11.9) |
| [[SW480 (line)]] | alt | 97.9 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +11.8) | [[Ixazomib citrate (drug)]] 5 µM 0.501× (z -10.6) |
| [[HOP62 (line)]] | alt | 101 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.385× (z -10.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.426× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 39.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.1) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.294× (z -12.1) |
| [[HS-578T (line)]] | alt | 95.7 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.386× (z -10.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -10.3) |
| [[PANC-1 (line)]] | alt | 78.0 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +13.1) | [[Docetaxel (drug)]] 0.05 µM 0.410× (z -12.8) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.522× (z -9.4) |
| [[COLO 205 (line)]] | alt | 163 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -8.6) |
| [[LoVo (line)]] | wt | 48.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +12.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.402× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SNU-423 (line)]] | alt | 89.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.295× (z -13.5) |
| [[A498 (line)]] | wt | 42.2 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.354× (z -11.3) |
| [[A549 (line)]] | wt | 71.0 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.313× (z -12.7) |
| [[HT-29 (line)]] | alt | 37.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.27× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -8.6) ⚠ cell-cycle shift, explains ~95% of this change |
| [[A-427 (line)]] | wt | 60.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.13× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.300× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 68.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.35× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 74.1 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.09× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.240× (z -17.3) |
| [[C-33 A (line)]] | alt | 94.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.355× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 80.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.401× (z -9.9) |
| [[H4 (line)]] | wt | 87.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -11.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 73.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -14.4) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 60.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -8.6) |
| [[J82 (line)]] | alt | 54.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.31× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 66.1 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.43× (z +8.6) | [[Harringtonine (drug)]] 0.5 µM 0.399× (z -8.9) |
| [[LS 180 (line)]] | wt | 49.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -11.0) ⚠ cell-cycle shift, explains ~95% of this change |
| [[RKO (line)]] | wt | 35.6 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.30× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 90.6 | 0 | 2 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0687× (z -9.5) |
| [[AN3 CA (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[AsPC-1 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.5) ⚠ cell-cycle shift, explains ~95% of this change |
| [[C32 (line)]] | wt | 57.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.59× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 53.3 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.279× (z -8.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 66.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.8) ⚠ cell-cycle shift, explains ~95% of this change |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX2]] | +0.75 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[TMEM67]] | +0.69 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[IFT172]] | +0.64 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ARL3]] | +0.64 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PIBF1]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[NME7]] | +0.62 | +0.57 / +0.42 | both halves | 4e-05 | STRING 849 |
| [[MLF1]] | +0.60 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[DNAAF3]] | +0.60 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[KIAA1328]] | +0.59 | +0.54 / +0.26 | both halves | 4e-04 |  |
| [[IFT122]] | +0.58 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[FBXO33]] | +0.58 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[CHEK2]] | +0.57 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN29]] | -0.69 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[FBXO30]] | -0.67 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[RNF6]] | -0.66 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ADCK1]] | -0.64 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[FAIM]] | -0.64 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[EIF5]] | -0.62 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[GRIP1]] | -0.61 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CDV3]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A21]] | -0.60 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[PRDM11]] | -0.60 | -0.57 / -0.24 | both halves | 4e-04 |  |
| [[DPH5-DT]] | -0.59 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[RHBDD3]] | -0.59 | -0.52 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers EFHC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-8.0, 8.5); signed map (-39.3, 14.0). **Vector** length 95.1, 25.1% of its response variance represented; |z| ≥ 3 in 1,332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.5 | +15.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +16.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +18.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.8 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +6.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.9 | -0.5 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.9 | +2.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | +1.7 | -0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -14.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -10.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -10.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.9 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -7.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.2 — chr6:52,362,123-52,529,886 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10466, RIB72, POC9; previously EJM1, EJM |
| Gene groups (HGNC) | EF-hand domain containing; EFHC family |
| Hallmark sets | BILE_ACID_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JVL4](https://www.uniprot.org/uniprotkb/Q5JVL4) (EF-hand domain-containing protein 1):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating. Microtubule-associated protein which regulates cell division and neuronal migration during cortical development. Necessary for radial and tangential cell migration during brain development, possibly acting as a regulator of cell morphology and process formation during migration. May enhance calcium influx through CACNA1E and stimulate programmed …

**Summary**, from NCBI Gene [114327](https://www.ncbi.nlm.nih.gov/gene/114327):

> This gene encodes an EF-hand-containing calcium binding protein. The encoded protein likely plays a role in calcium homeostasis. Mutations in this gene have been associated with susceptibility to juvenile myoclonic epilepsy and juvenile absence epilepsy. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:16406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16406) · Entrez [114327](https://www.ncbi.nlm.nih.gov/gene/114327) · UniProt [Q5JVL4](https://www.uniprot.org/uniprotkb/Q5JVL4) · Ensembl [ENSG00000096093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096093)

## Data

Gene col 1764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1764); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1764]; `tensor/DDL_lfc|DDL_z.npy` [1764]; `embed/gene_vectors.npy` [1764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1764 or target_col == 1764). Every well: [[EFHC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFHC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

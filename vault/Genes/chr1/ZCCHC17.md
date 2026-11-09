---
symbol: "ZCCHC17"
type: "gene"
col: 4294
ensembl_id: "ENSG00000121766"
name: "zinc finger CCHC-type containing 17"
location: "1p35.2"
module: 142
arm: "+"
pooled_cpm: 67.79
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# ZCCHC17

*zinc finger CCHC-type containing 17* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.00× (z +28.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.597× (z -13.0, q 5e-36, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RARS2]] (+0.79, fdr 7e-06), [[DHDDS]] (+0.74, fdr 7e-06), [[SLC30A6]] (+0.71, fdr 7e-06); moves opposite to [[VEZF1]] (-0.67, fdr 7e-06), [[LEKR1]] (-0.65, fdr 1e-05), [[POGLUT1]] (-0.64, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CIART]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.00×** | +28.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.95×** | +28.5 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.65×** | +25.7 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +13.1 | 3e-37 | 34/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +11.5 | 2e-28 | 40/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +11.3 | 2e-27 | 37/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +10.4 | 1e-23 | 40/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +9.7 | 1e-20 | 40/48 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +9.5 | 1e-19 | 35/48 (HOP62, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.30×** | +6.7 | 1e-09 | 28/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +6.2 | 3e-08 | 26/48 (HOP62, HT-29, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +5.8 | 3e-07 | 25/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.8 | 3e-07 | 24/45 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +5.3 | 4e-06 | 23/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 8e-05 | 19/49 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.008 | 10/48 (PANC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.11× | +3.7 | 0.008 | 5/48 (HOP62, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4294.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.597×** | -13.0 | 5e-36 | 41/48 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.716×** | -8.8 | 5e-16 | 33/48 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -7.8 | 2e-12 | 27/48 (hTERT-HPNE, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.753×** | -7.5 | 1e-11 | 26/48 (SK-MEL-2, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.826×** | -6.9 | 7e-10 | 23/48 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.776×** | -6.2 | 7e-08 | 22/44 (RKO, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.791×** | -5.9 | 3e-07 | 25/48 (J82, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.670×** | -5.5 | 3e-06 | 26/49 (AN3 CA, NCI-H2347, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.808×** | -5.4 | 4e-06 | 21/47 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.827×** | -5.0 | 3e-05 | 22/48 (NCI-H2347, C32, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.843× | -4.5 | 4e-04 | 21/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.4 | 4e-04 | 20/48 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.7 | 0.009 | 16/48 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.779×** | -3.4 | 0.024 | 14/36 (C32, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.882× | -3.3 | 0.037 | 12/48 (C32, KATO III, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | 0.882× | -3.1 | 0.058 | 15/49 (SW1417, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.921× | -3.0 | 0.086 | 2/48 (AsPC-1, SNU-1) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.893× | -3.0 | 0.092 | 8/48 (A498, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.893× | -3.0 | 0.092 | 6/48 (LoVo, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 69.8 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +22.1) | — |
| [[HOP62 (line)]] | alt | 85.3 | 7 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.95× (z +15.4) | — |
| [[AsPC-1 (line)]] | alt | 82.9 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -12.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 58.4 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 42.3 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.76× (z +17.7) | [[Harringtonine (drug)]] 5 µM 0.486× (z -9.3) |
| [[RKO (line)]] | wt | 59.2 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 98.7 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +11.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -13.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.447× (z -8.5) |
| [[A-172 (line)]] | wt | 44.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-427 (line)]] | wt | 50.2 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +13.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.436× (z -9.3) |
| [[A498 (line)]] | wt | 68.8 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.369× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 61.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +15.1) | — |
| [[J82 (line)]] | alt | 93.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.98× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.623× (z -9.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[PANC-1 (line)]] | alt | 73.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 78.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.77× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.364× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 41.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HS-578T (line)]] | alt | 135 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.611× (z -8.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[KATO III (line)]] | alt | 63.6 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.75× (z +14.6) | [[Harringtonine (drug)]] 5 µM 0.441× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 72.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 66.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H2347 (line)]] | alt | 65.6 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.11× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -9.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[RPMI-7951 (line)]] | alt | 86.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.97× (z +11.5) | [[Harringtonine (drug)]] 5 µM 0.329× (z -11.3) |
| [[SHP-77 (line)]] | alt | 87.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 62.8 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.39× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 47.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.58× (z +11.8) | — |
| [[C32 (line)]] | wt | 128 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.544× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.476× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 48.9 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.72× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 86.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +13.2) | — |
| [[hTERT-HPNE (line)]] | wt | 64.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.327× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 74.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +15.8) | — |
| [[LOX-IMVI (line)]] | wt | 42.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +15.3) | — |
| [[LS 180 (line)]] | wt | 65.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +14.6) | — |
| [[NCI-H1792 (line)]] | alt | 59.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.65× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 56.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +12.2) | — |
| [[SW48 (line)]] | wt | 45.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 65.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.83× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 72.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 56.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 45.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 46.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 72.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.401× (z -8.5) |
| [[AN3 CA (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 32.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0906× (z -9.1) |
| [[H4 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.2) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW 1088 (line)]] | alt | 99.0 | 0 | 1 (1 ⚠) | — | [[Larotrectinib sulfate (drug)]] 0.5 µM 0.0672× (z -10.0) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RARS2]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SLC30A6]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[GDAP2]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SAP130]] | +0.69 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SS18L1]] | +0.68 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[MFN1]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SGSM3]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.67 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[GPR89A]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CYB561D2]] | +0.67 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | -0.67 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[LEKR1]] | -0.65 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.64 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[BMI1]] | -0.63 | -0.64 / -0.49 | both halves | 2e-05 |  |
| [[NFKB1]] | -0.63 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[SCAF8]] | -0.63 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[TIGD2]] | -0.63 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.63 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PATL2]] | -0.62 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[KAT6A]] | -0.62 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[CX3CL1]] | -0.62 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[NFKBIA]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CIART]] | B | CIART activity raises ZCCHC17's level | lines that do not express CIART (22) vs lines expressing it (28) | 1.25× lower at baseline in the lines without CIART | 0.008 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, PTN, PPP2R2B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.9, -5.3); signed map (-44.7, 4.1). **Vector** length 124, 36.4% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.3 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +9.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +25.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +28.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.3 | -13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -10.3 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -8.8 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.1 | -5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,296,982-31,364,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PS1D, HSPC251, pNO40 |
| Gene groups (HGNC) | Zinc fingers CCHC-type |
| Matched by | ensembl_id |

UniProt [Q9NP64](https://www.uniprot.org/uniprotkb/Q9NP64) carries no function annotation.

**Summary**, from NCBI Gene [51538](https://www.ncbi.nlm.nih.gov/gene/51538):

> Enables identical protein binding activity. Predicted to be involved in RNA stabilization. Predicted to be located in nucleolus. Predicted to be part of cytosolic large ribosomal subunit. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30246) · Entrez [51538](https://www.ncbi.nlm.nih.gov/gene/51538) · UniProt [Q9NP64](https://www.uniprot.org/uniprotkb/Q9NP64) · Ensembl [ENSG00000121766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121766)

## Data

Gene col 4294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4294); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4294]; `tensor/DDL_lfc|DDL_z.npy` [4294]; `embed/gene_vectors.npy` [4294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4294 or target_col == 4294). Every well: [[ZCCHC17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

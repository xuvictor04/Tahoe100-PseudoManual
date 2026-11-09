---
symbol: "TSPAN9"
type: "gene"
col: 223
ensembl_id: "ENSG00000011105"
name: "tetraspanin 9"
location: "12p13.33-p13.32"
module: 84
arm: "+"
pooled_cpm: 58.14
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 23
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# TSPAN9

*tetraspanin 9* — 12p13.33-p13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.98× (z +19.9, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.559× (z -10.6, q 2e-23, down in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.460× (z -7.4, q 2e-11, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC45A4]] (+0.67, fdr 1e-05), [[INPP5A]] (+0.61, fdr 1e-05), [[SLC8B1]] (+0.60, fdr 2e-05); moves opposite to [[RC3H2]] (-0.61, fdr 1e-05), [[BMI1]] (-0.59, fdr 2e-05), [[CDKN1B]] (-0.59, fdr 2e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ITGB8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.98×** | +19.9 | 0e+00 | 43/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.89×** | +19.4 | 0e+00 | 41/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +15.2 | 0e+00 | 41/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.07×** | +13.3 | 5e-38 | 41/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +9.1 | 9e-18 | 37/48 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +9.0 | 2e-17 | 34/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +8.6 | 8e-16 | 33/48 (SW480, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.0 | 2e-10 | 29/48 (SW480, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +6.2 | 3e-08 | 33/49 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.92×** | +6.2 | 3e-08 | 28/44 (SW480, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 3e-05 | 29/49 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 6e-04 | 21/48 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.21×** | +3.3 | 0.042 | 14/48 (LS 180, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.068 | 22/48 (SW480, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.084 | 16/48 (Panc 03.27, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.559×** | -10.6 | 2e-23 | 38/49 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -9.3 | 3e-18 | 32/42 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.595×** | -8.7 | 5e-16 | 27/45 (C-33 A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -7.4 | 2e-11 | 36/49 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.693×** | -6.4 | 2e-08 | 25/48 (RPMI-7951, Hs 766T, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.741×** | -5.4 | 5e-06 | 26/48 (C32, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.747×** | -5.3 | 9e-06 | 27/48 (KATO III, A-427, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.605×** | -4.8 | 1e-04 | 22/48 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **0.772×** | -4.7 | 2e-04 | 25/48 (H4, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.817×** | -4.4 | 6e-04 | 24/48 (HOP62, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -4.2 | 0.002 | 23/48 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.729×** | -4.1 | 0.002 | 18/47 (NCI-H1792, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -4.0 | 0.003 | 24/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **0.802×** | -3.9 | 0.004 | 22/47 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.673×** | -3.8 | 0.006 | 20/47 (NCI-H23, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.675×** | -3.7 | 0.006 | 19/48 (RPMI-7951, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.010 | 22/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.773×** | -3.3 | 0.027 | 11/48 (KATO III, SW 1271, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.879× | -3.3 | 0.027 | 11/48 (C32, RKO, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.031 | 22/49 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.778×** | -3.2 | 0.031 | 16/48 (A549, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.831×** | -3.2 | 0.031 | 17/48 (PANC-1, A-172, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.845× | -3.1 | 0.052 | 16/49 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.852× | -2.9 | 0.082 | 10/48 (NCI-H1573, C32, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 51.5 | 9 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.04× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -19.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 60.9 | 6 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.34× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.163× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 24.8 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 4.49× (z +13.0) | — |
| [[C32 (line)]] | wt | 60.8 | 5 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.03× (z +10.2) | [[Harringtonine (drug)]] 0.5 µM 0.271× (z -12.1) ⚠ cell-cycle shift, explains ~23% of this change |
| [[MIA PaCa-2 (line)]] | alt | 64.6 | 4 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +25.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.97× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.4) |
| [[SW1417 (line)]] | alt | 34.2 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -14.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 33.3 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.71× (z +10.7) | — |
| [[KATO III (line)]] | alt | 26.1 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.96× (z +11.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -13.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HEC-1-A (line)]] | alt | 42.0 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.99× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 68.4 | 3 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.16× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 165 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.0812× (z -28.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.224× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 168 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[A-427 (line)]] | wt | 181 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -21.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 117 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 19.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 6.65× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 21.8 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.32× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 37.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.53× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 46.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +13.1) | — |
| [[A-172 (line)]] | wt | 96.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -12.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 17.7 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +10.8) | — |
| [[J82 (line)]] | alt | 26.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 38.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 77.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 23.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +11.5) | — |
| [[RKO (line)]] | wt | 81.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.38× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 46.7 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.02× (z +8.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -11.3) |
| [[SNU-423 (line)]] | alt | 19.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.45× (z +9.3) | — |
| [[A549 (line)]] | wt | 48.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.08× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 26.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +9.5) | — |
| [[H4 (line)]] | wt | 66.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.85× (z +8.6) | [[Docetaxel (drug)]] 0.05 µM 0.265× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~62% of this change |
| [[HOP62 (line)]] | alt | 105 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | [[Trametinib (drug)]] 0.5 µM 0.401× (z -8.6) |
| [[HS-578T (line)]] | alt | 39.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 63.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -14.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 84.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 40.4 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.01× (z +8.7) | [[Simotinib (drug)]] 5 µM 0.189× (z -8.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0885× (z -13.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 61.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.66× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 57.0 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.172× (z -15.4) |
| [[A498 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC45A4]] | +0.67 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[INPP5A]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SLC8B1]] | +0.60 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[KIF21B]] | +0.59 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ACOT7]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[DNAJB1]] | +0.58 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PLXND1]] | +0.58 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PBX4]] | +0.57 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PWWP3A]] | +0.57 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[KLHL25]] | +0.57 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.57 | +0.50 / +0.43 | both halves | 4e-05 |  |
| [[PRR5]] | +0.56 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RC3H2]] | -0.61 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[BMI1]] | -0.59 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CDKN1B]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ERCC6L2-AS1]] | -0.57 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[AASDHPPT]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[DNAI4]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[AHI1-DT]] | -0.53 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[DICER1-AS1]] | -0.52 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[LATS1]] | -0.52 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SMIM19]] | -0.52 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[SIRT1]] | -0.52 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[APOLD1]] | -0.52 | -0.47 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB8]] | B | ITGB8 activity lowers TSPAN9's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.34× higher at baseline in the lines without ITGB8 | 0.079 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TSPAN9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TSPAN9's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers TSPAN9's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.472). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.5, 5.7); signed map (-23.7, 21.8). **Vector** length 108, 29.2% of its response variance represented; |z| ≥ 3 in 1,365 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.1 | +13.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.3 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.7 | +8.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +6.5 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +3.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.0 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.3 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.0 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.8 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33-p13.32 — chr12:3,077,355-3,286,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NET-5 |
| Gene groups (HGNC) | Tetraspanin family |
| Matched by | ensembl_id |

UniProt [O75954](https://www.uniprot.org/uniprotkb/O75954) carries no function annotation.

**Summary**, from NCBI Gene [10867](https://www.ncbi.nlm.nih.gov/gene/10867):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. Alternatively spliced transcripts encoding the same protein have been identified. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:21640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21640) · Entrez [10867](https://www.ncbi.nlm.nih.gov/gene/10867) · UniProt [O75954](https://www.uniprot.org/uniprotkb/O75954) · Ensembl [ENSG00000011105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011105)

## Data

Gene col 223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 223); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 223]; `tensor/DDL_lfc|DDL_z.npy` [223]; `embed/gene_vectors.npy` [223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 223 or target_col == 223). Every well: [[TSPAN9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

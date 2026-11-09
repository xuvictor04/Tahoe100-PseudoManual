---
symbol: "ATL3"
type: "gene"
col: 11572
ensembl_id: "ENSG00000184743"
name: "atlastin GTPase 3"
location: "11q13.1"
module: 25
arm: "+"
pooled_cpm: 72.41
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ATL3

*atlastin GTPase 3* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.09× (z +21.1, q 0e+00, up in 38 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 1.15× (z +3.7, q 0.027, up in 13 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.294× (z -33.6, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARPP19]] (+0.71, fdr 7e-06), [[MOB1A]] (+0.67, fdr 1e-05), [[SETD7]] (+0.66, fdr 1e-05); moves opposite to [[ZNF503]] (-0.64, fdr 1e-05), [[SMIM26]] (-0.63, fdr 2e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[NOSIP]] (-0.60, fdr 1e-05), [[IFI27L2]] (-0.60, fdr 6e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CTSZ]] → it (grade B ⚠); 1 goes from it, the strongest it → [[UBE2V1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11572.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +21.1 | 0e+00 | 38/38 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +20.2 | 0e+00 | 45/46 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +12.6 | 4e-34 | 34/41 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.7 | 0.027 | 13/45 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.20× | +3.4 | 0.064 | 16/44 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.064 | 15/45 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.064 | 18/45 (NCI-H460, H4, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.064 | 13/45 (SNU-423, SW48, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.064 | 14/45 (H4, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.064 | 12/45 (A549, SW 900, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.064 | 13/45 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.064 | 12/46 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.064 | 15/45 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.080 | 13/45 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.18× | +3.1 | 0.080 | 17/46 (H4, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.080 | 13/44 (H4, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.080 | 11/45 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 1.11× | +3.0 | 0.080 | 4/46 (KATO III, SNU-423, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.080 | 15/46 (HS-578T, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[BI-3406 (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.099 | 8/46 (H4, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.294×** | -33.6 | 0e+00 | 43/45 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.490×** | -13.3 | 6e-38 | 38/45 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.509×** | -13.1 | 5e-37 | 41/45 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.534×** | -12.2 | 5e-32 | 42/45 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.542×** | -11.9 | 1e-30 | 30/45 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -10.1 | 8e-22 | 41/45 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -9.5 | 2e-19 | 37/45 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -8.7 | 3e-16 | 34/45 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.674×** | -7.6 | 1e-12 | 39/45 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.680×** | -7.5 | 4e-12 | 34/45 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.722×** | -6.3 | 1e-08 | 29/45 (J82, BT-474, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.772×** | -5.0 | 3e-05 | 24/45 (BT-474, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.632×** | -4.7 | 1e-04 | 26/46 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.809×** | -4.1 | 0.002 | 23/45 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.667×** | -4.1 | 0.002 | 25/45 (Panc 03.27, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.751×** | -4.0 | 0.003 | 21/45 (RPMI-7951, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -3.6 | 0.010 | 17/45 (HOP62, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.830×** | -3.6 | 0.010 | 20/45 (SK-MEL-2, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 164 | 2 (2 ⚠) | 10 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -26.8) |
| [[HS-578T (line)]] | alt | 139 | 3 (3 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -20.0) |
| [[HEC-1-A (line)]] | alt | 88.2 | 3 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.78× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -26.6) |
| [[Hs 766T (line)]] | wt | 110 | 2 (2 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.63× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -25.9) |
| [[AsPC-1 (line)]] | alt | 77.6 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.09× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -34.8) |
| [[PANC-1 (line)]] | alt | 111 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -23.3) |
| [[J82 (line)]] | alt | 120 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -24.5) |
| [[NCI-H460 (line)]] | wt | 53.1 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.95× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -25.0) |
| [[A498 (line)]] | wt | 78.7 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +15.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -19.3) |
| [[NCI-H1573 (line)]] | alt | 61.3 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -26.8) |
| [[NCI-H2030 (line)]] | alt | 132 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -14.4) |
| [[SNU-423 (line)]] | alt | 64.0 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -30.3) |
| [[A549 (line)]] | wt | 79.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 90.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 40.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -19.3) |
| [[NCI-H1792 (line)]] | alt | 68.9 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +14.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0379× (z -47.7) |
| [[NCI-H2347 (line)]] | alt | 77.4 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 69.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.8) |
| [[CFPAC-1 (line)]] | alt | 60.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -24.4) |
| [[HOP62 (line)]] | alt | 48.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -20.7) |
| [[LS 180 (line)]] | wt | 79.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -20.3) |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -19.3) |
| [[SW 900 (line)]] | alt | 65.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -18.3) |
| [[BT-474 (line)]] | alt | 63.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -17.4) |
| [[HT-29 (line)]] | alt | 65.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -17.1) |
| [[KATO III (line)]] | alt | 89.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 61.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -22.9) |
| [[SW1417 (line)]] | alt | 37.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.9) |
| [[A-427 (line)]] | wt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -17.4) |
| [[C-33 A (line)]] | alt | 77.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 72.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +11.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 41.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 75.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -15.9) |
| [[RKO (line)]] | wt | 50.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +10.1) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +15.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 78.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -17.1) |
| [[SW 1271 (line)]] | alt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.4) |
| [[SW48 (line)]] | wt | 52.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.1) |
| [[AN3 CA (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPP19]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.67 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[SETD7]] | +0.66 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[ZMPSTE24]] | +0.66 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[AIDA]] | +0.65 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[FGD5-AS1]] | +0.63 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[SLC25A24]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[USP39]] | +0.62 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[IPO5]] | +0.61 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[CTSZ]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[NAA50]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF503]] | -0.64 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.63 | -0.48 / -0.61 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NOSIP]] | -0.60 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[IFI27L2]] | -0.60 | -0.39 / -0.62 | both halves | 6e-05 |  |
| [[C19orf81]] | -0.59 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[LAMTOR5]] | -0.59 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[IMP3]] | -0.59 | -0.38 / -0.63 | both halves | 7e-05 |  |
| [[SLC25A4]] | -0.59 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[RPL36AL]] ⚠ | -0.58 | -0.46 / -0.54 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BTG1]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[KRT10]] ⚠ | -0.58 | -0.44 / -0.62 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM251]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MINCR]] | -0.58 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[CCDC85B]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSZ]] | B | CTSZ activity raises ATL3's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 2.19× lower at baseline in the lines without CTSZ | 0.023 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[SETD7]] | C | SETD7 activity raises ATL3's level | lines that do not express SETD7 (3) vs lines expressing it (47) | 2.87× lower at baseline in the lines without SETD7 | 0.071 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2V1]] | C | ATL3 activity raises UBE2V1's level | lines that do not express ATL3 (3) vs lines expressing it (47) | 1.38× lower at baseline in the lines without ATL3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARHGAP10, IQSEC2, GNE; its own permutation p |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.2, -21.1); signed map (-14.1, -38.1). **Vector** length 113, 34.7% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +21.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +20.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +5.1 | +3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.5 | +2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.6 | +3.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.4 | +3.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -33.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -7.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.5 | -4.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.5 | -2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | atlastin GTPase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:63,624,087-63,671,921 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564J0863 |
| Gene groups (HGNC) | Atlastins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6DD88](https://www.uniprot.org/uniprotkb/Q6DD88) (Atlastin-3):

> Atlastin-3 (ATL3) is a membrane-anchored GTPase that mediates the GTP-dependent fusion of endoplasmic reticulum (ER) membranes, maintaining the continuous ER network. It facilitates the formation of three-way junctions where ER tubules intersect. Two atlastin-3 on neighboring ER tubules bind GTP and form loose homodimers through the GB1/RHD3-type G domains and 3HB regions. Upon GTP hydrolysis, the 3HB regions tighten, pulling the membranes together to drive their fusion. After fusion, the …

**Summary**, from NCBI Gene [25923](https://www.ncbi.nlm.nih.gov/gene/25923):

> This gene encodes a member of a family of dynamin-like, integral membrane GTPases. The encoded protein is required for the proper formation of the network of interconnected tubules of the endoplasmic reticulum. Mutations in this gene may be associated with hereditary sensory neuropathy type IF. Alternatively spliced transcript variants that encode distinct isoforms have been described. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:24526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24526) · Entrez [25923](https://www.ncbi.nlm.nih.gov/gene/25923) · UniProt [Q6DD88](https://www.uniprot.org/uniprotkb/Q6DD88) · Ensembl [ENSG00000184743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184743)

## Data

Gene col 11572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11572); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11572]; `tensor/DDL_lfc|DDL_z.npy` [11572]; `embed/gene_vectors.npy` [11572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11572 or target_col == 11572). Every well: [[ATL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

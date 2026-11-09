---
symbol: "FLII"
type: "gene"
col: 10860
ensembl_id: "ENSG00000177731"
name: "FLII actin remodeling protein"
location: "17p11.2"
module: 54
arm: "-"
pooled_cpm: 57.05
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# FLII

*FLII actin remodeling protein* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.91× (z +20.8, q 0e+00, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.50× (z +7.9, q 3e-13, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.581× (z -10.6, q 2e-23, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN2]] (+0.67, fdr 7e-06), [[SBDS]] (+0.67, fdr 1e-05), [[SCRN1]] (+0.67, fdr 7e-06); moves opposite to [[MINCR]] (-0.62, fdr 3e-05), [[COX6C]] (-0.61, fdr 1e-05), [[COX7A2]] (-0.61, fdr 3e-05, ⚠ COX7A2 in the vector space only through flagged drug-doses), [[CHCHD1]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TCN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +20.8 | 0e+00 | 46/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +19.6 | 0e+00 | 42/42 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +13.3 | 7e-38 | 38/45 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +8.3 | 1e-14 | 31/48 (CFPAC-1, SW1417, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +7.9 | 3e-13 | 36/48 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.45×** | +7.3 | 3e-11 | 33/48 (LS 180, HT-29, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +6.4 | 9e-09 | 33/48 (A-172, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.26×** | +6.2 | 3e-08 | 24/48 (AsPC-1, SW1417, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.37×** | +6.1 | 7e-08 | 31/47 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 4e-07 | 33/48 (LS 180, NCI-H460, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.34×** | +5.6 | 9e-07 | 32/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +5.3 | 6e-06 | 29/47 (HT-29, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 2e-05 | 29/47 (LS 180, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.0 | 2e-05 | 24/48 (LS 180, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +4.8 | 6e-05 | 27/47 (HT-29, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.6 | 1e-04 | 24/49 (HT-29, LS 180, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.010 | 19/48 (LS 180, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Cyclosporin A (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.010 | 16/48 (NCI-H2347, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 1.20× | +3.4 | 0.018 | 15/48 (NCI-H23, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.3 | 0.024 | 18/48 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.039 | 14/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.0 | 0.064 | 13/48 (KATO III, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10860.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -10.6 | 2e-23 | 41/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.595×** | -10.1 | 1e-21 | 43/48 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.694×** | -10.1 | 1e-21 | 41/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.602×** | -9.9 | 7e-21 | 40/48 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.655×** | -8.2 | 2e-14 | 39/48 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.656×** | -8.2 | 2e-14 | 36/48 (RKO, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.810×** | -5.8 | 5e-07 | 23/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.845× | -4.7 | 2e-04 | 15/48 (HOP62, NCI-H460, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.798×** | -4.4 | 6e-04 | 25/48 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.671×** | -4.1 | 0.003 | 25/49 (LOX-IMVI, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.865× | -4.0 | 0.003 | 18/48 (LOX-IMVI, J82, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.822×** | -3.6 | 0.014 | 20/47 (BT-474, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | **0.826×** | -3.6 | 0.014 | 21/47 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.711×** | -3.5 | 0.021 | 22/49 (SNU-1, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.838× | -3.4 | 0.022 | 15/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.833× | -3.4 | 0.022 | 21/48 (SNU-423, A498, …) | top dose only | position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.842× | -3.4 | 0.025 | 12/48 (RKO, A-172, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.896× | -3.0 | 0.072 | 8/48 (LOX-IMVI, RKO, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.857× | -3.0 | 0.074 | 13/48 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.746×** | -3.0 | 0.076 | 14/48 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 63.3 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +17.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.497× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 102 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -12.4) |
| [[HOP62 (line)]] | alt | 95.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +13.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.459× (z -9.7) |
| [[HS-578T (line)]] | alt | 65.9 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.323× (z -11.8) |
| [[A-172 (line)]] | wt | 88.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.80× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.425× (z -10.9) |
| [[KATO III (line)]] | alt | 47.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.46× (z +9.0) | — |
| [[RKO (line)]] | wt | 84.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -9.9) |
| [[A-427 (line)]] | wt | 66.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +16.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 77.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +16.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 59.8 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.5) ⚠ cell-cycle shift, explains ~85% of this change | [[Panobinostat (drug)]] 5 µM 0.420× (z -8.6) |
| [[Hs 766T (line)]] | wt | 38.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 38.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +10.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 57.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 36.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +14.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 71.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 69.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 53.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +12.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 33.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +15.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 59.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 56.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.17× (z +11.4) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.228× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[CFPAC-1 (line)]] | alt | 45.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +9.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 49.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 64.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 45.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +12.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 52.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 45.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 46.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.2) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[A549 (line)]] | wt | 81.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +11.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 58.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 92.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -9.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 63.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN2]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[SBDS]] | +0.67 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[SCRN1]] | +0.67 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[DYNC1H1]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[CEP170B]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[DBN1]] | +0.64 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[SBDSP1]] | +0.64 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[PIEZO1]] | +0.63 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[SPTAN1]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MYOGENESIS |
| [[VPS4A]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PDAP1]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PAK2]] | +0.61 | +0.43 / +0.70 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINCR]] | -0.62 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[COX6C]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[COX7A2]] ⚠ | -0.61 | -0.45 / -0.62 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHCHD1]] | -0.61 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PTMAP2]] ⚠ | -0.61 | -0.46 / -0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6B1]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[CNOT8]] | -0.60 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[IGFBP2]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[MTF2]] | -0.59 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[NDUFA2]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[RNF145]] | -0.58 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[MNX1]] | -0.58 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.58 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCN1]] | B | TCN1 activity lowers FLII's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 1.31× higher at baseline in the lines without TCN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[GCHFR]] | B | GCHFR activity lowers FLII's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 1.18× higher at baseline in the lines without GCHFR | 0.099 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.3, -18.7); signed map (8.8, -9.4). **Vector** length 112, 32.4% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +19.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.6 | +8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +20.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +5.5 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.0 | +7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.7 | -8.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | FLII actin remodeling protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,244,815-18,258,738 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLI, FLIL, Fli1, MGC39265 |
| Gene groups (HGNC) | Gelsolin/villins |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13045](https://www.uniprot.org/uniprotkb/Q13045) (Protein flightless-1 homolog):

> Is a regulator of actin polymerization, required for proper myofibril organization and regulation of the length of sarcomeric thin filaments (By similarity). It also plays a role in the assembly of cardiomyocyte cell adhesion complexes (By similarity). Regulates cytoskeletal rearrangements involved in cytokinesis and cell migration, by inhibiting Rac1-dependent paxillin phosphorylation (By similarity). May play a role as coactivator in transcriptional activation by hormone-activated nuclear …

**Summary**, from NCBI Gene [2314](https://www.ncbi.nlm.nih.gov/gene/2314):

> This gene encodes a protein with a gelsolin-like actin binding domain and an N-terminal leucine-rich repeat-protein protein interaction domain. The protein is similar to a Drosophila protein involved in early embryogenesis and the structural organization of indirect flight muscle. The gene is located within the Smith-Magenis syndrome region on chromosome 17. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3750) · Entrez [2314](https://www.ncbi.nlm.nih.gov/gene/2314) · UniProt [Q13045](https://www.uniprot.org/uniprotkb/Q13045) · Ensembl [ENSG00000177731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177731)

## Data

Gene col 10860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10860); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10860]; `tensor/DDL_lfc|DDL_z.npy` [10860]; `embed/gene_vectors.npy` [10860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10860 or target_col == 10860). Every well: [[FLII — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLII.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

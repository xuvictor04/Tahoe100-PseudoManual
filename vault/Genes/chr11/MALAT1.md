---
symbol: "MALAT1"
type: "gene"
col: 14773
ensembl_id: "ENSG00000251562"
name: "metastasis associated lung adenocarcinoma transcript 1"
location: "11q13.1"
module: 16
arm: "-"
pooled_cpm: 43040.33
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MALAT1

*metastasis associated lung adenocarcinoma transcript 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.85× (z +11.0, q 1e-25, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.630× (z -8.0, q 7e-13, down in 43 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.519× (z -6.2, q 1e-07, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TALAM1]] (+0.88, fdr 7e-06, ⚠ same locus), [[NEAT1]] (+0.67, fdr 7e-06), [[SPAG9]] (+0.54, fdr 2e-05), [[CALCOCO2]] (+0.53, fdr 1e-05); moves opposite to [[UQCRFS1]] (-0.61, fdr 3e-05), [[CSTF1]] (-0.58, fdr 3e-05), [[RAVER1]] (-0.57, fdr 3e-05).
> It sits in the **-** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14773.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +11.0 | 1e-25 | 47/48 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +9.5 | 8e-19 | 47/48 (HT-29, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.7 | 7e-16 | 47/49 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +8.6 | 8e-16 | 40/48 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +8.5 | 2e-15 | 41/44 (HEC-1-A, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +8.4 | 4e-15 | 41/48 (H4, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +7.9 | 2e-13 | 40/48 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +7.9 | 2e-13 | 45/48 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.53×** | +7.6 | 1e-12 | 45/48 (H4, COLO 205, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +7.5 | 4e-12 | 41/48 (SHP-77, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +7.3 | 2e-11 | 38/48 (H4, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +7.1 | 6e-11 | 42/45 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.5 | 3e-09 | 44/45 (HS-578T, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.39×** | +5.9 | 1e-07 | 42/49 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.8 | 2e-07 | 34/48 (HS-578T, HCT15, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +5.4 | 2e-06 | 24/48 (COLO 205, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +4.7 | 1e-04 | 44/49 (HS-578T, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 1e-04 | 47/48 (SW1417, COLO 205, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.001 | 34/48 (COLO 205, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.007 | 27/48 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Hesperidin (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.048 | 28/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -8.0 | 7e-13 | 43/47 (A-427, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.519×** | -6.2 | 1e-07 | 45/49 (LOX-IMVI, NCI-H1792, …) | all doses, flat | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.711×** | -6.1 | 1e-07 | 44/48 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.553×** | -5.6 | 3e-06 | 45/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.743×** | -5.4 | 1e-05 | 46/48 (HS-578T, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.732×** | -5.3 | 1e-05 | 39/47 (BT-474, LOX-IMVI, …) | all doses, flat |  |
| [[Decitabine (drug)]] 0.05 µM |  | **0.782×** | -4.1 | 0.003 | 42/47 (C-33 A, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.820×** | -3.6 | 0.025 | 31/48 (SW 1271, C32, …) | inconsistent across doses |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **0.761×** | -3.5 | 0.025 | 43/48 (HCT15, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | **0.810×** | -3.5 | 0.025 | 39/47 (HepG2/C3A, HS-578T, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.029 | 44/48 (HT-29, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Malotilate (drug)]] 0.5 µM |  | 0.834× | -3.3 | 0.048 | 24/48 (C-33 A, A-172, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.3 | 0.048 | 0/50 | inconsistent across doses |  |
| [[Hesperidin (drug)]] 5 µM |  | 0.835× | -3.1 | 0.072 | 22/48 (NCI-H1792, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.072 | 19/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.846× | -3.0 | 0.086 | 17/48 (SHP-77, LoVo, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 0.5 µM |  | 0.846× | -3.0 | 0.086 | 14/48 (HepG2/C3A, COLO 205, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 34,363 | 13 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +18.4) | — |
| [[H4 (line)]] | wt | 28,630 | 12 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +18.6) | — |
| [[HEC-1-A (line)]] | alt | 28,488 | 12 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +13.7) | — |
| [[SW480 (line)]] | alt | 39,347 | 11 (4 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +15.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.498× (z -9.6) ⚠ toxic |
| [[A498 (line)]] | wt | 17,730 | 9 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.76× (z +16.3) | — |
| [[COLO 205 (line)]] | alt | 56,605 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +18.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.599× (z -8.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 42,883 | 9 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +13.7) | — |
| [[A-427 (line)]] | wt | 44,790 | 4 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.04× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.478× (z -11.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.555× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 19,587 | 5 (4 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.74× (z +12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 1.85× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.563× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.359× (z -8.7) |
| [[HOP62 (line)]] | alt | 57,629 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +13.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.505× (z -10.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.556× (z -8.5) |
| [[HT-29 (line)]] | alt | 58,528 | 4 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -11.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 42,295 | 5 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.51× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.448× (z -11.5) |
| [[SHP-77 (line)]] | alt | 35,303 | 5 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.60× (z +15.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.491× (z -10.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.629× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 53,933 | 3 (1 ⚠) | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.05× (z +10.2) | [[TAK-901 (drug)]] 0.05 µM 0.485× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 24,009 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.04× (z +17.1) | — |
| [[RPMI-7951 (line)]] | alt | 33,287 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +13.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.524× (z -9.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 56,720 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +15.0) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.603× (z -8.8) |
| [[SW48 (line)]] | wt | 28,552 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.12× (z +14.3) | — |
| [[A-172 (line)]] | wt | 42,523 | 4 | 0 | [[Auranofin (drug)]] 5 µM 1.85× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 25,411 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.9) | — |
| [[C32 (line)]] | wt | 40,829 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.3) | — |
| [[LoVo (line)]] | wt | 38,360 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.26× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 40,967 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.26× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 44,303 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 19,889 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 1.86× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 53,638 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 1.88× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 44,117 | 4 | 0 | [[Auranofin (drug)]] 5 µM 1.98× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 81,745 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +17.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.558× (z -8.5) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 43,587 | 3 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.59× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.76× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 42,817 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 61,342 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.51× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.497× (z -9.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.539× (z -8.6) |
| [[J82 (line)]] | alt | 48,871 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.0) | — |
| [[KATO III (line)]] | alt | 36,586 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +12.8) | — |
| [[RKO (line)]] | wt | 24,791 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 54,518 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 33,211 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.94× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 23,340 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.81× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.68× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 63,531 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 106,203 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.487× (z -9.7) |
| [[C-33 A (line)]] | alt | 58,173 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.585× (z -9.1) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 36,028 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.74× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 47,925 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 18,150 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.07× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 35,150 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2122 (line)]] | alt | 53,365 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61,658 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48,545 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38,955 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36,417 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47,371 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*29 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TALAM1]] | +0.88 | +0.79 / +0.91 | both halves | 7e-06 | same gene group; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NEAT1]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 | same gene group |
| [[SPAG9]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CALCOCO2]] | +0.53 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SNAP23]] | +0.52 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[CAST]] | +0.52 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[CALN1]] | +0.52 | +0.21 / +0.57 | both halves | 7e-04 |  |
| [[KTN1]] | +0.50 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[BEST1]] | +0.49 | +0.28 / +0.55 | both halves | 3e-04 |  |
| [[SAMD4B]] | +0.48 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[PRKCI]] | +0.48 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[CTC1]] | +0.47 | +0.29 / +0.50 | both halves | 2e-04 |  |
| [[ST13]] | +0.46 | +0.28 / +0.54 | both halves | 3e-04 |  |

## Genes that move opposite

*71 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRFS1]] | -0.61 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[CSTF1]] | -0.58 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[RAVER1]] | -0.57 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[FBXO5]] | -0.56 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[DDX20]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[NUP35]] | -0.55 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[SUV39H1]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[CTCF]] | -0.54 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[ADO]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TMEM11]] | -0.53 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[ABT1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[PATZ1]] | -0.52 | -0.42 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.257). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-55.6, -5.1); signed map (-20.7, 22.5). **Vector** length 156, 56.7% of its response variance represented; |z| ≥ 3 in 2,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.6 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.1 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.7 | +7.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +9.5 | +7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.5 | +7.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.8 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +5.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.7 | +4.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -13.1 | -8.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -12.2 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -10.5 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -9.5 | -6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -8.9 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.7 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.5 | -5.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -4.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | metastasis associated lung adenocarcinoma transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q13.1 — chr11:65,497,640-65,508,073 (+) |
| Ensembl biotype | lncRNA |
| Also known as | miPEP-52, PRO1073, MALAT-1, NCRNA00047, HCN, NEAT2, LINC00047, mascRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [378938](https://www.ncbi.nlm.nih.gov/gene/378938):

> This gene produces a precursor transcript from which a long non-coding RNA is derived by RNase P cleavage of a tRNA-like small ncRNA (known as mascRNA) from its 3' end. The resultant mature transcript lacks a canonical poly(A) tail but is instead stabilized by a 3' triple helical structure. This transcript is retained in the nucleus where it is thought to form molecular scaffolds for ribonucleoprotein complexes. It may act as a transcriptional regulator for numerous genes, including some genes …

**Accessions** — [HGNC:29665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29665) · Entrez [378938](https://www.ncbi.nlm.nih.gov/gene/378938) · Ensembl [ENSG00000251562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251562)

## Data

Gene col 14773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14773); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14773]; `tensor/DDL_lfc|DDL_z.npy` [14773]; `embed/gene_vectors.npy` [14773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14773 or target_col == 14773). Every well: [[MALAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MALAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

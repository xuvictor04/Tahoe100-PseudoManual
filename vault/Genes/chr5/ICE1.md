---
symbol: "ICE1"
type: "gene"
col: 8883
ensembl_id: "ENSG00000164151"
name: "interactor of little elongation complex ELL subunit 1"
location: "5p15.32"
module: 59
arm: "-"
pooled_cpm: 132.36
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# ICE1

*interactor of little elongation complex ELL subunit 1* — 5p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.60× (z +16.3, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.510× (z -17.4, q 0e+00, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.848× (z -6.0, q 2e-07, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SNU-1 0.157×, J82 0.313×, A549 0.320×, HS-578T 0.329×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HS-578T 0.291×, J82 0.328×, PANC-1 0.405×, A498 0.365×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HS-578T 0.265×, NCI-H2030 0.296×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPTP]] (+0.65, fdr 1e-05), [[GTF2E1]] (+0.61, fdr 1e-05), [[ZNF142]] (+0.60, fdr 7e-06); moves opposite to [[ABCA5]] (-0.58, fdr 1e-05), [[VAMP2]] (-0.56, fdr 1e-05), [[PNISR]] (-0.54, fdr 2e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.60×** | +16.3 | 0e+00 | 46/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.44×** | +15.7 | 0e+00 | 45/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +12.0 | 6e-31 | 43/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.47×** | +9.9 | 8e-21 | 38/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +9.7 | 2e-20 | 40/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +6.2 | 5e-08 | 33/48 (PANC-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +6.2 | 6e-08 | 26/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.1 | 7e-08 | 25/38 (NCI-H1573, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +6.0 | 1e-07 | 28/48 (Hs 766T, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +5.6 | 9e-07 | 30/48 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.4 | 4e-06 | 23/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +5.2 | 1e-05 | 25/48 (HOP62, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +5.1 | 2e-05 | 24/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +4.7 | 1e-04 | 22/50 (RKO, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +4.3 | 7e-04 | 21/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.005 | 18/48 (SW480, LS 180, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.7 | 0.006 | 14/48 (LS 180, SW480, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.14× | +3.4 | 0.016 | 9/47 (J82, LS 180, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.020 | 18/49 (SW480, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.035 | 9/48 (NCI-H460, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | 1.12× | +3.0 | 0.058 | 4/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.067 | 13/49 (C-33 A, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8883.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SNU-1 0.157×, J82 0.313×, A549 0.320×, HS-578T 0.329×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HS-578T 0.291×, J82 0.328×, PANC-1 0.405×, A498 0.365×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HS-578T 0.265×, NCI-H2030 0.296×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.510×** | -17.4 | 0e+00 | 42/49 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.558×** | -14.5 | 4e-45 | 40/44 (SNU-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.645×** | -9.5 | 6e-19 | 31/45 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -6.3 | 4e-08 | 0/50 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -6.0 | 2e-07 | 22/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.741×** | -5.5 | 3e-06 | 34/48 (A-427, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.853× | -4.1 | 0.003 | 17/48 (C-33 A, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.840× | -4.1 | 0.003 | 20/49 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.802×** | -4.1 | 0.003 | 23/48 (A-427, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.843× | -4.0 | 0.004 | 19/48 (H4, SW48, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.899× | -3.9 | 0.005 | 12/48 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -3.5 | 0.019 | 23/45 (SHP-77, H4, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.917× | -3.2 | 0.066 | 1/49 (hTERT-HPNE) | two highest doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.847× | -3.1 | 0.091 | 10/49 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 137 | 7 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.45× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -13.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 143 | 7 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.04× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -14.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 76.9 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 144 | 4 (1 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.85× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -14.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 157 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.65× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -11.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 154 | 3 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.96× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -12.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 110 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.39× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -15.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 192 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.25× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 186 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.41× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 132 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.60× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -15.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 144 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.08× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 75.5 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.0× (z +12.1) | — |
| [[J82 (line)]] | alt | 184 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 136 | 2 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.02× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.556× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 167 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.65× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -12.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 130 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.93× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -16.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 114 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.33× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.488× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -14.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 135 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.05× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -13.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 163 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.90× (z +9.0) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.210× (z -10.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 111 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.20× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -14.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 122 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.89× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 187 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.22× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.551× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 199 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 2.94× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -11.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -15.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -16.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 184 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -11.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 120 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.56× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 135 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.54× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -13.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -9.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 77.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.37× (z +10.9) | — |
| [[LoVo (line)]] | wt | 147 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.22× (z +17.5) | — |
| [[LS 180 (line)]] | wt | 88.2 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 8.16× (z +12.8) | — |
| [[SW48 (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 153 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.64× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -18.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.172× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~39% of this change |
| [[CHP-212 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPTP]] | +0.65 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[GTF2E1]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 | pathway: RNA polymerase II transcribes snRNA genes |
| [[ZNF142]] | +0.60 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[BAG5]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[FLAD1]] | +0.59 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[OGFOD1]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[RIC8A]] | +0.57 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[LSG1]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[BFAR]] | +0.56 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[TOMM70]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[EIF2S1]] | +0.55 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA5]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[VAMP2]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PNISR]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[LINC01273]] | -0.52 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[FAM151B-DT]] | -0.51 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[P2RX4]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CACNG2]] | -0.48 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[FAM117A]] | -0.48 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[BORCS7]] | -0.47 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[KMT2E-AS1]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[BTG3]] | -0.47 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SNAP25-AS1]] | -0.47 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.463). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-47.9, 2.0); signed map (-8.1, -27.7). **Vector** length 110, 33.2% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +16.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.3 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +12.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -10.6 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -7.1 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -17.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.7 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.5 | -1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | interactor of little elongation complex ELL subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.32 — chr5:5,420,664-5,490,220 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0947 |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2F5](https://www.uniprot.org/uniprotkb/Q9Y2F5) (Little elongation complex subunit 1):

> Component of the little elongation complex (LEC), a complex required to regulate small nuclear RNA (snRNA) gene transcription by RNA polymerase II and III. Specifically acts as a scaffold protein that promotes the LEC complex formation and recruitment and RNA polymerase II occupancy at snRNA genes in subnuclear bodies.

**Summary**, from NCBI Gene [23379](https://www.ncbi.nlm.nih.gov/gene/23379):

> Enables protein-macromolecule adaptor activity. Involved in several processes, including positive regulation of intracellular protein transport; positive regulation of transcription by RNA polymerase III; and snRNA transcription. Located in Cajal body; euchromatin; and histone locus body. Part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29154) · Entrez [23379](https://www.ncbi.nlm.nih.gov/gene/23379) · UniProt [Q9Y2F5](https://www.uniprot.org/uniprotkb/Q9Y2F5) · Ensembl [ENSG00000164151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164151)

## Data

Gene col 8883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8883); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8883]; `tensor/DDL_lfc|DDL_z.npy` [8883]; `embed/gene_vectors.npy` [8883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8883 or target_col == 8883). Every well: [[ICE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ICE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

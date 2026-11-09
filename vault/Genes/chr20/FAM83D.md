---
symbol: "FAM83D"
type: "gene"
col: 2140
ensembl_id: "ENSG00000101447"
name: "scaffolding CK1 anchoring protein D"
location: "20q11.23"
module: 22
arm: "+"
pooled_cpm: 28.35
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# FAM83D

*scaffolding CK1 anchoring protein D* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.06× (z +22.6, q 0e+00, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.85× (z +21.2, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.493× (z -9.7, q 1e-19, down in 27 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.751× (z -5.8, q 6e-07, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF2C]] (+0.87, fdr 7e-06), [[CDCA8]] (+0.87, fdr 7e-06), [[PIF1]] (+0.86, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **3.06×** | +22.6 | 0e+00 | 40/48 (Panc 03.27, PANC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +21.2 | 0e+00 | 42/47 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.66×** | +14.0 | 4e-42 | 38/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.51×** | +13.2 | 2e-37 | 39/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +11.6 | 6e-29 | 38/47 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **2.02×** | +9.7 | 3e-20 | 37/48 (PANC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.34×** | +9.0 | 1e-17 | 38/48 (HEC-1-A, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.61×** | +7.2 | 5e-11 | 31/46 (J82, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +6.6 | 2e-09 | 28/47 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +5.6 | 1e-06 | 23/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.6 | 1e-06 | 21/47 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.30×** | +5.3 | 5e-06 | 20/48 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.27×** | +4.8 | 8e-05 | 19/48 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 17/48 (A498, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +4.1 | 0.002 | 17/44 (PANC-1, HOP62, …) | all doses, flat | low cells (technical?) |
| [[AZD1390 (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.037 | 13/48 (Panc 03.27, HT-29, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.039 | 8/47 (A498, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.063 | 9/48 (RKO, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.493×** | -9.7 | 1e-19 | 27/37 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.554×** | -8.5 | 7e-15 | 38/48 (A-427, LOX-IMVI, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.571×** | -8.0 | 2e-13 | 28/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.619×** | -6.9 | 9e-10 | 27/47 (SNU-1, PANC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.658×** | -6.0 | 2e-07 | 25/48 (C32, H4, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.751×** | -5.8 | 6e-07 | 25/48 (LS 180, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.763×** | -5.5 | 4e-06 | 21/48 (A-427, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.677×** | -5.4 | 5e-06 | 25/47 (SHP-77, PANC-1, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.679×** | -5.3 | 6e-06 | 23/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.692×** | -5.3 | 7e-06 | 25/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.707×** | -5.0 | 3e-05 | 21/48 (A549, LOX-IMVI, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.793×** | -4.7 | 1e-04 | 19/48 (HCT15, C-33 A, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.729×** | -4.5 | 3e-04 | 17/47 (SW1417, NCI-H1573, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.712×** | -4.5 | 3e-04 | 20/47 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.741×** | -4.0 | 0.003 | 13/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Saquinavir (drug)]] 5 µM |  | 0.835× | -3.7 | 0.008 | 17/48 (Panc 03.27, H4, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **0.785×** | -3.5 | 0.017 | 8/47 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.667×** | -3.0 | 0.068 | 10/47 (SHP-77, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.806×** | -3.0 | 0.076 | 14/48 (HS-578T, SW 900, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.867× | -2.9 | 0.096 | 10/48 (SNU-1, HOP62, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.818×** | -2.9 | 0.097 | 10/47 (NCI-H661, CHP-212, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.85 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 84.7 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.4) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -10.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 29.0 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +15.2) | — |
| [[HEC-1-A (line)]] | alt | 41.6 | 3 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -22.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 40.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0781× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 22.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.5) | [[Selinexor (drug)]] 5 µM 0.318× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 27.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +12.8) ⚠ cell-cycle shift, explains ~55% of this change | [[Selinexor (drug)]] 5 µM 0.283× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 27.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +13.1) | — |
| [[LS 180 (line)]] | wt | 13.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +8.6) ⚠ cell-cycle shift, explains ~55% of this change | [[Selinexor (drug)]] 5 µM 0.223× (z -10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.292× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 26.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +16.9) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 18.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +15.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 22.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +10.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 67.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.220× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 26.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 9.48 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +14.0) | — |
| [[C32 (line)]] | wt | 23.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.0) ⚠ cell-cycle shift, explains ~55% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.141× (z -10.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[CFPAC-1 (line)]] | alt | 14.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +11.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +9.9) | — |
| [[H4 (line)]] | wt | 28.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0354× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 28.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -11.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 42.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +11.5) | — |
| [[LoVo (line)]] | wt | 14.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.141× (z -9.3) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.153× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 10.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 38.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +15.2) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 28.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +12.7) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 5 µM 0.116× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 18.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +14.3) | — |
| [[RKO (line)]] | wt | 27.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +12.9) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 41.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +11.4) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 23.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +9.5) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 5 µM 0.122× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.5 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.188× (z -9.3) |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +12.6) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H23 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF2C]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | STRING 668 |
| [[CDCA8]] | +0.87 | +0.80 / +0.90 | both halves | 7e-06 | STRING 669 |
| [[PIF1]] | +0.86 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[KIF20A]] | +0.86 | +0.85 / +0.88 | both halves | 7e-06 | STRING 925 |
| [[CCNB2]] | +0.86 | +0.90 / +0.86 | both halves | 7e-06 | STRING 599 |
| [[AURKA]] | +0.86 | +0.86 / +0.86 | both halves | 7e-06 | STRING 818 |
| [[TROAP]] | +0.85 | +0.85 / +0.86 | both halves | 7e-06 | STRING 532 |
| [[CCNB1]] | +0.85 | +0.85 / +0.85 | both halves | 7e-06 | STRING 601 |
| [[GTSE1]] | +0.84 | +0.80 / +0.86 | both halves | 7e-06 | STRING 446 |
| [[UBE2C]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 | STRING 636 |
| [[PLK1]] | +0.84 | +0.87 / +0.82 | both halves | 7e-06 | STRING 599 |
| [[HJURP]] | +0.83 | +0.76 / +0.85 | both halves | 7e-06 | STRING 572 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises FAM83D's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.24× lower at baseline in the lines without PIMREG | 0.015 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[FAM72B]] | B | FAM72B activity raises FAM83D's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without FAM72B | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[AURKB]] | C | AURKB activity raises FAM83D's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without AURKB | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[ACBD7]] | C | ACBD7 activity raises FAM83D's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[SAPCD2]] | C | SAPCD2 activity raises FAM83D's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without SAPCD2 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.836). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.8, -57.5); signed map (-51.4, -42.3). **Vector** length 134, 43.8% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.68 to 60); *DREAM G2/M down* (control, mean cos +0.79 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.61 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +21.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +5.4 | +22.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.3 | +4.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.5 | +7.2 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +4.2 | +5.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +6.6 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.2 | +2.0 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -6.8 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -2.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.1 | -6.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.0 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.8 | -5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -3.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +0.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | scaffolding CK1 anchoring protein D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:38,926,312-38,953,106 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ616B8.3, CHICA; previously C20orf129, FAM83D |
| Gene groups (HGNC) | Scaffolding anchor of CK1 domain containing |
| Reactome | 2 pathways, smallest: Signaling by EGFR; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4H8](https://www.uniprot.org/uniprotkb/Q9H4H8) (Scaffolding CK1 anchoring protein D):

> Through the degradation of FBXW7, may act indirectly on the expression and downstream signaling of MTOR, JUN and MYC. May play also a role in cell proliferation through activation of the ERK1/ERK2 signaling cascade. May also be important for proper chromosome congression and alignment during mitosis through its interaction with KIF22.

**Summary**, from NCBI Gene [81610](https://www.ncbi.nlm.nih.gov/gene/81610):

> Enables kinesin binding activity; microtubule binding activity; and protein kinase binding activity. Involved in several processes, including positive regulation of cell cycle G1/S phase transition; protein localization to mitotic spindle; and regulation of intracellular signal transduction. Located in cytosol and mitotic spindle pole. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16122) · Entrez [81610](https://www.ncbi.nlm.nih.gov/gene/81610) · UniProt [Q9H4H8](https://www.uniprot.org/uniprotkb/Q9H4H8) · Ensembl [ENSG00000101447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101447)

## Data

Gene col 2140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2140); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2140]; `tensor/DDL_lfc|DDL_z.npy` [2140]; `embed/gene_vectors.npy` [2140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2140 or target_col == 2140). Every well: [[FAM83D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM83D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

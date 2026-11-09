---
symbol: "SUFU"
type: "gene"
col: 2894
ensembl_id: "ENSG00000107882"
name: "SUFU negative regulator of hedgehog signaling"
location: "10q24.32"
module: 30
arm: "+"
pooled_cpm: 42.65
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 10
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SUFU

*SUFU negative regulator of hedgehog signaling* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.99× (z +30.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.453× (z -22.0, q 0e+00, down in 38 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.597× (z -14.3, q 3e-44, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM13B]] (+0.76, fdr 1e-05), [[PHAF1]] (+0.76, fdr 7e-06), [[SLC27A1]] (+0.74, fdr 7e-06); moves opposite to [[DESI1]] (-0.70, fdr 1e-05), [[TSTD2]] (-0.69, fdr 1e-05), [[ARRDC3-AS1]] (-0.69, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDGFL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.99×** | +30.4 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.62×** | +26.8 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.37×** | +23.9 | 0e+00 | 46/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +12.7 | 1e-34 | 40/48 (SW1417, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +9.9 | 5e-21 | 36/48 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.95×** | +9.3 | 2e-18 | 36/48 (SW480, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.22×** | +7.8 | 7e-13 | 24/48 (LS 180, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +6.2 | 5e-08 | 26/48 (NCI-H2030, RKO, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +6.1 | 5e-08 | 20/48 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +5.0 | 3e-05 | 9/48 (NCI-H2030, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.19× | +4.8 | 8e-05 | 19/48 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.18× | +4.5 | 3e-04 | 11/49 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.17× | +4.4 | 5e-04 | 5/48 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +4.4 | 5e-04 | 11/48 (NCI-H2347, SW480, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +4.2 | 8e-04 | 9/48 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.6 | 0.011 | 8/48 (HEC-1-A, HCT15, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.011 | 7/48 (NCI-H2030, HEC-1-A, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | 1.14× | +3.4 | 0.021 | 6/49 (NCI-H2030, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.453×** | -22.0 | 0e+00 | 38/46 (SNU-423, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.513×** | -17.2 | 0e+00 | 33/44 (Panc 03.27, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.567×** | -15.1 | 0e+00 | 30/40 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -14.3 | 3e-44 | 36/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -11.2 | 4e-27 | 34/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.713×** | -9.1 | 1e-17 | 27/48 (A-172, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.726×** | -8.9 | 5e-17 | 27/48 (A-172, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.754×** | -7.8 | 3e-13 | 28/48 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.570×** | -7.8 | 5e-13 | 26/49 (HOP62, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.778×** | -7.0 | 2e-10 | 25/47 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -6.9 | 3e-10 | 22/48 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.771×** | -6.7 | 1e-09 | 25/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.791×** | -6.5 | 3e-09 | 25/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.791×** | -6.5 | 3e-09 | 26/48 (A498, Hs 766T, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -6.4 | 8e-09 | 23/48 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -6.2 | 2e-08 | 24/48 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.859× | -6.0 | 8e-08 | 13/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.754×** | -5.6 | 6e-07 | 21/48 (RPMI-7951, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.833×** | -5.1 | 1e-05 | 15/47 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.738×** | -4.2 | 6e-04 | 14/48 (SW 900, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.861× | -4.0 | 0.001 | 18/47 (A498, SNU-423, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.882× | -3.5 | 0.010 | 13/48 (PANC-1, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 45.8 | 3 | 12 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -19.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -12.5) |
| [[HOP62 (line)]] | alt | 53.7 | 3 | 8 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 3.07× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.224× (z -8.5) |
| [[SNU-423 (line)]] | alt | 68.7 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.6) |
| [[SW 900 (line)]] | alt | 59.7 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 43.8 | 4 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.86× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -24.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 51.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.244× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 43.0 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.01× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -12.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 34.2 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.60× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.290× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 46.2 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 39.5 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.440× (z -10.6) |
| [[SW1417 (line)]] | alt | 46.7 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.39× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -11.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 51.0 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +12.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.420× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 60.0 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +10.5) | [[Lonafarnib (drug)]] 5 µM 0.0763× (z -15.3) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -13.0) |
| [[LoVo (line)]] | wt | 36.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.85× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -24.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 38.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 40.1 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.14× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -11.5) |
| [[A-427 (line)]] | wt | 34.4 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -14.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 52.2 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -16.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 46.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.47× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -10.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 47.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.53× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 40.3 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.80× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0970× (z -17.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 32.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.19× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 42.2 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -12.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.380× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 37.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.69× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.296× (z -9.3) |
| [[A549 (line)]] | wt | 38.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +15.5) | — |
| [[HCT15 (line)]] | alt | 52.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0957× (z -16.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 35.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.74× (z +13.8) | — |
| [[J82 (line)]] | alt | 23.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 46.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 56.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -16.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 34.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +17.2) | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.73× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 63.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -14.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 34.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 41.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.358× (z -9.7) |
| [[AN3 CA (line)]] | alt | 95.6 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.182× (z -9.6) |
| [[COLO 205 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.343× (z -8.8) |
| [[RKO (line)]] | wt | 35.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 28.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +8.8) | — |
| [[SW48 (line)]] | wt | 54.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -9.0) |
| [[BT-474 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM13B]] | +0.76 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PHAF1]] | +0.76 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SLC27A1]] | +0.74 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CARHSP1]] | +0.70 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.69 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[KIAA2013]] | +0.69 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.68 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ALAD]] | +0.68 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[ORC4]] | +0.68 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[NFRKB]] | +0.67 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[UNC45A]] | +0.66 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PAK4]] | +0.66 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DESI1]] | -0.70 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[TSTD2]] | -0.69 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ARRDC3-AS1]] | -0.69 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.67 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PSME3IP1]] | -0.65 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MSRA]] | -0.64 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ALG13]] | -0.64 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[LTO1]] | -0.63 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[ZNF655]] | -0.63 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[CPSF2]] | -0.63 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[TUG1]] | -0.63 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[EMG1]] | -0.62 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDGFL3]] | B | HDGFL3 activity raises SUFU's level | lines that do not express HDGFL3 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without HDGFL3 | 0.046 | ⚠ within organs, on part of the lines; also absent: HLTF, GAMT, TIGD7 |
| [[EVL]] | B | EVL activity raises SUFU's level | lines that do not express EVL (16) vs lines expressing it (34) | 1.12× lower at baseline in the lines without EVL | 0.084 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, GNB4 |
| [[NAT14]] | C | NAT14 activity raises SUFU's level | lines that do not express NAT14 (3) vs lines expressing it (47) | 1.37× lower at baseline in the lines without NAT14 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ODAD4, GGT7, MATN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (4.4, -7.0); signed map (-33.2, -0.7). **Vector** length 97.3, 25.0% of its response variance represented; |z| ≥ 3 in 1,281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +26.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +30.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +23.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.5 | +7.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +12.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.0 | +2.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.5 | -17.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.3 | -14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.1 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -15.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.5 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | SUFU negative regulator of hedgehog signaling |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,503,972-102,633,535 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SUFUH, SUFUXL, PRO1280 |
| Reactome | 6 pathways, smallest: Degradation of GLI1 by the proteasome; Degradation of GLI2 by the proteasome; GLI3 is processed to GLI3R by the proteasome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMX1](https://www.uniprot.org/uniprotkb/Q9UMX1) (Suppressor of fused homolog):

> Negative regulator in the hedgehog/smoothened signaling pathway that acts by sequestering the GLI (GI1, GLI2 and GLI3) transcription factors in the cytoplasm. When smoothened signaling is initiated, GLI transcription factors dissociate from SUFU, translocate to the nucleus and activate expression of target genes. In absence of smoothened signaling, the SUFU-GLI3 complex is recruited to cilia, leading to the efficient processing of full-length GLI3 into transcription repressor GLI3R: SUFU …

**Summary**, from NCBI Gene [51684](https://www.ncbi.nlm.nih.gov/gene/51684):

> The Hedgehog signaling pathway plays an important role in early human development. The pathway is a signaling cascade that plays a role in pattern formation and cellular proliferation during development. This gene encodes a negative regulator of the hedgehog signaling pathway. Defects in this gene are a cause of medulloblastoma. Alternative splicing results in multiple transcript variants.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:16466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16466) · Entrez [51684](https://www.ncbi.nlm.nih.gov/gene/51684) · UniProt [Q9UMX1](https://www.uniprot.org/uniprotkb/Q9UMX1) · Ensembl [ENSG00000107882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107882)

## Data

Gene col 2894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2894); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2894]; `tensor/DDL_lfc|DDL_z.npy` [2894]; `embed/gene_vectors.npy` [2894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2894 or target_col == 2894). Every well: [[SUFU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUFU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

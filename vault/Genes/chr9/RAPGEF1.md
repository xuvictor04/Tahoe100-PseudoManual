---
symbol: "RAPGEF1"
type: "gene"
col: 2839
ensembl_id: "ENSG00000107263"
name: "Rap guanine nucleotide exchange factor 1"
location: "9q34.13"
module: 1
arm: "+"
pooled_cpm: 87.46
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RAPGEF1

*Rap guanine nucleotide exchange factor 1* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.44× (z +10.3, q 3e-22, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.605× (z -20.4, q 0e+00, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHST3]] (+0.58, fdr 8e-06), [[RIPOR1]] (+0.55, fdr 2e-05), [[KLF11]] (+0.54, fdr 3e-05); moves opposite to [[INTS6L]] (-0.53, fdr 2e-05), [[KHDC4]] (-0.48, fdr 4e-05), [[ZFC3H1]] (-0.47, fdr 5e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +10.3 | 3e-22 | 28/48 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +8.2 | 6e-14 | 29/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +8.1 | 1e-13 | 33/48 (NCI-H1573, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +7.7 | 2e-12 | 30/49 (NCI-H1573, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +7.3 | 3e-11 | 25/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +5.5 | 4e-06 | 20/48 (PANC-1, SNU-423, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +5.1 | 3e-05 | 8/48 (CFPAC-1, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.0 | 4e-05 | 20/48 (A549, H4, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +4.9 | 6e-05 | 21/47 (NCI-H460, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +4.9 | 7e-05 | 20/47 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.7 | 1e-04 | 20/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +4.6 | 2e-04 | 21/48 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.2 | 0.001 | 22/48 (HT-29, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.14× | +3.9 | 0.004 | 12/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.14× | +3.7 | 0.008 | 12/47 (C32, LoVo, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.6 | 0.012 | 7/48 (PANC-1, CHP-212, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.014 | 12/48 (C32, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.12× | +3.4 | 0.020 | 16/48 (A549, A498, …) | all doses, stronger at high dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.031 | 6/49 (SHP-77, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2839.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -20.4 | 0e+00 | 39/49 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -13.9 | 1e-41 | 34/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -12.7 | 1e-34 | 35/50 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.758×** | -11.2 | 9e-27 | 28/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.698×** | -10.5 | 8e-24 | 34/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.723×** | -9.5 | 2e-19 | 32/48 (A498, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.766×** | -7.8 | 5e-13 | 27/48 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -7.3 | 2e-11 | 24/48 (Panc 03.27, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.829×** | -5.5 | 2e-06 | 23/49 (A-172, COLO 205, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.833× | -5.3 | 5e-06 | 21/49 (SNU-423, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.850× | -4.7 | 1e-04 | 21/48 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | 0.852× | -4.5 | 3e-04 | 18/47 (HepG2/C3A, RKO, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.863× | -4.3 | 7e-04 | 18/48 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.883× | -3.6 | 0.011 | 9/48 (BT-474, C32, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | 0.885× | -3.6 | 0.013 | 15/48 (AsPC-1, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Pimitespib (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.032 | 9/48 (A498, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | 0.897× | -3.1 | 0.058 | 8/48 (SW1417, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 118 | 4 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.34× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -9.9) |
| [[PANC-1 (line)]] | alt | 94.5 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -16.9) |
| [[A-427 (line)]] | wt | 72.8 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.05× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.447× (z -14.8) |
| [[A498 (line)]] | wt | 172 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -14.9) |
| [[HepG2_C3A (line)]] | wt | 236 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 72.4 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -18.3) |
| [[A-172 (line)]] | wt | 71.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -11.5) |
| [[COLO 205 (line)]] | alt | 191 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.1) |
| [[KATO III (line)]] | alt | 101 | 2 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.18× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.431× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 82.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 86.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -13.5) |
| [[SW1417 (line)]] | alt | 105 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 85.5 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.19× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.529× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.646× (z -8.6) |
| [[HOP62 (line)]] | alt | 47.9 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 2.64× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 73.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -9.3) |
| [[RKO (line)]] | wt | 189 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -11.5) |
| [[SNU-423 (line)]] | alt | 87.1 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.50× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.0) |
| [[SW48 (line)]] | wt | 111 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.79× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.267× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 86.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -14.8) |
| [[BT-474 (line)]] | alt | 116 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 2.91× (z +10.5) | — |
| [[H4 (line)]] | wt | 34.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.95× (z +9.4) | — |
| [[J82 (line)]] | alt | 99.3 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 49.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 84.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.448× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 74.6 | 1 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.15× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 72.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -10.5) |
| [[SNU-1 (line)]] | wt | 98.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.440× (z -9.6) |
| [[SW480 (line)]] | alt | 73.4 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -11.7) |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -9.1) |
| [[C32 (line)]] | wt | 62.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -15.9) |
| [[HS-578T (line)]] | alt | 62.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -12.0) |
| [[LoVo (line)]] | wt | 102 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.16× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 78.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.40× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 98.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 91.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 67.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.5) |
| [[C-33 A (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHST3]] | +0.58 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[RIPOR1]] | +0.55 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[KLF11]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ANXA7]] | +0.51 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[QDPR]] | +0.51 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[FAM171A1]] | +0.50 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[RAD51D]] | +0.49 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[ZFHX3]] | +0.49 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[POGK]] | +0.49 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[DLG5]] | +0.49 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[SLCO3A1]] | +0.48 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[AIMP2]] | +0.48 | +0.41 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6L]] | -0.53 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[KHDC4]] | -0.48 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[ZFC3H1]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[SPAG4]] | -0.47 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[SPICE1]] | -0.47 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[PIK3C2A]] | -0.46 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[PPP1R32]] | -0.45 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[DPM1]] | -0.45 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[SAR1A]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[SH3D21]] | -0.44 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[MLEC]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[SMAP2]] | -0.44 | -0.27 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RAPGEF1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.346). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.6, -29.9); signed map (5.9, -8.0). **Vector** length 107, 28.0% of its response variance represented; |z| ≥ 3 in 1,275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.0 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.8 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +3.6 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -20.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -7.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.7 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | Rap guanine nucleotide exchange factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:131,576,770-131,740,076 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C3G; previously GRF2 |
| Reactome | 21 pathways, smallest: MET activates RAP1 and RAC1; Frs2-mediated activation; Erythropoietin activates RAS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13905](https://www.uniprot.org/uniprotkb/Q13905) (Rap guanine nucleotide exchange factor 1):

> Guanine nucleotide-releasing protein that binds to SH3 domain of CRK and GRB2/ASH. Transduces signals from CRK to activate RAS. Involved in cell branching and adhesion mediated by BCAR1-CRK-RAPGEF1 signaling and activation of RAP1. Plays a role in the establishment of basal endothelial barrier function. Plays a role in nerve growth factor (NGF)-induced sustained activation of Rap1 and neurite outgrowth.

**Summary**, from NCBI Gene [2889](https://www.ncbi.nlm.nih.gov/gene/2889):

> This gene encodes a human guanine nucleotide exchange factor. It transduces signals from CRK by binding the SH3 domain of CRK, and activating several members of the Ras family of GTPases. This signaling cascade that may be involved in apoptosis, integrin-mediated signal transduction, and cell transformation. Several alternatively spliced transcript variants of this gene have been described, but the full-length nature of some variants has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4568) · Entrez [2889](https://www.ncbi.nlm.nih.gov/gene/2889) · UniProt [Q13905](https://www.uniprot.org/uniprotkb/Q13905) · Ensembl [ENSG00000107263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107263)

## Data

Gene col 2839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2839); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2839]; `tensor/DDL_lfc|DDL_z.npy` [2839]; `embed/gene_vectors.npy` [2839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2839 or target_col == 2839). Every well: [[RAPGEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAPGEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

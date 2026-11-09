---
symbol: "PIGN"
type: "gene"
col: 12418
ensembl_id: "ENSG00000197563"
name: "phosphatidylinositol glycan anchor biosynthesis class N"
location: "18q21.33"
module: 16
arm: "-"
pooled_cpm: 72.61
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PIGN

*phosphatidylinositol glycan anchor biosynthesis class N* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +21.8, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.621× (z -13.9, q 7e-41, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.554× (z -12.9, q 1e-35, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD3]] (+0.71, fdr 1e-05), [[KATNB1]] (+0.69, fdr 9e-06), [[MFN1]] (+0.67, fdr 7e-06); moves opposite to [[GSPT2]] (-0.67, fdr 1e-05), [[ZNF606]] (-0.66, fdr 1e-05), [[MRFAP1L1]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +21.8 | 0e+00 | 47/49 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +17.6 | 0e+00 | 46/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +17.3 | 0e+00 | 46/48 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +15.7 | 0e+00 | 46/48 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.4 | 7e-28 | 40/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +10.0 | 1e-21 | 41/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +7.7 | 8e-13 | 35/48 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.04×** | +7.5 | 6e-12 | 39/49 (SHP-77, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.6 | 3e-09 | 28/50 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.2 | 9e-06 | 23/48 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.12× | +3.2 | 0.074 | 3/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.621×** | -13.9 | 7e-41 | 37/48 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.554×** | -12.9 | 1e-35 | 43/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.558×** | -12.3 | 2e-32 | 40/48 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.580×** | -11.9 | 1e-30 | 44/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.623×** | -9.9 | 3e-21 | 39/47 (SW1417, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -8.3 | 1e-14 | 36/48 (LoVo, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.685×** | -8.3 | 1e-14 | 30/47 (SNU-1, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.693×** | -8.0 | 9e-14 | 30/48 (SNU-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.465×** | -8.0 | 1e-13 | 39/49 (LoVo, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -6.9 | 3e-10 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.736×** | -6.7 | 1e-09 | 29/48 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.753×** | -5.7 | 5e-07 | 28/47 (C32, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.794×** | -5.0 | 2e-05 | 27/48 (SW48, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.802×** | -4.6 | 2e-04 | 22/47 (SNU-423, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.813×** | -4.5 | 2e-04 | 23/48 (SNU-1, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.833× | -4.0 | 0.002 | 18/47 (LS 180, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 78.7 | 4 | 4 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.84× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -14.0) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -12.0) |
| [[J82 (line)]] | alt | 65.6 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.56× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -16.3) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 73.7 | 1 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.1) | [[Harringtonine (drug)]] 0.5 µM 0.345× (z -14.9) |
| [[A498 (line)]] | wt | 66.3 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -22.8) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -15.6) |
| [[HOP62 (line)]] | alt | 34.5 | 5 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.05× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -12.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-172 (line)]] | wt | 46.9 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -17.0) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -12.6) |
| [[A549 (line)]] | wt | 91.3 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -15.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.278× (z -15.1) |
| [[HS-578T (line)]] | alt | 84.5 | 2 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -16.0) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 51.0 | 4 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.6) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 74.8 | 4 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.22× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 52.7 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.47× (z +12.9) | [[Harringtonine (drug)]] 5 µM 0.370× (z -9.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 51.6 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.505× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HT-29 (line)]] | alt | 51.1 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +14.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.417× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 86.6 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -13.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[RKO (line)]] | wt | 97.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SNU-423 (line)]] | alt | 47.3 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -15.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[CFPAC-1 (line)]] | alt | 44.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 102 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +14.0) | — |
| [[Hs 766T (line)]] | wt | 47.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 96.0 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +16.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.309× (z -12.8) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 97.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +12.6) | — |
| [[SNU-1 (line)]] | wt | 84.4 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 67.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.282× (z -8.7) |
| [[COLO 205 (line)]] | alt | 48.2 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -12.7) |
| [[KATO III (line)]] | alt | 103 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.24× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 119 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 44.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 74.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0932× (z -26.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 67.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[LoVo (line)]] | wt | 107 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +13.8) | [[Auranofin (drug)]] 5 µM 0.499× (z -8.6) |
| [[LS 180 (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.384× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[PANC-1 (line)]] | alt | 83.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +9.1) | [[Docetaxel (drug)]] 0.05 µM 0.446× (z -12.0) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change |
| [[RPMI-7951 (line)]] | alt | 57.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.4) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SW 900 (line)]] | alt | 26.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 84.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.203× (z -16.7) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 91.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 113 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 78.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 49.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | +0.71 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[KATNB1]] | +0.69 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[MFN1]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[TMED4]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RPA1]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[METTL9]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TDP1]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PIGF]] | +0.61 | +0.58 / +0.44 | both halves | 3e-05 | same gene group; pathway: Post-translational modification: synthesis of GPI-anchored proteins; STRING 506 |
| [[SHQ1]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[GINM1]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NAP1L4]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[RCN2]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSPT2]] | -0.67 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[ZNF606]] | -0.66 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | -0.64 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.63 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[ZNF134]] | -0.62 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[ZNF155]] | -0.62 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.62 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[ZNF620]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ZFHX2]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ZNF829]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ZNF554]] | -0.60 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIGN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers PIGN's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers PIGN's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.8, 11.5); signed map (-48.6, -5.4). **Vector** length 104, 30.7% of its response variance represented; |z| ≥ 3 in 1,257 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +21.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +11.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +7.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | +1.5 | -0.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.4 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -9.9 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.3 | -12.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.1 | -9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.3 | -12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -5.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class N |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:61,905,255-62,187,118 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCD4, PIG-N |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O95427](https://www.uniprot.org/uniprotkb/O95427) (GPI ethanolamine phosphate transferase 1):

> Ethanolamine phosphate transferase that catalyzes an ethanolamine phosphate (EtNP) transfer from phosphatidylethanolamine (PE) to the 2-OH position of the first alpha-1,4-linked mannose of a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) intermediate to generate a …

**Summary**, from NCBI Gene [23556](https://www.ncbi.nlm.nih.gov/gene/23556):

> This gene encodes a protein that is involved in glycosylphosphatidylinositol (GPI)-anchor biosynthesis. The GPI-anchor is a glycolipid found on many blood cells and serves to anchor proteins to the cell surface. This protein is expressed in the endoplasmic reticulum and transfers phosphoethanolamine (EtNP) to the first mannose of the GPI anchor. Two alternatively spliced variants, which encode an identical isoform, have been reported. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8967) · Entrez [23556](https://www.ncbi.nlm.nih.gov/gene/23556) · UniProt [O95427](https://www.uniprot.org/uniprotkb/O95427) · Ensembl [ENSG00000197563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197563)

## Data

Gene col 12418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12418); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12418]; `tensor/DDL_lfc|DDL_z.npy` [12418]; `embed/gene_vectors.npy` [12418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12418 or target_col == 12418). Every well: [[PIGN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

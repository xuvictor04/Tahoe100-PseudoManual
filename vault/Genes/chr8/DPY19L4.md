---
symbol: "DPY19L4"
type: "gene"
col: 7953
ensembl_id: "ENSG00000156162"
name: "dpy-19 like 4"
location: "8q22.1"
module: 25
arm: "+"
pooled_cpm: 54.5
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DPY19L4

*dpy-19 like 4* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.58× (z +15.6, q 0e+00, up in 39 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW480 3.59×, A549 4.57×, C32 5.13×, LoVo 3.35×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 3.09×, HEC-1-A 3.10×, A-172 3.48×, HOP62 2.80×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 2.72×, KATO III 3.10×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.539× (z -14.9, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.575× (z -13.3, q 1e-37, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHFR]] (+0.69, fdr 5e-04), [[UHMK1]] (+0.68, fdr 1e-05), [[HDHD2]] (+0.68, fdr 1e-04); moves opposite to [[IMP3]] (-0.68, fdr 3e-05), [[EMC6]] (-0.65, fdr 1e-04), [[ING2]] (-0.65, fdr 2e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7953.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW480 3.59×, A549 4.57×, C32 5.13×, LoVo 3.35×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 3.09×, HEC-1-A 3.10×, A-172 3.48×, HOP62 2.80×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 2.72×, KATO III 3.10×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +15.6 | 0e+00 | 39/40 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +13.9 | 2e-41 | 46/49 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +8.5 | 2e-15 | 35/45 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.30×** | +6.3 | 3e-08 | 28/48 (AsPC-1, J82, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.1 | 0.22 | 15/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.539×** | -14.9 | 0e+00 | 42/48 (AsPC-1, A-427, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -13.3 | 1e-37 | 47/48 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.548×** | -10.3 | 2e-22 | 42/48 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.584×** | -9.2 | 5e-18 | 40/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.619×** | -8.2 | 3e-14 | 41/48 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.624×** | -8.1 | 6e-14 | 40/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.634×** | -7.8 | 5e-13 | 43/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.643×** | -7.6 | 3e-12 | 39/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -6.9 | 3e-10 | 38/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.682×** | -6.5 | 3e-09 | 32/48 (A498, NCI-H460, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.686×** | -6.4 | 6e-09 | 39/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.680×** | -6.4 | 1e-08 | 31/48 (AsPC-1, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.698×** | -6.2 | 3e-08 | 32/48 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.514×** | -6.0 | 1e-07 | 35/49 (RKO, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.723×** | -5.6 | 1e-06 | 34/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.725×** | -5.5 | 1e-06 | 32/48 (AN3 CA, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -4.8 | 6e-05 | 28/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -4.5 | 2e-04 | 28/48 (HCT15, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -4.4 | 3e-04 | 24/48 (SW480, HS-578T, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.615×** | -4.4 | 4e-04 | 23/48 (COLO 205, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -3.0 | 0.057 | 16/48 (HOP62, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.8 | 2 (2 ⚠) | 5 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.25× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -16.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 60.7 | 2 (2 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +11.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 55.5 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.14× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -19.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 51.0 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.63× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.0) |
| [[SW480 (line)]] | alt | 59.0 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.59× (z +14.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.437× (z -10.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.6) |
| [[A498 (line)]] | wt | 74.6 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.09× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -16.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HEC-1-A (line)]] | alt | 70.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -9.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HOP62 (line)]] | alt | 79.5 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +10.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -14.8) |
| [[A549 (line)]] | wt | 43.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.57× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 53.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.3) |
| [[HS-578T (line)]] | alt | 68.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.95× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -8.7) |
| [[HT-29 (line)]] | alt | 43.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -10.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -8.9) |
| [[J82 (line)]] | alt | 54.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -11.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.6) |
| [[KATO III (line)]] | alt | 59.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.10× (z +10.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.2) |
| [[LoVo (line)]] | wt | 42.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.35× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -9.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW1417 (line)]] | alt | 40.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.06× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +11.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 47.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -17.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 51.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 59.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 53.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -8.5) |
| [[LS 180 (line)]] | wt | 46.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[MIA PaCa-2 (line)]] | alt | 54.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.82× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H1792 (line)]] | alt | 42.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 49.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.44× (z +10.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.309× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 55.8 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -12.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 67.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 46.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.73× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 900 (line)]] | alt | 49.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.4) |
| [[C-33 A (line)]] | alt | 48.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.272× (z -8.8) |
| [[C32 (line)]] | wt | 44.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +12.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 73.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.0) |
| [[Hs 766T (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2347 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 97.7 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.149× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 70.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 46.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -11.4) |
| [[AN3 CA (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR]] | +0.69 | +0.24 / +0.75 | both halves | 5e-04 |  |
| [[UHMK1]] | +0.68 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[HDHD2]] | +0.68 | +0.33 / +0.74 | both halves | 1e-04 |  |
| [[LIN7C]] | +0.68 | +0.23 / +0.75 | both halves | 5e-04 |  |
| [[MANEA]] | +0.67 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[PCNP]] | +0.65 | +0.33 / +0.70 | both halves | 1e-04 |  |
| [[MBTPS2]] | +0.63 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[ARL5A]] | +0.63 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[OCRL]] | +0.63 | +0.23 / +0.73 | both halves | 5e-04 |  |
| [[FAM136A]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[NELFCD]] | +0.62 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[ARPP19]] | +0.62 | +0.27 / +0.69 | both halves | 3e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 8 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMP3]] | -0.68 | -0.43 / -0.71 | both halves | 3e-05 |  |
| [[EMC6]] | -0.65 | -0.32 / -0.68 | both halves | 1e-04 |  |
| [[ING2]] | -0.65 | -0.30 / -0.72 | both halves | 2e-04 |  |
| [[MRPL36]] | -0.65 | -0.35 / -0.70 | both halves | 1e-04 |  |
| [[RPL36AL]] ⚠ | -0.65 | -0.32 / -0.67 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NUDT22]] | -0.63 | -0.21 / -0.70 | both halves | 6e-04 |  |
| [[EXOSC4]] | -0.62 | -0.39 / -0.65 | both halves | 6e-05 |  |
| [[SEC61G]] | -0.61 | -0.25 / -0.70 | both halves | 4e-04 |  |
| [[ZBTB7A]] | -0.61 | -0.29 / -0.71 | both halves | 2e-04 |  |
| [[C16orf91]] | -0.60 | -0.27 / -0.62 | both halves | 3e-04 |  |
| [[RALGDS]] | -0.60 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[MILIP]] | -0.58 | -0.36 / -0.64 | both halves | 9e-05 |  |
| [[COX6B1]] | -0.58 | -0.29 / -0.62 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.5, -19.7); signed map (-17.2, -38.6). **Vector** length 103, 29.6% of its response variance represented; |z| ≥ 3 in 1,206 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.4 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.8 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +8.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +6.8 | +6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.6 | +1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.6 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.8 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | -2.7 | -1.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.6 | -1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.4 | -2.0 |
|  | [[Carbamazepine (drug)]] 5 µM |  | -2.4 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | dpy-19 like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,719,703-94,793,836 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z388](https://www.uniprot.org/uniprotkb/Q7Z388) (Probable C-mannosyltransferase DPY19L4):

> Probable C-mannosyltransferase that mediates C-mannosylation of tryptophan residues on target proteins.

**Summary**, from NCBI Gene [286148](https://www.ncbi.nlm.nih.gov/gene/286148):

> Predicted to enable mannosyltransferase activity. Predicted to be located in membrane. Predicted to be active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27829) · Entrez [286148](https://www.ncbi.nlm.nih.gov/gene/286148) · UniProt [Q7Z388](https://www.uniprot.org/uniprotkb/Q7Z388) · Ensembl [ENSG00000156162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156162)

## Data

Gene col 7953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7953); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7953]; `tensor/DDL_lfc|DDL_z.npy` [7953]; `embed/gene_vectors.npy` [7953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7953 or target_col == 7953). Every well: [[DPY19L4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

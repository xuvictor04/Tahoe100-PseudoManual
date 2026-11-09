---
symbol: "HLTF"
type: "gene"
col: 992
ensembl_id: "ENSG00000071794"
name: "helicase like transcription factor"
location: "3q24"
module: 57
arm: "+"
pooled_cpm: 87.34
n_lines_expressing: 42
n_dd_up: 14
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 14
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# HLTF

*helicase like transcription factor* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.37× (z +15.5, q 0e+00, up in 38 of 40 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.62× (z +12.2, q 3e-32, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.476× (z -18.8, q 0e+00, down in 37 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH7A1]] (+0.72, fdr 7e-06), [[LRRCC1]] (+0.72, fdr 7e-06), [[SSX2IP]] (+0.71, fdr 7e-06); moves opposite to [[GCNT4]] (-0.65, fdr 3e-05), [[LINC01004]] (-0.63, fdr 3e-05), [[ANKHD1-EIF4EBP3]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SORT1]] → it (grade B ⚠); 14 go from it, the strongest it → [[TMBIM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 992.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.37×** | +15.5 | 0e+00 | 38/40 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.17×** | +13.9 | 1e-41 | 39/40 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.09×** | +13.2 | 9e-38 | 40/40 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +12.2 | 3e-32 | 38/40 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.75×** | +10.1 | 9e-22 | 35/41 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +9.3 | 1e-18 | 38/40 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.69×** | +9.1 | 1e-17 | 29/38 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.18×** | +7.3 | 2e-11 | 35/41 (SHP-77, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.40×** | +5.5 | 2e-06 | 23/38 (SHP-77, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.65×** | +4.7 | 1e-04 | 25/39 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.4 | 6e-04 | 21/40 (NCI-H23, A549, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.1 | 0.002 | 15/40 (C32, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.002 | 22/40 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.16× | +3.8 | 0.006 | 10/40 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.22×** | +3.6 | 0.014 | 17/40 (SHP-77, NCI-H2030, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.033 | 13/40 (J82, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 992.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.476×** | -18.8 | 0e+00 | 37/40 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.445×** | -14.5 | 6e-45 | 35/40 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.493×** | -12.7 | 2e-34 | 37/40 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -11.7 | 2e-29 | 37/40 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.526×** | -11.5 | 2e-28 | 34/40 (HCT15, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.642×** | -7.6 | 3e-12 | 23/40 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -7.1 | 1e-10 | 30/40 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -5.6 | 2e-06 | 25/40 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -5.6 | 2e-06 | 27/40 (H4, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -5.5 | 2e-06 | 29/40 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -5.0 | 4e-05 | 21/40 (A-427, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.768×** | -4.7 | 1e-04 | 22/40 (MIA PaCa-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.670×** | -4.5 | 3e-04 | 21/40 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.775×** | -4.4 | 5e-04 | 21/39 (A498, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -4.2 | 1e-03 | 19/41 (Panc 03.27, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.8 | 0.005 | 19/40 (BT-474, A498, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.709×** | -3.7 | 0.006 | 22/40 (A-427, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.812×** | -3.7 | 0.006 | 19/40 (A498, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.3 | 4 (4 ⚠) | 8 | [[Panobinostat (drug)]] 5 µM 3.18× (z +11.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Harringtonine (drug)]] 0.5 µM 0.217× (z -15.5) |
| [[A498 (line)]] | wt | 116 | 4 (3 ⚠) | 6 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.80× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -22.3) |
| [[NCI-H23 (line)]] | alt | 124 | 4 (3 ⚠) | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.20× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.67× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 103 | 4 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.09× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -16.0) |
| [[SW 900 (line)]] | alt | 93.4 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -15.8) |
| [[A-172 (line)]] | wt | 105 | 3 (3 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | [[Digitoxin (drug)]] 0.5 µM 0.374× (z -10.8) |
| [[PANC-1 (line)]] | alt | 191 | 1 (1 ⚠) | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.91× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -14.0) |
| [[A549 (line)]] | wt | 65.5 | 4 (4 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 3.41× (z +11.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Harringtonine (drug)]] 0.5 µM 0.351× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 67.4 | 4 (4 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 3.36× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 81.3 | 4 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.95× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -15.6) |
| [[J82 (line)]] | alt | 192 | 3 (2 ⚠) | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.77× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 35.8 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.64× (z +12.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 227 | 2 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.07× (z +10.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.616× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 72.7 | 3 (2 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 1.91× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -9.7) |
| [[HOP62 (line)]] | alt | 79.5 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.82× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -16.2) |
| [[HS-578T (line)]] | alt | 119 | 2 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.17× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.4) |
| [[SHP-77 (line)]] | alt | 178 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.37× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -8.7) |
| [[BT-474 (line)]] | alt | 57.6 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.93× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.321× (z -9.0) |
| [[H4 (line)]] | wt | 99.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 259 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.51× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -20.1) |
| [[Hs 766T (line)]] | wt | 80.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 51.9 | 1 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 65.0 | 1 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -12.7) |
| [[C32 (line)]] | wt | 66.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -13.4) |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -12.0) |
| [[SW1417 (line)]] | alt | 41.4 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +9.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.12× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.242× (z -9.1) |
| [[HCT15 (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 136 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.65× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 96.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.7) |
| [[SNU-1 (line)]] | wt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.222× (z -12.9) |
| [[SNU-423 (line)]] | alt | 74.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 | — | [[Rifaximin (drug)]] 0.5 µM 0.0490× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 106 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.00 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH7A1]] | +0.72 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[LRRCC1]] | +0.72 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SSX2IP]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[PAPSS1]] | +0.69 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[MPP1]] | +0.68 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SKP2]] | +0.68 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PHF6]] | +0.68 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CDCA7L]] | +0.66 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[ALAD]] | +0.66 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.65 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[PARP1]] | +0.65 | +0.39 / +0.60 | both halves | 5e-05 | STRING 530 |
| [[POT1]] | +0.65 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCNT4]] | -0.65 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[LINC01004]] | -0.63 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ANKHD1-EIF4EBP3]] | -0.63 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ANKRD17-DT]] | -0.61 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[ZNF778]] | -0.60 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[CDR2]] | -0.60 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[ATE1OSP]] | -0.59 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[NRSN2-AS1]] | -0.59 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ATXN7L3-AS1]] | -0.59 | -0.26 / -0.52 | both halves | 3e-04 |  |
| [[ATXN1L]] | -0.59 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[SMIM12]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[LRRC41]] | -0.58 | -0.37 / -0.50 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORT1]] | B | SORT1 activity lowers HLTF's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.02× higher at baseline in the lines without SORT1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[DYNC2H1]] | C | DYNC2H1 activity raises HLTF's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 5.23× lower at baseline in the lines without DYNC2H1 | 0.071 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798; co-absent with the target |
| [[MPP1]] | C | MPP1 activity raises HLTF's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 5.60× lower at baseline in the lines without MPP1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2; co-absent with the target |
| [[DMXL2]] | C | DMXL2 activity raises HLTF's level | lines that do not express DMXL2 (3) vs lines expressing it (47) | 4.79× lower at baseline in the lines without DMXL2 | 0.090 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: PPP2R3A, CCDC102A, ENSG00000250264 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMBIM1]] | B | HLTF activity lowers TMBIM1's level | lines that do not express HLTF (8) vs lines expressing it (42) | 2.15× higher at baseline in the lines without HLTF | 0.010 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[LINC00888]] | B | HLTF activity raises LINC00888's level | lines that do not express HLTF (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without HLTF | 0.021 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[SEPTIN6]] | B | HLTF activity raises SEPTIN6's level | lines that do not express HLTF (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without HLTF | 0.024 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[ATG4C]] | B | HLTF activity raises ATG4C's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without HLTF | 0.027 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[FBXW9]] | B | HLTF activity raises FBXW9's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without HLTF | 0.045 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[FIGNL1]] | B | HLTF activity raises FIGNL1's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without HLTF | 0.049 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[DPYSL3]] | B | HLTF activity raises DPYSL3's level | lines that do not express HLTF (8) vs lines expressing it (42) | 6.67× lower at baseline in the lines without HLTF | 0.058 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[SKP2]] | B | HLTF activity raises SKP2's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without HLTF | 0.067 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[PDHB]] | B | HLTF activity raises PDHB's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without HLTF | 0.081 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[ANXA6]] | B | HLTF activity raises ANXA6's level | lines that do not express HLTF (8) vs lines expressing it (42) | 3.38× lower at baseline in the lines without HLTF | 0.082 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[CBX1]] | B | HLTF activity raises CBX1's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without HLTF | 0.086 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[RPGRIP1L]] | B | HLTF activity raises RPGRIP1L's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without HLTF | 0.090 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.4, -6.8); signed map (-33.8, -35.3). **Vector** length 135, 45.7% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.7 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.5 | +13.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.8 | +7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.6 | +13.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.1 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -14.9 | -18.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.1 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.8 | -11.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.7 | -3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | helicase like transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:149,030,127-149,086,554 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HIP116A, HLTF1, RNF80; previously SNF2L3, SMARCA3 |
| Gene groups (HGNC) | Ring finger proteins; SNF2 related family; RING finger E3 ubiquitin protein ligases |
| Reactome | 2 pathways, smallest: E3 ubiquitin ligases ubiquitinate target proteins; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14527](https://www.uniprot.org/uniprotkb/Q14527) (DNA-dependent ATPase/E3 ubiquitin-protein ligase HLTF):

> Functions as a DNA-dependent ATPase and E3 ubiquitin-protein ligase involved in chromatin regulation and DNA damage tolerance (DDT). Catalyzes 'Lys-63'-linked polyubiquitination of monoubiquitinated PCNA at 'Lys-164' in response to genotoxic stress, promoting error-free postreplication repair via template switching. Acts as an epigenetic regulator by promoting recruitment of DNMT1, thereby ensuring DNA methylation inheritance: specifically binds histone H3 trimethylated at 'Lys-9' (H3K9me3) and …

**Summary**, from NCBI Gene [6596](https://www.ncbi.nlm.nih.gov/gene/6596):

> This gene encodes a member of the SWI/SNF family. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein contains a RING finger DNA binding motif. Two transcript variants encoding the same protein have been found for this gene. However, use of an alternative translation start site produces an isoform that is truncated at the N-terminus compared to the …

**Accessions** — [HGNC:11099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11099) · Entrez [6596](https://www.ncbi.nlm.nih.gov/gene/6596) · UniProt [Q14527](https://www.uniprot.org/uniprotkb/Q14527) · Ensembl [ENSG00000071794](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071794)

## Data

Gene col 992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 992); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 992]; `tensor/DDL_lfc|DDL_z.npy` [992]; `embed/gene_vectors.npy` [992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 992 or target_col == 992). Every well: [[HLTF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLTF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

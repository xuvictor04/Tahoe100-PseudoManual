---
symbol: "RBBP4"
type: "gene"
col: 8528
ensembl_id: "ENSG00000162521"
name: "RB binding protein 4, chromatin remodeling factor"
location: "1p35.1"
module: 71
arm: "+"
pooled_cpm: 96.66
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# RBBP4

*RB binding protein 4, chromatin remodeling factor* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.90× (z +32.3, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +12.5, q 1e-33, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.797× (z -9.7, q 1e-19, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRE11]] (+0.72, fdr 7e-06), [[ZNF718]] (+0.66, fdr 1e-05), [[FUCA2]] (+0.66, fdr 1e-05); moves opposite to [[H3-3B]] (-0.66, fdr 1e-05), [[POLD4]] (-0.64, fdr 7e-06), [[ATF4]] (-0.62, fdr 9e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DLX6-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 22 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +32.3 | 0e+00 | 49/49 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +31.0 | 0e+00 | 43/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +25.1 | 0e+00 | 45/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +12.5 | 1e-33 | 36/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.41×** | +10.5 | 7e-24 | 28/48 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.41×** | +10.1 | 6e-22 | 36/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.41×** | +10.1 | 7e-22 | 34/47 (A-172, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.37×** | +9.7 | 3e-20 | 33/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +9.6 | 4e-20 | 37/50 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +7.6 | 1e-12 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +7.4 | 8e-12 | 29/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.27×** | +7.0 | 1e-10 | 27/47 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +6.9 | 2e-10 | 25/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +6.4 | 7e-09 | 23/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.17× | +4.7 | 9e-05 | 14/48 (PANC-1, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +4.6 | 2e-04 | 16/48 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +4.5 | 2e-04 | 12/48 (HOP62, J82, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +4.0 | 0.002 | 14/48 (HT-29, NCI-H1573, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.14× | +3.8 | 0.004 | 6/48 (SNU-423, HS-578T, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.08× | +3.4 | 0.015 | 2/49 (RPMI-7951, SW 1271) | all doses, flat |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.020 | 8/48 (HS-578T, RKO, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.024 | 6/48 (HEC-1-A, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.046 | 5/48 (SW 900, AsPC-1, …) | inconsistent across doses |  |
| [[LJI308 (drug)]] 0.05 µM |  | 1.11× | +2.9 | 0.082 | 3/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.10× | +2.8 | 0.082 | 5/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | 1.09× | +2.7 | 0.094 | 0/49 | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.797×** | -9.7 | 1e-19 | 27/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.731×** | -9.5 | 4e-19 | 30/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.742×** | -8.7 | 6e-16 | 29/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -5.9 | 7e-07 | 17/48 (SW480, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.851× | -4.9 | 1e-04 | 17/48 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -4.9 | 1e-04 | 19/48 (LS 180, J82, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -4.3 | 0.001 | 15/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.868× | -4.3 | 0.001 | 17/47 (NCI-H460, A549, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.871× | -4.2 | 0.002 | 19/49 (LS 180, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.869× | -4.1 | 0.002 | 15/47 (J82, RKO, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.894× | -3.4 | 0.032 | 14/48 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.927× | -3.3 | 0.054 | 5/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Clotrimazole (drug)]] 5 µM |  | 0.929× | -3.2 | 0.068 | 1/49 (CHP-212) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.930× | -3.1 | 0.079 | 2/48 (HS-578T, Hs 766T) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 117 | 7 (7 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +21.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.528× (z -10.1) |
| [[SW480 (line)]] | alt | 146 | 5 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +20.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -19.5) |
| [[KATO III (line)]] | alt | 106 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +15.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 128 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +20.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -12.0) |
| [[A-172 (line)]] | wt | 63.9 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 70.1 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +16.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -9.8) |
| [[HOP62 (line)]] | alt | 90.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +16.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 92.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 70.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 144 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 64.3 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +13.3) | — |
| [[C-33 A (line)]] | alt | 212 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.499× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 127 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.571× (z -8.9) |
| [[HT-29 (line)]] | alt | 108 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +15.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -11.0) |
| [[J82 (line)]] | alt | 140 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 115 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +15.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.9) |
| [[SW 900 (line)]] | alt | 63.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 87.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.2) | — |
| [[A498 (line)]] | wt | 71.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +15.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 58.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +17.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 44.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +12.2) | — |
| [[C32 (line)]] | wt | 71.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +16.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 92.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +15.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 90.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +17.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 51.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +17.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 73.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.73× (z +25.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 68.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 81.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +15.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +13.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 105 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -15.1) |
| [[H4 (line)]] | wt | 70.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 90.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 66.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.03× (z +17.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 83.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +12.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 63.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 58.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 170 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +14.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 152 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRE11]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[ZNF718]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FUCA2]] | +0.66 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[MCM5]] | +0.64 | +0.71 / +0.52 | both halves | 1e-05 | pathway: G1/S Transition; STRING 442 |
| [[TYMS]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 | pathway: G1/S Transition |
| [[RAD51AP1]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[PPT1]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TIMELESS]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[LAMTOR5-AS1]] | +0.63 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SUMO3]] | +0.63 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[XNDC1N]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CRTAP]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3B]] | -0.66 | -0.59 / -0.57 | both halves | 1e-05 | STRING 981 |
| [[POLD4]] | -0.64 | -0.60 / -0.61 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[ATF4]] | -0.62 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[YIF1A]] | -0.62 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[TUBB2A]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 | pathway: G2/M Transition |
| [[SURF2]] | -0.61 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SNAPIN]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[R3HCC1]] | -0.61 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SERTAD1]] | -0.60 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[MED19]] | -0.60 | -0.56 / -0.53 | both halves | 1e-05 | pathway: Adipogenesis |
| [[TNIP2]] | -0.59 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[METTL23]] | -0.59 | -0.47 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX6-AS1]] | B | DLX6-AS1 activity raises RBBP4's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.31× lower at baseline in the lines without DLX6-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RBBP4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.7, -26.6); signed map (-37.0, -49.6). **Vector** length 113, 33.2% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.4 | +10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.1 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +25.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.3 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +12.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +7.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | -1.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.8 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | RB binding protein 4, chromatin remodeling factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,651,142-32,686,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RbAp48, NURF55, lin-53 |
| Gene groups (HGNC) | WD repeat domain containing; EMSY complex; NuRD complex subunits; SIN3 histone deacetylase complex subunits; Polycomb repressive complex 2; NURF complex |
| Reactome | 75 pathways, smallest: Polo-like kinase mediated events; Transcription of E2F targets under negative control by p107 (RBL1) and p130 (RBL2) in complex with HDAC1; Transcription of E2F targets under negative control by DREAM complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q09028](https://www.uniprot.org/uniprotkb/Q09028) (Histone-binding protein RBBP4):

> Core histone-binding subunit that may target chromatin assembly factors, chromatin remodeling factors and histone deacetylases to their histone substrates in a manner that is regulated by nucleosomal DNA. Component of the chromatin assembly factor 1 (CAF-1) complex, which is required for chromatin assembly following DNA replication and DNA repair. Component of the core histone deacetylase (HDAC) complex, which promotes histone deacetylation and consequent transcriptional repression. Component …

**Summary**, from NCBI Gene [5928](https://www.ncbi.nlm.nih.gov/gene/5928):

> This gene encodes a ubiquitously expressed nuclear protein which belongs to a highly conserved subfamily of WD-repeat proteins. It is present in protein complexes involved in histone acetylation and chromatin assembly. It is part of the Mi-2 complex which has been implicated in chromatin remodeling and transcriptional repression associated with histone deacetylation. This encoded protein is also part of co-repressor complexes, which is an integral component of transcriptional silencing. It is …

**Accessions** — [HGNC:9887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9887) · Entrez [5928](https://www.ncbi.nlm.nih.gov/gene/5928) · UniProt [Q09028](https://www.uniprot.org/uniprotkb/Q09028) · Ensembl [ENSG00000162521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162521)

## Data

Gene col 8528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8528); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8528]; `tensor/DDL_lfc|DDL_z.npy` [8528]; `embed/gene_vectors.npy` [8528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8528 or target_col == 8528). Every well: [[RBBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

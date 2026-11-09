---
symbol: "PDCD6"
type: "gene"
col: 14651
ensembl_id: "ENSG00000249915"
name: "programmed cell death 6"
location: "5p15.33"
module: 52
arm: "+"
pooled_cpm: 83.56
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# PDCD6

*programmed cell death 6* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +15.8, q 0e+00, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.660× (z -15.7, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SENP5]] (+0.75, fdr 7e-06), [[PIGG]] (+0.71, fdr 7e-06), [[PMPCA]] (+0.70, fdr 7e-06); moves opposite to [[KPNA5]] (-0.64, fdr 7e-06), [[CFL2]] (-0.62, fdr 1e-05), [[ZNF711]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +15.8 | 0e+00 | 38/49 (LOX-IMVI, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.53×** | +11.4 | 7e-28 | 40/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.43×** | +9.5 | 3e-19 | 38/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +9.3 | 2e-18 | 35/50 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.40×** | +8.7 | 5e-16 | 37/48 (HS-578T, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.32×** | +7.4 | 2e-11 | 30/48 (SW480, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.37×** | +4.4 | 0.001 | 17/49 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +4.1 | 0.003 | 13/48 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | 1.16× | +3.8 | 0.008 | 20/47 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.14× | +3.5 | 0.022 | 15/48 (SW480, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14651.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.660×** | -15.7 | 0e+00 | 36/48 (A-427, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.627×** | -12.0 | 8e-31 | 38/48 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -8.3 | 2e-14 | 29/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.736×** | -8.2 | 3e-14 | 28/48 (HOP62, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -6.7 | 2e-09 | 27/47 (H4, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.809×** | -5.7 | 1e-06 | 27/49 (BT-474, SW 1271, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.815×** | -5.5 | 4e-06 | 24/48 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.831×** | -5.0 | 5e-05 | 22/48 (A-427, RKO, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.880× | -4.9 | 8e-05 | 14/48 (AsPC-1, A-427, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.839× | -4.5 | 3e-04 | 16/50 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -4.5 | 4e-04 | 5/50 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.846× | -4.3 | 8e-04 | 17/41 (SW480, J82, …) | rises with dose | composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.862× | -3.8 | 0.006 | 13/49 (A-427, NCI-H2122, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.872× | -3.7 | 0.010 | 21/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.872× | -3.6 | 0.010 | 7/48 (LOX-IMVI, LoVo, …) | rises with dose | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.873× | -3.6 | 0.010 | 13/48 (HEC-1-A, PANC-1, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.895× | -3.5 | 0.015 | 11/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.884× | -3.3 | 0.030 | 12/49 (A-427, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.897× | -3.2 | 0.037 | 13/49 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 0.880× | -3.2 | 0.039 | 12/49 (NCI-H1573, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.925× | -3.0 | 0.080 | 7/48 (SW480, PANC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.907× | -2.9 | 0.084 | 11/48 (AsPC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 86.4 | 5 (2 ⚠) | 3 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.51× (z +13.2) | [[Harringtonine (drug)]] 5 µM 0.258× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 95.3 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.337× (z -14.8) |
| [[SW480 (line)]] | alt | 99.0 | 4 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +13.3) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 5 µM 0.323× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 152 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -20.3) |
| [[HOP62 (line)]] | alt | 112 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.325× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -11.0) |
| [[RKO (line)]] | wt | 54.3 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.151× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~63% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.317× (z -10.1) |
| [[A-172 (line)]] | wt | 59.3 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.0) |
| [[A549 (line)]] | wt | 61.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -11.6) |
| [[J82 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 77.1 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.8) | [[Harringtonine (drug)]] 5 µM 0.470× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 67.6 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -18.0) |
| [[BT-474 (line)]] | alt | 108 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -14.4) |
| [[H4 (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -16.8) |
| [[HS-578T (line)]] | alt | 60.5 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 55.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 62.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 53.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -10.1) |
| [[SHP-77 (line)]] | alt | 94.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | [[Digitoxin (drug)]] 5 µM 0.354× (z -11.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 92.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -13.7) |
| [[C-33 A (line)]] | alt | 56.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -9.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 70.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 87.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -12.8) |
| [[CHP-212 (line)]] | wt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 76.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 54.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 134 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 73.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -8.9) |
| [[LoVo (line)]] | wt | 92.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.444× (z -11.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 76.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.5) | — |
| [[NCI-H596 (line)]] | alt | 78.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.313× (z -11.2) |
| [[PANC-1 (line)]] | alt | 86.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.559× (z -8.7) |
| [[SW 1088 (line)]] | alt | 84.7 | 0 | 1 | — | [[Verteporfin (drug)]] 0.5 µM 0.0890× (z -8.8) |
| [[SW 1271 (line)]] | alt | 68.1 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0831× (z -9.4) |
| [[SW 900 (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -12.2) |
| [[SW1417 (line)]] | alt | 92.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.0) |
| [[AN3 CA (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP5]] | +0.75 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[PIGG]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[PMPCA]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[FBH1]] | +0.66 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[IPPK]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[PMM2]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TMEM104]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[DPP9]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[FUBP3]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RER1]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SPG7]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA5]] | -0.64 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[CFL2]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[ZNF711]] | -0.61 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[WDSUB1]] | -0.61 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[GKAP1]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[ITSN2]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 | same gene group |
| [[RNFT1]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[MIER1]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[BTN2A2]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[FMR1]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[TAB2]] | -0.58 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[SETD2]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PDCD6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RHOU]] | B | RHOU activity raises PDCD6's level | lines that do not express RHOU (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without RHOU | 0.071 | ⚠ within organs, on part of the lines; also absent: JAKMIP3, HAP1 |
| [[HDAC6]] | B | HDAC6 activity lowers PDCD6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-14.3, 0.5); signed map (-48.2, 1.1). **Vector** length 115, 29.4% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +15.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.5 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.0 | -12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.4 | -15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.2 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.6 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -8.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:271,621-314,974 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALG-2, PEF1B |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75340](https://www.uniprot.org/uniprotkb/O75340) (Programmed cell death protein 6):

> Calcium sensor that plays a key role in processes such as endoplasmic reticulum (ER)-Golgi vesicular transport, endosomal biogenesis or membrane repair. Acts as an adapter that bridges unrelated proteins or stabilizes weak protein-protein complexes in response to calcium: calcium-binding triggers exposure of apolar surface, promoting interaction with different sets of proteins thanks to 3 different hydrophobic pockets, leading to translocation to membranes. Involved in ER-Golgi transport by …

**Summary**, from NCBI Gene [10016](https://www.ncbi.nlm.nih.gov/gene/10016):

> This gene encodes a calcium-binding protein belonging to the penta-EF-hand protein family. Calcium binding is important for homodimerization and for conformational changes required for binding to other protein partners. This gene product participates in T cell receptor-, Fas-, and glucocorticoid-induced programmed cell death. In mice deficient for this gene product, however, apoptosis was not blocked suggesting this gene product is functionally redundant. Alternatively spliced transcript …

**Accessions** — [HGNC:8765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8765) · Entrez [10016](https://www.ncbi.nlm.nih.gov/gene/10016) · UniProt [O75340](https://www.uniprot.org/uniprotkb/O75340) · Ensembl [ENSG00000249915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249915)

## Data

Gene col 14651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14651); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14651]; `tensor/DDL_lfc|DDL_z.npy` [14651]; `embed/gene_vectors.npy` [14651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14651 or target_col == 14651). Every well: [[PDCD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

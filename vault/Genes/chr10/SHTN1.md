---
symbol: "SHTN1"
type: "gene"
col: 11895
ensembl_id: "ENSG00000187164"
name: "shootin 1"
location: "10q25.3"
module: 48
arm: "-"
pooled_cpm: 134.98
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# SHTN1

*shootin 1* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.68× (z +13.7, q 6e-40, up in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.36× (z +8.1, q 8e-14, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.640× (z -16.8, q 0e+00, down in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (PANC-1 0.531×, HT-29 0.437×, A498 0.491×, NCI-H2030 0.471×, …); [[Panobinostat (drug)]] 0.5 µM in 2 lines (RKO 0.293×, A549 0.469×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (RKO 0.308×, A549 0.469×; ⚠ cell-cycle shift, explains ~30% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (RKO 0.216×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DST]] (+0.69, fdr 7e-06), [[YWHAH]] (+0.60, fdr 7e-06), [[BBOX1-AS1]] (+0.57, fdr 2e-05); moves opposite to [[TSEN34]] (-0.62, fdr 1e-05), [[SUPT4H1]] (-0.59, fdr 2e-05), [[MED26]] (-0.56, fdr 4e-05).
> It sits in the **-** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +13.7 | 6e-40 | 38/49 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +12.5 | 2e-33 | 37/44 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +8.1 | 8e-14 | 31/48 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +8.0 | 2e-13 | 27/48 (SW1417, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +7.5 | 8e-12 | 30/47 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +6.9 | 6e-10 | 29/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +6.8 | 1e-09 | 30/49 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +6.7 | 2e-09 | 25/47 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +6.1 | 7e-08 | 28/45 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +5.9 | 2e-07 | 22/47 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +5.9 | 2e-07 | 26/50 (A-172, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.23×** | +5.5 | 2e-06 | 25/47 (COLO 205, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +5.4 | 3e-06 | 24/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +5.1 | 1e-05 | 20/48 (LS 180, AsPC-1, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +5.1 | 1e-05 | 17/49 (HT-29, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +4.7 | 1e-04 | 17/47 (COLO 205, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.19× | +4.4 | 3e-04 | 19/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +4.4 | 4e-04 | 15/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +4.3 | 4e-04 | 18/48 (LS 180, LoVo, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +4.2 | 6e-04 | 19/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +4.2 | 6e-04 | 18/49 (NCI-H1573, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +4.2 | 7e-04 | 12/48 (LS 180, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11895.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (PANC-1 0.531×, HT-29 0.437×, A498 0.491×, NCI-H2030 0.471×, …); [[Panobinostat (drug)]] 0.5 µM in 2 lines (RKO 0.293×, A549 0.469×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (RKO 0.308×, A549 0.469×; ⚠ cell-cycle shift, explains ~30% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (RKO 0.216×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -16.8 | 0e+00 | 38/49 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.649×** | -11.5 | 5e-28 | 29/48 (RKO, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.732×** | -8.3 | 2e-14 | 30/48 (RKO, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.757×** | -7.4 | 2e-11 | 27/48 (RKO, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.820×** | -5.1 | 5e-05 | 26/47 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.831×** | -4.9 | 7e-05 | 23/48 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -4.9 | 8e-05 | 15/48 (A498, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.856× | -4.2 | 0.002 | 18/48 (RKO, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.757×** | -3.7 | 0.012 | 19/45 (H4, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | 0.881× | -3.4 | 0.039 | 17/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -3.3 | 0.047 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.884× | -3.3 | 0.048 | 16/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.787×** | -3.2 | 0.057 | 16/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.852× | -3.0 | 0.097 | 16/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 263 | 1 (1 ⚠) | 10 (9 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.62× (z +10.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -18.8) |
| [[RKO (line)]] | wt | 134 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.293× (z -17.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.216× (z -11.0) |
| [[HT-29 (line)]] | alt | 162 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -17.9) |
| [[LS 180 (line)]] | wt | 82.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 80.9 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 64.0 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.89× (z +9.7) | — |
| [[A-172 (line)]] | wt | 124 | 2 | 3 (2 ⚠) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 1.88× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -9.9) |
| [[A498 (line)]] | wt | 178 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -17.7) |
| [[A549 (line)]] | wt | 199 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.85× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.469× (z -12.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -11.1) |
| [[COLO 205 (line)]] | alt | 79.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 256 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +12.4) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 269 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -15.9) |
| [[A-427 (line)]] | wt | 192 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.79× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.491× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 45.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 139 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 163 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.524× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 51.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 175 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.2) |
| [[SW480 (line)]] | alt | 176 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 211 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.70× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 79.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.04× (z +9.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.419× (z -11.5) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 138 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.86× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 175 | 2 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.51× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -11.7) |
| [[C-33 A (line)]] | alt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +8.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 51.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 117 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.57× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 158 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -12.0) |
| [[SW1417 (line)]] | alt | 67.9 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -10.1) |
| [[HCT15 (line)]] | alt | 147 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 197 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.1) |
| [[HOP62 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -12.4) |
| [[J82 (line)]] | alt | 92.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.500× (z -9.2) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H1792 (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 75.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -15.9) |
| [[SW 1088 (line)]] | alt | 74.1 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0829× (z -8.6) |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 78.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DST]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[YWHAH]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[BBOX1-AS1]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[MYEF2]] | +0.56 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[PTPN21]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[KRT80]] | +0.55 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[CLIP1]] | +0.54 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[RNF180]] | +0.53 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[HOMER2]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[ANAPC7]] | +0.53 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[PAWR]] | +0.53 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[KLHL5]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSEN34]] | -0.62 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[SUPT4H1]] | -0.59 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[MED26]] | -0.56 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ZNHIT1]] | -0.56 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[NUDT22]] | -0.54 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[NDUFA2]] | -0.54 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[CNOT8]] | -0.54 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[MPG]] | -0.54 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[SDF2]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[QPCTL]] | -0.53 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[MGAT1]] | -0.52 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[TSC22D4]] | -0.52 | -0.43 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers SHTN1's level | compounds that target MAP2K1: 3 of 4 raise it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LONRF2]] | B | LONRF2 activity raises SHTN1's level | lines that do not express LONRF2 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without LONRF2 | 0.084 | ⚠ within organs, on part of the lines; also absent: ANKRD6, PPM1E, ADCY1 |
| [[HDAC6]] | B | HDAC6 activity raises SHTN1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **-** arm (projection on the module's main direction -0.386). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (4.4, -15.9); signed map (12.0, -10.4). **Vector** length 137, 41.2% of its response variance represented; |z| ≥ 3 in 1,408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +13.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +5.0 | +2.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +4.9 | +3.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.9 | +5.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -16.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.0 | -11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.4 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.4 | -7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | -4.2 | -5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.5 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.6 | -0.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | shootin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:116,881,477-117,126,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | shootin1, shootin-1; previously KIAA1598 |
| Reactome | 4 pathways, smallest: Recycling pathway of L1; L1CAM interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [A0MZ66](https://www.uniprot.org/uniprotkb/A0MZ66) (Shootin-1):

> Involved in the generation of internal asymmetric signals required for neuronal polarization and neurite outgrowth. Mediates netrin-1-induced F-actin-substrate coupling or 'clutch engagement' within the axon growth cone through activation of CDC42, RAC1 and PAK1-dependent signaling pathway, thereby converting the F-actin retrograde flow into traction forces, concomitantly with filopodium extension and axon outgrowth. Plays a role in cytoskeletal organization by regulating the subcellular …

**Summary**, from NCBI Gene [57698](https://www.ncbi.nlm.nih.gov/gene/57698):

> Enables identical protein binding activity. Involved in positive regulation of neuron migration. Located in cytoplasm and microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29319) · Entrez [57698](https://www.ncbi.nlm.nih.gov/gene/57698) · UniProt [A0MZ66](https://www.uniprot.org/uniprotkb/A0MZ66) · Ensembl [ENSG00000187164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187164)

## Data

Gene col 11895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11895); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11895]; `tensor/DDL_lfc|DDL_z.npy` [11895]; `embed/gene_vectors.npy` [11895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11895 or target_col == 11895). Every well: [[SHTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

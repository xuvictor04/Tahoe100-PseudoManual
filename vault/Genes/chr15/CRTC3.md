---
symbol: "CRTC3"
type: "gene"
col: 6435
ensembl_id: "ENSG00000140577"
name: "CREB regulated transcription coactivator 3"
location: "15q26.1"
module: 18
arm: "+"
pooled_cpm: 71.34
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CRTC3

*CREB regulated transcription coactivator 3* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.36× (z +6.3, q 1e-07, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.405× (z -18.7, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.503× (z -7.4, q 9e-12, down in 35 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SK-MEL-2 0.0727×, A-172 0.113×, A549 0.167×, C32 0.132×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.107×, SHP-77 0.112×, NCI-H460 0.131×, LoVo 0.186×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HT-29 0.0852×, HOP62 0.108×, RKO 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[TAK-901 (drug)]] 5 µM in 3 lines (NCI-H23 0.0396×, LOX-IMVI 0.201×, NCI-H2347 0.191×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.404×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.406×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPN9]] (+0.71, fdr 7e-06), [[NRF1]] (+0.61, fdr 1e-05), [[DNMT3A]] (+0.61, fdr 1e-05); moves opposite to [[RGL1]] (-0.48, fdr 5e-05), [[SF3B1]] (-0.47, fdr 3e-05), [[MYH9]] (-0.46, fdr 8e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[OR4F15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +6.3 | 1e-07 | 32/48 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +6.2 | 1e-07 | 30/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +6.2 | 1e-07 | 30/48 (BT-474, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.9 | 2e-04 | 25/47 (H4, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.006 | 20/48 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.21×** | +3.7 | 0.017 | 16/47 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.41×** | +3.7 | 0.017 | 17/43 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.019 | 17/47 (RPMI-7951, SW1417, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.021 | 20/47 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.040 | 19/47 (BT-474, SW480, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.19× | +3.3 | 0.052 | 15/48 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.065 | 4/48 (SW1417, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6435.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SK-MEL-2 0.0727×, A-172 0.113×, A549 0.167×, C32 0.132×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.107×, SHP-77 0.112×, NCI-H460 0.131×, LoVo 0.186×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HT-29 0.0852×, HOP62 0.108×, RKO 0.132×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[TAK-901 (drug)]] 5 µM in 3 lines (NCI-H23 0.0396×, LOX-IMVI 0.201×, NCI-H2347 0.191×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.404×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.406×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.405×** | -18.7 | 0e+00 | 46/49 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.445×** | -16.1 | 0e+00 | 36/43 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.476×** | -15.4 | 0e+00 | 41/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.491×** | -14.7 | 0e+00 | 42/48 (RKO, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.469×** | -14.5 | 1e-45 | 38/45 (HT-29, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.617×** | -10.0 | 1e-21 | 36/48 (NCI-H460, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.503×** | -7.4 | 9e-12 | 35/49 (NCI-H23, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.812×** | -6.0 | 1e-07 | 24/48 (NCI-H1792, A-172, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.750×** | -6.0 | 1e-07 | 27/48 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **0.764×** | -5.6 | 1e-06 | 28/48 (J82, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.788×** | -4.8 | 1e-04 | 26/50 (NCI-H2347, SW48, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.796×** | -4.8 | 1e-04 | 25/48 (NCI-H460, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -4.6 | 2e-04 | 23/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.819×** | -4.2 | 0.001 | 23/48 (A549, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.890× | -3.4 | 0.030 | 13/48 (A-172, SW1417, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.865× | -3.0 | 0.085 | 10/48 (HS-578T, AsPC-1, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.858× | -3.0 | 0.085 | 13/48 (J82, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 196 | 0 | 14 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.404× (z -9.1) |
| [[A-172 (line)]] | wt | 96.5 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HOP62 (line)]] | alt | 123 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 93.4 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 114 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 59.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 65.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LoVo (line)]] | wt | 97.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 73.5 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -25.9) ⚠ cell-cycle shift, explains ~91% of this change |
| [[NCI-H2030 (line)]] | alt | 90.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 58.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.191× (z -8.7) |
| [[C32 (line)]] | wt | 89.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 49.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-423 (line)]] | alt | 46.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 72.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 71.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 55.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0852× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 68.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.3) ⚠ cell-cycle shift, explains ~91% of this change |
| [[LOX-IMVI (line)]] | wt | 59.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.201× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 52.7 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 81.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.9) ⚠ cell-cycle shift, explains ~91% of this change |
| [[SHP-77 (line)]] | alt | 78.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 76.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 38.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.1) ⚠ cell-cycle shift, explains ~91% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -8.8) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HepG2_C3A (line)]] | wt | 45.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0874× (z -17.3) ⚠ toxic; cell-cycle shift, explains ~79% of this change |
| [[PANC-1 (line)]] | alt | 52.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 67.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0727× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 99.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -15.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0787× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[KATO III (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 45.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0396× (z -14.7) |
| [[SW480 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN9]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[NRF1]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 | pathway: Mitochondrial biogenesis |
| [[DNMT3A]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ARHGEF11]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PHLPP2]] | +0.59 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RILPL1]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ZNRF2P2]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[FGD1]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PKD2]] | +0.56 | +0.46 / +0.48 | both halves | 2e-05 | pathway: Organelle biogenesis and maintenance |
| [[MTFMT]] | +0.55 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[VAX2]] | +0.55 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[SVIL-AS1-1]] | +0.54 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGL1]] | -0.48 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[SF3B1]] | -0.47 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MYH9]] | -0.46 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[OR4F15]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[DNAH7]] | -0.44 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OR4F15]] | B | OR4F15 activity raises CRTC3's level | lines that do not express OR4F15 (32) vs lines expressing it (18) | 1.26× lower at baseline in the lines without OR4F15 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, PHACTR1, ITGA4 |
| [[ADCY3]] | B | ADCY3 activity raises CRTC3's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without ADCY3 | 0.095 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.374). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.5, 13.1); signed map (7.9, -4.8). **Vector** length 99.8, 28.4% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.5 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.5 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.1 | +6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.2 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | +4.1 | +3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | -0.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.0 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -0.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.4 | -15.4 |
|  | [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -0.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -0.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | CREB regulated transcription coactivator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,529,923-90,645,345 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21868 |
| Reactome | 8 pathways, smallest: Expression of BMAL (ARNTL), CLOCK, and NPAS2; Heme signaling; Transcriptional activation of mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UUV7](https://www.uniprot.org/uniprotkb/Q6UUV7) (CREB-regulated transcription coactivator 3):

> Transcriptional coactivator for CREB1 which activates transcription through both consensus and variant cAMP response element (CRE) sites. Acts as a coactivator, in the SIK/TORC signaling pathway, being active when dephosphorylated and acts independently of CREB1 'Ser-133' phosphorylation. Enhances the interaction of CREB1 with TAF4. Regulates the expression of specific CREB-activated genes such as the steroidogenic gene, StAR. Potent coactivator of PPARGC1A and inducer of mitochondrial …

**Summary**, from NCBI Gene [64784](https://www.ncbi.nlm.nih.gov/gene/64784):

> This gene is a member of the CREB regulated transcription coactivator gene family. This family regulates CREB-dependent gene transcription in a phosphorylation-independent manner and may be selective for cAMP-responsive genes. The protein encoded by this gene may induce mitochondrial biogenesis and attenuate catecholamine signaling in adipose tissue. A translocation event between this gene and Notch coactivator mastermind-like gene 2, which results in a fusion protein, has been reported in …

**Accessions** — [HGNC:26148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26148) · Entrez [64784](https://www.ncbi.nlm.nih.gov/gene/64784) · UniProt [Q6UUV7](https://www.uniprot.org/uniprotkb/Q6UUV7) · Ensembl [ENSG00000140577](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140577)

## Data

Gene col 6435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6435); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6435]; `tensor/DDL_lfc|DDL_z.npy` [6435]; `embed/gene_vectors.npy` [6435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6435 or target_col == 6435). Every well: [[CRTC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRTC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

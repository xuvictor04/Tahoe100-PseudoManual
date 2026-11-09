---
symbol: "TDRD3"
type: "gene"
col: 1374
ensembl_id: "ENSG00000083544"
name: "tudor domain containing 3"
location: "13q21.2"
module: 137
arm: "+"
pooled_cpm: 78.67
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 33
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# TDRD3

*tudor domain containing 3* — 13q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.17× (z +5.0, q 3e-04, up in 24 of 49 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.21× (z +4.3, q 0.004, up in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (LoVo 1.67×, Hs 766T 2.03×, SW480 1.61×, MIA PaCa-2 1.72×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (SK-MEL-2 4.61×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SK-MEL-2 4.37×; ⚠ toxic; cell-cycle shift, explains ~37% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (SK-MEL-2 4.03×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.14×).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.243× (z -32.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD2B]] (+0.64, fdr 3e-05), [[ARID1B]] (+0.63, fdr 1e-05), [[ANGEL2]] (+0.62, fdr 3e-05); moves opposite to [[BAIAP3]] (-0.64, fdr 2e-05), [[GDPD5]] (-0.62, fdr 1e-05), [[F11R]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[VWA5A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC12A2-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1374.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (LoVo 1.67×, Hs 766T 2.03×, SW480 1.61×, MIA PaCa-2 1.72×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (SK-MEL-2 4.61×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SK-MEL-2 4.37×; ⚠ toxic; cell-cycle shift, explains ~37% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (SK-MEL-2 4.03×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SK-MEL-2 3.14×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.0 | 3e-04 | 24/49 (LoVo, Hs 766T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.004 | 22/47 (C32, HCT15, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.9 | 0.018 | 20/48 (A498, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.030 | 13/48 (C32, BT-474, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.053 | 16/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.062 | 13/47 (C32, SW48, …) | rises with dose |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.15× | +3.2 | 0.11 | 12/48 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.14 | 3/48 (A549, SW 1088, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.16 | 13/48 (CFPAC-1, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.243×** | -32.7 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.250×** | -32.1 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.291×** | -28.6 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.488×** | -23.5 | 0e+00 | 46/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.470×** | -17.5 | 0e+00 | 43/48 (SW480, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.503×** | -15.9 | 0e+00 | 40/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.528×** | -14.8 | 0e+00 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.538×** | -13.8 | 1e-41 | 33/44 (NCI-H23, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.551×** | -13.8 | 2e-41 | 40/49 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.585×** | -12.4 | 1e-33 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.588×** | -11.4 | 3e-28 | 34/45 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.614×** | -11.3 | 7e-28 | 39/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -10.5 | 5e-24 | 37/49 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.642×** | -10.3 | 4e-23 | 43/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.639×** | -10.0 | 9e-22 | 35/48 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.743×** | -9.7 | 8e-21 | 38/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.684×** | -8.8 | 5e-17 | 38/48 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.486×** | -8.8 | 6e-17 | 40/48 (HCT15, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -7.8 | 1e-13 | 36/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.767×** | -5.8 | 2e-07 | 27/48 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.793×** | -5.4 | 2e-06 | 26/49 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 92.6 | 0 | 21 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0741× (z -39.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.228× (z -31.8) |
| [[SW480 (line)]] | alt | 118 | 1 (1 ⚠) | 14 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -32.8) |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -21.8) |
| [[PANC-1 (line)]] | alt | 90.5 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -23.0) |
| [[SW48 (line)]] | wt | 126 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.1) |
| [[LS 180 (line)]] | wt | 103 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -20.1) |
| [[NCI-H1573 (line)]] | alt | 65.2 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -30.8) |
| [[J82 (line)]] | alt | 104 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -29.2) |
| [[MIA PaCa-2 (line)]] | alt | 85.6 | 1 (1 ⚠) | 9 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -25.5) |
| [[C32 (line)]] | wt | 112 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -23.4) |
| [[HEC-1-A (line)]] | alt | 71.3 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -16.0) |
| [[SW 900 (line)]] | alt | 48.9 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.2) |
| [[COLO 205 (line)]] | alt | 157 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -28.2) |
| [[LoVo (line)]] | wt | 97.9 | 1 (1 ⚠) | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.246× (z -23.0) |
| [[NCI-H23 (line)]] | alt | 86.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -21.9) |
| [[SNU-1 (line)]] | wt | 184 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -20.2) |
| [[A-427 (line)]] | wt | 71.7 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -19.8) |
| [[A498 (line)]] | wt | 74.3 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -15.1) |
| [[HOP62 (line)]] | alt | 53.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -20.7) |
| [[HS-578T (line)]] | alt | 47.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -15.6) |
| [[RKO (line)]] | wt | 105 | 0 | 7 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.200× (z -17.6) |
| [[SHP-77 (line)]] | alt | 63.5 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -16.8) |
| [[H4 (line)]] | wt | 66.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -11.5) |
| [[HT-29 (line)]] | alt | 79.5 | 1 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.212× (z -18.0) |
| [[KATO III (line)]] | alt | 98.7 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -25.4) |
| [[NCI-H2030 (line)]] | alt | 60.0 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 82.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -19.2) |
| [[SK-MEL-2 (line)]] | alt | 131 | 5 (2 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.61× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 59.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -17.9) |
| [[A549 (line)]] | wt | 69.0 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -19.2) |
| [[BT-474 (line)]] | alt | 51.6 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -13.5) |
| [[Hs 766T (line)]] | wt | 91.2 | 1 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -16.7) |
| [[hTERT-HPNE (line)]] | wt | 66.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 36.9 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.240× (z -13.6) |
| [[SNU-423 (line)]] | alt | 60.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -15.6) |
| [[AN3 CA (line)]] | alt | 166 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0964× (z -17.8) |
| [[HCT15 (line)]] | alt | 99.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 52.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -17.9) |
| [[A-172 (line)]] | wt | 49.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -18.0) |
| [[C-33 A (line)]] | alt | 82.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -18.1) |
| [[HepG2_C3A (line)]] | wt | 44.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -10.1) |
| [[CHP-212 (line)]] | wt | 108 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0960× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.239× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 23.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -9.7) |
| [[SW 1271 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD2B]] | +0.64 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[ARID1B]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.62 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[UBTF]] | +0.59 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[KLHL42]] | +0.58 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[NCOA2]] | +0.58 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[DHX35]] | +0.58 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[GTF2I]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[QRSL1]] | +0.58 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[RAF1]] | +0.58 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[FBXL17]] | +0.58 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[NAF1]] | +0.58 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAIAP3]] | -0.64 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[GDPD5]] | -0.62 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[F11R]] | -0.56 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LMTK3]] | -0.56 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SPAG9]] | -0.55 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[FCHSD1]] | -0.55 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[ATP6V0A1]] | -0.55 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[GIPR]] | -0.54 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RGS9]] | -0.54 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[GNAI2]] | -0.54 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[FCHO1]] | -0.54 | -0.32 / -0.37 | both halves | 1e-04 |  |
| [[MFSD12]] | -0.53 | -0.34 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VWA5A]] | B | VWA5A activity raises TDRD3's level | lines that do not express VWA5A (13) vs lines expressing it (37) | 1.27× lower at baseline in the lines without VWA5A | 0.061 | ⚠ within organs, on part of the lines |
| [[GDPD5]] | C | GDPD5's natural level weakens TDRD3's drug response | GDPD5's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.27; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC12A2-DT]] | C | TDRD3's natural level strengthens SLC12A2-DT's drug response | TDRD3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.01; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.3, 13.9); signed map (27.3, -23.9). **Vector** length 99.4, 30.6% of its response variance represented; |z| ≥ 3 in 1,542 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +12.0 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.2 | +0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | -0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.8 | -5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.2 | -12.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -28.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -32.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -17.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | tudor domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q21.2 — chr13:60,396,457-60,573,878 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21007 |
| Gene groups (HGNC) | Tudor domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7E2](https://www.uniprot.org/uniprotkb/Q9H7E2) (Tudor domain-containing protein 3):

> Scaffolding protein that specifically recognizes and binds dimethylarginine-containing proteins. Plays a role in the regulation of translation of target mRNAs by binding Arg/Gly-rich motifs (GAR) in dimethylarginine-containing proteins. In nucleus, acts as a coactivator: recognizes and binds asymmetric dimethylation on the core histone tails associated with transcriptional activation (H3R17me2a and H4R3me2a) and recruits proteins at these arginine-methylated loci. In cytoplasm, acts as an …

**Summary**, from NCBI Gene [81550](https://www.ncbi.nlm.nih.gov/gene/81550):

> Enables chromatin binding activity; histone reader activity; and transcription coactivator activity. Predicted to be involved in siRNA-mediated heterochromatin formation. Located in cytosol; exon-exon junction complex; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20612) · Entrez [81550](https://www.ncbi.nlm.nih.gov/gene/81550) · UniProt [Q9H7E2](https://www.uniprot.org/uniprotkb/Q9H7E2) · Ensembl [ENSG00000083544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083544)

## Data

Gene col 1374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1374); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1374]; `tensor/DDL_lfc|DDL_z.npy` [1374]; `embed/gene_vectors.npy` [1374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1374 or target_col == 1374). Every well: [[TDRD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TDRD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

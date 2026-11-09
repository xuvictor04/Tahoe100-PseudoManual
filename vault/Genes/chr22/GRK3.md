---
symbol: "GRK3"
type: "gene"
col: 1860
ensembl_id: "ENSG00000100077"
name: "G protein-coupled receptor kinase 3"
location: "22q12.1"
module: 37
arm: "+"
pooled_cpm: 51.05
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 25
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# GRK3

*G protein-coupled receptor kinase 3* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.36× (z +16.7, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.618× (z -13.2, q 6e-37, down in 30 of 45 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.430× (z -8.6, q 9e-16, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYCP2L]] (+0.66, fdr 7e-06), [[PPP1R32]] (+0.64, fdr 7e-06), [[C9orf153]] (+0.62, fdr 8e-06); moves opposite to [[ZNF512B]] (-0.60, fdr 1e-05), [[ZNF414]] (-0.56, fdr 1e-05), [[EPC2]] (-0.55, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02885]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CRYBB2P1-1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +16.7 | 0e+00 | 38/45 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +12.9 | 1e-35 | 33/45 (SW1417, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +10.5 | 1e-23 | 34/45 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.9 | 6e-07 | 25/47 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.3 | 2e-05 | 23/45 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.5 | 6e-04 | 21/44 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.2 | 0.003 | 20/45 (NCI-H2347, NCI-H23, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.010 | 18/46 (C-33 A, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.15× | +3.7 | 0.011 | 7/45 (LS 180, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.056 | 13/46 (NCI-H2347, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.095 | 11/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1860.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.618×** | -13.2 | 6e-37 | 30/45 (COLO 205, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.517×** | -12.8 | 8e-35 | 30/45 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.541×** | -11.4 | 5e-28 | 29/39 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.587×** | -10.3 | 9e-23 | 31/45 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -9.8 | 1e-20 | 25/40 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -9.4 | 4e-19 | 31/43 (COLO 205, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.611×** | -9.2 | 4e-18 | 27/45 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.430×** | -8.6 | 9e-16 | 33/46 (NCI-H1573, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -8.5 | 2e-15 | 30/45 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -6.7 | 1e-09 | 26/45 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **0.739×** | -5.8 | 3e-07 | 21/45 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.764×** | -4.9 | 4e-05 | 19/44 (Panc 03.27, SW48, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.725×** | -4.3 | 9e-04 | 15/45 (SW 1271, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **0.805×** | -4.2 | 0.001 | 21/45 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.8 | 0.005 | 12/45 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.822×** | -3.8 | 0.005 | 15/45 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.008 | 13/45 (SW48, C32, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.832×** | -3.6 | 0.011 | 12/45 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.832×** | -3.5 | 0.011 | 12/45 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.835× | -3.5 | 0.013 | 16/45 (HepG2/C3A, HOP62, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.837× | -3.4 | 0.015 | 14/45 (H4, C-33 A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.837× | -3.3 | 0.023 | 17/45 (NCI-H1573, HS-578T, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.726×** | -3.2 | 0.028 | 13/45 (SNU-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.729×** | -3.2 | 0.031 | 16/45 (HS-578T, A549, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 277 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -26.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.262× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 128 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -20.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.194× (z -10.3) |
| [[HS-578T (line)]] | alt | 64.3 | 1 | 7 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.31× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.149× (z -15.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.243× (z -11.5) |
| [[C32 (line)]] | wt | 57.8 | 1 | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 5.89× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -20.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.229× (z -11.4) |
| [[A498 (line)]] | wt | 46.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -21.0) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.370× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 197 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -10.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2347 (line)]] | alt | 15.0 | 5 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.15× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 42.0 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.70× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -19.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.229× (z -12.8) |
| [[A-427 (line)]] | wt | 52.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.33× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 51.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[H4 (line)]] | wt | 87.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -12.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 151 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 48.6 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -11.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SHP-77 (line)]] | alt | 56.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.0) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.69× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 49.9 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.62× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.96× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 79.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.75× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -19.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.67× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HT-29 (line)]] | alt | 46.1 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.440× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 43.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.28× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -14.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[LS 180 (line)]] | wt | 63.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.173× (z -8.5) |
| [[PANC-1 (line)]] | alt | 52.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -12.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[RPMI-7951 (line)]] | alt | 54.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.42× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SK-MEL-2 (line)]] | alt | 59.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.09× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -13.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 13.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.61× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +12.7) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[C-33 A (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0965× (z -20.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CHP-212 (line)]] | wt | 76.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -9.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 21.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +8.5) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -8.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[J82 (line)]] | alt | 26.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.35× (z +9.6) | — |
| [[LoVo (line)]] | wt | 37.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.09× (z +17.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.71× (z +15.2) | — |
| [[NCI-H23 (line)]] | alt | 56.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.75× (z +9.1) | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -10.4) ⚠ cell-cycle shift, explains ~1% of this change |
| [[SW48 (line)]] | wt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 21.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.17× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.77 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.36 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYCP2L]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PPP1R32]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.62 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[PLAC1]] | +0.61 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[PIK3C2A]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 | pathway: Clathrin-mediated endocytosis |
| [[TMEM178A]] | +0.57 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[TMEM14B]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CRYBB2P1-1]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 | ⚠ same locus (43.8 kb, same strand: neighbours can correlate without regulation) |
| [[WDR49]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[BCO2]] | +0.56 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ANKFN1]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[KAZN]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[CCDC146]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF512B]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[ZNF414]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[EPC2]] | -0.55 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[ZNF623]] | -0.53 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[ZNF252P-1]] | -0.51 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ZBTB45]] | -0.51 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZFP41]] | -0.49 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[RBM15B]] | -0.49 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[ZNF252P]] | -0.48 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[FBXO38]] | -0.48 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PABIR1]] | -0.48 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ZNF839]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02885]] | B | LINC02885 activity raises GRK3's level | lines that do not express LINC02885 (15) vs lines expressing it (35) | 1.84× lower at baseline in the lines without LINC02885 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01399, PCDHB2, ENSG00000258168; maybe low, not absent |
| [[CRYBB2P1-1]] | C | CRYBB2P1-1 activity raises GRK3's level | lines that do not express CRYBB2P1-1 (4) vs lines expressing it (46) | 3.65× lower at baseline in the lines without CRYBB2P1-1 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYBB2P1-1]] | C | GRK3 activity raises CRYBB2P1-1's level | lines that do not express GRK3 (3) vs lines expressing it (47) | 4.41× lower at baseline in the lines without GRK3 | 0.006 | ⚠ few lines (3 vs 47); across organs; also absent: PALS2, PAM; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.540). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.6, -19.1); signed map (7.5, 7.0). **Vector** length 108, 28.1% of its response variance represented; |z| ≥ 3 in 1,244 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +14.2 | +16.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +10.6 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.2 | +10.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.9 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -6.1 | -13.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.3 | -10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.0 | -9.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -4.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:25,564,675-25,729,294 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BARK2; previously ADRBK2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; G protein-coupled receptor kinase family |
| Reactome | 7 pathways, smallest: G alpha (s) signalling events; Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P35626](https://www.uniprot.org/uniprotkb/P35626) (G protein-coupled receptor kinase 3):

> Specifically phosphorylates the activated forms of G protein-coupled receptors. Such receptor phosphorylation initiates beta-arrestin-mediated receptor internalization, and signaling events leading to their desensitization. Phosphorylates the agonist-occupied form of the beta-adrenergic and closely related receptors (By similarity). Also phosphorylates ligand-bound C3a and C5a anaphylatoxin receptors (C3AR1 and C5AR1, respectively), leading to receptor desensitization. Positively regulates …

**Summary**, from NCBI Gene [157](https://www.ncbi.nlm.nih.gov/gene/157):

> The beta-adrenergic receptor kinase specifically phosphorylates the agonist-occupied form of the beta-adrenergic and related G protein-coupled receptors. Overall, the beta adrenergic receptor kinase 2 has 85% amino acid similarity with beta adrenergic receptor kinase 1, with the protein kinase catalytic domain having 95% similarity. These data suggest the existence of a family of receptor kinases which may serve broadly to regulate receptor function. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:290) · Entrez [157](https://www.ncbi.nlm.nih.gov/gene/157) · UniProt [P35626](https://www.uniprot.org/uniprotkb/P35626) · Ensembl [ENSG00000100077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100077)

## Data

Gene col 1860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1860); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1860]; `tensor/DDL_lfc|DDL_z.npy` [1860]; `embed/gene_vectors.npy` [1860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1860 or target_col == 1860). Every well: [[GRK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

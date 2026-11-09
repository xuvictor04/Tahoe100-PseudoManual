---
symbol: "AMPD3"
type: "gene"
col: 5476
ensembl_id: "ENSG00000133805"
name: "adenosine monophosphate deaminase 3"
location: "11p15.4"
module: 181
arm: "+"
pooled_cpm: 74.69
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 31
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# AMPD3

*adenosine monophosphate deaminase 3* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +16.1, q 0e+00, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (20 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.261× (z -24.8, q 0e+00, down in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.711× (z -8.9, q 4e-17, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSANTD3]] (+0.66, fdr 9e-06), [[TMEFF1]] (+0.64, fdr 7e-06), [[IL1A]] (+0.62, fdr 1e-05); moves opposite to [[ATF7]] (-0.54, fdr 1e-04), [[TCTN3]] (-0.47, fdr 1e-04), [[APMAP]] (-0.46, fdr 4e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[G0S2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +16.1 | 0e+00 | 30/46 (NCI-H1792, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.64×** | +14.8 | 0e+00 | 34/48 (RPMI-7951, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +6.4 | 4e-08 | 30/47 (A498, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +5.9 | 5e-07 | 23/47 (hTERT-HPNE, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +5.6 | 3e-06 | 24/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.76×** | +5.5 | 4e-06 | 24/47 (CFPAC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.1 | 3e-05 | 22/46 (H4, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.0 | 4e-05 | 24/47 (HT-29, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.27×** | +4.5 | 5e-04 | 22/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +4.3 | 8e-04 | 22/47 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.001 | 22/46 (PANC-1, HepG2/C3A, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 17/48 (J82, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.23×** | +3.8 | 0.008 | 18/46 (RKO, H4, …) | rises with dose | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.012 | 18/47 (MIA PaCa-2, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.025 | 17/46 (BT-474, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.094 | 8/47 (BT-474, CHP-212, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 22 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.261×** | -24.8 | 0e+00 | 45/47 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.324×** | -20.8 | 0e+00 | 45/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.373×** | -18.1 | 0e+00 | 42/47 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.507×** | -12.0 | 4e-31 | 28/39 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.529×** | -11.3 | 2e-27 | 35/46 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.551×** | -10.5 | 5e-24 | 30/47 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.580×** | -10.0 | 9e-22 | 35/47 (BT-474, NCI-H23, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.581×** | -10.0 | 1e-21 | 34/47 (A-427, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.711×** | -8.9 | 4e-17 | 32/47 (SK-MEL-2, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **0.627×** | -8.6 | 5e-16 | 27/47 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.658×** | -7.7 | 7e-13 | 28/47 (BT-474, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.681×** | -6.8 | 5e-10 | 29/46 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.678×** | -6.6 | 2e-09 | 25/40 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.701×** | -6.5 | 2e-09 | 31/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.743×** | -5.5 | 2e-06 | 25/47 (COLO 205, BT-474, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.771×** | -4.8 | 6e-05 | 22/48 (HS-578T, NCI-H2122, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.779×** | -4.6 | 1e-04 | 22/47 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.663×** | -4.0 | 0.002 | 17/47 (NCI-H23, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.672×** | -3.8 | 0.003 | 18/48 (SK-MEL-2, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.815×** | -3.7 | 0.004 | 17/47 (NCI-H1792, A549, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.693×** | -3.5 | 0.009 | 12/46 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.827×** | -3.5 | 0.010 | 19/47 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -3.4 | 0.014 | 20/47 (A549, J82, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.728×** | -3.1 | 0.043 | 11/48 (NCI-H1573, A549, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.842× | -3.0 | 0.043 | 15/48 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.847× | -3.0 | 0.043 | 10/48 (A-172, HOP62, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.730×** | -3.0 | 0.043 | 8/47 (LoVo, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.890× | -3.0 | 0.043 | 11/47 (NCI-H1792, A549, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | 0.849× | -2.9 | 0.060 | 6/47 (HS-578T, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 94.8 | 0 | 13 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 90.4 | 1 | 11 (11 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -16.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 137 | 4 (1 ⚠) | 8 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +24.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -11.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 127 | 0 | 10 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -16.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.6) |
| [[HT-29 (line)]] | alt | 46.3 | 1 | 8 (7 ⚠) | [[Auranofin (drug)]] 5 µM 4.65× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.207× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 213 | 3 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.0856× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HS-578T (line)]] | alt | 128 | 3 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +27.8) | [[Panobinostat (drug)]] 5 µM 0.139× (z -15.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 116 | 2 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[LS 180 (line)]] | wt | 50.9 | 0 | 8 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -17.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 213 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +34.8) | [[Panobinostat (drug)]] 5 µM 0.245× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.389× (z -9.4) |
| [[RKO (line)]] | wt | 106 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.5) |
| [[SNU-423 (line)]] | alt | 182 | 1 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SW480 (line)]] | alt | 58.4 | 0 | 8 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -19.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 76.1 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -14.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 234 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.179× (z -12.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 146 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[PANC-1 (line)]] | alt | 56.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +24.2) | — |
| [[A-172 (line)]] | wt | 107 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -11.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 39.5 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +14.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0420× (z -22.8) ⚠ toxic |
| [[A498 (line)]] | wt | 43.5 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +32.0) | — |
| [[A549 (line)]] | wt | 104 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 79.3 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -12.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.282× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 30.3 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +18.5) | [[Harringtonine (drug)]] 5 µM 0.270× (z -11.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[C32 (line)]] | wt | 50.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 47.6× (z +33.9) | — |
| [[CFPAC-1 (line)]] | alt | 83.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.257× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 32.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +26.2) | [[Belinostat (drug)]] 5 µM 0.209× (z -13.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 38.2 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 111 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.63× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[HCT15 (line)]] | alt | 80.7 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 35.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 28.4× (z +29.2) | — |
| [[Panc 03.27 (line)]] | alt | 46.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 33.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.00× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.293× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 31.1 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.159× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 36.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +17.3) | [[Panobinostat (drug)]] 5 µM 0.285× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 83.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H2030 (line)]] | alt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +16.3) | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0594× (z -10.3) |
| [[SW 1271 (line)]] | alt | 64.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0623× (z -9.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD3]] | +0.66 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[TMEFF1]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[IL1A]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[LINC01933]] | +0.59 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[MSANTD3-TMEFF1]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ENTHD1]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[DSE]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZNF774]] | +0.57 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[HLA-L-1]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[LINC01291]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[IRAG1-AS1]] | +0.57 | +0.55 / +0.46 | both halves | 2e-05 | ⚠ same locus (33.7 kb, same strand: neighbours can correlate without regulation) |
| [[SLC4A10]] | +0.56 | +0.60 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF7]] | -0.54 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[TCTN3]] | -0.47 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[APMAP]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[TUFM]] | -0.46 | -0.49 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[G0S2]] | B | G0S2 activity raises AMPD3's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.05× lower at baseline in the lines without G0S2 | 0.022 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[ANKRD30B]] | B | ANKRD30B activity raises AMPD3's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 2.37× lower at baseline in the lines without ANKRD30B | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF |
| [[ADTRP]] | B | ADTRP activity raises AMPD3's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without ADTRP | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[AFF3]] | B | AFF3 activity raises AMPD3's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without AFF3 | 0.048 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[ROR1-AS1]] | B | ROR1-AS1 activity raises AMPD3's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without ROR1-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[HMGN2P46]] | B | HMGN2P46 activity raises AMPD3's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.13× lower at baseline in the lines without HMGN2P46 | 0.058 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[CSF2]] | B | CSF2 activity raises AMPD3's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.98× lower at baseline in the lines without CSF2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[CXCL8]] | B | CXCL8 activity raises AMPD3's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.82× lower at baseline in the lines without CXCL8 | 0.096 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.486). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.8, -1.1); signed map (39.8, 12.0). **Vector** length 129, 40.4% of its response variance represented; |z| ≥ 3 in 1,605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.9 | +16.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.0 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.3 | +14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +7.9 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +5.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.5 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.2 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.7 | -7.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -5.4 | -10.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -11.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.9 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.4 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.1 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | adenosine monophosphate deaminase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:10,308,313-10,507,579 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Adenosine deaminase family |
| Hallmark sets | HYPOXIA |
| Reactome | 5 pathways, smallest: Purine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01432](https://www.uniprot.org/uniprotkb/Q01432) (AMP deaminase 3):

> AMP deaminase plays a critical role in energy metabolism.

**Summary**, from NCBI Gene [272](https://www.ncbi.nlm.nih.gov/gene/272):

> This gene encodes a member of the AMP deaminase gene family. The encoded protein is a highly regulated enzyme that catalyzes the hydrolytic deamination of adenosine monophosphate to inosine monophosphate, a branch point in the adenylate catabolic pathway. This gene encodes the erythrocyte (E) isoforms, whereas other family members encode isoforms that predominate in muscle (M) and liver (L) cells. Mutations in this gene lead to the clinically asymptomatic, autosomal recessive condition …

**Accessions** — [HGNC:470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:470) · Entrez [272](https://www.ncbi.nlm.nih.gov/gene/272) · UniProt [Q01432](https://www.uniprot.org/uniprotkb/Q01432) · Ensembl [ENSG00000133805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133805)

## Data

Gene col 5476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5476); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5476]; `tensor/DDL_lfc|DDL_z.npy` [5476]; `embed/gene_vectors.npy` [5476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5476 or target_col == 5476). Every well: [[AMPD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMPD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

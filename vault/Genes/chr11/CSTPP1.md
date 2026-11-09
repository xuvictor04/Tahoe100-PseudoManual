---
symbol: "CSTPP1"
type: "gene"
col: 7346
ensembl_id: "ENSG00000149179"
name: "centriolar satellite-associated tubulin polyglutamylase complex regulator 1"
location: "11p11.2"
module: 230
arm: "+"
pooled_cpm: 116.25
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/230"]
generated_by: "tahoemap"
---

# CSTPP1

*centriolar satellite-associated tubulin polyglutamylase complex regulator 1* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.41× (z +9.0, q 2e-16, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.389× (z -34.6, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MINDY4]] (+0.70, fdr 7e-06), [[DNAAF4]] (+0.67, fdr 3e-05), [[VTA1]] (+0.67, fdr 7e-06); moves opposite to [[CRYGS]] (-0.52, fdr 2e-05), [[HNRNPLL]] (-0.52, fdr 3e-05), [[MTR]] (-0.51, fdr 6e-05).
> It is in [[Module 230]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DNAAF4]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +9.0 | 2e-16 | 34/48 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +8.4 | 1e-14 | 31/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.34×** | +7.2 | 1e-10 | 29/48 (A-172, C32, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +6.4 | 3e-08 | 29/48 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.28×** | +6.3 | 4e-08 | 26/48 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.19× | +6.2 | 5e-08 | 21/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.26×** | +5.9 | 3e-07 | 29/48 (AsPC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.8 | 1e-04 | 22/47 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +4.5 | 5e-04 | 20/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.004 | 19/49 (HEC-1-A, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.9 | 0.005 | 16/48 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.015 | 13/48 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.6 | 0.015 | 17/48 (RKO, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +3.4 | 0.026 | 11/48 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.029 | 16/47 (SW480, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.032 | 9/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.038 | 9/49 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.060 | 3/49 (NCI-H1573, LS 180, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7346.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.389×** | -34.6 | 0e+00 | 48/49 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.455×** | -19.7 | 0e+00 | 41/48 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -16.1 | 0e+00 | 38/49 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -16.0 | 0e+00 | 40/50 (C-33 A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -15.4 | 0e+00 | 36/44 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -13.0 | 7e-37 | 37/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.595×** | -12.5 | 8e-34 | 37/45 (LoVo, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.765×** | -9.8 | 6e-21 | 27/48 (COLO 205, LoVo, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.708×** | -9.0 | 2e-17 | 37/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.710×** | -8.9 | 3e-17 | 29/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.717×** | -8.7 | 2e-16 | 29/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -8.6 | 3e-16 | 32/48 (LoVo, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.763×** | -7.0 | 1e-10 | 26/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.805×** | -5.6 | 7e-07 | 21/48 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.809×** | -5.5 | 1e-06 | 25/48 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.820×** | -5.2 | 8e-06 | 22/48 (LoVo, LS 180, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.682×** | -5.0 | 2e-05 | 26/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.878× | -4.8 | 5e-05 | 17/49 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.846× | -4.4 | 4e-04 | 19/47 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.842× | -4.3 | 4e-04 | 20/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.891× | -4.2 | 6e-04 | 15/48 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.868× | -3.7 | 0.005 | 12/48 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.785×** | -3.2 | 0.034 | 13/46 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.850× | -3.0 | 0.050 | 17/48 (LoVo, SW480, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 325 | 0 | 16 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -27.5) |
| [[LS 180 (line)]] | wt | 184 | 0 | 14 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -26.5) |
| [[MIA PaCa-2 (line)]] | alt | 94.1 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -24.0) |
| [[NCI-H460 (line)]] | wt | 84.5 | 0 | 11 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.245× (z -21.9) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -21.7) |
| [[SW480 (line)]] | alt | 195 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -38.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -21.7) |
| [[PANC-1 (line)]] | alt | 104 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -20.6) |
| [[A498 (line)]] | wt | 149 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -21.1) |
| [[COLO 205 (line)]] | alt | 252 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -28.6) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -26.4) |
| [[HEC-1-A (line)]] | alt | 90.3 | 4 | 4 | [[Panobinostat (drug)]] 5 µM 2.03× (z +10.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -15.4) |
| [[C32 (line)]] | wt | 103 | 0 | 7 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -20.0) |
| [[HOP62 (line)]] | alt | 98.0 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.95× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -21.0) |
| [[LOX-IMVI (line)]] | wt | 110 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.336× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 49.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +16.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 7.00× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 154 | 0 | 6 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -19.8) |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -22.1) |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.9) |
| [[A-172 (line)]] | wt | 117 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -18.4) |
| [[BT-474 (line)]] | alt | 80.3 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.319× (z -11.1) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.5) |
| [[HCT15 (line)]] | alt | 130 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 79.2 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -16.9) |
| [[RKO (line)]] | wt | 136 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 114 | 1 | 3 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.20× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 149 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -18.8) |
| [[NCI-H2347 (line)]] | alt | 81.1 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.19× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -19.5) |
| [[SNU-423 (line)]] | alt | 100 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -17.8) |
| [[SW1417 (line)]] | alt | 90.7 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -21.6) |
| [[A-427 (line)]] | wt | 113 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -11.8) |
| [[CHP-212 (line)]] | wt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0848× (z -17.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 97.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -19.0) |
| [[SHP-77 (line)]] | alt | 213 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -10.0) |
| [[A549 (line)]] | wt | 108 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 37.3 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.42× (z +8.8) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.36× (z +8.6) | — |
| [[H4 (line)]] | wt | 69.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -11.6) |
| [[HT-29 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -20.3) |
| [[hTERT-HPNE (line)]] | wt | 78.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.5) |
| [[J82 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -20.0) |
| [[NCI-H1792 (line)]] | alt | 88.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -17.5) |
| [[SNU-1 (line)]] | wt | 98.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.235× (z -12.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -11.4) |
| [[SW 1088 (line)]] | alt | 93.0 | 0 | 2 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0715× (z -9.5) |
| [[SW 900 (line)]] | alt | 54.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -12.5) |
| [[SW48 (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -13.4) |
| [[AN3 CA (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0792× (z -17.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 62.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY4]] | +0.70 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[DNAAF4]] | +0.67 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[VTA1]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[STX8]] | +0.67 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MNAT1]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[DHX57]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FTO]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CWC27]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[WDR7]] | +0.63 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[VPS50]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[DCTN4]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYGS]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[HNRNPLL]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[MTR]] | -0.51 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[SLC35F5]] | -0.49 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[RO60]] | -0.48 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[LINC01135]] | -0.48 | -0.28 / -0.42 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAAF4]] | C | DNAAF4 activity raises CSTPP1's level | lines that do not express DNAAF4 (3) vs lines expressing it (47) | 2.12× lower at baseline in the lines without DNAAF4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 230]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-27.0, -5.3); signed map (-20.0, -19.2). **Vector** length 119, 35.7% of its response variance represented; |z| ≥ 3 in 1,393 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +8.7 | +6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | +8.0 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.9 | +3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +6.9 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.4 | -34.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -10.2 | -16.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -19.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.7 | -13.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.2 | -5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | centriolar satellite-associated tubulin polyglutamylase complex regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,936,689-47,164,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22210, MGC4707; previously C11orf49 |
| Gene groups (HGNC) | Tubulin polyglutamylase complex subunits; Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6J7](https://www.uniprot.org/uniprotkb/Q9H6J7) (Centriolar satellite-associated tubulin polyglutamylase complex regulator 1):

> Regulator of the tubulin polyglutamylase complex (TPGC) that controls cytoskeletal organization, nuclear shape, and cilium disassembly by balancing microtubule and actin assembly. Regulates the assembly and stability of the TPGC and thereby modulates polyglutamylation of the microtubule, which antagonizes MAP4 binding.

**Summary**, from NCBI Gene [79096](https://www.ncbi.nlm.nih.gov/gene/79096):

> Enables protein-macromolecule adaptor activity. Involved in regulation of protein complex stability. Is active in centriolar satellite. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28720) · Entrez [79096](https://www.ncbi.nlm.nih.gov/gene/79096) · UniProt [Q9H6J7](https://www.uniprot.org/uniprotkb/Q9H6J7) · Ensembl [ENSG00000149179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149179)

## Data

Gene col 7346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7346); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7346]; `tensor/DDL_lfc|DDL_z.npy` [7346]; `embed/gene_vectors.npy` [7346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7346 or target_col == 7346). Every well: [[CSTPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSTPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

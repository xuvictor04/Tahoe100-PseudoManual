---
symbol: "LINC-PINT"
type: "gene"
col: 13808
ensembl_id: "ENSG00000231721"
name: "long independently transcribed non-coding RNA, p53 induced transcript"
location: "7q32.3"
module: 116
arm: "+"
pooled_cpm: 969.03
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 28
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# LINC-PINT

*long independently transcribed non-coding RNA, p53 induced transcript* — 7q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.55× (z +8.3, q 8e-14, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.224× (z -28.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00513]] (+0.65, fdr 1e-05, ⚠ same locus), [[SRGAP1]] (+0.59, fdr 1e-05), [[MIR222HG]] (+0.58, fdr 7e-06), [[ZFPM2-AS1]] (+0.56, fdr 3e-05); moves opposite to [[UFSP2]] (-0.48, fdr 4e-05), [[PARP2]] (-0.47, fdr 7e-05), [[OTUD3]] (-0.46, fdr 3e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[HOXA13]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FAM86HP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +8.3 | 8e-14 | 38/48 (SW480, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +6.4 | 5e-08 | 33/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.22×** | +5.3 | 2e-05 | 27/48 (LS 180, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +5.2 | 3e-05 | 27/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.4 | 0.001 | 28/48 (SK-MEL-2, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.25×** | +4.3 | 0.002 | 29/48 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.004 | 34/48 (BT-474, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.004 | 27/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.004 | 26/47 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.009 | 37/49 (LS 180, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.010 | 24/48 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.010 | 28/49 (Hs 766T, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.6 | 0.015 | 11/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.20× | +3.5 | 0.022 | 20/49 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.20× | +3.4 | 0.022 | 22/48 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.097 | 24/48 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.224×** | -28.3 | 0e+00 | 48/48 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.244×** | -26.6 | 0e+00 | 48/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.332×** | -20.0 | 0e+00 | 42/44 (SNU-1, A498, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.368×** | -18.9 | 0e+00 | 48/48 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.442×** | -15.4 | 0e+00 | 47/49 (RKO, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.657×** | -11.2 | 4e-27 | 33/48 (RKO, PANC-1, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -8.1 | 3e-14 | 40/47 (SNU-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.739×** | -8.1 | 5e-14 | 31/49 (A549, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.661×** | -7.8 | 4e-13 | 44/48 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.696×** | -6.8 | 5e-10 | 40/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.721×** | -6.2 | 4e-08 | 39/48 (SW1417, CFPAC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.740×** | -5.4 | 3e-06 | 32/50 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.743×** | -5.4 | 3e-06 | 28/48 (RKO, PANC-1, …) | rises with dose | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.766×** | -5.0 | 2e-05 | 27/49 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.546×** | -5.0 | 2e-05 | 39/48 (RKO, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.783×** | -4.6 | 1e-04 | 29/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.780×** | -4.5 | 2e-04 | 29/48 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.832×** | -4.3 | 6e-04 | 22/48 (SHP-77, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.863× | -3.9 | 0.003 | 19/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.627×** | -3.8 | 0.003 | 27/48 (SW1417, A549, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.637×** | -3.7 | 0.005 | 25/48 (CHP-212, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.638×** | -3.7 | 0.005 | 28/47 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.681×** | -3.2 | 0.035 | 23/48 (SW1417, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.794×** | -3.1 | 0.043 | 23/47 (RPMI-7951, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 345 | 8 (4 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.55× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.229× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 1,006 | 7 (3 ⚠) | 6 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.04× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.189× (z -21.5) |
| [[NCI-H23 (line)]] | alt | 1,909 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -23.8) |
| [[RKO (line)]] | wt | 2,855 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.215× (z -21.8) |
| [[HEC-1-A (line)]] | alt | 633 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0934× (z -35.3) |
| [[LOX-IMVI (line)]] | wt | 1,344 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -24.4) |
| [[SNU-1 (line)]] | wt | 1,504 | 1 | 9 (6 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.92× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.121× (z -29.2) |
| [[SW48 (line)]] | wt | 2,921 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -17.9) |
| [[A549 (line)]] | wt | 1,176 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -22.3) |
| [[C32 (line)]] | wt | 1,389 | 4 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.307× (z -13.8) |
| [[H4 (line)]] | wt | 1,184 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -19.9) |
| [[HepG2_C3A (line)]] | wt | 479 | 2 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.16× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -15.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.295× (z -15.2) |
| [[HT-29 (line)]] | alt | 881 | 1 | 7 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.12× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.237× (z -18.5) |
| [[NCI-H1792 (line)]] | alt | 1,174 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -18.3) |
| [[NCI-H460 (line)]] | wt | 1,323 | 1 (1 ⚠) | 7 (4 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.03× (z +9.2) ⚠ toxic; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.225× (z -20.3) |
| [[PANC-1 (line)]] | alt | 820 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -18.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.203× (z -18.5) |
| [[A-427 (line)]] | wt | 1,027 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -19.9) |
| [[A498 (line)]] | wt | 1,053 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -22.3) |
| [[CHP-212 (line)]] | wt | 547 | 3 (1 ⚠) | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.86× (z +9.0) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.31× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.243× (z -14.5) |
| [[HS-578T (line)]] | alt | 776 | 4 (1 ⚠) | 3 | [[Digitoxin (drug)]] 0.5 µM 2.17× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -17.1) |
| [[KATO III (line)]] | alt | 496 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -23.5) |
| [[LoVo (line)]] | wt | 855 | 1 (1 ⚠) | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.178× (z -19.0) |
| [[SW 900 (line)]] | alt | 1,111 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -20.2) |
| [[SW1417 (line)]] | alt | 1,263 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -19.0) |
| [[AsPC-1 (line)]] | alt | 1,024 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.05× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.200× (z -19.9) |
| [[CFPAC-1 (line)]] | alt | 900 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -24.5) |
| [[HOP62 (line)]] | alt | 829 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.84× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.230× (z -20.5) |
| [[MIA PaCa-2 (line)]] | alt | 1,584 | 0 | 6 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.610× (z -18.0) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.424× (z -9.5) |
| [[SHP-77 (line)]] | alt | 559 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -20.0) |
| [[SW480 (line)]] | alt | 699 | 2 | 4 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.48× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.191× (z -19.3) |
| [[A-172 (line)]] | wt | 376 | 2 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.11× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.256× (z -17.0) |
| [[C-33 A (line)]] | alt | 819 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.226× (z -15.1) |
| [[Hs 766T (line)]] | wt | 967 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.7) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 5 µM 0.226× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.330× (z -14.4) |
| [[J82 (line)]] | alt | 840 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -18.5) |
| [[LS 180 (line)]] | wt | 742 | 1 (1 ⚠) | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.63× (z +9.8) ⚠ cell-cycle shift, explains ~72% of this change | [[Panobinostat (drug)]] 5 µM 0.203× (z -22.6) |
| [[NCI-H2030 (line)]] | alt | 1,002 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -15.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.381× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 751 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 909 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -22.6) |
| [[RPMI-7951 (line)]] | alt | 700 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -17.0) |
| [[SNU-423 (line)]] | alt | 1,081 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -16.3) |
| [[SW 1271 (line)]] | alt | 922 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -12.9) |
| [[COLO 205 (line)]] | alt | 678 | 1 (1 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 1.81× (z +9.5) ⚠ cell-cycle shift, explains ~72% of this change | [[Panobinostat (drug)]] 5 µM 0.184× (z -19.3) |
| [[BT-474 (line)]] | alt | 272 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -14.1) |
| [[HCT15 (line)]] | alt | 690 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 846 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -16.0) |
| [[SW 1088 (line)]] | alt | 1,012 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -11.8) |
| [[AN3 CA (line)]] | alt | 950 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1,046 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 931 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 273 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00513]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SRGAP1]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MIR222HG]] | +0.58 | +0.66 / +0.60 | both halves | 7e-06 | same gene group |
| [[ZFPM2-AS1]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[ITGB1-DT]] | +0.56 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[BCAR3]] | +0.55 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[ITGA2-AS1]] | +0.53 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[HCG18]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[SLC20A2]] | +0.53 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[DOCK5]] | +0.53 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[KIFC3]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[DUSP5-DT]] | +0.51 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[NABP1]] | +0.51 | +0.37 / +0.51 | both halves | 8e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFSP2]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PARP2]] | -0.47 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[OTUD3]] | -0.46 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[SF3B2]] | -0.46 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[SRRM1]] | -0.46 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ALAD]] | -0.45 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[STRA6LP]] | -0.45 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[GPI]] | -0.45 | -0.19 / -0.38 | ⚠ not reproduced | 8e-04 |  |
| [[PRPF39]] | -0.44 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[YY1AP1]] | -0.44 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[HOXA13]] | -0.43 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[DOP1A]] | -0.43 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[KMT2C]] | -0.43 | -0.27 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA13]] | B | HOXA13 activity raises LINC-PINT's level | lines that do not express HOXA13 (14) vs lines expressing it (36) | 1.60× lower at baseline in the lines without HOXA13 | 0.020 | ⚠ within organs, on part of the lines; also absent: PRR5L |
| [[KLHL29]] | B | KLHL29 activity raises LINC-PINT's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without KLHL29 | 0.050 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[ITPRIP]] | B | ITPRIP activity raises LINC-PINT's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without ITPRIP | 0.051 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[BCAR3]] | B | BCAR3 activity raises LINC-PINT's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 1.57× lower at baseline in the lines without BCAR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[LAMA1]] | B | LAMA1 activity raises LINC-PINT's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.30× lower at baseline in the lines without LAMA1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[CASC11]] | B | CASC11 activity raises LINC-PINT's level | lines that do not express CASC11 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without CASC11 | 0.093 | ⚠ within organs, on part of the lines; also absent: ANKRD18A; maybe low, not absent |
| [[RPSAP52]] | B | RPSAP52 activity raises LINC-PINT's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 1.33× lower at baseline in the lines without RPSAP52 | 0.099 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity raises LINC-PINT's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without SPRY4-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM86HP]] | C | LINC-PINT's natural level weakens FAM86HP's drug response | LINC-PINT's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.03; direction not clear | 0.087 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.2, 10.2); signed map (11.4, 42.6). **Vector** length 124, 49.4% of its response variance represented; |z| ≥ 3 in 1,849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +9.4 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.0 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.7 | +1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +7.2 | +8.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +6.2 | +4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.6 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +1.8 |
| fall | [[venetoclax (drug)]] 5 µM |  | -5.3 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.7 | -5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | long independently transcribed non-coding RNA, p53 induced transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q32.3 — chr7:130,791,264-131,110,176 (-) |
| Ensembl biotype | lncRNA |
| Also known as | PINT, TISPL, FLJ43663, PINT87aa, LOC646329, LincRNA-Pint; previously MKLN1-AS1 |
| Gene groups (HGNC) | MicroRNA non-coding host genes; Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A455ZAR2](https://www.uniprot.org/uniprotkb/A0A455ZAR2) (Transcriptional regulator PINT87aa):

> Enhances the binding of the PAF1 complex to target gene promoters and plays a role in negative regulation of transcription. May function as an anchor to keep the PAF1 complex on target gene promoters, sequentially pausing RNA polymerase II-induced mRNA elongation. Inhibits FOXM1-mediated transcription of PHB2.

**Summary**, from NCBI Gene [378805](https://www.ncbi.nlm.nih.gov/gene/378805):

> Involved in negative regulation of transcription by RNA polymerase II. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26885) · Entrez [378805](https://www.ncbi.nlm.nih.gov/gene/378805) · UniProt [A0A455ZAR2](https://www.uniprot.org/uniprotkb/A0A455ZAR2) · Ensembl [ENSG00000231721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231721)

## Data

Gene col 13808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13808); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13808]; `tensor/DDL_lfc|DDL_z.npy` [13808]; `embed/gene_vectors.npy` [13808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13808 or target_col == 13808). Every well: [[LINC-PINT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LINC-PINT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

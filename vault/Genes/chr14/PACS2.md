---
symbol: "PACS2"
type: "gene"
col: 11025
ensembl_id: "ENSG00000179364"
name: "phosphofurin acidic cluster sorting protein 2"
location: "14q32.33"
module: 2
arm: "+"
pooled_cpm: 36.36
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PACS2

*phosphofurin acidic cluster sorting protein 2* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.48× (z +7.2, q 5e-10, up in 25 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 1.21× (z +5.1, q 8e-05, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.330× (z -29.7, q 0e+00, down in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.300× (z -22.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX2]] (+0.71, fdr 7e-06), [[CORO7]] (+0.69, fdr 7e-06), [[FBRSL1]] (+0.68, fdr 7e-06); moves opposite to [[DNAJB4]] (-0.63, fdr 1e-05), [[BTN3A3]] (-0.62, fdr 1e-05), [[CAPS2]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +7.2 | 5e-10 | 25/40 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | **1.21×** | +5.1 | 8e-05 | 21/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +5.1 | 8e-05 | 22/44 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 0.001 | 19/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +4.1 | 0.004 | 13/48 (SW 900, LoVo, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.004 | 15/47 (C-33 A, A-172, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.004 | 21/48 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.24×** | +4.0 | 0.004 | 18/47 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.22×** | +3.6 | 0.017 | 13/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.020 | 16/47 (SNU-423, H4, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.020 | 10/48 (CFPAC-1, HEC-1-A, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.027 | 12/48 (SW1417, C32, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.062 | 8/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.330×** | -29.7 | 0e+00 | 46/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.300×** | -22.0 | 0e+00 | 47/48 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.444×** | -15.4 | 0e+00 | 38/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.510×** | -12.8 | 3e-35 | 42/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -12.2 | 5e-32 | 38/48 (HT-29, SNU-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.584×** | -10.2 | 2e-22 | 37/47 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -9.4 | 4e-19 | 37/47 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.613×** | -9.3 | 1e-18 | 35/48 (J82, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.398×** | -9.1 | 4e-18 | 39/49 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.622×** | -9.0 | 1e-17 | 36/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.722×** | -8.7 | 1e-16 | 30/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.651×** | -8.1 | 2e-14 | 33/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.469×** | -7.5 | 3e-12 | 30/47 (LOX-IMVI, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.676×** | -7.0 | 1e-10 | 33/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.512×** | -6.6 | 1e-09 | 33/42 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -6.2 | 1e-08 | 26/48 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.799×** | -4.3 | 6e-04 | 21/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.769×** | -3.6 | 0.010 | 9/48 (PANC-1, A549, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 44.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -23.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.143× (z -16.0) |
| [[PANC-1 (line)]] | alt | 35.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -27.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -18.1) |
| [[SW480 (line)]] | alt | 38.9 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.441× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.471× (z -9.6) |
| [[A-427 (line)]] | wt | 66.3 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.337× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 38.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 30.5 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.217× (z -15.4) |
| [[A549 (line)]] | wt | 49.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -23.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.163× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 54.0 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.39× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -20.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.308× (z -13.1) |
| [[J82 (line)]] | alt | 39.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -19.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.264× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 45.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -17.5) |
| [[SW48 (line)]] | wt | 68.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -12.1) |
| [[A-172 (line)]] | wt | 41.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -22.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.223× (z -13.0) |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -24.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.159× (z -15.3) |
| [[LoVo (line)]] | wt | 34.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -19.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.295× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 28.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -11.1) |
| [[A498 (line)]] | wt | 13.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -12.0) |
| [[BT-474 (line)]] | alt | 53.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -18.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.166× (z -14.8) |
| [[HT-29 (line)]] | alt | 31.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.237× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -15.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.248× (z -9.0) |
| [[LS 180 (line)]] | wt | 41.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.359× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 32.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 43.8 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.334× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 47.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -22.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.247× (z -13.4) |
| [[RKO (line)]] | wt | 34.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.251× (z -10.2) |
| [[SNU-423 (line)]] | alt | 35.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -15.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.233× (z -10.9) |
| [[SW 900 (line)]] | alt | 35.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -16.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.283× (z -9.1) |
| [[SW1417 (line)]] | alt | 40.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -15.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.330× (z -10.1) |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 2 | — | [[Ranolazine (drug)]] 0.5 µM 0.0840× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 25.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.97× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.134× (z -12.4) |
| [[KATO III (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.469× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 28.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.170× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 47.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.219× (z -12.3) |
| [[SNU-1 (line)]] | wt | 36.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.162× (z -10.8) |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Verapamil (drug)]] 0.05 µM 0.0605× (z -8.6) |
| [[C32 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.260× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -11.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.306× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX2]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CORO7]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[FBRSL1]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[TCF3]] | +0.67 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ABCA3]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[DGKZ]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[TNK2]] | +0.65 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[DVL1]] | +0.65 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[CROCCP3]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MAPK1]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[DOP1B]] | +0.61 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[ZDHHC8]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB4]] | -0.63 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[BTN3A3]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CAPS2]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[TET2]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[RBM7]] | -0.56 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NSUN3]] | -0.55 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[BTN3A1]] | -0.55 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[RNASEL]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[KLHL3]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[CREB3L4]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[BDH2]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[FUNDC1]] | -0.53 | -0.58 / -0.40 | both halves | 5e-05 | STRING 525 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers PACS2's level | compounds that target MTOR: 3 of 8 raise it (Rapamycin, Sapanisertib, Temsirolimus) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.9, -23.6); signed map (-44.6, -8.0). **Vector** length 88.4, 22.1% of its response variance represented; |z| ≥ 3 in 1,263 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | -0.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.1 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.8 | -29.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -15.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphofurin acidic cluster sorting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,300,563-105,398,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0602; previously PACS1L |
| Gene groups (HGNC) | Phosphofurin acidic cluster sorting protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VP3](https://www.uniprot.org/uniprotkb/Q86VP3) (Phosphofurin acidic cluster sorting protein 2):

> Multifunctional sorting protein that controls the endoplasmic reticulum (ER)-mitochondria communication, including the apposition of mitochondria with the ER and ER homeostasis. In addition, in response to apoptotic inducer, translocates BIB to mitochondria, which initiates a sequence of events including the formation of mitochondrial truncated BID, the release of cytochrome c, the activation of caspase-3 thereby causing cell death. May also be involved in ion channel trafficking, directing …

**Summary**, from NCBI Gene [23241](https://www.ncbi.nlm.nih.gov/gene/23241):

> Predicted to enable transmembrane transporter binding activity. Involved in endoplasmic reticulum calcium ion homeostasis; mitochondrion-endoplasmic reticulum membrane tethering; and protein localization to plasma membrane. Acts upstream of or within protein localization to phagophore assembly site. Located in endoplasmic reticulum. Implicated in developmental and epileptic encephalopathy 66. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23794](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23794) · Entrez [23241](https://www.ncbi.nlm.nih.gov/gene/23241) · UniProt [Q86VP3](https://www.uniprot.org/uniprotkb/Q86VP3) · Ensembl [ENSG00000179364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179364)

## Data

Gene col 11025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11025); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11025]; `tensor/DDL_lfc|DDL_z.npy` [11025]; `embed/gene_vectors.npy` [11025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11025 or target_col == 11025). Every well: [[PACS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PACS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

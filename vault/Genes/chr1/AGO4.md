---
symbol: "AGO4"
type: "gene"
col: 5591
ensembl_id: "ENSG00000134698"
name: "argonaute RISC component 4"
location: "1p34.3"
module: 187
arm: "+"
pooled_cpm: 48.93
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 37
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# AGO4

*argonaute RISC component 4* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Rapamycin (drug)]] 0.5 µM: 1.26× (z +4.4, q 0.004, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (19 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.232× (z -27.8, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.394× (z -25.1, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARRE1]] (+0.68, fdr 7e-06), [[RWDD3]] (+0.68, fdr 7e-06), [[EZH1]] (+0.63, fdr 7e-06); moves opposite to [[G6PD]] (-0.55, fdr 2e-05), [[NOLC1]] (-0.53, fdr 1e-05), [[ETF1]] (-0.53, fdr 2e-05).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rapamycin (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 0.004 | 23/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.3 | 0.004 | 22/47 (AsPC-1, LoVo, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.7 | 0.037 | 11/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.037 | 17/49 (LS 180, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.037 | 17/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.20×** | +3.4 | 0.061 | 17/47 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.061 | 11/47 (LS 180, PANC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.14 | 12/47 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.12× | +3.0 | 0.16 | 9/49 (PANC-1, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 24 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5591.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.232×** | -27.8 | 0e+00 | 48/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.249×** | -26.5 | 0e+00 | 47/48 (SNU-423, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.394×** | -25.1 | 0e+00 | 38/48 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.324×** | -21.4 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.414×** | -16.8 | 0e+00 | 46/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.461×** | -14.2 | 1e-43 | 40/47 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.487×** | -13.7 | 1e-40 | 35/47 (SNU-423, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.469×** | -13.3 | 1e-38 | 37/43 (NCI-H1792, NCI-H460, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.263×** | -13.1 | 4e-37 | 41/49 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.539×** | -11.7 | 5e-30 | 41/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.538×** | -11.3 | 5e-28 | 33/48 (NCI-H460, A-172, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.682×** | -10.3 | 5e-23 | 31/48 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.586×** | -9.8 | 8e-21 | 27/41 (SW 900, HS-578T, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.599×** | -9.7 | 9e-21 | 36/48 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.414×** | -8.6 | 2e-16 | 37/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.743×** | -7.9 | 6e-14 | 36/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.449×** | -7.8 | 2e-13 | 35/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.454×** | -7.7 | 4e-13 | 35/47 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.468×** | -7.4 | 3e-12 | 39/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.736×** | -5.8 | 1e-07 | 26/48 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -5.6 | 5e-07 | 26/48 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.567×** | -5.5 | 6e-07 | 26/47 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.630×** | -4.5 | 1e-04 | 23/49 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.723×** | -4.4 | 2e-04 | 23/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.746×** | -4.0 | 0.001 | 18/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.69 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.2 | 0 | 17 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -25.3) |
| [[MIA PaCa-2 (line)]] | alt | 86.7 | 0 | 15 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -20.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.354× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 73.6 | 0 | 13 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0354× (z -43.9) |
| [[A-172 (line)]] | wt | 45.2 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -24.9) |
| [[PANC-1 (line)]] | alt | 63.6 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -20.2) |
| [[SNU-423 (line)]] | alt | 72.4 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -24.8) |
| [[HEC-1-A (line)]] | alt | 58.8 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -19.7) |
| [[SW 900 (line)]] | alt | 46.9 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0738× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.6) |
| [[A549 (line)]] | wt | 50.8 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -17.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.332× (z -15.3) |
| [[HOP62 (line)]] | alt | 62.4 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -28.4) |
| [[HS-578T (line)]] | alt | 41.3 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -23.3) |
| [[LOX-IMVI (line)]] | wt | 43.6 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.5) |
| [[C32 (line)]] | wt | 36.5 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.7) |
| [[J82 (line)]] | alt | 51.2 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -24.6) |
| [[NCI-H1573 (line)]] | alt | 43.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -22.3) |
| [[NCI-H2347 (line)]] | alt | 49.4 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -16.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.8) |
| [[SW480 (line)]] | alt | 45.6 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -19.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.324× (z -11.5) |
| [[Hs 766T (line)]] | wt | 59.2 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -15.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.0) |
| [[LoVo (line)]] | wt | 40.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -20.7) |
| [[CFPAC-1 (line)]] | alt | 37.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.3) |
| [[COLO 205 (line)]] | alt | 34.5 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.5) |
| [[HCT15 (line)]] | alt | 53.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 49.5 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -13.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 49.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0937× (z -17.1) |
| [[SK-MEL-2 (line)]] | alt | 72.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.9) |
| [[C-33 A (line)]] | alt | 85.4 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -13.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 38.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[hTERT-HPNE (line)]] | wt | 39.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -16.6) |
| [[KATO III (line)]] | alt | 25.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[NCI-H23 (line)]] | alt | 44.7 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -18.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.7) |
| [[A-427 (line)]] | wt | 56.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -15.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 19.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.9) |
| [[AN3 CA (line)]] | alt | 67.8 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -12.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 24.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 57.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0777× (z -21.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 46.5 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0782× (z -17.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 44.5 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -11.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 42.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -12.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 41.3 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 57.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -13.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 34.0 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 44.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.174× (z -10.0) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARRE1]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RWDD3]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[EZH1]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[DSTYK]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ATXN3]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SLC49A4]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[RP9P]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[TATDN3]] | +0.58 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[EAPP]] | +0.58 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[MTFMT]] | +0.58 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[DENND10]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[THAP3]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[G6PD]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 | pathway: TP53 Regulates Metabolic Genes |
| [[NOLC1]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ETF1]] | -0.53 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[SLC25A10]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SYS1-DBNDD2]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SCART1]] | -0.52 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[LRRC59]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CLSTN3]] | -0.51 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[ARL5B]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[FAT1]] | -0.51 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TNC]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ATP5F1B]] | -0.48 | -0.39 / -0.46 | both halves | 6e-05 | pathway: Organelle biogenesis and maintenance |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | AGO4's natural level lowers the cells' numbers under Anethole trithione 0.5 µM (makes them more sensitive) | AGO4's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.429 over the table, 0.093 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.2, -44.0); signed map (-15.4, 7.4). **Vector** length 94.0, 28.7% of its response variance represented; |z| ≥ 3 in 1,422 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | +5.1 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.7 | +3.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -16.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.3 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -5.2 | -13.3 |
|  | [[EX229 (drug)]] 5 µM |  | -5.1 | -8.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.6 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | argonaute RISC component 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,808,016-35,857,890 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hAGO4, KIAA1567, FLJ20033; previously EIF2C4 |
| Gene groups (HGNC) | RISC loading complex subunits; Argonaute RISC component family |
| Hallmark sets | DNA_REPAIR |
| Reactome | 69 pathways, smallest: Post-transcriptional silencing by small RNAs; Regulation of NPAS4 mRNA translation; Regulation of CDH11 mRNA translation by microRNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCK5](https://www.uniprot.org/uniprotkb/Q9HCK5) (Protein argonaute-4):

> Required for RNA-mediated gene silencing (RNAi). Binds to short RNAs such as microRNAs (miRNAs) and represses the translation of mRNAs which are complementary to them. Lacks endonuclease activity and does not appear to cleave target mRNAs. Also required for RNA-directed transcription and replication of the human hapatitis delta virus (HDV).

**Summary**, from NCBI Gene [192670](https://www.ncbi.nlm.nih.gov/gene/192670):

> This gene encodes a member of the Argonaute family of proteins which contain PAZ and PIWI domains and play an integral role in RNA interference and short-interfering-RNA-mediated gene silencing. This gene is located on chromosome 1 in a cluster of related family members. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:18424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18424) · Entrez [192670](https://www.ncbi.nlm.nih.gov/gene/192670) · UniProt [Q9HCK5](https://www.uniprot.org/uniprotkb/Q9HCK5) · Ensembl [ENSG00000134698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134698)

## Data

Gene col 5591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5591); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5591]; `tensor/DDL_lfc|DDL_z.npy` [5591]; `embed/gene_vectors.npy` [5591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5591 or target_col == 5591). Every well: [[AGO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

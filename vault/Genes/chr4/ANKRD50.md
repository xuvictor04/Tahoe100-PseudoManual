---
symbol: "ANKRD50"
type: "gene"
col: 7520
ensembl_id: "ENSG00000151458"
name: "ankyrin repeat domain 50"
location: "4q28.1"
module: 40
arm: "-"
pooled_cpm: 55.98
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ANKRD50

*ankyrin repeat domain 50* — 4q28.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +20.1, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.610× (z -8.8, q 7e-16, down in 35 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 5 µM: 0.816× (z -3.5, q 0.067, down in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (CHP-212 0.0938×, PANC-1 0.389×, hTERT-HPNE 0.280×, A498 0.401×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.170×, SNU-423 0.101×, RPMI-7951 0.229×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (CHP-212 0.0765×, HepG2/C3A 0.139×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW48 0.0836×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PER3]] (+0.55, fdr 1e-05), [[ATF7IP]] (+0.55, fdr 1e-05), [[UBQLN2]] (+0.50, fdr 3e-05); moves opposite to [[NOP58]] (-0.54, fdr 5e-05), [[ISY1]] (-0.52, fdr 2e-05), [[THOC3]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DNAJB5]] → it (grade C ⚠); 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +20.1 | 0e+00 | 42/47 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +12.8 | 9e-35 | 44/47 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +12.6 | 7e-34 | 46/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.82×** | +10.6 | 3e-24 | 46/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +9.0 | 2e-17 | 38/47 (LS 180, SW1417, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +8.5 | 2e-15 | 41/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.6 | 2e-12 | 38/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.8 | 1e-09 | 28/47 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +6.6 | 2e-09 | 28/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 3e-09 | 32/47 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 4e-07 | 31/47 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.7 | 4e-07 | 29/47 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +5.6 | 7e-07 | 28/47 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.4 | 3e-06 | 28/47 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 2e-05 | 24/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +4.6 | 1e-04 | 25/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.008 | 19/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7520.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (CHP-212 0.0938×, PANC-1 0.389×, hTERT-HPNE 0.280×, A498 0.401×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.170×, SNU-423 0.101×, RPMI-7951 0.229×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (CHP-212 0.0765×, HepG2/C3A 0.139×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW48 0.0836×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.610×** | -8.8 | 7e-16 | 35/48 (CHP-212, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -8.1 | 2e-13 | 31/43 (CHP-212, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.664×** | -6.8 | 3e-09 | 27/45 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.816×** | -3.5 | 0.067 | 13/47 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.781× | -3.0 | 0.26 | 16/47 (NCI-H23, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 155 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +18.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 102 | 4 | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.29× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 64.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +17.4) | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -19.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 81.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 54.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +11.9) | — |
| [[C32 (line)]] | wt | 61.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +17.2) | — |
| [[PANC-1 (line)]] | alt | 59.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 79.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 54.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +21.6) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 29.2 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.38× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 44.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -18.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 20.8 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 44.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -9.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 47.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0765× (z -14.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 89.5 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 62.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.6) | — |
| [[hTERT-HPNE (line)]] | wt | 88.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 36.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 43.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -9.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 75.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 62.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.9) | — |
| [[SNU-1 (line)]] | wt | 45.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 42.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +13.6) | — |
| [[SW1417 (line)]] | alt | 26.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.7) | — |
| [[A-172 (line)]] | wt | 95.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.0) | — |
| [[A549 (line)]] | wt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 58.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0884× (z -11.3) ⚠ toxic |
| [[LS 180 (line)]] | wt | 35.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.18× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 63.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -10.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 31.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0836× (z -13.0) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PER3]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ATF7IP]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[UBQLN2]] | +0.50 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[MARCKS]] | +0.50 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[ZNF260]] | +0.50 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[TUBB2A]] | +0.49 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[PCDH18]] | +0.49 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ZNF134]] | +0.49 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[VEZF1]] | +0.49 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[HEXB]] | +0.48 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[TFE3]] | +0.48 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TEF]] | +0.48 | +0.40 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP58]] | -0.54 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[ISY1]] | -0.52 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[THOC3]] | -0.52 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[PARN]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TFB2M]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[EIF3B]] | -0.50 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[DDX49]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ARIH2]] | -0.47 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[CWF19L1]] | -0.47 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[CRLS1]] | -0.46 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[FAM156A]] | -0.46 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[TRMT44]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJB5]] | C | DNAJB5 activity raises ANKRD50's level | lines that do not express DNAJB5 (3) vs lines expressing it (47) | 2.70× lower at baseline in the lines without DNAJB5 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: CEP170, SRGAP2C, TLCD5; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | ANKRD50's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | ANKRD50's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.421 over the table, 0.071 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.373). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-12.4, 2.6); signed map (13.7, -32.8). **Vector** length 89.9, 22.1% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +12.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +5.5 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.8 | +12.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +3.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.5 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | +0.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 50 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.1 — chr4:124,664,048-124,712,732 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1223 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULJ7](https://www.uniprot.org/uniprotkb/Q9ULJ7) (Ankyrin repeat domain-containing protein 50):

> Involved in the endosome-to-plasma membrane trafficking and recycling of SNX27-retromer-dependent cargo proteins, such as GLUT1.

**Summary**, from NCBI Gene [57182](https://www.ncbi.nlm.nih.gov/gene/57182):

> Involved in endocytic recycling. Predicted to be located in endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29223) · Entrez [57182](https://www.ncbi.nlm.nih.gov/gene/57182) · UniProt [Q9ULJ7](https://www.uniprot.org/uniprotkb/Q9ULJ7) · Ensembl [ENSG00000151458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151458)

## Data

Gene col 7520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7520); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7520]; `tensor/DDL_lfc|DDL_z.npy` [7520]; `embed/gene_vectors.npy` [7520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7520 or target_col == 7520). Every well: [[ANKRD50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

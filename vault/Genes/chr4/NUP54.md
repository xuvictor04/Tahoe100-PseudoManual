---
symbol: "NUP54"
type: "gene"
col: 6224
ensembl_id: "ENSG00000138750"
name: "nucleoporin 54"
location: "4q21.1"
module: 65
arm: "+"
pooled_cpm: 99.97
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# NUP54

*nucleoporin 54* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.85× (z +9.9, q 3e-20, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.476× (z -12.9, q 4e-35, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.813× (z -3.6, q 0.038, down in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (HCT15 0.134×, NCI-H2347 0.233×, NCI-H1573 0.179×, CHP-212 0.0625×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.278×, RPMI-7951 0.222×, SW 900 0.236×, SK-MEL-2 0.321×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.350×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED17]] (+0.78, fdr 7e-06), [[NDUFAF7]] (+0.73, fdr 7e-06), [[KLHDC10]] (+0.72, fdr 7e-06); moves opposite to [[TFE3]] (-0.63, fdr 1e-05), [[THOC6]] (-0.62, fdr 1e-05), [[PEPD]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.85×** | +9.9 | 3e-20 | 46/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.66×** | +9.2 | 1e-17 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +9.1 | 2e-17 | 44/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +9.1 | 2e-17 | 37/49 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.62×** | +8.7 | 5e-16 | 34/48 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +7.4 | 1e-11 | 38/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.48×** | +7.1 | 1e-10 | 41/48 (LS 180, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.43×** | +6.5 | 6e-09 | 31/48 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.44×** | +6.3 | 2e-08 | 31/50 (SW480, A-427, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +5.7 | 9e-07 | 32/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.36×** | +5.5 | 2e-06 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.37×** | +5.5 | 2e-06 | 30/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.3 | 4e-06 | 33/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.36×** | +5.3 | 4e-06 | 30/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.21×** | +4.9 | 3e-05 | 22/48 (PANC-1, RKO, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 4e-04 | 27/48 (SW480, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.003 | 27/49 (PANC-1, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.023 | 8/49 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.072 | 12/48 (RKO, LoVo, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.19× | +2.8 | 0.089 | 16/49 (A498, HOP62, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +2.8 | 0.091 | 11/48 (CHP-212, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6224.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (HCT15 0.134×, NCI-H2347 0.233×, NCI-H1573 0.179×, CHP-212 0.0625×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.278×, RPMI-7951 0.222×, SW 900 0.236×, SK-MEL-2 0.321×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.350×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -12.9 | 4e-35 | 43/44 (HCT15, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.515×** | -10.8 | 9e-25 | 44/49 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.670×** | -6.7 | 5e-09 | 31/45 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -6.6 | 8e-09 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.038 | 19/47 (HOP62, H4, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.041 | 18/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 111 | 8 (5 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.68× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.71× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.534× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 79.1 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.80× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 100 | 4 (4 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.29× (z +10.1) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 95.6 | 2 (2 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.03× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.179× (z -16.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 67.1 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.3) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[BT-474 (line)]] | alt | 141 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 2.36× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 128 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.29× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -11.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 85.3 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.18× (z +10.1) | — |
| [[LoVo (line)]] | wt | 104 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.33× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.88× (z +8.8) | — |
| [[SW48 (line)]] | wt | 125 | 3 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.24× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 123 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +12.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.202× (z -14.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 99.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 174 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -19.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 120 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.8) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.60× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 72.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.40× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 92.8 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.28× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RPMI-7951 (line)]] | alt | 98.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -12.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -14.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 93.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -10.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -11.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 85.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.8) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[C-33 A (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -15.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 93.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -9.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0625× (z -16.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 82.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.34× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -21.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 86.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -10.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 70.3 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.40× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 95.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -11.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 112 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 134 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED17]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ASB7]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SNRPA1]] | +0.68 | +0.73 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TENT2]] | +0.67 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[ALG9]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[MED23]] | +0.66 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[USPL1]] | +0.66 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[COPS4]] | +0.65 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TFG]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[CRLS1]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFE3]] | -0.63 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[THOC6]] | -0.62 | -0.57 / -0.58 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 421 |
| [[PEPD]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.60 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[CELSR3]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.59 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[JUN]] | -0.59 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[PEA15]] | -0.59 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[DYNLL2]] | -0.58 | -0.56 / -0.43 | both halves | 3e-05 | pathway: HCMV Early Events; STRING 487 |
| [[LINC00641]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[KDM6B]] | -0.57 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[SKIL]] | -0.57 | -0.63 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.6, -13.4); signed map (-34.7, -8.8). **Vector** length 98.2, 32.5% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.8 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.2 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | +4.3 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | -1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | -0.6 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.1 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | +0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -4.9 | +4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.7 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -1.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:76,107,562-76,148,485 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Nucleoporins |
| Reactome | 73 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3B4](https://www.uniprot.org/uniprotkb/Q7Z3B4) (Nucleoporin p54):

> Component of the nuclear pore complex, a complex required for the trafficking across the nuclear membrane.

**Summary**, from NCBI Gene [53371](https://www.ncbi.nlm.nih.gov/gene/53371):

> The nuclear envelope creates distinct nuclear and cytoplasmic compartments in eukaryotic cells. It consists of two concentric membranes perforated by nuclear pores, large protein complexes that form aqueous channels to regulate the flow of macromolecules between the nucleus and the cytoplasm. These complexes are composed of at least 100 different polypeptide subunits, many of which belong to the nucleoporin family. This gene encodes a member of the phe-gly (FG) repeat-containing nucleoporin …

**Accessions** — [HGNC:17359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17359) · Entrez [53371](https://www.ncbi.nlm.nih.gov/gene/53371) · UniProt [Q7Z3B4](https://www.uniprot.org/uniprotkb/Q7Z3B4) · Ensembl [ENSG00000138750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138750)

## Data

Gene col 6224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6224); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6224]; `tensor/DDL_lfc|DDL_z.npy` [6224]; `embed/gene_vectors.npy` [6224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6224 or target_col == 6224). Every well: [[NUP54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

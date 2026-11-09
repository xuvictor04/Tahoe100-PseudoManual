---
symbol: "MED4"
type: "gene"
col: 5820
ensembl_id: "ENSG00000136146"
name: "mediator complex subunit 4"
location: "13q14.2"
module: 118
arm: "+"
pooled_cpm: 86.0
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# MED4

*mediator complex subunit 4* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.64× (z +14.5, q 4e-45, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.657× (z -11.9, q 7e-30, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 11 lines (SW 900 0.261×, J82 0.379×, SK-MEL-2 0.232×, C32 0.382×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.104×, HEC-1-A 0.516×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (C32 0.214×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC30]] (+0.66, fdr 8e-06), [[NDUFS3]] (+0.65, fdr 1e-05), [[APPBP2]] (+0.64, fdr 1e-05); moves opposite to [[CSRP1]] (-0.55, fdr 3e-04), [[ZFP36]] (-0.52, fdr 3e-05), [[R3HDM4]] (-0.52, fdr 7e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APOC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +14.5 | 4e-45 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +14.0 | 6e-42 | 44/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.34×** | +12.3 | 2e-32 | 35/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +9.9 | 4e-21 | 37/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.40×** | +9.9 | 7e-21 | 38/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +9.5 | 2e-19 | 38/48 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +9.1 | 1e-17 | 34/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.19× | +7.4 | 1e-11 | 19/49 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +7.2 | 3e-11 | 29/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +7.1 | 5e-11 | 28/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +7.0 | 1e-10 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +6.2 | 2e-08 | 30/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.17× | +4.7 | 1e-04 | 20/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.16× | +4.2 | 9e-04 | 20/48 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.16× | +4.2 | 0.001 | 18/50 (NCI-H460, A-427, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.11× | +4.2 | 0.001 | 6/48 (HT-29, AsPC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.003 | 13/49 (PANC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.034 | 14/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5820.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 11 lines (SW 900 0.261×, J82 0.379×, SK-MEL-2 0.232×, C32 0.382×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.104×, HEC-1-A 0.516×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (C32 0.214×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.657×** | -11.9 | 7e-30 | 31/44 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.780×** | -7.3 | 6e-11 | 30/49 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -6.4 | 2e-08 | 14/48 (LS 180, A-172, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -5.3 | 2e-05 | 0/50 | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.855× | -4.6 | 4e-04 | 11/49 (KATO III, SNU-423, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.865× | -4.3 | 0.002 | 18/48 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.859× | -4.2 | 0.003 | 22/45 (SNU-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.881× | -3.8 | 0.012 | 10/47 (SNU-423, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.888× | -3.5 | 0.029 | 15/49 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.896× | -3.3 | 0.062 | 4/48 (LoVo, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.2 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +16.2) | — |
| [[SW480 (line)]] | alt | 113 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.597× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 205 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +12.1) | — |
| [[KATO III (line)]] | alt | 123 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +15.8) | — |
| [[LoVo (line)]] | wt | 97.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.510× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 120 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.72× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 60.7 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +13.8) | — |
| [[BT-474 (line)]] | alt | 77.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.27× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.3) | — |
| [[C32 (line)]] | wt | 87.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 103 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +14.7) | — |
| [[NCI-H23 (line)]] | alt | 82.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.3) ⚠ cell-cycle shift, explains ~23% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -29.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 120 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.97× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.505× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 69.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +8.6) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[A498 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.525× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 74.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.7) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[HCT15 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.4) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[HEC-1-A (line)]] | alt | 89.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.516× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 68.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.7) | — |
| [[J82 (line)]] | alt | 93.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -13.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 84.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.6) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 71.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -14.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 81.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.466× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 112 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC30]] | +0.66 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[NDUFS3]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[APPBP2]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CNPY2]] | +0.64 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[ISY1]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[C2orf42]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ALG11]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ZNF248]] | +0.60 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[CWC15]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 | STRING 643 |
| [[WDR83OS]] ⚠ | +0.58 | +0.49 / +0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TAF3]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 | STRING 803 |
| [[ZNF148]] | +0.57 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[TMEM101]] | +0.57 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP1]] | -0.55 | -0.28 / -0.61 | both halves | 3e-04 |  |
| [[ZFP36]] | -0.52 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[R3HDM4]] | -0.52 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[RSC1A1]] | -0.51 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[HUS1]] | -0.51 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[ATP1A3]] | -0.50 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[ITPR3]] | -0.50 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CORO1C]] | -0.49 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[ZMIZ2]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PXN]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PEA15]] | -0.48 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[ACSL4]] | -0.48 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOC1]] | B | APOC1 activity lowers MED4's level | lines that do not express APOC1 (17) vs lines expressing it (33) | 1.19× higher at baseline in the lines without APOC1 | 0.090 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, MAP3K15 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-52.6, 4.4); signed map (-5.2, -3.5). **Vector** length 74.7, 15.3% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +3.9 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.8 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | +3.3 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.8 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | -0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | -1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.0 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.7 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -11.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | +1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:48,053,323-48,095,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC126, DRIP36, TRAP36; previously VDRIP |
| Gene groups (HGNC) | Mediator complex; Centriolar satellite proteins |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPJ6](https://www.uniprot.org/uniprotkb/Q9NPJ6) (Mediator of RNA polymerase II transcription subunit 4):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [29079](https://www.ncbi.nlm.nih.gov/gene/29079):

> This gene encodes a component of the Mediator complex. The Mediator complex interacts with DNA-binding gene-specific transcription factors to modulate transcription by RNA polymerase II. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:17903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17903) · Entrez [29079](https://www.ncbi.nlm.nih.gov/gene/29079) · UniProt [Q9NPJ6](https://www.uniprot.org/uniprotkb/Q9NPJ6) · Ensembl [ENSG00000136146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136146)

## Data

Gene col 5820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5820); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5820]; `tensor/DDL_lfc|DDL_z.npy` [5820]; `embed/gene_vectors.npy` [5820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5820 or target_col == 5820). Every well: [[MED4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

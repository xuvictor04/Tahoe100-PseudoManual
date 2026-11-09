---
symbol: "CAB39"
type: "gene"
col: 5784
ensembl_id: "ENSG00000135932"
name: "calcium binding protein 39"
location: "2q37.1"
module: 160
arm: "+"
pooled_cpm: 166.13
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# CAB39

*calcium binding protein 39* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.07× (z +9.4, q 2e-18, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Abemaciclib (drug)]] 5 µM: 0.675× (z -5.0, q 3e-04, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 0.321×, A549 0.366×, NCI-H23 0.385×, AsPC-1 0.423×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.389×, NCI-H1573 0.444×, A549 0.481×, BT-474 0.386×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (AsPC-1 0.418×, SW 900 0.355×); [[Arbutin (drug)]] 0.05 µM in 1 line (SW 1088 0.0645×); [[Belinostat (drug)]] 5 µM in 1 line (AsPC-1 0.458×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LUZP1]] (+0.57, fdr 1e-05), [[SMURF1]] (+0.56, fdr 4e-05), [[HIGD1A]] (+0.55, fdr 2e-05); moves opposite to [[TBC1D32]] (-0.48, fdr 7e-05), [[UQCRC2]] (-0.46, fdr 4e-05), [[ANK2]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MET]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +9.4 | 2e-18 | 38/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.07×** | +9.4 | 2e-18 | 41/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.8 | 1e-12 | 30/48 (HS-578T, RKO, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +6.2 | 9e-08 | 26/48 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +6.1 | 1e-07 | 31/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.7 | 1e-06 | 27/48 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +5.3 | 1e-05 | 26/48 (HCT15, SHP-77, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.2 | 2e-05 | 24/38 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +4.9 | 6e-05 | 22/48 (AsPC-1, HS-578T, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.22×** | +4.8 | 1e-04 | 24/47 (NCI-H2030, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +4.6 | 2e-04 | 24/48 (LoVo, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.20× | +4.4 | 5e-04 | 22/47 (SW480, BT-474, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +4.3 | 9e-04 | 19/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | 1.19× | +4.1 | 0.002 | 22/47 (C-33 A, HCT15, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.17× | +3.9 | 0.004 | 20/48 (HepG2/C3A, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.006 | 17/47 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.015 | 16/47 (NCI-H2030, SW480, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.015 | 16/48 (HT-29, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5784.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 0.321×, A549 0.366×, NCI-H23 0.385×, AsPC-1 0.423×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (Panc 03.27 0.389×, NCI-H1573 0.444×, A549 0.481×, BT-474 0.386×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (AsPC-1 0.418×, SW 900 0.355×); [[Arbutin (drug)]] 0.05 µM in 1 line (SW 1088 0.0645×); [[Belinostat (drug)]] 5 µM in 1 line (AsPC-1 0.458×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abemaciclib (drug)]] 5 µM |  | **0.675×** | -5.0 | 3e-04 | 24/48 (PANC-1, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.825×** | -4.7 | 7e-04 | 24/48 (COLO 205, HEC-1-A, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 0.841× | -4.2 | 0.004 | 24/48 (AsPC-1, SW 900, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.899× | -3.7 | 0.034 | 5/49 (H4, SNU-423, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.849× | -3.6 | 0.034 | 11/49 (A549, HEC-1-A, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.851× | -3.5 | 0.037 | 17/48 (BT-474, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.869× | -3.4 | 0.042 | 17/48 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.906× | -3.4 | 0.042 | 15/48 (NCI-H2347, NCI-H1573, …) | all doses, flat | low cells (technical?) |
| [[Aliskiren (drug)]] 0.5 µM |  | 0.870× | -3.4 | 0.042 | 11/49 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.869× | -3.3 | 0.056 | 13/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.915× | -3.1 | 0.12 | 1/48 (H4) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.884× | -3.0 | 0.12 | 16/49 (Panc 03.27, NCI-H1573, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 523 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.418× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 260 | 5 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.37× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.01× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 202 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.98× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 89.3 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +13.6) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.71× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 126 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 110 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 2.18× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 291 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 73.2 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.1) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[A549 (line)]] | wt | 163 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 233 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.0) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 91.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HT-29 (line)]] | alt | 207 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.36× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 273 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 112 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.5) ⚠ cell-cycle shift, explains ~49% of this change | [[Dinaciclib (drug)]] 5 µM 0.385× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 178 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.480× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 220 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 341 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.355× (z -10.1) |
| [[SW480 (line)]] | alt | 141 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.51× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 217 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -10.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[RKO (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW 1088 (line)]] | alt | 165 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.0645× (z -10.8) |
| [[A-172 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 150 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 155 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 127 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUZP1]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SMURF1]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[HIGD1A]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SNRK]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 | STRING 821 |
| [[CD59]] | +0.50 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[FAM118B]] | +0.49 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[NTN4]] | +0.48 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[IL4R]] | +0.48 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PDLIM5]] | +0.48 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[SH3RF1]] | +0.47 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[BCAR3]] | +0.47 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[RESF1]] | +0.46 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D32]] | -0.48 | -0.38 / -0.49 | both halves | 7e-05 | same gene group |
| [[UQCRC2]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ANK2]] | -0.45 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[FOXO3B]] | -0.44 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[SLC16A1]] | -0.43 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[HSPA9]] | -0.42 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[TRA2A]] | -0.42 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[SUCO]] | -0.42 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[FAM53C]] | -0.42 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[TMEM263]] | -0.42 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[TUBE1]] | -0.41 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[PREPL]] | -0.41 | -0.34 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MET]] | B | MET activity raises CAB39's level | lines that do not express MET (9) vs lines expressing it (41) | 1.78× lower at baseline in the lines without MET | 0.004 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[SMAD3]] | B | SMAD3 activity raises CAB39's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without SMAD3 | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity lowers CAB39's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.60× higher at baseline in the lines without ANK2 | 0.035 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[CD59]] | B | CD59 activity raises CAB39's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.52× lower at baseline in the lines without CD59 | 0.036 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[PMEPA1]] | B | PMEPA1 activity raises CAB39's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without PMEPA1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[RAB27B]] | B | RAB27B activity raises CAB39's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without RAB27B | 0.049 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[NTN4]] | B | NTN4 activity raises CAB39's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.37× lower at baseline in the lines without NTN4 | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[LAMC2]] | B | LAMC2 activity raises CAB39's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.54× lower at baseline in the lines without LAMC2 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[DDX3Y]] | B | DDX3Y activity lowers CAB39's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.35× higher at baseline in the lines without DDX3Y | 0.071 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[EGFR]] | B | EGFR activity raises CAB39's level | lines that do not express EGFR (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without EGFR | 0.091 | ⚠ within organs, on part of the lines; also absent: C1RL-AS1, PSD4, RNASEL |
| [[NRP1]] | B | NRP1 activity raises CAB39's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without NRP1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.374). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (35.7, 5.5); signed map (-3.9, 36.9). **Vector** length 119, 32.7% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +9.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | +3.6 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.6 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +3.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +2.9 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.9 | -3.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | -4.3 | -3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.2 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Afatinib (drug)]] 5 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | calcium binding protein 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:230,712,842-230,821,075 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-66, MO25 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 4 pathways, smallest: Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y376](https://www.uniprot.org/uniprotkb/Q9Y376) (Calcium-binding protein 39):

> Component of a complex that binds and activates STK11/LKB1. In the complex, required to stabilize the interaction between CAB39/MO25 (CAB39/MO25alpha or CAB39L/MO25beta) and STK11/LKB1.

**Summary**, from NCBI Gene [51719](https://www.ncbi.nlm.nih.gov/gene/51719):

> Enables protein serine/threonine kinase activator activity and protein serine/threonine kinase binding activity. Involved in cellular hypotonic response; intracellular signal transduction; and negative regulation of potassium ion transmembrane transport. Located in cytoplasm. Part of serine/threonine protein kinase complex. Implicated in hepatocellular carcinoma. Biomarker of hepatocellular carcinoma and pancreatic cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20292) · Entrez [51719](https://www.ncbi.nlm.nih.gov/gene/51719) · UniProt [Q9Y376](https://www.uniprot.org/uniprotkb/Q9Y376) · Ensembl [ENSG00000135932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135932)

## Data

Gene col 5784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5784); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5784]; `tensor/DDL_lfc|DDL_z.npy` [5784]; `embed/gene_vectors.npy` [5784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5784 or target_col == 5784). Every well: [[CAB39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAB39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

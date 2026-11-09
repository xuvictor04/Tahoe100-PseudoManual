---
symbol: "BCCIP"
type: "gene"
col: 2901
ensembl_id: "ENSG00000107949"
name: "BRCA2 and CDKN1A interacting protein"
location: "10q26.2"
module: 4
arm: "+"
pooled_cpm: 59.35
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# BCCIP

*BRCA2 and CDKN1A interacting protein* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +11.9, q 8e-30, up in 40 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.03× (z +10.5, q 1e-23, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.365×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.490×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSR1]] (+0.75, fdr 7e-06), [[LSG1]] (+0.74, fdr 7e-06), [[POLR1A]] (+0.73, fdr 7e-06); moves opposite to [[TXNDC16]] (-0.59, fdr 3e-05), [[LNX2]] (-0.58, fdr 1e-05), [[SMIM14]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.55×** | +11.9 | 8e-30 | 40/48 (A498, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.27×** | +11.2 | 8e-27 | 41/45 (SNU-423, A498, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +10.5 | 1e-23 | 46/48 (SW480, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.07×** | +10.4 | 5e-23 | 40/44 (NCI-H1792, A498, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +9.5 | 2e-19 | 42/47 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +9.1 | 9e-18 | 39/48 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +7.7 | 1e-12 | 37/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +7.5 | 4e-12 | 42/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +7.4 | 1e-11 | 43/49 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.63×** | +7.2 | 3e-11 | 39/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.62×** | +7.1 | 5e-11 | 38/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.57×** | +6.7 | 1e-09 | 39/48 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.18×** | +6.0 | 7e-08 | 31/48 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.48×** | +5.8 | 3e-07 | 30/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 3e-07 | 28/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +5.0 | 1e-05 | 33/48 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.84×** | +4.7 | 7e-05 | 36/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.79×** | +4.5 | 1e-04 | 30/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.1 | 7e-04 | 30/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.002 | 23/48 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.002 | 27/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.002 | 25/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.007 | 24/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.017 | 23/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2901.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.365×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.490×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.774× | -3.4 | 0.34 | 18/50 (LoVo, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.807× | -3.1 | 0.52 | 21/47 (SW480, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 43.2 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.68× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +9.5) | — |
| [[SW480 (line)]] | alt | 71.0 | 5 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.78× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 41.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.40× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 64.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[PANC-1 (line)]] | alt | 103 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +12.2) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[A498 (line)]] | wt | 62.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[KATO III (line)]] | alt | 47.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.09× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 53.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H1573 (line)]] | alt | 57.4 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +11.2) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[SNU-423 (line)]] | alt | 54.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[A549 (line)]] | wt | 54.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[COLO 205 (line)]] | alt | 47.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.21× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 44.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H2347 (line)]] | alt | 47.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[CFPAC-1 (line)]] | alt | 50.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.79× (z +8.7) ⚠ toxic | — |
| [[HOP62 (line)]] | alt | 31.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[HS-578T (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[J82 (line)]] | alt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[LoVo (line)]] | wt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[LOX-IMVI (line)]] | wt | 67.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[Panc 03.27 (line)]] | alt | 49.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[SW 900 (line)]] | alt | 60.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 108 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSR1]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[LSG1]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[HEATR1]] | +0.73 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[PUM3]] | +0.71 | +0.65 / +0.75 | both halves | 7e-06 | STRING 637 |
| [[GTPBP4]] | +0.70 | +0.66 / +0.75 | both halves | 7e-06 | STRING 421 |
| [[NOL10]] | +0.69 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[TWNK]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[NAA25]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.68 | +0.71 / +0.68 | both halves | 7e-06 | STRING 774 |
| [[CDC123]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[DFFA]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | -0.59 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[LNX2]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.55 | -0.46 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.4, -35.6); signed map (-3.8, -47.6). **Vector** length 71.5, 20.0% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +10.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +9.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | +1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -2.8 | +4.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | -1.8 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~83% of this change | -1.6 | +3.8 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | BRCA2 and CDKN1A interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:125,823,546-125,853,695 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCCIPalpha, TOK-1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P287](https://www.uniprot.org/uniprotkb/Q9P287) (BRCA2 and CDKN1A-interacting protein):

> During interphase, required for microtubule organizing and anchoring activities. During mitosis, required for the organization and stabilization of the spindle pole. Isoform 2/alpha is particularly important for the regulation of microtubule anchoring, microtubule stability, spindle architecture and spindle orientation, compared to isoform 1/beta. May promote cell cycle arrest by enhancing the inhibition of CDK2 activity by CDKN1A. May be required for repair of DNA damage by homologous …

**Summary**, from NCBI Gene [56647](https://www.ncbi.nlm.nih.gov/gene/56647):

> This gene product was isolated on the basis of its interaction with BRCA2 and p21 proteins. It is an evolutionarily conserved nuclear protein with multiple interacting domains. The N-terminal half shares moderate homology with regions of calmodulin and M-calpain, suggesting that it may also bind calcium. Functional studies indicate that this protein may be an important cofactor for BRCA2 in tumor suppression, and a modulator of CDK2 kinase activity via p21. This protein has also been implicated …

**Accessions** — [HGNC:978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:978) · Entrez [56647](https://www.ncbi.nlm.nih.gov/gene/56647) · UniProt [Q9P287](https://www.uniprot.org/uniprotkb/Q9P287) · Ensembl [ENSG00000107949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107949)

## Data

Gene col 2901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2901); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2901]; `tensor/DDL_lfc|DDL_z.npy` [2901]; `embed/gene_vectors.npy` [2901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2901 or target_col == 2901). Every well: [[BCCIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCCIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

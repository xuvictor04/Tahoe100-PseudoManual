---
symbol: "GOT2"
type: "gene"
col: 4592
ensembl_id: "ENSG00000125166"
name: "glutamic-oxaloacetic transaminase 2"
location: "16q21"
module: 4
arm: "+"
pooled_cpm: 34.71
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GOT2

*glutamic-oxaloacetic transaminase 2* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.40× (z +17.3, q 0e+00, up in 43 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.77× (z +8.0, q 1e-13, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.180×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.382×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPE]] (+0.75, fdr 7e-06), [[PRPS1]] (+0.74, fdr 7e-06), [[PHB1]] (+0.74, fdr 7e-06); moves opposite to [[OFD1]] (-0.69, fdr 7e-06), [[TERF2IP]] (-0.68, fdr 7e-06), [[INAFM1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.40×** | +17.3 | 0e+00 | 43/45 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.36×** | +16.5 | 0e+00 | 38/38 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.30×** | +10.8 | 4e-25 | 38/44 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.88×** | +8.9 | 1e-16 | 41/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +8.0 | 1e-13 | 38/48 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +8.0 | 1e-13 | 41/47 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.74×** | +7.8 | 5e-13 | 38/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.72×** | +7.6 | 2e-12 | 39/48 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.74×** | +7.5 | 4e-12 | 38/46 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +7.4 | 6e-12 | 41/46 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +7.0 | 1e-10 | 37/47 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.62×** | +6.5 | 3e-09 | 31/48 (NCI-H1792, A549, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +5.9 | 2e-07 | 32/48 (A498, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.6 | 9e-07 | 2/48 (Hs 766T, HCT15) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +5.5 | 1e-06 | 31/48 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.0 | 2e-05 | 23/47 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 3e-04 | 24/48 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.002 | 22/45 (A498, NCI-H1573, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +3.9 | 0.003 | 20/45 (LS 180, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.005 | 21/44 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.64×** | +3.6 | 0.005 | 14/45 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.009 | 14/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.011 | 17/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.016 | 18/47 (NCI-H1792, A549, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4592.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.180×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.382×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.640× | -3.3 | 0.38 | 14/48 (LoVo, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.779× | -3.2 | 0.38 | 17/45 (C32, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.788× | -3.0 | 0.38 | 10/48 (SW480, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 41.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 58.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SNU-423 (line)]] | alt | 19.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.21× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A498 (line)]] | wt | 31.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A549 (line)]] | wt | 38.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HOP62 (line)]] | alt | 25.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[Hs 766T (line)]] | wt | 31.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.86× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 24.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LoVo (line)]] | wt | 33.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LS 180 (line)]] | wt | 44.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1792 (line)]] | alt | 19.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.01× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[PANC-1 (line)]] | alt | 19.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SHP-77 (line)]] | alt | 62.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 60.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-427 (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LOX-IMVI (line)]] | wt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H23 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 71.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPE]] | +0.75 | +0.71 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[PRPS1]] | +0.74 | +0.69 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[PHB1]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PPP5C]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[C1QBP]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[HEATR3]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[DLAT]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 480 |
| [[ELAC2]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[COPS6]] | +0.70 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[MRPL19]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OFD1]] | -0.69 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.68 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.67 | -0.68 / -0.71 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.66 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.63 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[TESK2]] | -0.63 | -0.63 / -0.58 | both halves | 8e-06 |  |
| [[EIF1]] | -0.63 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[TMEM106A]] | -0.63 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.63 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GCC2]] | -0.63 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[CATSPERG]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.62 | -0.52 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.3, -34.3); signed map (-15.8, -45.2). **Vector** length 87.5, 23.1% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.54 to 8); *tRNA processing* (reactome, mean cos +0.51 to 10); *Folding of actin by CCT/TriC* (reactome, mean cos +0.59 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +4.7 | +17.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.7 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +4.5 | +10.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +7.0 |
|  | [[Lopinavir (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +2.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | glutamic-oxaloacetic transaminase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,707,131-58,734,342 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mitAAT, KATIV, KAT4, KYAT4, mAspAT |
| Gene groups (HGNC) | Glutamic-oxaloacetic transaminase family |
| Hallmark sets | GLYCOLYSIS, MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Aspartate and asparagine metabolism; Malate-aspartate shuttle; Glyoxylate metabolism and glycine degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P00505](https://www.uniprot.org/uniprotkb/P00505) (Aspartate aminotransferase, mitochondrial):

> Catalyzes the irreversible transamination of the L-tryptophan metabolite L-kynurenine to form kynurenic acid (KA). As a member of the malate-aspartate shuttle, it has a key role in the intracellular NAD(H) redox balance. Is important for metabolite exchange between mitochondria and cytosol, and for amino acid metabolism. Facilitates cellular uptake of long-chain free fatty acids.

**Summary**, from NCBI Gene [2806](https://www.ncbi.nlm.nih.gov/gene/2806):

> Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and inner-membrane mitochondrial forms, GOT1 and GOT2, respectively. GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2013]

**Accessions** — [HGNC:4433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4433) · Entrez [2806](https://www.ncbi.nlm.nih.gov/gene/2806) · UniProt [P00505](https://www.uniprot.org/uniprotkb/P00505) · Ensembl [ENSG00000125166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125166)

## Data

Gene col 4592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4592); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4592]; `tensor/DDL_lfc|DDL_z.npy` [4592]; `embed/gene_vectors.npy` [4592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4592 or target_col == 4592). Every well: [[GOT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

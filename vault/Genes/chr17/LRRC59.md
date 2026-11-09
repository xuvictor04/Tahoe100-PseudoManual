---
symbol: "LRRC59"
type: "gene"
col: 3001
ensembl_id: "ENSG00000108829"
name: "leucine rich repeat containing 59"
location: "17q21.33"
module: 52
arm: "+"
pooled_cpm: 73.94
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# LRRC59

*leucine rich repeat containing 59* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (17 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.31× (z +12.5, q 8e-33, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.821× (z -4.2, q 0.010, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~65% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.773× (z -3.9, q 0.021, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA3]] (+0.74, fdr 7e-06), [[GCN1]] (+0.73, fdr 7e-06), [[TMEM214]] (+0.70, fdr 7e-06); moves opposite to [[SPPL3]] (-0.67, fdr 1e-05), [[RAB9A]] (-0.60, fdr 2e-05), [[LAMTOR4]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +12.5 | 8e-33 | 47/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.21×** | +11.8 | 1e-29 | 44/49 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.12×** | +11.2 | 1e-26 | 47/48 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.07×** | +10.4 | 4e-23 | 38/42 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +7.9 | 2e-13 | 45/49 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.76×** | +7.9 | 2e-13 | 39/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.8 | 1e-09 | 37/48 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.59×** | +6.4 | 1e-08 | 31/45 (SNU-423, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.56×** | +6.3 | 1e-08 | 37/47 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.18×** | +6.1 | 8e-08 | 41/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.9 | 2e-07 | 34/48 (NCI-H1573, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.2 | 7e-06 | 35/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.44×** | +5.1 | 2e-05 | 30/48 (LOX-IMVI, HOP62, …) | two highest doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.91×** | +5.0 | 2e-05 | 37/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.90×** | +5.0 | 3e-05 | 38/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.56×** | +4.7 | 1e-04 | 36/48 (KATO III, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.39×** | +4.6 | 1e-04 | 37/48 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 3e-04 | 30/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 1e-03 | 26/48 (PANC-1, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.002 | 23/48 (MIA PaCa-2, LoVo, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +3.8 | 0.003 | 28/48 (HEC-1-A, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3001.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.821×** | -4.2 | 0.010 | 24/48 (LS 180, A498, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.759×** | -4.1 | 0.010 | 28/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.773×** | -3.9 | 0.021 | 28/48 (RKO, NCI-H2030, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.841× | -3.7 | 0.034 | 20/48 (BT-474, Hs 766T, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.787×** | -3.6 | 0.037 | 23/48 (HOP62, KATO III, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.062 | 22/48 (AN3 CA, KATO III, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.062 | 21/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.856× | -3.3 | 0.065 | 11/48 (NCI-H2030, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 59.4 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.1) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 44.9 | 5 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.50× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.52× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 53.7 | 5 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.34× (z +11.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 56.5 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.70× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 41.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.78× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.57× (z +9.9) | — |
| [[SW480 (line)]] | alt | 61.2 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.49× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 75.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.62× (z +9.4) | — |
| [[A-427 (line)]] | wt | 65.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A549 (line)]] | wt | 73.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 63.4 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.39× (z +11.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.53× (z +10.5) | — |
| [[A498 (line)]] | wt | 162 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 55.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.88× (z +8.9) | — |
| [[KATO III (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1573 (line)]] | alt | 47.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.24× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 74.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[BT-474 (line)]] | alt | 228 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.64× (z +10.3) | — |
| [[C32 (line)]] | wt | 39.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.79× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 98.7 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.166× (z -9.4) |
| [[HOP62 (line)]] | alt | 72.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.60× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HS-578T (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 82.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.49× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 72.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.23× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 84.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.42× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 54.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA3]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[GCN1]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[TMEM214]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[ZNF587B]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ZNF587]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SRPRA]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[B4GALT7]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[TBL3]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GMPPB]] | +0.66 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[FTSJ1]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZNF460]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NOL6]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPPL3]] | -0.67 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.60 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[LAMTOR4]] | -0.59 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[MTMR3]] | -0.58 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[PNISR]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[VAMP2]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[WDSUB1]] | -0.55 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.55 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[RNPC3]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ELF2]] | -0.55 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[PIAS1]] | -0.55 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[FBXL20]] | -0.55 | -0.52 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.9, -28.9); signed map (-51.5, 3.9). **Vector** length 114, 38.7% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.7 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.8 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +6.9 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +6.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +5.3 | +6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.1 | +5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.8 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.7 | +5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.1 | +3.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | -5.2 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.4 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | +0.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 59 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,375,059-50,397,523 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRO1855, FLJ21675 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AG4](https://www.uniprot.org/uniprotkb/Q96AG4) (Leucine-rich repeat-containing protein 59):

> Required for nuclear import of FGF1, but not that of FGF2. Might regulate nuclear import of exogenous FGF1 by facilitating interaction with the nuclear import machinery and by transporting cytosolic FGF1 to, and possibly through, the nuclear pores.

**Summary**, from NCBI Gene [55379](https://www.ncbi.nlm.nih.gov/gene/55379):

> Enables RNA binding activity and cadherin binding activity. Predicted to be involved in intracellular signal transduction. Located in endoplasmic reticulum and mitochondrial nucleoid. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28817) · Entrez [55379](https://www.ncbi.nlm.nih.gov/gene/55379) · UniProt [Q96AG4](https://www.uniprot.org/uniprotkb/Q96AG4) · Ensembl [ENSG00000108829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108829)

## Data

Gene col 3001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3001); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3001]; `tensor/DDL_lfc|DDL_z.npy` [3001]; `embed/gene_vectors.npy` [3001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3001 or target_col == 3001). Every well: [[LRRC59 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC59.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

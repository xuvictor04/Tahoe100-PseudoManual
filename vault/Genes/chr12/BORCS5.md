---
symbol: "BORCS5"
type: "gene"
col: 9174
ensembl_id: "ENSG00000165714"
name: "BLOC-1 related complex subunit 5"
location: "12p13.2"
module: 77
arm: "+"
pooled_cpm: 30.78
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# BORCS5

*BLOC-1 related complex subunit 5* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.83× (z +11.0, q 2e-25, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.456× (z -14.4, q 5e-44, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPG2]] (+0.65, fdr 1e-05), [[MTMR12]] (+0.59, fdr 3e-05), [[PEX7]] (+0.57, fdr 1e-05); moves opposite to [[DNAJB4]] (-0.61, fdr 1e-05), [[AKT1S1]] (-0.57, fdr 4e-05), [[CHD3]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +11.0 | 2e-25 | 40/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +9.8 | 4e-20 | 36/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +7.7 | 2e-12 | 33/48 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.2 | 6e-08 | 29/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.6 | 6e-04 | 19/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +4.4 | 0.001 | 15/48 (BT-474, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.005 | 15/47 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +3.9 | 0.007 | 16/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.038 | 12/47 (NCI-H460, LoVo, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.18× | +3.0 | 0.14 | 10/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.456×** | -14.4 | 5e-44 | 42/48 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.608×** | -12.9 | 2e-35 | 36/47 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.547×** | -11.1 | 4e-26 | 33/45 (A-427, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.538×** | -10.9 | 2e-25 | 25/38 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -10.2 | 3e-22 | 32/47 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.576×** | -10.1 | 5e-22 | 34/48 (LoVo, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.581×** | -9.9 | 2e-21 | 32/47 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.575×** | -9.7 | 1e-20 | 37/48 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.613×** | -9.0 | 2e-17 | 31/48 (CHP-212, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.629×** | -8.5 | 1e-15 | 27/47 (SW 900, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.695×** | -6.7 | 1e-09 | 27/47 (A-427, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.699×** | -6.1 | 6e-08 | 21/42 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -5.9 | 2e-07 | 24/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.776×** | -4.4 | 5e-04 | 19/48 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.792×** | -4.3 | 8e-04 | 23/48 (A549, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.825×** | -3.5 | 0.015 | 15/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.738×** | -2.9 | 0.091 | 10/48 (A-172, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.801×** | -2.9 | 0.091 | 9/48 (SHP-77, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 76.3 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0859× (z -27.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 66.1 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -24.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -8.9) |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.249× (z -11.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 44.7 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.416× (z -8.6) |
| [[LoVo (line)]] | wt | 51.8 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.301× (z -12.4) |
| [[A-427 (line)]] | wt | 71.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -20.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 24.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.7) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.338× (z -10.4) |
| [[C32 (line)]] | wt | 33.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -11.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[J82 (line)]] | alt | 18.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.4) |
| [[LS 180 (line)]] | wt | 54.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 41.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 92.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -20.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 35.7 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.162× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 45.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.1) ⚠ cell-cycle shift, explains ~59% of this change |
| [[SW 900 (line)]] | alt | 35.3 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -13.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 19.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 23.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -8.5) |
| [[SW480 (line)]] | alt | 38.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.7) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A498 (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.233× (z -10.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.207× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0427× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.137× (z -8.9) |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.223× (z -8.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.104× (z -9.4) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0520× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.240× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG2]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[MTMR12]] | +0.59 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[PEX7]] | +0.57 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ZFAND4]] | +0.56 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[TAF5L]] | +0.56 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[TCF20]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.55 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[ATG5]] | +0.55 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[TSEN54]] | +0.55 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[PINX1-1]] | +0.55 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ABCC10]] | +0.54 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[BCR]] | +0.54 | +0.49 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB4]] | -0.61 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CHD3]] | -0.55 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[PPP4R3B]] | -0.54 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[NQO1-DT]] | -0.53 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[SMARCA1]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GUCY1A2]] | -0.52 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[DDR2]] | -0.52 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[LINC01170]] | -0.52 | -0.49 / -0.29 | both halves | 3e-04 |  |
| [[CHODL]] | -0.51 | -0.48 / -0.23 | both halves | 5e-04 |  |
| [[PLS3-AS1]] | -0.51 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[TRIP6]] | -0.51 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers BORCS5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (14.0, -8.5); signed map (-40.3, -16.7). **Vector** length 82.3, 17.5% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +9.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +7.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | -0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -6.4 | -12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.4 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.4 | -9.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.3 | -0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | BLOC-1 related complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:12,357,078-12,471,233 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOH1CR12; previously LOH12CR1 |
| Gene groups (HGNC) | BLOC-1 related complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969J3](https://www.uniprot.org/uniprotkb/Q969J3) (BLOC-1-related complex subunit 5):

> As part of the BORC complex may play a role in lysosomes movement and localization at the cell periphery. Associated with the cytosolic face of lysosomes, the BORC complex may recruit ARL8B and couple lysosomes to microtubule plus-end-directed kinesin motor. Thereby, it may indirectly play a role in cell spreading and motility.

**Summary**, from NCBI Gene [118426](https://www.ncbi.nlm.nih.gov/gene/118426):

> Involved in lysosome localization and organelle transport along microtubule. Located in cytoplasmic side of lysosomal membrane and plus-end kinesin complex. Part of BORC complex. Implicated in colorectal adenocarcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17950) · Entrez [118426](https://www.ncbi.nlm.nih.gov/gene/118426) · UniProt [Q969J3](https://www.uniprot.org/uniprotkb/Q969J3) · Ensembl [ENSG00000165714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165714)

## Data

Gene col 9174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9174); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9174]; `tensor/DDL_lfc|DDL_z.npy` [9174]; `embed/gene_vectors.npy` [9174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9174 or target_col == 9174). Every well: [[BORCS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BORCS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

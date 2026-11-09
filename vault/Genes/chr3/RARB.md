---
symbol: "RARB"
type: "gene"
col: 1172
ensembl_id: "ENSG00000077092"
name: "retinoic acid receptor beta"
location: "3p24.2"
module: 152
arm: "+"
pooled_cpm: 30.8
n_lines_expressing: 22
n_dd_up: 33
n_dd_down: 17
n_dd_up_clean: 30
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 33
direction_downstream: 39
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# RARB

*retinoic acid receptor beta* — 3p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.80× (z +23.0, q 0e+00, up in 3 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.635× (z -7.1, q 6e-10, down in 14 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD16]] (+0.65, fdr 7e-06), [[KC6]] (+0.63, fdr 1e-05), [[MSC-AS1]] (+0.60, fdr 1e-05); moves opposite to [[IQANK1]] (-0.49, fdr 3e-05), [[PATJ]] (-0.47, fdr 8e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[IQANK1]] → it (grade B ⚠); 39 go from it, the strongest it → [[P2RX7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +23.0 | 0e+00 | 3/20 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +15.5 | 0e+00 | 10/20 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.15×** | +12.1 | 2e-31 | 8/20 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +10.2 | 2e-22 | 1/17 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | **1.53×** | +9.5 | 2e-19 | 17/20 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.9 | 6e-17 | 2/20 (BT-474, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +8.4 | 3e-15 | 9/20 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +8.3 | 5e-15 | 16/20 (SK-MEL-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.63×** | +7.7 | 1e-12 | 16/20 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.6 | 2e-12 | 2/20 (BT-474, NCI-H460) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +6.7 | 1e-09 | 10/20 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +6.6 | 2e-09 | 9/20 (SK-MEL-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +6.0 | 9e-08 | 15/19 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.45×** | +5.9 | 2e-07 | 12/20 (SHP-77, NCI-H1792, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 9e-07 | 8/20 (J82, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +5.5 | 2e-06 | 12/19 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 6e-05 | 13/20 (NCI-H460, NCI-H1792, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.635×** | -7.1 | 6e-10 | 14/20 (LOX-IMVI, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.641×** | -7.0 | 6e-10 | 16/20 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.703×** | -5.6 | 5e-06 | 10/19 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.705×** | -5.5 | 5e-06 | 18/20 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.714×** | -5.3 | 1e-05 | 17/20 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -5.2 | 2e-05 | 0/21 | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.797×** | -5.1 | 3e-05 | 10/20 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -4.2 | 0.002 | 16/20 (NCI-H1792, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.774×** | -4.0 | 0.003 | 7/20 (LOX-IMVI, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.785×** | -3.8 | 0.007 | 14/20 (A549, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.024 | 13/20 (NCI-H460, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -3.5 | 0.024 | 10/20 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.803×** | -3.5 | 0.024 | 7/20 (LOX-IMVI, A549, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.051 | 7/20 (C32, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.811×** | -3.2 | 0.051 | 7/20 (A549, J82, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -3.2 | 0.051 | 18/20 (RPMI-7951, C32, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.808×** | -3.1 | 0.062 | 6/19 (A549, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 261 | 2 | 10 (5 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.34× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -26.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 90.2 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0844× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 58.0 | 3 | 7 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.10× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.175× (z -12.1) |
| [[SHP-77 (line)]] | alt | 66.5 | 2 | 6 (4 ⚠) | [[Retinoic acid (drug)]] 5 µM 3.34× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.236× (z -10.5) |
| [[A549 (line)]] | wt | 104 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -19.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0832× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0858× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.131× (z -14.2) |
| [[C32 (line)]] | wt | 103 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0243× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.135× (z -13.9) |
| [[HS-578T (line)]] | alt | 155 | 0 | 6 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.247× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 44.9 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 4.12× (z +11.2) | — |
| [[J82 (line)]] | alt | 45.6 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.32× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -8.7) |
| [[AN3 CA (line)]] | alt | 71.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -9.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.158× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 13.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.22× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 63.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -10.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 16.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.57× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0637× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.21 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.79 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD16]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[KC6]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[MSC-AS1]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[GLYATL2]] | +0.60 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ADAM12]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[GXYLT2]] | +0.60 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[SLC8A1]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CA12]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PTPRD]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 | STRING 407 |
| [[TMEM178B]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[TRIM9]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ADGRB3]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQANK1]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[PATJ]] | -0.47 | -0.37 / -0.56 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 7, C 26. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IQANK1]] | B | IQANK1 activity lowers RARB's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 4.51× higher at baseline in the lines without IQANK1 | 0.014 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[P2RX7]] | B | P2RX7 activity raises RARB's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 3.09× lower at baseline in the lines without P2RX7 | 0.027 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[PLOD2]] | B | PLOD2 activity raises RARB's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 3.46× lower at baseline in the lines without PLOD2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[DAB2]] | B | DAB2 activity raises RARB's level | lines that do not express DAB2 (18) vs lines expressing it (32) | 3.51× lower at baseline in the lines without DAB2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: C9, NNMT, DPYSL3 |
| [[PATJ]] | B | PATJ activity lowers RARB's level | lines that do not express PATJ (9) vs lines expressing it (41) | 8.67× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[SLC16A5]] | B | SLC16A5 activity lowers RARB's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 2.88× higher at baseline in the lines without SLC16A5 | 0.078 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[DIRC3]] | B | DIRC3 activity raises RARB's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 3.04× lower at baseline in the lines without DIRC3 | 0.099 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[TRPA1]] | C | TRPA1 activity raises RARB's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 6.32× lower at baseline in the lines without TRPA1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises RARB's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 6.69× lower at baseline in the lines without MSC-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[TNS1]] | C | TNS1 activity raises RARB's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.57× lower at baseline in the lines without TNS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises RARB's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 4.38× lower at baseline in the lines without PDE3A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[ZMAT4]] | C | ZMAT4 activity raises RARB's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 4.72× lower at baseline in the lines without ZMAT4 | 0.012 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 10, C 29. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RX7]] | B | RARB activity raises P2RX7's level | lines that do not express RARB (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without RARB | 0.014 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[PAPSS2]] | B | RARB activity raises PAPSS2's level | lines that do not express RARB (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without RARB | 0.024 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[MLLT3]] | B | RARB activity raises MLLT3's level | lines that do not express RARB (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without RARB | 0.038 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[TMEM45A]] | B | RARB activity raises TMEM45A's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.98× lower at baseline in the lines without RARB | 0.060 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[NREP]] | B | RARB activity raises NREP's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.99× lower at baseline in the lines without RARB | 0.069 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[DAB2]] | B | RARB activity raises DAB2's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.13× lower at baseline in the lines without RARB | 0.087 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[PLOD2]] | B | RARB activity raises PLOD2's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.32× lower at baseline in the lines without RARB | 0.088 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | RARB activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express RARB (28) vs lines expressing it (20) | the lines without RARB: 0.88× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[NRP2]] | B | [[RARA]], RARB, [[RARG]] activity raises NRP2's level | compounds that target RARA, RARB, RARG: 2 of 2 raise it (Retinoic acid, Tazarotene) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[NRP2]] | B | RARB activity raises NRP2's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.01× lower at baseline in the lines without RARB | 0.096 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[ADAM12]] | C | RARB activity raises ADAM12's level | lines that do not express RARB (28) vs lines expressing it (22) | 7.81× lower at baseline in the lines without RARB | 0.008 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA; co-absent with the target |
| [[KCNE4]] | C | RARB activity raises KCNE4's level | lines that do not express RARB (28) vs lines expressing it (22) | 4.32× lower at baseline in the lines without RARB | 0.008 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.741). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.6, 27.2); signed map (31.7, 42.9). **Vector** length 77.7, 23.0% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +15.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +23.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -7.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | retinoic acid receptor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.2 — chr3:24,687,887-25,597,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HAP, NR1B2, RRB2, RARbeta, RAR-beta |
| Gene groups (HGNC) | Retinoic acid receptors |
| Reactome | 5 pathways, smallest: Signaling by Retinoic Acid; Nuclear Receptor transcription pathway; Activation of HOX genes during differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P10826](https://www.uniprot.org/uniprotkb/P10826) (Retinoic acid receptor beta):

> Receptor for retinoic acid. Retinoic acid receptors bind as heterodimers to their target response elements in response to their ligands, all-trans or 9-cis retinoic acid, and regulate gene expression in various biological processes. The RXR/RAR heterodimers bind to the retinoic acid response elements (RARE) composed of tandem 5'-AGGTCA-3' sites known as DR1-DR5. In the absence or presence of hormone ligand, acts mainly as an activator of gene expression due to weak binding to corepressors. The …

**Summary**, from NCBI Gene [5915](https://www.ncbi.nlm.nih.gov/gene/5915):

> This gene encodes retinoic acid receptor beta, a member of the thyroid-steroid hormone receptor superfamily of nuclear transcriptional regulators. This receptor localizes to the cytoplasm and to subnuclear compartments. It binds retinoic acid, the biologically active form of vitamin A which mediates cellular signalling in embryonic morphogenesis, cell growth and differentiation. It is thought that this protein limits growth of many cell types by regulating gene expression. The gene was first …

**Accessions** — [HGNC:9865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9865) · Entrez [5915](https://www.ncbi.nlm.nih.gov/gene/5915) · UniProt [P10826](https://www.uniprot.org/uniprotkb/P10826) · Ensembl [ENSG00000077092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077092)

## Data

Gene col 1172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1172); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1172]; `tensor/DDL_lfc|DDL_z.npy` [1172]; `embed/gene_vectors.npy` [1172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1172 or target_col == 1172). Every well: [[RARB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RARB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

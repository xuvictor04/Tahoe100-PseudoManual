---
symbol: "ARMC10"
type: "gene"
col: 9988
ensembl_id: "ENSG00000170632"
name: "armadillo repeat containing 10"
location: "7q22.1"
module: 18
arm: "+"
pooled_cpm: 48.19
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ARMC10

*armadillo repeat containing 10* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +8.3, q 8e-14, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -19.3, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM89A]] (+0.64, fdr 1e-05), [[TCTN3]] (+0.63, fdr 7e-06), [[FAM86DP]] (+0.59, fdr 1e-05); moves opposite to [[PRECSIT]] (-0.60, fdr 1e-05), [[SRSF3]] (-0.59, fdr 1e-05), [[PALLD]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9988.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +8.3 | 8e-14 | 35/48 (C32, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.5 | 7e-06 | 19/48 (LoVo, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.5 | 7e-06 | 24/48 (HS-578T, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.15× | +3.5 | 0.055 | 7/48 (J82, A549, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.17 | 4/48 (SW 900, SHP-77, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.09× | +3.1 | 0.17 | 2/48 (C32, NCI-H1792) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9988.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.582×** | -19.3 | 0e+00 | 42/48 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.664×** | -9.9 | 7e-21 | 34/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.733×** | -7.8 | 9e-13 | 28/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -7.4 | 3e-11 | 27/48 (A-172, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.764×** | -6.3 | 4e-08 | 26/43 (RKO, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.785×** | -6.1 | 8e-08 | 24/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.636×** | -6.0 | 2e-07 | 26/49 (PANC-1, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.804×** | -5.4 | 6e-06 | 23/48 (LS 180, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.677×** | -5.2 | 2e-05 | 18/35 (NCI-H1573, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.683×** | -5.0 | 3e-05 | 24/48 (A-427, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.849× | -4.1 | 0.002 | 21/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.891× | -4.1 | 0.002 | 12/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.857× | -4.1 | 0.002 | 15/48 (SW480, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.885× | -4.0 | 0.003 | 14/48 (SW480, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | 0.858× | -3.7 | 0.007 | 15/47 (C32, SNU-423, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.867× | -3.6 | 0.010 | 10/48 (RKO, PANC-1, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.768×** | -3.5 | 0.015 | 5/48 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.872× | -3.5 | 0.016 | 13/47 (NCI-H460, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.873× | -3.4 | 0.017 | 18/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 76.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -17.1) |
| [[RKO (line)]] | wt | 78.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -24.3) |
| [[NCI-H23 (line)]] | alt | 68.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -14.7) |
| [[PANC-1 (line)]] | alt | 67.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -15.8) |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 2 | — | [[Malotilate (drug)]] 0.5 µM 0.148× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 73.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 45.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H460 (line)]] | wt | 42.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -14.4) |
| [[SNU-423 (line)]] | alt | 46.8 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.333× (z -11.2) |
| [[SW480 (line)]] | alt | 69.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -13.6) |
| [[A-172 (line)]] | wt | 46.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.281× (z -13.6) |
| [[A-427 (line)]] | wt | 45.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -19.1) |
| [[A549 (line)]] | wt | 55.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -9.6) |
| [[C-33 A (line)]] | alt | 46.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.3) |
| [[C32 (line)]] | wt | 70.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -9.6) |
| [[HCT15 (line)]] | alt | 52.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.3) |
| [[HS-578T (line)]] | alt | 47.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 41.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.2) |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.113× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 63.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.9) |
| [[SNU-1 (line)]] | wt | 38.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.235× (z -9.0) |
| [[SW48 (line)]] | wt | 51.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89A]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TCTN3]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[FAM86DP]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[DPY19L3]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[AVL9]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TMEM87B]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ANKS1A]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[PIGF]] | +0.55 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FBXL4]] | +0.55 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[RABEPK]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PIGN]] | +0.55 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PAM16]] | +0.53 | +0.40 / +0.57 | both halves | 5e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRECSIT]] | -0.60 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PALLD]] | -0.57 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[CELSR3]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ENPP1]] | -0.53 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[DYNLRB2-AS1]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PABIR1]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[LINC02901]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PPP2CA]] | -0.51 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[PLS3]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CCDC80]] | -0.50 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[MAP7D1]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARMC10's level | compounds that target TOP2A: 2 of 5 raise it (Doxorubicin, Epirubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.386). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-13.6, 23.7); signed map (-40.7, -21.9). **Vector** length 98.9, 21.9% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -5.2 | -1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.0 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:103,074,881-103,099,759 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3195, SVH |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2F6](https://www.uniprot.org/uniprotkb/Q8N2F6) (Armadillo repeat-containing protein 10):

> May play a role in cell survival and cell growth. May suppress the transcriptional activity of p53/TP53.

**Summary**, from NCBI Gene [83787](https://www.ncbi.nlm.nih.gov/gene/83787):

> This gene encodes a protein that contains an armadillo repeat and transmembrane domain. The encoded protein decreases the transcriptional activity of the tumor suppressor protein p53 through direct interaction with the DNA-binding domain of p53, and may play a role in cell growth and survival. Upregulation of this gene may play a role in hepatocellular carcinoma. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and a pseudogene of this gene …

**Accessions** — [HGNC:21706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21706) · Entrez [83787](https://www.ncbi.nlm.nih.gov/gene/83787) · UniProt [Q8N2F6](https://www.uniprot.org/uniprotkb/Q8N2F6) · Ensembl [ENSG00000170632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170632)

## Data

Gene col 9988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9988); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9988]; `tensor/DDL_lfc|DDL_z.npy` [9988]; `embed/gene_vectors.npy` [9988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9988 or target_col == 9988). Every well: [[ARMC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

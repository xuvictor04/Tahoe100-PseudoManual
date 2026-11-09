---
symbol: "NMRAL1"
type: "gene"
col: 7721
ensembl_id: "ENSG00000153406"
name: "NmrA like redox sensor 1"
location: "16p13.3"
module: 30
arm: "+"
pooled_cpm: 16.56
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# NMRAL1

*NmrA like redox sensor 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.39× (z +5.2, q 1e-04, up in 20 of 45 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.35× (z +3.4, q 0.074, up in 11 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 5.02×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 2.76×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.34×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.554× (z -13.2, q 7e-37, down in 35 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC45A]] (+0.68, fdr 2e-05), [[FLYWCH1]] (+0.62, fdr 1e-05), [[TBCE]] (+0.62, fdr 2e-05); moves opposite to [[SKIL]] (-0.64, fdr 2e-05), [[CGGBP1]] (-0.61, fdr 4e-05), [[PCF11]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7721.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 5.02×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 2.76×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.34×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +5.2 | 1e-04 | 20/45 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.30×** | +4.2 | 0.009 | 18/44 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.28×** | +4.0 | 0.014 | 14/44 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.27×** | +3.8 | 0.020 | 15/38 (A498, KATO III, …) | inconsistent across doses | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.25×** | +3.6 | 0.040 | 14/45 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.074 | 11/43 (A498, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.24× | +3.2 | 0.11 | 12/45 (SW1417, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.554×** | -13.2 | 7e-37 | 35/44 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.449×** | -12.6 | 4e-34 | 44/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.493×** | -10.7 | 1e-24 | 34/44 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -9.1 | 9e-18 | 28/43 (HCT15, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.567×** | -9.0 | 4e-17 | 31/43 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.574×** | -8.8 | 2e-16 | 33/44 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -8.3 | 8e-15 | 34/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.515×** | -5.5 | 3e-06 | 19/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -5.4 | 4e-06 | 24/44 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -4.9 | 5e-05 | 16/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.729×** | -4.8 | 8e-05 | 20/41 (BT-474, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.578×** | -4.5 | 3e-04 | 18/41 (C32, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.753×** | -4.5 | 3e-04 | 17/45 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Gefitinib (drug)]] 5 µM |  | **0.772×** | -4.1 | 0.002 | 13/45 (NCI-H460, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.9 | 0.003 | 17/45 (C32, SNU-1, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.791×** | -3.7 | 0.008 | 13/44 (A498, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.804×** | -3.4 | 0.020 | 14/44 (MIA PaCa-2, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.2 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +20.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -12.2) |
| [[PANC-1 (line)]] | alt | 25.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -18.6) |
| [[C32 (line)]] | wt | 14.8 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 16.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -14.8) |
| [[J82 (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.302× (z -8.5) |
| [[LoVo (line)]] | wt | 11.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -18.2) |
| [[A498 (line)]] | wt | 28.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.2) |
| [[BT-474 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0938× (z -15.4) ⚠ toxic |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.7) |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.183× (z -8.6) |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.5) |
| [[KATO III (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -12.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.2) |
| [[RKO (line)]] | wt | 14.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.176× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0559× (z -17.5) |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.132× (z -10.2) |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.6) |
| [[A-172 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC45A]] | +0.68 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[FLYWCH1]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TBCE]] | +0.62 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[HTT]] | +0.62 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[CDK5RAP1]] | +0.61 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ANKRD39]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[GRB2]] | +0.60 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[XYLT2]] | +0.60 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[ECI2]] | +0.59 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[CRYZL1]] | +0.59 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ASB16-AS1]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[INPP5B]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIL]] | -0.64 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[CGGBP1]] | -0.61 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[PCF11]] | -0.60 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[BMI1]] | -0.56 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RFX3-DT]] | -0.56 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[RO60]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[APLF]] | -0.56 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[HIVEP2]] | -0.55 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[HIVEP1]] | -0.55 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[SLC30A1]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[BAZ1A]] | -0.55 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[WARS2-AS1]] | -0.55 | -0.32 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers NMRAL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.7, -14.0); signed map (-33.6, -2.9). **Vector** length 62.2, 9.83% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.5 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.1 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.7 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | -0.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -9.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -12.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | NmrA like redox sensor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,461,691-4,495,763 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25918, HSCARG, SDR48A1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 4 pathways, smallest: Diseases of the urea cycle; Urea cycle; Diseases of metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBL8](https://www.uniprot.org/uniprotkb/Q9HBL8) (NmrA-like family domain-containing protein 1):

> Redox sensor protein. Undergoes restructuring and subcellular redistribution in response to changes in intracellular NADPH/NADP(+) levels. At low NADPH concentrations the protein is found mainly as a monomer, and binds argininosuccinate synthase (ASS1), the enzyme involved in nitric oxide synthesis. Association with ASS1 impairs its activity and reduces the production of nitric oxide, which subsequently prevents apoptosis. Under normal NADPH concentrations, the protein is found as a dimer and …

**Summary**, from NCBI Gene [57407](https://www.ncbi.nlm.nih.gov/gene/57407):

> This gene encodes an NADPH sensor protein that preferentially binds to NADPH. The encoded protein also negatively regulates the activity of NF-kappaB in a ubiquitylation-dependent manner. It plays a key role in cellular antiviral response by negatively regulating the interferon response factor 3-mediated expression of interferon beta. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:24987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24987) · Entrez [57407](https://www.ncbi.nlm.nih.gov/gene/57407) · UniProt [Q9HBL8](https://www.uniprot.org/uniprotkb/Q9HBL8) · Ensembl [ENSG00000153406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153406)

## Data

Gene col 7721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7721); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7721]; `tensor/DDL_lfc|DDL_z.npy` [7721]; `embed/gene_vectors.npy` [7721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7721 or target_col == 7721). Every well: [[NMRAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMRAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

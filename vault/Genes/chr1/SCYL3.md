---
symbol: "SCYL3"
type: "gene"
col: 2
ensembl_id: "ENSG00000000457"
name: "SCY1 like pseudokinase 3"
location: "1q24.2"
module: 23
arm: "+"
pooled_cpm: 12.59
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SCYL3

*SCY1 like pseudokinase 3* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +5.7, q 7e-06, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.548× (z -7.1, q 8e-10, down in 24 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.680× (z -4.5, q 0.001, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 0.109×, SW480 0.273×, RPMI-7951 0.128×, AsPC-1 0.187×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LS 180 0.135×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0781×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 900 0.149×); [[Trimetrexate (drug)]] 0.05 µM in 1 line (SW48 0.0662×).
> Its strongest partners by |cos| (66 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 34 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNISR-AS1]] (+0.65, fdr 1e-04), [[MR1]] (+0.64, fdr 4e-05), [[HEXIM2-AS1]] (+0.63, fdr 5e-04); moves opposite to [[WASF3]] (-0.64, fdr 3e-04), [[GRAMD4]] (-0.56, fdr 3e-04), [[GNAI3]] (-0.54, fdr 0.001, ⚠ one half only (not replicated)), [[GNL2]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.7 | 7e-06 | 26/45 (MIA PaCa-2, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.7 | 4e-04 | 18/48 (HOP62, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.33×** | +4.7 | 4e-04 | 23/48 (BT-474, C32, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 0.002 | 20/47 (BT-474, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.008 | 13/46 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.008 | 18/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.032 | 12/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.033 | 14/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.033 | 16/46 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.078 | 20/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.67×** | +3.1 | 0.088 | 8/46 (BT-474, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.11 | 12/48 (Hs 766T, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 0.109×, SW480 0.273×, RPMI-7951 0.128×, AsPC-1 0.187×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LS 180 0.135×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0781×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 900 0.149×); [[Trimetrexate (drug)]] 0.05 µM in 1 line (SW48 0.0662×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.548×** | -7.1 | 8e-10 | 24/37 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.633×** | -5.0 | 2e-04 | 17/29 (LS 180, SW1417, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.680×** | -4.5 | 0.001 | 18/47 (AN3 CA, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.683×** | -4.0 | 0.008 | 19/40 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.758× | -3.2 | 0.15 | 12/44 (SNU-423, SK-MEL-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 13.2 | 0 | 2 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0781× (z -10.0) |
| [[LoVo (line)]] | wt | 12.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 2 | — | [[Pyridoxine (drug)]] 0.5 µM 0.149× (z -9.8) |
| [[A498 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LS 180 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 7.13 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.109× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW48 (line)]] | wt | 11.3 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0662× (z -9.7) |
| [[SW480 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 31 of them with an alert (⚠; 31 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR-AS1]] | +0.65 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[MR1]] | +0.64 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[HEXIM2-AS1]] | +0.63 | +0.62 / +0.23 | both halves | 5e-04 |  |
| [[DDX6]] | +0.63 | +0.56 / +0.28 | both halves | 3e-04 |  |
| [[RC3H2]] | +0.63 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[C12orf60]] | +0.63 | +0.63 / +0.24 | both halves | 5e-04 |  |
| [[WAC-AS1]] | +0.62 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[AHI1-DT]] | +0.62 | +0.58 / +0.24 | both halves | 4e-04 |  |
| [[RNF146]] | +0.61 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[ZBED5]] | +0.60 | +0.52 / +0.24 | both halves | 4e-04 |  |
| [[ERMAP]] | +0.60 | +0.49 / +0.31 | both halves | 2e-04 |  |
| [[TTC32]] | +0.60 | +0.53 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.64 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[GRAMD4]] | -0.56 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[GNAI3]] | -0.54 | -0.54 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[GNL2]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[HACE1]] | -0.53 | -0.46 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[C1orf21]] | -0.53 | -0.55 / -0.24 | both halves | 5e-04 |  |
| [[NANS]] | -0.53 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[STARD5]] | -0.52 | -0.24 / -0.29 | both halves | 4e-04 |  |
| [[GNB1L]] | -0.52 | -0.48 / -0.24 | both halves | 5e-04 |  |
| [[HK1]] | -0.52 | -0.52 / -0.21 | both halves | 7e-04 |  |
| [[MAPT]] | -0.52 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[EIF4EBP1]] | -0.52 | -0.48 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[SND1]] | -0.51 | -0.44 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SCYL3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXA-AS2]] | C | HOXA-AS2 activity lowers SCYL3's level | lines that do not express HOXA-AS2 (3) vs lines expressing it (47) | 1.75× higher at baseline in the lines without HOXA-AS2 | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (1.2, 11.3); signed map (23.8, -14.1). **Vector** length 76.2, 14.1% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.0 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.6 | +3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.8 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.1 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SCY1 like pseudokinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:169,849,631-169,894,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PACE-1, PACE1 |
| Gene groups (HGNC) | SCY1 like pseudokinases; Pseudokinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZE3](https://www.uniprot.org/uniprotkb/Q8IZE3) (Protein-associating with the carboxyl-terminal domain of ezrin):

> May play a role in regulating cell adhesion/migration complexes in migrating cells.

**Summary**, from NCBI Gene [57147](https://www.ncbi.nlm.nih.gov/gene/57147):

> This gene encodes a protein with a kinase domain and four HEAT repeats. The encoded protein interacts with the C-terminal domain of ezrin, an ERM protein, and may play a role in cell adhesion and migration. Alternative splicing results in multiple transcript variants encoding multiple isoforms. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:19285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19285) · Entrez [57147](https://www.ncbi.nlm.nih.gov/gene/57147) · UniProt [Q8IZE3](https://www.uniprot.org/uniprotkb/Q8IZE3) · Ensembl [ENSG00000000457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000000457)

## Data

Gene col 2: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2]; `tensor/DDL_lfc|DDL_z.npy` [2]; `embed/gene_vectors.npy` [2]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2 or target_col == 2). Every well: [[SCYL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCYL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

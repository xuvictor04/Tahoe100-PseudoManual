---
symbol: "MPST"
type: "gene"
col: 4875
ensembl_id: "ENSG00000128309"
name: "mercaptopyruvate sulfurtransferase"
location: "22q12.3"
module: 3
arm: "+"
pooled_cpm: 11.38
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MPST

*mercaptopyruvate sulfurtransferase* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.52× (z +4.2, q 0.014, up in 18 of 40 measured lines) ⚠ transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.44× (z +3.6, q 0.076, up in 11 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.243× (z -19.7, q 0e+00, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARD19]] (+0.74, fdr 7e-06), [[HEBP1]] (+0.73, fdr 7e-06), [[ANKRD27]] (+0.73, fdr 2e-05); moves opposite to [[ZNF532]] (-0.69, fdr 1e-05), [[DDX6]] (-0.69, fdr 1e-05), [[TIA1]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.2 | 0.014 | 18/40 (CFPAC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.076 | 11/46 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.096 | 15/44 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 1.39× | +3.3 | 0.11 | 14/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | 1.41× | +3.3 | 0.11 | 11/46 (HOP62, A-172, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.37× | +3.1 | 0.16 | 11/45 (NCI-H2030, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.243×** | -19.7 | 0e+00 | 40/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.294×** | -12.0 | 6e-31 | 36/42 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.414×** | -8.7 | 9e-16 | 36/46 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.431×** | -7.9 | 3e-13 | 34/44 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.459×** | -7.6 | 2e-12 | 38/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.494×** | -6.9 | 5e-10 | 31/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.538×** | -6.1 | 1e-07 | 31/46 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.551×** | -5.8 | 4e-07 | 30/45 (hTERT-HPNE, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -5.3 | 7e-06 | 24/45 (COLO 205, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.344×** | -5.3 | 8e-06 | 30/46 (A498, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.345×** | -5.2 | 8e-06 | 31/41 (HOP62, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -4.0 | 0.003 | 21/46 (COLO 205, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.693×** | -3.6 | 0.015 | 20/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.679×** | -3.6 | 0.015 | 18/45 (SW480, C32, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.707×** | -3.4 | 0.027 | 13/45 (NCI-H661, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 37.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -19.4) |
| [[A498 (line)]] | wt | 21.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -22.5) |
| [[SW480 (line)]] | alt | 14.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -17.5) |
| [[A-172 (line)]] | wt | 11.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.5) |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0429× (z -15.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.135× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 6.50 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0443× (z -9.8) |
| [[KATO III (line)]] | alt | 33.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -21.4) |
| [[AsPC-1 (line)]] | alt | 6.75 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0894× (z -9.5) |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0640× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.0) |
| [[HOP62 (line)]] | alt | 7.09 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -13.5) |
| [[SW48 (line)]] | wt | 11.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0632× (z -9.7) |
| [[A549 (line)]] | wt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -16.0) |
| [[C32 (line)]] | wt | 6.49 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0955× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 9.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 27.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.9) |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -13.8) |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -15.2) |
| [[J82 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -14.1) |
| [[LoVo (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -18.4) |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 7.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 5.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 6.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.2) |
| [[PANC-1 (line)]] | alt | 4.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -10.6) |
| [[A-427 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD19]] | +0.74 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[HEBP1]] | +0.73 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.73 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[MPG]] | +0.72 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[WIPI1]] | +0.71 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.71 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[CAMLG]] | +0.71 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.70 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[LRRC42]] | +0.69 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[GLRX5]] | +0.69 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[SDHAP2]] | +0.69 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF532]] | -0.69 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[DDX6]] | -0.69 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TIA1]] | -0.69 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.68 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[SDCBP2-AS1]] | -0.68 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.66 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ST7L]] | -0.65 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[DDX39B]] | -0.65 | -0.40 / -0.59 | both halves | 4e-05 |  |
| [[ERCC6L2]] | -0.64 | -0.63 / -0.37 | both halves | 7e-05 |  |
| [[HNRNPK]] | -0.64 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[VPS35L]] | -0.64 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[CRPPA]] | -0.63 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MPST's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SPIRE1]] | C | SPIRE1 activity lowers MPST's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 2.35× higher at baseline in the lines without SPIRE1 | 0.039 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[TST]] | C | TST's natural level strengthens MPST's drug response | TST's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.15; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[YPEL2]] | C | YPEL2 activity raises MPST's level | lines that do not express YPEL2 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without YPEL2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.770). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.5, -15.0); signed map (-38.1, 2.5). **Vector** length 81.7, 17.7% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.7 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.7 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -19.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | mercaptopyruvate sulfurtransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:37,019,635-37,029,821 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MST, TST2, TUM1 |
| Reactome | 3 pathways, smallest: Degradation of cysteine and homocysteine; Sulfur amino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P25325](https://www.uniprot.org/uniprotkb/P25325) (3-mercaptopyruvate sulfurtransferase):

> Transfer of a sulfur ion to cyanide or to other thiol compounds. Also has weak rhodanese activity. Detoxifies cyanide and is required for thiosulfate biosynthesis. Acts as an antioxidant. In combination with cysteine aminotransferase (CAT), contributes to the catabolism of cysteine and is an important producer of hydrogen sulfide in the brain, retina and vascular endothelial cells. Hydrogen sulfide H(2)S is an important synaptic modulator, signaling molecule, smooth muscle contractor and …

**Summary**, from NCBI Gene [4357](https://www.ncbi.nlm.nih.gov/gene/4357):

> This protein encoded by this gene catalyzes the transfer of a sulfur ion from 3-mercaptopyruvate to cyanide or other thiol compounds. It may be involved in cysteine degradation and cyanide detoxification. There is confusion in literature between this protein (mercaptopyruvate sulfurtransferase, MPST), which appears to be cytoplasmic, and thiosulfate sulfurtransferase (rhodanese, TST, GeneID:7263), which is a mitochondrial protein. Deficiency in MPST activity has been implicated in a rare …

**Accessions** — [HGNC:7223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7223) · Entrez [4357](https://www.ncbi.nlm.nih.gov/gene/4357) · UniProt [P25325](https://www.uniprot.org/uniprotkb/P25325) · Ensembl [ENSG00000128309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128309)

## Data

Gene col 4875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4875); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4875]; `tensor/DDL_lfc|DDL_z.npy` [4875]; `embed/gene_vectors.npy` [4875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4875 or target_col == 4875). Every well: [[MPST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

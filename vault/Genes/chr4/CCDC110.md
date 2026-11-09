---
symbol: "CCDC110"
type: "gene"
col: 9659
ensembl_id: "ENSG00000168491"
name: "coiled-coil domain containing 110"
location: "4q35.1"
module: 1
arm: "-"
pooled_cpm: 3.12
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CCDC110

*coiled-coil domain containing 110* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.76× (z +11.9, q 6e-30, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.299× (z -9.2, q 2e-17, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (56 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 44 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC3P1]] (+0.61, fdr 2e-05), [[SUSD4]] (+0.61, fdr 1e-05), [[SETD5]] (+0.59, fdr 2e-04); moves opposite to [[TOR1A]] (-0.55, fdr 4e-04), [[RNASEH1]] (-0.55, fdr 3e-04), [[SLC5A6]] (-0.54, fdr 5e-04).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CERS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.76×** | +11.9 | 6e-30 | 39/40 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.96×** | +10.5 | 2e-23 | 34/38 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.55×** | +10.1 | 1e-21 | 32/38 (KATO III, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.58×** | +9.7 | 3e-20 | 33/39 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.44×** | +9.4 | 5e-19 | 38/39 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.76×** | +7.7 | 9e-13 | 28/36 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +6.4 | 1e-08 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.60×** | +5.1 | 2e-05 | 15/35 (KATO III, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +4.8 | 1e-04 | 7/26 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.4 | 5e-04 | 9/32 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.68×** | +4.0 | 0.004 | 11/35 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.080 | 6/38 (J82, KATO III, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.080 | 13/28 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.080 | 5/36 (SW480, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.299×** | -9.2 | 2e-17 | 34/40 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.328×** | -8.5 | 6e-15 | 27/38 (HS-578T, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.456×** | -6.0 | 4e-07 | 17/21 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.559×** | -4.4 | 0.001 | 19/34 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -4.1 | 0.006 | 9/18 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.600×** | -3.9 | 0.010 | 11/39 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -3.7 | 0.019 | 12/26 (KATO III, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.647×** | -3.3 | 0.064 | 10/39 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.668× | -3.1 | 0.14 | 8/39 (SNU-423, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.68 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0430× (z -9.6) |
| [[LoVo (line)]] | wt | 4.75 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0520× (z -11.6) |
| [[HCT15 (line)]] | alt | 8.50 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0402× (z -9.5) |
| [[KATO III (line)]] | alt | 3.68 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 14.2× (z +8.7) | [[vincristine (drug)]] 0.05 µM 0.0617× (z -8.6) |
| [[SW480 (line)]] | alt | 8.72 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -10.9) |
| [[A-172 (line)]] | wt | 6.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0716× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 5.39 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0710× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 4.30 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0653× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 6.63 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.104× (z -8.8) |
| [[SHP-77 (line)]] | alt | 3.59 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0388× (z -8.9) |
| [[A498 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.845 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.969 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.974 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.815 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.625 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC3P1]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SUSD4]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SETD5]] | +0.59 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[JAKMIP2]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[SYP]] | +0.55 | +0.26 / +0.57 | both halves | 4e-04 |  |
| [[TMC3-AS1]] | +0.54 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[SLC17A7]] | +0.54 | +0.27 / +0.61 | both halves | 3e-04 |  |
| [[TUBB2B]] | +0.53 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[SPTBN4]] | +0.53 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[KMT2C]] | +0.53 | +0.32 / +0.39 | both halves | 2e-04 |  |
| [[TTLL7]] | +0.53 | +0.21 / +0.53 | both halves | 7e-04 |  |
| [[DDIT4]] | +0.52 | +0.20 / +0.48 | ⚠ not reproduced | 8e-04 |  |
| [[TNNT1]] | +0.51 | +0.21 / +0.35 | both halves | 6e-04 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 32 of them with an alert (⚠; 32 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR1A]] | -0.55 | -0.26 / -0.60 | both halves | 4e-04 |  |
| [[RNASEH1]] | -0.55 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[SLC5A6]] | -0.54 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[SNX5]] | -0.53 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[ZNF124]] | -0.52 | -0.15 / -0.23 | ⚠ not reproduced | 0.001 |  |
| [[PRDM5]] | -0.52 | -0.14 / -0.50 | ⚠ not reproduced | 0.002 |  |
| [[PSME3]] | -0.51 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[ELK4]] | -0.51 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[PIGW]] | -0.50 | -0.20 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[VPS52]] | -0.50 | -0.07 / -0.52 | ⚠ one half (not replicated) | 0.004 |  |
| [[MAPKAPK5]] | -0.50 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[EFCAB2]] | -0.50 | -0.06 / -0.49 | ⚠ not reproduced | 0.005 |  |
| [[CERS2]] | -0.49 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[RCC2]] | -0.48 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[MSANTD2]] | -0.48 | -0.25 / -0.32 | both halves | 4e-04 |  |
| [[DHRS11]] | -0.47 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[FBXO22]] | -0.47 | -0.32 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERS2]] | B | CCDC110 activity lowers CERS2's level | lines that do not express CCDC110 (5) vs lines expressing it (45) | 1.35× higher at baseline in the lines without CCDC110 | 0.072 | ⚠ within organs, on part of the lines; also absent: MLF1, CDC42EP3, C1orf216; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.240). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-0.2, 35.6); signed map (-26.4, 24.6). **Vector** length 53.6, 8.37% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.1 | +10.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +5.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.9 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -9.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | +0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 110 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,445,182-185,471,752 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KM-HN-1, MGC33607, CT52 |
| Matched by | ensembl_id |

UniProt [Q8TBZ0](https://www.uniprot.org/uniprotkb/Q8TBZ0) carries no function annotation.

**Summary**, from NCBI Gene [256309](https://www.ncbi.nlm.nih.gov/gene/256309):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28504) · Entrez [256309](https://www.ncbi.nlm.nih.gov/gene/256309) · UniProt [Q8TBZ0](https://www.uniprot.org/uniprotkb/Q8TBZ0) · Ensembl [ENSG00000168491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168491)

## Data

Gene col 9659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9659); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9659]; `tensor/DDL_lfc|DDL_z.npy` [9659]; `embed/gene_vectors.npy` [9659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9659 or target_col == 9659). Every well: [[CCDC110 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC110.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "MTARC1"
type: "gene"
col: 11793
ensembl_id: "ENSG00000186205"
name: "mitochondrial amidoxime reducing component 1"
location: "1q41"
module: 4
arm: "+"
pooled_cpm: 4.79
n_lines_expressing: 38
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MTARC1

*mitochondrial amidoxime reducing component 1* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.90× (z +21.5, q 0e+00, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.69× (z +7.2, q 9e-11, up in 16 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.130×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0460×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNNM1]] (+0.61, fdr 1e-05), [[AGMAT]] (+0.61, fdr 1e-05), [[LINC01357]] (+0.60, fdr 2e-05); moves opposite to [[TOX4]] (-0.52, fdr 3e-05), [[SHOC2]] (-0.48, fdr 6e-05), [[CDKL5]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AGMAT]] → it (grade B ⚠); 2 go from it, the strongest it → [[RNF157]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11793.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.90×** | +21.5 | 0e+00 | 5/5 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.14×** | +20.5 | 0e+00 | 20/21 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.08×** | +12.7 | 1e-34 | 11/13 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +7.2 | 9e-11 | 16/33 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +7.1 | 1e-10 | 17/33 (NCI-H2347, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.4 | 2e-08 | 5/18 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +6.2 | 5e-08 | 14/24 (NCI-H1573, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.74×** | +5.4 | 4e-06 | 16/34 (SW 900, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +4.9 | 6e-05 | 10/28 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +4.5 | 4e-04 | 13/34 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.5 | 4e-04 | 13/31 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.3 | 7e-04 | 7/19 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +4.0 | 0.003 | 12/32 (J82, SW 900, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.32×** | +3.9 | 0.005 | 7/27 (NCI-H2347, A549, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +3.7 | 0.007 | 7/32 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.062 | 7/34 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11793.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.130×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0460×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.505× | -3.5 | 0.27 | 8/27 (RKO, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 7.17 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.5× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.97× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 6.65 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.6× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 11.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.94× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 4.25 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0460× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -14.0) |
| [[A-172 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM1]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[AGMAT]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LINC01357]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[DHX15]] | +0.60 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[CGREF1]] | +0.60 | +0.36 / +0.72 | both halves | 9e-05 |  |
| [[DHRS4L2]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[LRP3]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ALDH5A1]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TTPA]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[MEST]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[FTCDNL1]] | +0.52 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[TMCC1-DT]] | +0.52 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOX4]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SHOC2]] | -0.48 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[CDKL5]] | -0.47 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[CPEB4]] | -0.46 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[ZKSCAN5]] | -0.46 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[CHMP5]] | -0.45 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[RNF181]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[SELENOK]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGMAT]] | B | AGMAT activity raises MTARC1's level | lines that do not express AGMAT (11) vs lines expressing it (39) | 2.21× lower at baseline in the lines without AGMAT | 0.077 | ⚠ within organs, on part of the lines; also absent: ETV7, LYPD5, TNK1; maybe low, not absent |
| [[SLC9B2]] | C | SLC9B2 activity raises MTARC1's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without SLC9B2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF157]] | B | MTARC1 activity lowers RNF157's level | lines that do not express MTARC1 (12) vs lines expressing it (38) | 1.29× higher at baseline in the lines without MTARC1 | 0.057 | ⚠ within organs, on part of the lines; also absent: C1orf115, SEPTIN9-DT, MTARC2 |
| [[EMSLR]] | C | MTARC1 activity raises EMSLR's level | lines that do not express MTARC1 (12) vs lines expressing it (38) | 2.25× lower at baseline in the lines without MTARC1 | 0.023 | ⚠ within organs, on part of the lines; also absent: C1orf115, SEPTIN9-DT, MTARC2; co-absent with the target |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.385). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.3, 43.3); signed map (-5.5, -58.8). **Vector** length 53.4, 9.12% of its response variance represented; |z| ≥ 3 in 709 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +21.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +20.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial amidoxime reducing component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:220,786,352-220,819,659 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22390; previously MOSC1, MARC1 |
| Gene groups (HGNC) | Mitochondrial amidoxime reducing component family |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VT66](https://www.uniprot.org/uniprotkb/Q5VT66) (Mitochondrial amidoxime-reducing component 1):

> Catalyzes the reduction of N-oxygenated molecules, acting as a counterpart of cytochrome P450 and flavin-containing monooxygenases in metabolic cycles. As a component of prodrug-converting system, reduces a multitude of N-hydroxylated prodrugs particularly amidoximes, leading to increased drug bioavailability. May be involved in mitochondrial N(omega)-hydroxy-L-arginine (NOHA) reduction, regulating endogenous nitric oxide levels and biosynthesis. Postulated to cleave the N-OH bond of …

**Summary**, from NCBI Gene [64757](https://www.ncbi.nlm.nih.gov/gene/64757):

> Enables molybdenum ion binding activity; molybdopterin cofactor binding activity; and oxidoreductase activity, acting on other nitrogenous compounds as donors. Contributes to nitrite reductase (NO-forming) activity. Involved in cellular detoxification of nitrogen compound; nitrate metabolic process; and nitric oxide biosynthetic process. Located in mitochondrion. Part of nitric-oxide synthase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26189) · Entrez [64757](https://www.ncbi.nlm.nih.gov/gene/64757) · UniProt [Q5VT66](https://www.uniprot.org/uniprotkb/Q5VT66) · Ensembl [ENSG00000186205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186205)

## Data

Gene col 11793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11793); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11793]; `tensor/DDL_lfc|DDL_z.npy` [11793]; `embed/gene_vectors.npy` [11793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11793 or target_col == 11793). Every well: [[MTARC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTARC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

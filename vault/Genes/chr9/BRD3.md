---
symbol: "BRD3"
type: "gene"
col: 9876
ensembl_id: "ENSG00000169925"
name: "bromodomain containing 3"
location: "9q34.2"
module: 145
arm: "+"
pooled_cpm: 39.61
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# BRD3

*bromodomain containing 3* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +9.8, q 6e-20, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.560× (z -11.1, q 6e-26, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHO2]] (+0.59, fdr 9e-05), [[BRWD1]] (+0.58, fdr 4e-05), [[NR2C2]] (+0.57, fdr 4e-05); moves opposite to [[FRRS1]] (-0.48, fdr 3e-05), [[XKR6]] (-0.46, fdr 3e-04), [[ZNF780B]] (-0.44, fdr 6e-04).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +9.8 | 6e-20 | 40/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.9 | 3e-04 | 33/47 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.7 | 4e-04 | 28/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +4.7 | 4e-04 | 31/47 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.36×** | +4.1 | 0.006 | 20/40 (Hs 766T, BT-474, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.30×** | +3.6 | 0.030 | 22/47 (A-172, A549, …) | rises with dose | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.098 | 20/47 (NCI-H460, A498, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.17× | +3.1 | 0.16 | 16/48 (CHP-212, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.16 | 18/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.560×** | -11.1 | 6e-26 | 40/48 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.232×** | -10.4 | 8e-23 | 46/48 (A-427, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.485×** | -9.8 | 2e-20 | 43/48 (KATO III, MIA PaCa-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.517×** | -8.9 | 5e-17 | 39/47 (J82, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.537×** | -8.4 | 4e-15 | 36/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -7.3 | 3e-11 | 39/48 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.633×** | -6.2 | 5e-08 | 29/48 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -5.3 | 6e-06 | 28/47 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -5.3 | 8e-06 | 30/48 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.484×** | -5.1 | 1e-05 | 34/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.677×** | -5.1 | 2e-05 | 27/48 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.521×** | -4.6 | 2e-04 | 29/47 (HS-578T, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -4.6 | 2e-04 | 27/48 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.522×** | -4.6 | 2e-04 | 29/47 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.526×** | -4.6 | 2e-04 | 29/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.701×** | -4.5 | 2e-04 | 26/48 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.568×** | -4.0 | 0.002 | 26/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.4 | 1 | 10 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 45.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0782× (z -29.5) |
| [[J82 (line)]] | alt | 85.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -19.9) |
| [[SW480 (line)]] | alt | 44.7 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 34.7 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 51.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0428× (z -27.5) |
| [[PANC-1 (line)]] | alt | 25.0 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.319× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.397× (z -8.6) |
| [[RKO (line)]] | wt | 68.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.2) |
| [[A-427 (line)]] | wt | 32.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0510× (z -13.4) |
| [[A-172 (line)]] | wt | 52.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -17.8) |
| [[A498 (line)]] | wt | 48.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 36.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.61× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Selinexor (drug)]] 5 µM 0.320× (z -11.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.304× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 29.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -9.8) |
| [[A549 (line)]] | wt | 40.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 41.1 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0424× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 59.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.133× (z -8.7) |
| [[HOP62 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.0) |
| [[HT-29 (line)]] | alt | 46.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.303× (z -11.0) |
| [[KATO III (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.320× (z -9.9) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 49.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.141× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.175× (z -11.5) |
| [[SNU-1 (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -12.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO2]] | +0.59 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[BRWD1]] | +0.58 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[NR2C2]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ATXN2]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[JMY]] | +0.54 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[CASP8AP2]] | +0.54 | +0.37 / +0.61 | both halves | 9e-05 |  |
| [[SPECC1L]] | +0.53 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[EHMT1]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 | STRING 563 |
| [[CRAMP1]] | +0.52 | +0.25 / +0.66 | both halves | 4e-04 |  |
| [[JADE3]] | +0.52 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[UBALD1]] | +0.52 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[MOB2]] | +0.51 | +0.19 / +0.67 | ⚠ one half (not replicated) | 8e-04 |  |
| [[SAP30L]] | +0.50 | +0.37 / +0.57 | both halves | 8e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRRS1]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[XKR6]] | -0.46 | -0.26 / -0.50 | both halves | 3e-04 |  |
| [[ZNF780B]] | -0.44 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[NBDY]] | -0.43 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[ZNF283]] | -0.42 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[MAGED1]] | -0.42 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[DISC1FP1]] | -0.41 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[CCNC]] | -0.41 | -0.25 / -0.45 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BRD3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.0, -41.5); signed map (-16.6, 13.0). **Vector** length 98.7, 28.3% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +9.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.6 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -7.2 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -6.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -6.2 | +3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.8 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -4.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:134,030,305-134,068,535 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RING3L, ORFX, KIAA0043, FSHRG2 |
| Gene groups (HGNC) | Bromodomain and extra-terminal domain family; Bromodomain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15059](https://www.uniprot.org/uniprotkb/Q15059) (Bromodomain-containing protein 3):

> Chromatin reader that recognizes and binds acetylated histones, thereby controlling gene expression and remodeling chromatin structures. Recruits transcription factors and coactivators to target gene sites, and activates RNA polymerase II machinery for transcriptional elongation. In vitro, binds acetylated lysine residues on the N-terminus of histone H2A, H2B, H3 and H4. Involved in endoderm differentiation via its association with long non-coding RNA (lncRNA) DIGIT: BRD3 undergoes …

**Summary**, from NCBI Gene [8019](https://www.ncbi.nlm.nih.gov/gene/8019):

> This gene was identified based on its homology to the gene encoding the RING3 protein, a serine/threonine kinase. The gene localizes to 9q34, a region which contains several major histocompatibility complex (MHC) genes. The function of the encoded protein is not known. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1104) · Entrez [8019](https://www.ncbi.nlm.nih.gov/gene/8019) · UniProt [Q15059](https://www.uniprot.org/uniprotkb/Q15059) · Ensembl [ENSG00000169925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169925)

## Data

Gene col 9876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9876); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9876]; `tensor/DDL_lfc|DDL_z.npy` [9876]; `embed/gene_vectors.npy` [9876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9876 or target_col == 9876). Every well: [[BRD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

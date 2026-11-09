---
symbol: "MINK1"
type: "gene"
col: 6530
ensembl_id: "ENSG00000141503"
name: "misshapen like kinase 1"
location: "17p13.2"
module: 77
arm: "+"
pooled_cpm: 88.14
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# MINK1

*misshapen like kinase 1* — 17p13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.428× (z -20.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST3]] (+0.69, fdr 9e-05), [[LPCAT4]] (+0.67, fdr 3e-05), [[BRAT1]] (+0.66, fdr 1e-05); moves opposite to [[PPP1R12A-AS2]] (-0.67, fdr 2e-04), [[RIPK2-DT]] (-0.67, fdr 4e-05), [[PCNX4-DT]] (-0.65, fdr 4e-04).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRC17]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6530.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.428×** | -20.9 | 0e+00 | 44/48 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.452×** | -13.8 | 4e-41 | 46/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.439×** | -13.8 | 5e-41 | 44/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.576×** | -13.6 | 4e-40 | 45/49 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.481×** | -12.8 | 3e-35 | 46/48 (C32, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.632×** | -7.4 | 1e-11 | 34/45 (SNU-1, A549, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -7.3 | 2e-11 | 42/47 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.682×** | -6.7 | 2e-09 | 34/49 (C-33 A, SW480, …) | all doses, flat | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -6.1 | 5e-08 | 35/48 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -6.0 | 1e-07 | 30/50 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -5.9 | 1e-07 | 34/48 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.702×** | -5.9 | 1e-07 | 25/43 (C-33 A, HS-578T, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -5.6 | 8e-07 | 30/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.548×** | -5.5 | 2e-06 | 35/45 (Hs 766T, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.746×** | -5.1 | 1e-05 | 28/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.587×** | -4.9 | 4e-05 | 30/49 (PANC-1, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.767×** | -4.6 | 1e-04 | 30/48 (CFPAC-1, A-172, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.002 | 28/48 (LoVo, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.876× | -3.2 | 0.031 | 19/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.841× | -2.9 | 0.091 | 19/48 (NCI-H1792, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 69.8 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -18.2) |
| [[HOP62 (line)]] | alt | 68.8 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -17.5) |
| [[C32 (line)]] | wt | 73.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -19.8) |
| [[CFPAC-1 (line)]] | alt | 81.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -18.3) |
| [[A-172 (line)]] | wt | 135 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -17.4) |
| [[HS-578T (line)]] | alt | 80.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -19.0) |
| [[LOX-IMVI (line)]] | wt | 73.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -20.5) |
| [[MIA PaCa-2 (line)]] | alt | 118 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -25.0) |
| [[NCI-H2347 (line)]] | alt | 54.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.7) |
| [[SNU-423 (line)]] | alt | 74.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -23.4) |
| [[SW 900 (line)]] | alt | 55.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.377× (z -12.2) |
| [[SW480 (line)]] | alt | 119 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -14.2) |
| [[LoVo (line)]] | wt | 113 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -20.0) |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.350× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 84.3 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.334× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 75.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -14.2) |
| [[A549 (line)]] | wt | 133 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.460× (z -12.6) |
| [[HT-29 (line)]] | alt | 107 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.277× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 73.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -14.2) |
| [[J82 (line)]] | alt | 83.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -10.4) |
| [[LS 180 (line)]] | wt | 148 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 46.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 73.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -17.0) |
| [[PANC-1 (line)]] | alt | 58.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -15.0) |
| [[RKO (line)]] | wt | 89.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -19.3) |
| [[SHP-77 (line)]] | alt | 83.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.8) |
| [[A498 (line)]] | wt | 98.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -10.3) |
| [[BT-474 (line)]] | alt | 90.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.1) |
| [[C-33 A (line)]] | alt | 88.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 116 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -17.1) |
| [[KATO III (line)]] | alt | 118 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 75.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.244× (z -14.6) |
| [[SW48 (line)]] | wt | 91.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.315× (z -9.6) |
| [[A-427 (line)]] | wt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -9.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 79.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -17.7) |
| [[CHP-212 (line)]] | wt | 82.3 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.145× (z -10.3) |
| [[H4 (line)]] | wt | 58.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -10.6) |
| [[HCT15 (line)]] | alt | 119 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.394× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 63.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.0) |
| [[Hs 766T (line)]] | wt | 84.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.5) |
| [[SNU-1 (line)]] | wt | 88.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -16.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 89.1 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0725× (z -9.1) |
| [[AN3 CA (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | +0.69 | +0.71 / +0.37 | both halves | 9e-05 |  |
| [[LPCAT4]] | +0.67 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[BRAT1]] | +0.66 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[LRFN3]] | +0.65 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[TMEM120B]] | +0.64 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[ABHD17A]] | +0.64 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[TNK2]] | +0.63 | +0.60 / +0.32 | both halves | 2e-04 |  |
| [[ACTR5]] | +0.63 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[ABCA2]] | +0.62 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[GRAMD4]] | +0.62 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[XYLT2]] | +0.61 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[FHIP1B]] | +0.61 | +0.62 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12A-AS2]] | -0.67 | -0.70 / -0.29 | both halves | 2e-04 |  |
| [[RIPK2-DT]] | -0.67 | -0.74 / -0.41 | both halves | 4e-05 |  |
| [[PCNX4-DT]] | -0.65 | -0.70 / -0.25 | both halves | 4e-04 |  |
| [[TTC6]] | -0.65 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[NQO1-DT]] | -0.65 | -0.68 / -0.32 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.65 | -0.63 / -0.30 | both halves | 2e-04 |  |
| [[KANSL1L]] | -0.64 | -0.62 / -0.36 | both halves | 9e-05 |  |
| [[ZCWPW1]] | -0.64 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[CCDC90B-AS1]] | -0.63 | -0.65 / -0.24 | both halves | 4e-04 |  |
| [[NEK11]] | -0.63 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[GALNT7-DT]] | -0.63 | -0.63 / -0.24 | both halves | 5e-04 |  |
| [[EFCAB2]] | -0.63 | -0.62 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC17]] | B | LRRC17 activity raises MINK1's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.27× lower at baseline in the lines without LRRC17 | 0.026 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (8.4, 12.2); signed map (-41.6, -4.9). **Vector** length 109, 32.4% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.2 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | -0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.0 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.9 | -12.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -20.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -2.6 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -0.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | misshapen like kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,833,340-4,898,061 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B55, MINK, ZC3, MAP4K6, YSK2 |
| Gene groups (HGNC) | STRIPAK complex; Armadillo like helical domain containing; MAP4K family (GCK-IV subfamily) |
| Reactome | 4 pathways, smallest: Oxidative Stress Induced Senescence; Cellular Senescence; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4C8](https://www.uniprot.org/uniprotkb/Q8N4C8) (Misshapen-like kinase 1):

> Serine/threonine kinase which acts as a negative regulator of Ras-related Rap2-mediated signal transduction to control neuronal structure and AMPA receptor trafficking. Required for normal synaptic density, dendrite complexity, as well as surface AMPA receptor expression in hippocampal neurons (By similarity). Can activate the JNK and MAPK14/p38 pathways and mediates stimulation of the stress-activated protein kinase MAPK14/p38 MAPK downstream of the Raf/ERK pathway. Phosphorylates TANC1 upon …

**Summary**, from NCBI Gene [50488](https://www.ncbi.nlm.nih.gov/gene/50488):

> This gene encodes a serine/threonine kinase belonging to the germinal center kinase (GCK) family. The protein is structurally similar to the kinases that are related to NIK and may belong to a distinct subfamily of NIK-related kinases within the GCK family. Studies of the mouse homolog indicate an up-regulation of expression in the course of postnatal mouse cerebral development and activation of the cJun N-terminal kinase (JNK) and the p38 pathways. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:17565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17565) · Entrez [50488](https://www.ncbi.nlm.nih.gov/gene/50488) · UniProt [Q8N4C8](https://www.uniprot.org/uniprotkb/Q8N4C8) · Ensembl [ENSG00000141503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141503)

## Data

Gene col 6530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6530); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6530]; `tensor/DDL_lfc|DDL_z.npy` [6530]; `embed/gene_vectors.npy` [6530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6530 or target_col == 6530). Every well: [[MINK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MINK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

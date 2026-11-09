---
symbol: "POMP"
type: "gene"
col: 5397
ensembl_id: "ENSG00000132963"
name: "proteasome maturation protein"
location: "13q12.3"
module: 72
arm: "+"
pooled_cpm: 131.4
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# POMP

*proteasome maturation protein* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.44× (z +9.4, q 4e-18, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.559× (z -4.7, q 0.001, down in 39 of 50 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.636× (z -4.4, q 0.003, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBR1]] (+0.64, fdr 1e-05), [[DGKG]] (+0.59, fdr 1e-05), [[DAP3]] (+0.58, fdr 3e-05); moves opposite to [[SIAH1]] (-0.54, fdr 2e-05), [[FOXJ2]] (-0.54, fdr 3e-05), [[HDGF]] (-0.53, fdr 2e-04).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC46A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.44×** | +9.4 | 4e-18 | 48/48 (HT-29, COLO 205, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.25×** | +8.5 | 6e-15 | 48/48 (COLO 205, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.14×** | +8.0 | 3e-13 | 46/49 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.92×** | +6.8 | 1e-09 | 46/48 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.96×** | +6.7 | 3e-09 | 48/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.90×** | +6.5 | 8e-09 | 37/44 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +5.9 | 3e-07 | 42/48 (C32, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.57×** | +4.6 | 3e-04 | 39/47 (LoVo, HCT15, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.53×** | +4.5 | 5e-04 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.47×** | +3.7 | 0.011 | 29/45 (SNU-423, J82, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~90% of this change | **1.40×** | +3.5 | 0.020 | 31/48 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.38×** | +3.4 | 0.029 | 32/48 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.35×** | +3.1 | 0.073 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.98× | +3.0 | 0.11 | 28/49 (RPMI-7951, COLO 205, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.559×** | -4.7 | 0.001 | 39/50 (NCI-H23, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.636×** | -4.4 | 0.003 | 44/48 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.741×** | -4.3 | 0.003 | 44/48 (NCI-H23, C32, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.693×** | -3.8 | 0.019 | 31/48 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.471×** | -3.3 | 0.100 | 34/50 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.721×** | -3.3 | 0.100 | 24/47 (NCI-H23, C32, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.742× | -3.1 | 0.15 | 34/48 (HT-29, NCI-H2030, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.727× | -3.1 | 0.15 | 32/48 (Panc 03.27, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 308 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.65× (z +11.8) | — |
| [[C32 (line)]] | wt | 146 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.40× (z +9.5) | [[Cobimetinib (drug)]] 0.5 µM 0.328× (z -8.6) |
| [[COLO 205 (line)]] | alt | 194 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.62× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 83.9 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.78× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 143 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.81× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 123 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[KATO III (line)]] | alt | 146 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.64× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 112 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.97× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[SW480 (line)]] | alt | 124 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.06× (z +8.6) | — |
| [[A549 (line)]] | wt | 93.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[AN3 CA (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 76.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.18× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 94.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.20× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[NCI-H1573 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.15× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H1792 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[NCI-H23 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.274× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[SW48 (line)]] | wt | 123 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +8.6) | — |
| [[A-172 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 201 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 200 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 194 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 89.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBR1]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[DGKG]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[DAP3]] | +0.58 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[VMP1]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[BIN3]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[BMERB1]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PSMB1]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 | pathway: Proteasome assembly; STRING 999 |
| [[PSMB4]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 | pathway: Proteasome assembly; STRING 999 |
| [[TSPAN9]] | +0.55 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[SNX29]] | +0.55 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[GSTO1]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[BIRC6]] | +0.54 | +0.46 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIAH1]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[FOXJ2]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[HDGF]] | -0.53 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[SORBS3]] | -0.53 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[HACD2]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[TAPT1]] | -0.51 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[TMEM237]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PATL1]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[OGFRL1]] | -0.50 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TMEM64]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[NFIX]] | -0.50 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[ATXN2L]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC46A3]] | B | SLC46A3 activity raises POMP's level | lines that do not express SLC46A3 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without SLC46A3 | 0.035 | ⚠ within organs, on part of the lines; also absent: PLCE1, CLCF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.1, -24.3); signed map (2.6, 26.8). **Vector** length 87.7, 36.6% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.8 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +8.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.7 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.6 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | -3.4 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome maturation protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:28,659,065-28,678,959 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC014, UMP1; previously C13orf12 |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y244](https://www.uniprot.org/uniprotkb/Q9Y244) (Proteasome maturation protein):

> Molecular chaperone essential for the assembly of standard proteasomes and immunoproteasomes. Degraded after completion of proteasome maturation. Mediates the association of 20S preproteasome with the endoplasmic reticulum.

**Summary**, from NCBI Gene [51371](https://www.ncbi.nlm.nih.gov/gene/51371):

> The protein encoded by this gene is a molecular chaperone that binds 20S preproteasome components and is essential for 20S proteasome formation. The 20S proteasome is the proteolytically active component of the 26S proteasome complex. The encoded protein is degraded before the maturation of the 20S proteasome is complete. A variant in the 5' UTR of this gene has been associated with KLICK syndrome, a rare skin disorder.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:20330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20330) · Entrez [51371](https://www.ncbi.nlm.nih.gov/gene/51371) · UniProt [Q9Y244](https://www.uniprot.org/uniprotkb/Q9Y244) · Ensembl [ENSG00000132963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132963)

## Data

Gene col 5397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5397); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5397]; `tensor/DDL_lfc|DDL_z.npy` [5397]; `embed/gene_vectors.npy` [5397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5397 or target_col == 5397). Every well: [[POMP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POMP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

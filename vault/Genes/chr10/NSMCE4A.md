---
symbol: "NSMCE4A"
type: "gene"
col: 2868
ensembl_id: "ENSG00000107672"
name: "NSE4A component of SMC5/6 complex"
location: "10q26.13"
module: 6
arm: "+"
pooled_cpm: 12.49
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# NSMCE4A

*NSE4A component of SMC5/6 complex* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.91× (z +10.8, q 2e-24, up in 13 of 23 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.32× (z +4.9, q 1e-04, up in 16 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.754× (z -6.8, q 5e-09, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~24% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.675× (z -6.7, q 5e-09, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP78]] (+0.67, fdr 7e-06), [[HAUS1]] (+0.64, fdr 7e-06), [[TADA2A]] (+0.63, fdr 1e-05); moves opposite to [[RSL1D1-DT]] (-0.69, fdr 9e-06), [[LAMTOR3]] (-0.63, fdr 1e-05), [[CD63]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SYTL4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.91×** | +10.8 | 2e-24 | 13/23 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.76×** | +9.8 | 3e-20 | 23/37 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +7.2 | 1e-10 | 23/40 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +6.1 | 2e-07 | 21/40 (NCI-H2347, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.6 | 3e-06 | 17/41 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +4.9 | 1e-04 | 16/47 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.33×** | +4.6 | 3e-04 | 13/30 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.015 | 9/44 (A498, SW 900, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.22×** | +3.5 | 0.029 | 12/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.047 | 14/47 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.064 | 1/45 (Panc 03.27) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.754×** | -6.8 | 5e-09 | 28/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.675×** | -6.7 | 5e-09 | 24/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -5.3 | 2e-05 | 19/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.545×** | -5.1 | 4e-05 | 16/46 (NCI-H23, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -5.0 | 7e-05 | 19/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.749×** | -4.9 | 7e-05 | 20/45 (Panc 03.27, HCT15, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.3 | 0.001 | 15/45 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.778×** | -4.3 | 0.001 | 16/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.784×** | -4.2 | 0.002 | 14/47 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.790×** | -4.0 | 0.003 | 10/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.801×** | -3.8 | 0.008 | 17/46 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -3.2 | 0.073 | 12/46 (PANC-1, A498, …) | top dose only |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.829×** | -3.1 | 0.084 | 6/47 (SNU-1, AsPC-1, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.696×** | -3.1 | 0.084 | 9/36 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.696×** | -3.1 | 0.084 | 6/43 (NCI-H460, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.8 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.94× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 18.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.396× (z -8.9) |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 16.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.376× (z -9.1) |
| [[A-172 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP78]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[HAUS1]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TADA2A]] | +0.63 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[TUBGCP3]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[NUP93]] | +0.62 | +0.49 / +0.67 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[PRIM1]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CSE1L]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[CCDC150]] | +0.58 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[RNASEH2B]] | +0.58 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SKA1]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[HEATR3]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CENPU]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSL1D1-DT]] | -0.69 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[LAMTOR3]] | -0.63 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CD63]] | -0.60 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.58 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ATP6V1D]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[SMIM4]] | -0.56 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[ATP6V1G1]] | -0.56 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[PLA2G12B]] | -0.56 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[DAZAP2]] | -0.55 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[CDKL3]] | -0.54 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[ATP6V0C]] | -0.53 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[FAM209A]] | -0.52 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYTL4]] | B | SYTL4 activity lowers NSMCE4A's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.19× higher at baseline in the lines without SYTL4 | 0.061 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-30.9, -43.0); signed map (-34.5, -42.2). **Vector** length 63.2, 9.69% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.6 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.9 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +2.0 | +9.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.1 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.6 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.6 | -4.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.8 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -5.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | NSE4A component of SMC5/6 complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:121,957,091-121,975,217 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20003, bA500G22.3, NSE4A; previously C10orf86 |
| Gene groups (HGNC) | SMC5/6 complex |
| Reactome | 3 pathways, smallest: SUMOylation of DNA damage response and repair proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXX6](https://www.uniprot.org/uniprotkb/Q9NXX6) (Non-structural maintenance of chromosomes element 4 homolog A):

> Component of the SMC5-SMC6 complex, a complex involved in DNA double-strand breaks by homologous recombination. The complex may promote sister chromatid homologous recombination by recruiting the SMC1-SMC3 cohesin complex to double-strand breaks. The complex is required for telomere maintenance via recombination in ALT (alternative lengthening of telomeres) cell lines and mediates sumoylation of shelterin complex (telosome) components which is proposed to lead to shelterin complex disassembly …

**Summary**, from NCBI Gene [54780](https://www.ncbi.nlm.nih.gov/gene/54780):

> Involved in DNA damage response. Located in nucleoplasm. Part of Smc5-Smc6 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25935) · Entrez [54780](https://www.ncbi.nlm.nih.gov/gene/54780) · UniProt [Q9NXX6](https://www.uniprot.org/uniprotkb/Q9NXX6) · Ensembl [ENSG00000107672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107672)

## Data

Gene col 2868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2868); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2868]; `tensor/DDL_lfc|DDL_z.npy` [2868]; `embed/gene_vectors.npy` [2868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2868 or target_col == 2868). Every well: [[NSMCE4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSMCE4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

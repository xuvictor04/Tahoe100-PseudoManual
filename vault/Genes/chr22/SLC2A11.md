---
symbol: "SLC2A11"
type: "gene"
col: 5450
ensembl_id: "ENSG00000133460"
name: "solute carrier family 2 member 11"
location: "22q11.23"
module: 51
arm: "+"
pooled_cpm: 11.14
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SLC2A11

*solute carrier family 2 member 11* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.18× (z +5.4, q 4e-05, up in 15 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.72× (z +5.0, q 1e-04, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.322× (z -10.6, q 1e-23, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP12]] (+0.61, fdr 3e-05), [[ATP6V0D1-DT]] (+0.60, fdr 1e-05), [[BMS1P1-1]] (+0.58, fdr 3e-05); moves opposite to [[CLIC1]] (-0.53, fdr 1e-05), [[RP2]] (-0.50, fdr 4e-05), [[ANO6]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF594-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +5.4 | 4e-05 | 15/46 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.72×** | +5.0 | 1e-04 | 26/45 (A-427, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.9 | 2e-04 | 12/20 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.7 | 5e-04 | 23/45 (LoVo, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.2 | 0.003 | 19/35 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.8 | 0.013 | 15/36 (HCT15, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.016 | 20/45 (NCI-H2030, LS 180, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.017 | 12/45 (Panc 03.27, LS 180, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.043 | 12/43 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.052 | 13/46 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.3 | 0.052 | 17/39 (LS 180, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.58× | +3.1 | 0.10 | 12/39 (J82, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.38× | +3.0 | 0.11 | 9/43 (HEC-1-A, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.322×** | -10.6 | 1e-23 | 41/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -8.5 | 7e-15 | 35/43 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.439×** | -7.7 | 2e-12 | 33/45 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -7.1 | 2e-10 | 33/44 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.598×** | -6.8 | 9e-10 | 30/44 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.558×** | -5.5 | 4e-06 | 26/42 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -5.4 | 6e-06 | 29/44 (A-427, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.341×** | -5.3 | 9e-06 | 23/41 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.630×** | -4.2 | 0.002 | 21/43 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.642×** | -4.2 | 0.002 | 21/45 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.692×** | -3.5 | 0.027 | 17/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.702×** | -3.3 | 0.041 | 19/44 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.719×** | -3.1 | 0.082 | 14/43 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.087 | 14/46 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.717×** | -3.0 | 0.097 | 17/41 (NCI-H23, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 23.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.54× (z +8.9) ⚠ position not correctable | [[Niclosamide (olamine) (drug)]] 5 µM 0.0880× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~24% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.183× (z -10.1) |
| [[A-427 (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.185× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 7.71 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.179× (z -8.9) |
| [[A-172 (line)]] | wt | 3.32 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.05 µM 0.0599× (z -9.1) |
| [[A498 (line)]] | wt | 8.79 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0902× (z -8.8) |
| [[J82 (line)]] | alt | 5.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0239× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0602× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 13.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -8.7) |
| [[A549 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP12]] | +0.61 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[ATP6V0D1-DT]] | +0.60 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[BMS1P1-1]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[TLK1]] | +0.57 | +0.57 / +0.27 | both halves | 3e-04 |  |
| [[PUM2]] | +0.56 | +0.27 / +0.33 | both halves | 3e-04 |  |
| [[ZNF32]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[URGCP]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[D2HGDH]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[SLTM]] | +0.54 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[DHFR2]] | +0.54 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RBM33]] | +0.54 | +0.53 / +0.23 | both halves | 5e-04 |  |
| [[RBM27]] | +0.53 | +0.46 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIC1]] | -0.53 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[RP2]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ANO6]] | -0.49 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ARPC2]] | -0.44 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[RECQL]] | -0.43 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[BZW1]] | -0.43 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[EHD4]] | -0.42 | -0.52 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594-DT]] | B | ZNF594-DT activity raises SLC2A11's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without ZNF594-DT | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[ZBED3]] | C | ZBED3 activity raises SLC2A11's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without ZBED3 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.384). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-29.5, 22.8); signed map (18.2, -43.7). **Vector** length 54.1, 8.47% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.4 | -6.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.3 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -7.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:23,856,703-23,886,312 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GLUT11 |
| Gene groups (HGNC) | Solute carrier family 2 |
| Reactome | 3 pathways, smallest: Cellular hexose transport; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYW1](https://www.uniprot.org/uniprotkb/Q9BYW1) (Solute carrier family 2, facilitated glucose transporter member 11):

> Facilitative glucose transporter.

**Summary**, from NCBI Gene [66035](https://www.ncbi.nlm.nih.gov/gene/66035):

> This gene belongs to a family of proteins that mediate the transport of sugars across the cell membrane. The encoded protein transports glucose and fructose. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:14239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14239) · Entrez [66035](https://www.ncbi.nlm.nih.gov/gene/66035) · UniProt [Q9BYW1](https://www.uniprot.org/uniprotkb/Q9BYW1) · Ensembl [ENSG00000133460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133460)

## Data

Gene col 5450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5450); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5450]; `tensor/DDL_lfc|DDL_z.npy` [5450]; `embed/gene_vectors.npy` [5450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5450 or target_col == 5450). Every well: [[SLC2A11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

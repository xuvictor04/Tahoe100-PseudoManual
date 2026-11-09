---
symbol: "SAMD11"
type: "gene"
col: 11932
ensembl_id: "ENSG00000187634"
name: "sterile alpha motif domain containing 11"
location: "1p36.33"
module: 10
arm: "+"
pooled_cpm: 5.96
n_lines_expressing: 37
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 16
direction_downstream: 18
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SAMD11

*sterile alpha motif domain containing 11* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.36× (z +5.7, q 6e-06, up in 4 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 2.09× (z +4.9, q 1e-04, up in 18 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.348× (z -6.9, q 3e-09, down in 25 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01013]] (+0.64, fdr 7e-06), [[PRRT2]] (+0.62, fdr 7e-06), [[UNC5C]] (+0.61, fdr 1e-05); moves opposite to [[APPL2]] (-0.47, fdr 3e-05), [[TMEM154]] (-0.47, fdr 1e-04), [[CREG2]] (-0.44, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[ELFN1]] → it (grade B ⚠); 18 go from it, the strongest it → [[PRAME]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +5.7 | 6e-06 | 4/10 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.09×** | +4.9 | 1e-04 | 18/31 (PANC-1, RKO, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **2.06×** | +4.9 | 1e-04 | 16/35 (NCI-H23, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +4.9 | 1e-04 | 9/19 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.82×** | +4.8 | 2e-04 | 17/33 (RKO, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **2.04×** | +4.7 | 2e-04 | 22/32 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **2.02×** | +4.7 | 2e-04 | 17/29 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.66×** | +4.3 | 0.001 | 17/33 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.80×** | +4.1 | 0.003 | 15/32 (PANC-1, A-427, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.009 | 18/34 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.02×** | +3.4 | 0.029 | 10/29 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.080 | 13/32 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | 1.55× | +3.0 | 0.10 | 14/34 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.54× | +3.0 | 0.10 | 14/34 (RKO, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.348×** | -6.9 | 3e-09 | 25/31 (AN3 CA, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.384×** | -6.6 | 9e-09 | 25/34 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.450×** | -5.5 | 6e-06 | 20/32 (A-427, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -5.5 | 6e-06 | 20/27 (C-33 A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.456×** | -5.4 | 6e-06 | 21/34 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.457×** | -5.4 | 6e-06 | 23/33 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.464×** | -5.3 | 9e-06 | 25/32 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.515×** | -4.6 | 3e-04 | 16/34 (MIA PaCa-2, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.529×** | -4.4 | 6e-04 | 19/34 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.530×** | -4.4 | 6e-04 | 16/26 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.644×** | -4.3 | 8e-04 | 19/30 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.262×** | -4.2 | 0.001 | 15/28 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.545×** | -4.2 | 0.001 | 17/30 (SNU-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.570×** | -3.9 | 0.004 | 18/34 (A-172, SHP-77, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.314×** | -3.6 | 0.010 | 16/32 (C-33 A, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.693×** | -3.6 | 0.012 | 14/33 (H4, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.605×** | -3.5 | 0.017 | 16/32 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.708×** | -3.4 | 0.023 | 13/34 (AN3 CA, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 34.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0400× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 4.23 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.81× (z +11.0) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.0547× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0617× (z -8.5) |
| [[SHP-77 (line)]] | alt | 21.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -8.6) ⚠ cell-cycle shift, explains ~95% of this change |
| [[A-172 (line)]] | wt | 27.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0858× (z -10.3) |
| [[A-427 (line)]] | wt | 16.6 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0727× (z -12.0) ⚠ cell-cycle shift, explains ~11% of this change |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0726× (z -11.2) ⚠ cell-cycle shift, explains ~66% of this change |
| [[H4 (line)]] | wt | 20.4 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0459× (z -10.3) |
| [[HOP62 (line)]] | alt | 5.77 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0739× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -11.3) |
| [[SNU-1 (line)]] | wt | 9.29 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0333× (z -11.0) |
| [[LoVo (line)]] | wt | 5.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 7.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -9.0) |
| [[NCI-H661 (line)]] | alt | 88.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.814 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01013]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[PRRT2]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[UNC5C]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SOX12]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[MXRA8]] | +0.60 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[ID3]] | +0.58 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[NREP]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[COL5A2]] | +0.57 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[LINC02211]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CRB1]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[BEND6]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[OLFML2A]] | +0.52 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APPL2]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TMEM154]] | -0.47 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[CREG2]] | -0.44 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[RABGEF1P3]] | -0.44 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[NBPF8]] | -0.43 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[LAMA1]] | -0.43 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[ZNF215]] | -0.42 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[MAPK13]] | -0.42 | -0.43 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 10, C 6. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN1]] | B | ELFN1 activity raises SAMD11's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without ELFN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[TMEM154]] | B | TMEM154 activity lowers SAMD11's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.66× higher at baseline in the lines without TMEM154 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[CREG2]] | B | CREG2 activity lowers SAMD11's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.93× higher at baseline in the lines without CREG2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[MAP2K1]] | B | MAP2K1 activity lowers SAMD11's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[MAPK13]] | B | MAPK13 activity lowers SAMD11's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 2.48× higher at baseline in the lines without MAPK13 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[MIR99AHG]] | B | MIR99AHG activity raises SAMD11's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.27× lower at baseline in the lines without MIR99AHG | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[PAX2]] | B | PAX2 activity raises SAMD11's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.64× lower at baseline in the lines without PAX2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[SOBP]] | B | SOBP activity raises SAMD11's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without SOBP | 0.079 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[RABGEF1P3]] | B | RABGEF1P3 activity lowers SAMD11's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 5.13× higher at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[MAP2K2]] | B | MAP2K2 activity lowers SAMD11's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ANKS1B]] | C | ANKS1B activity raises SAMD11's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 3.53× lower at baseline in the lines without ANKS1B | 0.003 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3; co-absent with the target |
| [[LNC-LBCS]] | C | LNC-LBCS activity raises SAMD11's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without LNC-LBCS | 0.013 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 11, C 7. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRAME]] | B | SAMD11 activity raises PRAME's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 4.19× lower at baseline in the lines without SAMD11 | 0.017 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[SOX12]] | B | SAMD11 activity raises SOX12's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without SAMD11 | 0.021 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[SOBP]] | B | SAMD11 activity raises SOBP's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 3.79× lower at baseline in the lines without SAMD11 | 0.026 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[MRAS]] | B | SAMD11 activity raises MRAS's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 2.80× lower at baseline in the lines without SAMD11 | 0.037 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[ELFN1]] | B | SAMD11 activity raises ELFN1's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 3.64× lower at baseline in the lines without SAMD11 | 0.060 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[MAZ]] | B | SAMD11 activity raises MAZ's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without SAMD11 | 0.063 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[CRB1]] | B | SAMD11 activity raises CRB1's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 1.93× lower at baseline in the lines without SAMD11 | 0.067 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[PAX2]] | B | SAMD11 activity raises PAX2's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 1.75× lower at baseline in the lines without SAMD11 | 0.086 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[LINC01013]] | B | SAMD11 activity raises LINC01013's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without SAMD11 | 0.088 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[COL5A2]] | B | SAMD11 activity raises COL5A2's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 4.39× lower at baseline in the lines without SAMD11 | 0.094 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[GSE1]] | B | SAMD11 activity raises GSE1's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without SAMD11 | 0.099 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[DCLK2]] | C | SAMD11 activity raises DCLK2's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 6.84× lower at baseline in the lines without SAMD11 | 0.002 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.340). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.1, 26.4); signed map (37.2, -2.9). **Vector** length 70.1, 15.6% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[Trametinib (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.4 | +3.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:923,923-944,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45873 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NU1](https://www.uniprot.org/uniprotkb/Q96NU1) (Sterile alpha motif domain-containing protein 11):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, essential for establishing rod photoreceptor cell identity and function by silencing nonrod gene expression in developing rod photoreceptor cells.

**Summary**, from NCBI Gene [148398](https://www.ncbi.nlm.nih.gov/gene/148398):

> Predicted to enable several functions, including DNA-binding transcription repressor activity, RNA polymerase II-specific; identical protein binding activity; and protein domain specific binding activity. Predicted to be involved in negative regulation of DNA-templated transcription and retinal rod cell development. Predicted to act upstream of or within negative regulation of transcription by RNA polymerase II. Predicted to be part of PRC1 complex. Predicted to be active in nucleus. [provided …

**Accessions** — [HGNC:28706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28706) · Entrez [148398](https://www.ncbi.nlm.nih.gov/gene/148398) · UniProt [Q96NU1](https://www.uniprot.org/uniprotkb/Q96NU1) · Ensembl [ENSG00000187634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187634)

## Data

Gene col 11932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11932); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11932]; `tensor/DDL_lfc|DDL_z.npy` [11932]; `embed/gene_vectors.npy` [11932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11932 or target_col == 11932). Every well: [[SAMD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

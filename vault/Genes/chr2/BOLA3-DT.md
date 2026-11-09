---
symbol: "BOLA3-DT"
type: "gene"
col: 13457
ensembl_id: "ENSG00000225439"
name: "BOLA3 divergent transcript"
location: "2p13.1"
module: 128
arm: "+"
pooled_cpm: 2.25
n_lines_expressing: 40
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 13
direction_downstream: 23
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# BOLA3-DT

*BOLA3 divergent transcript* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.90× (z +8.7, q 3e-15, up in 13 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.385× (z -9.0, q 1e-16, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC14L4]] (+0.60, fdr 4e-05), [[C3orf18]] (+0.58, fdr 4e-05), [[BARX1]] (+0.55, fdr 2e-04); moves opposite to [[POU5F1B]] (-0.45, fdr 1e-04), [[SIDT1]] (-0.42, fdr 4e-04), [[PTPRB]] (-0.41, fdr 1e-03, ⚠ one half only (not replicated)), [[ATP10B]] (-0.41, fdr 6e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SIDT1]] → it (grade B ⚠); 23 go from it, the strongest it → [[KIF3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +8.7 | 3e-15 | 13/33 (A-172, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +8.3 | 2e-14 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.59×** | +4.5 | 0.002 | 7/24 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +4.0 | 0.010 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +3.6 | 0.031 | 1/9 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.031 | 2/29 (HepG2/C3A, NCI-H23) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.40× | +3.1 | 0.15 | 0/16 | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.38× | +3.1 | 0.15 | 0/28 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.385×** | -9.0 | 1e-16 | 22/36 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.564×** | -7.6 | 7e-12 | 16/20 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.468×** | -7.2 | 1e-10 | 16/31 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.478×** | -7.0 | 5e-10 | 13/21 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.495×** | -6.4 | 2e-08 | 14/28 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -5.6 | 2e-06 | 14/36 (A-172, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -5.4 | 5e-06 | 12/20 (PANC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.632×** | -4.3 | 0.001 | 15/34 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.637×** | -4.2 | 0.001 | 5/35 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.644×** | -4.1 | 0.002 | 13/36 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -3.5 | 0.027 | 12/28 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.517×** | -3.3 | 0.054 | 3/27 (CHP-212, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.709×** | -3.2 | 0.055 | 5/29 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.713×** | -3.2 | 0.062 | 6/27 (LOX-IMVI, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.718×** | -3.1 | 0.071 | 9/34 (A-172, C-33 A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.10 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0308× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0468× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 4.65 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -17.5) |
| [[HOP62 (line)]] | alt | 3.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 5.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -8.9) |
| [[SW480 (line)]] | alt | 2.48 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -11.0) |
| [[A-172 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.684 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.683 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.775 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.756 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.861 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.688 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.642 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC14L4]] | +0.60 | +0.58 / +0.40 | both halves | 4e-05 | **novel candidate** |
| [[C3orf18]] | +0.58 | +0.57 / +0.40 | both halves | 4e-05 |  |
| [[BARX1]] | +0.55 | +0.61 / +0.29 | both halves | 2e-04 |  |
| [[TBX1]] | +0.54 | +0.55 / +0.37 | both halves | 7e-05 |  |
| [[CYS1]] | +0.54 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[ZFP69]] | +0.54 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[ARHGEF25]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[RNF212]] | +0.53 | +0.50 / +0.30 | both halves | 2e-04 |  |
| [[BASP1-AS1]] | +0.50 | +0.52 / +0.31 | both halves | 2e-04 |  |
| [[ZNF677]] | +0.49 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[LRRC63]] | +0.49 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[SEPTIN5]] | +0.48 | +0.53 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU5F1B]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[SIDT1]] | -0.42 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[PTPRB]] | -0.41 | -0.54 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[ATP10B]] | -0.41 | -0.48 / -0.22 | both halves | 6e-04 |  |
| [[MUC5B]] | -0.41 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[SRSF9]] ⚠ | -0.40 | -0.38 / -0.25 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[DENND1A]] | -0.40 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[CLEC16A]] | -0.39 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[FAM3D]] | -0.38 | -0.44 / -0.20 | both halves | 7e-04 |  |
| [[TMEM45B]] | -0.38 | -0.51 / -0.21 | both halves | 7e-04 |  |
| [[MLLT6]] | -0.38 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[PKP4]] | -0.38 | -0.32 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIDT1]] | B | SIDT1 activity lowers BOLA3-DT's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.11× higher at baseline in the lines without SIDT1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[PTPRB]] | B | PTPRB activity lowers BOLA3-DT's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.73× higher at baseline in the lines without PTPRB | 0.011 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[MUC5B]] | B | MUC5B activity lowers BOLA3-DT's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.84× higher at baseline in the lines without MUC5B | 0.013 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[C3orf18]] | B | C3orf18 activity raises BOLA3-DT's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without C3orf18 | 0.014 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity lowers BOLA3-DT's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 1.59× higher at baseline in the lines without POU5F1B | 0.047 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[FAM3D]] | B | FAM3D activity lowers BOLA3-DT's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 1.97× higher at baseline in the lines without FAM3D | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[SEC14L4]] | B | SEC14L4 activity raises BOLA3-DT's level | lines that do not express SEC14L4 (29) vs lines expressing it (21) | 1.44× lower at baseline in the lines without SEC14L4 | 0.060 | ⚠ within organs, on part of the lines; also absent: WT1-AS, ACP7, PLTP |
| [[PRAME]] | B | PRAME activity raises BOLA3-DT's level | lines that do not express PRAME (25) vs lines expressing it (25) | 1.68× lower at baseline in the lines without PRAME | 0.064 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[MEX3A]] | B | MEX3A activity raises BOLA3-DT's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without MEX3A | 0.065 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[SEPTIN5]] | B | SEPTIN5 activity raises BOLA3-DT's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.88× lower at baseline in the lines without SEPTIN5 | 0.069 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[ATP10B]] | B | ATP10B activity lowers BOLA3-DT's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 2.03× higher at baseline in the lines without ATP10B | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[WT1-AS]] | B | WT1-AS activity raises BOLA3-DT's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.62× lower at baseline in the lines without WT1-AS | 0.071 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF3C]] | B | BOLA3-DT activity raises KIF3C's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.78× lower at baseline in the lines without BOLA3-DT | 0.002 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[C3orf18]] | B | BOLA3-DT activity raises C3orf18's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without BOLA3-DT | 0.003 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[TMEM45B]] | B | BOLA3-DT activity lowers TMEM45B's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 10.46× higher at baseline in the lines without BOLA3-DT | 0.004 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[SIDT1]] | B | BOLA3-DT activity lowers SIDT1's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 6.68× higher at baseline in the lines without BOLA3-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[CHST14]] | B | BOLA3-DT activity raises CHST14's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.72× lower at baseline in the lines without BOLA3-DT | 0.009 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[ZIM2-AS1]] | B | BOLA3-DT activity raises ZIM2-AS1's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without BOLA3-DT | 0.013 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[ZNF2]] | B | BOLA3-DT activity raises ZNF2's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.48× lower at baseline in the lines without BOLA3-DT | 0.016 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[RNF220]] | B | BOLA3-DT activity raises RNF220's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without BOLA3-DT | 0.019 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[FAM161A]] | B | BOLA3-DT activity raises FAM161A's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.21× lower at baseline in the lines without BOLA3-DT | 0.030 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[DOK1]] | B | BOLA3-DT activity raises DOK1's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without BOLA3-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[EDRF1]] | B | BOLA3-DT activity raises EDRF1's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.33× lower at baseline in the lines without BOLA3-DT | 0.034 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[ATP10B]] | B | BOLA3-DT activity lowers ATP10B's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 4.80× higher at baseline in the lines without BOLA3-DT | 0.038 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.5, 40.7); signed map (22.6, 26.4). **Vector** length 36.3, 4.66% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.9 | +8.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.0 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.7 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +8.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +0.8 | +0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.7 | +0.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.0 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -1.6 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.7 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.6 | -3.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.6 | -2.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.6 | -0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | BOLA3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p13.1 — chr2:74,148,007-74,151,952 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously BOLA3-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42922) · Entrez [100507171](https://www.ncbi.nlm.nih.gov/gene/100507171) · Ensembl [ENSG00000225439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225439)

## Data

Gene col 13457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13457); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13457]; `tensor/DDL_lfc|DDL_z.npy` [13457]; `embed/gene_vectors.npy` [13457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13457 or target_col == 13457). Every well: [[BOLA3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BOLA3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

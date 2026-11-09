---
symbol: "DLK2"
type: "gene"
col: 10113
ensembl_id: "ENSG00000171462"
name: "delta like non-canonical Notch ligand 2"
location: "6p21.1"
module: 128
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 37
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# DLK2

*delta like non-canonical Notch ligand 2* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.26× (z +6.3, q 1e-07, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.495× (z -5.6, q 8e-06, down in 12 of 25 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYS1]] (+0.60, fdr 3e-05), [[PAQR7]] (+0.59, fdr 1e-05), [[UPK1A-AS1]] (+0.57, fdr 3e-05); moves opposite to [[LINC02474]] (-0.49, fdr 4e-05), [[TRIM2]] (-0.47, fdr 2e-04), [[UBAC2]] (-0.46, fdr 1e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PDZD4]] → it (grade B ⚠); 3 go from it, the strongest it → [[FKBP1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +6.3 | 1e-07 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.2 | 0.007 | 2/7 (PANC-1, NCI-H23) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.48× | +3.2 | 0.27 | 1/9 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | 1.47× | +3.0 | 0.33 | 2/25 (SNU-423, A-172) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.495×** | -5.6 | 8e-06 | 12/25 (LOX-IMVI, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.270×** | -5.5 | 8e-06 | 15/25 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.504×** | -5.5 | 8e-06 | 12/28 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.533×** | -5.0 | 6e-05 | 15/29 (A-427, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.533×** | -5.0 | 6e-05 | 12/28 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.501×** | -4.9 | 8e-05 | 9/19 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.658×** | -4.7 | 2e-04 | 16/21 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.556×** | -4.7 | 2e-04 | 7/19 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.330×** | -4.6 | 2e-04 | 11/15 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.559×** | -4.6 | 2e-04 | 11/24 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.591×** | -4.2 | 0.001 | 15/31 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.641×** | -3.5 | 0.018 | 12/32 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.660×** | -3.3 | 0.040 | 11/33 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -3.2 | 0.057 | 11/27 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.663×** | -3.1 | 0.062 | 10/28 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.04 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0530× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 5.83 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0894× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0583× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H2347 (line)]] | alt | 2.80 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0387× (z -9.9) |
| [[A-172 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.166 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.895 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.809 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.735 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.615 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 0.863 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.636 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.588 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYS1]] | +0.60 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[PAQR7]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[UPK1A-AS1]] | +0.57 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[ARID3A]] | +0.56 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[RNF220]] | +0.54 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[TRIM36]] | +0.54 | +0.36 / +0.45 | both halves | 9e-05 |  |
| [[LRFN4]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[PDZD4]] | +0.52 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[GLIS2]] | +0.52 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[OVOL1]] | +0.51 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[PDLIM2]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[NOG]] | +0.51 | +0.39 / +0.59 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02474]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TRIM2]] | -0.47 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[UBAC2]] | -0.46 | -0.32 / -0.56 | both halves | 1e-04 |  |
| [[XRCC5]] | -0.46 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[LAS1L]] | -0.45 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[GALNT5]] | -0.45 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[API5]] | -0.45 | -0.22 / -0.61 | both halves | 6e-04 |  |
| [[CEP20]] | -0.44 | -0.20 / -0.56 | both halves | 7e-04 |  |
| [[AKR1B10]] | -0.44 | -0.41 / -0.27 | both halves | 3e-04 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[BANF1]] | -0.44 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[MRPL42]] | -0.44 | -0.24 / -0.59 | both halves | 4e-04 |  |
| [[EFTUD2]] | -0.44 | -0.20 / -0.58 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TMX3]] | -0.43 | -0.21 / -0.60 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD4]] | B | PDZD4 activity raises DLK2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without PDZD4 | 0.030 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[SLC12A8]] | B | SLC12A8 activity lowers DLK2's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 1.91× higher at baseline in the lines without SLC12A8 | 0.033 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[OVOL1]] | B | OVOL1 activity lowers DLK2's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.80× higher at baseline in the lines without OVOL1 | 0.047 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[PBX1]] | B | PBX1 activity lowers DLK2's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 1.50× higher at baseline in the lines without PBX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[CYS1]] | C | CYS1 activity raises DLK2's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.82× lower at baseline in the lines without CYS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP1B]] | B | DLK2 activity raises FKBP1B's level | lines that do not express DLK2 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without DLK2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ETNK2, CHROMR, DUSP15 |
| [[TAGAP-AS1]] | B | DLK2 activity raises TAGAP-AS1's level | lines that do not express DLK2 (13) vs lines expressing it (37) | 1.52× lower at baseline in the lines without DLK2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ETNK2, CHROMR, DUSP15 |
| [[CYS1]] | C | DLK2 activity raises CYS1's level | lines that do not express DLK2 (13) vs lines expressing it (37) | 1.87× lower at baseline in the lines without DLK2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ETNK2, CHROMR, DUSP15; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.6, 40.2); signed map (-28.9, 32.7). **Vector** length 32.9, 4.21% of its response variance represented; |z| ≥ 3 in 655 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.8 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.8 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.8 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +0.7 | +1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.7 | +0.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +0.7 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.7 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -1.8 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.8 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.5 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.8 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | delta like non-canonical Notch ligand 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,450,352-43,456,632 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2487; previously EGFL9 |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UY11](https://www.uniprot.org/uniprotkb/Q6UY11) (Protein delta homolog 2):

> Regulates adipogenesis.

**Summary**, from NCBI Gene [65989](https://www.ncbi.nlm.nih.gov/gene/65989):

> Predicted to enable Notch binding activity. Involved in negative regulation of Notch signaling pathway. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21113) · Entrez [65989](https://www.ncbi.nlm.nih.gov/gene/65989) · UniProt [Q6UY11](https://www.uniprot.org/uniprotkb/Q6UY11) · Ensembl [ENSG00000171462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171462)

## Data

Gene col 10113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10113); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10113]; `tensor/DDL_lfc|DDL_z.npy` [10113]; `embed/gene_vectors.npy` [10113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10113 or target_col == 10113). Every well: [[DLK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

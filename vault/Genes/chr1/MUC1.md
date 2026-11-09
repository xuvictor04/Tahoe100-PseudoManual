---
symbol: "MUC1"
type: "gene"
col: 11688
ensembl_id: "ENSG00000185499"
name: "mucin 1, cell surface associated"
location: "1q22"
module: 8
arm: "+"
pooled_cpm: 19.14
n_lines_expressing: 25
n_dd_up: 16
n_dd_down: 29
n_dd_up_clean: 13
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 46
direction_downstream: 34
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MUC1

*mucin 1, cell surface associated* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.64× (z +7.8, q 3e-12, up in 9 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.96× (z +5.6, q 4e-06, up in 21 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.308× (z -9.5, q 2e-18, down in 23 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZK1IP1]] (+0.72, fdr 7e-06), [[BCL2L15]] (+0.70, fdr 7e-06), [[SECTM1]] (+0.65, fdr 9e-06); moves opposite to [[CAPN2]] (-0.49, fdr 3e-05), [[GPAT3]] (-0.49, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[ELF3-AS1]] → it (grade B ⚠); 34 go from it, the strongest it → [[B4GALT5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +7.8 | 3e-12 | 9/19 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +7.4 | 3e-11 | 6/13 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.96×** | +5.6 | 4e-06 | 21/23 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.02×** | +5.4 | 7e-06 | 15/23 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **2.00×** | +5.4 | 7e-06 | 20/23 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +5.3 | 1e-05 | 4/16 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.78×** | +4.4 | 7e-04 | 15/23 (MIA PaCa-2, AsPC-1, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.48×** | +4.3 | 0.001 | 16/23 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.77×** | +4.3 | 0.001 | 14/23 (AsPC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.58×** | +4.3 | 0.001 | 17/23 (AsPC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.43×** | +4.0 | 0.003 | 14/23 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.16×** | +4.0 | 0.003 | 14/23 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.014 | 14/23 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Capmatinib (drug)]] 5 µM |  | **2.53×** | +3.5 | 0.020 | 9/22 (AsPC-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.91×** | +3.3 | 0.033 | 11/21 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.048 | 12/23 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11688.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.308×** | -9.5 | 2e-18 | 23/23 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.317×** | -9.2 | 7e-18 | 23/23 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.355×** | -7.7 | 3e-12 | 23/23 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.419×** | -7.0 | 4e-10 | 18/21 (COLO 205, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.398×** | -6.8 | 1e-09 | 20/23 (COLO 205, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.453×** | -6.4 | 2e-08 | 23/23 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.464×** | -5.8 | 4e-07 | 22/23 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.488×** | -5.8 | 6e-07 | 17/23 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.468×** | -5.6 | 1e-06 | 18/23 (KATO III, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.538×** | -5.0 | 3e-05 | 18/23 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.560×** | -4.7 | 2e-04 | 18/23 (KATO III, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.690×** | -4.2 | 0.001 | 16/23 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.604×** | -4.1 | 0.002 | 11/23 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.608×** | -4.0 | 0.003 | 18/23 (KATO III, MIA PaCa-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.384×** | -3.6 | 0.012 | 8/22 (SW480, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 172 | 0 | 13 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0237× (z -21.0) |
| [[MIA PaCa-2 (line)]] | alt | 29.7 | 1 (1 ⚠) | 12 (5 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.07× (z +12.0) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0786× (z -17.5) |
| [[COLO 205 (line)]] | alt | 72.5 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0355× (z -22.3) |
| [[CFPAC-1 (line)]] | alt | 155 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.3) |
| [[BT-474 (line)]] | alt | 52.7 | 0 | 6 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.118× (z -10.3) |
| [[A-427 (line)]] | wt | 6.15 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0673× (z -9.5) |
| [[SW480 (line)]] | alt | 8.02 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.124× (z -10.5) |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0561× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 37.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0997× (z -10.9) |
| [[LS 180 (line)]] | wt | 6.38 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 5.07 | 0 | 2 | — | [[Peretinoin (drug)]] 5 µM 0.0625× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -10.4) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -10.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H23 (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -8.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H460 (line)]] | wt | 5.69 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0891× (z -10.6) |
| [[A498 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.52 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZK1IP1]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SECTM1]] | +0.65 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[SCNN1A]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 487 |
| [[ELF3-AS1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[FXYD3]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[UNC5CL]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[FXYD2]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LRG1]] | +0.60 | +0.52 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN2]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[GPAT3]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 8, C 38. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises MUC1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without ELF3-AS1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers MUC1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[SAA4]] | B | SAA4 activity raises MUC1's level | lines that do not express SAA4 (22) vs lines expressing it (28) | 1.74× lower at baseline in the lines without SAA4 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SAA2, SAA1, LMO2 |
| [[CGN]] | B | CGN activity raises MUC1's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.25× lower at baseline in the lines without CGN | 0.049 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[EFNA1]] | B | EFNA1 activity raises MUC1's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 2.47× lower at baseline in the lines without EFNA1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[PROM2]] | B | PROM2 activity raises MUC1's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.00× lower at baseline in the lines without PROM2 | 0.091 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[C11orf52]] | B | C11orf52 activity raises MUC1's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without C11orf52 | 0.092 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[SERPINA3]] | B | SERPINA3 activity raises MUC1's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 2.39× lower at baseline in the lines without SERPINA3 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5 |
| [[PDZK1IP1]] | C | PDZK1IP1 activity raises MUC1's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 4.06× lower at baseline in the lines without PDZK1IP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises MUC1's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 3.85× lower at baseline in the lines without SLC44A4 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises MUC1's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.51× lower at baseline in the lines without LCN2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises MUC1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 4.50× lower at baseline in the lines without MUC5B | 0.008 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 16, C 18. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALT5]] | B | MUC1 activity raises B4GALT5's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without MUC1 | 0.006 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[TMEM184A]] | B | MUC1 activity raises TMEM184A's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without MUC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[IL17RE]] | B | MUC1 activity raises IL17RE's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without MUC1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[SLC50A1]] | B | MUC1 activity raises SLC50A1's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without MUC1 | 0.026 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[EFNA1]] | B | MUC1 activity raises EFNA1's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without MUC1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[C11orf52]] | B | MUC1 activity raises C11orf52's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.88× lower at baseline in the lines without MUC1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[LPIN3]] | B | MUC1 activity raises LPIN3's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without MUC1 | 0.045 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[ERBB2]] | B | MUC1 activity raises ERBB2's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.20× lower at baseline in the lines without MUC1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[LGALS9]] | B | MUC1 activity raises LGALS9's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.11× lower at baseline in the lines without MUC1 | 0.058 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[CASP10]] | B | MUC1 activity raises CASP10's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without MUC1 | 0.068 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[AP1G2]] | B | MUC1 activity raises AP1G2's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without MUC1 | 0.073 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[CARD14]] | B | MUC1 activity raises CARD14's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 1.48× lower at baseline in the lines without MUC1 | 0.073 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, 53.0); signed map (60.0, 1.9). **Vector** length 82.8, 26.1% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +2.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.0 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | mucin 1, cell surface associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,185,824-155,192,916 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD227, PEM, ADMCKD, ADMCKD1, MCKD, MCD, KL-6, EMA; previously PUM, MCKD1 |
| Gene groups (HGNC) | CD molecules; Mucins; SEA domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_EARLY |
| Reactome | 15 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [P15941](https://www.uniprot.org/uniprotkb/P15941) (Mucin-1):

> The alpha subunit has cell adhesive properties. Can act both as an adhesion and an anti-adhesion protein. May provide a protective layer on epithelial cells against bacterial and enzyme attack.; The beta subunit contains a C-terminal domain which is involved in cell signaling, through phosphorylations and protein-protein interactions. Modulates signaling in ERK, SRC and NF-kappa-B pathways. In activated T-cells, influences directly or indirectly the Ras/MAPK pathway. Promotes tumor progression. …

**Summary**, from NCBI Gene [4582](https://www.ncbi.nlm.nih.gov/gene/4582):

> This gene encodes a membrane-bound protein that is a member of the mucin family. Mucins are O-glycosylated proteins that play an essential role in forming protective mucous barriers on epithelial surfaces. These proteins also play a role in intracellular signaling. This protein is expressed on the apical surface of epithelial cells that line the mucosal surfaces of many different tissues including lung, breast stomach and pancreas. This protein is proteolytically cleaved into alpha and beta …

**Accessions** — [HGNC:7508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7508) · Entrez [4582](https://www.ncbi.nlm.nih.gov/gene/4582) · UniProt [P15941](https://www.uniprot.org/uniprotkb/P15941) · Ensembl [ENSG00000185499](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185499)

## Data

Gene col 11688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11688); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11688]; `tensor/DDL_lfc|DDL_z.npy` [11688]; `embed/gene_vectors.npy` [11688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11688 or target_col == 11688). Every well: [[MUC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "POLD4"
type: "gene"
col: 10615
ensembl_id: "ENSG00000175482"
name: "DNA polymerase delta 4, accessory subunit"
location: "11q13.2"
module: 3
arm: "+"
pooled_cpm: 36.69
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 10
direction_downstream: 15
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# POLD4

*DNA polymerase delta 4, accessory subunit* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.64× (z +3.9, q 0.056, up in 27 of 42 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change.
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.350× (z -8.2, q 2e-13, down in 42 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.481× (z -8.0, q 3e-13, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM89B]] (+0.73, fdr 7e-06), [[CIB1]] (+0.71, fdr 7e-06), [[PLIN3]] (+0.69, fdr 1e-05); moves opposite to [[ILF3]] (-0.66, fdr 3e-05), [[SRSF1]] (-0.64, fdr 3e-05), [[SNX5]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[C19orf33]] → it (grade B ⚠); 15 go from it, the strongest it → cells under [[Glycyrrhizic acid (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.64×** | +3.9 | 0.056 | 27/42 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.350×** | -8.2 | 2e-13 | 42/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.481×** | -8.0 | 3e-13 | 38/44 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.401×** | -7.1 | 2e-10 | 42/45 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.411×** | -6.9 | 7e-10 | 39/45 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.488×** | -5.6 | 3e-06 | 39/44 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.177×** | -5.0 | 4e-05 | 35/45 (NCI-H1573, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -4.9 | 7e-05 | 33/44 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.188×** | -4.9 | 8e-05 | 36/42 (KATO III, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.597×** | -4.0 | 0.004 | 33/44 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.610×** | -3.8 | 0.007 | 30/44 (SW 1271, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.283×** | -3.7 | 0.012 | 30/42 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -3.4 | 0.027 | 24/43 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.644×** | -3.4 | 0.029 | 24/45 (NCI-H460, BT-474, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.645×** | -3.1 | 0.064 | 26/45 (SW 1088, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.645×** | -3.1 | 0.064 | 24/45 (BT-474, KATO III, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.672×** | -3.1 | 0.073 | 25/45 (NCI-H1792, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 41.0 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0831× (z -10.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 97.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.7) |
| [[J82 (line)]] | alt | 28.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 24.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.125× (z -10.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 52.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -11.1) |
| [[A-427 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -8.8) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 61.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 39.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -8.6) |
| [[KATO III (line)]] | alt | 83.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.271× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 48.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 51.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 38.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -10.0) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -9.4) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.86 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89B]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CIB1]] | +0.71 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[PLIN3]] | +0.69 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[ELOF1]] | +0.66 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[SMIM29]] | +0.66 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[TRPT1]] | +0.65 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[RNF181]] | +0.64 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[CTTNBP2NL]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[IFI27L2]] | +0.63 | +0.39 / +0.70 | both halves | 6e-05 |  |
| [[MED19]] | +0.63 | +0.34 / +0.67 | both halves | 1e-04 |  |
| [[ACAP1]] | +0.63 | +0.45 / +0.69 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILF3]] | -0.66 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[SRSF1]] | -0.64 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[SNX5]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[RBBP4]] | -0.64 | -0.60 / -0.61 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[ARL5A]] | -0.63 | -0.43 / -0.69 | both halves | 4e-05 |  |
| [[RCN1]] | -0.63 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ZC3HAV1L]] | -0.63 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[FUBP1]] | -0.62 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[PPT1]] | -0.62 | -0.46 / -0.71 | both halves | 3e-05 |  |
| [[NNT]] | -0.62 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[IPO5]] | -0.62 | -0.34 / -0.71 | both halves | 1e-04 |  |
| [[FAM53B]] ⚠ | -0.61 | -0.54 / -0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF3F]] | -0.61 | -0.29 / -0.65 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C19orf33]] | B | C19orf33 activity raises POLD4's level | lines that do not express C19orf33 (19) vs lines expressing it (31) | 2.12× lower at baseline in the lines without C19orf33 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG |
| [[MSX2]] | B | MSX2 activity raises POLD4's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without MSX2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[SIGIRR]] | B | SIGIRR activity raises POLD4's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without SIGIRR | 0.050 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[TUBA4A]] | B | TUBA4A activity raises POLD4's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without TUBA4A | 0.055 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[S100A6]] | B | S100A6 activity raises POLD4's level | lines that do not express S100A6 (5) vs lines expressing it (45) | 2.67× lower at baseline in the lines without S100A6 | 0.060 | ⚠ within organs, on part of the lines; also absent: GPRC5D-AS1, HLA-H, PRRG1; maybe low, not absent; its own permutation p |
| [[SERPINB1]] | B | SERPINB1 activity raises POLD4's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without SERPINB1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[PTK6]] | B | PTK6 activity raises POLD4's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.85× lower at baseline in the lines without PTK6 | 0.080 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[C19orf81]] | B | C19orf81 activity lowers POLD4's level | lines that do not express C19orf81 (18) vs lines expressing it (32) | 1.48× higher at baseline in the lines without C19orf81 | 0.0996 | ⚠ within organs, on part of the lines; also absent: LINC02269, LMX1B, CRMP1 |
| [[CHMP5]] | C | CHMP5's natural level strengthens POLD4's drug response | CHMP5's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.70, reverse -0.17; direction not clear | 0.025 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PLEKHN1]] | C | PLEKHN1 activity raises POLD4's level | lines that do not express PLEKHN1 (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without PLEKHN1 | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.50× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.45× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.48× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.42× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[IQ 1 (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.69× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.66× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.75× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Lidocaine (hydrochloride) (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity lowers the cells' numbers under Lidocaine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.64× the cells of the other lines | 0.053 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Tolcapone (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.77× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Naproxen (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.77× the cells of the other lines | 0.066 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.22× the cells of the other lines | 0.070 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Salicylic acid (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], POLD4, [[PPP1R14B-AS1]] activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.21× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.6, 2.3); signed map (-22.4, 20.4). **Vector** length 94.4, 32.2% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.9 | +1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase delta 4, accessory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,350,772-67,356,972 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p12, POLDS |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 41 pathways, smallest: Leading Strand Synthesis; Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCU8](https://www.uniprot.org/uniprotkb/Q9HCU8) (DNA polymerase delta subunit 4):

> As a component of the tetrameric DNA polymerase delta complex (Pol-delta4), plays a role in high fidelity genome replication and repair. Within this complex, increases the rate of DNA synthesis and decreases fidelity by regulating POLD1 polymerase and proofreading 3' to 5' exonuclease activity. Pol-delta4 participates in Okazaki fragment processing, through both the short flap pathway, as well as a nick translation system. Under conditions of DNA replication stress, required for the repair of …

**Summary**, from NCBI Gene [57804](https://www.ncbi.nlm.nih.gov/gene/57804):

> This gene encodes the smallest subunit of DNA polymerase delta. DNA polymerase delta possesses both polymerase and 3' to 5' exonuclease activity and plays a critical role in DNA replication and repair. The encoded protein enhances the activity of DNA polymerase delta and plays a role in fork repair and stabilization through interactions with the DNA helicase Bloom syndrome protein. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided …

**Accessions** — [HGNC:14106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14106) · Entrez [57804](https://www.ncbi.nlm.nih.gov/gene/57804) · UniProt [Q9HCU8](https://www.uniprot.org/uniprotkb/Q9HCU8) · Ensembl [ENSG00000175482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175482)

## Data

Gene col 10615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10615); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10615]; `tensor/DDL_lfc|DDL_z.npy` [10615]; `embed/gene_vectors.npy` [10615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10615 or target_col == 10615). Every well: [[POLD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

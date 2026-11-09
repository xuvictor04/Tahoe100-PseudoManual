---
symbol: "STEAP2-AS1"
type: "gene"
col: 13604
ensembl_id: "ENSG00000227646"
name: "STEAP2 antisense RNA 1"
location: "7q21.13"
module: 8
arm: "+"
pooled_cpm: 6.11
n_lines_expressing: 38
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# STEAP2-AS1

*STEAP2 antisense RNA 1* — 7q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.00× (z +18.6, q 0e+00, up in 26 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.529× (z -6.1, q 8e-07, down in 22 of 34 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.629× (z -4.4, q 0.003, down in 19 of 33 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCH-AS1]] (+0.70, fdr 3e-05), [[SATB1-AS1]] (+0.68, fdr 1e-05), [[GAS2]] (+0.67, fdr 2e-05); moves opposite to [[GNAI2]] (-0.60, fdr 4e-04), [[ATG16L2]] (-0.56, fdr 3e-04), [[KIAA1328]] (-0.52, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[IDNK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13604.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.00×** | +18.6 | 0e+00 | 26/30 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +8.0 | 5e-13 | 1/8 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.99×** | +6.5 | 1e-08 | 22/32 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +6.0 | 3e-07 | 12/32 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +5.7 | 1e-06 | 10/29 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.7 | 1e-06 | 10/25 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.50×** | +5.5 | 3e-06 | 15/33 (A-427, RKO, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +5.3 | 8e-06 | 5/12 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.9 | 7e-05 | 4/19 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.001 | 6/34 (AsPC-1, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.57×** | +4.1 | 0.002 | 10/32 (SW48, AsPC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.26×** | +4.1 | 0.002 | 10/25 (PANC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.0 | 0.003 | 5/27 (LoVo, C-33 A, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.20×** | +3.9 | 0.004 | 7/26 (AsPC-1, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.026 | 6/30 (SW480, SW1417, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.028 | 9/30 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.029 | 10/32 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.92×** | +3.2 | 0.038 | 7/21 (HepG2/C3A, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.054 | 1/27 (SW 900) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.090 | 2/33 (A549, A498) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13604.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.529×** | -6.1 | 8e-07 | 22/34 (COLO 205, NCI-H1573, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.629×** | -4.4 | 0.003 | 19/33 (COLO 205, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -4.4 | 0.003 | 15/33 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.631×** | -4.2 | 0.004 | 16/32 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.647×** | -4.2 | 0.004 | 12/25 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -3.8 | 0.014 | 12/26 (NCI-H1573, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -3.5 | 0.040 | 8/31 (COLO 205, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.716× | -3.2 | 0.10 | 7/32 (NCI-H1573, SW480, …) | rises with dose |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.704× | -3.2 | 0.10 | 7/32 (Hs 766T, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 59.5 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -19.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.136× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 51.7 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0546× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0873× (z -12.0) |
| [[SW480 (line)]] | alt | 11.9 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -10.1) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.234× (z -9.0) |
| [[LoVo (line)]] | wt | 10.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 7.01 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0575× (z -10.1) |
| [[A498 (line)]] | wt | 1.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +9.5) | — |
| [[A-172 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCH-AS1]] | +0.70 | +0.69 / +0.46 | both halves | 3e-05 | same gene group |
| [[SATB1-AS1]] | +0.68 | +0.63 / +0.52 | both halves | 1e-05 | same gene group |
| [[GAS2]] | +0.67 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ERICH2-DT]] | +0.67 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[LINC00869-1]] | +0.66 | +0.65 / +0.33 | both halves | 1e-04 |  |
| [[HOTAIR]] | +0.63 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[KLHL2P1]] | +0.63 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ACTR3C]] | +0.62 | +0.62 / +0.32 | both halves | 2e-04 |  |
| [[MGC32805]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 | same gene group |
| [[NINJ2]] | +0.61 | +0.57 / +0.31 | both halves | 2e-04 |  |
| [[PLCH1]] | +0.60 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[MAMDC2-AS1]] | +0.59 | +0.58 / +0.30 | both halves | 2e-04 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | -0.60 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[ATG16L2]] | -0.56 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[KIAA1328]] | -0.52 | -0.46 / -0.15 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STEAP2-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PON3]] | B | PON3 activity raises STEAP2-AS1's level | lines that do not express PON3 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without PON3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[SLC24A3]] | B | SLC24A3 activity raises STEAP2-AS1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.78× lower at baseline in the lines without SLC24A3 | 0.045 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises STEAP2-AS1's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without ZNF503-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[MPP2]] | B | MPP2 activity lowers STEAP2-AS1's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.78× higher at baseline in the lines without MPP2 | 0.068 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[MAP2K1]] | B | MAP2K1 activity lowers STEAP2-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises STEAP2-AS1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without SPINT1-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[STEAP1]] | C | STEAP1 activity raises STEAP2-AS1's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 2.49× lower at baseline in the lines without STEAP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2; co-absent with the target |
| [[STEAP2]] | C | STEAP2 activity raises STEAP2-AS1's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 2.67× lower at baseline in the lines without STEAP2 | 0.035 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IDNK]] | B | STEAP2-AS1 activity lowers IDNK's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 1.36× higher at baseline in the lines without STEAP2-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent |
| [[GUCY2C-AS1]] | B | STEAP2-AS1 activity lowers GUCY2C-AS1's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 1.40× higher at baseline in the lines without STEAP2-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent |
| [[PON3]] | B | STEAP2-AS1 activity raises PON3's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 2.34× lower at baseline in the lines without STEAP2-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent |
| [[STEAP2]] | C | STEAP2-AS1 activity raises STEAP2's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 5.99× lower at baseline in the lines without STEAP2-AS1 | 9e-05 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent; co-absent with the target |
| [[STEAP1]] | C | STEAP2-AS1 activity raises STEAP1's level | lines that do not express STEAP2-AS1 (12) vs lines expressing it (38) | 3.42× lower at baseline in the lines without STEAP2-AS1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: STEAP2, STEAP1, FCGRT; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 50.9); signed map (57.7, -0.6). **Vector** length 60.8, 11.7% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +18.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.1 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | STEAP2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q21.13 — chr7:89,882,353-90,211,635 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40820) · Entrez [100874100](https://www.ncbi.nlm.nih.gov/gene/100874100) · Ensembl [ENSG00000227646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227646)

## Data

Gene col 13604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13604); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13604]; `tensor/DDL_lfc|DDL_z.npy` [13604]; `embed/gene_vectors.npy` [13604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13604 or target_col == 13604). Every well: [[STEAP2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STEAP2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

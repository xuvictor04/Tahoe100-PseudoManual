---
symbol: "VNN1"
type: "gene"
col: 3351
ensembl_id: "ENSG00000112299"
name: "vanin 1"
location: "6q23.2"
module: 8
arm: "+"
pooled_cpm: 5.82
n_lines_expressing: 23
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 53
direction_downstream: 69
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# VNN1

*vanin 1* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.44× (z +10.9, q 5e-25, up in 3 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +6.0, q 4e-07, up in 8 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.384× (z -8.8, q 8e-16, down in 20 of 21 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Dexamethasone (drug)]] 0.5 µM: 0.626× (z -4.2, q 0.004, down in 6 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRF1]] (+0.62, fdr 7e-06), [[CASP10]] (+0.61, fdr 3e-05), [[TRIM31]] (+0.58, fdr 1e-05); moves opposite to [[GLT8D1]] (-0.47, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[MTUS1-DT]] → it (grade B ⚠); 69 go from it, the strongest it → [[RNF103-CHMP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +10.9 | 5e-25 | 3/8 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +10.5 | 1e-23 | 5/14 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +9.3 | 4e-18 | 4/9 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +6.0 | 4e-07 | 8/21 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.09×** | +4.8 | 2e-04 | 5/17 (HT-29, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +4.4 | 9e-04 | 9/19 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.001 | 2/21 (AsPC-1, SNU-423) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.36×** | +4.1 | 0.003 | 2/11 (NCI-H2347, SW1417) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.85×** | +4.0 | 0.004 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.14×** | +3.7 | 0.014 | 1/7 (AsPC-1) | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.4 | 0.030 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.035 | 4/21 (A498, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.046 | 4/21 (A498, NCI-H1792, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.2 | 0.052 | 2/17 (NCI-H2347, KATO III) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.064 | 1/18 (NCI-H1573) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3351.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.384×** | -8.8 | 8e-16 | 20/21 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.472×** | -6.9 | 1e-09 | 17/21 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.626×** | -4.2 | 0.004 | 6/21 (NCI-H1573, Panc 03.27, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.877× | -4.2 | 0.004 | 10/21 (BT-474, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.646×** | -3.9 | 0.010 | 15/20 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.657×** | -3.9 | 0.011 | 4/21 (SK-MEL-2, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.697×** | -3.3 | 0.074 | 8/21 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | 0.529× | -3.1 | 0.16 | 1/21 (NCI-H1573) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 60.9 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0411× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.131× (z -14.5) |
| [[HT-29 (line)]] | alt | 25.8 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 56.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -13.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[LOX-IMVI (line)]] | wt | 7.77 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0358× (z -12.4) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -9.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1573 (line)]] | alt | 4.62 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0770× (z -10.9) |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.929 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.465 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRF1]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CASP10]] | +0.61 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[TRIM31]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ENKUR]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[RAMP1]] | +0.57 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[DAPP1]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[DUOX2]] | +0.56 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[HHLA2]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ALDH1A2]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[MUC4]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[CTSS]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RBM47]] | +0.54 | +0.39 / +0.57 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLT8D1]] | -0.47 | -0.40 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 13, C 40. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1-DT]] | B | MTUS1-DT activity raises VNN1's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without MTUS1-DT | 0.021 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[SAMD12-AS1]] | B | SAMD12-AS1 activity raises VNN1's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without SAMD12-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[KIAA1217]] | B | KIAA1217 activity raises VNN1's level | lines that do not express KIAA1217 (10) vs lines expressing it (40) | 2.38× lower at baseline in the lines without KIAA1217 | 0.039 | ⚠ within organs, on part of the lines; also absent: FAM107B, MET, S100A16 |
| [[CTSS]] | B | CTSS activity raises VNN1's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.25× lower at baseline in the lines without CTSS | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[MTUS1]] | B | MTUS1 activity raises VNN1's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 1.73× lower at baseline in the lines without MTUS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[HDAC6]] | B | HDAC6 activity raises VNN1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GABRE]] | B | GABRE activity raises VNN1's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.98× lower at baseline in the lines without GABRE | 0.081 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[SCIN]] | B | SCIN activity raises VNN1's level | lines that do not express SCIN (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without SCIN | 0.083 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[CDHR2]] | B | CDHR2 activity raises VNN1's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 1.65× lower at baseline in the lines without CDHR2 | 0.088 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[SERPINB7]] | B | SERPINB7 activity raises VNN1's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.66× lower at baseline in the lines without SERPINB7 | 0.089 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[SPATA6L]] | B | SPATA6L activity raises VNN1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without SPATA6L | 0.091 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[LGALS9]] | B | LGALS9 activity raises VNN1's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.19× lower at baseline in the lines without LGALS9 | 0.095 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 30, C 39. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF103-CHMP3]] | B | VNN1 activity raises RNF103-CHMP3's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without VNN1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[RND1]] | B | VNN1 activity raises RND1's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without VNN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[ELF3-AS1]] | B | VNN1 activity raises ELF3-AS1's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without VNN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[RBM47]] | B | VNN1 activity raises RBM47's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 3.04× lower at baseline in the lines without VNN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[LGALS9]] | B | VNN1 activity raises LGALS9's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without VNN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[KIAA1217]] | B | VNN1 activity raises KIAA1217's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 3.01× lower at baseline in the lines without VNN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[SAMD12-AS1]] | B | VNN1 activity raises SAMD12-AS1's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without VNN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[STS]] | B | VNN1 activity raises STS's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without VNN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[MUC20]] | B | VNN1 activity raises MUC20's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.39× lower at baseline in the lines without VNN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[PRRG4]] | B | VNN1 activity raises PRRG4's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 1.99× lower at baseline in the lines without VNN1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[MTUS1-DT]] | B | VNN1 activity raises MTUS1-DT's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without VNN1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[CTSS]] | B | VNN1 activity raises CTSS's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without VNN1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.4, 49.5); signed map (60.5, 25.8). **Vector** length 51.6, 12.0% of its response variance represented; |z| ≥ 3 in 551 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +3.3 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +3.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | vanin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:132,680,849-132,714,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Tiff66 |
| Gene groups (HGNC) | Vanin family |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM |
| Reactome | 6 pathways, smallest: Vitamin B5 (pantothenate) metabolism; Post-translational modification: synthesis of GPI-anchored proteins; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [O95497](https://www.uniprot.org/uniprotkb/O95497) (Pantetheinase):

> Amidohydrolase that hydrolyzes specifically one of the carboamide linkages in D-pantetheine thus recycling pantothenic acid (vitamin B5) and releasing cysteamine.

**Summary**, from NCBI Gene [8876](https://www.ncbi.nlm.nih.gov/gene/8876):

> This gene encodes a member of the vanin family of proteins, which share extensive sequence similarity with each other, and also with biotinidase. The family includes secreted and membrane-associated proteins, a few of which have been reported to participate in hematopoietic cell trafficking. No biotinidase activity has been demonstrated for any of the vanin proteins, however, they possess pantetheinase activity, which may play a role in oxidative-stress response. This protein, like its mouse …

**Accessions** — [HGNC:12705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12705) · Entrez [8876](https://www.ncbi.nlm.nih.gov/gene/8876) · UniProt [O95497](https://www.uniprot.org/uniprotkb/O95497) · Ensembl [ENSG00000112299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112299)

## Data

Gene col 3351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3351); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3351]; `tensor/DDL_lfc|DDL_z.npy` [3351]; `embed/gene_vectors.npy` [3351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3351 or target_col == 3351). Every well: [[VNN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VNN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

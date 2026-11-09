---
symbol: "CPLX1"
type: "gene"
col: 9733
ensembl_id: "ENSG00000168993"
name: "complexin 1"
location: "4p16.3"
module: 47
arm: "+"
pooled_cpm: 3.84
n_lines_expressing: 41
n_dd_up: 34
n_dd_down: 3
n_dd_up_clean: 26
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# CPLX1

*complexin 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.35× (z +20.7, q 0e+00, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.498× (z -3.7, q 0.082, down in 10 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP2E1]] (+0.59, fdr 1e-05), [[GALNT8]] (+0.58, fdr 1e-05), [[PTCH2]] (+0.57, fdr 1e-05); moves opposite to [[NT5DC1]] (-0.55, fdr 6e-05), [[ATP6V0D1-DT]] (-0.51, fdr 1e-04), [[RNPC3]] (-0.51, fdr 5e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[XKR7]] → it (grade B ⚠); 3 go from it, the strongest it → [[NRARP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.35×** | +20.7 | 0e+00 | 22/26 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **5.70×** | +17.3 | 0e+00 | 34/37 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.48×** | +14.9 | 0e+00 | 31/35 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.67×** | +12.4 | 2e-33 | 2/3 (SW1417, SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.31×** | +11.9 | 1e-30 | 26/34 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +11.0 | 4e-26 | 16/28 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.78×** | +10.1 | 3e-22 | 10/15 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.63×** | +9.2 | 2e-18 | 7/15 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.03×** | +8.4 | 3e-15 | 19/32 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +8.0 | 5e-14 | 16/34 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +7.9 | 1e-13 | 3/5 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +7.5 | 4e-12 | 11/24 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +7.0 | 2e-10 | 14/36 (LS 180, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.98×** | +6.8 | 4e-10 | 17/36 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.88×** | +6.3 | 2e-08 | 10/25 (SHP-77, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +5.9 | 1e-07 | 11/31 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.93×** | +5.6 | 8e-07 | 12/27 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.004 | 4/25 (A-427, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[SBI-0640756 (drug)]] 5 µM |  | **2.04×** | +3.7 | 0.006 | 1/22 (A498) | top dose only | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.007 | 2/26 (SW1417, MIA PaCa-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.498×** | -3.7 | 0.082 | 10/25 (RKO, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.703×** | -3.6 | 0.082 | 7/37 (LOX-IMVI, KATO III, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.783×** | -3.5 | 0.082 | 8/32 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.717× | -3.4 | 0.10 | 7/32 (SHP-77, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adenine (drug)]] 5 µM |  | 0.799× | -3.2 | 0.14 | 3/37 (NCI-H460, CFPAC-1, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.732× | -3.2 | 0.14 | 10/36 (LoVo, SW1417, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.810× | -3.0 | 0.18 | 10/37 (COLO 205, SW1417, …) | rises with dose | low cells (technical?) |
| [[Afatinib (drug)]] 5 µM |  | 0.715× | -3.0 | 0.18 | 5/35 (A-172, J82, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.99 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.4× (z +9.1) | — |
| [[A498 (line)]] | wt | 3.17 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0825× (z -8.5) |
| [[COLO 205 (line)]] | alt | 6.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 1.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +10.0) | — |
| [[A-172 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.739 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP2E1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GALNT8]] | +0.58 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[PTCH2]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[NPAS1]] | +0.57 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[DUSP2]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[NUMBL]] | +0.56 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[NTRK1]] | +0.55 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[APC2]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[MYO15A]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[GSG1L]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[SH2D4B]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[KIAA1614]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5DC1]] | -0.55 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[ATP6V0D1-DT]] | -0.51 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[RNPC3]] | -0.51 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[DRAM2]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CIAO2A]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[RAB11FIP2]] | -0.49 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[MINDY1]] | -0.48 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[PI4K2B]] | -0.47 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[EPHX2]] | -0.47 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[FBXO9]] | -0.46 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[CISD2]] | -0.45 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[INTS8]] | -0.45 | -0.36 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XKR7]] | B | XKR7 activity raises CPLX1's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without XKR7 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[NRARP]] | B | NRARP activity raises CPLX1's level | lines that do not express NRARP (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without NRARP | 0.029 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[EPPK1]] | B | EPPK1 activity raises CPLX1's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.69× lower at baseline in the lines without EPPK1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[TUBB6]] | B | TUBB6 activity lowers CPLX1's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 2.08× higher at baseline in the lines without TUBB6 | 0.089 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRARP]] | B | CPLX1 activity raises NRARP's level | lines that do not express CPLX1 (9) vs lines expressing it (41) | 2.52× lower at baseline in the lines without CPLX1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LLGL2, CASZ1, MNX1; maybe low, not absent |
| [[BICDL1]] | B | CPLX1 activity raises BICDL1's level | lines that do not express CPLX1 (9) vs lines expressing it (41) | 3.37× lower at baseline in the lines without CPLX1 | 0.051 | ⚠ within organs, on part of the lines; also absent: LLGL2, CASZ1, MNX1; maybe low, not absent |
| [[NOP2]] | B | CPLX1 activity raises NOP2's level | lines that do not express CPLX1 (9) vs lines expressing it (41) | 1.71× lower at baseline in the lines without CPLX1 | 0.079 | ⚠ within organs, on part of the lines; also absent: LLGL2, CASZ1, MNX1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.5, -14.1); signed map (17.2, 15.8). **Vector** length 48.8, 6.78% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.9 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +20.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +3.6 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -1.9 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[NG25 (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | complexin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:784,957-826,129 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPX-I |
| Gene groups (HGNC) | Complexins |
| Reactome | 9 pathways, smallest: Acetylcholine Neurotransmitter Release Cycle; GABA synthesis, release, reuptake and degradation; Norepinephrine Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O14810](https://www.uniprot.org/uniprotkb/O14810) (Complexin-1):

> Positively regulates a late step in exocytosis of various cytoplasmic vesicles, such as synaptic vesicles and other secretory vesicles. Organizes the SNAREs into a cross-linked zigzag topology that, when interposed between the vesicle and plasma membranes, is incompatible with fusion, thereby preventing SNAREs from releasing neurotransmitters until an action potential arrives at the synapse. Also involved in glucose-induced secretion of insulin by pancreatic beta-cells. Essential for motor …

**Summary**, from NCBI Gene [10815](https://www.ncbi.nlm.nih.gov/gene/10815):

> Proteins encoded by the complexin/synaphin gene family are cytosolic proteins that function in synaptic vesicle exocytosis. These proteins bind syntaxin, part of the SNAP receptor. The protein product of this gene binds to the SNAP receptor complex and disrupts it, allowing transmitter release. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2309) · Entrez [10815](https://www.ncbi.nlm.nih.gov/gene/10815) · UniProt [O14810](https://www.uniprot.org/uniprotkb/O14810) · Ensembl [ENSG00000168993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168993)

## Data

Gene col 9733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9733); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9733]; `tensor/DDL_lfc|DDL_z.npy` [9733]; `embed/gene_vectors.npy` [9733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9733 or target_col == 9733). Every well: [[CPLX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPLX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

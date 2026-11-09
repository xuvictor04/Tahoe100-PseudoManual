---
symbol: "TMEM171"
type: "gene"
col: 8044
ensembl_id: "ENSG00000157111"
name: "transmembrane protein 171"
location: "5q13.2"
module: 34
arm: "+"
pooled_cpm: 4.02
n_lines_expressing: 35
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TMEM171

*transmembrane protein 171* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.70× (z +9.0, q 1e-16, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.83× (z +8.1, q 2e-13, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.447× (z -7.3, q 1e-10, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM150C]] (+0.54, fdr 1e-04), [[CARD11]] (+0.54, fdr 1e-05), [[IL1R2]] (+0.51, fdr 4e-05); moves opposite to [[ZNF33A]] (-0.48, fdr 1e-04), [[PCM1]] (-0.44, fdr 6e-05), [[RBM3]] (-0.42, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 3 go from it, the strongest it → [[PTPRE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +9.0 | 1e-16 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +8.1 | 2e-13 | 16/30 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.1 | 2e-07 | 7/15 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +4.8 | 2e-04 | 13/31 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.43×** | +4.7 | 3e-04 | 5/31 (LS 180, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +4.5 | 7e-04 | 9/27 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.020 | 5/22 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.6 | 0.024 | 5/21 (SW 900, PANC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.3 | 0.068 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.071 | 4/24 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.60×** | +3.2 | 0.073 | 2/7 (NCI-H2347, CFPAC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.2 | 0.073 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.447×** | -7.3 | 1e-10 | 18/26 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.602×** | -6.8 | 3e-09 | 18/23 (A-172, CFPAC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.510×** | -6.4 | 4e-08 | 18/31 (Panc 03.27, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.589×** | -5.0 | 8e-05 | 12/29 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.597×** | -4.9 | 1e-04 | 14/23 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.604×** | -4.8 | 2e-04 | 11/29 (NCI-H1792, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.610×** | -4.7 | 2e-04 | 16/31 (NCI-H2347, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.662×** | -3.9 | 0.007 | 15/32 (A-172, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.680×** | -3.6 | 0.017 | 10/29 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.691×** | -3.4 | 0.032 | 10/32 (A-172, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 22.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0113× (z -31.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.00690× (z -24.9) |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 5.02 | 0 | 2 | — | [[Ivermectin (drug)]] 0.5 µM 0.0629× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 31.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -11.2) |
| [[A498 (line)]] | wt | 2.54 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0460× (z -9.6) |
| [[A549 (line)]] | wt | 2.61 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0308× (z -9.6) |
| [[LS 180 (line)]] | wt | 7.58 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0344× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 1.30 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0568× (z -8.7) |
| [[A-427 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.950 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM150C]] | +0.54 | +0.32 / +0.50 | both halves | 1e-04 |  |
| [[CARD11]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[IL1R2]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[FAM124A]] | +0.50 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CDYL2]] | +0.50 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[LINC03004]] | +0.50 | +0.30 / +0.57 | both halves | 2e-04 |  |
| [[MAP6]] | +0.50 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[TBX20]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[TMEM92]] | +0.48 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.48 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[CBLC]] | +0.48 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[FKBP1B]] | +0.47 | +0.34 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF33A]] | -0.48 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[PCM1]] | -0.44 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[RBM3]] | -0.42 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[HP1BP3]] | -0.42 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[SLC35E2B]] | -0.41 | -0.54 / -0.21 | both halves | 7e-04 |  |
| [[NFIX]] | -0.40 | -0.42 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises TMEM171's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.31× lower at baseline in the lines without F3 | 0.004 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[CARD11]] | B | CARD11 activity raises TMEM171's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without CARD11 | 0.010 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[ITGA2]] | B | ITGA2 activity raises TMEM171's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.11× lower at baseline in the lines without ITGA2 | 0.039 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[PTPRE]] | B | PTPRE activity raises TMEM171's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.87× lower at baseline in the lines without PTPRE | 0.044 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[CREG2]] | B | CREG2 activity raises TMEM171's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without CREG2 | 0.087 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[KHDC1]] | B | KHDC1 activity raises TMEM171's level | lines that do not express KHDC1 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without KHDC1 | 0.093 | ⚠ within organs, on part of the lines; also absent: KHDC1-AS1, MAP9, C15orf48 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRE]] | B | TMEM171 activity raises PTPRE's level | lines that do not express TMEM171 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without TMEM171 | 0.055 | ⚠ within organs, on part of the lines; also absent: CD274, GBP5, PTGER4; maybe low, not absent |
| [[ITGA2]] | B | TMEM171 activity raises ITGA2's level | lines that do not express TMEM171 (15) vs lines expressing it (35) | 2.28× lower at baseline in the lines without TMEM171 | 0.067 | ⚠ within organs, on part of the lines; also absent: CD274, GBP5, PTGER4; maybe low, not absent |
| [[TMEM54]] | B | TMEM171 activity raises TMEM54's level | lines that do not express TMEM171 (15) vs lines expressing it (35) | 1.52× lower at baseline in the lines without TMEM171 | 0.093 | ⚠ within organs, on part of the lines; also absent: CD274, GBP5, PTGER4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, 59.4); signed map (3.7, 56.8). **Vector** length 49.5, 8.19% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.0 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +1.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 171 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:73,120,569-73,131,809 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRP2 |
| Matched by | ensembl_id |

UniProt [Q8WVE6](https://www.uniprot.org/uniprotkb/Q8WVE6) carries no function annotation.

**Summary**, from NCBI Gene [134285](https://www.ncbi.nlm.nih.gov/gene/134285):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27031) · Entrez [134285](https://www.ncbi.nlm.nih.gov/gene/134285) · UniProt [Q8WVE6](https://www.uniprot.org/uniprotkb/Q8WVE6) · Ensembl [ENSG00000157111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157111)

## Data

Gene col 8044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8044); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8044]; `tensor/DDL_lfc|DDL_z.npy` [8044]; `embed/gene_vectors.npy` [8044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8044 or target_col == 8044). Every well: [[TMEM171 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM171.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

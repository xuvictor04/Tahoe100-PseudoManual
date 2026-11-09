---
symbol: "HAS3"
type: "gene"
col: 2310
ensembl_id: "ENSG00000103044"
name: "hyaluronan synthase 3"
location: "16q22.1"
module: 34
arm: "+"
pooled_cpm: 5.45
n_lines_expressing: 32
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# HAS3

*hyaluronan synthase 3* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.37× (z +10.1, q 3e-21, up in 10 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.551× (z -6.1, q 6e-07, down in 17 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMA3]] (+0.67, fdr 7e-06), [[LAMC2]] (+0.66, fdr 7e-06), [[FERMT1]] (+0.62, fdr 7e-06); moves opposite to [[ERP29]] (-0.54, fdr 1e-05), [[SELENOP]] (-0.52, fdr 2e-05), [[CLN3]] (-0.51, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ABCC3]] → it (grade B ⚠); 5 go from it, the strongest it → [[EPHA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.37×** | +10.1 | 3e-21 | 10/22 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +9.1 | 2e-17 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +5.7 | 2e-06 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.4 | 7e-06 | 6/24 (HEC-1-A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +4.4 | 0.001 | 1/14 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.030 | 8/29 (NCI-H2347, KATO III, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.033 | 6/27 (LS 180, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.086 | 3/20 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.00× | +3.0 | 0.16 | 0/8 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.551×** | -6.1 | 6e-07 | 17/26 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.536×** | -5.9 | 9e-07 | 15/29 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.496×** | -5.8 | 1e-06 | 20/28 (AsPC-1, A498, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.546×** | -4.7 | 4e-04 | 15/28 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.625×** | -3.8 | 0.019 | 12/24 (HEC-1-A, AsPC-1, …) | rises with dose | position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.642×** | -3.7 | 0.020 | 2/28 (HepG2/C3A, SW1417) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.633×** | -3.7 | 0.020 | 15/26 (A549, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.739×** | -3.5 | 0.032 | 12/28 (AsPC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.705×** | -3.4 | 0.044 | 12/27 (COLO 205, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.479×** | -3.2 | 0.078 | 14/21 (A498, A549, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.774× | -3.0 | 0.13 | 12/27 (RKO, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 23.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0829× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.102× (z -11.2) |
| [[A549 (line)]] | wt | 25.3 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0630× (z -12.3) |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 4.08 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0608× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 7.01 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0729× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 3.75 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0761× (z -9.8) |
| [[A-172 (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.982 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.852 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMA3]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[C6orf141]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[CDC42EP2]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[EPHA2]] | +0.59 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ITGA6]] | +0.58 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[BMAL2]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SLC35F3]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SPIN4]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.57 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ICAM2]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERP29]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[SELENOP]] | -0.52 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[CLN3]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ALDH2]] | -0.48 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC3]] | B | ABCC3 activity raises HAS3's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without ABCC3 | 0.015 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[MAP2K1]] | B | MAP2K1 activity raises HAS3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[SLC22A3]] | B | SLC22A3 activity raises HAS3's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without SLC22A3 | 0.029 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[LAMC2]] | B | LAMC2 activity raises HAS3's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without LAMC2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[SYT13]] | B | SYT13 activity raises HAS3's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 2.12× lower at baseline in the lines without SYT13 | 0.051 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[ITGA2]] | B | ITGA2 activity raises HAS3's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without ITGA2 | 0.055 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[MAP2K2]] | B | MAP2K2 activity raises HAS3's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[LAMA3]] | C | LAMA3 activity raises HAS3's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.38× lower at baseline in the lines without LAMA3 | 0.012 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B; co-absent with the target |
| [[FGD6]] | C | FGD6 activity raises HAS3's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 2.33× lower at baseline in the lines without FGD6 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | HAS3 activity raises EPHA2's level | lines that do not express HAS3 (18) vs lines expressing it (32) | 2.99× lower at baseline in the lines without HAS3 | 0.037 | ⚠ within organs, on part of the lines; also absent: IQANK1, MLXIPL, CAMSAP3; maybe low, not absent |
| [[SPTBN5]] | B | HAS3 activity raises SPTBN5's level | lines that do not express HAS3 (18) vs lines expressing it (32) | 1.09× lower at baseline in the lines without HAS3 | 0.063 | ⚠ within organs, on part of the lines; also absent: IQANK1, MLXIPL, CAMSAP3; maybe low, not absent |
| [[TMC7]] | B | HAS3 activity raises TMC7's level | lines that do not express HAS3 (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without HAS3 | 0.099 | ⚠ within organs, on part of the lines; also absent: IQANK1, MLXIPL, CAMSAP3; maybe low, not absent |
| [[EPHA2-AS1]] | C | HAS3 activity raises EPHA2-AS1's level | lines that do not express HAS3 (18) vs lines expressing it (32) | 2.07× lower at baseline in the lines without HAS3 | 0.040 | ⚠ within organs, on part of the lines; also absent: IQANK1, MLXIPL, CAMSAP3; maybe low, not absent; co-absent with the target |
| [[FGD6]] | C | HAS3 activity raises FGD6's level | lines that do not express HAS3 (18) vs lines expressing it (32) | 2.55× lower at baseline in the lines without HAS3 | 0.068 | ⚠ within organs, on part of the lines; also absent: IQANK1, MLXIPL, CAMSAP3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.3, 3.0); signed map (5.2, 41.8). **Vector** length 69.1, 15.9% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +2.0 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.2 | +1.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.6 | -5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | hyaluronan synthase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,105,653-69,118,719 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycosyltransferase family 2 |
| Reactome | 3 pathways, smallest: Hyaluronan metabolism; Glycosaminoglycan metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [O00219](https://www.uniprot.org/uniprotkb/O00219) (Hyaluronan synthase 3):

> Catalyzes the addition of GlcNAc or GlcUA monosaccharides to the nascent hyaluronan polymer. Therefore, it is essential to hyaluronan synthesis a major component of most extracellular matrices that has a structural role in tissues architectures and regulates cell adhesion, migration and differentiation. This is one of three isoenzymes responsible for cellular hyaluronan synthesis.

**Summary**, from NCBI Gene [3038](https://www.ncbi.nlm.nih.gov/gene/3038):

> The protein encoded by this gene is involved in the synthesis of the unbranched glycosaminoglycan hyaluronan, or hyaluronic acid, which is a major constituent of the extracellular matrix. This gene is a member of the NODC/HAS gene family. Compared to the proteins encoded by other members of this gene family, this protein appears to be more of a regulator of hyaluronan synthesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:4820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4820) · Entrez [3038](https://www.ncbi.nlm.nih.gov/gene/3038) · UniProt [O00219](https://www.uniprot.org/uniprotkb/O00219) · Ensembl [ENSG00000103044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103044)

## Data

Gene col 2310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2310); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2310]; `tensor/DDL_lfc|DDL_z.npy` [2310]; `embed/gene_vectors.npy` [2310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2310 or target_col == 2310). Every well: [[HAS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

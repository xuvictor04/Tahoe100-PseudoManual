---
symbol: "TMEM177"
type: "gene"
col: 6846
ensembl_id: "ENSG00000144120"
name: "transmembrane protein 177"
location: "2q14.2"
module: 33
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TMEM177

*transmembrane protein 177* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.55× (z +8.7, q 1e-15, up in 33 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.517× (z -8.8, q 1e-15, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLE1]] (+0.81, fdr 7e-06), [[ASB13]] (+0.79, fdr 7e-06), [[FXN]] (+0.77, fdr 7e-06); moves opposite to [[GNAS]] (-0.66, fdr 1e-05), [[YPEL5]] (-0.64, fdr 1e-05), [[C12orf57]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IGFBP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +8.7 | 1e-15 | 33/40 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +8.7 | 1e-15 | 31/41 (RPMI-7951, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +7.8 | 2e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +7.6 | 6e-12 | 22/40 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +6.0 | 3e-07 | 6/41 (NCI-H2347, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.8 | 5e-07 | 4/11 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +5.5 | 3e-06 | 9/22 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +5.4 | 5e-06 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.71×** | +4.8 | 9e-05 | 11/33 (C-33 A, NCI-H460, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.4 | 5e-04 | 7/41 (SW480, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +4.3 | 9e-04 | 11/44 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.021 | 8/42 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.5 | 0.022 | 2/13 (NCI-H23, A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.98×** | +3.3 | 0.035 | 1/8 (HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.40×** | +3.1 | 0.065 | 1/41 (RPMI-7951) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.080 | 5/37 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -8.8 | 1e-15 | 20/25 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.529×** | -6.0 | 6e-07 | 22/45 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.667×** | -3.8 | 0.027 | 10/42 (HCT15, SNU-423, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.693× | -3.3 | 0.13 | 10/28 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.700× | -3.2 | 0.14 | 4/34 (SNU-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.713× | -3.2 | 0.14 | 11/39 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.720× | -3.1 | 0.16 | 8/29 (J82, RKO, …) | rises with dose | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.717× | -3.0 | 0.18 | 10/37 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.94 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0714× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -8.8) |
| [[A498 (line)]] | wt | 3.15 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 3.61 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -9.5) |
| [[PANC-1 (line)]] | alt | 3.34 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -8.6) |
| [[SW1417 (line)]] | alt | 3.14 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0351× (z -10.8) |
| [[A-172 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.678 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.954 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.871 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.631 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.870 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.740 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLE1]] | +0.81 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[ASB13]] | +0.79 | +0.62 / +0.79 | both halves | 7e-06 |  |
| [[FXN]] | +0.77 | +0.60 / +0.80 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[TSEN2]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[COG2]] | +0.73 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[RRP1B]] | +0.71 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[EXOSC2]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ZNF485]] | +0.70 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[DHODH]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MCAT]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ORC5]] | +0.69 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[ZNF232]] | +0.69 | +0.57 / +0.73 | both halves | 9e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.66 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[YPEL5]] | -0.64 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[C12orf57]] | -0.63 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[CD27-AS1]] | -0.63 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ATOSA]] | -0.63 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ZNF451-AS1]] | -0.61 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[LASP1]] | -0.61 | -0.58 / -0.60 | both halves | 8e-06 |  |
| [[C2]] | -0.60 | -0.40 / -0.32 | both halves | 1e-04 |  |
| [[KMT2E-AS1]] | -0.59 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[LRP2BP]] | -0.59 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFBP6]] | B | IGFBP6 activity lowers TMEM177's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 1.33× higher at baseline in the lines without IGFBP6 | 0.074 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[USP31]] | C | USP31 activity raises TMEM177's level | lines that do not express USP31 (3) vs lines expressing it (47) | 1.76× lower at baseline in the lines without USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.801). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.3, -41.0); signed map (-8.5, -52.7). **Vector** length 47.6, 6.28% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.51 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.52 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +1.7 | +8.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.7 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.2 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -8.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 177 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:119,679,167-119,686,507 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10993 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53S58](https://www.uniprot.org/uniprotkb/Q53S58) (Transmembrane protein 177):

> Plays a role in the early steps of cytochrome c oxidase subunit II (MT-CO2/COX2) maturation and is required for the stabilization of COX20 and the newly synthesized MT-CO2/COX2 protein.

**Summary**, from NCBI Gene [80775](https://www.ncbi.nlm.nih.gov/gene/80775):

> Located in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28143) · Entrez [80775](https://www.ncbi.nlm.nih.gov/gene/80775) · UniProt [Q53S58](https://www.uniprot.org/uniprotkb/Q53S58) · Ensembl [ENSG00000144120](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144120)

## Data

Gene col 6846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6846); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6846]; `tensor/DDL_lfc|DDL_z.npy` [6846]; `embed/gene_vectors.npy` [6846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6846 or target_col == 6846). Every well: [[TMEM177 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM177.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

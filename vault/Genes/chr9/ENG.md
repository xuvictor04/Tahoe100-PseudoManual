---
symbol: "ENG"
type: "gene"
col: 2817
ensembl_id: "ENSG00000106991"
name: "endoglin"
location: "9q34.11"
module: 110
arm: "+"
pooled_cpm: 8.4
n_lines_expressing: 33
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# ENG

*endoglin* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.06× (z +8.9, q 2e-16, up in 13 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.451× (z -9.4, q 3e-18, down in 24 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02985]] (+0.59, fdr 2e-05), [[ZNF496]] (+0.56, fdr 2e-05), [[PACC1]] (+0.53, fdr 2e-05); moves opposite to [[STAG2]] (-0.53, fdr 9e-05), [[TNFAIP6]] (-0.50, fdr 3e-05), [[ABCA5]] (-0.50, fdr 2e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[INSYN2B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CASC9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +8.9 | 2e-16 | 13/27 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.6 | 0.001 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.9 | 0.018 | 0/11 | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.5 | 0.064 | 3/18 (hTERT-HPNE, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.072 | 5/28 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | 1.29× | +3.2 | 0.14 | 2/26 (NCI-H460, NCI-H1792) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.451×** | -9.4 | 3e-18 | 24/28 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -6.1 | 3e-07 | 17/28 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.739×** | -5.2 | 3e-05 | 20/27 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -4.7 | 3e-04 | 10/29 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -4.1 | 0.004 | 15/25 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.726×** | -3.9 | 0.008 | 10/31 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.732×** | -3.8 | 0.010 | 9/30 (HOP62, J82, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.762×** | -3.3 | 0.057 | 13/28 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.057 | 10/29 (A-172, CHP-212, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | 0.785× | -3.1 | 0.10 | 9/30 (LOX-IMVI, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.767× | -3.0 | 0.13 | 5/28 (HOP62, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 17.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.178× (z -8.6) |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.166× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0859× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 9.80 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.131× (z -12.8) |
| [[A-172 (line)]] | wt | 52.2 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0996× (z -14.2) |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -17.4) |
| [[RPMI-7951 (line)]] | alt | 19.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -11.4) |
| [[J82 (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 24.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.8) |
| [[SW 900 (line)]] | alt | 8.65 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.118× (z -8.6) |
| [[CHP-212 (line)]] | wt | 34.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0864× (z -10.3) |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -8.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HS-578T (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 5.68 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0528× (z -9.9) |
| [[A-427 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.83 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02985]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ZNF496]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PACC1]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[SLC27A4]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.53 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZNF549]] | +0.53 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[AK5]] | +0.53 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[GFOD2]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[HIRA]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[XYLT2]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[KCNQ5]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG2]] | -0.53 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[TNFAIP6]] | -0.50 | -0.53 / -0.45 | both halves | 3e-05 | STRING 496 |
| [[ABCA5]] | -0.50 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[CGGBP1]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CYLD]] | -0.50 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[FMR1]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MAT2B]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[OGFRL1]] | -0.48 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[LINC00882]] | -0.48 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[OPTN]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[TSGA10]] | -0.47 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[SOD2]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INSYN2B]] | B | INSYN2B activity raises ENG's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.13× lower at baseline in the lines without INSYN2B | 0.047 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[RGS4]] | B | RGS4 activity raises ENG's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.51× lower at baseline in the lines without RGS4 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC9]] | B | ENG activity raises CASC9's level | lines that do not express ENG (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without ENG | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CSPG4, EGF; maybe low, not absent |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.4, -30.6); signed map (-54.1, -15.9). **Vector** length 60.0, 12.2% of its response variance represented; |z| ≥ 3 in 637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +2.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +1.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +0.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -4.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -6.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | endoglin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,811,130-127,854,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | END, HHT1, CD105; previously ORW1, ORW |
| Gene groups (HGNC) | CD molecules |
| Hallmark sets | TGF_BETA_SIGNALING, KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [P17813](https://www.uniprot.org/uniprotkb/P17813) (Endoglin):

> Vascular endothelium glycoprotein that plays an important role in the regulation of angiogenesis. Required for normal structure and integrity of adult vasculature. Regulates the migration of vascular endothelial cells. Required for normal extraembryonic angiogenesis and for embryonic heart development (By similarity). May regulate endothelial cell shape changes in response to blood flow, which drive vascular remodeling and establishment of normal vascular morphology during angiogenesis (By …

**Summary**, from NCBI Gene [2022](https://www.ncbi.nlm.nih.gov/gene/2022):

> This gene encodes a homodimeric transmembrane protein which is a major glycoprotein of the vascular endothelium. This protein is a component of the transforming growth factor beta receptor complex and it binds to the beta1 and beta3 peptides with high affinity. Mutations in this gene cause hereditary hemorrhagic telangiectasia, also known as Osler-Rendu-Weber syndrome 1, an autosomal dominant multisystemic vascular dysplasia. This gene may also be involved in preeclampsia and several types of …

**Accessions** — [HGNC:3349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3349) · Entrez [2022](https://www.ncbi.nlm.nih.gov/gene/2022) · UniProt [P17813](https://www.uniprot.org/uniprotkb/P17813) · Ensembl [ENSG00000106991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106991)

## Data

Gene col 2817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2817); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2817]; `tensor/DDL_lfc|DDL_z.npy` [2817]; `embed/gene_vectors.npy` [2817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2817 or target_col == 2817). Every well: [[ENG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

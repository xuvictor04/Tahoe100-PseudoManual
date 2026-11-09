---
symbol: "SYNGR2"
type: "gene"
col: 2979
ensembl_id: "ENSG00000108639"
name: "synaptogyrin 2"
location: "17q25.3"
module: 24
arm: "+"
pooled_cpm: 26.91
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SYNGR2

*synaptogyrin 2* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.76× (z +6.3, q 2e-07, up in 33 of 43 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.35× (z +3.3, q 0.088, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.429× (z -4.5, q 0.003, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CKB]] (+0.57, fdr 2e-05), [[IFFO2]] (+0.56, fdr 1e-05), [[CYP2S1]] (+0.55, fdr 1e-05); moves opposite to [[BMS1P23]] (-0.50, fdr 2e-04), [[AHSA2P]] (-0.49, fdr 4e-05), [[DHX38]] (-0.43, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[GRB7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.76×** | +6.3 | 2e-07 | 33/43 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.59×** | +5.1 | 8e-05 | 24/40 (J82, HT-29, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.43×** | +3.6 | 0.052 | 17/35 (Panc 03.27, SNU-423, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.38×** | +3.4 | 0.085 | 22/46 (HEC-1-A, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.088 | 17/47 (Panc 03.27, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.37×** | +3.3 | 0.088 | 15/31 (LS 180, SNU-423, …) | all doses, flat | composition shift |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 1.22× | +3.2 | 0.12 | 12/48 (SW1417, KATO III, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.34× | +3.2 | 0.12 | 20/47 (NCI-H2030, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.429×** | -4.5 | 0.003 | 26/45 (HOP62, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.673×** | -4.2 | 0.007 | 25/47 (A498, J82, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.474×** | -4.0 | 0.012 | 25/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 8.36 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0872× (z -9.4) |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.280× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[LS 180 (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.358× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 29.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -11.8) |
| [[A-172 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKB]] | +0.57 | +0.50 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_MYOGENESIS |
| [[IFFO2]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CYP2S1]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ARHGEF3]] | +0.52 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[PIM1]] | +0.52 | +0.46 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[TIMM17B]] ⚠ | +0.51 | +0.37 / +0.52 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC50A1]] | +0.50 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[TNFRSF1B]] | +0.49 | +0.42 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[PSME1]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[NDUFAF3]] | +0.49 | +0.28 / +0.56 | both halves | 3e-04 |  |
| [[LAGE3]] | +0.48 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[SOX9]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ZMIZ2]] | +0.48 | +0.46 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P23]] | -0.50 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[AHSA2P]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[DHX38]] | -0.43 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[CDK11B]] | -0.43 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[NUDT13]] | -0.43 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[WASH2P-1]] | -0.42 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[CDK11A]] | -0.41 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[DPY19L3-DT]] | -0.41 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[ANP32B]] | -0.41 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[PRIMPOL]] | -0.41 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[U2SURP]] | -0.41 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[ANXA2R-OT1]] | -0.41 | -0.34 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRB7]] | B | GRB7 activity raises SYNGR2's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.87× lower at baseline in the lines without GRB7 | 0.012 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[MUC3A]] | B | MUC3A activity raises SYNGR2's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.71× lower at baseline in the lines without MUC3A | 0.020 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[SLC52A3]] | B | SLC52A3 activity raises SYNGR2's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 1.65× lower at baseline in the lines without SLC52A3 | 0.029 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[MISP]] | B | MISP activity raises SYNGR2's level | lines that do not express MISP (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without MISP | 0.037 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[RASSF7]] | B | RASSF7 activity raises SYNGR2's level | lines that do not express RASSF7 (5) vs lines expressing it (45) | 1.72× lower at baseline in the lines without RASSF7 | 0.051 | ⚠ within organs, on part of the lines; also absent: SORBS1, CTSV, BCL2L1; maybe low, not absent |
| [[SELENOM]] | B | SELENOM activity lowers SYNGR2's level | lines that do not express SELENOM (14) vs lines expressing it (36) | 1.48× higher at baseline in the lines without SELENOM | 0.071 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S |
| [[CGN]] | B | CGN activity raises SYNGR2's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.48× lower at baseline in the lines without CGN | 0.087 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[TSPAN2]] | B | TSPAN2 activity raises SYNGR2's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without TSPAN2 | 0.099 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[RHPN2]] | C | RHPN2 activity raises SYNGR2's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without RHPN2 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.232). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.3, 32.8); signed map (-5.3, 27.3). **Vector** length 86.3, 20.8% of its response variance represented; |z| ≥ 3 in 669 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +5.1 | +3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Canagliflozin (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.5 | +1.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -2.4 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | synaptogyrin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,168,581-78,173,527 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Synaptogyrins |
| Hallmark sets | MYOGENESIS, IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [O43760](https://www.uniprot.org/uniprotkb/O43760) (Synaptogyrin-2):

> May play a role in regulated exocytosis. In neuronal cells, modulates the localization of synaptophysin/SYP into synaptic-like microvesicles and may therefore play a role in the formation and/or the maturation of this vesicles. May also play a role in GLUT4 storage and transport to the plasma membrane.; (Microbial infection) May play a role in the assembly of cytoplasmic inclusion bodies required for SFTS phlebovirus replication.

**Summary**, from NCBI Gene [9144](https://www.ncbi.nlm.nih.gov/gene/9144):

> This gene encodes an integral membrane protein containing four transmembrane regions and a C-terminal cytoplasmic tail that is tyrosine phosphorylated. The exact function of this protein is unclear, but studies of a similar rat protein suggest that it may play a role in regulating membrane traffic in non-neuronal cells. The gene belongs to the synaptogyrin gene family. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:11499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11499) · Entrez [9144](https://www.ncbi.nlm.nih.gov/gene/9144) · UniProt [O43760](https://www.uniprot.org/uniprotkb/O43760) · Ensembl [ENSG00000108639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108639)

## Data

Gene col 2979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2979); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2979]; `tensor/DDL_lfc|DDL_z.npy` [2979]; `embed/gene_vectors.npy` [2979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2979 or target_col == 2979). Every well: [[SYNGR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNGR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

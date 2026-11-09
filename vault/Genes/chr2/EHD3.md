---
symbol: "EHD3"
type: "gene"
col: 264
ensembl_id: "ENSG00000013016"
name: "EH domain containing 3"
location: "2p23.1"
module: 132
arm: "+"
pooled_cpm: 3.54
n_lines_expressing: 36
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# EHD3

*EH domain containing 3* — 2p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.55× (z +8.0, q 6e-13, up in 6 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.60× (z +5.9, q 6e-07, up in 15 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.353× (z -9.3, q 7e-18, down in 24 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[F2R]] (+0.63, fdr 2e-05), [[ELOVL2]] (+0.61, fdr 1e-05), [[SRPX2]] (+0.60, fdr 3e-05); moves opposite to [[MICU1]] (-0.61, fdr 1e-05), [[ZFYVE1]] (-0.49, fdr 3e-05), [[TRNAU1AP]] (-0.49, fdr 3e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PXDN]] → it (grade B ⚠); 3 go from it, the strongest it → [[PCDHGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +8.0 | 6e-13 | 6/7 (Hs 766T, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +7.9 | 7e-13 | 8/9 (HS-578T, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +7.3 | 4e-11 | 13/18 (Hs 766T, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +5.9 | 6e-07 | 15/33 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.004 | 10/29 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.040 | 9/34 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.049 | 5/34 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.057 | 8/32 (CFPAC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 264.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.353×** | -9.3 | 7e-18 | 24/34 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -8.2 | 5e-14 | 21/26 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.402×** | -8.2 | 6e-14 | 22/30 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.408×** | -8.0 | 2e-13 | 19/30 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.614×** | -4.4 | 0.001 | 14/34 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.623×** | -4.2 | 0.002 | 14/33 (hTERT-HPNE, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.645×** | -3.9 | 0.007 | 12/28 (C32, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.741×** | -3.8 | 0.010 | 14/27 (A-172, A549, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.657×** | -3.6 | 0.024 | 9/29 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.17 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0901× (z -9.7) |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0350× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Pyridoxine (drug)]] 0.5 µM 0.0779× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 8.26 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0176× (z -14.1) |
| [[A-172 (line)]] | wt | 5.23 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -9.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[C32 (line)]] | wt | 4.54 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 7.25 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0921× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -9.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0690× (z -9.1) |
| [[A-427 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.273 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F2R]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ELOVL2]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SRPX2]] | +0.60 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[VASH1]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[COL4A2]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SH3RF3]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PCDHGC3]] | +0.55 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[KCTD12]] | +0.54 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[FHL1]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LDOC1]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MOCS1]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[JCAD]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICU1]] | -0.61 | -0.55 / -0.54 | both halves | 1e-05 | same gene group |
| [[ZFYVE1]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TRNAU1AP]] | -0.49 | -0.28 / -0.61 | both halves | 3e-04 |  |
| [[SYNRG]] | -0.48 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[NDUFA1]] | -0.46 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[CEP164P1]] | -0.46 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[SCAMP2]] | -0.45 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[TM2D1]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ATP5PD]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[COX17]] | -0.45 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[RAB33B-AS1]] | -0.44 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[CDK19]] | -0.44 | -0.44 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PXDN]] | B | PXDN activity raises EHD3's level | lines that do not express PXDN (29) vs lines expressing it (21) | 2.22× lower at baseline in the lines without PXDN | 0.021 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EHD3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PSMB5]] | B | PSMB5 activity raises EHD3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MIR646HG]] | B | MIR646HG activity raises EHD3's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.11× lower at baseline in the lines without MIR646HG | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |
| [[SPANXA2-OT1]] | C | SPANXA2-OT1 activity raises EHD3's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 2.68× lower at baseline in the lines without SPANXA2-OT1 | 0.041 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3; co-absent with the target |
| [[LDOC1]] | C | LDOC1 activity raises EHD3's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 2.76× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |
| [[STK32B]] | C | STK32B activity raises EHD3's level | lines that do not express STK32B (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without STK32B | 0.085 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHGA2]] | B | EHD3 activity raises PCDHGA2's level | lines that do not express EHD3 (14) vs lines expressing it (36) | 2.78× lower at baseline in the lines without EHD3 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MAP9, EVC, AKR1B1 |
| [[STK32B]] | C | EHD3 activity raises STK32B's level | lines that do not express EHD3 (14) vs lines expressing it (36) | 4.01× lower at baseline in the lines without EHD3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MAP9, EVC, AKR1B1; co-absent with the target |
| [[ZNF354C]] | C | EHD3 activity raises ZNF354C's level | lines that do not express EHD3 (14) vs lines expressing it (36) | 3.46× lower at baseline in the lines without EHD3 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MAP9, EVC, AKR1B1; co-absent with the target |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.4, 20.2); signed map (22.1, 41.1). **Vector** length 49.0, 7.94% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | -0.6 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -9.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | EH domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.1 — chr2:31,234,152-31,269,451 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PAST3 |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZN3](https://www.uniprot.org/uniprotkb/Q9NZN3) (EH domain-containing protein 3):

> ATP- and membrane-binding protein that controls membrane reorganization/tubulation upon ATP hydrolysis. In vitro causes tubulation of endocytic membranes. Binding to phosphatidic acid induces its membrane tubulation activity (By similarity). Plays a role in endocytic transport. Involved in early endosome to recycling endosome compartment (ERC), retrograde early endosome to Golgi, and endosome to plasma membrane (rapid recycling) protein transport. Involved in the regulation of Golgi maintenance …

**Summary**, from NCBI Gene [30845](https://www.ncbi.nlm.nih.gov/gene/30845):

> Predicted to enable protein-macromolecule adaptor activity. Involved in several processes, including cytosolic transport; endocytic recycling; and protein homooligomerization. Acts upstream of or within protein localization to plasma membrane and regulation of cardiac muscle cell membrane potential. Located in ciliary pocket membrane; ciliary transition zone; and recycling endosome membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3244) · Entrez [30845](https://www.ncbi.nlm.nih.gov/gene/30845) · UniProt [Q9NZN3](https://www.uniprot.org/uniprotkb/Q9NZN3) · Ensembl [ENSG00000013016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013016)

## Data

Gene col 264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 264); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 264]; `tensor/DDL_lfc|DDL_z.npy` [264]; `embed/gene_vectors.npy` [264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 264 or target_col == 264). Every well: [[EHD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

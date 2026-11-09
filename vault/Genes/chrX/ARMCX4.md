---
symbol: "ARMCX4"
type: "gene"
col: 12206
ensembl_id: "ENSG00000196440"
name: "armadillo repeat containing X-linked 4"
location: "Xq22.1"
module: 88
arm: "+"
pooled_cpm: 12.56
n_lines_expressing: 32
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# ARMCX4

*armadillo repeat containing X-linked 4* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Filgotinib (drug)]] 5 µM: 1.53× (z +3.9, q 0.039, up in 12 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 4.87×, SW 900 4.11×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.238× (z -12.9, q 2e-35, down in 26 of 29 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.452× (z -6.1, q 9e-08, down in 19 of 30 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP3CB-AS1]] (+0.71, fdr 3e-05), [[LINC00571]] (+0.69, fdr 1e-05), [[CLHC1]] (+0.69, fdr 1e-05); moves opposite to [[MAPT]] (-0.69, fdr 1e-05), [[GMCL1]] (-0.67, fdr 1e-05), [[YIF1B]] (-0.66, fdr 9e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF69]] → it (grade B ⚠); 8 go from it, the strongest it → [[ZNF69]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12206.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 4.87×, SW 900 4.11×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.039 | 12/30 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +3.8 | 0.039 | 13/30 (AsPC-1, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.97× | +3.2 | 0.21 | 12/30 (SW480, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.45× | +3.2 | 0.21 | 9/29 (RKO, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.238×** | -12.9 | 2e-35 | 26/29 (SW480, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.259×** | -12.2 | 1e-31 | 27/30 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.302×** | -10.8 | 9e-25 | 27/30 (COLO 205, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.303×** | -10.7 | 9e-25 | 23/28 (SW480, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.375×** | -8.8 | 1e-16 | 27/30 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.446×** | -6.6 | 4e-09 | 17/26 (RKO, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.452×** | -6.1 | 9e-08 | 19/30 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.276×** | -6.1 | 9e-08 | 19/30 (RKO, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.519×** | -5.9 | 2e-07 | 20/28 (RKO, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.552×** | -5.3 | 5e-06 | 17/29 (PANC-1, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.580×** | -4.9 | 5e-05 | 18/29 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.372×** | -4.7 | 1e-04 | 18/27 (PANC-1, RPMI-7951, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.377×** | -4.6 | 2e-04 | 15/27 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.624×** | -4.2 | 9e-04 | 18/29 (PANC-1, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.635×** | -4.1 | 0.002 | 16/29 (PANC-1, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.474×** | -3.5 | 0.016 | 12/30 (SNU-423, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.021 | 14/30 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.679×** | -3.3 | 0.033 | 17/30 (CHP-212, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.721×** | -2.9 | 0.098 | 10/30 (SK-MEL-2, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.9 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0982× (z -15.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0873× (z -8.6) |
| [[RKO (line)]] | wt | 34.9 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0883× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.127× (z -12.4) |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0191× (z -21.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 19.7 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0938× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0533× (z -14.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 21.5 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0655× (z -14.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 31.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +15.1) | [[Bortezomib (drug)]] 5 µM 0.0521× (z -10.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 8.01 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0785× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 36.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -8.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -10.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.247× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +9.4) | — |
| [[A-172 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB-AS1]] | +0.71 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[LINC00571]] | +0.69 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CLHC1]] | +0.69 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.67 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RFX3-DT]] | +0.67 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[RAB30-DT]] | +0.67 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.67 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[ST7L]] | +0.67 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.66 | +0.57 / +0.26 | both halves | 4e-04 |  |
| [[INO80D]] | +0.66 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[GABPB2]] | +0.66 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ERMAP]] | +0.65 | +0.58 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPT]] | -0.69 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.67 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[YIF1B]] | -0.66 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[HDAC3]] | -0.66 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[PDXP]] | -0.66 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ATP7B]] | -0.65 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[VKORC1]] | -0.65 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MMS19]] | -0.64 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[UBE2O]] | -0.64 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[STK32C]] | -0.64 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[EFNA3]] | -0.63 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ARL3]] | -0.62 | -0.41 / -0.59 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF69]] | B | ZNF69 activity raises ARMCX4's level | lines that do not express ZNF69 (15) vs lines expressing it (35) | 3.15× lower at baseline in the lines without ZNF69 | 0.010 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, TNFRSF14-AS1, CIART |
| [[ZNF91]] | B | ZNF91 activity raises ARMCX4's level | lines that do not express ZNF91 (6) vs lines expressing it (44) | 2.73× lower at baseline in the lines without ZNF91 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF493 |
| [[TBX15]] | B | TBX15 activity raises ARMCX4's level | lines that do not express TBX15 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without TBX15 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MTMR9LP]] | C | MTMR9LP activity raises ARMCX4's level | lines that do not express MTMR9LP (9) vs lines expressing it (41) | 4.84× lower at baseline in the lines without MTMR9LP | 0.005 | ⚠ within organs, on part of the lines; also absent: SMAD7, TNFRSF21, TNFRSF14; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF69]] | B | ARMCX4 activity raises ZNF69's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without ARMCX4 | 0.008 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[GALNT16]] | B | ARMCX4 activity lowers GALNT16's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.54× higher at baseline in the lines without ARMCX4 | 0.019 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[EFNA3]] | B | ARMCX4 activity lowers EFNA3's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.47× higher at baseline in the lines without ARMCX4 | 0.019 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[TSR2]] | B | ARMCX4 activity raises TSR2's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.26× lower at baseline in the lines without ARMCX4 | 0.056 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[ZNF91]] | B | ARMCX4 activity raises ZNF91's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without ARMCX4 | 0.067 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[FAM117B]] | B | ARMCX4 activity weakens FAM117B's drug response | lines that do not express ARMCX4 (18) vs lines expressing it (31) | the lines without ARMCX4 respond 1.27× as strongly (z diff -1.28); strongest at Digitoxin 5 µM: 0.42x vs 0.63x (z diff -3.2) | 0.070 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC; target measured in part of the lines; artifact flags |
| [[ZNF626]] | B | ARMCX4 activity raises ZNF626's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without ARMCX4 | 0.089 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[MTMR9LP]] | C | ARMCX4 activity raises MTMR9LP's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without ARMCX4 | 0.001 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC; co-absent with the target |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (4.7, 8.1); signed map (17.8, -25.3). **Vector** length 68.6, 16.5% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.5 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.2 | -12.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.6 | -10.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.1 | -12.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing X-linked 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,418,287-101,533,459 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40053, GASP4; previously CXorf35 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

UniProt [Q5H9R4](https://www.uniprot.org/uniprotkb/Q5H9R4) carries no function annotation.

**Summary**, from NCBI Gene [100131755](https://www.ncbi.nlm.nih.gov/gene/100131755):

> The product of this gene belongs to the armadillo repeat-containing family of proteins, which interact with other proteins in a variety of cellular processes. The function of this family member is currently unknown. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:28615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28615) · Entrez [100131755](https://www.ncbi.nlm.nih.gov/gene/100131755) · UniProt [Q5H9R4](https://www.uniprot.org/uniprotkb/Q5H9R4) · Ensembl [ENSG00000196440](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196440)

## Data

Gene col 12206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12206); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12206]; `tensor/DDL_lfc|DDL_z.npy` [12206]; `embed/gene_vectors.npy` [12206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12206 or target_col == 12206). Every well: [[ARMCX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMCX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

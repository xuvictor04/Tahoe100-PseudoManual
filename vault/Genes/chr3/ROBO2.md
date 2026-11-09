---
symbol: "ROBO2"
type: "gene"
col: 11606
ensembl_id: "ENSG00000185008"
name: "roundabout guidance receptor 2"
location: "3p12.3"
module: 27
arm: "+"
pooled_cpm: 246.85
n_lines_expressing: 12
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 16
direction_downstream: 25
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ROBO2

*roundabout guidance receptor 2* — 3p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.14× (z +7.5, q 2e-11, up in 0 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +7.5, q 2e-11, up in 0 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (H4 4.92×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.499× (z -6.8, q 7e-09, down in 8 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGF20]] (+0.64, fdr 7e-06), [[HS3ST5]] (+0.59, fdr 1e-05), [[CSMD3]] (+0.56, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[FIRRE]] → it (grade B ⚠); 25 go from it, the strongest it → [[ZFPM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11606.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (H4 4.92×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.5 | 2e-11 | 0/11 | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.5 | 2e-11 | 0/11 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.4 | 2e-05 | 0/10 | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.090 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.25× | +3.2 | 0.15 | 3/10 (SK-MEL-2, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.499×** | -6.8 | 7e-09 | 8/10 (H4, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.532×** | -6.1 | 2e-07 | 9/10 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.556×** | -5.7 | 2e-06 | 8/10 (SW480, A-427, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.574×** | -5.4 | 9e-06 | 6/10 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.625×** | -4.6 | 6e-04 | 5/10 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.659×** | -4.0 | 0.005 | 9/10 (SW480, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -3.6 | 0.027 | 7/10 (CHP-212, LoVo, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.503×** | -3.5 | 0.029 | 8/10 (A-427, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.687×** | -3.5 | 0.029 | 10/10 (SW480, A-427, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.700×** | -3.5 | 0.032 | 8/10 (SW480, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.713×** | -3.3 | 0.055 | 7/10 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.720×** | -3.2 | 0.071 | 5/10 (H4, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1,911 | 0 | 20 (13 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0266× (z -24.8) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0956× (z -22.7) |
| [[A-427 (line)]] | wt | 1,113 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -14.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LoVo (line)]] | wt | 129 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.1) |
| [[NCI-H2030 (line)]] | alt | 2,755 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -18.9) |
| [[H4 (line)]] | wt | 175 | 1 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 4.92× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 599 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 50.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 24.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 29.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 22.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 27.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 32.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 28.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 41.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 32.3 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 27.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 24.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.2 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 23.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 371 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 24.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 60.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 27.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 48.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 38.7 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 30.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 30.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGF20]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[HS3ST5]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CSMD3]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 | STRING 502 |
| [[APCDD1]] | +0.55 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[COLGALT2]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[NETO1]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[NELL2]] | +0.53 | +0.44 / +0.44 | both halves | 3e-05 | pathway: Regulation of commissural axon pathfinding by SLIT and ROBO; STRING 689 |
| [[MIR3667HG]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ST18]] | +0.52 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[JAKMIP2-AS1]] | +0.52 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[BMP5]] | +0.51 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[CDK15]] | +0.51 | +0.54 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 2, C 14. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FIRRE]] | B | FIRRE activity raises ROBO2's level | lines that do not express FIRRE (18) vs lines expressing it (32) | 2.62× lower at baseline in the lines without FIRRE | 0.045 | ⚠ within organs, on part of the lines; also absent: HMCN1, GAP43, ENSG00000286033 |
| [[MLPH]] | B | MLPH activity lowers ROBO2's level | lines that do not express MLPH (13) vs lines expressing it (37) | 2.89× higher at baseline in the lines without MLPH | 0.049 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[NTM]] | C | NTM activity raises ROBO2's level | lines that do not express NTM (33) vs lines expressing it (17) | 3.40× lower at baseline in the lines without NTM | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[ZFHX4-AS1]] | C | ZFHX4-AS1 activity raises ROBO2's level | lines that do not express ZFHX4-AS1 (29) vs lines expressing it (21) | 3.01× lower at baseline in the lines without ZFHX4-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PCDH17, LRCH2, GNAT3; maybe low, not absent; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises ROBO2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 4.16× lower at baseline in the lines without CSMD3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises ROBO2's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 3.15× lower at baseline in the lines without MGAT4C | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises ROBO2's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 3.80× lower at baseline in the lines without PSG1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[SOX5]] | C | SOX5 activity raises ROBO2's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 2.65× lower at baseline in the lines without SOX5 | 0.031 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises ROBO2's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 6.70× lower at baseline in the lines without NETO1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises ROBO2's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 2.56× lower at baseline in the lines without LINC02616 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises ROBO2's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 2.93× lower at baseline in the lines without EPHA5 | 0.060 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises ROBO2's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.39× lower at baseline in the lines without CDH10 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 5, C 20. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFPM2]] | B | ROBO2 activity raises ZFPM2's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 3.14× lower at baseline in the lines without ROBO2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |
| [[DKK2]] | B | ROBO2 activity raises DKK2's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.68× lower at baseline in the lines without ROBO2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |
| [[ADAMTS19]] | B | ROBO2 activity raises ADAMTS19's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.75× lower at baseline in the lines without ROBO2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |
| [[DMD]] | B | ROBO2 activity raises DMD's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.86× lower at baseline in the lines without ROBO2 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |
| [[FIRRE]] | B | ROBO2 activity raises FIRRE's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.64× lower at baseline in the lines without ROBO2 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |
| [[MIR99AHG]] | C | ROBO2 activity raises MIR99AHG's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 4.42× lower at baseline in the lines without ROBO2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[NTM]] | C | ROBO2 activity raises NTM's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 4.47× lower at baseline in the lines without ROBO2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[ZFHX4-AS1]] | C | ROBO2 activity raises ZFHX4-AS1's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 3.00× lower at baseline in the lines without ROBO2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[EPHA5]] | C | ROBO2 activity raises EPHA5's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 4.44× lower at baseline in the lines without ROBO2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[CSMD3]] | C | ROBO2 activity raises CSMD3's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 6.72× lower at baseline in the lines without ROBO2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[COLGALT2]] | C | ROBO2 activity raises COLGALT2's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.94× lower at baseline in the lines without ROBO2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[PCDH9]] | C | ROBO2 activity raises PCDH9's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 4.72× lower at baseline in the lines without ROBO2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, 41.4); signed map (63.3, 17.7). **Vector** length 48.2, 16.7% of its response variance represented; |z| ≥ 3 in 373 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | -0.9 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | roundabout guidance receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p12.3 — chr3:75,906,695-77,649,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1568 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family; Roundabout guidance receptor family |
| Reactome | 9 pathways, smallest: Regulation of cortical dendrite branching; ROBO receptors bind AKAP5; Regulation of commissural axon pathfinding by SLIT and ROBO |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCK4](https://www.uniprot.org/uniprotkb/Q9HCK4) (Roundabout homolog 2):

> Receptor for SLIT2, and probably SLIT1, which are thought to act as molecular guidance cue in cellular migration, including axonal navigation at the ventral midline of the neural tube and projection of axons to different regions during neuronal development.

**Summary**, from NCBI Gene [6092](https://www.ncbi.nlm.nih.gov/gene/6092):

> The protein encoded by this gene belongs to the ROBO family, part of the immunoglobulin superfamily of proteins that are highly conserved from fly to human. The encoded protein is a transmembrane receptor for the slit homolog 2 protein and functions in axon guidance and cell migration. Mutations in this gene are associated with vesicoureteral reflux, characterized by the backward flow of urine from the bladder into the ureters or the kidney. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:10250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10250) · Entrez [6092](https://www.ncbi.nlm.nih.gov/gene/6092) · UniProt [Q9HCK4](https://www.uniprot.org/uniprotkb/Q9HCK4) · Ensembl [ENSG00000185008](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185008)

## Data

Gene col 11606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11606); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11606]; `tensor/DDL_lfc|DDL_z.npy` [11606]; `embed/gene_vectors.npy` [11606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11606 or target_col == 11606). Every well: [[ROBO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROBO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

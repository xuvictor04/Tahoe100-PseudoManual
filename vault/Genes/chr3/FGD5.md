---
symbol: "FGD5"
type: "gene"
col: 7839
ensembl_id: "ENSG00000154783"
name: "FYVE, RhoGEF and PH domain containing 5"
location: "3p25.1"
module: 27
arm: "+"
pooled_cpm: 8.83
n_lines_expressing: 13
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 35
direction_downstream: 49
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# FGD5

*FYVE, RhoGEF and PH domain containing 5* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.71× (z +10.3, q 3e-22, up in 1 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.518× (z -4.8, q 6e-04, down in 9 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (SW1417 0.0502×, BT-474 0.0440×, SW480 0.319×); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 0.0680×, COLO 205 0.0880×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.170×, COLO 205 0.256×); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.0891×, COLO 205 0.134×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GJB1]] (+0.74, fdr 7e-06), [[VWA2]] (+0.74, fdr 7e-06), [[IL20RA]] (+0.73, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[DMRTA1]] → it (grade B ⚠); 49 go from it, the strongest it → [[TLDC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +10.3 | 3e-22 | 1/9 (RPMI-7951) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +8.9 | 1e-16 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +7.5 | 8e-12 | 1/6 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +6.8 | 2e-09 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +4.0 | 0.007 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.065 | 1/10 (RPMI-7951) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.2 | 0.098 | 0/9 | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.52× | +3.1 | 0.14 | 3/9 (AsPC-1, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7839.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (SW1417 0.0502×, BT-474 0.0440×, SW480 0.319×); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 0.0680×, COLO 205 0.0880×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.170×, COLO 205 0.256×); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.0891×, COLO 205 0.134×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.518×** | -4.8 | 6e-04 | 9/10 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.525×** | -4.7 | 6e-04 | 9/10 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.651× | -3.0 | 0.34 | 3/10 (LS 180, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 88.6 | 0 | 19 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0680× (z -20.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.170× (z -19.4) |
| [[COLO 205 (line)]] | alt | 152 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0809× (z -17.6) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.134× (z -14.0) |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 3 (1 ⚠) | — | [[Neratinib (drug)]] 5 µM 0.0337× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -9.0) ⚠ cell-cycle shift, explains ~88% of this change |
| [[SW1417 (line)]] | alt | 6.46 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0502× (z -11.7) |
| [[LS 180 (line)]] | wt | 3.72 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0492× (z -9.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GJB1]] | +0.74 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[VWA2]] | +0.74 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.73 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[PROX1]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC02058]] | +0.72 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[MPZL2]] | +0.72 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.71 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[CLRN3]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[LGR6]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.69 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PROX1-AS1]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 1, C 34. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMRTA1]] | B | DMRTA1 activity raises FGD5's level | lines that do not express DMRTA1 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without DMRTA1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN |
| [[RMST]] | C | RMST activity raises FGD5's level | lines that do not express RMST (35) vs lines expressing it (15) | 2.51× lower at baseline in the lines without RMST | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises FGD5's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.88× lower at baseline in the lines without KRT23 | 0.009 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[HSD17B2]] | C | HSD17B2 activity raises FGD5's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.39× lower at baseline in the lines without HSD17B2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises FGD5's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.43× lower at baseline in the lines without TFF3 | 0.010 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises FGD5's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.89× lower at baseline in the lines without PSG1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises FGD5's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 4.06× lower at baseline in the lines without CLRN3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[FGF19]] | C | FGF19 activity raises FGD5's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 4.49× lower at baseline in the lines without FGF19 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises FGD5's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without LINC01819 | 0.018 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[EDAR]] | C | EDAR activity raises FGD5's level | lines that do not express EDAR (36) vs lines expressing it (14) | 3.38× lower at baseline in the lines without EDAR | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |
| [[MYO7B]] | C | MYO7B activity raises FGD5's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without MYO7B | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1; co-absent with the target |
| [[C9orf152]] | C | C9orf152 activity raises FGD5's level | lines that do not express C9orf152 (32) vs lines expressing it (18) | 2.46× lower at baseline in the lines without C9orf152 | 0.021 | ⚠ within organs, on part of the lines; also absent: AGR3, MYO7B, KRT17; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 7, C 42. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLDC2]] | B | FGD5 activity raises TLDC2's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.33× lower at baseline in the lines without FGD5 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[HUNK]] | B | FGD5 activity raises HUNK's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.53× lower at baseline in the lines without FGD5 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[LASTR]] | B | FGD5 activity raises LASTR's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.20× lower at baseline in the lines without FGD5 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[RHOXF1-AS1]] | B | FGD5 activity raises RHOXF1-AS1's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 1.36× lower at baseline in the lines without FGD5 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[LINC01622]] | B | FGD5 activity raises LINC01622's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 1.36× lower at baseline in the lines without FGD5 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[ZNF503-AS1]] | B | FGD5 activity raises ZNF503-AS1's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without FGD5 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[DZIP1L]] | B | FGD5 activity lowers DZIP1L's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.14× higher at baseline in the lines without FGD5 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[NKD1]] | C | FGD5 activity raises NKD1's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 3.13× lower at baseline in the lines without FGD5 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |
| [[CLRN3]] | C | FGD5 activity raises CLRN3's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.52× lower at baseline in the lines without FGD5 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |
| [[IL20RA]] | C | FGD5 activity raises IL20RA's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 3.71× lower at baseline in the lines without FGD5 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |
| [[VIL1]] | C | FGD5 activity raises VIL1's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.61× lower at baseline in the lines without FGD5 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |
| [[EPS8L3]] | C | FGD5 activity raises EPS8L3's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 3.55× lower at baseline in the lines without FGD5 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.2, 44.9); signed map (63.3, 14.1). **Vector** length 52.8, 22.0% of its response variance represented; |z| ≥ 3 in 334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | FYVE, RhoGEF and PH domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,810,853-14,934,571 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZFYVE23, FLJ39957, FLJ00274 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 4 pathways, smallest: RAC1 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZNL6](https://www.uniprot.org/uniprotkb/Q6ZNL6) (FYVE, RhoGEF and PH domain-containing protein 5):

> Activates CDC42, a member of the Ras-like family of Rho- and Rac proteins, by exchanging bound GDP for free GTP. Mediates VEGF-induced CDC42 activation. May regulate pro-angiogenic action of VEGF in vascular endothelial cells, including network formation, directional movement and proliferation. May play a role in regulating the actin cytoskeleton and cell shape.

**Summary**, from NCBI Gene [152273](https://www.ncbi.nlm.nih.gov/gene/152273):

> Predicted to enable guanyl-nucleotide exchange factor activity and small GTPase binding activity. Predicted to be involved in actin cytoskeleton organization; filopodium assembly; and regulation of cell shape. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19117) · Entrez [152273](https://www.ncbi.nlm.nih.gov/gene/152273) · UniProt [Q6ZNL6](https://www.uniprot.org/uniprotkb/Q6ZNL6) · Ensembl [ENSG00000154783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154783)

## Data

Gene col 7839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7839); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7839]; `tensor/DDL_lfc|DDL_z.npy` [7839]; `embed/gene_vectors.npy` [7839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7839 or target_col == 7839). Every well: [[FGD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

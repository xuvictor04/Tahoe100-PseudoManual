---
symbol: "PYGO1"
type: "gene"
col: 10039
ensembl_id: "ENSG00000171016"
name: "pygopus family PHD finger 1"
location: "15q21.3"
module: 18
arm: "+"
pooled_cpm: 12.43
n_lines_expressing: 34
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 7
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PYGO1

*pygopus family PHD finger 1* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.43× (z +6.2, q 3e-07, up in 19 of 32 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.46× (z +4.6, q 9e-04, up in 15 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.294× (z -15.0, q 0e+00, down in 24 of 31 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POU6F1]] (+0.67, fdr 3e-05), [[FGF2]] (+0.66, fdr 2e-05), [[USP46]] (+0.63, fdr 1e-05); moves opposite to [[CASP9]] (-0.60, fdr 6e-05), [[GBF1]] (-0.56, fdr 1e-04), [[FBXO33]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SIRPA]] → it (grade B ⚠); 7 go from it, the strongest it → [[PRDM5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.43×** | +6.2 | 3e-07 | 19/32 (SK-MEL-2, PANC-1, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +5.2 | 7e-05 | 20/31 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 9e-04 | 15/31 (HOP62, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.4 | 0.002 | 9/21 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.005 | 11/31 (NCI-H2347, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.0 | 0.005 | 8/29 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.041 | 14/31 (H4, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.32×** | +3.2 | 0.088 | 10/32 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.294×** | -15.0 | 0e+00 | 24/31 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.297×** | -14.9 | 0e+00 | 25/31 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.395×** | -11.4 | 1e-27 | 25/31 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.473×** | -4.8 | 2e-04 | 15/32 (AN3 CA, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Malotilate (drug)]] 0.05 µM |  | **0.750×** | -3.5 | 0.046 | 11/31 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.754×** | -3.5 | 0.048 | 17/31 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.743×** | -3.4 | 0.054 | 12/31 (A-172, C-33 A, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.760× | -3.1 | 0.12 | 12/30 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.616× | -3.1 | 0.12 | 10/30 (H4, NCI-H23, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0499× (z -21.5) |
| [[SNU-423 (line)]] | alt | 23.7 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.136× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 32.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -18.1) |
| [[SNU-1 (line)]] | wt | 69.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.152× (z -12.3) |
| [[A-172 (line)]] | wt | 37.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0963× (z -19.5) |
| [[A498 (line)]] | wt | 31.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -16.5) |
| [[A549 (line)]] | wt | 36.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0923× (z -18.2) |
| [[C-33 A (line)]] | alt | 49.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -15.2) |
| [[A-427 (line)]] | wt | 28.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.307× (z -9.0) |
| [[C32 (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0849× (z -10.5) |
| [[H4 (line)]] | wt | 19.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0559× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -12.2) |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.111× (z -8.9) |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.898 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU6F1]] | +0.67 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[FGF2]] | +0.66 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[USP46]] | +0.63 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[FAM169A]] | +0.62 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SNHG26]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[NSMAF]] | +0.61 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[METTL8]] | +0.60 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[TBKBP1]] | +0.60 | +0.49 / +0.37 | both halves | 9e-05 |  |
| [[PRDM11]] | +0.60 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[HDGFL3]] | +0.59 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[HACD1]] | +0.59 | +0.55 / +0.28 | both halves | 3e-04 |  |
| [[NDST1]] | +0.58 | +0.38 / +0.49 | both halves | 7e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP9]] | -0.60 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[GBF1]] | -0.56 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[FBXO33]] | -0.55 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[CARHSP1]] | -0.55 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[DNAAF3]] | -0.54 | -0.22 / -0.35 | both halves | 6e-04 |  |
| [[RAB3A]] | -0.54 | -0.44 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[LGALS1]] | -0.53 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[MTMR14]] | -0.53 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[ORC4]] | -0.53 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[GNAI2]] | -0.53 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD37]] | -0.52 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[HEATR5B]] | -0.51 | -0.42 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[TRPT1]] | -0.51 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[NDRG1]] | -0.51 | -0.47 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRPA]] | B | SIRPA activity raises PYGO1's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 4.76× lower at baseline in the lines without SIRPA | 0.023 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[TENM3-AS1]] | B | TENM3-AS1 activity raises PYGO1's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without TENM3-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[SLC2A3]] | B | SLC2A3 activity raises PYGO1's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 3.23× lower at baseline in the lines without SLC2A3 | 0.061 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[TXLNGY]], [[TXLNGY-1]] | B | TXLNGY, TXLNGY-1 activity raises PYGO1's level | lines that do not express TXLNGY, TXLNGY-1 (30) vs lines expressing them (20) | 2.28× lower at baseline in the lines without TXLNGY, TXLNGY-1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent genes |
| [[HDAC6]] | B | HDAC6 activity raises PYGO1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NCS1]] | B | NCS1 activity raises PYGO1's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 4.31× lower at baseline in the lines without NCS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[FGF2]] | C | FGF2 activity raises PYGO1's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 3.73× lower at baseline in the lines without FGF2 | 0.034 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2; co-absent with the target |
| [[TTC28]] | C | TTC28 activity raises PYGO1's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 5.09× lower at baseline in the lines without TTC28 | 0.054 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1; co-absent with the target |
| [[HECW2]] | C | HECW2 activity raises PYGO1's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 4.14× lower at baseline in the lines without HECW2 | 0.065 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041; co-absent with the target |
| [[DZIP1L]] | C | DZIP1L activity raises PYGO1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 5.18× lower at baseline in the lines without DZIP1L | 0.097 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM5]] | B | PYGO1 activity raises PRDM5's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 2.59× lower at baseline in the lines without PYGO1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[CHST3]] | B | PYGO1 activity raises CHST3's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 2.00× lower at baseline in the lines without PYGO1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[NDST1]] | B | PYGO1 activity raises NDST1's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without PYGO1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[HECTD2]] | B | PYGO1 activity raises HECTD2's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 2.62× lower at baseline in the lines without PYGO1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[SLC16A1-AS1]] | B | PYGO1 activity raises SLC16A1-AS1's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without PYGO1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[SLC2A3]] | B | PYGO1 activity raises SLC2A3's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 3.42× lower at baseline in the lines without PYGO1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[FGF2]] | C | PYGO1 activity raises FGF2's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 4.63× lower at baseline in the lines without PYGO1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1; co-absent with the target |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.3, 11.4); signed map (24.0, -38.4). **Vector** length 77.9, 18.8% of its response variance represented; |z| ≥ 3 in 662 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.7 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -14.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -15.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -11.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | pygopus family PHD finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:55,538,884-55,588,947 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PHD finger proteins; Wnt enhanceosome complex |
| Reactome | 4 pathways, smallest: Deactivation of the beta-catenin transactivating complex; Formation of the beta-catenin:TCF transactivating complex; TCF dependent signaling in response to WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3Y4](https://www.uniprot.org/uniprotkb/Q9Y3Y4) (Pygopus homolog 1):

> Involved in signal transduction through the Wnt pathway.

**Summary**, from NCBI Gene [26108](https://www.ncbi.nlm.nih.gov/gene/26108):

> Enables histone H3K4me3 reader activity. Predicted to be involved in kidney development and spermatid nucleus differentiation. Predicted to act upstream of or within several processes, including hematopoietic progenitor cell differentiation; positive regulation of transcription by RNA polymerase II; and spermatid development. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30256) · Entrez [26108](https://www.ncbi.nlm.nih.gov/gene/26108) · UniProt [Q9Y3Y4](https://www.uniprot.org/uniprotkb/Q9Y3Y4) · Ensembl [ENSG00000171016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171016)

## Data

Gene col 10039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10039); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10039]; `tensor/DDL_lfc|DDL_z.npy` [10039]; `embed/gene_vectors.npy` [10039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10039 or target_col == 10039). Every well: [[PYGO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYGO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

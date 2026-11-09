---
symbol: "BOC"
type: "gene"
col: 6939
ensembl_id: "ENSG00000144857"
name: "BOC cell adhesion associated, oncogene regulated"
location: "3q13.2"
module: 13
arm: "+"
pooled_cpm: 5.16
n_lines_expressing: 29
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 24
direction_downstream: 6
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# BOC

*BOC cell adhesion associated, oncogene regulated* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.93× (z +7.5, q 4e-11, up in 0 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +6.4, q 4e-08, up in 6 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.446× (z -9.5, q 8e-19, down in 19 of 27 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETBP1]] (+0.57, fdr 1e-05), [[LOXL3]] (+0.56, fdr 1e-05), [[MDGA2]] (+0.55, fdr 2e-05); moves opposite to [[PATJ]] (-0.41, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[INSYN2B]] → it (grade B ⚠); 6 go from it, the strongest it → [[GBX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +7.5 | 4e-11 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.4 | 4e-08 | 6/23 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.2 | 5e-05 | 3/16 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +4.3 | 0.003 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.2 | 0.003 | 1/11 (A549) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.007 | 5/25 (SW480, SNU-423, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.007 | 7/26 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.036 | 6/25 (HEC-1-A, SNU-1, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.063 | 1/20 (A549) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.446×** | -9.5 | 8e-19 | 19/27 (A-172, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.456×** | -9.3 | 6e-18 | 22/27 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.515×** | -7.8 | 9e-13 | 17/26 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.541×** | -7.2 | 7e-11 | 16/26 (A-172, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.567×** | -6.7 | 3e-09 | 16/26 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -6.2 | 4e-08 | 17/22 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.603×** | -6.0 | 2e-07 | 12/26 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.664×** | -4.8 | 1e-04 | 16/26 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.467×** | -4.7 | 2e-04 | 9/26 (HS-578T, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.530×** | -3.9 | 0.005 | 12/22 (HEC-1-A, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -3.5 | 0.020 | 8/25 (A-172, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.733×** | -3.5 | 0.021 | 14/24 (A-172, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.570×** | -3.5 | 0.023 | 7/24 (C32, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.750×** | -3.4 | 0.029 | 9/27 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.673×** | -3.3 | 0.033 | 1/27 (SW 1088) | rises with dose | noisy plate (z scaled) |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.769×** | -3.1 | 0.070 | 2/25 (H4, HCT15) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.611×** | -3.0 | 0.079 | 7/21 (A-172, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.613×** | -3.0 | 0.080 | 4/22 (NCI-H1792, H4, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 195 | 0 | 10 (6 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0128× (z -21.1) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0586× (z -14.3) |
| [[A-172 (line)]] | wt | 32.5 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0658× (z -27.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0660× (z -19.5) |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0684× (z -12.3) |
| [[C32 (line)]] | wt | 13.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0884× (z -15.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.112× (z -9.0) |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0892× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 4.20 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0786× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.113× (z -13.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.220× (z -9.0) |
| [[H4 (line)]] | wt | 12.0 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0898× (z -8.8) |
| [[SW480 (line)]] | alt | 4.87 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -8.7) |
| [[A-427 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.787 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.682 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETBP1]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LOXL3]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 | same gene group |
| [[FZD1]] | +0.55 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[SDC2]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[CACNA2D2]] | +0.53 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[STK32B]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[INSYN2B]] | +0.52 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[COL1A2]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[CTHRC1]] | +0.51 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[TCF7L1]] | +0.51 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[AEBP1]] | +0.50 | +0.42 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATJ]] | -0.41 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 15, C 9. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INSYN2B]] | B | INSYN2B activity raises BOC's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.38× lower at baseline in the lines without INSYN2B | 0.022 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[APOBEC3G]] | B | APOBEC3G activity raises BOC's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 1.43× lower at baseline in the lines without APOBEC3G | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3 |
| [[FRMD4A]] | B | FRMD4A activity raises BOC's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 1.71× lower at baseline in the lines without FRMD4A | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[CYGB]] | B | CYGB activity raises BOC's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.49× lower at baseline in the lines without CYGB | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[GBX1]] | B | GBX1 activity raises BOC's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.99× lower at baseline in the lines without GBX1 | 0.068 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[COL15A1]] | B | COL15A1 activity raises BOC's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without COL15A1 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[APCDD1L]] | B | APCDD1L activity raises BOC's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.49× lower at baseline in the lines without APCDD1L | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[EDNRA]] | B | EDNRA activity raises BOC's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without EDNRA | 0.083 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[FLT1]] | B | FLT1 activity raises BOC's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without FLT1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[TWIST2]] | B | TWIST2 activity raises BOC's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without TWIST2 | 0.093 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1 |
| [[PATJ]] | B | PATJ activity lowers BOC's level | lines that do not express PATJ (9) vs lines expressing it (41) | 1.66× higher at baseline in the lines without PATJ | 0.093 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent |
| [[ISM2]] | B | ISM2 activity raises BOC's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 2.31× lower at baseline in the lines without ISM2 | 0.095 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBX1]] | B | BOC activity raises GBX1's level | lines that do not express BOC (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without BOC | 0.039 | ⚠ within organs, on part of the lines; also absent: VSTM4, PIEZO2, ARNT2 |
| [[GRIK4]] | C | BOC activity raises GRIK4's level | lines that do not express BOC (21) vs lines expressing it (29) | 2.39× lower at baseline in the lines without BOC | 0.026 | ⚠ within organs, on part of the lines; also absent: VSTM4, PIEZO2, ARNT2; co-absent with the target |
| [[FAM20C]] | C | BOC activity raises FAM20C's level | lines that do not express BOC (21) vs lines expressing it (29) | 4.86× lower at baseline in the lines without BOC | 0.037 | ⚠ within organs, on part of the lines; also absent: VSTM4, PIEZO2, ARNT2; co-absent with the target |
| [[MRC2]] | C | BOC activity raises MRC2's level | lines that do not express BOC (21) vs lines expressing it (29) | 3.33× lower at baseline in the lines without BOC | 0.045 | ⚠ within organs, on part of the lines; also absent: VSTM4, PIEZO2, ARNT2; co-absent with the target |
| [[VSTM4]] | C | BOC activity raises VSTM4's level | lines that do not express BOC (21) vs lines expressing it (29) | 3.08× lower at baseline in the lines without BOC | 0.054 | ⚠ within organs, on part of the lines; also absent: VSTM4, PIEZO2, ARNT2; co-absent with the target |
| [[TCF7L1]] | C | BOC activity raises TCF7L1's level | lines that do not express BOC (21) vs lines expressing it (29) | 2.62× lower at baseline in the lines without BOC | 0.082 | ⚠ within organs, on part of the lines; also absent: VSTM4, PIEZO2, ARNT2; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.9, 26.9); signed map (27.9, 40.8). **Vector** length 52.6, 9.69% of its response variance represented; |z| ≥ 3 in 703 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -6.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.8 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -7.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | BOC cell adhesion associated, oncogene regulated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:113,211,003-113,287,459 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDON2, Boi |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Reactome | 6 pathways, smallest: Ligand-receptor interactions; GLI proteins bind promoters of Hh responsive genes to promote transcription; Activation of SMO |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWV1](https://www.uniprot.org/uniprotkb/Q9BWV1) (Brother of CDO):

> Together with CDON, forms a coreceptor required for sonic hedgehog (SHH) handoff to its patched receptor (PTCH1 or PTCH2), thereby allowing activation of the smoothened signaling pathway (By similarity). Binds to the dually lipid-modified Sonic hedgehog protein N-product (ShhN) downstream of SCUBE2 carrier and promotes its release to GAS1 (By similarity). ShhN is then directly transferred to patched receptor by GAS1 (By similarity). May also mediate cell-cell interactions between muscle …

**Summary**, from NCBI Gene [91653](https://www.ncbi.nlm.nih.gov/gene/91653):

> The protein encoded by this gene is a member of the immunoglobulin/fibronectin type III repeat family. It is a component of a cell-surface receptor complex that mediates cell-cell interactions between muscle precursor cells, and promotes myogenic differentiation. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:17173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17173) · Entrez [91653](https://www.ncbi.nlm.nih.gov/gene/91653) · UniProt [Q9BWV1](https://www.uniprot.org/uniprotkb/Q9BWV1) · Ensembl [ENSG00000144857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144857)

## Data

Gene col 6939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6939); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6939]; `tensor/DDL_lfc|DDL_z.npy` [6939]; `embed/gene_vectors.npy` [6939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6939 or target_col == 6939). Every well: [[BOC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BOC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

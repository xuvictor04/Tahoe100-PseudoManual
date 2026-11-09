---
symbol: "FZD1"
type: "gene"
col: 8056
ensembl_id: "ENSG00000157240"
name: "frizzled class receptor 1"
location: "7q21.13"
module: 87
arm: "+"
pooled_cpm: 2.92
n_lines_expressing: 44
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# FZD1

*frizzled class receptor 1* — 7q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +9.6, q 4e-19, up in 23 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.492× (z -6.6, q 2e-08, down in 17 of 35 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEF1]] (+0.64, fdr 8e-06), [[FCRLA]] (+0.64, fdr 3e-05), [[C10orf90]] (+0.63, fdr 1e-05); moves opposite to [[PATJ]] (-0.50, fdr 2e-05), [[EMC2]] (-0.46, fdr 5e-05), [[KCP]] (-0.44, fdr 9e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TRIM9]] → it (grade B ⚠); 9 go from it, the strongest it → [[CEP85L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +9.6 | 4e-19 | 23/31 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.14×** | +6.9 | 2e-09 | 1/4 (CFPAC-1) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +5.9 | 7e-07 | 15/39 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.7 | 2e-06 | 6/17 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.9 | 1e-04 | 12/38 (SW1417, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.66×** | +4.4 | 0.001 | 2/5 (A498, CFPAC-1) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.59×** | +4.3 | 0.001 | 2/17 (hTERT-HPNE, J82) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.53×** | +4.0 | 0.004 | 8/40 (PANC-1, RKO, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.52×** | +3.9 | 0.005 | 10/38 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.7 | 0.011 | 4/17 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.47×** | +3.6 | 0.014 | 10/38 (CFPAC-1, HEC-1-A, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.051 | 11/33 (BT-474, SW480, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.089 | 4/38 (RPMI-7951, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.492×** | -6.6 | 2e-08 | 17/35 (A498, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.513×** | -6.2 | 1e-07 | 18/37 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.567×** | -5.3 | 2e-05 | 18/31 (LoVo, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.690×** | -4.9 | 2e-04 | 14/36 (PANC-1, SHP-77, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.630×** | -4.3 | 0.002 | 9/39 (C32, A498, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.628×** | -4.2 | 0.003 | 13/30 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.644×** | -4.1 | 0.003 | 14/40 (SNU-423, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.657×** | -3.7 | 0.016 | 10/36 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.690×** | -3.4 | 0.036 | 8/39 (RKO, SW48, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.701×** | -3.3 | 0.054 | 13/33 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.792× | -3.1 | 0.12 | 10/39 (SW480, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.714× | -3.0 | 0.12 | 13/32 (NCI-H2030, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 20.5 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.0863× (z -11.3) |
| [[A-172 (line)]] | wt | 4.63 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0378× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 5.96 | 0 | 2 (1 ⚠) | — | [[Budesonide (drug)]] 0.5 µM 0.0348× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 3.68 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0495× (z -9.9) |
| [[SW480 (line)]] | alt | 1.69 | 0 | 2 | — | [[Methotrexate (drug)]] 0.05 µM 0.0766× (z -9.1) |
| [[LoVo (line)]] | wt | 2.52 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0716× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 5.26 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0733× (z -9.3) |
| [[A-427 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.857 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.820 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.975 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEF1]] | +0.64 | +0.60 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_WNT_BETA_CATENIN_SIGNALING; STRING 579 |
| [[FCRLA]] | +0.64 | +0.53 / +0.44 | both halves | 3e-05 | **novel candidate** |
| [[C10orf90]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SETBP1]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PCDHGC3]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[AEBP1]] | +0.58 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[COL19A1]] | +0.56 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[BOC]] | +0.55 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[A2M]] | +0.54 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[LEF1-AS1]] | +0.53 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[EFR3B]] | +0.53 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SDC2]] | +0.52 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATJ]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[EMC2]] | -0.46 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[KCP]] | -0.44 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[NSA2]] | -0.42 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[TPCN2]] | -0.42 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[TMEM260]] | -0.41 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[TATDN1]] | -0.41 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[TTC1]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[MRPL23]] | -0.40 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[EPB41]] | -0.40 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[MTRF1]] | -0.40 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[TM2D1]] | -0.40 | -0.36 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM9]] | B | TRIM9 activity raises FZD1's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without TRIM9 | 0.008 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[DPYSL3]] | B | DPYSL3 activity raises FZD1's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 1.70× lower at baseline in the lines without DPYSL3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[SAMMSON]] | B | SAMMSON activity raises FZD1's level | lines that do not express SAMMSON (34) vs lines expressing it (16) | 1.75× lower at baseline in the lines without SAMMSON | 0.048 | ⚠ within organs, on part of the lines; also absent: MSR1, ENSG00000286523, PDE1A |
| [[PCDHGC3]] | B | PCDHGC3 activity raises FZD1's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 1.70× lower at baseline in the lines without PCDHGC3 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P |
| [[MIR3681HG]] | B | MIR3681HG activity raises FZD1's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without MIR3681HG | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[LEF1]] | B | LEF1 activity raises FZD1's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.51× lower at baseline in the lines without LEF1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[LOXL3]] | B | LOXL3 activity raises FZD1's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 1.40× lower at baseline in the lines without LOXL3 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[AEBP1]] | B | AEBP1 activity raises FZD1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 1.81× lower at baseline in the lines without AEBP1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEP85L]] | B | FZD1 activity raises CEP85L's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 3.05× lower at baseline in the lines without FZD1 | 0.032 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[SETBP1]] | B | FZD1 activity raises SETBP1's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 4.95× lower at baseline in the lines without FZD1 | 0.040 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[DPYSL3]] | B | FZD1 activity raises DPYSL3's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 6.36× lower at baseline in the lines without FZD1 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[TMEM45A]] | B | FZD1 activity raises TMEM45A's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 3.80× lower at baseline in the lines without FZD1 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[CHST14]] | B | FZD1 activity raises CHST14's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without FZD1 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[TRIM9]] | B | FZD1 activity raises TRIM9's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 4.66× lower at baseline in the lines without FZD1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[PTPN14]] | B | FZD1 activity raises PTPN14's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 1.75× lower at baseline in the lines without FZD1 | 0.082 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[KCTD12]] | B | FZD1 activity raises KCTD12's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 3.01× lower at baseline in the lines without FZD1 | 0.093 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[NLGN1]] | B | FZD1 activity raises NLGN1's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 4.28× lower at baseline in the lines without FZD1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.8, 27.4); signed map (28.3, 40.4). **Vector** length 52.0, 7.53% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +9.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.0 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +5.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.0 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +0.9 | +2.1 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +0.8 | +2.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.0 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -6.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -4.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | frizzled class receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.13 — chr7:91,264,433-91,271,326 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564G072, Hfz1 |
| Gene groups (HGNC) | G protein-coupled receptors, Class F frizzled |
| Hallmark sets | NOTCH_SIGNALING, WNT_BETA_CATENIN_SIGNALING |
| Reactome | 9 pathways, smallest: Disassembly of the destruction complex and recruitment of AXIN to the membrane; Class B/2 (Secretin family receptors); Asymmetric localization of PCP proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UP38](https://www.uniprot.org/uniprotkb/Q9UP38) (Frizzled-1):

> Receptor for Wnt proteins. Activated by WNT3A, WNT3, WNT1 and to a lesser extent WNT2, but apparently not by WNT4, WNT5A, WNT5B, WNT6, WNT7A or WNT7B. Contradictory results showing activation by WNT7B have been described for mouse (By similarity). Functions in the canonical Wnt/beta-catenin signaling pathway. The canonical Wnt/beta-catenin signaling pathway leads to the activation of disheveled proteins, inhibition of GSK-3 kinase, nuclear accumulation of beta-catenin and activation of Wnt …

**Summary**, from NCBI Gene [8321](https://www.ncbi.nlm.nih.gov/gene/8321):

> Members of the 'frizzled' gene family encode 7-transmembrane domain proteins that are receptors for Wnt signaling proteins. The FZD1 protein contains a signal peptide, a cysteine-rich domain in the N-terminal extracellular region, 7 transmembrane domains, and a C-terminal PDZ domain-binding motif. The FZD1 transcript is expressed in various tissues. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4038) · Entrez [8321](https://www.ncbi.nlm.nih.gov/gene/8321) · UniProt [Q9UP38](https://www.uniprot.org/uniprotkb/Q9UP38) · Ensembl [ENSG00000157240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157240)

## Data

Gene col 8056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8056); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8056]; `tensor/DDL_lfc|DDL_z.npy` [8056]; `embed/gene_vectors.npy` [8056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8056 or target_col == 8056). Every well: [[FZD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FZD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

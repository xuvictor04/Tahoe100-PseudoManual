---
symbol: "FAM83E"
type: "gene"
col: 2617
ensembl_id: "ENSG00000105523"
name: "scaffolding CK1 anchoring protein E"
location: "19q13.33"
module: 31
arm: "+"
pooled_cpm: 13.79
n_lines_expressing: 39
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 105
direction_downstream: 23
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# FAM83E

*scaffolding CK1 anchoring protein E* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +7.2, q 3e-10, up in 14 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.492× (z -6.3, q 2e-07, down in 22 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPRSS4]] (+0.76, fdr 7e-06), [[LSMEM2]] (+0.71, fdr 7e-06), [[ARHGAP30]] (+0.70, fdr 7e-06); moves opposite to [[ANTXR1]] (-0.52, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 105 arrows point to it, the strongest [[RAB25]] → it (grade B ⚠); 23 go from it, the strongest it → [[ARHGEF5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +7.2 | 3e-10 | 14/30 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +6.7 | 6e-09 | 5/18 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +5.2 | 4e-05 | 12/36 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.7 | 3e-04 | 5/13 (NCI-H2030, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.7 | 3e-04 | 11/35 (SW480, HEC-1-A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.34×** | +4.1 | 0.003 | 8/31 (HEC-1-A, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.003 | 8/34 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +3.9 | 0.008 | 7/31 (SW1417, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.012 | 9/35 (HEC-1-A, J82, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.7 | 0.013 | 7/26 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.014 | 9/33 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.025 | 8/36 (SW480, SW48, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.42×** | +3.2 | 0.054 | 3/26 (LOX-IMVI, AsPC-1, …) | all doses, flat | composition shift |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.054 | 6/34 (SW480, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.054 | 6/34 (Panc 03.27, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2617.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.492×** | -6.3 | 2e-07 | 22/31 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.617×** | -4.1 | 0.010 | 15/36 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.658×** | -4.0 | 0.011 | 14/36 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.740×** | -3.9 | 0.011 | 14/36 (NCI-H661, J82, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -3.6 | 0.035 | 17/35 (KATO III, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.765×** | -3.5 | 0.048 | 13/34 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -3.4 | 0.048 | 17/34 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.698×** | -3.3 | 0.061 | 11/36 (KATO III, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -3.3 | 0.061 | 17/32 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.704×** | -3.3 | 0.064 | 17/36 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.712×** | -3.1 | 0.086 | 5/36 (C-33 A, HEC-1-A, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.715×** | -3.1 | 0.089 | 13/34 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.721× | -3.0 | 0.11 | 10/35 (BT-474, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 69.9 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -20.1) |
| [[COLO 205 (line)]] | alt | 57.8 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0692× (z -22.2) |
| [[Panc 03.27 (line)]] | alt | 40.9 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -17.2) |
| [[KATO III (line)]] | alt | 59.7 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0822× (z -20.9) |
| [[LS 180 (line)]] | wt | 46.0 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 29.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -13.8) |
| [[BT-474 (line)]] | alt | 38.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 23.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -11.0) |
| [[SW1417 (line)]] | alt | 47.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -11.9) |
| [[LoVo (line)]] | wt | 21.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -9.2) |
| [[SW48 (line)]] | wt | 18.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0849× (z -8.9) |
| [[A-172 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS4]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[LSMEM2]] | +0.71 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP30]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[RDH13]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[MROH3P]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[C6orf132]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PTK6]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[AMN]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[CATSPERB]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TMEM45B]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[HSH2D]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTXR1]] | -0.52 | -0.55 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*105 arrows, 105 of them with an alert ⚠; grade A 0, B 104, C 1. Shown: the 12 strongest; 93 more arrows (93 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB25]] | B | RAB25 activity raises FAM83E's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 5.16× lower at baseline in the lines without RAB25 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises FAM83E's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.16× lower at baseline in the lines without TMPRSS4 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[CDH1]] | B | CDH1 activity raises FAM83E's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 4.77× lower at baseline in the lines without CDH1 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[FAM83B]] | B | FAM83B activity raises FAM83E's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 4.38× lower at baseline in the lines without FAM83B | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[TMEM125]] | B | TMEM125 activity raises FAM83E's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.18× lower at baseline in the lines without TMEM125 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[PRSS8]] | B | PRSS8 activity raises FAM83E's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 4.77× lower at baseline in the lines without PRSS8 | 2e-04 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[SLC44A4]] | B | SLC44A4 activity raises FAM83E's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 4.33× lower at baseline in the lines without SLC44A4 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[ST14]] | B | ST14 activity raises FAM83E's level | lines that do not express ST14 (32) vs lines expressing it (18) | 4.95× lower at baseline in the lines without ST14 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ADGRF1]] | B | ADGRF1 activity raises FAM83E's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 4.14× lower at baseline in the lines without ADGRF1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[ESRP1]] | B | ESRP1 activity raises FAM83E's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 4.61× lower at baseline in the lines without ESRP1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[SLC5A1]] | B | SLC5A1 activity raises FAM83E's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 5.06× lower at baseline in the lines without SLC5A1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[TNNT2]] | B | TNNT2 activity raises FAM83E's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 4.37× lower at baseline in the lines without TNNT2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF5]] | B | FAM83E activity raises ARHGEF5's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 2.34× lower at baseline in the lines without FAM83E | 0.020 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[SMIM41]] | B | FAM83E activity raises SMIM41's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 1.59× lower at baseline in the lines without FAM83E | 0.035 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[CLDN3]] | B | FAM83E activity raises CLDN3's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 2.94× lower at baseline in the lines without FAM83E | 0.039 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[TMC4]] | B | FAM83E activity raises TMC4's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 3.19× lower at baseline in the lines without FAM83E | 0.045 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[SULT2B1]] | B | FAM83E activity raises SULT2B1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 2.61× lower at baseline in the lines without FAM83E | 0.045 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[EPS8L1]] | B | FAM83E activity raises EPS8L1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 2.53× lower at baseline in the lines without FAM83E | 0.050 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[CDH1]] | B | FAM83E activity raises CDH1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 5.54× lower at baseline in the lines without FAM83E | 0.053 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[SPINT1]] | B | FAM83E activity raises SPINT1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 4.54× lower at baseline in the lines without FAM83E | 0.054 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[ESRP1]] | B | FAM83E activity raises ESRP1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 5.09× lower at baseline in the lines without FAM83E | 0.055 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[IQANK1]] | B | FAM83E activity raises IQANK1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 2.56× lower at baseline in the lines without FAM83E | 0.059 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[INAVA]] | B | FAM83E activity raises INAVA's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 3.61× lower at baseline in the lines without FAM83E | 0.062 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[ELMO3]] | B | FAM83E activity raises ELMO3's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without FAM83E | 0.069 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.7, 56.0); signed map (57.6, 6.6). **Vector** length 105, 29.3% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +3.8 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.2 | +2.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.4 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | scaffolding CK1 anchoring protein E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,599,961-48,615,076 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20200; previously FAM83E |
| Gene groups (HGNC) | Scaffolding anchor of CK1 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2M2I3](https://www.uniprot.org/uniprotkb/Q2M2I3) (Scaffolding CK1 anchoring protein E):

> May play a role in MAPK signaling.

**Summary**, from NCBI Gene [54854](https://www.ncbi.nlm.nih.gov/gene/54854):

> Enables protein kinase binding activity. Predicted to be involved in signal transduction. Predicted to be located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25972) · Entrez [54854](https://www.ncbi.nlm.nih.gov/gene/54854) · UniProt [Q2M2I3](https://www.uniprot.org/uniprotkb/Q2M2I3) · Ensembl [ENSG00000105523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105523)

## Data

Gene col 2617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2617); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2617]; `tensor/DDL_lfc|DDL_z.npy` [2617]; `embed/gene_vectors.npy` [2617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2617 or target_col == 2617). Every well: [[FAM83E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM83E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

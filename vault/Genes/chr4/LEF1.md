---
symbol: "LEF1"
type: "gene"
col: 6242
ensembl_id: "ENSG00000138795"
name: "lymphoid enhancer binding factor 1"
location: "4q25"
module: 87
arm: "+"
pooled_cpm: 28.42
n_lines_expressing: 21
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 28
direction_downstream: 19
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# LEF1

*lymphoid enhancer binding factor 1* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.73× (z +19.5, q 0e+00, up in 14 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.867× (z -6.9, q 2e-09, down in 5 of 20 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.608× (z -6.9, q 2e-09, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEF1-AS1]] (+0.80, fdr 7e-06, ⚠ same locus), [[C10orf90]] (+0.75, fdr 7e-06), [[SOX10]] (+0.68, fdr 7e-06), [[PTPRZ1]] (+0.67, fdr 1e-05); moves opposite to [[MKNK1]] (-0.45, fdr 9e-05), [[TP63]] (-0.43, fdr 4e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[STAG3]] → it (grade B ⚠); 19 go from it, the strongest it → [[DAAM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +19.5 | 0e+00 | 14/18 (LoVo, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +8.2 | 8e-14 | 5/19 (LoVo, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +6.0 | 5e-07 | 13/19 (A498, SHP-77, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.52×** | +5.5 | 4e-06 | 8/18 (RPMI-7951, H4, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.5 | 4e-06 | 7/20 (RPMI-7951, SW1417, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[venetoclax (drug)]] 5 µM |  | **2.06×** | +5.2 | 2e-05 | 7/17 (A-427, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.44×** | +5.0 | 5e-05 | 0/19 | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.45×** | +4.9 | 6e-05 | 0/15 | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 6e-05 | 6/19 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.87×** | +4.5 | 4e-04 | 6/19 (SHP-77, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.28×** | +3.4 | 0.030 | 7/18 (LoVo, A498, …) | two highest doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.031 | 9/18 (SHP-77, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.25× | +3.0 | 0.11 | 3/19 (LoVo, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6242.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.867× | -6.9 | 2e-09 | 5/20 (A-427, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.608×** | -6.9 | 2e-09 | 15/19 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.601×** | -6.7 | 2e-09 | 12/19 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.708×** | -6.7 | 2e-09 | 13/19 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -6.7 | 2e-09 | 9/19 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.634×** | -5.8 | 6e-07 | 3/19 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.663×** | -5.4 | 4e-06 | 8/18 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -4.9 | 5e-05 | 11/19 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.014 | 5/20 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.608×** | -3.6 | 0.019 | 3/18 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.836× | -3.4 | 0.030 | 4/19 (C32, J82, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.786×** | -3.3 | 0.041 | 4/20 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.827×** | -3.3 | 0.044 | 4/19 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.782×** | -3.1 | 0.073 | 3/20 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.1 | 0.073 | 6/19 (SW480, A-427, …) | rises with dose | low cells (technical?) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.795×** | -3.0 | 0.083 | 1/19 (SW 1088) | rises with dose | plate-row cell shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.658×** | -3.0 | 0.084 | 3/19 (C32, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 823 | 0 | 24 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0672× (z -30.5) |
| [[SK-MEL-2 (line)]] | alt | 210 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0590× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.137× (z -18.9) |
| [[SW480 (line)]] | alt | 39.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.8) |
| [[A-427 (line)]] | wt | 42.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -16.5) |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -15.8) |
| [[RKO (line)]] | wt | 64.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -14.8) |
| [[SHP-77 (line)]] | alt | 41.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.253× (z -8.5) |
| [[LoVo (line)]] | wt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 32.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +8.5) | — |
| [[A-172 (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.77 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEF1-AS1]] | +0.80 | +0.74 / +0.78 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[C10orf90]] | +0.75 | +0.70 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SOX10]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 | pathway: MITF-M-dependent gene expression; STRING 506 |
| [[PTPRZ1]] | +0.67 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[FKBP9P1-1]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[CTTNBP2]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[COL19A1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[OPRD1]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[FZD1]] | +0.64 | +0.60 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_WNT_BETA_CATENIN_SIGNALING; STRING 579 |
| [[SAMMSON]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[A2M]] | +0.64 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[RHOJ]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[MIR3681HG]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKNK1]] | -0.45 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[TP63]] | -0.43 | -0.49 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 3, C 25. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAG3]] | B | STAG3 activity raises LEF1's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without STAG3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |
| [[SOBP]] | B | SOBP activity raises LEF1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without SOBP | 0.063 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[TOP2A]] | B | TOP2A activity lowers LEF1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises LEF1's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 5.22× lower at baseline in the lines without LEF1-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[DCT]] | C | DCT activity raises LEF1's level | lines that do not express DCT (42) vs lines expressing it (8) | 6.16× lower at baseline in the lines without DCT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[ZNF521]] | C | ZNF521 activity raises LEF1's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 4.18× lower at baseline in the lines without ZNF521 | 0.004 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises LEF1's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 3.59× lower at baseline in the lines without LOXL3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises LEF1's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 8.82× lower at baseline in the lines without LHFPL3-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[LINC01812]] | C | LINC01812 activity raises LEF1's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 3.98× lower at baseline in the lines without LINC01812 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; co-absent with the target |
| [[TYR]] | C | TYR activity raises LEF1's level | lines that do not express TYR (43) vs lines expressing it (7) | 7.93× lower at baseline in the lines without TYR | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises LEF1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 4.57× lower at baseline in the lines without AEBP1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[PTPRZ1]] | C | PTPRZ1 activity raises LEF1's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 5.33× lower at baseline in the lines without PTPRZ1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 8, C 11. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAAM2]] | B | LEF1 activity raises DAAM2's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 2.14× lower at baseline in the lines without LEF1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[SOBP]] | B | LEF1 activity raises SOBP's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without LEF1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[PDE7A]] | B | LEF1 activity raises PDE7A's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.30× lower at baseline in the lines without LEF1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[MIR3681HG]] | B | LEF1 activity raises MIR3681HG's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without LEF1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[FZD1]] | B | LEF1 activity raises FZD1's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.51× lower at baseline in the lines without LEF1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[AADAT]] | B | LEF1 activity raises AADAT's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.67× lower at baseline in the lines without LEF1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| cells under [[Filgotinib (drug)]] 0.05 µM | B | LEF1 activity raises the cells' numbers under Filgotinib 0.05 µM (protects the cells) | lines that do not express LEF1 (29) vs lines expressing it (19) | the lines without LEF1: 0.92× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[NELL1]] | B | LEF1 activity raises NELL1's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without LEF1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[LOXL3]] | C | LEF1 activity raises LOXL3's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 2.77× lower at baseline in the lines without LEF1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1; co-absent with the target |
| [[AEBP1]] | C | LEF1 activity raises AEBP1's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 3.02× lower at baseline in the lines without LEF1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1 activity raises LEF1-AS1's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 2.15× lower at baseline in the lines without LEF1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1; co-absent with the target |
| [[NLGN1]] | C | LEF1 activity raises NLGN1's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 3.82× lower at baseline in the lines without LEF1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.1, 28.9); signed map (28.9, 38.7). **Vector** length 73.6, 24.6% of its response variance represented; |z| ≥ 3 in 443 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +19.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.0 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +8.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | lymphoid enhancer binding factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:108,047,545-108,168,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TCF1ALPHA, TCF10, TCF7L3 |
| Gene groups (HGNC) | TCF/LEF transcription factor family; Wnt enhanceosome complex |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, APOPTOSIS |
| Reactome | 29 pathways, smallest: RUNX3 regulates WNT signaling; Binding of TCF/LEF:CTNNB1 to target gene promoters; Germ layer formation at gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJU2](https://www.uniprot.org/uniprotkb/Q9UJU2) (Lymphoid enhancer-binding factor 1):

> Transcription factor that binds DNA in a sequence-specific manner. Participates in the Wnt signaling pathway (By similarity). Activates transcription of target genes in the presence of CTNNB1 and EP300 (By similarity). PIAG antagonizes both Wnt-dependent and Wnt-independent activation by LEF1 (By similarity). TLE1, TLE2, TLE3 and TLE4 repress transactivation mediated by LEF1 and CTNNB1. Regulates T-cell receptor alpha enhancer function. Required for IL17A expressing gamma-delta T-cell …

**Summary**, from NCBI Gene [51176](https://www.ncbi.nlm.nih.gov/gene/51176):

> This gene encodes a transcription factor belonging to a family of proteins that share homology with the high mobility group protein-1. The protein encoded by this gene can bind to a functionally important site in the T-cell receptor-alpha enhancer, thereby conferring maximal enhancer activity. This transcription factor is involved in the Wnt signaling pathway, and it may function in hair cell differentiation and follicle morphogenesis. Mutations in this gene have been found in somatic sebaceous …

**Accessions** — [HGNC:6551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6551) · Entrez [51176](https://www.ncbi.nlm.nih.gov/gene/51176) · UniProt [Q9UJU2](https://www.uniprot.org/uniprotkb/Q9UJU2) · Ensembl [ENSG00000138795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138795)

## Data

Gene col 6242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6242); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6242]; `tensor/DDL_lfc|DDL_z.npy` [6242]; `embed/gene_vectors.npy` [6242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6242 or target_col == 6242). Every well: [[LEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

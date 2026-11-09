---
symbol: "TYR"
type: "gene"
col: 1190
ensembl_id: "ENSG00000077498"
name: "tyrosinase"
location: "11q14.3"
module: 87
arm: "+"
pooled_cpm: 3.02
n_lines_expressing: 7
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 19
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# TYR

*tyrosinase* — 11q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.61× (z +8.9, q 3e-16, up in 0 of 2 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM: 0.458× (z -3.9, q 0.053, down in 0 of 3 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.175×, C32 0.156×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.123×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LHFPL3-AS1]] (+0.94, fdr 7e-06), [[A2M]] (+0.83, fdr 7e-06), [[SOX10]] (+0.81, fdr 7e-06); moves opposite to [[ELL2]] (-0.39, fdr 3e-04), [[KBTBD8]] (-0.36, fdr 4e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[RHOJ]] → it (grade C ⚠); 19 go from it, the strongest it → [[LINC02226]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.61×** | +8.9 | 3e-16 | 0/2 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.93×** | +8.5 | 8e-15 | 1/2 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.21×** | +8.2 | 7e-14 | 1/2 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.09×** | +7.4 | 2e-11 | 1/2 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.55×** | +4.4 | 0.001 | 2/2 (C32, SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.78×** | +3.6 | 0.029 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.029 | 2/3 (C32, SK-MEL-2) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +3.5 | 0.032 | 0/2 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.03×** | +3.5 | 0.032 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.4 | 0.041 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.3 | 0.047 | 2/2 (C32, SK-MEL-2) | top dose only | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.95×** | +3.3 | 0.049 | 2/2 (C32, SK-MEL-2) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.42×** | +3.1 | 0.081 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1190.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.175×, C32 0.156×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.123×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.458×** | -3.9 | 0.053 | 0/3 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -10.2) |
| [[C32 (line)]] | wt | 56.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -8.9) |
| [[A-172 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.466 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.420 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LHFPL3-AS1]] | +0.94 | +0.95 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[A2M]] | +0.83 | +0.85 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SOX10]] | +0.81 | +0.87 / +0.74 | both halves | 7e-06 | pathway: MITF-M-dependent gene expression; STRING 884 |
| [[TF]] | +0.80 | +0.84 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC02941]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[RMEL3]] | +0.73 | +0.77 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[PI15]] | +0.71 | +0.64 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[EDNRB]] | +0.69 | +0.60 / +0.59 | both halves | 7e-06 | pathway: MITF-M-regulated melanocyte development; STRING 691 |
| [[LINC02566]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TRPM8]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SAMMSON]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[C10orf90]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELL2]] | -0.39 | -0.27 / -0.42 | both halves | 3e-04 | pathway: HALLMARK_HEME_METABOLISM |
| [[KBTBD8]] | -0.36 | -0.25 / -0.35 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOJ]] | C | RHOJ activity raises TYR's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.07× lower at baseline in the lines without RHOJ | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises TYR's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 6.82× lower at baseline in the lines without LHFPL3-AS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises TYR's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 2.41× lower at baseline in the lines without COL19A1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises TYR's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 2.17× lower at baseline in the lines without EDNRB | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises TYR's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 3.62× lower at baseline in the lines without FCRLA | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[IHO1]] | C | IHO1 activity raises TYR's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 2.35× lower at baseline in the lines without IHO1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[A2M]] | C | A2M activity raises TYR's level | lines that do not express A2M (42) vs lines expressing it (8) | 4.36× lower at baseline in the lines without A2M | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[SOX10]] | C | SOX10 activity raises TYR's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 9.27× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[LINC00879]] | C | LINC00879 activity raises TYR's level | lines that do not express LINC00879 (46) vs lines expressing it (4) | 5.65× lower at baseline in the lines without LINC00879 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, ENSG00000234426, APOB; co-absent with the target; its own permutation p |
| [[LINC01242]] | C | LINC01242 activity raises TYR's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 2.40× lower at baseline in the lines without LINC01242 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises TYR's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.80× lower at baseline in the lines without FKBP9P1-1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[TF]] | C | TF activity raises TYR's level | lines that do not express TF (41) vs lines expressing it (9) | 3.72× lower at baseline in the lines without TF | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02226]] | B | TYR activity raises LINC02226's level | lines that do not express TYR (43) vs lines expressing it (7) | 3.43× lower at baseline in the lines without TYR | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10 |
| [[TF]] | C | TYR activity raises TF's level | lines that do not express TYR (43) vs lines expressing it (7) | 2.96× lower at baseline in the lines without TYR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[A2M]] | C | TYR activity raises A2M's level | lines that do not express TYR (43) vs lines expressing it (7) | 10.24× lower at baseline in the lines without TYR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[AEBP1]] | C | TYR activity raises AEBP1's level | lines that do not express TYR (43) vs lines expressing it (7) | 8.62× lower at baseline in the lines without TYR | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[MIR3681HG]] | C | TYR activity raises MIR3681HG's level | lines that do not express TYR (43) vs lines expressing it (7) | 15.32× lower at baseline in the lines without TYR | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[C10orf90]] | C | TYR activity raises C10orf90's level | lines that do not express TYR (43) vs lines expressing it (7) | 7.48× lower at baseline in the lines without TYR | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[LHFPL3-AS1]] | C | TYR activity raises LHFPL3-AS1's level | lines that do not express TYR (43) vs lines expressing it (7) | 11.78× lower at baseline in the lines without TYR | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[FCRLA]] | C | TYR activity raises FCRLA's level | lines that do not express TYR (43) vs lines expressing it (7) | 6.53× lower at baseline in the lines without TYR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[SOX10]] | C | TYR activity raises SOX10's level | lines that do not express TYR (43) vs lines expressing it (7) | 8.69× lower at baseline in the lines without TYR | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[DAAM2]] | C | TYR activity raises DAAM2's level | lines that do not express TYR (43) vs lines expressing it (7) | 5.22× lower at baseline in the lines without TYR | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[LOXL3]] | C | TYR activity raises LOXL3's level | lines that do not express TYR (43) vs lines expressing it (7) | 5.42× lower at baseline in the lines without TYR | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[LEF1]] | C | TYR activity raises LEF1's level | lines that do not express TYR (43) vs lines expressing it (7) | 7.93× lower at baseline in the lines without TYR | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.9, 28.9); signed map (29.9, 39.5). **Vector** length 19.8, 14.8% of its response variance represented; |z| ≥ 3 in 59 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +0.8 | +4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.6 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.5 | -0.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.4 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.4 | +0.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.4 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.4 | +1.1 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.6 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.5 | +0.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -0.5 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.5 | +0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.4 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | tyrosinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.3 — chr11:89,177,875-89,295,759 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OCAIA, OCA1A, OCA1 |
| Gene groups (HGNC) | Tyrosinase family; Oxygenases |
| Hallmark sets | XENOBIOTIC_METABOLISM, HEME_METABOLISM |
| Reactome | 5 pathways, smallest: Melanin biosynthesis; Regulation of MITF-M-dependent genes involved in pigmentation; MITF-M-dependent gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P14679](https://www.uniprot.org/uniprotkb/P14679) (Tyrosinase):

> This is a copper-containing oxidase that functions in the formation of pigments such as melanins and other polyphenolic compounds. Catalyzes the initial and rate limiting step in the cascade of reactions leading to melanin production from tyrosine (By similarity). In addition to hydroxylating tyrosine to DOPA (3,4-dihydroxyphenylalanine), also catalyzes the oxidation of DOPA to DOPA-quinone, and possibly the oxidation of DHI (5,6-dihydroxyindole) to indole-5,6 quinone.

**Summary**, from NCBI Gene [7299](https://www.ncbi.nlm.nih.gov/gene/7299):

> The enzyme encoded by this gene catalyzes the first 2 steps, and at least 1 subsequent step, in the conversion of tyrosine to melanin. The enzyme has both tyrosine hydroxylase and dopa oxidase catalytic activities, and requires copper for function. Mutations in this gene result in oculocutaneous albinism, and nonpathologic polymorphisms result in skin pigmentation variation. The human genome contains a pseudogene similar to the 3' half of this gene. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:12442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12442) · Entrez [7299](https://www.ncbi.nlm.nih.gov/gene/7299) · UniProt [P14679](https://www.uniprot.org/uniprotkb/P14679) · Ensembl [ENSG00000077498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077498)

## Data

Gene col 1190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1190); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1190]; `tensor/DDL_lfc|DDL_z.npy` [1190]; `embed/gene_vectors.npy` [1190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1190 or target_col == 1190). Every well: [[TYR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

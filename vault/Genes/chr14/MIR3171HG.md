---
symbol: "MIR3171HG"
type: "gene"
col: 15153
ensembl_id: "ENSG00000258932"
name: "MIR3171 host gene"
location: "14q12"
module: 108
arm: "+"
pooled_cpm: 57.23
n_lines_expressing: 17
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 11
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# MIR3171HG

*MIR3171 host gene* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.95× (z +13.5, q 2e-38, up in 1 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +10.6, q 6e-24, up in 0 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.633× (z -5.6, q 9e-06, down in 11 of 15 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRD]] (+0.71, fdr 7e-06), [[ZFHX4]] (+0.70, fdr 7e-06), [[MSC-AS1]] (+0.70, fdr 7e-06); moves opposite to [[BDH1]] (-0.50, fdr 4e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MIR4307HG]] → it (grade C ⚠); 11 go from it, the strongest it → [[LINC02328]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +13.5 | 2e-38 | 1/15 (H4) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +10.6 | 6e-24 | 0/15 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +7.4 | 2e-11 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +5.7 | 1e-06 | 1/15 (H4) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.8 | 2e-04 | 9/15 (KATO III, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 0.002 | 10/15 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.007 | 0/15 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.012 | 11/15 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.021 | 0/15 | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.050 | 8/15 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.079 | 9/15 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 0.05 µM |  | 1.30× | +3.0 | 0.11 | 0/15 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15153.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -5.6 | 9e-06 | 11/15 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.694×** | -4.3 | 0.005 | 9/15 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.722×** | -4.0 | 0.011 | 10/15 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.756×** | -3.4 | 0.085 | 0/15 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.3 | 0.087 | 0/15 | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.767×** | -3.3 | 0.087 | 7/15 (AN3 CA, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.605×** | -3.2 | 0.087 | 7/15 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.606×** | -3.2 | 0.087 | 6/15 (CFPAC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.781× | -3.0 | 0.14 | 6/15 (LOX-IMVI, SNU-423, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.770× | -3.0 | 0.14 | 0/15 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 252 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 87.5 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 442 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -17.2) |
| [[SK-MEL-2 (line)]] | alt | 401 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 273 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -15.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 162 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -14.4) |
| [[A-172 (line)]] | wt | 77.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -10.4) |
| [[A498 (line)]] | wt | 201 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.3) |
| [[H4 (line)]] | wt | 28.6 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0736× (z -11.0) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0668× (z -10.6) |
| [[KATO III (line)]] | alt | 31.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.211× (z -10.0) |
| [[SNU-423 (line)]] | alt | 97.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 67.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -9.4) |
| [[A-427 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.45 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRD]] | +0.71 | +0.62 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ZFHX4]] | +0.70 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MSC-AS1]] | +0.70 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MIR548XHG]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 | same gene group |
| [[KCNH5]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LINC02377]] | +0.67 | +0.57 / +0.67 | both halves | 9e-06 | **novel candidate** |
| [[CDH8]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ADGRB3]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[LINC01687]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[IGSF1]] | +0.63 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[LINC00648]] | +0.63 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[ARHGAP28]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDH1]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR4307HG]] | C | MIR4307HG activity raises MIR3171HG's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 4.71× lower at baseline in the lines without MIR4307HG | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438; co-absent with the target |
| [[SLC8A1]] | C | SLC8A1 activity raises MIR3171HG's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 4.92× lower at baseline in the lines without SLC8A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[PEX5L]] | C | PEX5L activity raises MIR3171HG's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 4.63× lower at baseline in the lines without PEX5L | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[TENM1]] | C | TENM1 activity raises MIR3171HG's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 4.37× lower at baseline in the lines without TENM1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises MIR3171HG's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 5.27× lower at baseline in the lines without LINC02616 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[MAGI2]] | C | MAGI2 activity raises MIR3171HG's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 4.57× lower at baseline in the lines without MAGI2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[MSC]] | C | MSC activity raises MIR3171HG's level | lines that do not express MSC (34) vs lines expressing it (16) | 6.54× lower at baseline in the lines without MSC | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[OR9Q1]] | C | OR9Q1 activity raises MIR3171HG's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 3.47× lower at baseline in the lines without OR9Q1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L; co-absent with the target |
| [[ST8SIA6-AS1]] | C | ST8SIA6-AS1 activity raises MIR3171HG's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 5.24× lower at baseline in the lines without ST8SIA6-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[KCNT2]] | C | KCNT2 activity raises MIR3171HG's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 4.05× lower at baseline in the lines without KCNT2 | 0.069 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises MIR3171HG's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.59× lower at baseline in the lines without TCF4 | 0.071 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[CHMP1B2P]] | C | CHMP1B2P activity raises MIR3171HG's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 3.36× lower at baseline in the lines without CHMP1B2P | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02328]] | B | MIR3171HG activity raises LINC02328's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 2.76× lower at baseline in the lines without MIR3171HG | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC |
| [[FLRT2]] | C | MIR3171HG activity raises FLRT2's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 4.40× lower at baseline in the lines without MIR3171HG | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[TDO2]] | C | MIR3171HG activity raises TDO2's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 2.53× lower at baseline in the lines without MIR3171HG | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[MIR548XHG]] | C | MIR3171HG activity raises MIR548XHG's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 4.10× lower at baseline in the lines without MIR3171HG | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[SLC8A1]] | C | MIR3171HG activity raises SLC8A1's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 4.23× lower at baseline in the lines without MIR3171HG | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[CHMP1B2P]] | C | MIR3171HG activity raises CHMP1B2P's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 4.25× lower at baseline in the lines without MIR3171HG | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[LINC02616]] | C | MIR3171HG activity raises LINC02616's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 3.21× lower at baseline in the lines without MIR3171HG | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[MSC]] | C | MIR3171HG activity raises MSC's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 2.98× lower at baseline in the lines without MIR3171HG | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[LINC00648]] | C | MIR3171HG activity raises LINC00648's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 3.21× lower at baseline in the lines without MIR3171HG | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[LINC02476]] | C | MIR3171HG activity raises LINC02476's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 5.41× lower at baseline in the lines without MIR3171HG | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[TENM1]] | C | MIR3171HG activity raises TENM1's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 3.32× lower at baseline in the lines without MIR3171HG | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.818). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 25.6); signed map (33.5, 42.3). **Vector** length 63.3, 23.3% of its response variance represented; |z| ≥ 3 in 447 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +13.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | +0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | MIR3171 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q12 — chr14:27,258,717-27,259,166 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56193) · Entrez [728755](https://www.ncbi.nlm.nih.gov/gene/728755) · Ensembl [ENSG00000258932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258932)

## Data

Gene col 15153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15153); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15153]; `tensor/DDL_lfc|DDL_z.npy` [15153]; `embed/gene_vectors.npy` [15153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15153 or target_col == 15153). Every well: [[MIR3171HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR3171HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

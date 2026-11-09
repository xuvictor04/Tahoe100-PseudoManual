---
symbol: "COL19A1"
type: "gene"
col: 1344
ensembl_id: "ENSG00000082293"
name: "collagen type XIX alpha 1 chain"
location: "6q13"
module: 87
arm: "+"
pooled_cpm: 15.56
n_lines_expressing: 14
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 32
direction_downstream: 34
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# COL19A1

*collagen type XIX alpha 1 chain* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.15× (z +9.3, q 5e-18, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +9.2, q 7e-18, up in 1 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.632× (z -3.9, q 0.049, down in 3 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (C32 0.0632×, SK-MEL-2 0.131×); [[Panobinostat (drug)]] 5 µM in 1 line (C32 0.0369×); [[Panobinostat (drug)]] 0.5 µM in 1 line (C32 0.0567×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C10orf90]] (+0.83, fdr 7e-06), [[LEF1-AS1]] (+0.79, fdr 7e-06), [[MIR3681HG]] (+0.76, fdr 7e-06); moves opposite to [[DCT]] (-0.46, fdr 5e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[EDNRB]] → it (grade C ⚠); 34 go from it, the strongest it → [[PLEKHS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +9.3 | 5e-18 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +9.2 | 7e-18 | 1/10 (LOX-IMVI) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.86×** | +8.9 | 1e-16 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +7.5 | 1e-11 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.2 | 0.002 | 2/9 (LOX-IMVI, RPMI-7951) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.38×** | +3.8 | 0.012 | 3/9 (hTERT-HPNE, CHP-212, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.048 | 1/12 (LOX-IMVI) | rises with dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.062 | 0/9 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.073 | 0/9 | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.50×** | +3.2 | 0.077 | 1/9 (SK-MEL-2) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.77× | +3.0 | 0.12 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1344.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (C32 0.0632×, SK-MEL-2 0.131×); [[Panobinostat (drug)]] 5 µM in 1 line (C32 0.0369×); [[Panobinostat (drug)]] 0.5 µM in 1 line (C32 0.0567×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.632×** | -3.9 | 0.049 | 3/12 (SW 1271, SW 1088, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.668× | -3.5 | 0.11 | 4/12 (C32, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | 0.469× | -3.4 | 0.13 | 1/12 (C32) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.707× | -3.3 | 0.13 | 3/11 (C32, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.672× | -3.1 | 0.19 | 1/10 (LOX-IMVI) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 688 | 0 | 19 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0369× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.178× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.131× (z -9.4) |
| [[A-172 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C10orf90]] | +0.83 | +0.84 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[LEF1-AS1]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[MIR3681HG]] | +0.76 | +0.70 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SOX10]] | +0.75 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SAMMSON]] | +0.72 | +0.59 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LOXL3]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 | pathway: Collagen formation |
| [[LINC01812]] | +0.70 | +0.62 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CDH19]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[RHOJ]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[AEBP1]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[A2M]] | +0.67 | +0.51 / +0.73 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix |
| [[SETBP1]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCT]] | -0.46 | -0.40 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 0, C 32. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDNRB]] | C | EDNRB activity raises COL19A1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 4.15× lower at baseline in the lines without EDNRB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[DCT]] | C | DCT activity raises COL19A1's level | lines that do not express DCT (42) vs lines expressing it (8) | 5.37× lower at baseline in the lines without DCT | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises COL19A1's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 3.38× lower at baseline in the lines without LEF1-AS1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises COL19A1's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 3.71× lower at baseline in the lines without C10orf90 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises COL19A1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.98× lower at baseline in the lines without AEBP1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises COL19A1's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.47× lower at baseline in the lines without FCRLA | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[RHOJ]] | C | RHOJ activity raises COL19A1's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.68× lower at baseline in the lines without RHOJ | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises COL19A1's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 7.77× lower at baseline in the lines without LHFPL3-AS1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises COL19A1's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 3.10× lower at baseline in the lines without LINC01583 | 0.027 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |
| [[TYR]] | C | TYR activity raises COL19A1's level | lines that do not express TYR (43) vs lines expressing it (7) | 6.19× lower at baseline in the lines without TYR | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[ARHGAP6]] | C | ARHGAP6 activity raises COL19A1's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 2.27× lower at baseline in the lines without ARHGAP6 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[LINC01242]] | C | LINC01242 activity raises COL19A1's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 3.52× lower at baseline in the lines without LINC01242 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 3, C 31. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHS1]] | B | COL19A1 activity raises PLEKHS1's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 1.73× lower at baseline in the lines without COL19A1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7 |
| [[OBI1-AS1]] | B | COL19A1 activity raises OBI1-AS1's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 1.75× lower at baseline in the lines without COL19A1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7 |
| cells under [[vincristine (drug)]] 5 µM | B | COL19A1 activity lowers the cells' numbers under vincristine 5 µM (makes them more sensitive) | lines that do not express COL19A1 (36) vs lines expressing it (12) | the lines without COL19A1: 1.48× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7 |
| [[C10orf90]] | C | COL19A1 activity raises C10orf90's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 3.43× lower at baseline in the lines without COL19A1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[AEBP1]] | C | COL19A1 activity raises AEBP1's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 5.74× lower at baseline in the lines without COL19A1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[DCT]] | C | COL19A1 activity raises DCT's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 3.19× lower at baseline in the lines without COL19A1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[LHFPL3-AS1]] | C | COL19A1 activity raises LHFPL3-AS1's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 3.99× lower at baseline in the lines without COL19A1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[LINC02941]] | C | COL19A1 activity raises LINC02941's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 2.63× lower at baseline in the lines without COL19A1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[FCRLA]] | C | COL19A1 activity raises FCRLA's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without COL19A1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[SDC2]] | C | COL19A1 activity raises SDC2's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 6.57× lower at baseline in the lines without COL19A1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[LOXL3]] | C | COL19A1 activity raises LOXL3's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 4.43× lower at baseline in the lines without COL19A1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[SOX10]] | C | COL19A1 activity raises SOX10's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 3.13× lower at baseline in the lines without COL19A1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.838). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.9, 28.2); signed map (28.7, 39.4). **Vector** length 49.0, 21.1% of its response variance represented; |z| ≥ 3 in 237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.9 | +1.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +2.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | +0.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.2 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -3.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XIX alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:69,866,556-70,212,468 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibril associated collagens with interrupted triple helices |
| Reactome | 6 pathways, smallest: Collagen chain trimerization; Collagen degradation; Collagen biosynthesis and modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14993](https://www.uniprot.org/uniprotkb/Q14993) (Collagen alpha-1(XIX) chain):

> May act as a cross-bridge between fibrils and other extracellular matrix molecules. Involved in skeletal myogenesis in the developing esophagus. May play a role in organization of the pericellular matrix or the sphinteric smooth muscle.

**Summary**, from NCBI Gene [1310](https://www.ncbi.nlm.nih.gov/gene/1310):

> This gene encodes the alpha chain of type XIX collagen, a member of the FACIT collagen family (fibril-associated collagens with interrupted helices). Although the function of this collagen is not known, other members of this collagen family are found in association with fibril-forming collagens such as type I and II, and serve to maintain the integrity of the extracellular matrix. The transcript produced from this gene has an unusually large 3' UTR which has not been completely sequenced. …

**Accessions** — [HGNC:2196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2196) · Entrez [1310](https://www.ncbi.nlm.nih.gov/gene/1310) · UniProt [Q14993](https://www.uniprot.org/uniprotkb/Q14993) · Ensembl [ENSG00000082293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082293)

## Data

Gene col 1344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1344); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1344]; `tensor/DDL_lfc|DDL_z.npy` [1344]; `embed/gene_vectors.npy` [1344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1344 or target_col == 1344). Every well: [[COL19A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL19A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

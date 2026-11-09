---
symbol: "APOD"
type: "gene"
col: 12084
ensembl_id: "ENSG00000189058"
name: "apolipoprotein D"
location: "3q29"
module: 87
arm: "+"
pooled_cpm: 4.7
n_lines_expressing: 7
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 17
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# APOD

*apolipoprotein D* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.82× (z +8.8, q 7e-16, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +4.8, q 3e-04, up in 1 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (56 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 44 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TF]] (+0.73, fdr 1e-05), [[A2M]] (+0.70, fdr 6e-04), [[AEBP1]] (+0.58, fdr 6e-04); moves opposite to [[AKT3]] (-0.33, fdr 3e-04), [[NSMCE4A]] (-0.32, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[AFP]], [[ALB]] → it (grade C ⚠); 17 go from it, the strongest it → [[SAMMSON]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.82×** | +8.8 | 7e-16 | 1/2 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.99×** | +8.6 | 2e-15 | 2/2 (SK-MEL-2, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.61×** | +7.2 | 8e-11 | 1/2 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +4.8 | 3e-04 | 1/2 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +3.6 | 0.027 | 1/2 (SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.6 | 0.027 | 1/2 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~13% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.74×** | +3.6 | 0.027 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.4 | 0.053 | 0/3 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.54×** | +3.3 | 0.053 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.3 | 0.053 | 1/2 (SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.49×** | +3.2 | 0.061 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.90×** | +3.2 | 0.068 | 1/2 (SK-MEL-2) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.43×** | +3.2 | 0.069 | 2/2 (SK-MEL-2, C32) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +3.1 | 0.079 | 1/2 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +3.0 | 0.096 | 0/4 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.470 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 43 of them with an alert (⚠; 43 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TF]] | +0.73 | +0.73 / +0.49 | both halves | 1e-05 | STRING 428 |
| [[A2M]] | +0.70 | +0.89 / +0.22 | both halves | 6e-04 | STRING 574 |
| [[AEBP1]] | +0.58 | +0.68 / +0.21 | both halves | 6e-04 | pathway: HALLMARK_MYOGENESIS |
| [[LHFPL3-AS1]] | +0.57 | +0.79 / +0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[SPARC]] | +0.57 | +0.49 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_MYOGENESIS |
| [[CFI]] | +0.57 | +0.50 / +0.30 | both halves | 2e-04 | **novel candidate** |
| [[COL1A2]] | +0.53 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[TYR]] | +0.52 | +0.74 / +0.06 | ⚠ one half (not replicated) | 0.004 |  |
| [[FCRLA]] | +0.51 | +0.70 / +0.24 | both halves | 4e-04 |  |
| [[CTTNBP2]] | +0.50 | +0.52 / +0.21 | both halves | 7e-04 |  |
| [[PI15]] | +0.50 | +0.63 / +0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[THY1]] | +0.50 | +0.32 / +0.41 | both halves | 1e-04 |  |
| [[EDNRB]] | +0.50 | +0.55 / +0.27 | both halves | 3e-04 |  |
| [[RNF175]] | +0.48 | +0.58 / +0.26 | both halves | 4e-04 |  |
| [[PANTR1]] | +0.47 | +0.43 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT3]] | -0.33 | -0.27 / -0.33 | both halves | 3e-04 | pathway: Signaling by Nuclear Receptors |
| [[NSMCE4A]] | -0.32 | -0.15 / -0.32 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFP]], [[ALB]] | C | AFP, ALB activity raises APOD's level | lines that do not express AFP, ALB (45) vs lines expressing them (5) | 1.72× lower at baseline in the lines without AFP, ALB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises APOD's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 6.84× lower at baseline in the lines without LHFPL3-AS1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[CTTNBP2]] | C | CTTNBP2 activity raises APOD's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without CTTNBP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises APOD's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without EDNRB | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises APOD's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 2.30× lower at baseline in the lines without COL19A1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[SOX10]] | C | SOX10 activity raises APOD's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 8.91× lower at baseline in the lines without SOX10 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target |
| [[A2M]] | C | A2M activity raises APOD's level | lines that do not express A2M (42) vs lines expressing it (8) | 4.30× lower at baseline in the lines without A2M | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[TYR]] | C | TYR activity raises APOD's level | lines that do not express TYR (43) vs lines expressing it (7) | 5.30× lower at baseline in the lines without TYR | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises APOD's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 3.53× lower at baseline in the lines without FCRLA | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMMSON]] | C | APOD activity raises SAMMSON's level | lines that do not express APOD (43) vs lines expressing it (7) | 10.00× lower at baseline in the lines without APOD | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[CTTNBP2]] | C | APOD activity raises CTTNBP2's level | lines that do not express APOD (43) vs lines expressing it (7) | 6.19× lower at baseline in the lines without APOD | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[MIR3681HG]] | C | APOD activity raises MIR3681HG's level | lines that do not express APOD (43) vs lines expressing it (7) | 7.33× lower at baseline in the lines without APOD | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[AGMO]] | C | APOD activity raises AGMO's level | lines that do not express APOD (43) vs lines expressing it (7) | 3.48× lower at baseline in the lines without APOD | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[LHFPL3-AS1]] | C | APOD activity raises LHFPL3-AS1's level | lines that do not express APOD (43) vs lines expressing it (7) | 10.45× lower at baseline in the lines without APOD | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[A2M]] | C | APOD activity raises A2M's level | lines that do not express APOD (43) vs lines expressing it (7) | 6.84× lower at baseline in the lines without APOD | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[DGKB]] | C | APOD activity raises DGKB's level | lines that do not express APOD (43) vs lines expressing it (7) | 3.68× lower at baseline in the lines without APOD | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[CFI]] | C | APOD activity raises CFI's level | lines that do not express APOD (43) vs lines expressing it (7) | 4.47× lower at baseline in the lines without APOD | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[PPP2R2B]] | C | APOD activity raises PPP2R2B's level | lines that do not express APOD (43) vs lines expressing it (7) | 5.27× lower at baseline in the lines without APOD | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[TF]] | C | APOD activity raises TF's level | lines that do not express APOD (43) vs lines expressing it (7) | 2.36× lower at baseline in the lines without APOD | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[SOX10]] | C | APOD activity raises SOX10's level | lines that do not express APOD (43) vs lines expressing it (7) | 6.98× lower at baseline in the lines without APOD | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[C10orf90]] | C | APOD activity raises C10orf90's level | lines that do not express APOD (43) vs lines expressing it (7) | 5.40× lower at baseline in the lines without APOD | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.6, 29.4); signed map (29.5, 40.3). **Vector** length 9.16, 2.89% of its response variance represented; |z| ≥ 3 in 47 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.4 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.3 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.3 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +0.3 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.2 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.2 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.2 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.2 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.2 | +0.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -0.3 | -0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.2 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -0.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -0.2 | +8.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.2 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.2 | +0.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:195,568,705-195,584,033 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Apo-D |
| Gene groups (HGNC) | Apolipoproteins; Lipocalins |
| Hallmark sets | MYOGENESIS, KRAS_SIGNALING_UP |
| Reactome | 7 pathways, smallest: Transport of fatty acids; Transport of vitamins, nucleosides, and related molecules; NR1H3 & NR1H2 regulate gene expression linked to cholesterol transport and efflux |
| Matched by | ensembl_id |

**Function**, from UniProt [P05090](https://www.uniprot.org/uniprotkb/P05090) (Apolipoprotein D):

> APOD occurs in the macromolecular complex with lecithin-cholesterol acyltransferase. It is probably involved in the transport and binding of bilin. Appears to be able to transport a variety of ligands in a number of different contexts.

**Summary**, from NCBI Gene [347](https://www.ncbi.nlm.nih.gov/gene/347):

> This gene encodes a component of high density lipoprotein that has no marked similarity to other apolipoprotein sequences. It has a high degree of homology to plasma retinol-binding protein and other members of the alpha 2 microglobulin protein superfamily of carrier proteins, also known as lipocalins. This glycoprotein is closely associated with the enzyme lecithin:cholesterol acyltransferase - an enzyme involved in lipoprotein metabolism. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:612) · Entrez [347](https://www.ncbi.nlm.nih.gov/gene/347) · UniProt [P05090](https://www.uniprot.org/uniprotkb/P05090) · Ensembl [ENSG00000189058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189058)

## Data

Gene col 12084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12084); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12084]; `tensor/DDL_lfc|DDL_z.npy` [12084]; `embed/gene_vectors.npy` [12084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12084 or target_col == 12084). Every well: [[APOD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SOX10"
type: "gene"
col: 1878
ensembl_id: "ENSG00000100146"
name: "SRY-box transcription factor 10"
location: "22q13.1"
module: 87
arm: "+"
pooled_cpm: 7.19
n_lines_expressing: 5
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 20
direction_downstream: 20
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# SOX10

*SRY-box transcription factor 10* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.71× (z +7.3, q 2e-10, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +4.2, q 0.002, up in 0 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (C32 0.0903×, SK-MEL-2 0.151×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.101×, C32 0.0959×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.177×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LHFPL3-AS1]] (+0.89, fdr 7e-06), [[A2M]] (+0.87, fdr 7e-06), [[TYR]] (+0.81, fdr 7e-06); moves opposite to [[PYDC2-AS1]] (-0.41, fdr 3e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[RHOJ]] → it (grade C ⚠); 20 go from it, the strongest it → [[PLEKHS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.71×** | +7.3 | 2e-10 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.37×** | +7.0 | 6e-10 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +5.1 | 5e-05 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.21×** | +4.6 | 6e-04 | 0/3 | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.5 | 9e-04 | 0/3 | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.2 | 0.002 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.9 | 0.007 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.72× | +3.2 | 0.11 | 3/3 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1878.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (C32 0.0903×, SK-MEL-2 0.151×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.101×, C32 0.0959×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.177×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.549× | -3.2 | 0.67 | 0/3 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 244 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -12.1) |
| [[C32 (line)]] | wt | 150 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0903× (z -11.5) |
| [[A-172 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.980 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.940 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.835 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.759 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LHFPL3-AS1]] | +0.89 | +0.84 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[A2M]] | +0.87 | +0.79 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[TYR]] | +0.81 | +0.87 / +0.74 | both halves | 7e-06 | pathway: MITF-M-dependent gene expression; STRING 884 |
| [[LINC02941]] | +0.81 | +0.76 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[LINC02566]] | +0.79 | +0.77 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SAMMSON]] | +0.78 | +0.68 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[C10orf90]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[LEF1-AS1]] | +0.76 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[COL19A1]] | +0.75 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PI15]] | +0.73 | +0.57 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[CTTNBP2]] | +0.72 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[LINC02226]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYDC2-AS1]] | -0.41 | -0.50 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 0, C 20. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOJ]] | C | RHOJ activity raises SOX10's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.55× lower at baseline in the lines without RHOJ | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises SOX10's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 10.42× lower at baseline in the lines without LHFPL3-AS1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[TYR]] | C | TYR activity raises SOX10's level | lines that do not express TYR (43) vs lines expressing it (7) | 8.69× lower at baseline in the lines without TYR | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises SOX10's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 3.13× lower at baseline in the lines without COL19A1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises SOX10's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without EDNRB | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises SOX10's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.18× lower at baseline in the lines without FCRLA | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[A2M]] | C | A2M activity raises SOX10's level | lines that do not express A2M (42) vs lines expressing it (8) | 6.59× lower at baseline in the lines without A2M | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[TF]] | C | TF activity raises SOX10's level | lines that do not express TF (41) vs lines expressing it (9) | 5.41× lower at baseline in the lines without TF | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[LINC01242]] | C | LINC01242 activity raises SOX10's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 2.94× lower at baseline in the lines without LINC01242 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |
| [[IHO1]] | C | IHO1 activity raises SOX10's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 3.04× lower at baseline in the lines without IHO1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises SOX10's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 4.04× lower at baseline in the lines without AEBP1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises SOX10's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.16× lower at baseline in the lines without FKBP9P1-1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 1, C 19. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHS1]] | B | SOX10 activity raises PLEKHS1's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 3.60× lower at baseline in the lines without SOX10 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR |
| [[LHFPL3-AS1]] | C | SOX10 activity raises LHFPL3-AS1's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 20.60× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[A2M]] | C | SOX10 activity raises A2M's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 19.47× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[SAMMSON]] | C | SOX10 activity raises SAMMSON's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 16.32× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[AEBP1]] | C | SOX10 activity raises AEBP1's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 16.13× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[C10orf90]] | C | SOX10 activity raises C10orf90's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 14.19× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[LEF1]] | C | SOX10 activity raises LEF1's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 13.23× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[FCRLA]] | C | SOX10 activity raises FCRLA's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 12.02× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[TIMP3]] | C | SOX10 activity raises TIMP3's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 11.97× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[MIR3681HG]] | C | SOX10 activity raises MIR3681HG's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 10.97× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[COL19A1]] | C | SOX10 activity raises COL19A1's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 10.19× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |
| [[TYR]] | C | SOX10 activity raises TYR's level | lines that do not express SOX10 (45) vs lines expressing it (5) | 9.27× lower at baseline in the lines without SOX10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01425, ENSG00000241168, TYR; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.885). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.0, 28.7); signed map (29.7, 39.5). **Vector** length 26.6, 20.0% of its response variance represented; |z| ≥ 3 in 82 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.0 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.8 | +5.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +0.7 | +2.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +0.6 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.5 | +0.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.5 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.4 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.4 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.4 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.4 | -2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.4 | -1.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.3 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.3 | -2.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | SRY-box transcription factor 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,970,686-37,987,422 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DOM, WS4, WS2E, SOX-10 |
| Gene groups (HGNC) | SRY-box transcription factors |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 13 pathways, smallest: Regulation of CDH19 Expression and Function; EGR2 and SOX10-mediated initiation of Schwann cell myelination; Regulation of Expression and Function of Type II Classical Cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [P56693](https://www.uniprot.org/uniprotkb/P56693) (Transcription factor SOX-10):

> Transcription factor that plays a central role in developing and mature glia (By similarity). Specifically activates expression of myelin genes, during oligodendrocyte (OL) maturation, such as DUSP15 and MYRF, thereby playing a central role in oligodendrocyte maturation and CNS myelination (By similarity). Once induced, MYRF cooperates with SOX10 to implement the myelination program (By similarity). Transcriptional activator of MITF, acting synergistically with PAX3. Transcriptional activator …

**Summary**, from NCBI Gene [6663](https://www.ncbi.nlm.nih.gov/gene/6663):

> This gene encodes a member of the SOX (SRY-related HMG-box) family of transcription factors involved in the regulation of embryonic development and in the determination of the cell fate. The encoded protein may act as a transcriptional activator after forming a protein complex with other proteins. This protein acts as a nucleocytoplasmic shuttle protein and is important for neural crest and peripheral nervous system development. Mutations in this gene are associated with Waardenburg-Shah and …

**Accessions** — [HGNC:11190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11190) · Entrez [6663](https://www.ncbi.nlm.nih.gov/gene/6663) · UniProt [P56693](https://www.uniprot.org/uniprotkb/P56693) · Ensembl [ENSG00000100146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100146)

## Data

Gene col 1878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1878); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1878]; `tensor/DDL_lfc|DDL_z.npy` [1878]; `embed/gene_vectors.npy` [1878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1878 or target_col == 1878). Every well: [[SOX10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

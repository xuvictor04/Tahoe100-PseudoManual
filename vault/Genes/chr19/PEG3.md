---
symbol: "PEG3"
type: "gene"
col: 12568
ensembl_id: "ENSG00000198300"
name: "paternally expressed 3"
location: "19q13.43"
module: 27
arm: "+"
pooled_cpm: 11.54
n_lines_expressing: 9
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 14
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PEG3

*paternally expressed 3* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.96× (z +11.3, q 4e-27, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +4.7, q 2e-04, up in 2 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Irinotecan (hydrochloride) (drug)]] 0.5 µM: 0.573× (z -3.9, q 0.047, down in 0 of 7 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.150×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.195×; ⚠ cell-cycle shift, explains ~43% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0620×; ⚠ cell-cycle shift, explains ~45% of this change); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-423 0.0521×).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOB]] (+0.82, fdr 1e-05), [[LNCAROD]] (+0.68, fdr 7e-06), [[AFP]] (+0.62, fdr 0.004, ⚠ one half only (not replicated)), [[FGL1]] (+0.54, fdr 2e-04); moves opposite to [[GPRIN2]] (-0.30, fdr 0.002, ⚠ not reproduced).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC02008]] → it (grade C ⚠); 14 go from it, the strongest it → [[F2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.96×** | +11.3 | 4e-27 | 1/5 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +8.7 | 1e-15 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.14×** | +7.5 | 1e-11 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.09×** | +5.2 | 2e-05 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.7 | 2e-04 | 2/6 (SNU-423, BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.3 | 0.098 | 0/6 | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.11× | +3.2 | 0.12 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12568.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.150×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.195×; ⚠ cell-cycle shift, explains ~43% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0620×; ⚠ cell-cycle shift, explains ~45% of this change); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-423 0.0521×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.573×** | -3.9 | 0.047 | 0/7 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 885 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -16.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 9.63 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0620× (z -9.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 3.72 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0521× (z -8.9) |
| [[A-172 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.994 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.967 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.962 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOB]] | +0.82 | +0.90 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[LNCAROD]] | +0.68 | +0.66 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[AFP]] | +0.62 | +0.78 / +0.06 | ⚠ one half (not replicated) | 0.004 |  |
| [[APOA2]] | +0.59 | +0.88 / -0.33 | ⚠ not reproduced | 1.00 |  |
| [[FGL1]] | +0.54 | +0.70 / +0.29 | both halves | 2e-04 |  |
| [[LRRTM4]] | +0.53 | +0.41 / +0.43 | both halves | 4e-05 | **novel candidate** |
| [[LINC02575]] | +0.46 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[RNF128]] | +0.46 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[NKD1]] | +0.45 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[CARMN]] | +0.45 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[PHYHIPL]] | +0.44 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[ANGPTL2]] | +0.43 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[KRT23]] | +0.43 | +0.49 / +0.28 | both halves | 3e-04 |  |
| [[ATP10A]] | +0.43 | +0.39 / +0.39 | both halves | 5e-05 | STRING 462 |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN2]] | -0.30 | -0.22 / -0.11 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02008]] | C | LINC02008 activity raises PEG3's level | lines that do not express LINC02008 (36) vs lines expressing it (14) | 3.14× lower at baseline in the lines without LINC02008 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01242, ENSG00000260126, ENSG00000253363; co-absent with the target |
| [[PLXDC2]] | C | PLXDC2 activity raises PEG3's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.15× lower at baseline in the lines without PLXDC2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent; co-absent with the target |
| [[AFP]] | C | AFP activity raises PEG3's level | lines that do not express AFP (45) vs lines expressing it (5) | 11.03× lower at baseline in the lines without AFP | 0.061 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[TF]] | C | TF activity raises PEG3's level | lines that do not express TF (41) vs lines expressing it (9) | 4.39× lower at baseline in the lines without TF | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises PEG3's level | lines that do not express CARMN (40) vs lines expressing it (10) | 4.12× lower at baseline in the lines without CARMN | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[A2M]] | C | A2M activity raises PEG3's level | lines that do not express A2M (42) vs lines expressing it (8) | 5.28× lower at baseline in the lines without A2M | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[PAX6]] | C | PAX6 activity raises PEG3's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without PAX6 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1; co-absent with the target |
| [[AXIN2]] | C | AXIN2 activity raises PEG3's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 1.74× lower at baseline in the lines without AXIN2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964; co-absent with the target |
| [[RBP1]] | C | RBP1 activity raises PEG3's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 2.14× lower at baseline in the lines without RBP1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 3, C 11. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2]] | B | PEG3 activity raises F2's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 2.01× lower at baseline in the lines without PEG3 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1 |
| [[MALRD1]] | B | PEG3 activity raises MALRD1's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 2.79× lower at baseline in the lines without PEG3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1 |
| [[COLGALT2]] | B | PEG3 activity raises COLGALT2's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 1.91× lower at baseline in the lines without PEG3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1 |
| [[APOB]] | C | PEG3 activity raises APOB's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 3.55× lower at baseline in the lines without PEG3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[NKD1]] | C | PEG3 activity raises NKD1's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 2.24× lower at baseline in the lines without PEG3 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[AFP]] | C | PEG3 activity raises AFP's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 3.31× lower at baseline in the lines without PEG3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[APOA2]] | C | PEG3 activity raises APOA2's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 2.97× lower at baseline in the lines without PEG3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[LGR5]] | C | PEG3 activity raises LGR5's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 1.67× lower at baseline in the lines without PEG3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[KRT23]] | C | PEG3 activity raises KRT23's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 1.85× lower at baseline in the lines without PEG3 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[HS3ST5]] | C | PEG3 activity raises HS3ST5's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 2.83× lower at baseline in the lines without PEG3 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[A1CF]] | C | PEG3 activity raises A1CF's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 1.72× lower at baseline in the lines without PEG3 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[TF]] | C | PEG3 activity raises TF's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 3.17× lower at baseline in the lines without PEG3 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.277). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.8, 54.0); signed map (65.6, 19.8). **Vector** length 20.4, 5.22% of its response variance represented; |z| ≥ 3 in 195 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.1 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.0 | +8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.0 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.9 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.5 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.5 | +0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.4 | +1.7 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.5 | -1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | +0.5 |
|  | [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -0.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | -0.4 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.4 | -2.4 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | paternally expressed 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:56,810,077-56,840,728 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZKSCAN22, KIAA0287, ZNF904, ZSCAN24 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZU2](https://www.uniprot.org/uniprotkb/Q9GZU2) (Paternally-expressed gene 3 protein):

> Induces apoptosis in cooperation with SIAH1A. Acts as a mediator between p53/TP53 and BAX in a neuronal death pathway that is activated by DNA damage. Acts synergistically with TRAF2 and inhibits TNF induced apoptosis through activation of NF-kappa-B (By similarity). Possesses a tumor suppressing activity in glioma cells.

**Summary**, from NCBI Gene [5178](https://www.ncbi.nlm.nih.gov/gene/5178):

> In human, ZIM2 and PEG3 are treated as two distinct genes though they share multiple 5' exons and a common promoter and both genes are paternally expressed (PMID:15203203). Alternative splicing events connect their shared 5' exons either with the remaining 4 exons unique to ZIM2, or with the remaining 2 exons unique to PEG3. In contrast, in other mammals ZIM2 does not undergo imprinting and, in mouse, cow, and likely other mammals as well, the ZIM2 and PEG3 genes do not share exons. Human PEG3 …

**Accessions** — [HGNC:8826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8826) · Entrez [5178](https://www.ncbi.nlm.nih.gov/gene/5178) · UniProt [Q9GZU2](https://www.uniprot.org/uniprotkb/Q9GZU2) · Ensembl [ENSG00000198300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198300)

## Data

Gene col 12568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12568); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12568]; `tensor/DDL_lfc|DDL_z.npy` [12568]; `embed/gene_vectors.npy` [12568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12568 or target_col == 12568). Every well: [[PEG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

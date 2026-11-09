---
symbol: "IGFBP5"
type: "gene"
col: 3679
ensembl_id: "ENSG00000115461"
name: "insulin like growth factor binding protein 5"
location: "2q35"
module: 66
arm: "+"
pooled_cpm: 63.47
n_lines_expressing: 16
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 25
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# IGFBP5

*insulin like growth factor binding protein 5* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.42× (z +14.3, q 2e-43, up in 8 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Entrectinib (drug)]] 5 µM: 1.65× (z +3.9, q 0.015, up in 6 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.287× (z -9.5, q 9e-19, down in 13 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMP3]] (+0.70, fdr 7e-06), [[EYA1]] (+0.66, fdr 7e-06), [[COL1A2]] (+0.65, fdr 1e-05); moves opposite to [[SHANK2]] (-0.46, fdr 5e-05), [[C16orf74]] (-0.46, fdr 3e-05), [[SLC16A5]] (-0.45, fdr 8e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RIT2]] → it (grade C ⚠); 25 go from it, the strongest it → [[TENT5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.42×** | +14.3 | 2e-43 | 8/15 (SW 900, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.83×** | +9.9 | 9e-21 | 8/12 (BT-474, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.73×** | +9.4 | 2e-18 | 3/12 (BT-474, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.015 | 6/14 (A-172, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | 1.52× | +3.2 | 0.14 | 0/14 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.287×** | -9.5 | 9e-19 | 13/13 (C32, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -7.2 | 1e-10 | 13/13 (H4, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.417×** | -6.7 | 5e-09 | 10/13 (C32, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.415×** | -6.5 | 2e-08 | 13/13 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.480×** | -5.6 | 2e-06 | 14/14 (C32, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.509×** | -5.1 | 3e-05 | 12/14 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.582×** | -4.1 | 0.003 | 12/13 (CHP-212, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.686×** | -4.0 | 0.004 | 6/14 (NCI-H1573, H4, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.617×** | -3.7 | 0.015 | 13/14 (C32, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.621×** | -3.6 | 0.017 | 7/14 (NCI-H1573, H4, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.607×** | -3.5 | 0.023 | 1/14 (SW 1088) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.637×** | -3.4 | 0.027 | 8/14 (C32, SW 900, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.638×** | -3.4 | 0.027 | 6/14 (NCI-H1573, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.639×** | -3.4 | 0.027 | 9/14 (NCI-H1573, J82, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.734×** | -3.3 | 0.035 | 10/14 (H4, J82, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.437×** | -3.2 | 0.044 | 6/14 (C32, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 1,206 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0206× (z -32.5) |
| [[NCI-H1573 (line)]] | alt | 262 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0188× (z -25.7) |
| [[SHP-77 (line)]] | alt | 356 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0231× (z -30.8) |
| [[CHP-212 (line)]] | wt | 135 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0289× (z -18.0) |
| [[H4 (line)]] | wt | 558 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.00343× (z -44.7) |
| [[RPMI-7951 (line)]] | alt | 145 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.00907× (z -25.4) |
| [[BT-474 (line)]] | alt | 556 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0326× (z -18.6) |
| [[Hs 766T (line)]] | wt | 28.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0587× (z -16.6) |
| [[J82 (line)]] | alt | 183 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -14.2) |
| [[SW 900 (line)]] | alt | 48.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.00427× (z -19.5) |
| [[A-172 (line)]] | wt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -8.8) |
| [[HS-578T (line)]] | alt | 45.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0446× (z -11.6) |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.123× (z -10.3) |
| [[A-427 (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.74 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.88 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.09 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.78 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.95 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.42 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.05 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.59 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.77 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMP3]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 | STRING 516 |
| [[EYA1]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[COL1A2]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 494 |
| [[MDGA2]] | +0.64 | +0.72 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[DIRC3]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[FCRLA]] | +0.59 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[TMEM178B]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 | **novel candidate** |
| [[AEBP1]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SETBP1]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PTPRD]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[LOXL3]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[DPYSL3]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHANK2]] | -0.46 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[C16orf74]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SLC16A5]] | -0.45 | -0.39 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIT2]] | C | RIT2 activity raises IGFBP5's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 9.10× lower at baseline in the lines without RIT2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[DOK5]] | C | DOK5 activity raises IGFBP5's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 9.78× lower at baseline in the lines without DOK5 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises IGFBP5's level | lines that do not express CALCA (45) vs lines expressing it (5) | 6.37× lower at baseline in the lines without CALCA | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[PRICKLE2]] | C | PRICKLE2 activity raises IGFBP5's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 4.39× lower at baseline in the lines without PRICKLE2 | 0.094 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises IGFBP5's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 6.96× lower at baseline in the lines without SYT4 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[CDH8]] | C | CDH8 activity raises IGFBP5's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 6.08× lower at baseline in the lines without CDH8 | 0.095 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[ZNF883]] | C | ZNF883 activity raises IGFBP5's level | lines that do not express ZNF883 (22) vs lines expressing it (28) | 2.66× lower at baseline in the lines without ZNF883 | 0.0999 | ⚠ within organs, on part of the lines; also absent: AK5, SOX5, GAP43; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 8, C 17. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENT5A]] | B | IGFBP5 activity raises TENT5A's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without IGFBP5 | 0.014 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[NYAP2]] | B | IGFBP5 activity raises NYAP2's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without IGFBP5 | 0.023 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[SETBP1]] | B | IGFBP5 activity raises SETBP1's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 5.36× lower at baseline in the lines without IGFBP5 | 0.031 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[DIRC3]] | B | IGFBP5 activity raises DIRC3's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 3.32× lower at baseline in the lines without IGFBP5 | 0.052 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[SLC14A2]] | B | IGFBP5 activity raises SLC14A2's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without IGFBP5 | 0.059 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[DIRC3-AS1]] | B | IGFBP5 activity raises DIRC3-AS1's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.80× lower at baseline in the lines without IGFBP5 | 0.060 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[SLC6A6]] | B | IGFBP5 activity raises SLC6A6's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without IGFBP5 | 0.078 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[MAN1C1]] | B | IGFBP5 activity raises MAN1C1's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without IGFBP5 | 0.084 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[DOK5]] | C | IGFBP5 activity raises DOK5's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.68× lower at baseline in the lines without IGFBP5 | 7e-04 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[TIMP3]] | C | IGFBP5 activity raises TIMP3's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 9.02× lower at baseline in the lines without IGFBP5 | 0.016 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[SLITRK6]] | C | IGFBP5 activity raises SLITRK6's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 3.02× lower at baseline in the lines without IGFBP5 | 0.019 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[SEMA5A]] | C | IGFBP5 activity raises SEMA5A's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 7.01× lower at baseline in the lines without IGFBP5 | 0.024 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.7, 27.2); signed map (30.0, 41.7). **Vector** length 73.2, 25.6% of its response variance represented; |z| ≥ 3 in 613 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Scavenging by Class A Receptors* (reactome, mean cos +0.51 to 5); *Binding and Uptake of Ligands by Scavenger Receptors* (reactome, mean cos +0.52 to 6); *Developmental Lineage of Pancreatic Ductal Cells* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | -1.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor binding protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:216,672,105-216,695,549 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Insulin like growth factor binding proteins |
| Hallmark sets | UV_RESPONSE_DN, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P24593](https://www.uniprot.org/uniprotkb/P24593) (Insulin-like growth factor-binding protein 5):

> Multifunctional protein that plays a critical role in regulating the availability of IGFs to their receptors and thereby regulates IGF-mediated cellular processes including proliferation, differentiation, and apoptosis in a cell-type specific manner. Increases the cell proliferation of osteoblasts, intestinal smooth muscle cells and neuroblastoma cells. Enhances adhesion and survival of epithelial cells but decreases adhesion of mesenchymal cells (By similarity). Once secreted, acts as a major …

**Summary**, from NCBI Gene [3488](https://www.ncbi.nlm.nih.gov/gene/3488):

> Enables insulin-like growth factor I binding activity and receptor ligand activity. Involved in several processes, including cellular response to cAMP; regulation of smooth muscle cell migration; and regulation of smooth muscle cell proliferation. Part of insulin-like growth factor ternary complex. Biomarker of pulmonary fibrosis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:5474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5474) · Entrez [3488](https://www.ncbi.nlm.nih.gov/gene/3488) · UniProt [P24593](https://www.uniprot.org/uniprotkb/P24593) · Ensembl [ENSG00000115461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115461)

## Data

Gene col 3679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3679); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3679]; `tensor/DDL_lfc|DDL_z.npy` [3679]; `embed/gene_vectors.npy` [3679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3679 or target_col == 3679). Every well: [[IGFBP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFBP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

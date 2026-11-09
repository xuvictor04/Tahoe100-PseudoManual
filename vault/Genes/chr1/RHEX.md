---
symbol: "RHEX"
type: "gene"
col: 15432
ensembl_id: "ENSG00000263961"
name: "regulator of hemoglobinization and erythroid cell expansion"
location: "1q32.1"
module: 8
arm: "+"
pooled_cpm: 22.52
n_lines_expressing: 7
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 26
direction_downstream: 32
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RHEX

*regulator of hemoglobinization and erythroid cell expansion* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.38× (z +11.0, q 2e-25, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +7.6, q 1e-11, up in 1 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.0336×, A498 0.118×, LoVo 0.140×; ⚠ cell-cycle shift, explains ~53% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (HEC-1-A 0.0553×, A498 0.103×, CFPAC-1 0.0934×; ⚠ cell-cycle shift, explains ~40% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.0768×, A498 0.164×; ⚠ cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.188×, CFPAC-1 0.160×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMD4]] (+0.77, fdr 7e-06), [[DSCAML1]] (+0.67, fdr 7e-06), [[POU5F1]] (+0.66, fdr 7e-06); moves opposite to [[FIBCD1]] (-0.43, fdr 1e-04), [[CA2]] (-0.42, fdr 2e-04), [[NECTIN1]] (-0.42, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[UGT2B7]] → it (grade C ⚠); 32 go from it, the strongest it → [[ZNF385B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.38×** | +11.0 | 2e-25 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +7.6 | 1e-11 | 1/5 (LoVo) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +7.0 | 4e-10 | 1/5 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +6.6 | 7e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.75×** | +4.5 | 9e-04 | 5/5 (HEC-1-A, CFPAC-1, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +4.1 | 0.004 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +3.9 | 0.008 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.4 | 0.054 | 1/4 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.057 | 4/5 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.057 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Afatinib (drug)]] 0.05 µM |  | **1.37×** | +3.2 | 0.060 | 0/5 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15432.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.0336×, A498 0.118×, LoVo 0.140×; ⚠ cell-cycle shift, explains ~53% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (HEC-1-A 0.0553×, A498 0.103×, CFPAC-1 0.0934×; ⚠ cell-cycle shift, explains ~40% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (HEC-1-A 0.0768×, A498 0.164×; ⚠ cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.188×, CFPAC-1 0.160×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.847× | -4.6 | 0.003 | 0/5 | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.735× | -3.4 | 0.14 | 5/5 (A498, HEC-1-A, …) | top dose only | position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.647× | -3.4 | 0.14 | 0/5 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 357 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0336× (z -15.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -10.8) |
| [[A498 (line)]] | wt | 171 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -11.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[CFPAC-1 (line)]] | alt | 83.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -10.3) |
| [[LoVo (line)]] | wt | 9.32 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -9.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMD4]] | +0.77 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[DSCAML1]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[POU5F1]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[HAVCR1]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[CP]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[SLC34A2]] | +0.61 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[FGA]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ARSL]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PREX2]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[PDZK1IP1]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ABCC6]] | +0.55 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[SLC15A1]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIBCD1]] | -0.43 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[CA2]] | -0.42 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[NECTIN1]] | -0.42 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[KDM7A]] | -0.40 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[PLEKHG5]] | -0.39 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[CAPRIN2]] | -0.39 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[WDFY2]] | -0.39 | -0.31 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 0, C 26. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT2B7]] | C | UGT2B7 activity raises RHEX's level | lines that do not express UGT2B7 (37) vs lines expressing it (13) | 3.12× lower at baseline in the lines without UGT2B7 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A1, AFP, RHEX; co-absent with the target |
| [[SLC34A2]] | C | SLC34A2 activity raises RHEX's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 2.09× lower at baseline in the lines without SLC34A2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP; co-absent with the target |
| [[FGG]] | C | FGG activity raises RHEX's level | lines that do not express FGG (42) vs lines expressing it (8) | 1.89× lower at baseline in the lines without FGG | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[FGA]] | C | FGA activity raises RHEX's level | lines that do not express FGA (43) vs lines expressing it (7) | 2.25× lower at baseline in the lines without FGA | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises RHEX's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 5.77× lower at baseline in the lines without TIMD4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[SMIM2-AS1]] | C | SMIM2-AS1 activity raises RHEX's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 1.33× lower at baseline in the lines without SMIM2-AS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent; co-absent with the target |
| [[GABRP]] | C | GABRP activity raises RHEX's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.48× lower at baseline in the lines without GABRP | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises RHEX's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 4.87× lower at baseline in the lines without HAVCR1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[RNF183]] | C | RNF183 activity raises RHEX's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 2.43× lower at baseline in the lines without RNF183 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1; co-absent with the target |
| [[FXYD2]] | C | FXYD2 activity raises RHEX's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without FXYD2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises RHEX's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.00× lower at baseline in the lines without ADGRF1 | 0.033 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises RHEX's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 1.48× lower at baseline in the lines without STEAP4 | 0.037 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 9, C 23. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF385B]] | B | RHEX activity raises ZNF385B's level | lines that do not express RHEX (43) vs lines expressing it (7) | 3.44× lower at baseline in the lines without RHEX | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[HNF4G]] | B | RHEX activity raises HNF4G's level | lines that do not express RHEX (43) vs lines expressing it (7) | 3.52× lower at baseline in the lines without RHEX | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[CHST9]] | B | RHEX activity raises CHST9's level | lines that do not express RHEX (43) vs lines expressing it (7) | 3.19× lower at baseline in the lines without RHEX | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[TMEM51-AS1]] | B | RHEX activity raises TMEM51-AS1's level | lines that do not express RHEX (43) vs lines expressing it (7) | 2.28× lower at baseline in the lines without RHEX | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[LNX1]] | B | RHEX activity raises LNX1's level | lines that do not express RHEX (43) vs lines expressing it (7) | 2.97× lower at baseline in the lines without RHEX | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[SLC44A3]] | B | RHEX activity raises SLC44A3's level | lines that do not express RHEX (43) vs lines expressing it (7) | 2.56× lower at baseline in the lines without RHEX | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[TLR3]] | B | RHEX activity raises TLR3's level | lines that do not express RHEX (43) vs lines expressing it (7) | 2.12× lower at baseline in the lines without RHEX | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[SLC44A3-AS1]] | B | RHEX activity raises SLC44A3-AS1's level | lines that do not express RHEX (43) vs lines expressing it (7) | 2.69× lower at baseline in the lines without RHEX | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[ACTR3C]] | B | RHEX activity raises ACTR3C's level | lines that do not express RHEX (43) vs lines expressing it (7) | 2.28× lower at baseline in the lines without RHEX | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[APOL1]] | C | RHEX activity raises APOL1's level | lines that do not express RHEX (43) vs lines expressing it (7) | 6.53× lower at baseline in the lines without RHEX | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB; co-absent with the target |
| [[UGT2B7]] | C | RHEX activity raises UGT2B7's level | lines that do not express RHEX (43) vs lines expressing it (7) | 6.66× lower at baseline in the lines without RHEX | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB; co-absent with the target |
| [[CATSPERB]] | C | RHEX activity raises CATSPERB's level | lines that do not express RHEX (43) vs lines expressing it (7) | 3.01× lower at baseline in the lines without RHEX | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.6, 44.4); signed map (52.0, 27.0). **Vector** length 32.0, 15.7% of its response variance represented; |z| ≥ 3 in 184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.8 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.8 | +3.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -0.9 | -1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -0.7 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -0.7 | -2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.6 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.6 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | regulator of hemoglobinization and erythroid cell expansion |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,053,173-206,102,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16052; previously C1orf186 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZWK4](https://www.uniprot.org/uniprotkb/Q6ZWK4) (Regulator of hemoglobinization and erythroid cell expansion protein):

> Acts as a signaling transduction factor of the EPO-EPOR signaling pathway promoting erythroid cell differentiation.

**Summary**, from NCBI Gene [440712](https://www.ncbi.nlm.nih.gov/gene/440712):

> Enables erythropoietin receptor binding activity. Involved in erythropoietin-mediated signaling pathway and positive regulation of erythrocyte differentiation. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25341) · Entrez [440712](https://www.ncbi.nlm.nih.gov/gene/440712) · UniProt [Q6ZWK4](https://www.uniprot.org/uniprotkb/Q6ZWK4) · Ensembl [ENSG00000263961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263961)

## Data

Gene col 15432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15432); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15432]; `tensor/DDL_lfc|DDL_z.npy` [15432]; `embed/gene_vectors.npy` [15432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15432 or target_col == 15432). Every well: [[RHEX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHEX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

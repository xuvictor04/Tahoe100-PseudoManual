---
symbol: "MIR137HG"
type: "gene"
col: 13442
ensembl_id: "ENSG00000225206"
name: "MIR137 host gene"
location: "1p21.3"
module: 121
arm: "+"
pooled_cpm: 9.71
n_lines_expressing: 22
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 14
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# MIR137HG

*MIR137 host gene* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +8.2, q 1e-13, up in 0 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +4.8, q 2e-04, up in 1 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 4.19×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.471× (z -7.2, q 3e-10, down in 16 of 19 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.681× (z -3.7, q 0.021, down in 8 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-172 0.0592×, SNU-423 0.0553×, A-427 0.196×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (A-427 0.142×, LOX-IMVI 0.0955×, NCI-H1792 0.122×; ⚠ cell-cycle shift, explains ~66% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H23 0.109×, NCI-H1792 0.237×, A-172 0.294×); [[Roxadustat (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0662×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EVC2]] (+0.68, fdr 7e-06), [[PAPPA]] (+0.68, fdr 7e-06), [[MAGI2]] (+0.61, fdr 1e-05); moves opposite to [[PDIA4]] (-0.46, fdr 2e-04), [[RNASET2]] (-0.46, fdr 1e-04), [[SPICE1]] (-0.46, fdr 6e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC01429]] → it (grade B ⚠); 14 go from it, the strongest it → [[TRPC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13442.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 4.19×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +8.2 | 1e-13 | 0/14 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +7.8 | 2e-12 | 1/14 (MIA PaCa-2) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +7.5 | 1e-11 | 2/14 (A-427, MIA PaCa-2) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.8 | 2e-04 | 1/20 (MIA PaCa-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.41×** | +4.7 | 3e-04 | 10/20 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +3.8 | 0.014 | 6/19 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.057 | 4/20 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.41× | +3.2 | 0.11 | 4/19 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.86× | +3.1 | 0.12 | 1/14 (RPMI-7951) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13442.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-172 0.0592×, SNU-423 0.0553×, A-427 0.196×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (A-427 0.142×, LOX-IMVI 0.0955×, NCI-H1792 0.122×; ⚠ cell-cycle shift, explains ~66% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H23 0.109×, NCI-H1792 0.237×, A-172 0.294×); [[Roxadustat (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0662×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.471×** | -7.2 | 3e-10 | 16/19 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.507×** | -6.5 | 2e-08 | 16/19 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.544×** | -5.8 | 1e-06 | 16/19 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.610×** | -4.5 | 0.001 | 2/19 (SHP-77, CFPAC-1) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.663×** | -3.8 | 0.016 | 7/19 (hTERT-HPNE, A-427, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.681×** | -3.7 | 0.021 | 8/19 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.723× | -3.1 | 0.15 | 10/19 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.64 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 30.8 | 0 | 8 (7 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0592× (z -15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 39.3 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -12.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -11.5) |
| [[A-427 (line)]] | wt | 113 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -13.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 0 | 4 (3 ⚠) | — | [[Roxadustat (drug)]] 0.05 µM 0.0662× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 36.9 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0926× (z -13.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0553× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -8.6) ⚠ cell-cycle shift, explains ~63% of this change |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0894× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.76 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0725× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.527 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EVC2]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PAPPA]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MAGI2]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ZEB2]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[APBB1IP]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MSC-AS1]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MIR548XHG]] | +0.59 | +0.49 / +0.50 | both halves | 2e-05 | same gene group |
| [[LINC00470]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[FLRT2]] | +0.57 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[OR9Q1]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LINC02377]] | +0.56 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[MIR3171HG]] | +0.55 | +0.46 / +0.61 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA4]] | -0.46 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[RNASET2]] | -0.46 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SPICE1]] | -0.46 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01429]] | B | LINC01429 activity raises MIR137HG's level | lines that do not express LINC01429 (6) vs lines expressing it (44) | 2.92× lower at baseline in the lines without LINC01429 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01762, MPP4, ENSG00000237356; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MIR137HG's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZEB2]] | C | ZEB2 activity raises MIR137HG's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 4.54× lower at baseline in the lines without ZEB2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[TSHZ3-AS1]] | C | TSHZ3-AS1 activity raises MIR137HG's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 4.39× lower at baseline in the lines without TSHZ3-AS1 | 0.035 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[WNT5B]] | C | WNT5B activity raises MIR137HG's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 4.24× lower at baseline in the lines without WNT5B | 0.037 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; co-absent with the target |
| [[MME]] | C | MME activity raises MIR137HG's level | lines that do not express MME (30) vs lines expressing it (20) | 4.21× lower at baseline in the lines without MME | 0.039 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[AKT3]] | C | AKT3 activity raises MIR137HG's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 4.13× lower at baseline in the lines without AKT3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises MIR137HG's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.07× lower at baseline in the lines without EVC2 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[GPR176]] | C | GPR176 activity raises MIR137HG's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 4.17× lower at baseline in the lines without GPR176 | 0.091 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPC1]] | B | MIR137HG activity raises TRPC1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.82× lower at baseline in the lines without MIR137HG | 0.018 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2 |
| [[IPO9-AS1]] | B | MIR137HG activity raises IPO9-AS1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 1.49× lower at baseline in the lines without MIR137HG | 0.045 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2 |
| [[ZKSCAN7-AS1]] | B | MIR137HG activity raises ZKSCAN7-AS1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 1.29× lower at baseline in the lines without MIR137HG | 0.090 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2 |
| [[GSDME]] | B | MIR137HG activity raises GSDME's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.57× lower at baseline in the lines without MIR137HG | 0.094 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2 |
| [[AKT3]] | C | MIR137HG activity raises AKT3's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 5.34× lower at baseline in the lines without MIR137HG | 0.002 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[ADAMTS12]] | C | MIR137HG activity raises ADAMTS12's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 4.69× lower at baseline in the lines without MIR137HG | 0.014 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[TSHZ3-AS1]] | C | MIR137HG activity raises TSHZ3-AS1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.89× lower at baseline in the lines without MIR137HG | 0.026 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[JAM2]] | C | MIR137HG activity raises JAM2's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.59× lower at baseline in the lines without MIR137HG | 0.030 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[MME]] | C | MIR137HG activity raises MME's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 5.45× lower at baseline in the lines without MIR137HG | 0.034 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[MSR1]] | C | MIR137HG activity raises MSR1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.43× lower at baseline in the lines without MIR137HG | 0.039 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[APBB1IP]] | C | MIR137HG activity raises APBB1IP's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without MIR137HG | 0.062 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[EVC2]] | C | MIR137HG activity raises EVC2's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.96× lower at baseline in the lines without MIR137HG | 0.083 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.7, 20.8); signed map (27.7, 48.1). **Vector** length 60.9, 18.8% of its response variance represented; |z| ≥ 3 in 448 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.2 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.4 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -1.6 | -7.2 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -1.3 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MIR137 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p21.3 — chr1:97,933,474-98,049,871 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [400765](https://www.ncbi.nlm.nih.gov/gene/400765):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:42871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42871) · Entrez [400765](https://www.ncbi.nlm.nih.gov/gene/400765) · Ensembl [ENSG00000225206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225206)

## Data

Gene col 13442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13442); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13442]; `tensor/DDL_lfc|DDL_z.npy` [13442]; `embed/gene_vectors.npy` [13442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13442 or target_col == 13442). Every well: [[MIR137HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR137HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

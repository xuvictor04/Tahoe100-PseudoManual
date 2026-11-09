---
symbol: "CDH7"
type: "gene"
col: 1308
ensembl_id: "ENSG00000081138"
name: "cadherin 7"
location: "18q22.1"
module: 19
arm: "+"
pooled_cpm: 4.98
n_lines_expressing: 15
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 14
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CDH7

*cadherin 7* — 18q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.20× (z +11.7, q 5e-29, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.63× (z +10.1, q 7e-22, up in 3 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (H4 0.0201×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.189×); [[Daptomycin (drug)]] 0.5 µM in 1 line (H4 0.0344×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.292×); [[Budesonide (drug)]] 5 µM in 1 line (H4 0.0682×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01035]] (+0.79, fdr 7e-06), [[LINC03000]] (+0.77, fdr 7e-06), [[GLP2R]] (+0.77, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NALCN]] → it (grade B ⚠); 14 go from it, the strongest it → [[ANO3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.20×** | +11.7 | 5e-29 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.48×** | +11.1 | 3e-26 | 2/6 (NCI-H2347, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +10.1 | 7e-22 | 3/10 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +7.5 | 1e-11 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +6.7 | 3e-09 | 5/10 (BT-474, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.20×** | +4.2 | 0.003 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.004 | 7/12 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.74×** | +3.9 | 0.007 | 0/3 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +3.5 | 0.026 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.041 | 5/12 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.054 | 6/11 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.064 | 1/8 (NCI-H2347) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.2 | 0.064 | 1/8 (NCI-H2347) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.1 | 0.067 | 2/6 (NCI-H2347, SHP-77) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +3.0 | 0.096 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.49×** | +3.0 | 0.096 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.0 | 0.096 | 2/9 (SK-MEL-2, NCI-H2347) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +2.9 | 0.097 | 4/13 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1308.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (H4 0.0201×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.189×); [[Daptomycin (drug)]] 0.5 µM in 1 line (H4 0.0344×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.292×); [[Budesonide (drug)]] 5 µM in 1 line (H4 0.0682×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.642× | -3.0 | 0.98 | 1/12 (BT-474) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 35.0 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0201× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 5 µM 0.0682× (z -9.4) |
| [[NCI-H661 (line)]] | alt | 461 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -11.8) |
| [[BT-474 (line)]] | alt | 1.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.2× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 2.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.8) |
| [[A-172 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.539 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01035]] | +0.79 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[LINC03000]] | +0.77 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.77 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PDE7B]] | +0.76 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CTNND2]] | +0.76 | +0.74 / +0.62 | both halves | 7e-06 | STRING 451 |
| [[GREM2]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[KCNK2]] | +0.75 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.74 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[CHL1]] | +0.73 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[TBXT]] ⚠ | +0.72 | +0.61 / +0.64 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PDE1A]] | +0.72 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[SCARA5]] | +0.72 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PAX7]] | +0.71 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NALCN]] | B | NALCN activity lowers CDH7's level | lines that do not express NALCN (22) vs lines expressing it (28) | 1.25× higher at baseline in the lines without NALCN | 0.037 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[KCNH5]] | C | KCNH5 activity raises CDH7's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 4.91× lower at baseline in the lines without KCNH5 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises CDH7's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.71× lower at baseline in the lines without BCHE | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[PGR]] | C | PGR activity raises CDH7's level | lines that do not express PGR (36) vs lines expressing it (14) | 3.57× lower at baseline in the lines without PGR | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises CDH7's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.62× lower at baseline in the lines without MIR99AHG | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[CNTN1]] | C | CNTN1 activity raises CDH7's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 3.32× lower at baseline in the lines without CNTN1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; co-absent with the target |
| [[TTTY14]] | C | TTTY14 activity raises CDH7's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 2.32× lower at baseline in the lines without TTTY14 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO3]] | B | CDH7 activity raises ANO3's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 1.92× lower at baseline in the lines without CDH7 | 0.014 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9 |
| [[SEMA6A]] | B | CDH7 activity raises SEMA6A's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 2.42× lower at baseline in the lines without CDH7 | 0.072 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9 |
| [[KCNH5]] | C | CDH7 activity raises KCNH5's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 6.23× lower at baseline in the lines without CDH7 | 0.006 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[MARCHF1]] | C | CDH7 activity raises MARCHF1's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 3.82× lower at baseline in the lines without CDH7 | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[DOK6]] | C | CDH7 activity raises DOK6's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 3.68× lower at baseline in the lines without CDH7 | 0.027 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[CADM2]] | C | CDH7 activity raises CADM2's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 5.64× lower at baseline in the lines without CDH7 | 0.029 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[ACSS3]] | C | CDH7 activity raises ACSS3's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 2.41× lower at baseline in the lines without CDH7 | 0.029 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[NCAM2]] | C | CDH7 activity raises NCAM2's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 5.53× lower at baseline in the lines without CDH7 | 0.038 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[EGF]] | C | CDH7 activity raises EGF's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 2.74× lower at baseline in the lines without CDH7 | 0.048 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[NPFFR2]] | C | CDH7 activity raises NPFFR2's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 2.58× lower at baseline in the lines without CDH7 | 0.069 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[ASXL3]] | C | CDH7 activity raises ASXL3's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 3.31× lower at baseline in the lines without CDH7 | 0.069 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[LINC02994]] | C | CDH7 activity raises LINC02994's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 3.33× lower at baseline in the lines without CDH7 | 0.069 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, 35.3); signed map (42.3, 43.3). **Vector** length 41.0, 12.8% of its response variance represented; |z| ≥ 3 in 334 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.53 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +0.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.1 — chr18:65,750,252-65,890,337 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Type II classical cadherins |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULB5](https://www.uniprot.org/uniprotkb/Q9ULB5) (Cadherin-7):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types.

**Summary**, from NCBI Gene [1005](https://www.ncbi.nlm.nih.gov/gene/1005):

> This gene encodes a type II classical cadherin of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature glycoprotein. This calcium dependent cell-cell adhesion molecule is comprised of five extracellular cadherin repeats, a transmembrane region and a highly conserved cytoplasmic tail. Type II (atypical) cadherins are defined based on their lack of a …

**Accessions** — [HGNC:1766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1766) · Entrez [1005](https://www.ncbi.nlm.nih.gov/gene/1005) · UniProt [Q9ULB5](https://www.uniprot.org/uniprotkb/Q9ULB5) · Ensembl [ENSG00000081138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081138)

## Data

Gene col 1308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1308); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1308]; `tensor/DDL_lfc|DDL_z.npy` [1308]; `embed/gene_vectors.npy` [1308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1308 or target_col == 1308). Every well: [[CDH7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

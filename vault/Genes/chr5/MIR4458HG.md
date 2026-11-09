---
symbol: "MIR4458HG"
type: "gene"
col: 14497
ensembl_id: "ENSG00000247516"
name: "MIR4458 host gene"
location: "5p15.31"
module: 24
arm: "+"
pooled_cpm: 7.34
n_lines_expressing: 38
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MIR4458HG

*MIR4458 host gene* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.27× (z +12.3, q 5e-32, up in 33 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (CFPAC-1 4.67×, A498 3.59×, NCI-H2347 3.36×, NCI-H460 3.70×, …).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.586× (z -5.6, q 1e-05, down in 22 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.298×); [[Thymopentin (drug)]] 5 µM in 1 line (A549 0.0666×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG19]] (+0.79, fdr 7e-06), [[COMMD6]] (+0.78, fdr 7e-06), [[MZT2B]] (+0.74, fdr 7e-06); moves opposite to [[SRSF3]] (-0.71, fdr 7e-06), [[SFPQ]] (-0.71, fdr 1e-05), [[CEP41]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[KCTD7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (CFPAC-1 4.67×, A498 3.59×, NCI-H2347 3.36×, NCI-H460 3.70×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.27×** | +12.3 | 5e-32 | 33/33 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.87×** | +7.4 | 3e-11 | 25/28 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.01×** | +5.1 | 5e-05 | 15/23 (C32, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.70×** | +3.6 | 0.036 | 8/17 (SW480, NCI-H1792, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +3.6 | 0.036 | 19/36 (C32, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.66×** | +3.6 | 0.036 | 4/12 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.3 | 0.080 | 16/34 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +3.2 | 0.099 | 15/32 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.53× | +3.1 | 0.12 | 13/32 (A498, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.298×); [[Thymopentin (drug)]] 5 µM in 1 line (A549 0.0666×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.586×** | -5.6 | 1e-05 | 22/35 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.535×** | -4.6 | 0.001 | 18/33 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.630× | -3.2 | 0.24 | 11/36 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.632× | -3.1 | 0.24 | 9/36 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 19.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.6) |
| [[A-427 (line)]] | wt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +8.5) | — |
| [[A498 (line)]] | wt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.9) | — |
| [[A549 (line)]] | wt | 4.45 | 0 | 1 | — | [[Thymopentin (drug)]] 5 µM 0.0666× (z -8.5) |
| [[BT-474 (line)]] | alt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.6) | — |
| [[C32 (line)]] | wt | 8.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 8.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG19]] | +0.79 | +0.63 / +0.81 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.78 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[MZT2B]] | +0.74 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[NENF]] | +0.73 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[HIGD2A]] | +0.73 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[APOC1]] | +0.73 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[RHOQ-AS1]] | +0.72 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[RABAC1]] | +0.71 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[ADGRL3-AS1]] | +0.71 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[MZT2A]] | +0.71 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.71 | +0.39 / +0.78 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF3]] | -0.71 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[SFPQ]] | -0.71 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[CEP41]] | -0.70 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[YWHAE]] | -0.67 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.65 | -0.54 / -0.74 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.65 | -0.49 / -0.73 | both halves | 1e-05 |  |
| [[GMFB]] | -0.64 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.64 | -0.60 / -0.67 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCTD7]] | B | MIR4458HG activity lowers KCTD7's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.61× higher at baseline in the lines without MIR4458HG | 0.036 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |
| [[OST4]] | B | MIR4458HG activity lowers OST4's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.38× higher at baseline in the lines without MIR4458HG | 0.043 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |
| [[EIF4ENIF1]] | B | MIR4458HG activity lowers EIF4ENIF1's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.19× higher at baseline in the lines without MIR4458HG | 0.068 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |
| [[FNTB]] | B | MIR4458HG activity raises FNTB's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.24× lower at baseline in the lines without MIR4458HG | 0.089 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |
| [[SNHG9]] | B | MIR4458HG activity lowers SNHG9's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without MIR4458HG | 0.090 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |
| [[LINC02210-CRHR1]] | B | MIR4458HG activity raises LINC02210-CRHR1's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without MIR4458HG | 0.098 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.0, -23.7); signed map (-32.3, 9.8). **Vector** length 55.9, 11.8% of its response variance represented; |z| ≥ 3 in 437 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +12.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +7.4 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.7 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.4 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.0 | +2.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +0.9 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -2.9 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.8 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -0.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.1 | -0.5 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | MIR4458 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p15.31 — chr5:8,450,701-8,486,930 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49008) · Entrez [100505738](https://www.ncbi.nlm.nih.gov/gene/100505738) · Ensembl [ENSG00000247516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247516)

## Data

Gene col 14497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14497); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14497]; `tensor/DDL_lfc|DDL_z.npy` [14497]; `embed/gene_vectors.npy` [14497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14497 or target_col == 14497). Every well: [[MIR4458HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR4458HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

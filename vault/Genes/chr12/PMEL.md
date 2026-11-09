---
symbol: "PMEL"
type: "gene"
col: 11713
ensembl_id: "ENSG00000185664"
name: "premelanosome protein"
location: "12q13.2"
module: 1
arm: "-"
pooled_cpm: 9.23
n_lines_expressing: 37
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PMEL

*premelanosome protein* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.89× (z +12.8, q 7e-35, up in 10 of 12 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +10.5, q 2e-23, up in 19 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (A-172 0.0675×); [[Ferulic acid (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0727×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0835×; ⚠ cell-cycle shift, explains ~3% of this change).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNNI3]] (+0.57, fdr 2e-04), [[CLDN10]] (+0.56, fdr 4e-05), [[SLC26A5]] (+0.55, fdr 2e-04); moves opposite to [[ICE2]] (-0.57, fdr 1e-04), [[DPH5]] (-0.55, fdr 1e-04), [[PRMT5]] (-0.54, fdr 4e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CYP2U1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.89×** | +12.8 | 7e-35 | 10/12 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.42×** | +11.2 | 2e-26 | 3/4 (A498, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +10.5 | 2e-23 | 19/27 (LOX-IMVI, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.22×** | +9.6 | 8e-20 | 4/5 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.63×** | +9.1 | 9e-18 | 26/33 (Panc 03.27, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.36×** | +8.1 | 6e-14 | 25/31 (Panc 03.27, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.99×** | +6.5 | 8e-09 | 18/32 (Panc 03.27, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.92×** | +6.1 | 6e-08 | 9/21 (SW480, NCI-H2347, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.7 | 9e-07 | 7/14 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.70×** | +4.8 | 9e-05 | 8/25 (SK-MEL-2, A-172, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.6 | 3e-04 | 9/31 (A-427, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.002 | 10/30 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.003 | 3/31 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.53×** | +3.8 | 0.005 | 4/25 (SK-MEL-2, AsPC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.52×** | +3.8 | 0.007 | 4/19 (A-172, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.043 | 3/32 (SK-MEL-2, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.056 | 4/26 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.056 | 1/21 (LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (A-172 0.0675×); [[Ferulic acid (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0727×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0835×; ⚠ cell-cycle shift, explains ~3% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 4.53 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 15.1× (z +9.2) ⚠ cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.0835× (z -8.5) ⚠ cell-cycle shift, explains ~3% of this change |
| [[A-172 (line)]] | wt | 2.71 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.0675× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 2.98 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0727× (z -8.5) |
| [[A-427 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNNI3]] | +0.57 | +0.32 / +0.62 | both halves | 2e-04 |  |
| [[CLDN10]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[SLC26A5]] | +0.55 | +0.31 / +0.74 | both halves | 2e-04 |  |
| [[METRN]] | +0.54 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[LINC00698]] | +0.54 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[RNF24]] | +0.53 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[FAM13B]] | +0.52 | +0.23 / +0.54 | both halves | 5e-04 |  |
| [[PI4KAP1]] | +0.52 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[SLC17A7]] | +0.52 | +0.14 / +0.61 | ⚠ one half (not replicated) | 0.002 |  |
| [[CYBA]] | +0.52 | +0.45 / +0.27 | both halves | 3e-04 |  |
| [[LYPD5]] | +0.52 | +0.22 / +0.52 | both halves | 6e-04 |  |
| [[PI4KAP1-1]] | +0.51 | +0.43 / +0.32 | both halves | 2e-04 |  |
| [[NFATC2IP-AS1]] | +0.51 | +0.36 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICE2]] | -0.57 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[DPH5]] | -0.55 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[PRMT5]] | -0.54 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LARS1]] | -0.52 | -0.37 / -0.45 | both halves | 7e-05 | pathway: MITF-M-regulated melanocyte development |
| [[MAPKAPK5]] | -0.51 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[GUF1]] | -0.51 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[SRP72]] | -0.51 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[KICS2]] | -0.51 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[DNAJC11]] | -0.50 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[RNF6]] | -0.50 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[MTHFSD]] | -0.50 | -0.23 / -0.47 | both halves | 6e-04 |  |
| [[ZXDB]] | -0.50 | -0.27 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PMEL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CCK]] | B | CCK activity raises PMEL's level | lines that do not express CCK (42) vs lines expressing it (8) | 1.06× lower at baseline in the lines without CCK | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: BMP10, ENSG00000287530, S100A8 |
| [[AMBP]] | B | AMBP activity raises PMEL's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.20× lower at baseline in the lines without AMBP | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[PI4KAP1-1]] | B | PI4KAP1-1 activity lowers PMEL's level | lines that do not express PI4KAP1-1 (26) vs lines expressing it (24) | 1.08× higher at baseline in the lines without PI4KAP1-1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1, ENSG00000260573, LCK |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP2U1-AS1]] | B | PMEL activity raises CYP2U1-AS1's level | lines that do not express PMEL (13) vs lines expressing it (37) | 1.25× lower at baseline in the lines without PMEL | 0.032 | ⚠ within organs, on part of the lines; also absent: CGN, SH3BGRL2, MDFI; maybe low, not absent |
| [[LINC00922]] | B | PMEL activity lowers LINC00922's level | lines that do not express PMEL (13) vs lines expressing it (37) | 2.35× higher at baseline in the lines without PMEL | 0.074 | ⚠ within organs, on part of the lines; also absent: CGN, SH3BGRL2, MDFI; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (18.2, 34.6); signed map (26.7, 14.4). **Vector** length 27.3, 2.68% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +2.0 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +2.0 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.6 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +1.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +0.7 | +1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.6 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -1.6 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | premelanosome protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,954,105-55,973,317 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D12S53E, SI, Pmel17, gp100, HMB-45, ME20, HMB45; previously SIL, SILV |
| Reactome | 3 pathways, smallest: Regulation of MITF-M-dependent genes involved in pigmentation; MITF-M-dependent gene expression; MITF-M-regulated melanocyte development |
| Matched by | ensembl_id |

**Function**, from UniProt [P40967](https://www.uniprot.org/uniprotkb/P40967) (Melanocyte protein PMEL):

> Forms physiological amyloids that play a central role in melanosome morphogenesis and pigmentation. The maturation of unpigmented premelanosomes from stage I to II is marked by assembly of processed amyloidogenic fragments into parallel fibrillar sheets, which elongate the vesicle into a striated ellipsoidal shape. In pigmented stage III and IV melanosomes, the amyloid matrix serves as a platform where eumelanin precursors accumulate at high local concentrations for pigment formation. May …

**Summary**, from NCBI Gene [6490](https://www.ncbi.nlm.nih.gov/gene/6490):

> This gene encodes a melanocyte-specific type I transmembrane glycoprotein. The encoded protein is enriched in melanosomes, which are the melanin-producing organelles in melanocytes, and plays an essential role in the structural organization of premelanosomes. This protein is involved in generating internal matrix fibers that define the transition from Stage I to Stage II melanosomes. This protein undergoes a complex pattern of prosttranslational processing and modification that is essential to …

**Accessions** — [HGNC:10880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10880) · Entrez [6490](https://www.ncbi.nlm.nih.gov/gene/6490) · UniProt [P40967](https://www.uniprot.org/uniprotkb/P40967) · Ensembl [ENSG00000185664](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185664)

## Data

Gene col 11713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11713); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11713]; `tensor/DDL_lfc|DDL_z.npy` [11713]; `embed/gene_vectors.npy` [11713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11713 or target_col == 11713). Every well: [[PMEL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMEL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

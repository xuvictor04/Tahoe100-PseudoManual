---
symbol: "PPFIA2"
type: "gene"
col: 6282
ensembl_id: "ENSG00000139220"
name: "PPFI scaffold protein A2"
location: "12q21.31"
module: 150
arm: "+"
pooled_cpm: 5.33
n_lines_expressing: 30
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# PPFIA2

*PPFI scaffold protein A2* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.38× (z +23.6, q 0e+00, up in 15 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.182×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.189×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.234×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL25A1]] (+0.73, fdr 7e-06), [[ADGRL3]] (+0.64, fdr 1e-05), [[GRID2]] (+0.64, fdr 7e-06); moves opposite to [[DZANK1]] (-0.49, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SAMSN1]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC02268]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.38×** | +23.6 | 0e+00 | 15/17 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.83×** | +18.8 | 0e+00 | 19/25 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.59×** | +12.2 | 5e-32 | 2/6 (HOP62, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +11.4 | 4e-28 | 12/19 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +11.4 | 5e-28 | 6/11 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.95×** | +10.8 | 5e-25 | 18/22 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.89×** | +10.6 | 4e-24 | 13/23 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.57×** | +9.4 | 5e-19 | 9/21 (A498, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +8.9 | 5e-17 | 8/15 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +8.4 | 4e-15 | 10/20 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +7.4 | 8e-12 | 2/7 (HOP62, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.07×** | +7.2 | 2e-11 | 12/25 (NCI-H1792, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.1 | 4e-08 | 8/25 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +6.0 | 1e-07 | 10/19 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.75×** | +5.2 | 6e-06 | 10/21 (HOP62, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +5.0 | 2e-05 | 9/25 (NCI-H23, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +4.8 | 4e-05 | 7/24 (LOX-IMVI, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.010 | 8/25 (NCI-H23, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6282.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.182×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.189×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.234×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | 0.715× | -3.1 | 0.92 | 3/15 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 64.2 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 49.8 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.91× (z +15.8) | [[Digitoxin (drug)]] 5 µM 0.293× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 6.25 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.05× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.01× (z +12.2) | — |
| [[A-172 (line)]] | wt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 1.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.1× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 2.18 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.8× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 2.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.64× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 1.69 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 21.9× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.215× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.870 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.980 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL25A1]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[ADGRL3]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[GRID2]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[TMEFF2]] | +0.63 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[LINC00607]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SVEP1]] | +0.62 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[SPOCK3]] | +0.61 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[MYO3B]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PTPRO]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[PRDM6]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[GRIA4]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 | pathway: Neuronal System |
| [[CNBD1]] | +0.59 | +0.41 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZANK1]] | -0.49 | -0.17 / -0.46 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMSN1]] | B | SAMSN1 activity lowers PPFIA2's level | lines that do not express SAMSN1 (6) vs lines expressing it (44) | 2.76× higher at baseline in the lines without SAMSN1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SYTL2, GNA14, ENSG00000235609; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PPFIA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ERBB4]] | C | ERBB4 activity raises PPFIA2's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 2.87× lower at baseline in the lines without ERBB4 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[PRKG1]] | C | PRKG1 activity raises PPFIA2's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without PRKG1 | 0.054 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02268]] | B | PPFIA2 activity raises LINC02268's level | lines that do not express PPFIA2 (20) vs lines expressing it (30) | 1.70× lower at baseline in the lines without PPFIA2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CASC20, ENSG00000285330, GHR; maybe low, not absent |
| [[LINC01266]] | B | PPFIA2 activity lowers LINC01266's level | lines that do not express PPFIA2 (20) vs lines expressing it (30) | 1.26× higher at baseline in the lines without PPFIA2 | 0.093 | ⚠ within organs, on part of the lines; also absent: CASC20, ENSG00000285330, GHR; maybe low, not absent |
| [[PRKG1]] | C | PPFIA2 activity raises PRKG1's level | lines that do not express PPFIA2 (20) vs lines expressing it (30) | 3.34× lower at baseline in the lines without PPFIA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: CASC20, ENSG00000285330, GHR; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.1, 29.0); signed map (33.9, 17.2). **Vector** length 44.7, 8.04% of its response variance represented; |z| ≥ 3 in 650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +18.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +23.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | -1.2 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -0.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | PPFI scaffold protein A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:81,257,975-81,759,553 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sterile alpha motif domain containing; PPFI scaffold protein family |
| Reactome | 10 pathways, smallest: Acetylcholine Neurotransmitter Release Cycle; Norepinephrine Neurotransmitter Release Cycle; Receptor-type tyrosine-protein phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [O75334](https://www.uniprot.org/uniprotkb/O75334) (Liprin-alpha-2):

> Alters PTPRF cellular localization and induces PTPRF clustering. May regulate the disassembly of focal adhesions. May localize receptor-like tyrosine phosphatases type 2A at specific sites on the plasma membrane, possibly regulating their interaction with the extracellular environment and their association with substrates. In neuronal cells, is a scaffolding protein in the dendritic spines which acts as immobile postsynaptic post able to recruit KIF1A-driven dense core vesicles to dendritic …

**Summary**, from NCBI Gene [8499](https://www.ncbi.nlm.nih.gov/gene/8499):

> The protein encoded by this gene is a member of the LAR protein-tyrosine phosphatase-interacting protein (liprin) family. Liprins interact with members of LAR family of transmembrane protein tyrosine phosphatases, which are known to be important for axon guidance and mammary gland development. It has been proposed that liprins are multivalent proteins that form complex structures and act as scaffolds for the recruitment and anchoring of LAR family of tyrosine phosphatases. This protein has been …

**Accessions** — [HGNC:9246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9246) · Entrez [8499](https://www.ncbi.nlm.nih.gov/gene/8499) · UniProt [O75334](https://www.uniprot.org/uniprotkb/O75334) · Ensembl [ENSG00000139220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139220)

## Data

Gene col 6282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6282); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6282]; `tensor/DDL_lfc|DDL_z.npy` [6282]; `embed/gene_vectors.npy` [6282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6282 or target_col == 6282). Every well: [[PPFIA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPFIA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

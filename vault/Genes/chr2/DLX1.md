---
symbol: "DLX1"
type: "gene"
col: 6868
ensembl_id: "ENSG00000144355"
name: "distal-less homeobox 1"
location: "2q31.1"
module: 7
arm: "+"
pooled_cpm: 2.07
n_lines_expressing: 37
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 20
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DLX1

*distal-less homeobox 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.83× (z +16.7, q 0e+00, up in 17 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0610×; ⚠ cell-cycle shift, explains ~0% of this change); [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.0630×; ⚠ toxic).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIX1]] (+0.55, fdr 3e-05), [[BCL2]] (+0.51, fdr 3e-05), [[HHEX]] (+0.50, fdr 3e-05); moves opposite to [[SEPTIN2]] (-0.48, fdr 4e-05), [[MAP3K13]] (-0.46, fdr 2e-04), [[SPAG9]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SERTAD4]] → it (grade B ⚠); 20 go from it, the strongest it → [[GBX2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.83×** | +16.7 | 0e+00 | 17/20 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.49×** | +7.6 | 7e-12 | 0/3 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +7.0 | 6e-10 | 5/11 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.94×** | +5.4 | 1e-05 | 0/3 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.020 | 7/32 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.024 | 4/32 (PANC-1, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.090 | 6/17 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.46× | +3.1 | 0.12 | 5/19 (A-172, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.41× | +3.0 | 0.15 | 1/10 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6868.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0610×; ⚠ cell-cycle shift, explains ~0% of this change); [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.0630×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.711× | -3.0 | 0.62 | 12/33 (LOX-IMVI, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0610× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 47.8 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0630× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +9.4) | — |
| [[A-172 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.721 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.187 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.651 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.544 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.181 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.761 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.887 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIX1]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[BCL2]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[HHEX]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[GBX2-AS1]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[DBR1]] | +0.49 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[TOE1]] | +0.49 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[ZNF618]] | +0.48 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[CCNJ]] | +0.48 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[KLHL42]] | +0.48 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[TLR4]] | +0.48 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[TBX2]] | +0.47 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[PITX1]] | +0.47 | +0.36 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN2]] | -0.48 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[MAP3K13]] | -0.46 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[SPAG9]] | -0.45 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[HEMK1]] | -0.45 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[XRRA1]] | -0.45 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[MAGT1]] | -0.44 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[ARL8B]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PLD3]] | -0.43 | -0.52 / -0.21 | both halves | 7e-04 |  |
| [[PPP1R21]] | -0.42 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[RHOA]] | -0.42 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[MALAT1]] | -0.40 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[NBEAL1]] | -0.40 | -0.45 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERTAD4]] | B | SERTAD4 activity lowers DLX1's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.51× higher at baseline in the lines without SERTAD4 | 0.009 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[GALNT14]] | B | GALNT14 activity lowers DLX1's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.95× higher at baseline in the lines without GALNT14 | 0.021 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[GJB2]] | B | GJB2 activity lowers DLX1's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.80× higher at baseline in the lines without GJB2 | 0.055 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[SH3RF1]] | C | SH3RF1 activity lowers DLX1's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 3.28× higher at baseline in the lines without SH3RF1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 18, C 2. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBX2-AS1]] | B | DLX1 activity raises GBX2-AS1's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without DLX1 | 0.012 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[SH3RF1]] | B | DLX1 activity lowers SH3RF1's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 2.15× higher at baseline in the lines without DLX1 | 0.036 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[ADCY3]] | B | DLX1 activity raises ADCY3's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without DLX1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[ADO]] | B | DLX1 activity raises ADO's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.11× lower at baseline in the lines without DLX1 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| cells under [[Trifluridine (drug)]] 5 µM | B | DLX1 activity lowers the cells' numbers under Trifluridine 5 µM (makes them more sensitive) | lines that do not express DLX1 (13) vs lines expressing it (35) | the lines without DLX1: 1.14× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[ZNF689]] | B | DLX1 activity raises ZNF689's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.28× lower at baseline in the lines without DLX1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[MAP3K13]] | B | DLX1 activity lowers MAP3K13's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.63× higher at baseline in the lines without DLX1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[KLHL42]] | B | DLX1 activity raises KLHL42's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without DLX1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[FJX1]] | B | DLX1 activity raises FJX1's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without DLX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[ARHGAP31]] | B | DLX1 activity raises ARHGAP31's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 2.72× lower at baseline in the lines without DLX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | DLX1 activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express DLX1 (13) vs lines expressing it (35) | the lines without DLX1: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[MSH6]] | B | DLX1 activity raises MSH6's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without DLX1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.299). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (22.0, -10.3); signed map (17.4, -11.2). **Vector** length 33.5, 3.95% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +16.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.6 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.6 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | distal-less homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:172,084,740-172,089,677 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Distal-less homeobox family |
| Matched by | ensembl_id |

**Function**, from UniProt [P56177](https://www.uniprot.org/uniprotkb/P56177) (Homeobox protein DLX-1):

> Plays a role as a transcriptional activator or repressor. Inhibits several cytokine signaling pathways, such as TGFB1, activin-A/INHBA and BMP4 by interfering with the transcriptional stimulatory activity of transcription factors, such as MSX2, FAST2, SMAD2 and SMAD3 during hematopoietic cell differentiation. Plays a role in terminal differentiation of interneurons, such as amacrine and bipolar cells in the developing retina (By similarity). Likely to play a regulatory role in the development …

**Summary**, from NCBI Gene [1745](https://www.ncbi.nlm.nih.gov/gene/1745):

> This gene encodes a member of a homeobox transcription factor gene family similiar to the Drosophila distal-less gene. The encoded protein is localized to the nucleus where it may function as a transcriptional regulator of signals from multiple TGF-{beta} superfamily members. The encoded protein may play a role in the control of craniofacial patterning and the differentiation and survival of inhibitory neurons in the forebrain. This gene is located in a tail-to-tail configuration with another …

**Accessions** — [HGNC:2914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2914) · Entrez [1745](https://www.ncbi.nlm.nih.gov/gene/1745) · UniProt [P56177](https://www.uniprot.org/uniprotkb/P56177) · Ensembl [ENSG00000144355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144355)

## Data

Gene col 6868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6868); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6868]; `tensor/DDL_lfc|DDL_z.npy` [6868]; `embed/gene_vectors.npy` [6868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6868 or target_col == 6868). Every well: [[DLX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

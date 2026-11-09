---
symbol: "PART1"
type: "gene"
col: 7667
ensembl_id: "ENSG00000152931"
name: "prostate androgen-regulated transcript 1"
location: "5q12.1"
module: 19
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PART1

*prostate androgen-regulated transcript 1* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.82× (z +10.3, q 4e-22, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.92× (z +9.9, q 1e-20, up in 13 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.839× (z -4.1, q 0.029, down in 19 of 44 measured lines) ⚠ position not correctable. The strongest without an alert is [[Decitabine (drug)]] 5 µM: 0.563× (z -3.6, q 0.086, down in 3 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0959×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.204×; ⚠ cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.122×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AQP4-AS1]] (+0.79, fdr 7e-06), [[C3orf49]] (+0.77, fdr 7e-06), [[LINC02755]] (+0.71, fdr 7e-06); moves opposite to [[TTLL12]] (-0.52, fdr 3e-05), [[JPT2]] (-0.51, fdr 8e-05), [[PSMG1]] (-0.51, fdr 8e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PRSS23-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +10.3 | 4e-22 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +9.9 | 1e-20 | 13/17 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **4.27×** | +9.5 | 4e-19 | 13/21 (C32, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.39×** | +9.3 | 2e-18 | 1/1 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.91×** | +8.3 | 2e-14 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.31×** | +7.8 | 8e-13 | 9/22 (LoVo, C32, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.11×** | +7.4 | 9e-12 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +5.9 | 3e-07 | 3/4 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.45×** | +4.2 | 0.002 | 1/1 (NCI-H460) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.87×** | +4.1 | 0.002 | 3/17 (Hs 766T, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.004 | 1/9 (NCI-H460) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.18×** | +3.6 | 0.013 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.014 | 0/40 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.5 | 0.022 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.3 | 0.033 | 1/3 (SW480) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.3 | 0.033 | 1/19 (SW480) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.043 | 1/9 (SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7667.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.0959×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.204×; ⚠ cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.122×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.839× | -4.1 | 0.029 | 19/44 (LoVo, HepG2/C3A, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 5 µM |  | **0.563×** | -3.6 | 0.086 | 3/18 (PANC-1, HOP62, …) | top dose only | position effect removed |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.609× | -3.2 | 0.22 | 7/40 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.605× | -3.0 | 0.34 | 6/37 (NCI-H23, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.5 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0959× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 0.780 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.586 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.880 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.932 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.653 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.712 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.669 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.804 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.706 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.857 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.930 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.775 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.907 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.660 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.851 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.707 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.834 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.972 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.720 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.746 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.993 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.846 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AQP4-AS1]] | +0.79 | +0.70 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[C3orf49]] | +0.77 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[LINC02755]] | +0.71 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[ANO3]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[PCDH15]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SPDYE10]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[LINC01257]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[IQCM]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[IGF2BP2-AS1]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PLAC4]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL12]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[JPT2]] | -0.51 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[PSMG1]] | -0.51 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[MAPKAPK3]] | -0.51 | -0.54 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PART1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC03000]] | B | LINC03000 activity raises PART1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.30× lower at baseline in the lines without LINC03000 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4 |
| [[SCARA5]] | B | SCARA5 activity raises PART1's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 1.99× lower at baseline in the lines without SCARA5 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[CTNND2]] | B | CTNND2 activity raises PART1's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.68× lower at baseline in the lines without CTNND2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[CHL1]] | B | CHL1 activity raises PART1's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 1.86× lower at baseline in the lines without CHL1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[SLC15A5]] | B | SLC15A5 activity raises PART1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.19× lower at baseline in the lines without SLC15A5 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |
| [[DPP10]] | B | DPP10 activity raises PART1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 1.75× lower at baseline in the lines without DPP10 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[SERPINB11]] | B | SERPINB11 activity raises PART1's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 1.85× lower at baseline in the lines without SERPINB11 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX |
| [[TBXT]] | C | TBXT activity raises PART1's level | lines that do not express TBXT (47) vs lines expressing it (3) | 3.85× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23-AS1]] | C | PART1's natural level weakens PRSS23-AS1's drug response | PART1's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.34; direction clear | 0.082 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.4, 25.8); signed map (32.3, 8.3). **Vector** length 30.3, 3.40% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +1.9 | +7.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.2 | +8.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +3.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -3.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.8 | -1.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | prostate androgen-regulated transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q12.1 — chr5:60,487,713-60,548,813 (+) |
| Ensembl biotype | lncRNA |
| Also known as | DKFZP586D0823, NCRNA00206 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [25859](https://www.ncbi.nlm.nih.gov/gene/25859):

> This gene is induced by androgen in prostate adenocarcinoma cells. Multiple alternatively transcript variants have been described for this gene, none of which are predicted to encode a protein product. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:17263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17263) · Entrez [25859](https://www.ncbi.nlm.nih.gov/gene/25859) · Ensembl [ENSG00000152931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152931)

## Data

Gene col 7667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7667); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7667]; `tensor/DDL_lfc|DDL_z.npy` [7667]; `embed/gene_vectors.npy` [7667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7667 or target_col == 7667). Every well: [[PART1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PART1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

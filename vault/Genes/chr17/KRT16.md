---
symbol: "KRT16"
type: "gene"
col: 11859
ensembl_id: "ENSG00000186832"
name: "keratin 16"
location: "17q21.2"
module: 31
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 23
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 20
direction_downstream: 41
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# KRT16

*keratin 16* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 5 µM: 43.2× (z +9.4, q 3e-18, up in 7 of 7 measured lines) ⚠ toxic. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 5.66× (z +7.8, q 1e-12, up in 14 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.0528×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0380×; ⚠ cell-cycle shift, explains ~50% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT14]] (+0.76, fdr 7e-06, ⚠ same locus), [[KRT6A]] (+0.70, fdr 7e-06), [[LINC01564]] (+0.61, fdr 7e-06), [[SEMA3B]] (+0.57, fdr 1e-05); moves opposite to [[ZBTB44]] (-0.45, fdr 2e-04), [[CEP43]] (-0.45, fdr 5e-05), [[LRRC37A4P]] (-0.44, fdr 7e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[S100A14]] → it (grade C ⚠); 41 go from it, the strongest it → [[ALS2CL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **43.2×** | +9.4 | 3e-18 | 7/7 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **5.66×** | +7.8 | 1e-12 | 14/15 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.89×** | +7.6 | 6e-12 | 15/18 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.10×** | +6.5 | 1e-08 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.25×** | +6.4 | 2e-08 | 2/4 (Panc 03.27, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.69×** | +6.2 | 4e-08 | 3/7 (Panc 03.27, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.04×** | +5.2 | 1e-05 | 12/16 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.13×** | +5.2 | 1e-05 | 6/11 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.13×** | +5.1 | 2e-05 | 8/18 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **5.09×** | +4.9 | 6e-05 | 10/17 (SW480, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.65×** | +4.6 | 2e-04 | 1/8 (Panc 03.27) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.60×** | +4.6 | 2e-04 | 1/11 (Hs 766T) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.40×** | +4.2 | 0.001 | 5/16 (KATO III, SW480, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.38×** | +4.1 | 0.002 | 2/11 (NCI-H2347, LoVo) | inconsistent across doses | low cells (technical?); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.83×** | +4.0 | 0.002 | 1/5 (A-172) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +3.6 | 0.009 | 1/15 (SW1417) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Bendamustine (drug)]] 5 µM |  | **1.95×** | +3.0 | 0.070 | 2/11 (SW480, LoVo) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.86×** | +3.0 | 0.085 | 2/14 (Hs 766T, Panc 03.27) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11859.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.0528×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0380×; ⚠ cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | 0.484× | -3.5 | 0.16 | 13/19 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.461× | -3.5 | 0.16 | 1/18 (HS-578T) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | 0.273× | -3.3 | 0.21 | 4/17 (CFPAC-1, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 22.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 13.5× (z +9.9) | — |
| [[LoVo (line)]] | wt | 5.27 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0380× (z -8.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 3.39 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0528× (z -9.4) |
| [[SW480 (line)]] | alt | 1.07 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 181× (z +9.4) | — |
| [[A-172 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.121 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.165 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.160 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.130 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.185 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.225 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.142 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.169 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.147 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.120 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.164 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT14]] | +0.76 | +0.77 / +0.59 | both halves | 7e-06 | same gene group; pathway: Formation of the cornified envelope; STRING 868; ⚠ same locus (22.9 kb, same strand: neighbours can correlate without regulation) |
| [[KRT6A]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | pathway: Formation of the cornified envelope; STRING 928 |
| [[LINC01564]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SEMA3B]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[SFN]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 | STRING 421 |
| [[CRYBG2]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[CYP4F11]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ADCY7]] | +0.54 | +0.58 / +0.40 | both halves | 4e-05 |  |
| [[KRT17]] | +0.54 | +0.51 / +0.58 | both halves | 1e-05 | same gene group; pathway: Formation of the cornified envelope; STRING 880; ⚠ **readthrough risk**: this gene lies 3.5 kb 3′ of KRT17 on the same strand (can correlate by spillover, not regulation) |
| [[S100P]] | +0.53 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[DSG3]] | +0.53 | +0.56 / +0.46 | both halves | 3e-05 | pathway: Formation of the cornified envelope; STRING 570 |
| [[NCF2]] | +0.51 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[ALS2CL]] | +0.50 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SDCBP2]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB44]] | -0.45 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[CEP43]] | -0.45 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[LRRC37A4P]] | -0.44 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[PCM1]] | -0.42 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[PHF7]] | -0.41 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[SETDB2]] | -0.40 | -0.31 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 0, C 20. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A14]] | C | S100A14 activity raises KRT16's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without S100A14 | 0.001 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises KRT16's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without TRIM29 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises KRT16's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.18× lower at baseline in the lines without SERPINB5 | 0.004 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[GJB3]] | C | GJB3 activity raises KRT16's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.75× lower at baseline in the lines without GJB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10; co-absent with the target |
| [[SCEL]] | C | SCEL activity raises KRT16's level | lines that do not express SCEL (35) vs lines expressing it (15) | 2.82× lower at baseline in the lines without SCEL | 0.005 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1; co-absent with the target |
| [[TTC22]] | C | TTC22 activity raises KRT16's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.83× lower at baseline in the lines without TTC22 | 0.007 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; co-absent with the target |
| [[KRT6A]] | C | KRT6A activity raises KRT16's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 3.90× lower at baseline in the lines without KRT6A | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[SGPP2]] | C | SGPP2 activity raises KRT16's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.58× lower at baseline in the lines without SGPP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4; co-absent with the target |
| [[CYP4F3]] | C | CYP4F3 activity raises KRT16's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.45× lower at baseline in the lines without CYP4F3 | 0.011 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6; co-absent with the target |
| [[FAM83B]] | C | FAM83B activity raises KRT16's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 2.30× lower at baseline in the lines without FAM83B | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[KRT14]] | C | KRT14 activity raises KRT16's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 3.71× lower at baseline in the lines without KRT14 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[ANO1]] | C | ANO1 activity raises KRT16's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.42× lower at baseline in the lines without ANO1 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2; co-absent with the target |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 22, C 19. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALS2CL]] | B | KRT16 activity raises ALS2CL's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 3.27× lower at baseline in the lines without KRT16 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[LSMEM2]] | B | KRT16 activity raises LSMEM2's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without KRT16 | 0.004 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[PKP3]] | B | KRT16 activity raises PKP3's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.51× lower at baseline in the lines without KRT16 | 0.007 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[SFN]] | B | KRT16 activity raises SFN's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 3.07× lower at baseline in the lines without KRT16 | 0.008 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[UNC13D]] | B | KRT16 activity raises UNC13D's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.36× lower at baseline in the lines without KRT16 | 0.009 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[LINC00592]] | B | KRT16 activity raises LINC00592's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without KRT16 | 0.010 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[EPS8L1]] | B | KRT16 activity raises EPS8L1's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 3.05× lower at baseline in the lines without KRT16 | 0.011 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[CRYBG2]] | B | KRT16 activity raises CRYBG2's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.69× lower at baseline in the lines without KRT16 | 0.016 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[NCF2]] | B | KRT16 activity raises NCF2's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 1.85× lower at baseline in the lines without KRT16 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[HSPA1B]] | B | KRT16 activity raises HSPA1B's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 1.43× lower at baseline in the lines without KRT16 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[DENND2C]] | B | KRT16 activity raises DENND2C's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 1.60× lower at baseline in the lines without KRT16 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[FBXW10B]] | B | KRT16 activity raises FBXW10B's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without KRT16 | 0.024 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.4, 51.2); signed map (3.6, 36.3). **Vector** length 49.0, 13.2% of its response variance represented; |z| ≥ 3 in 496 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +1.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.1 | +1.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | keratin 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,609,778-41,615,899 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NEPPK |
| Gene groups (HGNC) | Keratins, type I |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P08779](https://www.uniprot.org/uniprotkb/P08779) (Keratin, type I cytoskeletal 16):

> Structural component of intermediate filaments in epithelial keratinocytes. Forms heteropolymers with type II keratins KRT6A and KRT6B, assembling into keratin intermediate filament networks that contribute to cytoskeletal resilience of palm, sole, nail bed and oral mucosa. Regulates epidermal innate immunity and inflammatory signaling in response to barrier disruption. Required for normal palmoplantar epidermal differentiation and nail unit structure (By similarity).

**Summary**, from NCBI Gene [3868](https://www.ncbi.nlm.nih.gov/gene/3868):

> The protein encoded by this gene is a member of the keratin gene family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. Most of the type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains and are clustered in a region of chromosome 17q12-q21. This keratin has been coexpressed with keratin 14 in a number of epithelial tissues, …

**Accessions** — [HGNC:6423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6423) · Entrez [3868](https://www.ncbi.nlm.nih.gov/gene/3868) · UniProt [P08779](https://www.uniprot.org/uniprotkb/P08779) · Ensembl [ENSG00000186832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186832)

## Data

Gene col 11859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11859); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11859]; `tensor/DDL_lfc|DDL_z.npy` [11859]; `embed/gene_vectors.npy` [11859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11859 or target_col == 11859). Every well: [[KRT16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

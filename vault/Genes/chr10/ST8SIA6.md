---
symbol: "ST8SIA6"
type: "gene"
col: 7291
ensembl_id: "ENSG00000148488"
name: "ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 6"
location: "10p12.33"
module: 8
arm: "+"
pooled_cpm: 13.49
n_lines_expressing: 19
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 37
direction_downstream: 24
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ST8SIA6

*ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 6* — 10p12.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.22× (z +18.3, q 0e+00, up in 7 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Mebendazole (drug)]] 5 µM: 0.664× (z -4.4, q 0.006, down in 5 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (CFPAC-1 0.0618×, Panc 03.27 0.113×, BT-474 0.235×, PANC-1 0.209×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (CFPAC-1 0.0760×, LoVo 0.0977×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0898×, Panc 03.27 0.0383×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.228×, LoVo 0.263×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPERB]] (+0.66, fdr 7e-06), [[PROM2]] (+0.65, fdr 1e-05), [[TMPRSS4]] (+0.64, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 24 go from it, the strongest it → [[CARD14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.22×** | +18.3 | 0e+00 | 7/15 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.26×** | +13.1 | 1e-36 | 3/11 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +11.7 | 3e-29 | 2/6 (HT-29, Panc 03.27) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +11.1 | 3e-26 | 1/9 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +7.4 | 2e-11 | 6/17 (A-427, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +6.1 | 1e-07 | 6/17 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.8 | 5e-07 | 2/13 (NCI-H460, PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +5.2 | 1e-05 | 1/15 (HCT15) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.0 | 4e-05 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.9 | 6e-05 | 1/17 (PANC-1) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.2 | 0.001 | 3/16 (SW1417, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.007 | 3/17 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.030 | 2/16 (SK-MEL-2, COLO 205) | all doses, flat | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.038 | 4/17 (NCI-H460, HT-29, …) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.086 | 4/17 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.087 | 1/16 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7291.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (CFPAC-1 0.0618×, Panc 03.27 0.113×, BT-474 0.235×, PANC-1 0.209×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (CFPAC-1 0.0760×, LoVo 0.0977×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0898×, Panc 03.27 0.0383×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.228×, LoVo 0.263×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | **0.664×** | -4.4 | 0.006 | 5/17 (CFPAC-1, Hs 766T, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -3.8 | 0.047 | 8/17 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.746× | -3.3 | 0.13 | 8/17 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.748× | -3.3 | 0.13 | 2/17 (BT-474, SW1417) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.736× | -3.2 | 0.13 | 3/17 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.766× | -3.0 | 0.25 | 2/17 (HCT15, PANC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 255 | 0 | 24 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0618× (z -28.6) |
| [[LoVo (line)]] | wt | 47.2 | 0 | 14 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0746× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 29.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0383× (z -17.2) |
| [[BT-474 (line)]] | alt | 97.4 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0761× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.6) |
| [[PANC-1 (line)]] | alt | 7.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.6) |
| [[A-172 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.72 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERB]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PROM2]] | +0.65 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TMPRSS4]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ITGB6]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TSPAN1]] | +0.62 | +0.69 / +0.36 | both halves | 9e-05 |  |
| [[TC2N]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[ARHGAP30]] | +0.62 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[TMEM45B]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CDH3]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SIDT1]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SLC44A4]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MUC16]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 3, C 34. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ST8SIA6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BICDL2]] | B | BICDL2 activity raises ST8SIA6's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without BICDL2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[DAPK1]] | B | DAPK1 activity raises ST8SIA6's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.47× lower at baseline in the lines without DAPK1 | 0.084 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[SIDT1]] | C | SIDT1 activity raises ST8SIA6's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without SIDT1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2; co-absent with the target |
| [[GPR141]] | C | GPR141 activity raises ST8SIA6's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 2.37× lower at baseline in the lines without GPR141 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |
| [[MUC16]] | C | MUC16 activity raises ST8SIA6's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 3.16× lower at baseline in the lines without MUC16 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; co-absent with the target |
| [[GSDMC]] | C | GSDMC activity raises ST8SIA6's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 5.38× lower at baseline in the lines without GSDMC | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises ST8SIA6's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without TMEM125 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[AGR2]] | C | AGR2 activity raises ST8SIA6's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 2.87× lower at baseline in the lines without AGR2 | 0.030 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1; co-absent with the target |
| [[SERPINB3]] | C | SERPINB3 activity raises ST8SIA6's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.89× lower at baseline in the lines without SERPINB3 | 0.032 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[GABRP]] | C | GABRP activity raises ST8SIA6's level | lines that do not express GABRP (44) vs lines expressing it (6) | 3.83× lower at baseline in the lines without GABRP | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[BARX2]] | C | BARX2 activity raises ST8SIA6's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without BARX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 8, C 16. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD14]] | B | ST8SIA6 activity raises CARD14's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 1.89× lower at baseline in the lines without ST8SIA6 | 0.009 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2 |
| [[CARD14]] | B | ST8SIA6 activity strengthens CARD14's drug response | lines that do not express ST8SIA6 (28) vs lines expressing it (17) | the lines without ST8SIA6 respond 0.53× as strongly (z diff +0.73); rises at some drug-doses, falls at others (63% from rises): Dinaciclib 0.05 µM: 0.33x vs 0.92x (z diff +2.8); Ouabain (Octahydrate) 5 µM: 0.83x vs 0.35x (z diff +2.7); Tucidinostat 5 µM: 1.24x vs 1.85x (z diff +2.3) | 0.014 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[KLHL2P1]] | B | ST8SIA6 activity raises KLHL2P1's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 1.64× lower at baseline in the lines without ST8SIA6 | 0.036 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2 |
| [[FAM83E]] | B | ST8SIA6 activity raises FAM83E's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 2.61× lower at baseline in the lines without ST8SIA6 | 0.042 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2 |
| [[BICDL2]] | B | ST8SIA6 activity raises BICDL2's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 2.72× lower at baseline in the lines without ST8SIA6 | 0.042 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2 |
| [[PRRG2]] | B | ST8SIA6 activity raises PRRG2's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 2.09× lower at baseline in the lines without ST8SIA6 | 0.048 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2 |
| [[PROM2]] | B | ST8SIA6 activity raises PROM2's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 2.22× lower at baseline in the lines without ST8SIA6 | 0.085 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2 |
| [[IQANK1]] | B | ST8SIA6 activity raises IQANK1's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 2.90× lower at baseline in the lines without ST8SIA6 | 0.093 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2 |
| [[PRR15-DT]] | C | ST8SIA6 activity raises PRR15-DT's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 3.06× lower at baseline in the lines without ST8SIA6 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2; co-absent with the target |
| [[PRR15]] | C | ST8SIA6 activity raises PRR15's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 2.73× lower at baseline in the lines without ST8SIA6 | 0.010 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2; co-absent with the target |
| [[ARHGAP30]] | C | ST8SIA6 activity raises ARHGAP30's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 3.15× lower at baseline in the lines without ST8SIA6 | 0.019 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2; co-absent with the target |
| [[CRACDL]] | C | ST8SIA6 activity raises CRACDL's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without ST8SIA6 | 0.019 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 56.0); signed map (59.3, 6.9). **Vector** length 53.8, 15.1% of its response variance represented; |z| ≥ 3 in 473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +13.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +4.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -3.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.3 | -1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.33 — chr10:17,315,421-17,454,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SIAT8F |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 7 pathways, smallest: N-Glycan antennae elongation; N-glycan antennae elongation in the medial/trans-Golgi; Sialic acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P61647](https://www.uniprot.org/uniprotkb/P61647) (Alpha-2,8-sialyltransferase 8F):

> Alpha-2,8-sialyltransferase that prefers O-glycans to N-glycans or glycolipids as acceptor substrates. The minimal acceptor substrate is the NeuAc-alpha-2,3(6)-Gal sequence at the non-reducing end of their carbohydrate groups.

**Summary**, from NCBI Gene [338596](https://www.ncbi.nlm.nih.gov/gene/338596):

> This gene encodes a member of the glycosyltransferase 29 protein family. Members of this protein family synthesize sialylglycoconjugates. Sialylation may contribute to multidrug resistance in cancer cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:23317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23317) · Entrez [338596](https://www.ncbi.nlm.nih.gov/gene/338596) · UniProt [P61647](https://www.uniprot.org/uniprotkb/P61647) · Ensembl [ENSG00000148488](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148488)

## Data

Gene col 7291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7291); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7291]; `tensor/DDL_lfc|DDL_z.npy` [7291]; `embed/gene_vectors.npy` [7291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7291 or target_col == 7291). Every well: [[ST8SIA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST8SIA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

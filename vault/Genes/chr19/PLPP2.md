---
symbol: "PLPP2"
type: "gene"
col: 6581
ensembl_id: "ENSG00000141934"
name: "phospholipid phosphatase 2"
location: "19p13.3"
module: 170
arm: "-"
pooled_cpm: 7.88
n_lines_expressing: 42
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# PLPP2

*phospholipid phosphatase 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.94× (z +13.4, q 3e-38, up in 26 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bendamustine (drug)]] 5 µM: 1.43× (z +4.3, q 0.002, up in 8 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.458× (z -9.4, q 3e-18, down in 30 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLXND1]] (+0.57, fdr 3e-05), [[CTDSPL]] (+0.52, fdr 1e-04), [[MEST]] (+0.52, fdr 6e-05); moves opposite to [[ZNF397]] (-0.57, fdr 1e-04), [[ZNF7]] (-0.56, fdr 4e-05), [[DDX50]] (-0.54, fdr 5e-05).
> It sits in the **-** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[XK]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6581.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +13.4 | 3e-38 | 26/27 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +13.2 | 4e-37 | 14/15 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +9.3 | 3e-18 | 19/19 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +7.1 | 2e-10 | 19/31 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.49×** | +4.9 | 9e-05 | 12/31 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.43×** | +4.3 | 0.002 | 8/37 (A498, NCI-H1792, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.030 | 10/38 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.030 | 8/38 (LoVo, HT-29, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.5 | 0.034 | 11/36 (A-172, SW48, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.038 | 9/38 (HCT15, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.044 | 6/36 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.095 | 6/38 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.1 | 0.095 | 9/39 (SHP-77, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, none with an alert; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -9.4 | 3e-18 | 30/39 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -8.9 | 2e-16 | 24/35 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -7.6 | 4e-12 | 23/36 (Panc 03.27, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.585×** | -6.7 | 3e-09 | 20/36 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.606×** | -6.3 | 3e-08 | 26/39 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.640×** | -5.6 | 2e-06 | 20/39 (AsPC-1, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.648×** | -5.5 | 4e-06 | 18/39 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.676×** | -4.9 | 6e-05 | 19/39 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -4.8 | 8e-05 | 15/35 (SW 900, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.497×** | -4.6 | 3e-04 | 13/37 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.717×** | -4.0 | 0.003 | 17/37 (LoVo, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -3.8 | 0.007 | 11/36 (LS 180, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.742×** | -3.8 | 0.007 | 10/39 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ciclopirox (drug)]] 5 µM |  | **0.822×** | -3.5 | 0.018 | 14/38 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.605×** | -3.3 | 0.037 | 4/36 (LoVo, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -15.7) |
| [[LS 180 (line)]] | wt | 18.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.8) |
| [[SW480 (line)]] | alt | 7.13 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.7) |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 7.13 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +9.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 7.39 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -8.5) |
| [[SNU-423 (line)]] | alt | 3.40 | 0 | 1 | — | [[Rifaximin (drug)]] 0.5 µM 0.0667× (z -8.7) |
| [[SW 900 (line)]] | alt | 4.72 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0706× (z -9.1) |
| [[A-172 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.956 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXND1]] | +0.57 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[CTDSPL]] | +0.52 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[MEST]] | +0.52 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[PRXL2A]] | +0.52 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[CTSH]] | +0.51 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[COBL]] | +0.51 | +0.51 / +0.32 | both halves | 2e-04 |  |
| [[BAIAP2-DT]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TMEM97]] | +0.50 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CPT1A]] | +0.50 | +0.35 / +0.38 | both halves | 1e-04 |  |
| [[DHX15]] | +0.50 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[PODXL2]] | +0.50 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[TBL1XR1]] | +0.49 | +0.40 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF397]] | -0.57 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[ZNF7]] | -0.56 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[DDX50]] | -0.54 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[GOLGA1]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CCDC22]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.52 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[NDUFAF1]] | -0.52 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[HMGCL]] | -0.52 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[FAM149B1]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ZSWIM3]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[TAF12]] | -0.51 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[TJAP1]] | -0.51 | -0.51 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XK]] | B | XK activity raises PLPP2's level | lines that do not express XK (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without XK | 0.013 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[ZNF563]] | B | ZNF563 activity lowers PLPP2's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 1.60× higher at baseline in the lines without ZNF563 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |
| [[SYTL4]] | B | SYTL4 activity raises PLPP2's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without SYTL4 | 0.083 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[COBL]] | B | COBL activity raises PLPP2's level | lines that do not express COBL (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without COBL | 0.094 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF7]] | B | PLPP2 activity raises ZNF7's level | lines that do not express PLPP2 (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without PLPP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: MAP3K21, C3orf52, REPS2 |
| [[RECQL5]] | B | PLPP2 activity raises RECQL5's level | lines that do not express PLPP2 (8) vs lines expressing it (42) | 1.16× lower at baseline in the lines without PLPP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MAP3K21, C3orf52, REPS2 |

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-26.0, 17.9); signed map (15.1, -51.9). **Vector** length 55.3, 9.13% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +13.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.7 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | -2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.7 | -4.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid phosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:281,040-291,403 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAP-2c, LPP2; previously PPAP2C |
| Gene groups (HGNC) | Phospholipid phosphatases |
| Reactome | 3 pathways, smallest: Sphingolipid catabolism; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O43688](https://www.uniprot.org/uniprotkb/O43688) (Phospholipid phosphatase 2):

> Magnesium-independent phospholipid phosphatase that catalyzes the dephosphorylation of a variety of glycerolipid and sphingolipid phosphate esters including phosphatidate/PA, lysophosphatidate/LPA, sphingosine 1-phosphate/S1P and ceramide 1-phosphate/C1P. Has no apparent extracellular phosphatase activity and therefore most probably acts intracellularly. Also acts on N-oleoyl ethanolamine phosphate/N-(9Z-octadecenoyl)-ethanolamine phosphate, a potential physiological compound. Through …

**Summary**, from NCBI Gene [8612](https://www.ncbi.nlm.nih.gov/gene/8612):

> The protein encoded by this gene is a member of the phosphatidic acid phosphatase (PAP) family. PAPs convert phosphatidic acid to diacylglycerol, and function in de novo synthesis of glycerolipids as well as in receptor-activated signal transduction mediated by phospholipase D. This protein is similar to phosphatidic acid phosphatase type 2A (PPAP2A) and type 2B (PPAP2B). All three proteins contain 6 transmembrane regions, and a consensus N-glycosylation site. This protein has been shown to …

**Accessions** — [HGNC:9230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9230) · Entrez [8612](https://www.ncbi.nlm.nih.gov/gene/8612) · UniProt [O43688](https://www.uniprot.org/uniprotkb/O43688) · Ensembl [ENSG00000141934](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141934)

## Data

Gene col 6581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6581); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6581]; `tensor/DDL_lfc|DDL_z.npy` [6581]; `embed/gene_vectors.npy` [6581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6581 or target_col == 6581). Every well: [[PLPP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLPP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

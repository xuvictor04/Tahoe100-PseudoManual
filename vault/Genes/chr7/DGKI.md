---
symbol: "DGKI"
type: "gene"
col: 8095
ensembl_id: "ENSG00000157680"
name: "diacylglycerol kinase iota"
location: "7q33"
module: 39
arm: "+"
pooled_cpm: 36.09
n_lines_expressing: 23
n_dd_up: 20
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 18
direction_downstream: 14
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# DGKI

*diacylglycerol kinase iota* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.14× (z +17.6, q 0e+00, up in 16 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.608× (z -5.5, q 3e-05, down in 15 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUBN]] (+0.66, fdr 7e-06), [[ITPR2-AS1]] (+0.66, fdr 7e-06), [[LINC02516]] (+0.65, fdr 7e-06); moves opposite to [[SLC9A6]] (-0.54, fdr 3e-05), [[SNTA1]] (-0.53, fdr 1e-05), [[PRKRA]] (-0.53, fdr 3e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[TLR1]] → it (grade B ⚠); 14 go from it, the strongest it → [[C12orf50]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.14×** | +17.6 | 0e+00 | 16/21 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +14.8 | 0e+00 | 10/20 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.57×** | +13.8 | 3e-41 | 16/21 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +11.2 | 5e-27 | 5/14 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +10.9 | 1e-25 | 8/18 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +8.9 | 4e-17 | 12/21 (SNU-423, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.7 | 1e-12 | 3/16 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +6.8 | 1e-09 | 7/20 (A-172, SNU-423, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.73×** | +6.0 | 2e-07 | 15/21 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 5e-04 | 13/21 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 12/21 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +4.0 | 0.003 | 9/21 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.003 | 8/21 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.006 | 5/20 (SW48, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.007 | 7/21 (SNU-423, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.035 | 6/20 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.040 | 4/21 (SW48, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.079 | 3/21 (HOP62, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.608×** | -5.5 | 3e-05 | 15/20 (COLO 205, H4, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.645×** | -4.6 | 0.001 | 15/21 (H4, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.665×** | -4.5 | 0.001 | 13/21 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.756×** | -4.4 | 0.002 | 9/21 (RKO, CHP-212, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.680×** | -4.2 | 0.002 | 10/20 (RKO, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.698×** | -3.7 | 0.018 | 11/21 (HOP62, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.716×** | -3.7 | 0.019 | 7/20 (A498, SNU-423, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.728×** | -3.5 | 0.033 | 9/20 (A498, RPMI-7951, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.743×** | -3.3 | 0.067 | 9/20 (H4, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.089 | 8/21 (A498, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.755×** | -3.1 | 0.095 | 9/20 (H4, BT-474, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **0.584×** | -3.1 | 0.095 | 7/19 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 643 | 1 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.0567× (z -23.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0766× (z -21.2) |
| [[A498 (line)]] | wt | 227 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.40× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.280× (z -8.9) |
| [[H4 (line)]] | wt | 106 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0447× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0594× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 172 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.118× (z -14.1) |
| [[SNU-423 (line)]] | alt | 15.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +11.1) | — |
| [[A-172 (line)]] | wt | 9.22 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +16.0) | — |
| [[C32 (line)]] | wt | 45.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +14.9) | — |
| [[COLO 205 (line)]] | alt | 22.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0458× (z -11.4) |
| [[HOP62 (line)]] | alt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 66.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +10.2) | — |
| [[SW48 (line)]] | wt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 36.2× (z +9.0) | — |
| [[A-427 (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.52 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.64 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.78 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.17 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.00 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.50 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUBN]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ITPR2-AS1]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[LINC02516]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[LINC00702]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[FSIP1]] | +0.64 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[ADAMTSL1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[DPYS]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MSR1]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[SCUBE2]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[MPP4]] | +0.63 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[GARIN1B]] | +0.63 | +0.68 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A6]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[SNTA1]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PRKRA]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[CHPT1]] | -0.53 | -0.63 / -0.48 | both halves | 2e-05 | STRING 664 |
| [[PMS2P3-1]] | -0.53 | -0.53 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 5, C 13. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR1]] | B | TLR1 activity raises DGKI's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without TLR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[GLIPR1]] | B | GLIPR1 activity raises DGKI's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without GLIPR1 | 0.040 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent |
| [[TLR6]] | B | TLR6 activity raises DGKI's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without TLR6 | 0.048 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[LINC03041]] | B | LINC03041 activity raises DGKI's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without LINC03041 | 0.084 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[ADTRP]] | B | ADTRP activity raises DGKI's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.70× lower at baseline in the lines without ADTRP | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[TMPRSS15]] | C | TMPRSS15 activity raises DGKI's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 4.63× lower at baseline in the lines without TMPRSS15 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises DGKI's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 3.01× lower at baseline in the lines without LINC01592 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[EBF1]] | C | EBF1 activity raises DGKI's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 3.14× lower at baseline in the lines without EBF1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises DGKI's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 3.17× lower at baseline in the lines without ALPK2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[RDUR]] | C | RDUR activity raises DGKI's level | lines that do not express RDUR (28) vs lines expressing it (22) | 3.05× lower at baseline in the lines without RDUR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises DGKI's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.67× lower at baseline in the lines without NLGN4Y | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[FGF5]] | C | FGF5 activity raises DGKI's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.59× lower at baseline in the lines without FGF5 | 0.012 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf50]] | B | DGKI activity raises C12orf50's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.75× lower at baseline in the lines without DGKI | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent |
| [[FHAD1]] | B | DGKI activity raises FHAD1's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.76× lower at baseline in the lines without DGKI | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent |
| [[SELPLG]] | B | DGKI activity raises SELPLG's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without DGKI | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent |
| [[SLC9A6]] | B | DGKI activity lowers SLC9A6's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.53× higher at baseline in the lines without DGKI | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent |
| [[FGF5]] | C | DGKI activity raises FGF5's level | lines that do not express DGKI (27) vs lines expressing it (23) | 3.73× lower at baseline in the lines without DGKI | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[RDUR]] | C | DGKI activity raises RDUR's level | lines that do not express DGKI (27) vs lines expressing it (23) | 2.95× lower at baseline in the lines without DGKI | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[LINC00504]] | C | DGKI activity raises LINC00504's level | lines that do not express DGKI (27) vs lines expressing it (23) | 2.13× lower at baseline in the lines without DGKI | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[LINC00702]] | C | DGKI activity raises LINC00702's level | lines that do not express DGKI (27) vs lines expressing it (23) | 3.02× lower at baseline in the lines without DGKI | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[ABCC9]] | C | DGKI activity raises ABCC9's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without DGKI | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[FRMD4A]] | C | DGKI activity raises FRMD4A's level | lines that do not express DGKI (27) vs lines expressing it (23) | 4.61× lower at baseline in the lines without DGKI | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[COL5A3]] | C | DGKI activity raises COL5A3's level | lines that do not express DGKI (27) vs lines expressing it (23) | 2.92× lower at baseline in the lines without DGKI | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[COLEC10]] | C | DGKI activity raises COLEC10's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without DGKI | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.2, 24.4); signed map (36.8, 25.3). **Vector** length 71.5, 19.4% of its response variance represented; |z| ≥ 3 in 642 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.0 | +3.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.3 | -5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -3.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol kinase iota |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:137,381,037-137,847,092 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DGK-IOTA |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Diacylglycerol kinase family |
| Reactome | 6 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (q) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75912](https://www.uniprot.org/uniprotkb/O75912) (Diacylglycerol kinase iota):

> Diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids. Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes (Probable). Has probably no preference for any of the diacylglycerols in terms of the acyl chain composition, especially for the acyl chain at the …

**Summary**, from NCBI Gene [9162](https://www.ncbi.nlm.nih.gov/gene/9162):

> This gene is a member of the type IV diacylglycerol kinase subfamily. Diacylglycerol kinases regulate the intracellular concentration of diacylglycerol through its phosphorylation, producing phosphatidic acid. The specific role of the enzyme encoded by this gene is undetermined, however, it may play a crucial role in the production of phosphatidic acid in the retina or in recessive forms of retinal degeneration. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2855) · Entrez [9162](https://www.ncbi.nlm.nih.gov/gene/9162) · UniProt [O75912](https://www.uniprot.org/uniprotkb/O75912) · Ensembl [ENSG00000157680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157680)

## Data

Gene col 8095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8095); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8095]; `tensor/DDL_lfc|DDL_z.npy` [8095]; `embed/gene_vectors.npy` [8095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8095 or target_col == 8095). Every well: [[DGKI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGKI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

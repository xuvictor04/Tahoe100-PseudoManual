---
symbol: "COL18A1"
type: "gene"
col: 11337
ensembl_id: "ENSG00000182871"
name: "collagen type XVIII alpha 1 chain"
location: "21q22.3"
module: 2
arm: "+"
pooled_cpm: 57.38
n_lines_expressing: 32
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# COL18A1

*collagen type XVIII alpha 1 chain* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.30× (z +15.9, q 0e+00, up in 27 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.444× (z -15.6, q 0e+00, down in 25 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCA2]] (+0.79, fdr 7e-06), [[TCF3]] (+0.67, fdr 1e-05), [[PIK3R2]] (+0.65, fdr 1e-05); moves opposite to [[PBDC1]] (-0.65, fdr 1e-05), [[C14orf119]] (-0.63, fdr 1e-05), [[RPP38]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MMP2]] → it (grade B ⚠); 7 go from it, the strongest it → [[TIMP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11337.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +15.9 | 0e+00 | 27/30 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +14.0 | 2e-42 | 23/29 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +13.8 | 4e-41 | 24/30 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +12.0 | 9e-31 | 20/25 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +10.6 | 2e-24 | 20/28 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +8.7 | 3e-16 | 22/30 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +4.0 | 0.005 | 9/30 (SW480, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.9 | 0.006 | 9/30 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.6 | 0.023 | 7/30 (A549, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.4 | 0.034 | 8/30 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +3.3 | 0.053 | 8/30 (HEC-1-A, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11337.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.444×** | -15.6 | 0e+00 | 25/29 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.662×** | -11.2 | 8e-27 | 20/30 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.580×** | -10.1 | 2e-21 | 24/30 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.620×** | -9.2 | 5e-18 | 22/30 (AN3 CA, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.683×** | -7.3 | 2e-11 | 22/30 (PANC-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -6.1 | 1e-07 | 19/30 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.842× | -4.7 | 2e-04 | 10/30 (PANC-1, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.794×** | -4.5 | 6e-04 | 15/30 (SK-MEL-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.809×** | -4.1 | 0.003 | 18/30 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.890× | -3.2 | 0.073 | 3/30 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.077 | 9/28 (C-33 A, H4, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.897× | -3.0 | 0.12 | 5/30 (SW480, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.0 | 0.12 | 6/28 (H4, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 120 | 4 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.10× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -13.7) |
| [[PANC-1 (line)]] | alt | 324 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -26.5) |
| [[CFPAC-1 (line)]] | alt | 78.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -10.9) |
| [[SW480 (line)]] | alt | 85.9 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.85× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.540× (z -8.8) |
| [[A498 (line)]] | wt | 71.3 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.04× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -11.6) |
| [[A-172 (line)]] | wt | 179 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -11.0) |
| [[A549 (line)]] | wt | 31.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +11.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 264 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.1) |
| [[HS-578T (line)]] | alt | 53.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 86.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 84.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -16.8) |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0932× (z -10.8) |
| [[C-33 A (line)]] | alt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.2) |
| [[C32 (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.6) |
| [[HT-29 (line)]] | alt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.9) |
| [[SNU-423 (line)]] | alt | 40.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +9.0) | — |
| [[A-427 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA2]] | +0.79 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[TCF3]] | +0.67 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.65 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PLXND1]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ANXA6]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[INTS1]] | +0.65 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[NOMO1]] | +0.64 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[NCOR2]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PLBD2]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PRKCSH]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[TBCD]] | +0.62 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[CEP131]] | +0.62 | +0.57 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBDC1]] | -0.65 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.63 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RPP38]] | -0.63 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.63 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[EID2]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[NME6]] | -0.61 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.60 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[RDH14]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ZNF181]] | -0.60 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[NSMCE3]] | -0.60 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[CARD6]] | -0.60 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ZNF525]] | -0.60 | -0.62 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP2]] | B | MMP2 activity raises COL18A1's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 2.99× lower at baseline in the lines without MMP2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[HDAC6]] | B | HDAC6 activity lowers COL18A1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[L1CAM]] | B | L1CAM activity raises COL18A1's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 2.23× lower at baseline in the lines without L1CAM | 0.074 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[BCAM]] | B | BCAM activity raises COL18A1's level | lines that do not express BCAM (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without BCAM | 0.074 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[ZNF525]] | B | ZNF525 activity raises COL18A1's level | lines that do not express ZNF525 (10) vs lines expressing it (40) | 3.04× lower at baseline in the lines without ZNF525 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF331, ZNF577, ZNF83 |
| [[SLIT3]] | B | SLIT3 activity raises COL18A1's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 2.20× lower at baseline in the lines without SLIT3 | 0.096 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3 |
| [[DKK3]] | C | DKK3 activity raises COL18A1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 3.32× lower at baseline in the lines without DKK3 | 0.036 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIMP2]] | B | COL18A1 activity raises TIMP2's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 2.61× lower at baseline in the lines without COL18A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[BCAM]] | B | COL18A1 activity raises BCAM's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 1.85× lower at baseline in the lines without COL18A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[ZNF525]] | B | COL18A1 activity raises ZNF525's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without COL18A1 | 0.042 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[HSPG2]] | B | COL18A1 activity raises HSPG2's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 1.98× lower at baseline in the lines without COL18A1 | 0.045 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[FBRSL1]] | B | COL18A1 activity lowers FBRSL1's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 1.32× higher at baseline in the lines without COL18A1 | 0.046 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[L1CAM]] | B | COL18A1 activity raises L1CAM's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 2.56× lower at baseline in the lines without COL18A1 | 0.092 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B |
| [[DKK3]] | C | COL18A1 activity raises DKK3's level | lines that do not express COL18A1 (18) vs lines expressing it (32) | 4.23× lower at baseline in the lines without COL18A1 | 0.028 | ⚠ within organs, on part of the lines; also absent: NGFR, CX3CL1, PPP2R2B; co-absent with the target |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.6, -23.0); signed map (-45.4, -11.8). **Vector** length 84.6, 21.5% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +10.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +15.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.6 | -9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -15.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.6 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.9 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XVIII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:45,405,165-45,513,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KS, KNO1; previously KNO |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Multiplexin collagens |
| Reactome | 10 pathways, smallest: Activation of Matrix Metalloproteinases; Laminin interactions; Collagen chain trimerization |
| Matched by | ensembl_id |

**Function**, from UniProt [P39060](https://www.uniprot.org/uniprotkb/P39060) (Collagen alpha-1(XVIII) chain):

> Probably plays a major role in determining the retinal structure as well as in the closure of the neural tube.; [Non-collagenous domain 1]: May regulate extracellular matrix-dependent motility and morphogenesis of endothelial and non-endothelial cells; the function requires homotrimerization and implicates MAPK signaling.; [Endostatin]: Potently inhibits endothelial cell proliferation and angiogenesis. May inhibit angiogenesis by binding to the heparan sulfate proteoglycans involved in growth …

**Summary**, from NCBI Gene [80781](https://www.ncbi.nlm.nih.gov/gene/80781):

> This gene encodes the alpha chain of type XVIII collagen. This collagen is one of the multiplexins, extracellular matrix proteins that contain multiple triple-helix domains (collagenous domains) interrupted by non-collagenous domains. A long isoform of the protein has an N-terminal domain that is homologous to the extracellular part of frizzled receptors. Proteolytic processing at several endogenous cleavage sites in the C-terminal domain results in production of endostatin, a potent …

**Accessions** — [HGNC:2195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2195) · Entrez [80781](https://www.ncbi.nlm.nih.gov/gene/80781) · UniProt [P39060](https://www.uniprot.org/uniprotkb/P39060) · Ensembl [ENSG00000182871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182871)

## Data

Gene col 11337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11337); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11337]; `tensor/DDL_lfc|DDL_z.npy` [11337]; `embed/gene_vectors.npy` [11337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11337 or target_col == 11337). Every well: [[COL18A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL18A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

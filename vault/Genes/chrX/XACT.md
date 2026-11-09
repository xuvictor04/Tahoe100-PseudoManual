---
symbol: "XACT"
type: "gene"
col: 14285
ensembl_id: "ENSG00000241743"
name: "X active specific transcript"
location: "Xq23"
module: 73
arm: "+"
pooled_cpm: 44.12
n_lines_expressing: 20
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 22
direction_downstream: 21
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# XACT

*X active specific transcript* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.94× (z +18.7, q 0e+00, up in 16 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.724× (z -4.0, q 0.022, down in 12 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.0389×, LS 180 0.0814×, NCI-H1792 0.117×, A549 0.263×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.0553×, LS 180 0.131×, HEC-1-A 0.138×; ⚠ cell-cycle shift, explains ~13% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.0643×, LS 180 0.0698×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (LS 180 0.0722×, LoVo 0.121×); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 0.0432×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02582]] (+0.58, fdr 2e-05), [[DSG4]] (+0.57, fdr 1e-05), [[TPTEP1-1]] (+0.57, fdr 2e-05); moves opposite to [[ZNF362]] (-0.44, fdr 6e-05), [[CDIPT]] (-0.44, fdr 6e-05), [[OBSL1]] (-0.43, fdr 2e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[CDK18]] → it (grade B ⚠); 21 go from it, the strongest it → [[WSCD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.94×** | +18.7 | 0e+00 | 16/18 (KATO III, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.68×** | +12.0 | 6e-31 | 14/17 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +8.5 | 5e-15 | 5/18 (SNU-423, A-427, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +7.6 | 6e-12 | 1/13 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +7.5 | 6e-12 | 2/15 (LOX-IMVI, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +5.9 | 4e-07 | 10/18 (SHP-77, KATO III, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +5.0 | 5e-05 | 12/17 (KATO III, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 3e-04 | 8/18 (A-427, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +3.8 | 0.010 | 6/18 (Hs 766T, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.018 | 2/17 (NCI-H1573, SHP-77) | inconsistent across doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.036 | 1/17 (NCI-H1573) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.31×** | +3.3 | 0.050 | 4/17 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.068 | 0/18 | top dose only | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.076 | 7/18 (SNU-423, A-427, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14285.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.0389×, LS 180 0.0814×, NCI-H1792 0.117×, A549 0.263×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.0553×, LS 180 0.131×, HEC-1-A 0.138×; ⚠ cell-cycle shift, explains ~13% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.0643×, LS 180 0.0698×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (LS 180 0.0722×, LoVo 0.121×); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 0.0432×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.724×** | -4.0 | 0.022 | 12/18 (LS 180, HS-578T, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -4.0 | 0.022 | 1/18 (SNU-1) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.756× | -3.4 | 0.11 | 7/17 (HEC-1-A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | 0.762× | -3.2 | 0.15 | 8/18 (A549, NCI-H1792, …) | top dose only | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | 0.832× | -3.2 | 0.15 | 11/18 (KATO III, RPMI-7951, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.771× | -3.1 | 0.19 | 14/17 (A549, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 125 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0814× (z -19.5) |
| [[KATO III (line)]] | alt | 102 | 5 (3 ⚠) | 5 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.70× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 483 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0389× (z -28.5) |
| [[A549 (line)]] | wt | 54.5 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.26× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0916× (z -13.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 302 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -14.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H1792 (line)]] | alt | 39.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -17.0) |
| [[C32 (line)]] | wt | 59.1 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.57× (z +12.3) | [[Ixazomib citrate (drug)]] 5 µM 0.160× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 75.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 13.0 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 11.3× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.54× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.0879× (z -13.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.100× (z -8.6) |
| [[HS-578T (line)]] | alt | 14.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.70× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0870× (z -9.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 21.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.56× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 15.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.68× (z +9.6) | — |
| [[A-172 (line)]] | wt | 5.56 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.59 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.72 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.63 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.99 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.79 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.39 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02582]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[DSG4]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TPTEP1-1]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[WSCD1]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CTSE]] | +0.55 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[SPON1]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SLCO1B3]] | +0.53 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[CALB1]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[CAPN14]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[IQGAP2]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[FA2H]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[REG4]] | +0.51 | +0.56 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | -0.44 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[CDIPT]] | -0.44 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[OBSL1]] | -0.43 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[DVL3]] | -0.43 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[NCOA2]] | -0.42 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[ANGEL2]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[HOXC6]] | -0.41 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[INPPL1]] | -0.40 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[ADI1]] | -0.40 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[TARBP2]] | -0.40 | -0.39 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 4, C 18. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDK18]] | B | CDK18 activity raises XACT's level | lines that do not express CDK18 (9) vs lines expressing it (41) | 2.09× lower at baseline in the lines without CDK18 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC00511, ABCG2, CYP2J2; maybe low, not absent |
| [[PRSS3]] | B | PRSS3 activity raises XACT's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.30× lower at baseline in the lines without PRSS3 | 0.056 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[IL2RG]] | B | IL2RG activity raises XACT's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.46× lower at baseline in the lines without IL2RG | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[ZNF365]] | B | ZNF365 activity raises XACT's level | lines that do not express ZNF365 (24) vs lines expressing it (26) | 1.48× lower at baseline in the lines without ZNF365 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000285837, CHSY3, FLT1 |
| [[LINC02582]] | C | LINC02582 activity raises XACT's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 5.94× lower at baseline in the lines without LINC02582 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[IL33]] | C | IL33 activity raises XACT's level | lines that do not express IL33 (35) vs lines expressing it (15) | 2.06× lower at baseline in the lines without IL33 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |
| [[LINC00923]] | C | LINC00923 activity raises XACT's level | lines that do not express LINC00923 (33) vs lines expressing it (17) | 3.16× lower at baseline in the lines without LINC00923 | 0.017 | ⚠ within organs, on part of the lines; also absent: TM4SF4, SLC25A24P1, ENSG00000283633; co-absent with the target |
| [[ERG]] | C | ERG activity raises XACT's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.53× lower at baseline in the lines without ERG | 0.026 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[TPTEP1-1]] | C | TPTEP1-1 activity raises XACT's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 3.69× lower at baseline in the lines without TPTEP1-1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[LINC00457]] | C | LINC00457 activity raises XACT's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 2.22× lower at baseline in the lines without LINC00457 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent; co-absent with the target |
| [[SPON1]] | C | SPON1 activity raises XACT's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 2.85× lower at baseline in the lines without SPON1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[REG4]] | C | REG4 activity raises XACT's level | lines that do not express REG4 (43) vs lines expressing it (7) | 3.79× lower at baseline in the lines without REG4 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 5, C 16. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WSCD1]] | B | XACT activity raises WSCD1's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without XACT | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |
| [[NRXN3]] | B | XACT activity raises NRXN3's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.90× lower at baseline in the lines without XACT | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |
| [[NEURL1]] | B | XACT activity raises NEURL1's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.45× lower at baseline in the lines without XACT | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |
| [[IL1R2]] | B | XACT activity raises IL1R2's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.59× lower at baseline in the lines without XACT | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |
| [[CAPN14]] | B | XACT activity raises CAPN14's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.70× lower at baseline in the lines without XACT | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |
| [[LINC02582]] | C | XACT activity raises LINC02582's level | lines that do not express XACT (30) vs lines expressing it (20) | 3.56× lower at baseline in the lines without XACT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[CALB1]] | C | XACT activity raises CALB1's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.31× lower at baseline in the lines without XACT | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[ERG]] | C | XACT activity raises ERG's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without XACT | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[IL33]] | C | XACT activity raises IL33's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without XACT | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[SPON1]] | C | XACT activity raises SPON1's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.75× lower at baseline in the lines without XACT | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[REG4]] | C | XACT activity raises REG4's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.63× lower at baseline in the lines without XACT | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[CD200]] | C | XACT activity raises CD200's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without XACT | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.2, 50.1); signed map (66.5, 8.3). **Vector** length 69.6, 21.4% of its response variance represented; |z| ≥ 3 in 531 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +18.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.0 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.9 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | X active specific transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq23 — chrX:113,616,300-114,059,289 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [105463123](https://www.ncbi.nlm.nih.gov/gene/105463123):

> This gene produces a spliced long non-coding RNA that is thought to play a role in the control of X-chromosome inactivation (XCI). This transcript has been shown to specifically coat the active X chromosome in human pluripotent cells. [provided by RefSeq, Mar 2015]

**Accessions** — [HGNC:45056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45056) · Entrez [105463123](https://www.ncbi.nlm.nih.gov/gene/105463123) · Ensembl [ENSG00000241743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241743)

## Data

Gene col 14285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14285); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14285]; `tensor/DDL_lfc|DDL_z.npy` [14285]; `embed/gene_vectors.npy` [14285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14285 or target_col == 14285). Every well: [[XACT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XACT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

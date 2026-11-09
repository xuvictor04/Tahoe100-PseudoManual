---
symbol: "SREK1IP1"
type: "gene"
col: 7678
ensembl_id: "ENSG00000153006"
name: "SREK1 interacting protein 1"
location: "5q12.3"
module: 203
arm: "+"
pooled_cpm: 79.83
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/203"]
generated_by: "tahoemap"
---

# SREK1IP1

*SREK1 interacting protein 1* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.83× (z +8.4, q 3e-14, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.96× (z +7.9, q 1e-12, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.515× (z -9.2, q 3e-17, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KANSL1]] (+0.64, fdr 9e-06), [[MPHOSPH8]] (+0.63, fdr 1e-05), [[CWC15]] (+0.63, fdr 7e-06); moves opposite to [[AKAP11]] (-0.60, fdr 1e-05), [[DNMT1]] (-0.58, fdr 1e-05), [[RBBP7]] (-0.56, fdr 2e-05).
> It is in [[Module 203]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +8.4 | 3e-14 | 46/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.96×** | +7.9 | 1e-12 | 43/49 (RKO, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +6.3 | 4e-08 | 40/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +5.2 | 3e-05 | 35/48 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.0 | 8e-05 | 33/48 (C32, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +4.8 | 1e-04 | 34/48 (HEC-1-A, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 7e-04 | 31/48 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +4.4 | 9e-04 | 32/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.2 | 0.002 | 29/48 (NCI-H1573, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +4.1 | 0.003 | 27/48 (A549, SW 900, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.33×** | +4.0 | 0.003 | 27/48 (Hs 766T, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.006 | 21/49 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.007 | 30/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.31×** | +3.6 | 0.013 | 26/48 (SNU-1, SW 900, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.28×** | +3.4 | 0.023 | 25/48 (COLO 205, A549, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.038 | 23/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.038 | 21/47 (LS 180, SW480, …) | two highest doses | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.073 | 21/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +2.9 | 0.088 | 15/48 (HCT15, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.515×** | -9.2 | 3e-17 | 47/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.570×** | -7.8 | 2e-12 | 46/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.655×** | -5.8 | 9e-07 | 37/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -4.5 | 8e-04 | 30/48 (LoVo, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.729×** | -4.4 | 0.001 | 30/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.798× | -3.1 | 0.18 | 18/48 (RPMI-7951, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 127 | 4 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.43× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.586× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 211 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -17.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.320× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 54.2 | 5 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.51× (z +11.2) | — |
| [[SW480 (line)]] | alt | 102 | 3 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.96× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.381× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 145 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -12.4) |
| [[KATO III (line)]] | alt | 58.7 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -9.1) |
| [[LS 180 (line)]] | wt | 92.8 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.44× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 87.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 176 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.427× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 86.2 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.96× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +10.2) | — |
| [[A498 (line)]] | wt | 55.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[Hs 766T (line)]] | wt | 66.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 59.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.03× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.44× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | — |
| [[RKO (line)]] | wt | 101 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.57× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 97.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[A-172 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANSL1]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[MPHOSPH8]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CWC15]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[MRPL32]] | +0.63 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ARL8A]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TEFM]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[NGDN]] | +0.60 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[ALKBH4]] | +0.59 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[ZNF358]] | +0.59 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[FAM182B]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF528-AS1]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP11]] | -0.60 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[DNMT1]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.56 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[G6PD]] | -0.56 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[PRPS2]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[NUP188]] | -0.54 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[TRIP13]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RRM2]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[H2AX]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MTHFD1]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[COTL1]] | -0.52 | -0.39 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SREK1IP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SREK1IP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM182B]] | C | FAM182B activity lowers SREK1IP1's level | lines that do not express FAM182B (4) vs lines expressing it (46) | 1.87× higher at baseline in the lines without FAM182B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FGF12, SLFNL1-AS1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 203]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.2, -11.3); signed map (-14.1, -5.3). **Vector** length 107, 34.8% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.5 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -9.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | +1.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.9 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.8 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | SREK1 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:64,718,148-64,768,691 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36754, P18SRP; previously SFRS12IP1 |
| Gene groups (HGNC) | Zinc fingers CCHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9Q2](https://www.uniprot.org/uniprotkb/Q8N9Q2) (Protein SREK1IP1):

> Possible splicing regulator involved in the control of cellular survival.

**Summary**, from NCBI Gene [285672](https://www.ncbi.nlm.nih.gov/gene/285672):

> Predicted to enable nucleic acid binding activity and zinc ion binding activity. Predicted to be involved in RNA splicing and mRNA processing. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26716) · Entrez [285672](https://www.ncbi.nlm.nih.gov/gene/285672) · UniProt [Q8N9Q2](https://www.uniprot.org/uniprotkb/Q8N9Q2) · Ensembl [ENSG00000153006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153006)

## Data

Gene col 7678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7678); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7678]; `tensor/DDL_lfc|DDL_z.npy` [7678]; `embed/gene_vectors.npy` [7678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7678 or target_col == 7678). Every well: [[SREK1IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SREK1IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "FLG-AS1"
type: "gene"
col: 14160
ensembl_id: "ENSG00000237975"
name: "cervical cancer associated DHX9 suppressive transcript"
location: "1q21.3"
module: 10
arm: "+"
pooled_cpm: 17.4
n_lines_expressing: 28
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 24
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FLG-AS1

*cervical cancer associated DHX9 suppressive transcript* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.82× (z +27.4, q 0e+00, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.528× (z -7.0, q 1e-09, down in 20 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.563× (z -6.3, q 8e-08, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD31]] (+0.70, fdr 3e-05), [[TAFA2]] (+0.68, fdr 1e-05), [[NPAS3]] (+0.68, fdr 3e-05); moves opposite to [[PRUNE1]] (-0.62, fdr 3e-05), [[PHKA2]] (-0.60, fdr 1e-04), [[RAB40B]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 5 go from it, the strongest it → [[NECTIN3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.82×** | +27.4 | 0e+00 | 22/26 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.40×** | +15.6 | 0e+00 | 22/25 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.44×** | +13.8 | 3e-41 | 25/26 (NCI-H460, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.18×** | +12.2 | 4e-32 | 20/26 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +10.4 | 2e-23 | 18/26 (SW480, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.19×** | +8.6 | 5e-16 | 16/26 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +8.2 | 3e-14 | 13/26 (SW48, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +7.5 | 5e-12 | 12/26 (NCI-H2347, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.1 | 8e-11 | 6/23 (NCI-H2347, SW 900, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +7.0 | 1e-10 | 14/26 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +6.6 | 2e-09 | 8/25 (SW48, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.2 | 3e-08 | 5/16 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +6.0 | 9e-08 | 6/21 (NCI-H2030, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +4.7 | 9e-05 | 14/26 (SW480, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.3 | 6e-04 | 11/26 (SW48, LS 180, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +4.3 | 7e-04 | 12/26 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.03×** | +4.1 | 0.002 | 12/25 (NCI-H460, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.010 | 7/26 (SW48, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -7.0 | 1e-09 | 20/23 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.563×** | -6.3 | 8e-08 | 18/26 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.635×** | -5.0 | 1e-04 | 16/26 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -4.7 | 3e-04 | 15/26 (SK-MEL-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -4.1 | 0.005 | 17/26 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 142 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 174 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.313× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.332× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 5.09 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +14.5) | — |
| [[SHP-77 (line)]] | alt | 97.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -12.7) |
| [[SW48 (line)]] | wt | 36.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +15.0) | — |
| [[A-172 (line)]] | wt | 8.96 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.69× (z +8.7) | — |
| [[C32 (line)]] | wt | 34.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +10.0) | — |
| [[SW480 (line)]] | alt | 16.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 7.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +17.2) | — |
| [[NCI-H1792 (line)]] | alt | 6.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.22× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 44.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 5.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 6.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.10× (z +10.1) | — |
| [[A-427 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD31]] | +0.70 | +0.72 / +0.46 | both halves | 3e-05 |  |
| [[TAFA2]] | +0.68 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NPAS3]] | +0.68 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[FBXO38-DT]] | +0.65 | +0.71 / +0.34 | both halves | 1e-04 |  |
| [[NECTIN3-AS1]] | +0.65 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[RAP2C-AS1]] | +0.65 | +0.72 / +0.38 | both halves | 7e-05 |  |
| [[FRG1-DT]] | +0.64 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[STPG2]] | +0.64 | +0.63 / +0.43 | both halves | 4e-05 |  |
| [[TMLHE-AS1]] | +0.64 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ARRDC3-AS1]] | +0.63 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[PKN2-AS1]] | +0.63 | +0.65 / +0.32 | both halves | 2e-04 |  |
| [[MAD2L1-DT]] | +0.63 | +0.65 / +0.22 | both halves | 6e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRUNE1]] | -0.62 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[PHKA2]] | -0.60 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[RAB40B]] | -0.58 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[BRAT1]] | -0.57 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[KIAA1328]] | -0.56 | -0.58 / -0.21 | both halves | 6e-04 |  |
| [[L2HGDH]] | -0.56 | -0.54 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[CABLES2]] | -0.56 | -0.41 / -0.22 | both halves | 6e-04 |  |
| [[DPY30]] | -0.55 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[DHTKD1]] | -0.55 | -0.44 / -0.22 | both halves | 6e-04 |  |
| [[KLHL8]] | -0.55 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[FAM118A]] | -0.55 | -0.49 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[FBXO21]] | -0.54 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers FLG-AS1's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.9% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds |
| [[TOP2A]] | B | TOP2A activity lowers FLG-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GAS6-AS1]] | B | GAS6-AS1 activity raises FLG-AS1's level | lines that do not express GAS6-AS1 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without GAS6-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ECM1, LINC02055, LINC02220; maybe low, not absent |
| [[CDH8]] | B | CDH8 activity raises FLG-AS1's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without CDH8 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent |
| [[RIMS2]] | C | RIMS2 activity raises FLG-AS1's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 3.67× lower at baseline in the lines without RIMS2 | 0.015 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3; co-absent with the target |
| [[FLRT2]] | C | FLRT2 activity raises FLG-AS1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 3.05× lower at baseline in the lines without FLRT2 | 0.076 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2; co-absent with the target |
| [[KRT8P12]] | C | KRT8P12's natural level weakens FLG-AS1's drug response | KRT8P12's natural level across 26 lines (lineage-adjusted; a glimpse) | r -0.87, reverse -0.14; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NECTIN3-AS1]] | B | FLG-AS1 activity lowers NECTIN3-AS1's level | lines that do not express FLG-AS1 (22) vs lines expressing it (28) | 1.10× higher at baseline in the lines without FLG-AS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: FLRT2, CNRIP1, MARCHF4 |
| [[LINC02328]] | B | FLG-AS1 activity raises LINC02328's level | lines that do not express FLG-AS1 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without FLG-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: FLRT2, CNRIP1, MARCHF4 |
| [[ABCA12]] | B | FLG-AS1 activity raises ABCA12's level | lines that do not express FLG-AS1 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without FLG-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: FLRT2, CNRIP1, MARCHF4 |
| [[FAM118A]] | B | FLG-AS1 activity raises FAM118A's level | lines that do not express FLG-AS1 (22) vs lines expressing it (28) | 1.02× lower at baseline in the lines without FLG-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: FLRT2, CNRIP1, MARCHF4 |
| [[FLRT2]] | C | FLG-AS1 activity raises FLRT2's level | lines that do not express FLG-AS1 (22) vs lines expressing it (28) | 4.50× lower at baseline in the lines without FLG-AS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: FLRT2, CNRIP1, MARCHF4; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (16.6, 19.6); signed map (31.9, -9.7). **Vector** length 69.9, 17.0% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +27.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +15.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | +1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.9 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Piroxicam (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cervical cancer associated DHX9 suppressive transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q21.3 — chr1:152,168,125-152,445,456 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AL589986.2, lnc-CCDST; previously LINC02962, FLG-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | prev_symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55988) · Entrez [339400](https://www.ncbi.nlm.nih.gov/gene/339400) · Ensembl [ENSG00000237975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237975)

## Data

Gene col 14160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14160); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14160]; `tensor/DDL_lfc|DDL_z.npy` [14160]; `embed/gene_vectors.npy` [14160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14160 or target_col == 14160). Every well: [[FLG-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLG-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

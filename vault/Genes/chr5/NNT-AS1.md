---
symbol: "NNT-AS1"
type: "gene"
col: 14516
ensembl_id: "ENSG00000248092"
name: "NNT antisense RNA 1"
location: "5p12"
module: 68
arm: "+"
pooled_cpm: 18.14
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# NNT-AS1

*NNT antisense RNA 1* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.24× (z +3.7, q 0.054, up in 20 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.79×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.261× (z -16.4, q 0e+00, down in 39 of 42 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF764]] (+0.70, fdr 3e-05), [[GTF2H1]] (+0.69, fdr 1e-05), [[METTL18]] (+0.67, fdr 1e-05); moves opposite to [[RIMS3]] (-0.63, fdr 2e-05), [[TMEM184B]] (-0.59, fdr 1e-04), [[PCMT1]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PGAP4]] → it (grade B ⚠); 9 go from it, the strongest it → [[FAM200A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14516.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.79×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.054 | 20/41 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.6 | 0.054 | 19/37 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.054 | 13/42 (KATO III, J82, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.31× | +3.3 | 0.14 | 13/41 (COLO 205, HT-29, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.16 | 8/42 (NCI-H2347, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.16 | 13/41 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.16 | 13/41 (KATO III, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.261×** | -16.4 | 0e+00 | 39/42 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.311×** | -14.2 | 2e-43 | 41/42 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.362×** | -12.4 | 5e-33 | 39/41 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -8.3 | 2e-14 | 30/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.577×** | -6.7 | 3e-09 | 27/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.353×** | -6.6 | 3e-09 | 30/42 (SHP-77, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.355×** | -6.6 | 3e-09 | 30/41 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -5.7 | 7e-07 | 23/42 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -5.6 | 1e-06 | 22/42 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.427×** | -5.4 | 3e-06 | 27/41 (SW480, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.642×** | -5.4 | 4e-06 | 23/41 (PANC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -5.1 | 1e-05 | 20/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.654×** | -4.9 | 5e-05 | 22/42 (AN3 CA, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.494×** | -4.5 | 3e-04 | 24/41 (LOX-IMVI, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.780×** | -4.3 | 8e-04 | 21/42 (SW480, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.726×** | -3.9 | 0.003 | 17/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.4 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0906× (z -28.5) |
| [[PANC-1 (line)]] | alt | 19.5 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -11.8) |
| [[SHP-77 (line)]] | alt | 109 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -22.2) |
| [[Hs 766T (line)]] | wt | 33.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -12.4) |
| [[SNU-423 (line)]] | alt | 31.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -15.1) |
| [[A-172 (line)]] | wt | 20.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0797× (z -15.4) |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -9.5) |
| [[J82 (line)]] | alt | 32.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -13.5) |
| [[KATO III (line)]] | alt | 25.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.100× (z -15.2) |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0914× (z -9.8) |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0622× (z -11.1) |
| [[COLO 205 (line)]] | alt | 28.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -10.4) |
| [[H4 (line)]] | wt | 36.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 6.51 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0610× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0492× (z -9.6) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -9.2) |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0787× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.112× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 23.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 8.83 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -9.9) |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -8.9) |
| [[A-427 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF764]] | +0.70 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[GTF2H1]] | +0.69 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[METTL18]] | +0.67 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[ZNF518A]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[PLS3-AS1]] | +0.67 | +0.59 / +0.48 | both halves | 2e-05 | same gene group |
| [[PCNX4-DT]] | +0.67 | +0.66 / +0.32 | both halves | 2e-04 |  |
| [[LATS1]] | +0.67 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[KIAA1586]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[LINC02307]] | +0.65 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[INO80D]] | +0.65 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[TMEM35B]] | +0.65 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD26]] | +0.65 | +0.66 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS3]] | -0.63 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TMEM184B]] | -0.59 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[PCMT1]] | -0.59 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[ABHD17A]] | -0.59 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[PDIA4]] | -0.59 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CADM4]] | -0.59 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[STRAP]] | -0.58 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[LPCAT1]] | -0.58 | -0.61 / -0.23 | both halves | 5e-04 |  |
| [[TNK2]] | -0.58 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[GNAI2]] | -0.58 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[RSU1]] | -0.58 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SIPA1]] | -0.58 | -0.55 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGAP4]] | B | PGAP4 activity raises NNT-AS1's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without PGAP4 | 0.023 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[PLXNB3-AS1]] | B | PLXNB3-AS1 activity strengthens NNT-AS1's drug response | lines that do not express PLXNB3-AS1 (10) vs lines expressing it (32) | the lines without PLXNB3-AS1 respond 0.66× as strongly (z diff +1.53); strongest at Belinostat 5 µM: 0.45x vs 0.31x (z diff +2.9) | 0.042 | ⚠ within organs, on part of the lines; also absent: CA9; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises NNT-AS1's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 2.13× lower at baseline in the lines without SLC25A24P1 | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |
| [[LINC00649]] | B | LINC00649 activity strengthens NNT-AS1's drug response | lines that do not express LINC00649 (21) vs lines expressing it (21) | the lines without LINC00649 respond 0.79× as strongly (z diff +1.18); strongest at Panobinostat 0.5 µM: 0.37x vs 0.24x (z diff +2.5) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000287923, RMST, SERPINF1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC25A24P1]] | B | SLC25A24P1 activity strengthens NNT-AS1's drug response | lines that do not express SLC25A24P1 (34) vs lines expressing it (8) | the lines without SLC25A24P1 respond 0.78× as strongly (z diff +1.14); strongest at Panobinostat 0.05 µM: 0.69x vs 0.49x (z diff +2.6) | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM200A]] | B | NNT-AS1 activity lowers FAM200A's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without NNT-AS1 | 0.016 | ⚠ within organs, on part of the lines; co-absent genes |
| [[THBS4]] | B | NNT-AS1 activity lowers THBS4's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.69× higher at baseline in the lines without NNT-AS1 | 0.018 | ⚠ within organs, on part of the lines; co-absent genes |
| [[GNPDA1]] | B | NNT-AS1 activity lowers GNPDA1's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.71× higher at baseline in the lines without NNT-AS1 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes |
| [[KRIT1]] | B | NNT-AS1 activity lowers KRIT1's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.33× higher at baseline in the lines without NNT-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes |
| [[DUS4L]] | B | NNT-AS1 activity lowers DUS4L's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without NNT-AS1 | 0.057 | ⚠ within organs, on part of the lines; co-absent genes |
| [[PCNX4-DT]] | B | NNT-AS1 activity lowers PCNX4-DT's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.33× higher at baseline in the lines without NNT-AS1 | 0.059 | ⚠ within organs, on part of the lines; co-absent genes |
| [[OXA1L-DT]] | B | NNT-AS1 activity lowers OXA1L-DT's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.44× higher at baseline in the lines without NNT-AS1 | 0.063 | ⚠ within organs, on part of the lines; co-absent genes |
| cells under [[Topotecan (hydrochloride) (drug)]] 5 µM | B | [[NNT]], NNT-AS1 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express NNT, NNT-AS1 (6) vs lines expressing them (42) | the lines without NNT, NNT-AS1: 0.65× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-absent genes |
| cells under [[Docetaxel (drug)]] 5 µM | B | [[NNT]], NNT-AS1 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express NNT, NNT-AS1 (6) vs lines expressing them (42) | the lines without NNT, NNT-AS1: 0.85× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-absent genes |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.708). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (0.1, 9.3); signed map (19.0, -19.6). **Vector** length 86.8, 19.8% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.2 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.9 | -14.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -16.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | NNT antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p12 — chr5:43,571,594-43,603,230 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-159F24.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49005) · Entrez [100652772](https://www.ncbi.nlm.nih.gov/gene/100652772) · Ensembl [ENSG00000248092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248092)

## Data

Gene col 14516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14516); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14516]; `tensor/DDL_lfc|DDL_z.npy` [14516]; `embed/gene_vectors.npy` [14516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14516 or target_col == 14516). Every well: [[NNT-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NNT-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

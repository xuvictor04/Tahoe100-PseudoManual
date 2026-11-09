---
symbol: "SESN3"
type: "gene"
col: 7350
ensembl_id: "ENSG00000149212"
name: "sestrin 3"
location: "11q21"
module: 9
arm: "+"
pooled_cpm: 25.47
n_lines_expressing: 30
n_dd_up: 37
n_dd_down: 11
n_dd_up_clean: 31
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SESN3

*sestrin 3* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.01× (z +33.9, q 0e+00, up in 27 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.424× (z -7.8, q 3e-12, down in 23 of 29 measured lines).
> Its strongest partners by |cos| (69 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 31 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORBS1]] (+0.58, fdr 3e-05), [[MAN1A1]] (+0.53, fdr 1e-05), [[PPP2R2B]] (+0.53, fdr 1e-05); moves opposite to [[TIPIN]] (-0.51, fdr 3e-04), [[MRM1]] (-0.50, fdr 5e-04), [[ZNF324B]] (-0.50, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DPYSL3]] → it (grade B ⚠); 6 go from it, the strongest it → [[DPYSL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.01×** | +33.9 | 0e+00 | 27/28 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.62×** | +30.1 | 0e+00 | 27/28 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.55×** | +29.9 | 0e+00 | 27/28 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +24.4 | 0e+00 | 23/28 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.50×** | +22.6 | 0e+00 | 25/28 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.61×** | +22.4 | 0e+00 | 27/28 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +20.8 | 0e+00 | 19/28 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +14.5 | 1e-45 | 25/28 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +13.2 | 4e-38 | 12/20 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.21×** | +13.1 | 2e-37 | 25/28 (A498, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.05×** | +12.5 | 4e-34 | 22/28 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **2.03×** | +12.4 | 2e-33 | 26/28 (NCI-H2347, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.95×** | +9.9 | 3e-21 | 13/23 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +9.3 | 5e-19 | 8/24 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +8.7 | 1e-16 | 14/28 (BT-474, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +8.5 | 7e-16 | 15/28 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.27×** | +7.5 | 2e-12 | 19/28 (NCI-H2347, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.2 | 2e-11 | 10/28 (C-33 A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -7.8 | 3e-12 | 23/29 (SW1417, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.502×** | -6.3 | 1e-07 | 14/28 (SNU-423, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.752×** | -5.0 | 1e-04 | 10/28 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.838× | -4.4 | 0.002 | 13/28 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.773×** | -4.3 | 0.002 | 9/28 (CHP-212, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -3.9 | 0.010 | 1/28 (HCT15) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.801×** | -3.7 | 0.016 | 16/28 (C-33 A, SW 1271, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.818×** | -3.5 | 0.033 | 7/28 (H4, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.824×** | -3.4 | 0.047 | 9/28 (C32, HS-578T, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.826×** | -3.3 | 0.047 | 9/28 (CHP-212, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.819×** | -3.2 | 0.064 | 8/28 (COLO 205, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.775×** | -3.2 | 0.070 | 9/28 (NCI-H460, SW1417, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.830×** | -3.1 | 0.075 | 3/28 (SW480, NCI-H460, …) | top dose only |  |
| [[Clotrimazole (drug)]] 5 µM |  | 0.886× | -3.0 | 0.11 | 2/28 (CHP-212, Panc 03.27) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 16.5 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +19.8) | — |
| [[C32 (line)]] | wt | 134 | 2 | 7 (4 ⚠) | [[Elimusertib hydrochloride (drug)]] 0.05 µM 2.95× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -16.3) |
| [[HT-29 (line)]] | alt | 12.6 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 12.9× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 35.7 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.49× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 62.2 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.14× (z +10.9) | [[Lonafarnib (drug)]] 5 µM 0.0760× (z -10.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 71.2 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.25× (z +9.9) | [[Allantoin (drug)]] 0.5 µM 0.321× (z -9.5) |
| [[SW1417 (line)]] | alt | 116 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.78× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 9.90 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +11.7) | — |
| [[LoVo (line)]] | wt | 30.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 23.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.13× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.05× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 21.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +14.3) | — |
| [[NCI-H460 (line)]] | wt | 53.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +10.8) | — |
| [[SW480 (line)]] | alt | 119 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.99× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.24× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 6.83 | 2 | 0 | [[Belinostat (drug)]] 5 µM 9.14× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 8.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 44.7 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.188× (z -9.1) |
| [[COLO 205 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +11.4) | — |
| [[A-172 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORBS1]] | +0.58 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[MAN1A1]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PPP2R2B]] | +0.53 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ABCD3]] | +0.52 | +0.37 / +0.60 | both halves | 7e-05 |  |
| [[ADD3]] | +0.52 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[TNFRSF19]] | +0.52 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[GXYLT2]] | +0.49 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[PRKD1]] | +0.48 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[SLC25A27]] | +0.45 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[CA8]] | +0.45 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[CAT]] | +0.44 | +0.12 / +0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[LMCD1]] | +0.44 | +0.32 / +0.42 | both halves | 1e-04 |  |
| [[MEX3B]] | +0.43 | +0.37 / +0.48 | both halves | 8e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 23 of them with an alert (⚠; 23 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIPIN]] | -0.51 | -0.28 / -0.32 | both halves | 3e-04 |  |
| [[MRM1]] | -0.50 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[ZNF324B]] | -0.50 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[C1orf109]] | -0.49 | -0.15 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[RPUSD2]] | -0.47 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[MYH3]] | -0.47 | -0.18 / -0.31 | ⚠ not reproduced | 1e-03 |  |
| [[RPSAP52]] | -0.46 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[DDX51]] | -0.44 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[TMEM186]] | -0.44 | -0.16 / -0.26 | ⚠ not reproduced | 0.001 |  |
| [[TIMM23B-AGAP6]] | -0.43 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[ZNF623]] | -0.42 | -0.22 / -0.39 | both halves | 6e-04 |  |
| [[PALB2]] | -0.42 | -0.14 / -0.42 | ⚠ not reproduced | 0.002 |  |
| [[ZNF696]] | -0.42 | -0.24 / -0.40 | both halves | 4e-04 |  |
| [[USP36]] | -0.42 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[TRMT44]] | -0.41 | -0.27 / -0.33 | both halves | 3e-04 |  |
| [[AGAP6]] | -0.39 | -0.21 / -0.28 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPYSL3]] | B | DPYSL3 activity raises SESN3's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 2.46× lower at baseline in the lines without DPYSL3 | 0.024 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[PPP2R2B]] | B | PPP2R2B activity raises SESN3's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without PPP2R2B | 0.025 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SESN3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADD3]] | B | ADD3 activity raises SESN3's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 3.18× lower at baseline in the lines without ADD3 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPYSL3]] | B | SESN3 activity raises DPYSL3's level | lines that do not express SESN3 (20) vs lines expressing it (30) | 3.03× lower at baseline in the lines without SESN3 | 0.032 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent |
| [[PGM2L1]] | B | SESN3 activity raises PGM2L1's level | lines that do not express SESN3 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without SESN3 | 0.049 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent |
| [[OVGP1]] | B | SESN3 activity lowers OVGP1's level | lines that do not express SESN3 (20) vs lines expressing it (30) | 1.13× higher at baseline in the lines without SESN3 | 0.087 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent |
| [[SCO1]] | B | SESN3 activity lowers SCO1's level | lines that do not express SESN3 (20) vs lines expressing it (30) | 1.21× higher at baseline in the lines without SESN3 | 0.094 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent |
| [[DHX34]] | B | SESN3 activity strengthens DHX34's drug response | lines that do not express SESN3 (20) vs lines expressing it (29) | the lines without SESN3 respond 0.72× as strongly (z diff +1.16); strongest at Homoharringtonine 5 µM: 1.40x vs 1.82x (z diff +3.0) | 0.099 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MAN1A1]] | C | SESN3 activity raises MAN1A1's level | lines that do not express SESN3 (20) vs lines expressing it (30) | 3.21× lower at baseline in the lines without SESN3 | 0.041 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.310). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.1, 43.7); signed map (35.3, 34.2). **Vector** length 65.0, 12.7% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +22.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +14.5 |
|  | [[NG25 (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +24.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +7.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +12.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | sestrin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:95,165,513-95,232,541 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEST3, MGC29667 |
| Gene groups (HGNC) | Sestrin family |
| Reactome | 2 pathways, smallest: TP53 Regulates Metabolic Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [P58005](https://www.uniprot.org/uniprotkb/P58005) (Sestrin-3):

> May function as an intracellular leucine sensor that negatively regulates the TORC1 signaling pathway. May also regulate the insulin-receptor signaling pathway through activation of TORC2 (By similarity). This metabolic regulator may also play a role in protection against oxidative and genotoxic stresses (By similarity). May prevent the accumulation of reactive oxygen species (ROS) through the alkylhydroperoxide reductase activity born by the N-terminal domain of the protein (By similarity).

**Summary**, from NCBI Gene [143686](https://www.ncbi.nlm.nih.gov/gene/143686):

> This gene encodes a member of the sestrin family of stress-induced proteins. The encoded protein reduces the levels of intracellular reactive oxygen species induced by activated Ras downstream of RAC-alpha serine/threonine-protein kinase (Akt) and FoxO transcription factor. The protein is required for normal regulation of blood glucose, insulin resistance and plays a role in lipid storage in obesity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:23060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23060) · Entrez [143686](https://www.ncbi.nlm.nih.gov/gene/143686) · UniProt [P58005](https://www.uniprot.org/uniprotkb/P58005) · Ensembl [ENSG00000149212](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149212)

## Data

Gene col 7350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7350); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7350]; `tensor/DDL_lfc|DDL_z.npy` [7350]; `embed/gene_vectors.npy` [7350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7350 or target_col == 7350). Every well: [[SESN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SESN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

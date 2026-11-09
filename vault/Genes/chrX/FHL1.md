---
symbol: "FHL1"
type: "gene"
col: 332
ensembl_id: "ENSG00000022267"
name: "four and a half LIM domains 1"
location: "Xq26.3"
module: 132
arm: "+"
pooled_cpm: 15.91
n_lines_expressing: 31
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 10
direction_downstream: 19
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# FHL1

*four and a half LIM domains 1* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.65× (z +17.5, q 0e+00, up in 18 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.63× (z +12.4, q 8e-33, up in 21 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.448× (z -20.3, q 0e+00, down in 19 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNB5]] (+0.64, fdr 1e-05), [[PRKAR2B]] (+0.60, fdr 1e-04), [[F2R]] (+0.60, fdr 1e-05); moves opposite to [[GTF2IRD2B]] (-0.52, fdr 2e-05), [[SYNRG]] (-0.50, fdr 3e-05), [[RPP38]] (-0.49, fdr 4e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SCD5]] → it (grade B ⚠); 19 go from it, the strongest it → [[F2R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +17.5 | 0e+00 | 18/25 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +13.6 | 8e-40 | 12/17 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +12.4 | 8e-33 | 21/29 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +10.8 | 5e-25 | 21/29 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +8.7 | 3e-16 | 14/21 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.005 | 9/28 (SW480, Hs 766T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.010 | 7/29 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.8 | 0.011 | 7/29 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.055 | 6/28 (C-33 A, SW480, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.071 | 7/28 (NCI-H2030, Panc 03.27, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.083 | 3/16 (HOP62, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | 1.38× | +3.0 | 0.11 | 2/28 (A549, NCI-H2030) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 332.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.448×** | -20.3 | 0e+00 | 19/26 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.437×** | -14.8 | 0e+00 | 19/26 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.612×** | -8.8 | 3e-16 | 17/28 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.613×** | -8.4 | 5e-15 | 16/29 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -8.1 | 8e-14 | 17/29 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -7.2 | 4e-11 | 13/29 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -6.6 | 3e-09 | 13/27 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -6.4 | 1e-08 | 17/28 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.715×** | -5.8 | 5e-07 | 12/26 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.734×** | -5.5 | 2e-06 | 13/29 (NCI-H2030, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.771×** | -4.7 | 1e-04 | 15/28 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.764×** | -4.6 | 1e-04 | 8/28 (NCI-H23, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.772×** | -4.6 | 1e-04 | 12/29 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.784×** | -4.4 | 5e-04 | 11/29 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.782×** | -4.1 | 0.002 | 8/27 (SNU-1, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.855× | -4.0 | 0.002 | 3/29 (NCI-H1792, H4, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -3.9 | 0.003 | 11/29 (NCI-H2030, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 119 | 1 (1 ⚠) | 10 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -24.0) |
| [[HS-578T (line)]] | alt | 92.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.56× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.9) | — |
| [[SW480 (line)]] | alt | 10.4 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.17× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -11.6) |
| [[A-427 (line)]] | wt | 25.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -16.4) |
| [[NCI-H2030 (line)]] | alt | 55.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -15.1) |
| [[SW 1271 (line)]] | alt | 193 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -13.3) |
| [[H4 (line)]] | wt | 52.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -19.8) |
| [[HOP62 (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -13.0) |
| [[Hs 766T (line)]] | wt | 78.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -18.0) |
| [[A498 (line)]] | wt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0901× (z -9.1) |
| [[CHP-212 (line)]] | wt | 74.7 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0853× (z -12.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.8) |
| [[PANC-1 (line)]] | alt | 11.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.41× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.8) |
| [[SW 900 (line)]] | alt | 9.84 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -8.9) |
| [[A-172 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB5]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PRKAR2B]] | +0.60 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[F2R]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[VASH1]] | +0.59 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PAPSS1]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TMEM170B]] | +0.56 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ANXA6]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TMOD2]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[EHD3]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PTPRS]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[NRG2]] | +0.54 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ADAM22]] | +0.52 | +0.39 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2B]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SYNRG]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[RPP38]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[RBX1]] | -0.49 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[GGA3]] | -0.49 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[PSMB10]] | -0.49 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[PDCD7]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ZNF785]] | -0.47 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[UNK]] | -0.47 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[LINS1]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[DOHH]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TOPORS]] | -0.47 | -0.44 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCD5]] | B | SCD5 activity raises FHL1's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 3.69× lower at baseline in the lines without SCD5 | 0.026 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[UNC13A]] | B | UNC13A activity raises FHL1's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 2.01× lower at baseline in the lines without UNC13A | 0.083 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises FHL1's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MCOLN2]] | B | MCOLN2 activity raises FHL1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.08× lower at baseline in the lines without MCOLN2 | 0.089 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[NRG2]] | C | NRG2 activity raises FHL1's level | lines that do not express NRG2 (15) vs lines expressing it (35) | 4.56× lower at baseline in the lines without NRG2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B; co-absent with the target |
| [[VASH1]] | C | VASH1 activity raises FHL1's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 4.41× lower at baseline in the lines without VASH1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises FHL1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 3.50× lower at baseline in the lines without PDZD4 | 0.035 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |
| [[JCAD]] | C | JCAD activity raises FHL1's level | lines that do not express JCAD (20) vs lines expressing it (30) | 4.58× lower at baseline in the lines without JCAD | 0.079 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1; co-absent with the target |
| [[CDH4]] | C | CDH4 activity raises FHL1's level | lines that do not express CDH4 (32) vs lines expressing it (18) | 3.07× lower at baseline in the lines without CDH4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, UCHL1, SIRLNT; co-absent with the target |
| [[LDOC1]] | C | LDOC1 activity raises FHL1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 4.09× lower at baseline in the lines without LDOC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 13, C 6. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2R]] | B | FHL1 activity raises F2R's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 3.27× lower at baseline in the lines without FHL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[ANXA6]] | B | FHL1 activity raises ANXA6's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 3.26× lower at baseline in the lines without FHL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[CRTAP]] | B | FHL1 activity raises CRTAP's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without FHL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[NDRG3]] | B | FHL1 activity raises NDRG3's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 1.40× lower at baseline in the lines without FHL1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| cells under [[Naproxen (drug)]] 5 µM | B | FHL1 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express FHL1 (19) vs lines expressing it (29) | the lines without FHL1: 0.86× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[TOX2]] | B | FHL1 activity raises TOX2's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.68× lower at baseline in the lines without FHL1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[ALDH7A1]] | B | FHL1 activity raises ALDH7A1's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 1.50× lower at baseline in the lines without FHL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[PRSS23-AS1]] | B | FHL1 activity raises PRSS23-AS1's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.11× lower at baseline in the lines without FHL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[TSPAN13]] | B | FHL1 activity lowers TSPAN13's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.07× higher at baseline in the lines without FHL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[SCARA3]] | B | FHL1 activity raises SCARA3's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without FHL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | FHL1 activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express FHL1 (19) vs lines expressing it (29) | the lines without FHL1: 0.87× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[COLGALT1]] | B | FHL1 activity raises COLGALT1's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without FHL1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.5, 38.8); signed map (24.0, 31.1). **Vector** length 67.9, 14.5% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +17.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -14.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -5.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | four and a half LIM domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:136,146,702-136,211,359 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLIM1, KYO-T, bA535K18.1, FHL1B, XMPMA, FLH1A, MGC111107 |
| Gene groups (HGNC) | LIM domain containing |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13642](https://www.uniprot.org/uniprotkb/Q13642) (Four and a half LIM domains protein 1):

> May have an involvement in muscle development or hypertrophy.

**Summary**, from NCBI Gene [2273](https://www.ncbi.nlm.nih.gov/gene/2273):

> This gene encodes a member of the four-and-a-half-LIM-only protein family. Family members contain two highly conserved, tandemly arranged, zinc finger domains with four highly conserved cysteines binding a zinc atom in each zinc finger. Expression of these family members occurs in a cell- and tissue-specific mode and these proteins are involved in many cellular processes. Mutations in this gene have been found in patients with Emery-Dreifuss muscular dystrophy. Multiple alternately spliced …

**Accessions** — [HGNC:3702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3702) · Entrez [2273](https://www.ncbi.nlm.nih.gov/gene/2273) · UniProt [Q13642](https://www.uniprot.org/uniprotkb/Q13642) · Ensembl [ENSG00000022267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000022267)

## Data

Gene col 332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 332); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 332]; `tensor/DDL_lfc|DDL_z.npy` [332]; `embed/gene_vectors.npy` [332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 332 or target_col == 332). Every well: [[FHL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

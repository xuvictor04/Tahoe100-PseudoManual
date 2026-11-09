---
symbol: "CGN"
type: "gene"
col: 6728
ensembl_id: "ENSG00000143375"
name: "cingulin"
location: "1q21.3"
module: 44
arm: "+"
pooled_cpm: 19.44
n_lines_expressing: 29
n_dd_up: 30
n_dd_down: 15
n_dd_up_clean: 27
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 51
direction_downstream: 53
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CGN

*cingulin* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.44× (z +17.7, q 0e+00, up in 19 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.591× (z -7.0, q 1e-09, down in 17 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TJP3]] (+0.67, fdr 7e-06), [[AMOT]] (+0.67, fdr 7e-06), [[HHLA2]] (+0.66, fdr 1e-05); moves opposite to [[TIMM23B-AGAP6]] (-0.57, fdr 3e-05), [[MCM9]] (-0.55, fdr 1e-05), [[EEF1AKMT1]] (-0.53, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 51 arrows point to it, the strongest [[ALOX5]] → it (grade B ⚠); 53 go from it, the strongest it → [[TRAF4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.44×** | +17.7 | 0e+00 | 19/26 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.39×** | +17.3 | 0e+00 | 22/27 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.76×** | +14.2 | 1e-43 | 21/27 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.64×** | +13.6 | 3e-40 | 21/27 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.61×** | +13.0 | 2e-36 | 21/26 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +11.6 | 3e-29 | 18/27 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +10.5 | 7e-24 | 20/27 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +9.7 | 3e-20 | 21/27 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +7.7 | 8e-13 | 16/26 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +6.8 | 6e-10 | 15/25 (LS 180, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.44×** | +6.6 | 3e-09 | 17/28 (NCI-H2030, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.55×** | +5.7 | 5e-07 | 13/24 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 8e-07 | 14/27 (AsPC-1, NCI-H1573, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.0 | 2e-05 | 9/24 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +4.8 | 5e-05 | 14/26 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +4.7 | 8e-05 | 13/26 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.591×** | -7.0 | 1e-09 | 17/26 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.611×** | -6.9 | 1e-09 | 18/27 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.620×** | -6.7 | 4e-09 | 17/27 (COLO 205, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.647×** | -6.1 | 2e-07 | 15/26 (HT-29, CFPAC-1, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.482×** | -5.3 | 1e-05 | 13/21 (SW1417, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.520×** | -4.8 | 2e-04 | 15/25 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.699×** | -4.7 | 2e-04 | 13/25 (SW1417, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.714×** | -4.7 | 2e-04 | 12/27 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.756×** | -3.8 | 0.011 | 7/26 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.832×** | -3.6 | 0.016 | 11/28 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.619×** | -3.5 | 0.023 | 11/28 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.786×** | -3.4 | 0.035 | 8/28 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.801×** | -3.1 | 0.086 | 6/27 (AsPC-1, A-427, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.798×** | -3.0 | 0.091 | 13/24 (HT-29, COLO 205, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.661×** | -3.0 | 0.091 | 5/27 (C-33 A, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 62.9 | 4 | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.06× (z +11.6) | [[Ixazomib citrate (drug)]] 5 µM 0.321× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 76.5 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.5) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.310× (z -11.2) |
| [[COLO 205 (line)]] | alt | 114 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0674× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.131× (z -17.7) |
| [[HT-29 (line)]] | alt | 87.1 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.173× (z -15.4) |
| [[LoVo (line)]] | wt | 38.8 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 5.19× (z +12.5) | [[Bortezomib (drug)]] 0.05 µM 0.192× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 70.2 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 27.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +15.5) | — |
| [[NCI-H1573 (line)]] | alt | 33.2 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.174× (z -11.1) |
| [[SW1417 (line)]] | alt | 45.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.8) | [[Bortezomib (drug)]] 5 µM 0.157× (z -8.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 5.00 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 25.3 | 1 | 1 | [[Trametinib (drug)]] 0.5 µM 3.98× (z +9.2) | [[Auranofin (drug)]] 5 µM 0.159× (z -10.3) |
| [[BT-474 (line)]] | alt | 16.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 9.72 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.68× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.180× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 13.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -8.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 4.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +9.2) | — |
| [[KATO III (line)]] | alt | 53.3 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.77× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 27.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.63× (z +9.1) | — |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP3]] | +0.67 | +0.58 / +0.74 | both halves | 7e-06 | STRING 997 |
| [[AMOT]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 | STRING 475 |
| [[HHLA2]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[TSPAN15]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ATP8B1]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[RHOV]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[RSPH1]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PLEKHG6]] | +0.63 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | +0.62 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[CXADR]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[CTNND1]] | +0.61 | +0.44 / +0.54 | both halves | 3e-05 | STRING 433 |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[MCM9]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[EEF1AKMT1]] | -0.53 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[TRAPPC12]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PSMB5]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[FBXW11]] | -0.50 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[GHRLOS]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 19, C 32. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALOX5]] | B | ALOX5 activity raises CGN's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 3.29× lower at baseline in the lines without ALOX5 | 0.010 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[CXADR]] | B | CXADR activity raises CGN's level | lines that do not express CXADR (16) vs lines expressing it (34) | 3.97× lower at baseline in the lines without CXADR | 0.011 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[MMP7]] | B | MMP7 activity raises CGN's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 3.21× lower at baseline in the lines without MMP7 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises CGN's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 3.67× lower at baseline in the lines without PDZK1IP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[CDC42BPG]] | B | CDC42BPG activity raises CGN's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 3.81× lower at baseline in the lines without CDC42BPG | 0.016 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[SLC40A1]] | B | SLC40A1 activity raises CGN's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 3.09× lower at baseline in the lines without SLC40A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[ANO9]] | B | ANO9 activity raises CGN's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without ANO9 | 0.024 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[RAB17]] | B | RAB17 activity raises CGN's level | lines that do not express RAB17 (22) vs lines expressing it (28) | 3.08× lower at baseline in the lines without RAB17 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MAL2, TNNT2, BSPRY |
| [[MMP7]] | B | MMP7 activity weakens CGN's drug response | lines that do not express MMP7 (21) vs lines expressing it (7) | the lines without MMP7 respond 1.46× as strongly (z diff -1.35); strongest at Belinostat 5 µM: 2.38x vs 0.99x (z diff -4.7) | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; target measured in part of the lines; artifact flags |
| [[CRACR2B]] | B | CRACR2B activity raises CGN's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 3.95× lower at baseline in the lines without CRACR2B | 0.037 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[SCIN]] | B | SCIN activity raises CGN's level | lines that do not express SCIN (22) vs lines expressing it (28) | 3.22× lower at baseline in the lines without SCIN | 0.037 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[DAPK2]] | B | DAPK2 activity raises CGN's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 4.90× lower at baseline in the lines without DAPK2 | 0.039 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 28, C 25. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAF4]] | B | CGN activity raises TRAF4's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.62× lower at baseline in the lines without CGN | 0.006 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[CDC42BPG]] | B | CGN activity raises CDC42BPG's level | lines that do not express CGN (21) vs lines expressing it (29) | 3.31× lower at baseline in the lines without CGN | 0.008 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[RAB17]] | B | CGN activity raises RAB17's level | lines that do not express CGN (21) vs lines expressing it (29) | 3.12× lower at baseline in the lines without CGN | 0.008 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[BIK]] | B | CGN activity raises BIK's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.86× lower at baseline in the lines without CGN | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[FZD5]] | B | CGN activity raises FZD5's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.39× lower at baseline in the lines without CGN | 0.013 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[CXADR]] | B | CGN activity raises CXADR's level | lines that do not express CGN (21) vs lines expressing it (29) | 4.52× lower at baseline in the lines without CGN | 0.013 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[TUFT1]] | B | CGN activity raises TUFT1's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without CGN | 0.016 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[MAP3K1]] | B | CGN activity raises MAP3K1's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without CGN | 0.019 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[USP2]] | B | CGN activity raises USP2's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without CGN | 0.025 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[PRXL2B]] | B | CGN activity raises PRXL2B's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.56× lower at baseline in the lines without CGN | 0.030 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[SCIN]] | B | CGN activity raises SCIN's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without CGN | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[ALOX5]] | B | CGN activity raises ALOX5's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without CGN | 0.045 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.7, 1.5); signed map (49.3, 5.5). **Vector** length 93.1, 26.7% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +17.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +13.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +5.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.2 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | cingulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,510,510-151,538,692 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1319 |
| Reactome | 3 pathways, smallest: TGF-beta receptor signaling in EMT (epithelial to mesenchymal transition); Signaling by TGF-beta Receptor Complex; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2M7](https://www.uniprot.org/uniprotkb/Q9P2M7) (Cingulin):

> Probably plays a role in the formation and regulation of the tight junction (TJ) paracellular permeability barrier.

**Summary**, from NCBI Gene [57530](https://www.ncbi.nlm.nih.gov/gene/57530):

> Enables cadherin binding activity. Predicted to be involved in microtubule cytoskeleton organization. Predicted to act upstream of or within bicellular tight junction assembly and epithelial cell morphogenesis. Located in bicellular tight junction and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17429) · Entrez [57530](https://www.ncbi.nlm.nih.gov/gene/57530) · UniProt [Q9P2M7](https://www.uniprot.org/uniprotkb/Q9P2M7) · Ensembl [ENSG00000143375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143375)

## Data

Gene col 6728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6728); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6728]; `tensor/DDL_lfc|DDL_z.npy` [6728]; `embed/gene_vectors.npy` [6728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6728 or target_col == 6728). Every well: [[CGN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CGN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

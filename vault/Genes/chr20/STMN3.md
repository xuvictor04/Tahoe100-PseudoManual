---
symbol: "STMN3"
type: "gene"
col: 12401
ensembl_id: "ENSG00000197457"
name: "stathmin 3"
location: "20q13.33"
module: 78
arm: "+"
pooled_cpm: 15.46
n_lines_expressing: 37
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# STMN3

*stathmin 3* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.62× (z +15.2, q 0e+00, up in 25 of 26 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +7.5, q 8e-12, up in 13 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.461× (z -8.2, q 1e-13, down in 27 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA3]] (+0.73, fdr 7e-06), [[TSPAN4]] (+0.70, fdr 7e-06), [[MAP2K3]] (+0.65, fdr 7e-06); moves opposite to [[KEAP1]] (-0.51, fdr 3e-05), [[PSMB5]] (-0.50, fdr 5e-05), [[SNX13]] (-0.49, fdr 5e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.62×** | +15.2 | 0e+00 | 25/26 (SW480, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +14.7 | 0e+00 | 17/18 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +9.6 | 2e-19 | 18/20 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.63×** | +8.2 | 4e-14 | 15/32 (HOP62, LOX-IMVI, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.5 | 8e-12 | 13/33 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +6.0 | 1e-07 | 17/30 (HOP62, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.4 | 5e-06 | 14/35 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.57×** | +5.3 | 9e-06 | 10/30 (SW1417, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.5 | 5e-04 | 9/35 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.1 | 0.002 | 12/35 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.8 | 0.006 | 8/25 (MIA PaCa-2, LS 180, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.8 | 0.006 | 4/14 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.37×** | +3.7 | 0.009 | 9/35 (KATO III, C32, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.036 | 8/34 (LS 180, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.32×** | +3.2 | 0.045 | 7/34 (C32, NCI-H1792, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.074 | 5/30 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.095 | 7/30 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.461×** | -8.2 | 1e-13 | 27/35 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.616×** | -5.8 | 2e-06 | 20/34 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.397×** | -5.2 | 3e-05 | 21/33 (MIA PaCa-2, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -5.0 | 9e-05 | 16/34 (KATO III, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.658×** | -4.9 | 1e-04 | 14/35 (MIA PaCa-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.728×** | -3.8 | 0.015 | 14/34 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.724×** | -3.7 | 0.017 | 14/34 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.802×** | -3.5 | 0.028 | 15/35 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.812×** | -3.4 | 0.039 | 13/35 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.755×** | -3.4 | 0.041 | 14/34 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.755×** | -3.4 | 0.041 | 15/35 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.558×** | -3.3 | 0.045 | 8/34 (MIA PaCa-2, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.743×** | -3.3 | 0.045 | 14/34 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.770×** | -3.1 | 0.075 | 11/34 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.794×** | -3.1 | 0.085 | 10/35 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 82.1 | 2 (2 ⚠) | 13 (7 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -19.8) |
| [[SW1417 (line)]] | alt | 85.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.21× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.112× (z -10.9) |
| [[KATO III (line)]] | alt | 20.0 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.132× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 9.81 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 15.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 5.65 | 0 | 2 (1 ⚠) | — | [[Radotinib (drug)]] 0.5 µM 0.0792× (z -8.9) |
| [[LoVo (line)]] | wt | 5.42 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.111× (z -9.1) |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0799× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA3]] | +0.73 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN4]] | +0.70 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[MAP2K3]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SLCO4A1]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[TNFRSF6B]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 | ⚠ same locus (39.0 kb: neighbours can correlate without regulation) |
| [[SPRY4]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[PLEC]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LAPTM5]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LTBP3]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PODXL]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CD82]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[HPCAL1]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CCND1]] | +0.57 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KEAP1]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[PSMB5]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SNX13]] | -0.49 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[FTL]] | -0.48 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[LURAP1L]] | -0.48 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[PIR]] | -0.47 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[DNAJB4]] | -0.47 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[SPART]] | -0.47 | -0.38 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises STMN3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SPART]] | B | SPART activity lowers STMN3's level | lines that do not express SPART (15) vs lines expressing it (35) | 1.58× higher at baseline in the lines without SPART | 0.095 | ⚠ within organs, on part of the lines; also absent: CCDC169, SPART-AS1, FIGN |
| [[RGS17]] | B | RGS17 activity lowers STMN3's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 1.66× higher at baseline in the lines without RGS17 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.7, 1.7); signed map (6.2, 52.0). **Vector** length 66.6, 13.1% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.3 | +15.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.1 | +0.9 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.0 | +1.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.6 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -5.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.4 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | stathmin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,639,705-63,657,682 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCLIP |
| Gene groups (HGNC) | Stathmins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ72](https://www.uniprot.org/uniprotkb/Q9NZ72) (Stathmin-3):

> Exhibits microtubule-destabilizing activity, which is antagonized by STAT3.

**Summary**, from NCBI Gene [50861](https://www.ncbi.nlm.nih.gov/gene/50861):

> This gene encodes a protein which is a member of the stathmin protein family. Members of this protein family form a complex with tubulins at a ratio of 2 tubulins for each stathmin protein. Microtubules require the ordered assembly of alpha- and beta-tubulins, and formation of a complex with stathmin disrupts microtubule formation and function. A pseudogene of this gene is located on chromosome 22. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:15926](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15926) · Entrez [50861](https://www.ncbi.nlm.nih.gov/gene/50861) · UniProt [Q9NZ72](https://www.uniprot.org/uniprotkb/Q9NZ72) · Ensembl [ENSG00000197457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197457)

## Data

Gene col 12401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12401); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12401]; `tensor/DDL_lfc|DDL_z.npy` [12401]; `embed/gene_vectors.npy` [12401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12401 or target_col == 12401). Every well: [[STMN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STMN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

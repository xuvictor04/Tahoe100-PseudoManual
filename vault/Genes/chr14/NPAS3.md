---
symbol: "NPAS3"
type: "gene"
col: 7506
ensembl_id: "ENSG00000151322"
name: "neuronal PAS domain protein 3"
location: "14q13.1"
module: 10
arm: "+"
pooled_cpm: 45.01
n_lines_expressing: 34
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 9
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# NPAS3

*neuronal PAS domain protein 3* — 14q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.55× (z +23.0, q 0e+00, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.578× (z -7.0, q 1e-09, down in 23 of 32 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.611× (z -6.0, q 3e-07, down in 22 of 32 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO38-DT]] (+0.74, fdr 2e-05), [[KCNMB2-AS1]] (+0.71, fdr 1e-05), [[DKK2]] (+0.70, fdr 7e-06); moves opposite to [[CCDC134]] (-0.57, fdr 6e-05), [[YIF1B]] (-0.55, fdr 0.002, ⚠ one half only (not replicated)), [[SMYD4]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[GLI3]] → it (grade B ⚠); 9 go from it, the strongest it → [[FBXO38-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.55×** | +23.0 | 0e+00 | 27/32 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +9.9 | 8e-21 | 12/26 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +8.0 | 3e-13 | 23/32 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +7.4 | 2e-11 | 14/32 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.3 | 4e-08 | 16/30 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +6.2 | 4e-08 | 9/23 (LoVo, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +5.5 | 3e-06 | 12/32 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.5 | 3e-06 | 10/25 (LoVo, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.0 | 4e-05 | 12/33 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.002 | 12/31 (A498, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.003 | 16/30 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.004 | 12/32 (SK-MEL-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.016 | 5/31 (HCT15, CFPAC-1, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +3.4 | 0.023 | 11/32 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.023 | 12/32 (A498, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.066 | 12/32 (NCI-H2030, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7506.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.578×** | -7.0 | 1e-09 | 23/32 (C-33 A, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.613×** | -6.3 | 1e-07 | 21/30 (SW480, C-33 A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.603×** | -6.2 | 1e-07 | 20/32 (C-33 A, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.611×** | -6.0 | 3e-07 | 22/32 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.656×** | -5.4 | 8e-06 | 17/32 (C-33 A, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.677×** | -5.0 | 6e-05 | 16/31 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -4.7 | 2e-04 | 14/32 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.696×** | -4.5 | 6e-04 | 19/30 (C-33 A, SW 900, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.720×** | -4.2 | 0.002 | 18/32 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.731×** | -4.0 | 0.003 | 12/30 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -4.0 | 0.003 | 20/31 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.748×** | -3.6 | 0.018 | 5/32 (NCI-H2030, H4, …) | top dose only | plate-row cell shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.765×** | -3.3 | 0.045 | 10/32 (AN3 CA, HOP62, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.787×** | -3.0 | 0.093 | 15/32 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 94.4 | 0 | 15 (10 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.108× (z -14.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.187× (z -10.5) |
| [[C-33 A (line)]] | alt | 1,125 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0618× (z -20.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -19.8) |
| [[A498 (line)]] | wt | 19.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.38× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +22.6) | — |
| [[H4 (line)]] | wt | 72.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 26.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +10.0) | — |
| [[LoVo (line)]] | wt | 14.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +21.8) | — |
| [[NCI-H23 (line)]] | alt | 21.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 256 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -9.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW 900 (line)]] | alt | 43.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.121× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 58.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.6) | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0912× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 51.7 | 0 | 1 | — | [[Mebendazole (drug)]] 5 µM 0.0943× (z -8.6) |
| [[BT-474 (line)]] | alt | 68.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.86× (z +14.6) | — |
| [[CHP-212 (line)]] | wt | 166 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.297× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0913× (z -9.0) |
| [[HCT15 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 43.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +8.8) | — |
| [[A549 (line)]] | wt | 7.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.94 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 460 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.55 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO38-DT]] | +0.74 | +0.78 / +0.46 | both halves | 2e-05 |  |
| [[KCNMB2-AS1]] | +0.71 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[DKK2]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[FLG-AS1]] | +0.68 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[STPG2]] | +0.67 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[NEB]] | +0.67 | +0.69 / +0.36 | both halves | 1e-04 |  |
| [[GRM8]] | +0.66 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[CFAP418-AS1]] | +0.66 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[RALYL]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[GRID2]] | +0.64 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[SOX2-OT]] | +0.64 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[KIF6]] | +0.64 | +0.67 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC134]] | -0.57 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[YIF1B]] | -0.55 | -0.56 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[SMYD4]] | -0.55 | -0.48 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLI3]] | B | GLI3 activity raises NPAS3's level | lines that do not express GLI3 (19) vs lines expressing it (31) | 2.60× lower at baseline in the lines without GLI3 | 0.012 | ⚠ within organs, on part of the lines; also absent: GPNMB, SLIT2, PRICKLE2 |
| [[LINC02315]] | B | LINC02315 activity raises NPAS3's level | lines that do not express LINC02315 (31) vs lines expressing it (19) | 3.20× lower at baseline in the lines without LINC02315 | 0.012 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1 |
| [[TOP2A]] | B | TOP2A activity lowers NPAS3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HTR2C]] | B | HTR2C activity raises NPAS3's level | lines that do not express HTR2C (22) vs lines expressing it (28) | 3.10× lower at baseline in the lines without HTR2C | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000234156, KCNJ6, PTPRN; maybe low, not absent |
| [[HS3ST5]] | B | HS3ST5 activity raises NPAS3's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 2.66× lower at baseline in the lines without HS3ST5 | 0.029 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[LRRTM4]] | B | LRRTM4 activity strengthens NPAS3's drug response | lines that do not express LRRTM4 (22) vs lines expressing it (11) | the lines without LRRTM4 respond 1.48× as strongly (z diff -0.85); strongest at Panobinostat 0.5 µM: 0.62x vs 0.32x (z diff +3.6) | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973; target measured in part of the lines; both ways; artifact flags |
| [[CSMD3]] | B | CSMD3 activity raises NPAS3's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.24× lower at baseline in the lines without CSMD3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[FGF13]] | B | FGF13 activity raises NPAS3's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 2.57× lower at baseline in the lines without FGF13 | 0.049 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[FAM13C]] | B | FAM13C activity raises NPAS3's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.11× lower at baseline in the lines without FAM13C | 0.073 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO38-DT]] | B | NPAS3 activity raises FBXO38-DT's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without NPAS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[GLI3]] | B | NPAS3 activity raises GLI3's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 4.85× lower at baseline in the lines without NPAS3 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[LINC02315]] | B | NPAS3 activity raises LINC02315's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 3.01× lower at baseline in the lines without NPAS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[ARRDC3-AS1]] | B | NPAS3 activity raises ARRDC3-AS1's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 1.48× lower at baseline in the lines without NPAS3 | 0.061 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[FGF13]] | B | NPAS3 activity raises FGF13's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 3.74× lower at baseline in the lines without NPAS3 | 0.065 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[MAPK10]] | B | NPAS3 activity raises MAPK10's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 2.40× lower at baseline in the lines without NPAS3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[DRAIC]] | B | NPAS3 activity raises DRAIC's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 1.62× lower at baseline in the lines without NPAS3 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[RIMS2]] | B | NPAS3 activity raises RIMS2's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without NPAS3 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[OBSL1]] | B | NPAS3 activity raises OBSL1's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without NPAS3 | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (25.4, 36.2); signed map (37.2, 18.4). **Vector** length 87.3, 22.6% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.3 | +23.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +2.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.5 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.5 | -7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.5 | -6.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.6 | -5.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | neuronal PAS domain protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.1 — chr14:32,934,396-33,820,863 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOP6, PASD6, bHLHe12 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXF0](https://www.uniprot.org/uniprotkb/Q8IXF0) (Neuronal PAS domain-containing protein 3):

> May play a broad role in neurogenesis. May control regulatory pathways relevant to schizophrenia and to psychotic illness (By similarity).

**Summary**, from NCBI Gene [64067](https://www.ncbi.nlm.nih.gov/gene/64067):

> This gene encodes a member of the basic helix-loop-helix and PAS domain-containing family of transcription factors. The encoded protein is localized to the nucleus and may regulate genes involved in neurogenesis. Chromosomal abnormalities that affect the coding potential of this gene are associated with schizophrenia and cognitive disability. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:19311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19311) · Entrez [64067](https://www.ncbi.nlm.nih.gov/gene/64067) · UniProt [Q8IXF0](https://www.uniprot.org/uniprotkb/Q8IXF0) · Ensembl [ENSG00000151322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151322)

## Data

Gene col 7506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7506); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7506]; `tensor/DDL_lfc|DDL_z.npy` [7506]; `embed/gene_vectors.npy` [7506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7506 or target_col == 7506). Every well: [[NPAS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPAS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

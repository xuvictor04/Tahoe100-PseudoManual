---
symbol: "DELEC1"
type: "gene"
col: 10337
ensembl_id: "ENSG00000173077"
name: "deleted in esophageal cancer 1"
location: "9q33.1"
module: 165
arm: "+"
pooled_cpm: 17.94
n_lines_expressing: 44
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 10
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# DELEC1

*deleted in esophageal cancer 1* — 9q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +18.3, q 0e+00, up in 31 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.730× (z -4.8, q 1e-03, down in 9 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HCG20]] (+0.71, fdr 1e-05), [[ATP8A2]] (+0.68, fdr 1e-05), [[DIRC3-AS1]] (+0.67, fdr 7e-06); moves opposite to [[TADA1]] (-0.54, fdr 2e-05).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC02934]] → it (grade B ⚠); 10 go from it, the strongest it → [[RUNX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10337.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +18.3 | 0e+00 | 31/39 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +13.7 | 2e-40 | 31/42 (SW480, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +11.8 | 5e-30 | 21/33 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +11.2 | 5e-27 | 26/39 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +10.6 | 5e-24 | 18/29 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +10.4 | 2e-23 | 21/39 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +10.1 | 3e-22 | 26/42 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +9.4 | 5e-19 | 26/40 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +9.3 | 8e-19 | 14/21 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +8.3 | 8e-15 | 26/39 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 7e-08 | 16/36 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +5.4 | 4e-06 | 14/41 (A498, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.1 | 2e-05 | 11/37 (A549, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.9 | 3e-05 | 11/38 (SK-MEL-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[EX229 (drug)]] 5 µM |  | **1.73×** | +4.3 | 6e-04 | 9/37 (SW480, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.003 | 5/39 (SK-MEL-2, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.006 | 7/38 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.035 | 6/42 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.035 | 11/40 (RKO, SNU-423, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10337.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | **0.730×** | -4.8 | 1e-03 | 9/39 (RKO, C32, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -4.4 | 0.003 | 7/42 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.755×** | -4.3 | 0.004 | 12/39 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.751×** | -4.0 | 0.008 | 9/41 (RKO, HT-29, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.847× | -3.6 | 0.030 | 11/41 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.848× | -3.6 | 0.030 | 12/41 (RKO, SNU-423, …) | two highest doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.791×** | -3.6 | 0.030 | 12/41 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.810×** | -3.2 | 0.096 | 9/40 (LOX-IMVI, SNU-423, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.817× | -3.1 | 0.12 | 11/41 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Asciminib (drug)]] 0.05 µM |  | 0.817× | -3.1 | 0.12 | 8/41 (HCT15, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 422 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -14.9) |
| [[SW480 (line)]] | alt | 11.7 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.29× (z +13.0) | — |
| [[A-172 (line)]] | wt | 13.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.12× (z +11.1) | — |
| [[A498 (line)]] | wt | 5.01 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +11.6) | — |
| [[A549 (line)]] | wt | 4.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.90× (z +10.5) | — |
| [[C32 (line)]] | wt | 28.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.180× (z -9.1) |
| [[COLO 205 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +9.0) | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.100× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HOP62 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.50× (z +9.8) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[J82 (line)]] | alt | 5.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +9.0) | — |
| [[LoVo (line)]] | wt | 8.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +14.7) | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.85× (z +10.2) | — |
| [[SW48 (line)]] | wt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +10.2) | — |
| [[A-427 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCG20]] | +0.71 | +0.53 / +0.68 | both halves | 1e-05 | same gene group |
| [[ATP8A2]] | +0.68 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[DIRC3-AS1]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 | same gene group |
| [[FGF1]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[CCDC26]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 | same gene group |
| [[ZPLD1]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SSUH2]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ALG13]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ELAPOR1]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[PEBP4]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[LINC00513]] | +0.62 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA1]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02934]] | B | LINC02934 activity lowers DELEC1's level | lines that do not express LINC02934 (8) vs lines expressing it (42) | 1.98× higher at baseline in the lines without LINC02934 | 0.017 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CCDC190]] | B | CCDC190 activity raises DELEC1's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 1.61× lower at baseline in the lines without CCDC190 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[ROBO4]] | B | ROBO4 activity raises DELEC1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without ROBO4 | 0.028 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[IL13RA2]] | B | IL13RA2 activity raises DELEC1's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.01× lower at baseline in the lines without IL13RA2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[TOP2A]] | B | TOP2A activity lowers DELEC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02509]] | B | LINC02509 activity raises DELEC1's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 1.40× lower at baseline in the lines without LINC02509 | 0.038 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2 |
| [[ADTRP]] | B | ADTRP activity raises DELEC1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.39× lower at baseline in the lines without ADTRP | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[KCNIP4]] | B | KCNIP4 activity raises DELEC1's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without KCNIP4 | 0.047 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[MAST4]] | B | MAST4 activity raises DELEC1's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without MAST4 | 0.089 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[DIRC3-AS1]] | C | DIRC3-AS1 activity raises DELEC1's level | lines that do not express DIRC3-AS1 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without DIRC3-AS1 | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC00298, LYG1, IQCM; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUNX1]] | B | DELEC1 activity raises RUNX1's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without DELEC1 | 0.003 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[CXCL8]] | B | DELEC1 activity raises CXCL8's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 6.46× lower at baseline in the lines without DELEC1 | 0.005 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[LIF]] | B | DELEC1 activity raises LIF's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 3.21× lower at baseline in the lines without DELEC1 | 0.007 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[LUCAT1]] | B | DELEC1 activity raises LUCAT1's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 3.41× lower at baseline in the lines without DELEC1 | 0.033 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[SNX9]] | B | DELEC1 activity raises SNX9's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without DELEC1 | 0.039 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[BACH1]] | B | DELEC1 activity raises BACH1's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without DELEC1 | 0.071 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[LINC01426]] | B | DELEC1 activity raises LINC01426's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without DELEC1 | 0.093 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[PSMG2]] | B | DELEC1 activity lowers PSMG2's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without DELEC1 | 0.094 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[FHL2]] | B | DELEC1 activity raises FHL2's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without DELEC1 | 0.099 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[IER3]] | C | DELEC1 activity raises IER3's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 4.20× lower at baseline in the lines without DELEC1 | 0.015 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.4, 11.3); signed map (26.0, 36.2). **Vector** length 79.1, 14.7% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +18.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +10.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | deleted in esophageal cancer 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q33.1 — chr9:114,850,968-115,402,644 (+) |
| Ensembl biotype | lncRNA |
| Also known as | CTS9; previously DEC1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2X7](https://www.uniprot.org/uniprotkb/Q9P2X7) (Deleted in esophageal cancer 1):

> Candidate tumor suppressor.

**Summary**, from NCBI Gene [50514](https://www.ncbi.nlm.nih.gov/gene/50514):

> The function of this gene is not known. This gene is located in a region commonly deleted in esophageal squamous cell carcinomas. Gene expression is reduced or absent in these carcinomas and thus this is a candidate tumor suppressor gene for esophageal squamous cell carcinomas. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23658) · Entrez [50514](https://www.ncbi.nlm.nih.gov/gene/50514) · UniProt [Q9P2X7](https://www.uniprot.org/uniprotkb/Q9P2X7) · Ensembl [ENSG00000173077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173077)

## Data

Gene col 10337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10337); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10337]; `tensor/DDL_lfc|DDL_z.npy` [10337]; `embed/gene_vectors.npy` [10337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10337 or target_col == 10337). Every well: [[DELEC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DELEC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

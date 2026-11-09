---
symbol: "UNC13A"
type: "gene"
col: 5069
ensembl_id: "ENSG00000130477"
name: "unc-13 homolog A"
location: "19p13.11"
module: 34
arm: "+"
pooled_cpm: 21.5
n_lines_expressing: 21
n_dd_up: 25
n_dd_down: 16
n_dd_up_clean: 19
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# UNC13A

*unc-13 homolog A* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.05× (z +24.5, q 0e+00, up in 9 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.590× (z -6.5, q 3e-08, down in 11 of 18 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.606× (z -5.8, q 3e-06, down in 9 of 18 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC5D]] (+0.63, fdr 2e-05), [[MMP17]] (+0.62, fdr 3e-05), [[CADM4]] (+0.59, fdr 1e-04); moves opposite to [[CYP27A1]] (-0.49, fdr 1e-04), [[PDCD6IP]] (-0.47, fdr 9e-05), [[DNAI4]] (-0.47, fdr 4e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → [[TMEM170B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.05×** | +24.5 | 0e+00 | 9/19 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.54×** | +22.1 | 0e+00 | 11/19 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **4.86×** | +18.4 | 0e+00 | 10/18 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.84×** | +18.4 | 0e+00 | 10/18 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.04×** | +17.3 | 0e+00 | 12/18 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.25×** | +14.6 | 0e+00 | 9/15 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.07×** | +13.9 | 6e-42 | 10/18 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.16×** | +13.7 | 7e-41 | 8/18 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.70×** | +12.3 | 6e-33 | 13/18 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.50×** | +10.9 | 6e-26 | 5/8 (NCI-H2030, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +9.7 | 2e-20 | 8/18 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +9.4 | 3e-19 | 4/11 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +5.7 | 5e-07 | 14/18 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +5.0 | 3e-05 | 5/17 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.44×** | +4.8 | 7e-05 | 6/19 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.004 | 3/18 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.008 | 3/19 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.015 | 0/18 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5069.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.590×** | -6.5 | 3e-08 | 11/18 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.606×** | -5.8 | 3e-06 | 9/18 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.725×** | -5.6 | 3e-06 | 12/19 (NCI-H460, SNU-1, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM |  | **0.626×** | -5.3 | 2e-05 | 14/19 (NCI-H460, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.676×** | -4.9 | 1e-04 | 11/18 (NCI-H23, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.738×** | -4.6 | 4e-04 | 8/19 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.692×** | -4.6 | 4e-04 | 15/18 (NCI-H460, SNU-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.683×** | -4.5 | 4e-04 | 14/18 (NCI-H460, SNU-1, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.697×** | -4.5 | 4e-04 | 10/18 (C-33 A, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.750×** | -4.5 | 4e-04 | 13/19 (NCI-H460, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.774×** | -4.5 | 4e-04 | 8/19 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.010 | 12/18 (NCI-H460, SNU-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.730×** | -3.7 | 0.010 | 10/18 (A-427, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.817×** | -3.5 | 0.022 | 9/19 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.778×** | -3.1 | 0.069 | 6/18 (NCI-H460, SNU-1, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.791×** | -3.0 | 0.085 | 10/19 (NCI-H460, SNU-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.5 | 0 | 16 (3 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.0947× (z -15.5) |
| [[SNU-1 (line)]] | wt | 206 | 0 | 12 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.266× (z -13.2) |
| [[C-33 A (line)]] | alt | 46.7 | 0 | 8 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -13.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.138× (z -12.6) |
| [[Hs 766T (line)]] | wt | 66.2 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.251× (z -10.1) |
| [[A-172 (line)]] | wt | 6.17 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +15.8) | — |
| [[A-427 (line)]] | wt | 89.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -10.6) |
| [[SW1417 (line)]] | alt | 215 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -18.0) |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +10.8) | — |
| [[C32 (line)]] | wt | 5.83 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0662× (z -8.8) |
| [[LoVo (line)]] | wt | 6.77 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.17× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +9.1) | — |
| [[SW480 (line)]] | alt | 20.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +9.3) | — |
| [[A498 (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.97 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.07 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC5D]] | +0.63 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[MMP17]] | +0.62 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[CADM4]] | +0.59 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[TMEM170B]] | +0.57 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[SCUBE1]] | +0.57 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[EBF2]] | +0.56 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[CCDC68]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[NTSR1]] | +0.55 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SCG2]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[KCNQ2]] | +0.54 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[RTN1]] | +0.53 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CDH4]] | +0.53 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP27A1]] | -0.49 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[PDCD6IP]] | -0.47 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[DNAI4]] | -0.47 | -0.28 / -0.25 | both halves | 4e-04 |  |
| [[DERA]] | -0.47 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[CIAO2A]] | -0.47 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[DDX59]] | -0.46 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[WDFY3]] | -0.46 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[DECR1]] | -0.46 | -0.36 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises UNC13A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises UNC13A's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[RAB3C]] | C | RAB3C activity raises UNC13A's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 2.71× lower at baseline in the lines without RAB3C | 0.042 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[CNKSR2]] | C | CNKSR2 activity raises UNC13A's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 2.31× lower at baseline in the lines without CNKSR2 | 0.066 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |
| [[OLFM1]] | C | OLFM1 activity raises UNC13A's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 2.63× lower at baseline in the lines without OLFM1 | 0.089 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8; co-absent with the target |
| [[LINC02643]] | C | LINC02643 activity raises UNC13A's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 3.93× lower at baseline in the lines without LINC02643 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM170B]] | B | UNC13A activity raises TMEM170B's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 2.51× lower at baseline in the lines without UNC13A | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[FZD4]] | B | UNC13A activity raises FZD4's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without UNC13A | 0.029 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[PRSS23-AS1]] | B | UNC13A activity raises PRSS23-AS1's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.44× lower at baseline in the lines without UNC13A | 0.045 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[PDCD6IP]] | B | UNC13A activity raises PDCD6IP's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.19× lower at baseline in the lines without UNC13A | 0.075 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[SLC4A11]] | B | UNC13A activity raises SLC4A11's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.37× lower at baseline in the lines without UNC13A | 0.082 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[FHL1]] | B | UNC13A activity raises FHL1's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 2.01× lower at baseline in the lines without UNC13A | 0.083 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[ST8SIA4]] | B | UNC13A activity lowers ST8SIA4's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.05× higher at baseline in the lines without UNC13A | 0.095 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[OLFM1]] | C | UNC13A activity raises OLFM1's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without UNC13A | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent; co-absent with the target |
| [[CDH4]] | C | UNC13A activity raises CDH4's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 3.04× lower at baseline in the lines without UNC13A | 0.061 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent; co-absent with the target |
| [[RAB3C]] | C | UNC13A activity raises RAB3C's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 2.03× lower at baseline in the lines without UNC13A | 0.076 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.480). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.5, 33.8); signed map (15.6, 56.6). **Vector** length 63.8, 16.2% of its response variance represented; |z| ≥ 3 in 623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +14.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +22.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.4 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.2 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.4 | -5.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | -4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | unc-13 homolog A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,601,336-17,688,365 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1032, Munc13-1 |
| Gene groups (HGNC) | UNC13 homologs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPW8](https://www.uniprot.org/uniprotkb/Q9UPW8) (Protein unc-13 homolog A):

> Plays a role in vesicle maturation during exocytosis as a target of the diacylglycerol second messenger pathway. Involved in neurotransmitter release by acting in synaptic vesicle priming prior to vesicle fusion and participates in the activity-dependent refilling of readily releasable vesicle pool (RRP). Essential for synaptic vesicle maturation in most excitatory/glutamatergic but not inhibitory/GABA-mediated synapses. Facilitates neuronal dense core vesicles fusion as well as controls the …

**Summary**, from NCBI Gene [23025](https://www.ncbi.nlm.nih.gov/gene/23025):

> This gene encodes a member of the UNC13 family. UNC13 proteins bind to phorbol esters and diacylglycerol and play important roles in neurotransmitter release at synapses. Single nucleotide polymorphisms in this gene may be associated with sporadic amyotrophic lateral sclerosis. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:23150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23150) · Entrez [23025](https://www.ncbi.nlm.nih.gov/gene/23025) · UniProt [Q9UPW8](https://www.uniprot.org/uniprotkb/Q9UPW8) · Ensembl [ENSG00000130477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130477)

## Data

Gene col 5069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5069); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5069]; `tensor/DDL_lfc|DDL_z.npy` [5069]; `embed/gene_vectors.npy` [5069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5069 or target_col == 5069). Every well: [[UNC13A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC13A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

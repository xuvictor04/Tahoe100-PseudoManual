---
symbol: "KPNA2P3"
type: "gene"
col: 15497
ensembl_id: "ENSG00000266820"
name: "karyopherin subunit alpha 2 pseudogene 3"
location: "17q24.1"
module: 34
arm: "+"
pooled_cpm: 6.44
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 18
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# KPNA2P3

*karyopherin subunit alpha 2 pseudogene 3* — 17q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.66× (z +6.3, q 1e-07, up in 17 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.569× (z -7.0, q 1e-09, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP27P1-BPTFP1-KPNA2P3]] (+0.92, fdr 7e-06, ⚠ same locus), [[PLEKHM1P1]] (+0.75, fdr 7e-06, ⚠ same locus), [[ARHGAP27]] (+0.69, fdr 7e-06), [[TMC7]] (+0.66, fdr 7e-06), [[FERMT1]] (+0.66, fdr 7e-06); moves opposite to [[CFAP418]] (-0.57, fdr 3e-05), [[CNTNAP1]] (-0.50, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +6.3 | 1e-07 | 17/46 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.7 | 7e-04 | 3/14 (HT-29, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +3.7 | 0.046 | 2/19 (HT-29, PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.095 | 4/34 (NCI-H23, HT-29, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.29× | +3.2 | 0.13 | 7/46 (LoVo, A-172, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.63× | +3.2 | 0.13 | 3/45 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.28× | +3.1 | 0.15 | 5/39 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.16 | 13/43 (HOP62, SW48, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -7.0 | 1e-09 | 22/36 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.578×** | -6.8 | 2e-09 | 21/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.643×** | -5.5 | 7e-06 | 18/45 (LoVo, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.678×** | -4.8 | 2e-04 | 21/43 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -4.4 | 0.001 | 17/36 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.529×** | -4.2 | 0.003 | 13/32 (LoVo, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.733×** | -3.7 | 0.014 | 14/32 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.807×** | -3.7 | 0.014 | 9/44 (A-427, COLO 205, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.7 | 0.014 | 9/47 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.745×** | -3.7 | 0.014 | 15/43 (NCI-H460, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.583×** | -3.5 | 0.021 | 5/35 (CFPAC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | **0.746×** | -3.5 | 0.021 | 7/41 (COLO 205, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.758×** | -3.4 | 0.025 | 14/44 (AsPC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.803×** | -3.4 | 0.029 | 15/46 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.767×** | -3.3 | 0.035 | 16/44 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.790×** | -3.3 | 0.037 | 12/43 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.606×** | -3.3 | 0.037 | 14/41 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.772×** | -3.2 | 0.039 | 11/45 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.614×** | -3.2 | 0.043 | 9/36 (LoVo, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -3.1 | 0.043 | 12/41 (LoVo, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 3 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.05 µM 0.0499× (z -12.7) |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 11.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -10.2) |
| [[SNU-423 (line)]] | alt | 7.60 | 0 | 2 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0896× (z -8.7) |
| [[SW480 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 7.65 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.205× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~84% of this change |
| [[J82 (line)]] | alt | 4.25 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0782× (z -9.7) |
| [[KATO III (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PLEKHM1P1]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 | ⚠ same locus (26.7 kb, same strand: neighbours can correlate without regulation) |
| [[ARHGAP27]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[TMC7]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RAPGEF3]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[PLEKHM1]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[LSMEM2]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[KLK10]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LEMD1]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[C11orf91]] | +0.63 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.63 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[PLEK2]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PADI1]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP418]] | -0.57 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[CNTNAP1]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises KPNA2P3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 4.8% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TNS4]] | B | TNS4 activity raises KPNA2P3's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 1.86× lower at baseline in the lines without TNS4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[ITGB4]] | B | ITGB4 activity raises KPNA2P3's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without ITGB4 | 0.033 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[TFF2]] | B | TFF2 activity raises KPNA2P3's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.07× lower at baseline in the lines without TFF2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[HSD17B2]] | B | HSD17B2 activity raises KPNA2P3's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without HSD17B2 | 0.034 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[GJB3]] | B | GJB3 activity raises KPNA2P3's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without GJB3 | 0.039 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[CALB1]] | B | CALB1 activity raises KPNA2P3's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 1.85× lower at baseline in the lines without CALB1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[B3GNT3]] | B | B3GNT3 activity raises KPNA2P3's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 1.70× lower at baseline in the lines without B3GNT3 | 0.051 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[SH3TC2]] | B | SH3TC2 activity raises KPNA2P3's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 1.34× lower at baseline in the lines without SH3TC2 | 0.051 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent |
| [[LEMD1]] | B | LEMD1 activity raises KPNA2P3's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.57× lower at baseline in the lines without LEMD1 | 0.055 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[LSMEM2]] | B | LSMEM2 activity raises KPNA2P3's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without LSMEM2 | 0.058 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[BCL2L1]] | B | BCL2L1 activity raises KPNA2P3's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without BCL2L1 | 0.062 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.1, 53.8); signed map (0.9, 36.9). **Vector** length 74.0, 12.3% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.9 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.3 | +0.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | karyopherin subunit alpha 2 pseudogene 3 |
| Locus type | pseudogene |
| Location | 17q24.1 — chr17:64,749,918-64,758,603 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52870) · Entrez [109286552](https://www.ncbi.nlm.nih.gov/gene/109286552) · Ensembl [ENSG00000266820](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266820)

## Data

Gene col 15497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15497); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15497]; `tensor/DDL_lfc|DDL_z.npy` [15497]; `embed/gene_vectors.npy` [15497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15497 or target_col == 15497). Every well: [[KPNA2P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNA2P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

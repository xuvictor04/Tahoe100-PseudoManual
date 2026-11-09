---
symbol: "TMEM92"
type: "gene"
col: 9415
ensembl_id: "ENSG00000167105"
name: "transmembrane protein 92"
location: "17q21.33"
module: 34
arm: "+"
pooled_cpm: 4.69
n_lines_expressing: 28
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 27
direction_downstream: 62
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TMEM92

*transmembrane protein 92* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.13× (z +6.1, q 5e-07, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.03× (z +5.9, q 8e-07, up in 11 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.327× (z -13.3, q 8e-38, down in 22 of 23 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMTK3]] (+0.76, fdr 1e-05), [[LYPD3]] (+0.73, fdr 1e-05), [[FA2H]] (+0.68, fdr 1e-05); moves opposite to [[ZMYND11]] (-0.61, fdr 4e-05), [[TMEM80]] (-0.61, fdr 2e-04), [[GALNT7-DT]] (-0.61, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[ENPP5]] → it (grade B ⚠); 62 go from it, the strongest it → [[MYO1E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +6.1 | 5e-07 | 0/5 | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +5.9 | 8e-07 | 11/25 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +4.4 | 0.002 | 10/25 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.006 | 10/25 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.62×** | +4.0 | 0.006 | 10/25 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +3.8 | 0.013 | 6/17 (A-172, COLO 205, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.5 | 0.041 | 5/26 (Hs 766T, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.48×** | +3.3 | 0.077 | 2/17 (SW 900, NCI-H2030) | rises with dose | composition shift; position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.082 | 3/24 (A549, COLO 205, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.45× | +3.1 | 0.10 | 8/25 (BT-474, SW1417, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | 1.30× | +3.1 | 0.10 | 3/24 (SW 900, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.10 | 6/23 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.327×** | -13.3 | 8e-38 | 22/23 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.255×** | -11.5 | 3e-28 | 20/23 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.403×** | -7.7 | 3e-12 | 18/25 (NCI-H1792, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.405×** | -7.6 | 3e-12 | 20/25 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.451×** | -6.5 | 1e-08 | 15/24 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -6.3 | 3e-08 | 19/22 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.530×** | -5.4 | 6e-06 | 17/25 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.626×** | -4.0 | 0.005 | 18/25 (A498, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -3.6 | 0.022 | 12/24 (KATO III, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.666×** | -3.4 | 0.032 | 7/25 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.671×** | -3.4 | 0.036 | 10/25 (SW 900, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -3.1 | 0.081 | 16/22 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 10.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0924× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0801× (z -20.3) |
| [[A-172 (line)]] | wt | 8.34 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0964× (z -10.2) |
| [[A498 (line)]] | wt | 18.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -9.6) |
| [[COLO 205 (line)]] | alt | 8.73 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0924× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 7.70 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0763× (z -14.5) |
| [[A549 (line)]] | wt | 7.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0777× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 3.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0581× (z -10.3) |
| [[HOP62 (line)]] | alt | 6.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -12.9) |
| [[HT-29 (line)]] | alt | 8.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 5.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0599× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 8.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -11.8) |
| [[SW480 (line)]] | alt | 3.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -11.5) |
| [[A-427 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.835 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.373 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK3]] | +0.76 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[LYPD3]] | +0.73 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[FA2H]] | +0.68 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[AGPAT2]] | +0.63 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[SERPINB1]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[GIPR]] | +0.61 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[CORO2A]] | +0.61 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[KRT19]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[CBLC]] | +0.60 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FCHO1]] | +0.60 | +0.55 / +0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[RASSF7]] | +0.60 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TNNI3]] | +0.59 | +0.48 / +0.33 | both halves | 1e-04 |  |
| [[RDH13]] | +0.59 | +0.49 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.61 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TMEM80]] | -0.61 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[GALNT7-DT]] | -0.61 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[BRD1]] | -0.61 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[TXNRD2]] | -0.60 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MCCC2]] | -0.59 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[SNX5]] | -0.58 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[PLBD1-AS1]] | -0.58 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[UPF3A]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[FAIM]] | -0.57 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[DDX6]] | -0.56 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[ST7L]] | -0.56 | -0.50 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 8, C 19. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP5]] | B | ENPP5 activity raises TMEM92's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.36× lower at baseline in the lines without ENPP5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[SERPINB1]] | B | SERPINB1 activity raises TMEM92's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.01× lower at baseline in the lines without SERPINB1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[MYO1E]] | B | MYO1E activity raises TMEM92's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without MYO1E | 0.076 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[SERPINA5]] | B | SERPINA5 activity raises TMEM92's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.66× lower at baseline in the lines without SERPINA5 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TMEM92's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CCDC33]] | B | CCDC33 activity raises TMEM92's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 1.83× lower at baseline in the lines without CCDC33 | 0.087 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[CRYBG2]] | B | CRYBG2 activity raises TMEM92's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.54× lower at baseline in the lines without CRYBG2 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[KIF21B]] | B | KIF21B activity raises TMEM92's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 2.05× lower at baseline in the lines without KIF21B | 0.094 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CARD11]] | C | CARD11 activity raises TMEM92's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without CARD11 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises TMEM92's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without P2RY2 | 0.017 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises TMEM92's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.03× lower at baseline in the lines without TMPRSS4 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises TMEM92's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.02× lower at baseline in the lines without ATP2C2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |

### Downstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 43, C 19. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | TMEM92 activity raises MYO1E's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without TMEM92 | 0.003 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[CORO2A]] | B | TMEM92 activity strengthens CORO2A's drug response | lines that do not express TMEM92 (20) vs lines expressing it (25) | the lines without TMEM92 respond 0.65× as strongly (z diff +1.56); strongest at Homoharringtonine 0.5 µM: 0.57x vs 0.27x (z diff +4.4) | 0.006 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10; target measured in part of the lines; artifact flags |
| [[RASSF7]] | B | TMEM92 activity raises RASSF7's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without TMEM92 | 0.007 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[DPH5]] | B | TMEM92 activity lowers DPH5's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.46× higher at baseline in the lines without TMEM92 | 0.010 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[KIF21B]] | B | TMEM92 activity raises KIF21B's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without TMEM92 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[LYPD3]] | B | TMEM92 activity raises LYPD3's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without TMEM92 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[KCTD17]] | B | TMEM92 activity lowers KCTD17's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.48× higher at baseline in the lines without TMEM92 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[POGLUT1]] | B | TMEM92 activity lowers POGLUT1's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.45× higher at baseline in the lines without TMEM92 | 0.014 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[RPAP2]] | B | TMEM92 activity lowers RPAP2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.38× higher at baseline in the lines without TMEM92 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[RAB11FIP2]] | B | TMEM92 activity lowers RAB11FIP2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.38× higher at baseline in the lines without TMEM92 | 0.023 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[DPF1]] | B | TMEM92 activity lowers DPF1's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.59× higher at baseline in the lines without TMEM92 | 0.024 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[EFCAB2]] | B | TMEM92 activity lowers EFCAB2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.37× higher at baseline in the lines without TMEM92 | 0.025 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.1, 3.1); signed map (-3.5, 45.0). **Vector** length 57.5, 14.9% of its response variance represented; |z| ≥ 3 in 480 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | -0.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.5 | -13.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 92 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,271,406-50,281,485 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33318 |
| Matched by | ensembl_id |

UniProt [Q6UXU6](https://www.uniprot.org/uniprotkb/Q6UXU6) carries no function annotation.

**Summary**, from NCBI Gene [162461](https://www.ncbi.nlm.nih.gov/gene/162461):

> Predicted to be located in membrane. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26579) · Entrez [162461](https://www.ncbi.nlm.nih.gov/gene/162461) · UniProt [Q6UXU6](https://www.uniprot.org/uniprotkb/Q6UXU6) · Ensembl [ENSG00000167105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167105)

## Data

Gene col 9415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9415); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9415]; `tensor/DDL_lfc|DDL_z.npy` [9415]; `embed/gene_vectors.npy` [9415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9415 or target_col == 9415). Every well: [[TMEM92 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM92.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

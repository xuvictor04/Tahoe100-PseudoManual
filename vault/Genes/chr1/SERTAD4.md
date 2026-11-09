---
symbol: "SERTAD4"
type: "gene"
col: 1349
ensembl_id: "ENSG00000082497"
name: "SERTA domain containing 4"
location: "1q32.2"
module: 120
arm: "+"
pooled_cpm: 2.89
n_lines_expressing: 36
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 11
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# SERTAD4

*SERTA domain containing 4* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.18× (z +15.1, q 0e+00, up in 19 of 25 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.37× (z +6.5, q 1e-08, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.400× (z -6.9, q 3e-09, down in 20 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM111A]] (+0.71, fdr 1e-05), [[RASGRF1]] (+0.68, fdr 7e-06), [[LYPD1]] (+0.66, fdr 7e-06); moves opposite to [[ANO10]] (-0.63, fdr 1e-05), [[ZDHHC9]] (-0.62, fdr 2e-05), [[CTNNBL1]] (-0.58, fdr 1e-04).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LRRN1]] → it (grade B ⚠); 11 go from it, the strongest it → [[DLX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **4.18×** | +15.1 | 0e+00 | 19/25 (NCI-H1573, C32, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.79×** | +10.0 | 6e-21 | 7/12 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.95×** | +9.9 | 1e-20 | 5/8 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.10×** | +7.8 | 8e-13 | 7/9 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.75×** | +7.3 | 4e-11 | 12/26 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +6.5 | 1e-08 | 16/23 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.7 | 8e-07 | 12/24 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +5.4 | 5e-06 | 15/30 (LS 180, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.91×** | +4.8 | 9e-05 | 5/12 (NCI-H1573, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.74×** | +4.1 | 0.002 | 7/17 (BT-474, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +3.9 | 0.005 | 9/31 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.72×** | +3.9 | 0.005 | 6/17 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.66×** | +3.8 | 0.008 | 9/33 (SW 900, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.025 | 10/28 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.34×** | +3.1 | 0.074 | 6/30 (J82, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.400×** | -6.9 | 3e-09 | 20/29 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.607×** | -5.3 | 3e-05 | 15/32 (CHP-212, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.489×** | -5.1 | 7e-05 | 17/26 (SW 900, CHP-212, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.520×** | -4.9 | 1e-04 | 14/27 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.540×** | -4.6 | 4e-04 | 11/28 (KATO III, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -4.0 | 0.005 | 13/28 (Panc 03.27, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.598×** | -3.9 | 0.009 | 12/32 (LS 180, BT-474, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.740×** | -3.2 | 0.090 | 11/28 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.670× | -3.0 | 0.16 | 5/32 (SW 900, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 5.64 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +11.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.0765× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0274× (z -16.8) |
| [[KATO III (line)]] | alt | 6.19 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.0972× (z -8.7) |
| [[LoVo (line)]] | wt | 2.34 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 22.2× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[BT-474 (line)]] | alt | 9.11 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0844× (z -10.1) |
| [[C32 (line)]] | wt | 1.68 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 42.4× (z +10.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 3.49 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[CHP-212 (line)]] | wt | 31.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0718× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -10.5) |
| [[SW 900 (line)]] | alt | 6.02 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0469× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.913 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.211 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.737 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.992 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.156 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.725 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.494 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM111A]] | +0.71 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.68 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[LYPD1]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[IKBKE]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ZNF462]] | +0.60 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SOCS2]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ENC1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PHF19]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[HIVEP1]] | +0.58 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ZNF702P]] | +0.58 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[SPAG1]] | +0.58 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[RAB38]] | +0.57 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO10]] | -0.63 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[ZDHHC9]] | -0.62 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[CTNNBL1]] | -0.58 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[SS18L1]] | -0.56 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[MKRN2]] | -0.56 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[VDAC2]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[YIPF1]] | -0.55 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[SGTB]] | -0.55 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[SHARPIN]] | -0.55 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ST6GALNAC6]] | -0.55 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[EDEM2]] | -0.54 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RARS2]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRN1]] | B | LRRN1 activity raises SERTAD4's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.72× lower at baseline in the lines without LRRN1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[RASEF]] | B | RASEF activity raises SERTAD4's level | lines that do not express RASEF (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without RASEF | 0.003 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[LINC02605]] | B | LINC02605 activity raises SERTAD4's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 1.48× lower at baseline in the lines without LINC02605 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[DEPDC7]] | B | DEPDC7 activity lowers SERTAD4's level | lines that do not express DEPDC7 (13) vs lines expressing it (37) | 1.65× higher at baseline in the lines without DEPDC7 | 0.053 | ⚠ within organs, on part of the lines |
| [[ITGB8]] | B | ITGB8 activity raises SERTAD4's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without ITGB8 | 0.081 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[PSMB5]] | B | PSMB5 activity raises SERTAD4's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SMAD3]] | B | SMAD3 activity raises SERTAD4's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.02× lower at baseline in the lines without SMAD3 | 0.096 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[NALCN]] | C | NALCN activity raises SERTAD4's level | lines that do not express NALCN (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without NALCN | 0.082 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX1]] | B | SERTAD4 activity lowers DLX1's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.51× higher at baseline in the lines without SERTAD4 | 0.009 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[RASEF]] | B | SERTAD4 activity raises RASEF's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 2.22× lower at baseline in the lines without SERTAD4 | 0.034 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[VDR]] | B | SERTAD4 activity raises VDR's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without SERTAD4 | 0.037 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[GATA6]] | B | SERTAD4 activity raises GATA6's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without SERTAD4 | 0.045 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[IRF2]] | B | SERTAD4 activity raises IRF2's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.26× lower at baseline in the lines without SERTAD4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[GPR89A]] | B | SERTAD4 activity lowers GPR89A's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.12× higher at baseline in the lines without SERTAD4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[SH2D4A]] | B | SERTAD4 activity raises SH2D4A's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without SERTAD4 | 0.061 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[TAPBPL]] | B | SERTAD4 activity raises TAPBPL's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.27× lower at baseline in the lines without SERTAD4 | 0.079 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| cells under [[MK-3903 (drug)]] 0.05 µM | B | SERTAD4 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express SERTAD4 (14) vs lines expressing it (34) | the lines without SERTAD4: 0.94× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[PLEKHG3]] | B | SERTAD4 activity raises PLEKHG3's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.09× lower at baseline in the lines without SERTAD4 | 0.097 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[NALCN]] | C | SERTAD4 activity raises NALCN's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 3.11× lower at baseline in the lines without SERTAD4 | 0.032 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.9, 6.2); signed map (27.5, 6.5). **Vector** length 61.4, 13.0% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.4 | +15.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.6 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.9 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SERTA domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2 — chr1:210,232,796-210,246,631 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DJ667H12.2 |
| Gene groups (HGNC) | SERTA domain containing |
| Matched by | ensembl_id |

UniProt [Q9NUC0](https://www.uniprot.org/uniprotkb/Q9NUC0) carries no function annotation.

**Summary**, from NCBI Gene [56256](https://www.ncbi.nlm.nih.gov/gene/56256):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25236) · Entrez [56256](https://www.ncbi.nlm.nih.gov/gene/56256) · UniProt [Q9NUC0](https://www.uniprot.org/uniprotkb/Q9NUC0) · Ensembl [ENSG00000082497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082497)

## Data

Gene col 1349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1349); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1349]; `tensor/DDL_lfc|DDL_z.npy` [1349]; `embed/gene_vectors.npy` [1349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1349 or target_col == 1349). Every well: [[SERTAD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERTAD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

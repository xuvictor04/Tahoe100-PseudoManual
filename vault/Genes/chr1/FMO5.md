---
symbol: "FMO5"
type: "gene"
col: 5246
ensembl_id: "ENSG00000131781"
name: "flavin containing dimethylaniline monoxygenase 5"
location: "1q21.1"
module: 8
arm: "+"
pooled_cpm: 5.0
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 30
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FMO5

*flavin containing dimethylaniline monoxygenase 5* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.10× (z +12.8, q 1e-34, up in 5 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +9.2, q 1e-17, up in 18 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.461× (z -9.1, q 5e-17, down in 26 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LNX1]] (+0.64, fdr 1e-05), [[ARSL]] (+0.63, fdr 1e-05), [[SMIM2-AS1]] (+0.62, fdr 1e-05); moves opposite to [[ZBED4]] (-0.53, fdr 2e-05), [[PAQR4]] (-0.51, fdr 2e-04), [[PLGRKT]] (-0.50, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[DUOX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +12.8 | 1e-34 | 5/7 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +9.5 | 6e-19 | 13/23 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +9.2 | 1e-17 | 18/36 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +8.1 | 6e-14 | 23/44 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +7.4 | 2e-11 | 18/40 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +6.5 | 1e-08 | 4/11 (A498, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +5.8 | 4e-07 | 18/44 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +5.6 | 1e-06 | 18/40 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.004 | 7/42 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.008 | 12/45 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.023 | 13/40 (AsPC-1, SW480, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.52×** | +3.5 | 0.023 | 2/35 (AsPC-1, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.21×** | +3.2 | 0.055 | 7/43 (KATO III, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.10 | 14/44 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5246.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.461×** | -9.1 | 5e-17 | 26/42 (HT-29, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.489×** | -8.2 | 1e-13 | 29/46 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -6.8 | 2e-09 | 22/41 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.569×** | -6.4 | 2e-08 | 15/34 (HT-29, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.682×** | -4.5 | 8e-04 | 14/40 (NCI-H1792, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.733×** | -3.6 | 0.025 | 13/44 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.032 | 12/43 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.032 | 8/44 (HT-29, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.745×** | -3.5 | 0.032 | 13/45 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.739×** | -3.4 | 0.032 | 14/44 (HT-29, H4, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.769× | -3.1 | 0.10 | 10/44 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.770× | -3.1 | 0.10 | 14/44 (HT-29, AsPC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 26.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0982× (z -10.8) |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0312× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 8.60 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.57 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0792× (z -9.1) |
| [[A498 (line)]] | wt | 1.73 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 22.2× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 2.35 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0631× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 5.04 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0478× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 3.24 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0754× (z -10.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 2.99 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0687× (z -9.9) |
| [[A-427 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNX1]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ARSL]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SMIM2-AS1]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[HNF1A-AS1]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SELENOP]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[ACSM3]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SCIN]] | +0.59 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[STX19]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[BCAS1]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MTCP1]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[BCL2L15]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED4]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[PAQR4]] | -0.51 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[PLGRKT]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ABCC10]] | -0.50 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[CAD]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PUS1]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[NLN]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[CCM2]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[XXYLT1]] | -0.48 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[R3HDM1]] | -0.48 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[SLFNL1-AS1]] | -0.48 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[CMSS1]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 30, C 0. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUOX2]] | B | DUOX2 activity raises FMO5's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.32× lower at baseline in the lines without DUOX2 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[SLC44A4]] | B | SLC44A4 activity raises FMO5's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.51× lower at baseline in the lines without SLC44A4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[MMP7]] | B | MMP7 activity raises FMO5's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.08× lower at baseline in the lines without MMP7 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[SLC40A1]] | B | SLC40A1 activity raises FMO5's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.88× lower at baseline in the lines without SLC40A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[FRK]] | B | FRK activity raises FMO5's level | lines that do not express FRK (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without FRK | 0.007 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[MMP7]] | B | MMP7 activity strengthens FMO5's drug response | lines that do not express MMP7 (38) vs lines expressing it (8) | the lines without MMP7 respond 0.78× as strongly (z diff +0.66); strongest at Digitoxin 5 µM: 0.55x vs 0.26x (z diff +3.5) | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; target measured in part of the lines; both ways; artifact flags |
| [[SYNPR-AS1]] | B | SYNPR-AS1 activity raises FMO5's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 1.60× lower at baseline in the lines without SYNPR-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[ARSL]] | B | ARSL activity raises FMO5's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without ARSL | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[FAAH2]] | B | FAAH2 activity raises FMO5's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 1.58× lower at baseline in the lines without FAAH2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[RASSF6]] | B | RASSF6 activity raises FMO5's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.72× lower at baseline in the lines without RASSF6 | 0.017 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[C11orf52]] | B | C11orf52 activity raises FMO5's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.54× lower at baseline in the lines without C11orf52 | 0.030 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[DPP4]] | B | DPP4 activity raises FMO5's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.75× lower at baseline in the lines without DPP4 | 0.035 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, 52.4); signed map (60.6, -0.7). **Vector** length 63.3, 9.44% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -3.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -6.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -4.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | flavin containing dimethylaniline monoxygenase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:147,175,351-147,243,050 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavin containing monooxygenases; Flavoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P49326](https://www.uniprot.org/uniprotkb/P49326) (Flavin-containing monooxygenase 5):

> Acts as a Baeyer-Villiger monooxygenase on a broad range of substrates. Catalyzes the insertion of an oxygen atom into a carbon-carbon bond adjacent to a carbonyl, which converts ketones to esters. Active on diverse carbonyl compounds, whereas soft nucleophiles are mostly non- or poorly reactive. In contrast with other forms of FMO it is non- or poorly active on 'classical' substrates such as drugs, pesticides, and dietary components containing soft nucleophilic heteroatoms (Probable). Able to …

**Summary**, from NCBI Gene [2330](https://www.ncbi.nlm.nih.gov/gene/2330):

> Metabolic N-oxidation of the diet-derived amino-trimethylamine (TMA) is mediated by flavin-containing monooxygenase and is subject to an inherited FMO3 polymorphism in man resulting in a small subpopulation with reduced TMA N-oxidation capacity resulting in fish odor syndrome Trimethylaminuria. Three forms of the enzyme, FMO1 found in fetal liver, FMO2 found in adult liver, and FMO3 are encoded by genes clustered in the 1q23-q25 region. Flavin-containing monooxygenases are NADPH-dependent …

**Accessions** — [HGNC:3773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3773) · Entrez [2330](https://www.ncbi.nlm.nih.gov/gene/2330) · UniProt [P49326](https://www.uniprot.org/uniprotkb/P49326) · Ensembl [ENSG00000131781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131781)

## Data

Gene col 5246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5246); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5246]; `tensor/DDL_lfc|DDL_z.npy` [5246]; `embed/gene_vectors.npy` [5246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5246 or target_col == 5246). Every well: [[FMO5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMO5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

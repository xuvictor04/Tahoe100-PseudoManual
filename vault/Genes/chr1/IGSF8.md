---
symbol: "IGSF8"
type: "gene"
col: 8570
ensembl_id: "ENSG00000162729"
name: "immunoglobulin superfamily member 8"
location: "1q23.2"
module: 88
arm: "-"
pooled_cpm: 10.23
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# IGSF8

*immunoglobulin superfamily member 8* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.61× (z +10.8, q 3e-24, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.252× (z -21.9, q 0e+00, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOSPD3]] (+0.78, fdr 7e-06), [[AP1S1]] (+0.75, fdr 7e-06), [[CD81]] (+0.74, fdr 7e-06); moves opposite to [[ST7L]] (-0.75, fdr 7e-06), [[THOC7]] (-0.72, fdr 7e-06), [[WARS2-AS1]] (-0.71, fdr 2e-05).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LYPD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.61×** | +10.8 | 3e-24 | 41/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.54×** | +10.4 | 4e-23 | 42/45 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +10.3 | 1e-22 | 39/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.38×** | +9.7 | 3e-20 | 26/36 (C32, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +6.7 | 3e-09 | 32/40 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.85×** | +6.6 | 3e-09 | 10/16 (NCI-H460, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +6.6 | 3e-09 | 34/47 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.66×** | +5.3 | 1e-05 | 12/23 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.25×** | +3.6 | 0.020 | 17/43 (A498, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.024 | 12/47 (A498, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.90×** | +3.4 | 0.029 | 4/39 (A498, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.35×** | +3.4 | 0.036 | 13/38 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | 1.67× | +3.0 | 0.11 | 8/45 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8570.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.252×** | -21.9 | 0e+00 | 40/42 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.196×** | -18.3 | 0e+00 | 40/42 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.243×** | -15.3 | 0e+00 | 43/45 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.393×** | -10.5 | 1e-23 | 38/45 (H4, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.446×** | -9.1 | 1e-17 | 35/46 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.452×** | -8.6 | 1e-15 | 35/44 (SNU-423, A-172, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.586×** | -6.0 | 2e-07 | 27/47 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -5.6 | 1e-06 | 26/46 (RKO, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -4.1 | 0.003 | 20/42 (RKO, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -4.0 | 0.004 | 23/45 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.715×** | -3.8 | 0.008 | 13/45 (SNU-423, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.703×** | -3.7 | 0.012 | 15/45 (SW48, SNU-423, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.722×** | -3.4 | 0.031 | 15/40 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.724×** | -3.3 | 0.033 | 10/45 (A-172, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.734×** | -3.2 | 0.050 | 9/45 (KATO III, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0678× (z -13.2) |
| [[A-172 (line)]] | wt | 21.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -12.5) |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0970× (z -13.4) |
| [[HT-29 (line)]] | alt | 4.59 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0779× (z -13.8) |
| [[KATO III (line)]] | alt | 9.92 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0623× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0737× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 8.26 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0771× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 9.35 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -11.7) |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 3 | — | [[Verteporfin (drug)]] 5 µM 0.0628× (z -12.6) |
| [[SW480 (line)]] | alt | 8.46 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.5) |
| [[A498 (line)]] | wt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -13.2) |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -13.9) |
| [[C32 (line)]] | wt | 49.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -10.6) |
| [[J82 (line)]] | alt | 9.00 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -15.8) |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 5.79 | 0 | 2 | — | [[BI-78D3 (drug)]] 0.05 µM 0.0794× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 25.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0959× (z -18.5) |
| [[PANC-1 (line)]] | alt | 4.29 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0714× (z -12.2) |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -11.4) |
| [[A549 (line)]] | wt | 5.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 9.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.8) |
| [[H4 (line)]] | wt | 12.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0388× (z -11.8) |
| [[HCT15 (line)]] | alt | 9.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 8.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -10.6) |
| [[Hs 766T (line)]] | wt | 6.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -12.8) |
| [[LoVo (line)]] | wt | 5.67 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.100× (z -8.8) |
| [[RKO (line)]] | wt | 6.77 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0946× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 6.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0684× (z -9.2) |
| [[A-427 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | +0.78 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[AP1S1]] | +0.75 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[CD81]] | +0.74 | +0.67 / +0.74 | both halves | 7e-06 | same gene group; STRING 997 |
| [[ADIPOR1]] | +0.74 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[LPCAT4]] | +0.71 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[DNASE1L1]] | +0.71 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[PDZD7]] | +0.70 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SEZ6L2]] | +0.70 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.70 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[PLA2G15]] | +0.70 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[GM2A]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | -0.75 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[THOC7]] | -0.72 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | -0.71 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[GABPB2]] | -0.71 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[RAB30-DT]] | -0.71 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[KRCC1]] | -0.70 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[RBM26-AS1]] | -0.70 | -0.70 / -0.35 | both halves | 1e-04 |  |
| [[TRMT13]] | -0.70 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.70 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[BCDIN3D]] | -0.69 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.69 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[TIA1]] | -0.69 | -0.65 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD3]] | B | LYPD3 activity raises IGSF8's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without LYPD3 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[IGSF3]] | B | IGSF3 activity raises IGSF8's level | lines that do not express IGSF3 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without IGSF3 | 0.081 | ⚠ within organs, on part of the lines; also absent: FARP1, KCNIP3 |
| [[HDAC6]] | B | HDAC6 activity lowers IGSF8's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.819). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (4.1, -0.0); signed map (-35.0, 13.7). **Vector** length 93.0, 21.1% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.9 | +10.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +10.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.1 | +6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.7 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.3 | -18.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.0 | -15.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.8 | -9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.4 | -21.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -8.6 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin superfamily member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:160,091,340-160,098,943 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD81P3, EWI2, PGRL, CD316 |
| Gene groups (HGNC) | CD molecules; V-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969P0](https://www.uniprot.org/uniprotkb/Q969P0) (Immunoglobulin superfamily member 8):

> Member of the immunoglobulin superfamily (IgSF) that links tetraspanin-enriched microdomains to the actin cytoskeleton and plays several important roles in innate and adaptive immunity. Acts as an inducible receptor of HSPA8 on dendritic cells to enhance the CCL21/SLC-dependent migration of activated mature dendritic cells while attenuating their antigen-specific stimulatory capacities. In complex with alpha-actinins ACTN1 and ACTN4, regulates actin dynamics in the immune synapse and subsequent …

**Summary**, from NCBI Gene [93185](https://www.ncbi.nlm.nih.gov/gene/93185):

> This gene encodes a member the EWI subfamily of the immunoglobulin protein superfamily. Members of this family contain a single transmembrane domain, an EWI (Glu-Trp-Ile)-motif and a variable number of immunoglobulin domains. This protein interacts with the tetraspanins CD81 and CD9 and may regulate their role in certain cellular functions including cell migration and viral infection. The encoded protein may also function as a tumor suppressor by inhibiting the proliferation of certain cancers. …

**Accessions** — [HGNC:17813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17813) · Entrez [93185](https://www.ncbi.nlm.nih.gov/gene/93185) · UniProt [Q969P0](https://www.uniprot.org/uniprotkb/Q969P0) · Ensembl [ENSG00000162729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162729)

## Data

Gene col 8570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8570); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8570]; `tensor/DDL_lfc|DDL_z.npy` [8570]; `embed/gene_vectors.npy` [8570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8570 or target_col == 8570). Every well: [[IGSF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGSF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

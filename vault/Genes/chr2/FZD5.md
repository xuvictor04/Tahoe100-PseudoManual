---
symbol: "FZD5"
type: "gene"
col: 8659
ensembl_id: "ENSG00000163251"
name: "frizzled class receptor 5"
location: "2q33.3"
module: 8
arm: "+"
pooled_cpm: 11.77
n_lines_expressing: 46
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 41
direction_downstream: 6
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FZD5

*frizzled class receptor 5* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.06× (z +11.1, q 4e-26, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.743× (z -4.3, q 0.009, down in 15 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC3A]] (+0.56, fdr 2e-05), [[CGN]] (+0.56, fdr 3e-05), [[TOB1]] (+0.54, fdr 1e-05); moves opposite to [[PEX6]] (-0.56, fdr 3e-05), [[TIMM23B]] (-0.49, fdr 3e-05), [[VPS51]] (-0.48, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 41 arrows point to it, the strongest [[MUC5B]] → it (grade B ⚠); 6 go from it, the strongest it → [[SLC38A9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +11.1 | 4e-26 | 31/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +11.1 | 6e-26 | 22/39 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +10.6 | 7e-24 | 21/36 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +9.8 | 1e-20 | 29/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +9.4 | 8e-19 | 22/43 (KATO III, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +6.4 | 1e-08 | 20/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +6.3 | 3e-08 | 14/43 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 2e-06 | 16/37 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 6e-06 | 16/42 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 6e-06 | 17/41 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 0.002 | 11/43 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +4.1 | 0.002 | 13/37 (CFPAC-1, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.075 | 6/40 (RKO, SW1417, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +3.1 | 0.083 | 6/43 (J82, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.1 | 0.083 | 10/40 (PANC-1, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.743×** | -4.3 | 0.009 | 15/40 (HT-29, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.757×** | -4.1 | 0.010 | 12/40 (HT-29, HepG2/C3A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -3.8 | 0.027 | 16/43 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.638×** | -3.6 | 0.042 | 11/40 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -3.5 | 0.054 | 13/41 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.679× | -3.1 | 0.18 | 10/27 (COLO 205, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 70.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.243× (z -9.6) |
| [[KATO III (line)]] | alt | 29.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.0600× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[A498 (line)]] | wt | 13.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 17.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +8.9) | [[AZD2858 (drug)]] 0.5 µM 0.0675× (z -10.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 27.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.279× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[NCI-H460 (line)]] | wt | 10.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +12.8) | — |
| [[A549 (line)]] | wt | 9.05 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 5.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 9.37 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.117× (z -8.5) |
| [[SW480 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +13.4) | — |
| [[A-172 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC3A]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CGN]] | +0.56 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[TOB1]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MUC13]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[CYP2S1]] | +0.53 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ANKRD22]] | +0.52 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[ST14]] | +0.52 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[DAB2IP]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[SLC44A4]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TMEM45B]] | +0.51 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CDC42EP1]] | +0.51 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX6]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[TIMM23B]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[VPS51]] | -0.48 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[CWC27]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ERCC8]] | -0.47 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[LINC03006-1]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PSMC1]] | -0.45 | -0.38 / -0.45 | both halves | 7e-05 | pathway: Asymmetric localization of PCP proteins |
| [[ISY1]] | -0.44 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[SLC38A9]] | -0.44 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[HERC2P3-1]] | -0.44 | -0.39 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 41, C 0. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC5B]] | B | MUC5B activity raises FZD5's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.98× lower at baseline in the lines without MUC5B | 0.004 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[SLC44A4]] | B | SLC44A4 activity raises FZD5's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.89× lower at baseline in the lines without SLC44A4 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[GCNT3]] | B | GCNT3 activity raises FZD5's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.11× lower at baseline in the lines without GCNT3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[ALOX5]] | B | ALOX5 activity raises FZD5's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without ALOX5 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[MUC3A]] | B | MUC3A activity raises FZD5's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without MUC3A | 0.009 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[ADGRF1]] | B | ADGRF1 activity raises FZD5's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.26× lower at baseline in the lines without ADGRF1 | 0.010 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[PCDH1]] | B | PCDH1 activity raises FZD5's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.03× lower at baseline in the lines without PCDH1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[CLDN3]] | B | CLDN3 activity raises FZD5's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.11× lower at baseline in the lines without CLDN3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[ITGB6]] | B | ITGB6 activity raises FZD5's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without ITGB6 | 0.012 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[CGN]] | B | CGN activity raises FZD5's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.39× lower at baseline in the lines without CGN | 0.013 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[TJP3]] | B | TJP3 activity raises FZD5's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.34× lower at baseline in the lines without TJP3 | 0.014 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises FZD5's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.17× lower at baseline in the lines without TMPRSS2 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC38A9]] | C | FZD5 activity raises SLC38A9's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without FZD5 | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |
| [[SLC50A1]] | C | FZD5 activity raises SLC50A1's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without FZD5 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |
| [[ABHD11]] | C | FZD5 activity raises ABHD11's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without FZD5 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |
| [[TPPP]] | C | FZD5 activity raises TPPP's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without FZD5 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |
| [[SLC9A3R1]] | C | FZD5 activity raises SLC9A3R1's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without FZD5 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |
| [[IFFO2]] | C | FZD5 activity raises IFFO2's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without FZD5 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.508). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, 58.2); signed map (50.5, 5.7). **Vector** length 66.1, 10.5% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.4 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | frizzled class receptor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:207,762,598-207,769,906 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HFZ5, DKFZP434E2135; previously C2orf31 |
| Gene groups (HGNC) | G protein-coupled receptors, Class F frizzled |
| Hallmark sets | NOTCH_SIGNALING, INFLAMMATORY_RESPONSE |
| Reactome | 15 pathways, smallest: Signaling by RNF43 mutants; WNT5A-dependent internalization of FZD2, FZD5 and ROR2; Regulation of FZD by ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13467](https://www.uniprot.org/uniprotkb/Q13467) (Frizzled-5):

> Receptor for Wnt proteins. Functions in the canonical Wnt/beta-catenin signaling pathway. In vitro activates WNT2, WNT10B, WNT5A, but not WNT2B or WNT4 signaling (By similarity). In neurons, activation by WNT7A promotes formation of synapses. May be involved in transduction and intercellular transmission of polarity information during tissue morphogenesis and/or in differentiated tissues (Probable). Plays a role in yolk sac angiogenesis and in placental vascularization (By similarity). Plays a …

**Summary**, from NCBI Gene [7855](https://www.ncbi.nlm.nih.gov/gene/7855):

> Members of the 'frizzled' gene family encode 7-transmembrane domain proteins that are receptors for Wnt signaling proteins. The FZD5 protein is believed to be the receptor for the Wnt5A ligand. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4043) · Entrez [7855](https://www.ncbi.nlm.nih.gov/gene/7855) · UniProt [Q13467](https://www.uniprot.org/uniprotkb/Q13467) · Ensembl [ENSG00000163251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163251)

## Data

Gene col 8659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8659); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8659]; `tensor/DDL_lfc|DDL_z.npy` [8659]; `embed/gene_vectors.npy` [8659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8659 or target_col == 8659). Every well: [[FZD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FZD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

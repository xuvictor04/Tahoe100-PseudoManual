---
symbol: "RCC1L"
type: "gene"
col: 15823
ensembl_id: "ENSG00000274523"
name: "RCC1 like"
location: "7q11.23"
module: 64
arm: "+"
pooled_cpm: 30.8
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# RCC1L

*RCC1 like* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.85× (z +17.5, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.430× (z -24.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHBDD3]] (+0.72, fdr 5e-05), [[QRSL1]] (+0.70, fdr 1e-05), [[CDK12]] (+0.70, fdr 1e-05); moves opposite to [[DNAAF3]] (-0.66, fdr 5e-05), [[PJA2]] (-0.63, fdr 4e-05), [[PAFAH1B3]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +17.5 | 0e+00 | 40/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +14.1 | 1e-42 | 38/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +13.0 | 3e-36 | 42/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +12.0 | 4e-31 | 31/48 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +10.1 | 5e-22 | 19/37 (HS-578T, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +7.5 | 5e-12 | 24/45 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +6.7 | 2e-09 | 18/48 (PANC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.15× | +5.7 | 7e-07 | 16/48 (PANC-1, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +5.6 | 1e-06 | 18/48 (LoVo, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 3e-04 | 14/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.18× | +4.5 | 3e-04 | 18/46 (A498, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +4.0 | 0.003 | 8/48 (NCI-H1573, A549, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.14× | +3.8 | 0.007 | 5/46 (HCT15, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.14× | +3.7 | 0.008 | 10/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +3.5 | 0.018 | 8/48 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.11× | +2.9 | 0.097 | 7/48 (PANC-1, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.430×** | -24.0 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.488×** | -20.4 | 0e+00 | 47/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.511×** | -19.1 | 0e+00 | 46/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.575×** | -15.7 | 0e+00 | 41/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.728×** | -12.7 | 5e-35 | 40/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.642×** | -12.6 | 3e-34 | 34/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.530×** | -9.4 | 3e-19 | 37/48 (SNU-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.725×** | -9.1 | 5e-18 | 29/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -6.0 | 1e-07 | 0/48 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.726×** | -4.7 | 1e-04 | 17/48 (PANC-1, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.733×** | -4.6 | 2e-04 | 9/47 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.882× | -3.6 | 0.017 | 5/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.789×** | -3.5 | 0.019 | 13/48 (RKO, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Aliskiren (drug)]] 0.5 µM |  | 0.893× | -3.2 | 0.056 | 6/48 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.4 | 2 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.461× (z -10.8) |
| [[SW480 (line)]] | alt | 36.8 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.322× (z -15.9) |
| [[KATO III (line)]] | alt | 41.7 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.327× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 38.0 | 2 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.359× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 27.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.85× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 32.4 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.443× (z -10.1) |
| [[A-172 (line)]] | wt | 34.6 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.407× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.427× (z -8.6) |
| [[A498 (line)]] | wt | 40.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.414× (z -11.1) |
| [[BT-474 (line)]] | alt | 40.4 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.215× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 42.0 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.417× (z -10.7) |
| [[HOP62 (line)]] | alt | 24.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.380× (z -10.1) |
| [[LoVo (line)]] | wt | 36.0 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.445× (z -9.9) |
| [[COLO 205 (line)]] | alt | 23.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -9.8) |
| [[HCT15 (line)]] | alt | 30.7 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.109× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 41.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.415× (z -9.6) |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 1 | — | [[Berbamine (drug)]] 5 µM 0.202× (z -27.0) |
| [[NCI-H23 (line)]] | alt | 29.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.372× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.345× (z -10.3) |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 1 | — | [[Brivudine (drug)]] 5 µM 0.0520× (z -9.0) |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.335× (z -11.1) |
| [[A-427 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHBDD3]] | +0.72 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[QRSL1]] | +0.70 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CDK12]] | +0.70 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[VPS52]] | +0.69 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[UQCC1]] | +0.69 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[IREB2]] | +0.68 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[ALG8]] | +0.68 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NSMAF]] | +0.68 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ZNF346]] | +0.67 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[POU6F1]] | +0.66 | +0.51 / +0.40 | both halves | 4e-05 |  |
| [[TIRAP]] | +0.66 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[AIFM2]] | +0.66 | +0.61 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.66 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[PJA2]] | -0.63 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PAFAH1B3]] | -0.62 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[PTP4A2]] | -0.62 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[UGCG]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[FCHO1]] | -0.60 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[USP2]] | -0.60 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[GDE1]] | -0.60 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[FOXO6]] | -0.59 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[CFD]] | -0.59 | -0.32 / -0.46 | both halves | 1e-04 |  |
| [[SPAG9]] | -0.59 | -0.43 / -0.32 | both halves | 1e-04 |  |
| [[RYBP]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers RCC1L's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DNAJA4]] | B | DNAJA4 activity raises RCC1L's level | lines that do not express DNAJA4 (22) vs lines expressing it (28) | 1.08× lower at baseline in the lines without DNAJA4 | 0.082 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RCC1L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises RCC1L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-10.0, 15.7); signed map (23.1, -24.3). **Vector** length 100, 22.2% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.1 | +17.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.7 | +14.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +12.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -6.9 | -15.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -12.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.2 | -24.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -19.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.1 | -12.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.3 | -9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RCC1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:75,027,122-75,074,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously WBSCR16 |
| Reactome | 5 pathways, smallest: rRNA modification in the mitochondrion; Mitochondrial mRNA modification; rRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I51](https://www.uniprot.org/uniprotkb/Q96I51) (RCC1-like G exchanging factor-like protein):

> Guanine nucleotide exchange factor (GEF) for mitochondrial dynamin-related GTPase OPA1. Activates OPA1, by exchanging bound GDP for free GTP, and drives OPA1 and MFN1-dependent mitochondrial fusion. Plays an essential role in mitochondrial ribosome biogenesis. As a component of a functional protein-RNA module, consisting of RCC1L, NGRN, RPUSD3, RPUSD4, TRUB2, FASTKD2 and 16S mitochondrial ribosomal RNA (16S mt-rRNA), controls 16S mt-rRNA abundance and is required for intra-mitochondrial …

**Summary**, from NCBI Gene [81554](https://www.ncbi.nlm.nih.gov/gene/81554):

> This gene encodes a protein containing regulator of chromosome condensation 1-like repeats. The encoded protein may function as a guanine nucleotide exchange factor. This gene is located in a region of chromosome 7 that is deleted in Williams-Beuren syndrome, a multisystem developmental disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:14948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14948) · Entrez [81554](https://www.ncbi.nlm.nih.gov/gene/81554) · UniProt [Q96I51](https://www.uniprot.org/uniprotkb/Q96I51) · Ensembl [ENSG00000274523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274523)

## Data

Gene col 15823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15823); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15823]; `tensor/DDL_lfc|DDL_z.npy` [15823]; `embed/gene_vectors.npy` [15823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15823 or target_col == 15823). Every well: [[RCC1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCC1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

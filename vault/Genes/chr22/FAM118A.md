---
symbol: "FAM118A"
type: "gene"
col: 1943
ensembl_id: "ENSG00000100376"
name: "SIR2 antiphage like 2"
location: "22q13.31"
module: 10
arm: "-"
pooled_cpm: 31.32
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FAM118A

*SIR2 antiphage like 2* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.89× (z +14.6, q 1e-45, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.604× (z -16.4, q 0e+00, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST3]] (+0.72, fdr 1e-05), [[TRABD]] (+0.72, fdr 1e-05), [[BRAT1]] (+0.69, fdr 1e-05); moves opposite to [[PCNX4-DT]] (-0.77, fdr 1e-05), [[PKN2-AS1]] (-0.75, fdr 2e-05), [[LINC02542]] (-0.74, fdr 2e-04).
> It sits in the **-** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LHX6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +14.6 | 1e-45 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +13.6 | 1e-39 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +12.4 | 9e-33 | 39/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +6.7 | 3e-09 | 1/48 (NCI-H23) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +5.7 | 1e-06 | 19/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +5.6 | 2e-06 | 18/48 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +5.5 | 3e-06 | 18/46 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.8 | 1e-04 | 12/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.8 | 1e-04 | 16/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.7 | 1e-04 | 16/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.006 | 14/46 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.007 | 14/48 (HS-578T, KATO III, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | 1.12× | +3.7 | 0.010 | 8/48 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.026 | 10/46 (SNU-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1943.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.604×** | -16.4 | 0e+00 | 32/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -11.1 | 3e-26 | 35/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.655×** | -9.7 | 4e-20 | 26/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.650×** | -9.6 | 2e-19 | 30/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.697×** | -8.3 | 1e-14 | 32/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -7.5 | 8e-12 | 29/48 (SW1417, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.764×** | -6.2 | 4e-08 | 19/42 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.650×** | -5.2 | 1e-05 | 15/45 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.853× | -5.2 | 1e-05 | 14/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.808×** | -4.9 | 5e-05 | 19/48 (PANC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.807×** | -4.6 | 2e-04 | 17/41 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.821×** | -4.4 | 6e-04 | 19/47 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -4.3 | 7e-04 | 20/46 (SK-MEL-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.700×** | -4.3 | 7e-04 | 17/48 (A-427, SW480, …) | all doses, flat | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.835× | -3.9 | 0.003 | 15/47 (A-172, A-427, …) | all doses, flat |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.869× | -3.2 | 0.040 | 4/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.876× | -3.0 | 0.072 | 3/48 (C-33 A, Hs 766T, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.878× | -3.0 | 0.079 | 3/48 (SW 1271, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.9 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -12.3) |
| [[PANC-1 (line)]] | alt | 49.6 | 1 | 4 | [[Panobinostat (drug)]] 5 µM 2.13× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -23.6) |
| [[LoVo (line)]] | wt | 45.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -17.2) |
| [[C32 (line)]] | wt | 23.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 52.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -10.1) |
| [[LS 180 (line)]] | wt | 37.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 46.2 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.6) |
| [[C-33 A (line)]] | alt | 46.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -12.9) |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.7) |
| [[A-172 (line)]] | wt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -8.8) |
| [[A498 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -9.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 26.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -10.4) |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0929× (z -11.5) |
| [[HS-578T (line)]] | alt | 66.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.2) |
| [[SNU-423 (line)]] | alt | 52.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -15.4) |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[SW48 (line)]] | wt | 73.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.3) |
| [[A-427 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*24 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | +0.72 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TRABD]] | +0.72 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.69 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[FBXL16]] | +0.69 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.68 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[KYAT1]] | +0.67 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[TMEM120B]] | +0.66 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[BRF1]] | +0.66 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[ANKRD27]] | +0.65 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TCF3]] | +0.65 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[CEP131]] | +0.65 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[TPST2]] | +0.65 | +0.66 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*76 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | -0.77 | -0.73 / -0.52 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | -0.75 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[LINC02542]] | -0.74 | -0.75 / -0.30 | both halves | 2e-04 |  |
| [[MZF1-AS1]] | -0.74 | -0.72 / -0.36 | both halves | 9e-05 |  |
| [[KRCC1]] | -0.72 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[CTBP1-DT]] | -0.72 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | -0.71 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[METTL6]] | -0.71 | -0.70 / -0.35 | both halves | 1e-04 |  |
| [[SEPTIN7-DT]] | -0.71 | -0.67 / -0.30 | both halves | 2e-04 |  |
| [[ZNF747]] | -0.70 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[CLHC1]] | -0.69 | -0.70 / -0.21 | both halves | 7e-04 |  |
| [[MCTS1]] | -0.69 | -0.63 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHX6]] | B | LHX6 activity raises FAM118A's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.22× lower at baseline in the lines without LHX6 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers FAM118A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises FAM118A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FLG-AS1]] | B | FLG-AS1 activity raises FAM118A's level | lines that do not express FLG-AS1 (22) vs lines expressing it (28) | 1.02× lower at baseline in the lines without FLG-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: FLRT2, CNRIP1, MARCHF4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.0, 12.9); signed map (-40.9, -6.4). **Vector** length 93.2, 19.0% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +13.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.8 | +12.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +14.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.8 | -16.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -11.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | SIR2 antiphage like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:45,308,968-45,341,955 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIRal2, FLJ20635, bK268H5.C22.4; previously C22orf8, FAM118A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWS6](https://www.uniprot.org/uniprotkb/Q9NWS6) (SIR2 antiphage-like protein 2):

> Exhibits weak intrinsic NAD(+) nucleosidase activity, which is strongly stimulated upon interaction with its paralog SIRAL2 and the formation of SIRAL1-SIRAL2 filaments.

**Summary**, from NCBI Gene [55007](https://www.ncbi.nlm.nih.gov/gene/55007):

> Enables identical protein binding activity. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1313) · Entrez [55007](https://www.ncbi.nlm.nih.gov/gene/55007) · UniProt [Q9NWS6](https://www.uniprot.org/uniprotkb/Q9NWS6) · Ensembl [ENSG00000100376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100376)

## Data

Gene col 1943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1943); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1943]; `tensor/DDL_lfc|DDL_z.npy` [1943]; `embed/gene_vectors.npy` [1943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1943 or target_col == 1943). Every well: [[FAM118A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM118A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

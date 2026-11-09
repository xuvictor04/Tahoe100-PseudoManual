---
symbol: "PDE5A"
type: "gene"
col: 6221
ensembl_id: "ENSG00000138735"
name: "phosphodiesterase 5A"
location: "4q26"
module: 1
arm: "-"
pooled_cpm: 27.33
n_lines_expressing: 47
n_dd_up: 24
n_dd_down: 12
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PDE5A

*phosphodiesterase 5A* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +14.5, q 1e-44, up in 26 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.591× (z -11.2, q 4e-26, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGI3]] (+0.53, fdr 1e-05), [[CDS1]] (+0.52, fdr 3e-05), [[PLEKHA5]] (+0.52, fdr 1e-05); moves opposite to [[TERF2]] (-0.52, fdr 5e-05), [[EEFSEC]] (-0.50, fdr 6e-05), [[ZNG1F]] (-0.50, fdr 4e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EDIL3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC35C2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +14.5 | 1e-44 | 26/43 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +13.2 | 2e-37 | 26/45 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +12.4 | 4e-33 | 25/45 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +11.4 | 9e-28 | 29/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +8.0 | 2e-13 | 18/45 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.3 | 2e-11 | 14/36 (SNU-423, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +7.2 | 3e-11 | 19/45 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +6.8 | 6e-10 | 21/43 (HOP62, H4, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 4e-09 | 18/41 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +6.4 | 1e-08 | 13/44 (LoVo, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 1e-06 | 14/45 (NCI-H1573, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +5.3 | 6e-06 | 14/45 (H4, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.25×** | +4.8 | 9e-05 | 16/45 (H4, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.7 | 9e-05 | 15/44 (PANC-1, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 1e-04 | 15/44 (H4, PANC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 2e-04 | 16/45 (H4, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.591×** | -11.2 | 4e-26 | 27/45 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -9.4 | 2e-18 | 24/43 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.732×** | -9.3 | 2e-18 | 25/43 (Panc 03.27, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -7.5 | 1e-11 | 25/45 (BT-474, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.750×** | -6.1 | 1e-07 | 22/43 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -5.7 | 9e-07 | 21/44 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.764×** | -5.7 | 1e-06 | 20/45 (KATO III, A498, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.8 | 1e-04 | 3/45 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.802×** | -4.7 | 2e-04 | 19/43 (BT-474, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.814×** | -4.4 | 7e-04 | 12/45 (PANC-1, SW 1271, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.824×** | -4.0 | 0.004 | 14/44 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 0.846× | -3.6 | 0.017 | 5/44 (NCI-H460, SW 1271, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.848× | -3.3 | 0.049 | 14/41 (BT-474, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.049 | 3/45 (PANC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.728×** | -3.2 | 0.059 | 9/43 (PANC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 45.2 | 1 | 2 (2 ⚠) | [[Trametinib (drug)]] 0.5 µM 5.07× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0325× (z -30.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 22.8 | 2 | 1 | [[Panobinostat (drug)]] 0.05 µM 3.25× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 30.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 58.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -12.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.0) |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.108× (z -9.3) |
| [[LoVo (line)]] | wt | 43.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 49.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -20.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -13.4) |
| [[RKO (line)]] | wt | 16.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 7.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.8) | — |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGI3]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CDS1]] | +0.52 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[PLEKHA5]] | +0.52 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[RALGPS2]] | +0.52 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[L3MBTL3]] | +0.51 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.51 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RTN3]] | +0.50 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ROR2]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[VAV3]] | +0.49 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[GOLM1]] | +0.49 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[NXPE3]] | +0.48 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[CASTOR2]] | +0.48 | +0.39 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[EEFSEC]] | -0.50 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[ZNG1F]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[RPAP2]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SPOUT1]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MIOS]] | -0.47 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[POLI]] | -0.47 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[SLC35C2]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[UBIAD1]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ACSF3]] | -0.46 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[H6PD]] | -0.45 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[MYSM1]] | -0.45 | -0.46 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDIL3]] | B | EDIL3 activity raises PDE5A's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 1.42× lower at baseline in the lines without EDIL3 | 0.035 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[CELF2]] | B | CELF2 activity raises PDE5A's level | lines that do not express CELF2 (24) vs lines expressing it (26) | 1.45× lower at baseline in the lines without CELF2 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENPP5, LMO3, GNAT3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PDE5A's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35C2]] | C | PDE5A activity lowers SLC35C2's level | lines that do not express PDE5A (3) vs lines expressing it (47) | 1.84× higher at baseline in the lines without PDE5A | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: GPLD1, PDE4C, ZFHX2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.7, 13.6); signed map (-17.1, 28.8). **Vector** length 79.5, 14.3% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +14.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +13.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +3.6 | +0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -5.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.0 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -9.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:119,494,397-119,628,804 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 11 pathways, smallest: cGMP effects; Nitric oxide stimulates guanylate cyclase; RHOBTB1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O76074](https://www.uniprot.org/uniprotkb/O76074) (cGMP-specific 3',5'-cyclic phosphodiesterase):

> Plays a role in signal transduction by regulating the intracellular concentration of cyclic nucleotides. This phosphodiesterase catalyzes the specific hydrolysis of cGMP to 5'-GMP. Specifically regulates nitric-oxide-generated cGMP.

**Summary**, from NCBI Gene [8654](https://www.ncbi.nlm.nih.gov/gene/8654):

> This gene encodes a cGMP-binding, cGMP-specific phosphodiesterase, a member of the cyclic nucleotide phosphodiesterase family. This phosphodiesterase specifically hydrolyzes cGMP to 5'-GMP. It is involved in the regulation of intracellular concentrations of cyclic nucleotides and is important for smooth muscle relaxation in the cardiovascular system. Alternative splicing of this gene results in three transcript variants encoding distinct isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8784) · Entrez [8654](https://www.ncbi.nlm.nih.gov/gene/8654) · UniProt [O76074](https://www.uniprot.org/uniprotkb/O76074) · Ensembl [ENSG00000138735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138735)

## Data

Gene col 6221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6221); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6221]; `tensor/DDL_lfc|DDL_z.npy` [6221]; `embed/gene_vectors.npy` [6221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6221 or target_col == 6221). Every well: [[PDE5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

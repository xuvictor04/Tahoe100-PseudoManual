---
symbol: "SPATA20"
type: "gene"
col: 107
ensembl_id: "ENSG00000006282"
name: "spermatogenesis associated 20"
location: "17q21.33"
module: 96
arm: "+"
pooled_cpm: 9.55
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# SPATA20

*spermatogenesis associated 20* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.79× (z +13.7, q 4e-40, up in 27 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.36× (z +5.8, q 8e-07, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.590× (z -9.9, q 2e-20, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDUA]] (+0.68, fdr 1e-05), [[PPM1M]] (+0.65, fdr 1e-05), [[TKFC]] (+0.64, fdr 7e-06); moves opposite to [[MFSD11]] (-0.54, fdr 2e-05), [[KCNJ14]] (-0.49, fdr 1e-04), [[DHRS7B]] (-0.49, fdr 4e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALDH5A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +13.7 | 4e-40 | 27/30 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +13.2 | 2e-37 | 16/18 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +9.2 | 4e-18 | 15/22 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +5.8 | 8e-07 | 18/48 (CFPAC-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.4 | 0.002 | 11/37 (J82, SW48, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.007 | 6/44 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.7 | 0.014 | 8/37 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.7 | 0.014 | 7/25 (A-172, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.014 | 10/35 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.017 | 7/44 (A-172, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.024 | 8/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.024 | 9/46 (NCI-H1792, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.038 | 6/47 (BT-474, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.590×** | -9.9 | 2e-20 | 31/46 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -7.1 | 3e-10 | 28/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -7.1 | 3e-10 | 25/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -6.6 | 6e-09 | 26/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -6.5 | 7e-09 | 23/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -6.0 | 2e-07 | 25/47 (Panc 03.27, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -5.7 | 9e-07 | 19/47 (BT-474, NCI-H460, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.642×** | -5.6 | 2e-06 | 24/44 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.655×** | -5.4 | 4e-06 | 21/46 (SK-MEL-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.699×** | -4.8 | 1e-04 | 17/47 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.726×** | -4.3 | 0.001 | 17/43 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.733×** | -4.1 | 0.002 | 15/47 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.746×** | -3.9 | 0.004 | 19/47 (SW1417, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.747×** | -3.9 | 0.004 | 9/47 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.006 | 17/47 (SHP-77, AN3 CA, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.772×** | -3.4 | 0.019 | 13/47 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.705×** | -3.3 | 0.026 | 6/46 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.783×** | -3.3 | 0.032 | 13/46 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -3.1 | 0.050 | 13/48 (SNU-423, Panc 03.27, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 14.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.1) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.298× (z -9.0) |
| [[A549 (line)]] | wt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.1) |
| [[C32 (line)]] | wt | 9.81 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.138× (z -9.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 4.92 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0759× (z -9.2) |
| [[HS-578T (line)]] | alt | 8.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 8.12 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0701× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 6.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 7.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 5.26 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0457× (z -9.8) |
| [[SNU-423 (line)]] | alt | 6.13 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.104× (z -8.7) |
| [[A-172 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDUA]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[PPM1M]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TKFC]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ALDH5A1]] | +0.64 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[TSPAN6]] | +0.60 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[GAA]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZBED6]] | +0.58 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ARPIN]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ZMYM3]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PIGO]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD11]] | -0.54 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[KCNJ14]] | -0.49 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[DHRS7B]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[SEC61G]] | -0.49 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[ING2]] | -0.48 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[SELENOK]] | -0.48 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH5A1]] | B | ALDH5A1 activity raises SPATA20's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without ALDH5A1 | 0.096 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-27.8, 23.7); signed map (16.0, -43.1). **Vector** length 62.5, 9.30% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.1 | +5.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +4.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -7.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -1.7 | -3.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.2 | +0.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,543,058-50,555,852 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21347, SSP411, Tisp78 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB22](https://www.uniprot.org/uniprotkb/Q8TB22) (Spermatogenesis-associated protein 20):

> May play a role in fertility regulation.

**Summary**, from NCBI Gene [64847](https://www.ncbi.nlm.nih.gov/gene/64847):

> Predicted to be involved in carbohydrate metabolic process; cell differentiation; and spermatogenesis. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26125) · Entrez [64847](https://www.ncbi.nlm.nih.gov/gene/64847) · UniProt [Q8TB22](https://www.uniprot.org/uniprotkb/Q8TB22) · Ensembl [ENSG00000006282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006282)

## Data

Gene col 107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 107); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 107]; `tensor/DDL_lfc|DDL_z.npy` [107]; `embed/gene_vectors.npy` [107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 107 or target_col == 107). Every well: [[SPATA20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

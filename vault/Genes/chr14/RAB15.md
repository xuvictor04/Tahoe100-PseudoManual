---
symbol: "RAB15"
type: "gene"
col: 6364
ensembl_id: "ENSG00000139998"
name: "RAB15, member RAS oncogene family"
location: "14q23.3"
module: 44
arm: "+"
pooled_cpm: 5.9
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# RAB15

*RAB15, member RAS oncogene family* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.96× (z +13.7, q 1e-39, up in 7 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 0.05 µM: 1.37× (z +3.8, q 0.013, up in 9 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.411× (z -11.7, q 1e-28, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XK]] (+0.62, fdr 1e-05), [[TP53I11]] (+0.62, fdr 1e-05), [[NPNT]] (+0.62, fdr 4e-05); moves opposite to [[ZMYM6]] (-0.54, fdr 4e-05), [[SCFD1]] (-0.49, fdr 4e-05), [[NOSIP]] (-0.49, fdr 9e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MUC5B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +13.7 | 1e-39 | 7/8 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +12.0 | 7e-31 | 17/23 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +12.0 | 1e-30 | 11/14 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.4 | 0.002 | 9/29 (LS 180, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.0 | 0.006 | 5/29 (A-172, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.013 | 9/39 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.015 | 3/27 (SW480, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.057 | 6/37 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 1.27× | +3.1 | 0.12 | 3/44 (LoVo, J82, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.12 | 3/44 (C-33 A, NCI-H2347, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.12 | 3/40 (SW1417, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.411×** | -11.7 | 1e-28 | 32/46 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.598×** | -9.5 | 5e-19 | 24/39 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.531×** | -8.3 | 2e-14 | 24/46 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -8.0 | 2e-13 | 22/37 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -6.9 | 5e-10 | 25/45 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.591×** | -6.9 | 5e-10 | 18/46 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.672×** | -5.0 | 4e-05 | 17/42 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -4.8 | 1e-04 | 15/37 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Naproxen (drug)]] 5 µM |  | **0.736×** | -3.9 | 0.007 | 12/43 (HEC-1-A, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.575×** | -3.5 | 0.024 | 10/43 (RKO, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.597×** | -3.3 | 0.051 | 8/44 (KATO III, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 12.9 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.118× (z -11.7) |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0307× (z -14.3) |
| [[LoVo (line)]] | wt | 9.01 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.7) |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.145× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 7.94 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +8.5) ⚠ toxic; transcription drop | [[Orlistat (drug)]] 0.05 µM 0.101× (z -10.9) |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0472× (z -8.9) |
| [[C32 (line)]] | wt | 4.79 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0733× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 7.35 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.119× (z -9.1) |
| [[J82 (line)]] | alt | 3.25 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0584× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 3.07 | 0 | 1 | — | [[Artemether (drug)]] 0.5 µM 0.0663× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 6.17 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 1.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0941× (z -8.6) |
| [[RKO (line)]] | wt | 9.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -8.9) |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0644× (z -8.8) |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -9.1) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XK]] | +0.62 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TP53I11]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[NPNT]] | +0.62 | +0.57 / +0.43 | both halves | 4e-05 |  |
| [[DENND2D]] | +0.61 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CFTR]] | +0.60 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[PLBD1]] | +0.58 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[LRP4]] | +0.57 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[TSPAN8]] | +0.56 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[TMEM98]] | +0.56 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[SRC]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SYK]] | +0.56 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SPINT1-AS1]] | +0.55 | +0.53 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM6]] | -0.54 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[SCFD1]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[NOSIP]] | -0.49 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[DIS3]] | -0.48 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[LGALS1]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC5B]] | B | MUC5B activity raises RAB15's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.54× lower at baseline in the lines without MUC5B | 0.065 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises RAB15's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 1.64× lower at baseline in the lines without TMPRSS2 | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TMEM30B]] | B | TMEM30B activity raises RAB15's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 1.74× lower at baseline in the lines without TMEM30B | 0.079 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[CLIC5]] | B | CLIC5 activity raises RAB15's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 1.55× lower at baseline in the lines without CLIC5 | 0.097 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, 49.6); signed map (65.7, 3.6). **Vector** length 57.7, 8.00% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +12.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | -1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.3 | -8.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RAB15, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,945,814-64,973,226 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P59190](https://www.uniprot.org/uniprotkb/P59190) (Ras-related protein Rab-15):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes (By similarity). Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB15 may act in concert with RAB3A in regulating aspects of synaptic vesicle membrane …

**Summary**, from NCBI Gene [376267](https://www.ncbi.nlm.nih.gov/gene/376267):

> Enables G protein activity. Involved in positive regulation of regulated secretory pathway and receptor-mediated endocytosis. Located in cilium; endosome membrane; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20150) · Entrez [376267](https://www.ncbi.nlm.nih.gov/gene/376267) · UniProt [P59190](https://www.uniprot.org/uniprotkb/P59190) · Ensembl [ENSG00000139998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139998)

## Data

Gene col 6364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6364); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6364]; `tensor/DDL_lfc|DDL_z.npy` [6364]; `embed/gene_vectors.npy` [6364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6364 or target_col == 6364). Every well: [[RAB15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

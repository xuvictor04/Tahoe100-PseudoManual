---
symbol: "SLC35C2"
type: "gene"
col: 1275
ensembl_id: "ENSG00000080189"
name: "solute carrier family 35 member H1"
location: "20q13.12"
module: 182
arm: "-"
pooled_cpm: 52.1
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# SLC35C2

*solute carrier family 35 member H1* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.16× (z +8.2, q 1e-13, up in 4 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.40× (z +7.6, q 7e-12, up in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (A-172 2.74×, NCI-H460 2.25×, CFPAC-1 2.35×, BT-474 2.61×, …).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.656× (z -9.7, q 2e-19, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC30A7]] (+0.64, fdr 7e-06), [[PNKP]] (+0.57, fdr 1e-05), [[SETX]] (+0.57, fdr 2e-05); moves opposite to [[SMAD5]] (-0.61, fdr 1e-05), [[GNAI1]] (-0.60, fdr 1e-05), [[PDK1]] (-0.55, fdr 2e-05).
> It sits in the **-** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDE5A]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1275.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (A-172 2.74×, NCI-H460 2.25×, CFPAC-1 2.35×, BT-474 2.61×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +8.2 | 1e-13 | 4/49 (COLO 205, RPMI-7951, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +7.6 | 7e-12 | 27/47 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.43 | 17/48 (SHP-77, RPMI-7951, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -9.7 | 2e-19 | 37/48 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -5.8 | 2e-06 | 33/48 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.711×** | -5.5 | 6e-06 | 35/48 (BT-474, KATO III, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -5.2 | 2e-05 | 29/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **0.754×** | -4.6 | 6e-04 | 26/48 (C-33 A, NCI-H23, …) | two highest doses | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.777×** | -4.1 | 0.004 | 26/48 (A-172, LoVo, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.779×** | -4.0 | 0.004 | 24/48 (SW480, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.693×** | -4.0 | 0.004 | 25/41 (SNU-1, NCI-H23, …) | two highest doses | composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -3.9 | 0.006 | 24/48 (HT-29, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.791×** | -3.8 | 0.008 | 23/49 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.642×** | -3.7 | 0.009 | 21/48 (HEC-1-A, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -3.7 | 0.011 | 22/48 (RPMI-7951, LoVo, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.831×** | -3.6 | 0.012 | 19/48 (CHP-212, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.658×** | -3.5 | 0.016 | 19/48 (SNU-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -3.5 | 0.016 | 16/48 (KATO III, NCI-H23, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.664×** | -3.5 | 0.019 | 19/47 (NCI-H661, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.670×** | -3.4 | 0.023 | 19/47 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.813×** | -3.3 | 0.024 | 19/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.683×** | -3.2 | 0.032 | 18/48 (A498, CHP-212, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 105 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.2) |
| [[RKO (line)]] | wt | 71.0 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -15.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -13.6) |
| [[SNU-1 (line)]] | wt | 73.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -13.3) |
| [[SW480 (line)]] | alt | 58.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.459× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 38.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 42.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 63.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0655× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[CFPAC-1 (line)]] | alt | 37.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.0) | — |
| [[H4 (line)]] | wt | 52.4 | 0 | 1 | — | [[LJI308 (drug)]] 5 µM 0.0698× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[HOP62 (line)]] | alt | 34.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.1) | — |
| [[J82 (line)]] | alt | 57.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 49.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 56.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 41.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.2) | — |
| [[NCI-H661 (line)]] | alt | 33.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0780× (z -8.5) |
| [[PANC-1 (line)]] | alt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SW 900 (line)]] | alt | 39.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 89.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.8) |
| [[A-427 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A7]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[PNKP]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SETX]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ERCC1]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[RNF123]] | +0.57 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[DELE1]] | +0.56 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[PILRB]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[EGR3]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[REXO1]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MYO1C]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[DNAH1]] | +0.53 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[RBMXL1]] | +0.53 | +0.55 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD5]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[GNAI1]] | -0.60 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[PDK1]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PPP2R5A]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ARL6IP5]] | -0.55 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[PPP2R5E]] | -0.55 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[DCAF5]] | -0.54 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[SEPTIN7]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZNF148]] | -0.53 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[CAPZA2]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[RELCH]] | -0.53 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[NPEPPS]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE5A]] | C | PDE5A activity lowers SLC35C2's level | lines that do not express PDE5A (3) vs lines expressing it (47) | 1.84× higher at baseline in the lines without PDE5A | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: GPLD1, PDE4C, ZFHX2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.3, -5.6); signed map (4.6, 26.4). **Vector** length 99.9, 25.8% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +7.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +0.8 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.6 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member H1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:46,345,980-46,364,458 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-15, bA394O2.1; previously C20orf5, OVCOV1, SLC35C2 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQQ7](https://www.uniprot.org/uniprotkb/Q9NQQ7) (Solute carrier family 35 member H1):

> Putative GDP-fucose transporter.

**Summary**, from NCBI Gene [51006](https://www.ncbi.nlm.nih.gov/gene/51006):

> This gene encodes a member of the triose-phosphate transporter protein family. This gene is regulated by oxygen tension, is induced in hypoxic trophoblast cells, and is overexpressed in ovarian cancer. Alternative splicing results in multiple transcript variants. A pseudogene of this gene has been defined on the X chromosome. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:17117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17117) · Entrez [51006](https://www.ncbi.nlm.nih.gov/gene/51006) · UniProt [Q9NQQ7](https://www.uniprot.org/uniprotkb/Q9NQQ7) · Ensembl [ENSG00000080189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080189)

## Data

Gene col 1275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1275); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1275]; `tensor/DDL_lfc|DDL_z.npy` [1275]; `embed/gene_vectors.npy` [1275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1275 or target_col == 1275). Every well: [[SLC35C2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35C2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

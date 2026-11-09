---
symbol: "PLPPR2"
type: "gene"
col: 2616
ensembl_id: "ENSG00000105520"
name: "phospholipid phosphatase related 2"
location: "19p13.2"
module: 85
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# PLPPR2

*phospholipid phosphatase related 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.95× (z +13.6, q 1e-39, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.727× (z -5.7, q 6e-06, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCIRG1]] (+0.71, fdr 1e-05), [[GNAI2]] (+0.69, fdr 2e-04), [[PIGH]] (+0.68, fdr 1e-05); moves opposite to [[YARS2]] (-0.62, fdr 1e-04), [[GALNT7-DT]] (-0.59, fdr 4e-04), [[OTUD4]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.95×** | +13.6 | 1e-39 | 43/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.81×** | +13.0 | 2e-36 | 42/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.40×** | +11.0 | 5e-26 | 40/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +10.1 | 8e-22 | 19/24 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.9 | 4e-21 | 6/12 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +6.3 | 3e-08 | 21/46 (A498, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +6.1 | 1e-07 | 20/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.1 | 3e-05 | 13/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +4.9 | 5e-05 | 12/40 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.6 | 2e-04 | 10/32 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.002 | 9/45 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.016 | 3/41 (A498, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.3 | 0.041 | 7/41 (SW 900, SNU-423, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.050 | 4/45 (C32, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.36×** | +3.2 | 0.050 | 4/19 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.061 | 2/47 (RKO, SW480) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.061 | 5/38 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -5.7 | 6e-06 | 22/41 (Hs 766T, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -4.5 | 0.002 | 11/40 (SW 900, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.783×** | -4.4 | 0.002 | 18/48 (Hs 766T, A498, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.702×** | -4.3 | 0.002 | 15/43 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -3.8 | 0.017 | 10/40 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.530×** | -3.7 | 0.021 | 9/38 (HOP62, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.750×** | -3.6 | 0.021 | 13/40 (hTERT-HPNE, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.752×** | -3.6 | 0.021 | 12/46 (SNU-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.754×** | -3.6 | 0.022 | 11/47 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.059 | 11/47 (LS 180, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 6.63 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0754× (z -9.2) |
| [[A-172 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCIRG1]] | +0.71 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.69 | +0.60 / +0.31 | both halves | 2e-04 |  |
| [[PIGH]] | +0.68 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[KCTD17]] | +0.67 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[YIF1B]] | +0.66 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[RING1]] | +0.65 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GGCX]] | +0.65 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[BAIAP3]] | +0.64 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[MAST3]] | +0.64 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[FCHO1]] | +0.63 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[SKIC2]] | +0.63 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[GDI1]] | +0.62 | +0.66 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YARS2]] | -0.62 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[GALNT7-DT]] | -0.59 | -0.36 / -0.24 | both halves | 4e-04 |  |
| [[OTUD4]] | -0.59 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GABPB1-AS1]] | -0.58 | -0.51 / -0.20 | both halves | 7e-04 |  |
| [[CRPPA]] | -0.58 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[KLHL42]] | -0.58 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[ANGEL2]] | -0.57 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[CPSF2]] | -0.56 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[PSME3IP1]] | -0.56 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[NINJ2]] | -0.56 | -0.39 / -0.06 | ⚠ not reproduced | 0.004 |  |
| [[GNG12-AS1]] | -0.55 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[CCDC122]] | -0.55 | -0.39 / -0.26 | both halves | 4e-04 |  |
| [[MMADHC-DT]] | -0.55 | -0.28 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PLPPR2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RHPN1]] | B | RHPN1 activity lowers PLPPR2's level | lines that do not express RHPN1 (7) vs lines expressing it (43) | 2.11× higher at baseline in the lines without RHPN1 | 0.084 | ⚠ within organs, on part of the lines; also absent: RHOF, LRRC8B, MBP; maybe low, not absent; its own permutation p |
| [[LMTK3]] | B | LMTK3 activity lowers PLPPR2's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.59× higher at baseline in the lines without LMTK3 | 0.086 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.5, -4.7); signed map (-30.5, 0.7). **Vector** length 65.2, 10.4% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +13.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +13.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid phosphatase related 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,355,386-11,365,698 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LPPR2, PRG-4 |
| Gene groups (HGNC) | Phospholipid phosphatase related |
| Reactome | 4 pathways, smallest: Lysosphingolipid and LPA receptors; Class A/1 (Rhodopsin-like receptors); GPCR ligand binding |
| Matched by | ensembl_id |

UniProt [Q96GM1](https://www.uniprot.org/uniprotkb/Q96GM1) carries no function annotation.

**Summary**, from NCBI Gene [64748](https://www.ncbi.nlm.nih.gov/gene/64748):

> Predicted to enable phosphatidate phosphatase activity. Predicted to be involved in phospholipid dephosphorylation; phospholipid metabolic process; and signal transduction. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29566) · Entrez [64748](https://www.ncbi.nlm.nih.gov/gene/64748) · UniProt [Q96GM1](https://www.uniprot.org/uniprotkb/Q96GM1) · Ensembl [ENSG00000105520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105520)

## Data

Gene col 2616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2616); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2616]; `tensor/DDL_lfc|DDL_z.npy` [2616]; `embed/gene_vectors.npy` [2616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2616 or target_col == 2616). Every well: [[PLPPR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLPPR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

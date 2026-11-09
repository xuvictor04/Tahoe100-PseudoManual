---
symbol: "FLYWCH2"
type: "gene"
col: 8478
ensembl_id: "ENSG00000162076"
name: "FLYWCH family member 2"
location: "16p13.3"
module: 30
arm: "+"
pooled_cpm: 7.4
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# FLYWCH2

*FLYWCH family member 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.51× (z +10.5, q 6e-23, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.639× (z -7.3, q 2e-10, down in 30 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC45A]] (+0.71, fdr 7e-06), [[RAP1A]] (+0.70, fdr 1e-05), [[LCMT1]] (+0.68, fdr 7e-06); moves opposite to [[SLC2A9]] (-0.67, fdr 1e-05), [[ST7L]] (-0.63, fdr 2e-05), [[ZC3H4]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GPR39]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.51×** | +10.5 | 6e-23 | 41/47 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.14×** | +8.7 | 1e-15 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +8.3 | 2e-14 | 37/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.3 | 3e-11 | 9/11 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +7.0 | 3e-10 | 22/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.7 | 2e-09 | 26/42 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 2e-05 | 21/42 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.5 | 6e-04 | 15/36 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.47×** | +4.2 | 0.001 | 11/37 (LoVo, NCI-H1573, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.029 | 8/37 (NCI-H460, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.036 | 9/47 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.34×** | +3.1 | 0.090 | 10/20 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.090 | 5/38 (HS-578T, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -7.3 | 2e-10 | 30/44 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.550×** | -6.9 | 2e-09 | 26/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.582×** | -6.2 | 9e-08 | 25/46 (BT-474, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.626×** | -5.4 | 1e-05 | 22/43 (HS-578T, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -4.3 | 0.002 | 16/46 (LOX-IMVI, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.528×** | -3.8 | 0.012 | 15/45 (NCI-H1792, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.718×** | -3.7 | 0.019 | 14/45 (BT-474, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.604× | -3.0 | 0.16 | 14/41 (hTERT-HPNE, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.770× | -3.0 | 0.16 | 16/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 4.11 | 0 | 2 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0642× (z -9.3) |
| [[A549 (line)]] | wt | 5.99 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0527× (z -11.8) |
| [[HS-578T (line)]] | alt | 6.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0622× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 5.58 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.106× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 6.65 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +8.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -8.7) |
| [[SHP-77 (line)]] | alt | 9.02 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.117× (z -8.9) |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC45A]] | +0.71 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RAP1A]] | +0.70 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.68 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ARL3]] | +0.67 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[CCZ1B]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[MMS19]] | +0.67 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.67 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[SLC9A6]] | +0.67 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[CCZ1]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TMEM219]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[SNX1]] | +0.64 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A9]] | -0.67 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ST7L]] | -0.63 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZC3H4]] | -0.62 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[PARD6G-AS1]] | -0.62 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[MYH15]] | -0.61 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.61 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[SSUH2]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TASOR]] | -0.60 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[RGS5]] | -0.59 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LINC02516]] | -0.59 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[RABL3]] | -0.59 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.59 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR39]] | B | GPR39 activity lowers FLYWCH2's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 1.48× higher at baseline in the lines without GPR39 | 0.003 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[PLEKHA6]] | B | PLEKHA6 activity lowers FLYWCH2's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.31× higher at baseline in the lines without PLEKHA6 | 0.003 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[SLC2A9]] | B | SLC2A9 activity lowers FLYWCH2's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.50× higher at baseline in the lines without SLC2A9 | 0.008 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[SSUH2]] | C | SSUH2 activity lowers FLYWCH2's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 1.75× higher at baseline in the lines without SSUH2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (3.1, -12.4); signed map (-37.7, -0.4). **Vector** length 57.2, 7.89% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +10.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.4 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.0 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[palbociclib (drug)]] 0.05 µM |  | +1.1 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.7 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | FLYWCH family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,883,213-2,899,382 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | FLYWCH family |
| Matched by | ensembl_id |

UniProt [Q96CP2](https://www.uniprot.org/uniprotkb/Q96CP2) carries no function annotation.

**Summary**, from NCBI Gene [114984](https://www.ncbi.nlm.nih.gov/gene/114984):

> Enables RNA binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25178) · Entrez [114984](https://www.ncbi.nlm.nih.gov/gene/114984) · UniProt [Q96CP2](https://www.uniprot.org/uniprotkb/Q96CP2) · Ensembl [ENSG00000162076](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162076)

## Data

Gene col 8478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8478); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8478]; `tensor/DDL_lfc|DDL_z.npy` [8478]; `embed/gene_vectors.npy` [8478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8478 or target_col == 8478). Every well: [[FLYWCH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLYWCH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

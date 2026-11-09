---
symbol: "DPH3"
type: "gene"
col: 7841
ensembl_id: "ENSG00000154813"
name: "diphthamide biosynthesis 3"
location: "3p25.1"
module: 7
arm: "+"
pooled_cpm: 12.97
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DPH3

*diphthamide biosynthesis 3* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (24 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.71× (z +15.4, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Entecavir (monohydrate) (drug)]] 5 µM: 0.742× (z -4.4, q 0.005, down in 11 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERVK13-1]] (+0.57, fdr 2e-05), [[FASTKD5]] (+0.56, fdr 2e-05), [[BAG5]] (+0.55, fdr 3e-05); moves opposite to [[PTMA]] (-0.53, fdr 3e-05), [[MTF2]] (-0.49, fdr 3e-05), [[CHEK2]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 26 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.71×** | +15.4 | 0e+00 | 43/47 (HOP62, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.46×** | +14.0 | 9e-42 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.50×** | +13.1 | 5e-37 | 28/32 (NCI-H460, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.39×** | +13.0 | 2e-36 | 19/24 (J82, A-172, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +12.8 | 2e-35 | 36/40 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +12.4 | 2e-33 | 39/44 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +12.1 | 1e-31 | 39/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.70×** | +11.6 | 2e-29 | 39/46 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.11×** | +11.5 | 5e-29 | 29/36 (SK-MEL-2, LoVo, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.02×** | +10.9 | 6e-26 | 39/47 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.96×** | +10.4 | 1e-23 | 36/44 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.93×** | +10.2 | 1e-22 | 39/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.96×** | +9.9 | 2e-21 | 36/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.18×** | +9.4 | 3e-19 | 40/48 (PANC-1, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.80×** | +9.1 | 2e-18 | 36/47 (SW480, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +8.5 | 5e-16 | 31/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +7.0 | 1e-10 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.9 | 1e-10 | 28/48 (HOP62, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +6.5 | 2e-09 | 20/43 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +5.8 | 2e-07 | 20/47 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.7 | 6e-05 | 17/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.001 | 12/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.003 | 12/47 (NCI-H2030, LS 180, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.019 | 4/48 (SNU-423, LS 180, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7841.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.742×** | -4.4 | 0.005 | 11/48 (RPMI-7951, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.849× | -3.6 | 0.10 | 15/48 (A498, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.4 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 20.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.41× (z +9.9) | — |
| [[LoVo (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.24× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 8.82 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.54× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[SNU-423 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +8.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK13-1]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[FASTKD5]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[BAG5]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TMEM199]] | +0.54 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[UNC50]] | +0.53 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[PSMC4]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ACTR1A]] | +0.52 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[SNX19]] | +0.52 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ARL16]] | +0.51 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[DCTN5]] | +0.51 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[SOCS4]] | +0.50 | +0.59 / +0.37 | both halves | 9e-05 |  |
| [[FBXO30]] | +0.50 | +0.46 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMA]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[MTF2]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[CHEK2]] | -0.49 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[MNS1]] | -0.47 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PLLP]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[SOX13]] | -0.45 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[SCML2]] | -0.45 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[RPL22L1]] ⚠ | -0.44 | -0.23 / -0.39 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ORC4]] | -0.44 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[EPHB3]] | -0.43 | -0.21 / -0.39 | both halves | 6e-04 |  |
| [[TCAF1]] | -0.43 | -0.16 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[TEC]] | -0.43 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[ALDH7A1]] | -0.42 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[CNNM4]] | -0.42 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPH3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-28.7, -11.3); signed map (-7.9, -27.2). **Vector** length 54.5, 8.47% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.0 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.6 | +13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +2.8 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +4.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | -1.4 | +6.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -0.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | diphthamide biosynthesis 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:16,257,061-16,264,969 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DESR1, DELGIP1, MGC20197, KTI11, DELGIP, DPH3A; previously ZCSL2 |
| Gene groups (HGNC) | Diphthamide biosynthesis genes |
| Reactome | 2 pathways, smallest: Synthesis of diphthamide-EEF2; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FX2](https://www.uniprot.org/uniprotkb/Q96FX2) (Diphthamide biosynthesis protein 3):

> Required for the first step of diphthamide biosynthesis, a post-translational modification of histidine which occurs in elongation factor 2. DPH1 and DPH2 transfer a 3-amino-3-carboxypropyl (ACP) group from S-adenosyl-L-methionine (SAM) to a histidine residue, the reaction is assisted by a reduction system comprising DPH3 and a NADH-dependent reductase. Acts as an electron donor to reduce the Fe-S cluster in DPH1-DPH2 keeping the [4Fe-4S] clusters in the active and reduced state. Restores iron …

**Summary**, from NCBI Gene [285381](https://www.ncbi.nlm.nih.gov/gene/285381):

> This gene encodes a CSL zinc finger-containing protein that is required for dipthamide biosynthesis. The encoded protein is necessary for the initial step in the modification of a histidine residue in elongation factor-2 to diphthamide. This modified residue is a target for ADP ribosylation by the bacterial toxins diphtheria toxin and Pseudomonas exotoxin A. Alternative splicing results in multiple transcript variants that encode the same isoform. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:27717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27717) · Entrez [285381](https://www.ncbi.nlm.nih.gov/gene/285381) · UniProt [Q96FX2](https://www.uniprot.org/uniprotkb/Q96FX2) · Ensembl [ENSG00000154813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154813)

## Data

Gene col 7841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7841); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7841]; `tensor/DDL_lfc|DDL_z.npy` [7841]; `embed/gene_vectors.npy` [7841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7841 or target_col == 7841). Every well: [[DPH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

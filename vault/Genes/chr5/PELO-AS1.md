---
symbol: "PELO-AS1"
type: "gene"
col: 14577
ensembl_id: "ENSG00000248898"
name: "PELO antisense RNA 1"
location: "5q11.2"
module: 26
arm: "+"
pooled_cpm: 5.69
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 21
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PELO-AS1

*PELO antisense RNA 1* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.21× (z +29.7, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.511× (z -7.4, q 1e-10, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.80, fdr 7e-06), [[DARS1-AS1]] (+0.80, fdr 7e-06), [[SAXO1]] (+0.77, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.21×** | +29.7 | 0e+00 | 37/37 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.38×** | +14.1 | 1e-42 | 28/46 (HS-578T, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +13.4 | 9e-39 | 27/36 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.37×** | +13.3 | 4e-38 | 37/43 (LoVo, HT-29, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +9.9 | 6e-21 | 24/39 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +5.4 | 7e-06 | 15/45 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +5.0 | 4e-05 | 17/45 (NCI-H23, A498, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **2.20×** | +4.7 | 1e-04 | 7/32 (SW 900, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.7 | 1e-04 | 1/12 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +4.3 | 0.001 | 13/46 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.2 | 0.001 | 14/44 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.001 | 10/46 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.001 | 14/46 (SW480, SW1417, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.004 | 10/42 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.011 | 7/46 (A498, HepG2/C3A, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.030 | 12/42 (KATO III, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14577.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -7.4 | 1e-10 | 24/46 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -4.9 | 3e-04 | 14/42 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -4.8 | 4e-04 | 14/43 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.685×** | -4.4 | 0.002 | 14/44 (KATO III, COLO 205, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.513×** | -4.0 | 0.007 | 12/37 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.701×** | -3.9 | 0.009 | 15/44 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.735×** | -3.6 | 0.030 | 9/46 (PANC-1, A498, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.741×** | -3.3 | 0.059 | 12/33 (LoVo, A498, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.582×** | -3.3 | 0.069 | 9/30 (J82, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 5.93 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +9.0) | [[Trifluridine (drug)]] 0.5 µM 0.0714× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.105× (z -8.6) |
| [[SW480 (line)]] | alt | 6.53 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 10.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 10.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.94× (z +12.6) | — |
| [[LoVo (line)]] | wt | 8.34 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.52× (z +10.9) | — |
| [[A-172 (line)]] | wt | 4.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.31× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 2.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 5.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 4.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.74× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 7.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.08× (z +11.7) | — |
| [[KATO III (line)]] | alt | 5.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 2.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 5.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 4.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.83× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 2.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 6.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 4.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +15.5) | — |
| [[Panc 03.27 (line)]] | alt | 3.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.50× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.85× (z +13.0) | — |
| [[RKO (line)]] | wt | 5.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 5.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.13× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.47× (z +9.1) | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.80 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[DARS1-AS1]] | +0.80 | +0.71 / +0.66 | both halves | 7e-06 | same gene group |
| [[SAXO1]] | +0.77 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.75 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[LINC01762]] | +0.74 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[GLIPR1-AS1]] | +0.74 | +0.67 / +0.59 | both halves | 7e-06 | same gene group |
| [[HLA-DMA]] | +0.74 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.73 | +0.67 / +0.65 | both halves | 7e-06 | same gene group |
| [[LINC01482]] | +0.73 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[LNP1]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SPESP1]] | +0.70 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[MGAM]] | +0.70 | +0.71 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PELO-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IQCJ]] | B | IQCJ activity raises PELO-AS1's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without IQCJ | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[LINC01762]] | B | LINC01762 activity raises PELO-AS1's level | lines that do not express LINC01762 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without LINC01762 | 0.060 | ⚠ within organs, on part of the lines; also absent: MPP4, LINC01429, DNAH6; maybe low, not absent |
| [[CA3]] | B | CA3 activity raises PELO-AS1's level | lines that do not express CA3 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without CA3 | 0.065 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2 |
| [[WDR49]] | C | WDR49 activity raises PELO-AS1's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without WDR49 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.3, 18.5); signed map (25.2, -1.8). **Vector** length 72.7, 12.3% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +29.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.1 | +13.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +4.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.6 | +4.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +1.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | PELO antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q11.2 — chr5:52,673,186-52,799,987 (-) |
| Ensembl biotype | lncRNA |
| Also known as | CTD-2288O8.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56263) · Entrez [125775243](https://www.ncbi.nlm.nih.gov/gene/125775243) · Ensembl [ENSG00000248898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248898)

## Data

Gene col 14577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14577); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14577]; `tensor/DDL_lfc|DDL_z.npy` [14577]; `embed/gene_vectors.npy` [14577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14577 or target_col == 14577). Every well: [[PELO-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PELO-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

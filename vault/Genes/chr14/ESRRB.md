---
symbol: "ESRRB"
type: "gene"
col: 4109
ensembl_id: "ENSG00000119715"
name: "estrogen related receptor beta"
location: "14q24.3"
module: 26
arm: "+"
pooled_cpm: 3.33
n_lines_expressing: 45
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ESRRB

*estrogen related receptor beta* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.23× (z +18.1, q 0e+00, up in 29 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.383× (z -4.5, q 0.004, down in 10 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H1573 0.0552×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.117×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH10]] (+0.75, fdr 7e-06), [[PKD1L1]] (+0.73, fdr 7e-06), [[LINC02646]] (+0.72, fdr 7e-06); moves opposite to [[L2HGDH]] (-0.59, fdr 3e-05), [[KLHL8]] (-0.57, fdr 1e-04), [[GLMN]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02306]] → it (grade B ⚠); 2 go from it, the strongest it → [[ALOX12-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.23×** | +18.1 | 0e+00 | 29/33 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **7.22×** | +17.5 | 0e+00 | 37/40 (SW480, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +12.0 | 6e-31 | 22/31 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.45×** | +11.0 | 5e-26 | 21/29 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +9.8 | 9e-21 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.61×** | +8.5 | 1e-15 | 28/42 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.91×** | +8.1 | 3e-14 | 20/41 (A-172, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +6.4 | 1e-08 | 13/34 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +6.1 | 7e-08 | 19/40 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +6.1 | 7e-08 | 19/40 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.6 | 1e-06 | 12/26 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.66×** | +4.5 | 3e-04 | 6/37 (C32, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +4.4 | 5e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.001 | 9/41 (SW480, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +4.1 | 0.001 | 9/35 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +4.0 | 0.002 | 13/37 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +3.5 | 0.015 | 11/41 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4109.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H1573 0.0552×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.117×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.383×** | -4.5 | 0.004 | 10/27 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.767× | -3.4 | 0.23 | 12/39 (CFPAC-1, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.65 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.37× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.117× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 1.89 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +13.0) | [[Belumosudil (drug)]] 5 µM 0.0552× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 6.13 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +11.3) | — |
| [[C32 (line)]] | wt | 8.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 2.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 6.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 2.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +9.0) | — |
| [[SW48 (line)]] | wt | 6.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +10.3) | — |
| [[SW480 (line)]] | alt | 2.96 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.2× (z +9.6) | — |
| [[A-172 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.849 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH10]] | +0.75 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[NEB]] | +0.72 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[LINC01422]] | +0.72 | +0.56 / +0.78 | both halves | 1e-05 |  |
| [[COLQ]] | +0.71 | +0.81 / +0.58 | both halves | 8e-06 |  |
| [[LINC00907]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ST8SIA5]] | +0.70 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[LINC01252]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CAVIN4]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.67 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[LINC01618]] | +0.66 | +0.71 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.59 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[KLHL8]] | -0.57 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[GLMN]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[COPG2]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02306]] | B | LINC02306 activity raises ESRRB's level | lines that do not express LINC02306 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without LINC02306 | 0.027 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ESRRB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02112]] | B | LINC02112 activity raises ESRRB's level | lines that do not express LINC02112 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without LINC02112 | 0.048 | ⚠ within organs, on part of the lines; also absent: DNAH6, IQCM, LINC02932; maybe low, not absent |
| [[SLC26A4]] | B | SLC26A4 activity raises ESRRB's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without SLC26A4 | 0.061 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALOX12-AS1]] | B | ESRRB activity raises ALOX12-AS1's level | lines that do not express ESRRB (5) vs lines expressing it (45) | 2.33× lower at baseline in the lines without ESRRB | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02932, DYNLRB2-AS1, ARHGAP15; maybe low, not absent |
| [[PRRT3]] | B | ESRRB activity raises PRRT3's level | lines that do not express ESRRB (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without ESRRB | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC02932, DYNLRB2-AS1, ARHGAP15; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (14.5, 16.2); signed map (23.1, 2.8). **Vector** length 60.5, 9.14% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.6 | +17.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.6 |
|  | [[NG25 (drug)]] 5 µM |  | -1.8 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | estrogen related receptor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:76,310,712-76,501,837 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERR2, ERRbeta, NR3B2, ERRb; previously ESRL2, DFNB35 |
| Gene groups (HGNC) | Estrogen related receptors |
| Reactome | 1 pathways, smallest: Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O95718](https://www.uniprot.org/uniprotkb/O95718) (Steroid hormone receptor ERR2):

> [Isoform 3]: Transcription factor that binds a canonical ESRRB recognition (ERRE) sequence 5'TCAAGGTCA-3' localized on promoter and enhancer of targets genes regulating their expression or their transcription activity. Plays a role, in a LIF-independent manner, in maintainance of self-renewal and pluripotency of embryonic and trophoblast stem cells through different signaling pathways including FGF signaling pathway and Wnt signaling pathways. Involved in morula development (2-16 cells embryos) …

**Summary**, from NCBI Gene [2103](https://www.ncbi.nlm.nih.gov/gene/2103):

> This gene encodes a protein with similarity to the estrogen receptor. Its function is unknown; however, a similar protein in mouse plays an essential role in placental development. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3473) · Entrez [2103](https://www.ncbi.nlm.nih.gov/gene/2103) · UniProt [O95718](https://www.uniprot.org/uniprotkb/O95718) · Ensembl [ENSG00000119715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119715)

## Data

Gene col 4109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4109); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4109]; `tensor/DDL_lfc|DDL_z.npy` [4109]; `embed/gene_vectors.npy` [4109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4109 or target_col == 4109). Every well: [[ESRRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESRRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ACYP1"
type: "gene"
col: 4089
ensembl_id: "ENSG00000119640"
name: "acylphosphatase 1"
location: "14q24.3"
module: 6
arm: "+"
pooled_cpm: 11.25
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ACYP1

*acylphosphatase 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.91× (z +9.1, q 4e-17, up in 11 of 17 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.34× (z +4.4, q 6e-04, up in 10 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.410× (z -7.0, q 2e-09, down in 25 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.126×; ⚠ cell-cycle shift, explains ~0% of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (HCT15 0.0861×; ⚠ cell-cycle shift, would explain all of this change); [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (KATO III 0.188×); [[Methotrexate (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0815×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (SNU-1 0.0969×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLE2]] (+0.62, fdr 7e-06), [[GINS1]] (+0.60, fdr 1e-05), [[RAD51]] (+0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.91×** | +9.1 | 4e-17 | 11/17 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.69×** | +7.9 | 1e-12 | 16/33 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.58×** | +6.5 | 2e-08 | 23/38 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.49×** | +5.9 | 5e-07 | 20/46 (SHP-77, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.48×** | +5.9 | 5e-07 | 21/47 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.52×** | +5.8 | 7e-07 | 12/26 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.44×** | +5.4 | 4e-06 | 19/47 (NCI-H460, NCI-H2347, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +5.3 | 1e-05 | 14/40 (NCI-H2030, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +4.9 | 8e-05 | 10/47 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.26×** | +4.8 | 9e-05 | 15/46 (C32, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 6e-04 | 10/47 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +4.1 | 0.002 | 11/47 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.31×** | +4.1 | 0.002 | 15/47 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.8 | 0.007 | 9/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.29×** | +3.7 | 0.007 | 9/47 (KATO III, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.5 | 0.014 | 10/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.018 | 11/42 (SW480, BT-474, …) | inconsistent across doses | position effect removed |
| [[Decitabine (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.046 | 9/43 (A549, HCT15, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.049 | 8/47 (HOP62, NCI-H2347, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +2.9 | 0.078 | 6/40 (SHP-77, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.083 | 8/46 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4089.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.126×; ⚠ cell-cycle shift, explains ~0% of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (HCT15 0.0861×; ⚠ cell-cycle shift, would explain all of this change); [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (KATO III 0.188×); [[Methotrexate (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0815×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (SNU-1 0.0969×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.410×** | -7.0 | 2e-09 | 25/43 (A-427, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.541×** | -4.8 | 4e-04 | 20/47 (SK-MEL-2, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.733× | -3.3 | 0.16 | 8/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.670× | -3.2 | 0.20 | 12/31 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.864× | -3.1 | 0.20 | 9/48 (SHP-77, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -8.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-427 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0861× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 8.87 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0815× (z -8.6) |
| [[KATO III (line)]] | alt | 12.0 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.188× (z -8.8) |
| [[LoVo (line)]] | wt | 8.91 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 9.82 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0969× (z -8.5) |
| [[A498 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLE2]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[GINS1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[RAD51]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[WDR76]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CENPM]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[FEN1]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SPC24]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CENPK]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RBL1]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[FANCA]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[MELK]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[DTL]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises ACYP1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without CDC25A | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F1]] | C | E2F1 activity raises ACYP1's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 1.65× lower at baseline in the lines without E2F1 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.0, -46.8); signed map (-39.4, -43.0). **Vector** length 62.3, 9.57% of its response variance represented; |z| ≥ 3 in 773 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +3.7 | +6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +3.6 | +5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.0 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.2 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +3.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -7.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -1.6 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | acylphosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,053,237-75,069,483 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [P07311](https://www.uniprot.org/uniprotkb/P07311) carries no function annotation.

**Summary**, from NCBI Gene [97](https://www.ncbi.nlm.nih.gov/gene/97):

> This gene is a member of the acylphosphatase family. The encoded protein is a small cytosolic enzyme that catalyzes the hydrolysis of the carboxyl-phosphate bond of acylphosphates. Two isoenzymes have been isolated and described based on their tissue localization: erythrocyte (common) type acylphosphatase encoded by this gene, and muscle type acylphosphatase. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:179) · Entrez [97](https://www.ncbi.nlm.nih.gov/gene/97) · UniProt [P07311](https://www.uniprot.org/uniprotkb/P07311) · Ensembl [ENSG00000119640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119640)

## Data

Gene col 4089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4089); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4089]; `tensor/DDL_lfc|DDL_z.npy` [4089]; `embed/gene_vectors.npy` [4089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4089 or target_col == 4089). Every well: [[ACYP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACYP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

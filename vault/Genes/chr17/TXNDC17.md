---
symbol: "TXNDC17"
type: "gene"
col: 4958
ensembl_id: "ENSG00000129235"
name: "thioredoxin domain containing 17"
location: "17p13.1"
module: 3
arm: "+"
pooled_cpm: 40.85
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TXNDC17

*thioredoxin domain containing 17* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.24× (z +6.8, q 4e-09, up in 40 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 5.64×, A-427 4.81×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 7.26×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.521× (z -4.3, q 0.008, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.549× (z -4.2, q 0.008, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A4]] (+0.71, fdr 1e-05), [[C4orf3]] (+0.67, fdr 7e-06), [[ANAPC11]] (+0.65, fdr 3e-05); moves opposite to [[CSDE1]] (-0.60, fdr 2e-05), [[ACCS]] (-0.58, fdr 1e-04), [[CATSPERE]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4958.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 5.64×, A-427 4.81×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 7.26×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **3.24×** | +6.8 | 4e-09 | 40/44 (A498, A549, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **2.71×** | +6.8 | 4e-09 | 34/38 (A498, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.25×** | +5.7 | 2e-06 | 46/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **2.04×** | +5.0 | 7e-05 | 39/46 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.91×** | +4.6 | 6e-04 | 39/48 (HOP62, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +4.4 | 9e-04 | 39/46 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.84×** | +4.3 | 0.001 | 37/48 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.80×** | +3.8 | 0.009 | 30/42 (A498, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.38×** | +3.2 | 0.073 | 37/48 (SK-MEL-2, SW 900, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.521×** | -4.3 | 0.008 | 37/48 (C32, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.549×** | -4.2 | 0.008 | 33/47 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.356×** | -3.7 | 0.038 | 37/47 (HEC-1-A, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.360×** | -3.6 | 0.038 | 35/48 (HOP62, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.386×** | -3.4 | 0.076 | 34/47 (A-427, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.394×** | -3.3 | 0.084 | 35/48 (J82, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.630× | -3.2 | 0.10 | 37/48 (SW 1088, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.569× | -3.2 | 0.10 | 29/48 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.728× | -3.1 | 0.11 | 27/48 (C-33 A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 44.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.64× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[A-427 (line)]] | wt | 60.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[A-172 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A4]] | +0.71 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[C4orf3]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.65 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[TRPT1]] | +0.65 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MRPL17]] | +0.64 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[MEA1]] | +0.63 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CCDC85B]] | +0.62 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[KIAA1958]] | +0.62 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[B3GAT3]] | +0.62 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[ROMO1]] | +0.61 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[NUDT22]] | +0.61 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[GALNT18]] | +0.60 | +0.60 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | -0.60 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ACCS]] | -0.58 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[CATSPERE]] | -0.58 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[POU6F1]] | -0.58 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[HTATIP2]] | -0.58 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[ZFR]] | -0.57 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[PAPOLA]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[AHSA2P]] | -0.56 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[CYBRD1]] | -0.56 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[BAG2]] | -0.55 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[C8orf44-SGK3]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[JAKMIP3]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises TXNDC17's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without HES6 | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises TXNDC17's level | compounds that target MTOR: 3 of 8 lower it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[HDAC6]] | B | HDAC6 activity lowers TXNDC17's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises TXNDC17's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (9.7, -13.0); signed map (-37.1, 18.2). **Vector** length 77.4, 27.7% of its response variance represented; |z| ≥ 3 in 659 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.9 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +3.9 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +3.4 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.0 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.4 | +0.2 |
|  | [[Pimitespib (drug)]] 0.05 µM |  | +1.0 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | -6.1 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | -5.8 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -5.3 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.7 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin domain containing 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:6,640,985-6,644,541 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14353, TRP14; previously TXNL5 |
| Gene groups (HGNC) | Thioredoxin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRA2](https://www.uniprot.org/uniprotkb/Q9BRA2) (Thioredoxin domain-containing protein 17):

> Disulfide reductase. May participate in various redox reactions through the reversible oxidation of its active center dithiol to a disulfide and catalyze dithiol-disulfide exchange reactions. Modulates TNF signaling and NF-kappa-B activation. Has peroxidase activity and may contribute to the elimination of cellular hydrogen peroxide.

**Summary**, from NCBI Gene [84817](https://www.ncbi.nlm.nih.gov/gene/84817):

> Enables protein-disulfide reductase [NAD(P)H] activity. Involved in tumor necrosis factor-mediated signaling pathway. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28218](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28218) · Entrez [84817](https://www.ncbi.nlm.nih.gov/gene/84817) · UniProt [Q9BRA2](https://www.uniprot.org/uniprotkb/Q9BRA2) · Ensembl [ENSG00000129235](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129235)

## Data

Gene col 4958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4958); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4958]; `tensor/DDL_lfc|DDL_z.npy` [4958]; `embed/gene_vectors.npy` [4958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4958 or target_col == 4958). Every well: [[TXNDC17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNDC17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

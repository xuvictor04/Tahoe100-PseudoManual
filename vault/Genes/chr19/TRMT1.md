---
symbol: "TRMT1"
type: "gene"
col: 2523
ensembl_id: "ENSG00000104907"
name: "tRNA methyltransferase 1"
location: "19p13.13"
module: 5
arm: "+"
pooled_cpm: 12.29
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 17
n_dd_up_clean: 29
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TRMT1

*tRNA methyltransferase 1* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.34× (z +13.5, q 1e-38, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.630× (z -10.5, q 7e-23, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX37]] (+0.75, fdr 7e-06), [[TSR1]] (+0.73, fdr 7e-06), [[RBM19]] (+0.73, fdr 7e-06); moves opposite to [[PJA2]] (-0.56, fdr 3e-05), [[VWA5A]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.34×** | +13.5 | 1e-38 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +13.4 | 3e-38 | 39/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.31×** | +13.3 | 5e-38 | 43/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +11.5 | 3e-28 | 33/42 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +11.4 | 5e-28 | 39/46 (NCI-H460, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.98×** | +10.8 | 3e-25 | 39/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.95×** | +10.6 | 2e-24 | 34/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.88×** | +9.4 | 2e-19 | 36/45 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +9.4 | 3e-19 | 30/46 (NCI-H2030, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.78×** | +9.1 | 5e-18 | 27/40 (NCI-H460, HCT15, …) | all doses, flat | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +8.9 | 4e-17 | 37/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.26×** | +8.6 | 3e-16 | 32/44 (RKO, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.65×** | +7.3 | 9e-12 | 17/28 (NCI-H460, LoVo, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.57×** | +7.1 | 5e-11 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +6.9 | 1e-10 | 29/47 (A498, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.74×** | +6.0 | 5e-08 | 16/45 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.21×** | +5.8 | 2e-07 | 16/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.19×** | +5.7 | 3e-07 | 15/45 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.62×** | +5.2 | 5e-06 | 13/47 (PANC-1, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.1 | 9e-06 | 20/45 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-733 (drug)]] 5 µM |  | **2.00×** | +5.0 | 1e-05 | 8/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2523.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.630×** | -10.5 | 7e-23 | 38/48 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.627×** | -7.5 | 2e-11 | 26/46 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -5.6 | 4e-06 | 17/47 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.711×** | -5.5 | 6e-06 | 18/47 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.742×** | -4.8 | 2e-04 | 17/47 (NCI-H2030, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.809×** | -4.8 | 2e-04 | 16/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.736×** | -4.6 | 4e-04 | 13/47 (MIA PaCa-2, NCI-H2030, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.738×** | -4.6 | 4e-04 | 20/46 (HCT15, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.572×** | -4.1 | 0.003 | 15/48 (SW48, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.768×** | -4.0 | 0.003 | 14/46 (LoVo, SK-MEL-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.814×** | -3.8 | 0.007 | 13/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.793×** | -3.7 | 0.009 | 15/47 (NCI-H23, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.821×** | -3.7 | 0.011 | 15/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.794×** | -3.4 | 0.030 | 12/48 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.866× | -3.2 | 0.056 | 9/48 (HCT15, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.4 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 5.37× (z +11.7) | — |
| [[SW480 (line)]] | alt | 14.4 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.25× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.11× (z +10.8) | — |
| [[LoVo (line)]] | wt | 14.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +9.5) | — |
| [[A498 (line)]] | wt | 18.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.412× (z -9.8) |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0831× (z -11.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.120× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 9.94 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +8.6) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 11.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +9.8) | — |
| [[A-172 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX37]] | +0.75 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[TSR1]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[RBM19]] | +0.73 | +0.75 / +0.67 | both halves | 7e-06 | STRING 422 |
| [[PUS1]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | pathway: tRNA modification in the nucleus and cytosol; STRING 715 |
| [[WDR4]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 | pathway: tRNA modification in the nucleus and cytosol; STRING 736 |
| [[MRTO4]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 | STRING 496 |
| [[LRRC41]] | +0.69 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[COX10]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[DUS3L]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 | same gene group; STRING 709 |
| [[DDX31]] | +0.67 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[GTPBP4]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 | STRING 415 |
| [[FBXW9]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | -0.56 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[VWA5A]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TRMT1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.776). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.3, -32.5); signed map (0.2, -47.4). **Vector** length 79.4, 16.3% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.57 to 13); *rRNA processing* (reactome, mean cos +0.54 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.53 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +11.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +13.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +8.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +4.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.9 | -7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:13,104,902-13,117,567 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20244, TRM1 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; 7BS DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXH9](https://www.uniprot.org/uniprotkb/Q9NXH9) (tRNA):

> Dimethylates a single guanine residue at position 26 of most nuclear- and mitochondrial-encoded tRNAs using S-adenosyl-L-methionine as donor of the methyl groups. tRNA guanine(26)-dimethylation is required for redox homeostasis and ensure proper cellular proliferation and oxidative stress survival.

**Summary**, from NCBI Gene [55621](https://www.ncbi.nlm.nih.gov/gene/55621):

> This gene encodes a tRNA-modifying enzyme that acts as a dimethyltransferase, modifying a single guanine residue at position 26 of the tRNA. The encoded enzyme has both mono- and dimethylase activity when exogenously expressed, and uses S-adenosyl methionine as a methyl donor. The C-terminal region of the encoded protein has both a zinc finger motif, and an arginine/proline-rich region. Mutations in this gene have been implicated in autosomal recessive intellectual disorder (ARID). Alternative …

**Accessions** — [HGNC:25980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25980) · Entrez [55621](https://www.ncbi.nlm.nih.gov/gene/55621) · UniProt [Q9NXH9](https://www.uniprot.org/uniprotkb/Q9NXH9) · Ensembl [ENSG00000104907](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104907)

## Data

Gene col 2523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2523); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2523]; `tensor/DDL_lfc|DDL_z.npy` [2523]; `embed/gene_vectors.npy` [2523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2523 or target_col == 2523). Every well: [[TRMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

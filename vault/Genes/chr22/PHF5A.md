---
symbol: "PHF5A"
type: "gene"
col: 1952
ensembl_id: "ENSG00000100410"
name: "PHD finger protein 5A"
location: "22q13.2"
module: 7
arm: "+"
pooled_cpm: 15.24
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PHF5A

*PHD finger protein 5A* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (16 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.90× (z +8.8, q 6e-16, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.729× (z -6.1, q 5e-07, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.217×, Hs 766T 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SNU-1 0.0728×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.230×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[L3MBTL2]] (+0.68, fdr 7e-06), [[TBP]] (+0.68, fdr 7e-06), [[TSSC4]] (+0.67, fdr 7e-06); moves opposite to [[CXADR]] (-0.59, fdr 1e-05), [[LTA4H]] (-0.54, fdr 1e-05), [[CREG1]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.90×** | +8.8 | 6e-16 | 38/47 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +8.7 | 6e-16 | 36/46 (SK-MEL-2, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +8.6 | 2e-15 | 40/46 (SW480, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.78×** | +7.9 | 5e-13 | 37/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.75×** | +7.7 | 2e-12 | 31/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +7.2 | 4e-11 | 30/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.64×** | +6.8 | 1e-09 | 29/43 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.60×** | +6.5 | 7e-09 | 32/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +6.4 | 1e-08 | 25/46 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +6.3 | 2e-08 | 26/47 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.54×** | +5.9 | 2e-07 | 30/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.56×** | +5.8 | 3e-07 | 25/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +5.5 | 2e-06 | 24/47 (KATO III, PANC-1, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +5.4 | 4e-06 | 23/38 (A-427, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +5.3 | 4e-06 | 25/47 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +4.1 | 1e-03 | 16/44 (HS-578T, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.005 | 15/48 (BT-474, COLO 205, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.024 | 6/44 (LOX-IMVI, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.059 | 4/48 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1952.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.217×, Hs 766T 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SNU-1 0.0728×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.230×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.729×** | -6.1 | 5e-07 | 30/48 (Hs 766T, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.736×** | -3.9 | 0.027 | 13/48 (HEC-1-A, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.774×** | -3.5 | 0.060 | 18/47 (KATO III, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.825×** | -3.5 | 0.060 | 13/48 (LOX-IMVI, HEC-1-A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.844× | -3.1 | 0.22 | 7/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -9.3) |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0728× (z -9.4) |
| [[SW480 (line)]] | alt | 17.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[A-172 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L3MBTL2]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[TBP]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TSSC4]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[FLAD1]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[DHRS7B]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[WAPL]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[WDR53]] | +0.64 | +0.58 / +0.59 | both halves | 8e-06 | STRING 450 |
| [[ARL16]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[COMMD5]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SDHAF2]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[MRM3]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[FAM32A]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXADR]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[LTA4H]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[CREG1]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[TWSG1]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A23]] | -0.53 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[AMOT]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[LAMP2]] | -0.52 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[CAT]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CAPZA2]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[CPE]] | -0.50 | -0.31 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.558). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-44.7, 2.0); signed map (-5.3, -23.4). **Vector** length 55.3, 8.65% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.9 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.6 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.3 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.3 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,459,717-41,468,692 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC1346, SF3b14b, INI, bK223H9.2, Rds3, SAP14b, SF3B7 |
| Gene groups (HGNC) | PHD finger proteins; SF3b complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7RTV0](https://www.uniprot.org/uniprotkb/Q7RTV0) (PHD finger-like domain-containing protein 5A):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, PHF5A is part of the SF3B subcomplex, which is …

**Summary**, from NCBI Gene [84844](https://www.ncbi.nlm.nih.gov/gene/84844):

> This gene encodes a subunit of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence-independent manner and may anchor the U2 snRNP to the pre-mRNA. The protein encoded by this gene contains a PHD-finger-like domain that is flanked by highly basic N- and C-termini. This …

**Accessions** — [HGNC:18000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18000) · Entrez [84844](https://www.ncbi.nlm.nih.gov/gene/84844) · UniProt [Q7RTV0](https://www.uniprot.org/uniprotkb/Q7RTV0) · Ensembl [ENSG00000100410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100410)

## Data

Gene col 1952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1952); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1952]; `tensor/DDL_lfc|DDL_z.npy` [1952]; `embed/gene_vectors.npy` [1952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1952 or target_col == 1952). Every well: [[PHF5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

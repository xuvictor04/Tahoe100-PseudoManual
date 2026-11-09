---
symbol: "STRADA"
type: "gene"
col: 15483
ensembl_id: "ENSG00000266173"
name: "STE20 related adaptor alpha"
location: "17q23.3"
module: 38
arm: "+"
pooled_cpm: 8.29
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# STRADA

*STE20 related adaptor alpha* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +14.1, q 2e-42, up in 38 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 2.63×, A498 2.98×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.46×, NCI-H1792 6.10×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.523× (z -8.9, q 3e-16, down in 28 of 46 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.583× (z -7.2, q 7e-11, down in 21 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC9A5]] (+0.55, fdr 3e-05), [[IKZF4]] (+0.54, fdr 1e-05), [[L3MBTL2-AS1]] (+0.53, fdr 5e-05); moves opposite to [[DNAJC19]] (-0.53, fdr 3e-04), [[PAFAH1B3]] (-0.50, fdr 1e-04), [[ESD]] (-0.50, fdr 2e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ITGA2B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15483.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 2.63×, A498 2.98×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.46×, NCI-H1792 6.10×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +14.1 | 2e-42 | 38/43 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.8 | 2e-06 | 6/48 (NCI-H460, C-33 A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.066 | 10/47 (HOP62, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.27× | +3.2 | 0.18 | 10/47 (LS 180, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.523×** | -8.9 | 3e-16 | 28/46 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.573×** | -8.2 | 4e-14 | 27/44 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.538×** | -8.2 | 4e-14 | 21/34 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.605×** | -7.4 | 2e-11 | 20/47 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -7.2 | 6e-11 | 23/39 (NCI-H1573, HCT15, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.583×** | -7.2 | 7e-11 | 21/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.650×** | -6.4 | 2e-08 | 20/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.691×** | -5.5 | 3e-06 | 17/46 (J82, KATO III, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.685×** | -5.2 | 1e-05 | 13/16 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.710×** | -5.1 | 2e-05 | 20/46 (NCI-H2030, LS 180, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **0.740×** | -4.5 | 4e-04 | 14/40 (LOX-IMVI, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.746×** | -4.3 | 7e-04 | 15/45 (CHP-212, SW 900, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.751×** | -3.9 | 0.004 | 9/47 (H4, A498, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.768×** | -3.9 | 0.004 | 15/43 (A498, A549, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.831×** | -3.9 | 0.004 | 14/47 (SNU-423, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -3.4 | 0.023 | 7/46 (A549, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.033 | 15/47 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.865× | -3.0 | 0.075 | 7/47 (HT-29, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.82 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 7.16 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 5.58 | 0 | 2 | — | [[Menadione (drug)]] 5 µM 0.0701× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 9.44 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 7.96 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.178× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 7.38 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 4.64 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0675× (z -10.0) |
| [[LoVo (line)]] | wt | 7.05 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 9.55 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.128× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 7.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0615× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A5]] | +0.55 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[IKZF4]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[L3MBTL2-AS1]] | +0.53 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[TRPV1]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PHYHD1]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[RECQL5]] | +0.52 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[AGAP5]] | +0.52 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[COL20A1]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[CHADL]] | +0.51 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[TMED6]] | +0.51 | +0.54 / +0.26 | both halves | 4e-04 |  |
| [[VWCE]] | +0.51 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[SAXO1]] | +0.51 | +0.35 / +0.39 | both halves | 1e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC19]] | -0.53 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[PAFAH1B3]] | -0.50 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[ESD]] | -0.50 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[MOSPD2]] | -0.49 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[HMGN3]] | -0.49 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[COMMD2]] | -0.49 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[DYNC2H1]] | -0.48 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[CCDC112]] | -0.48 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[MIR181A1HG]] | -0.47 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[PRXL2C]] | -0.46 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[MOCS1]] | -0.46 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[SOAT1]] | -0.46 | -0.32 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2B]] | C | ITGA2B activity raises STRADA's level | lines that do not express ITGA2B (3) vs lines expressing it (47) | 1.59× lower at baseline in the lines without ITGA2B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PHC1, CFL2, HECTD2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.4, -22.9); signed map (9.6, 10.3). **Vector** length 51.9, 6.35% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.1 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.9 | +1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.8 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.0 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -7.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | STE20 related adaptor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,682,336-63,741,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STLK5, NY-BR-96, LYK5, Stlk, STRAD |
| Gene groups (HGNC) | Pseudokinases |
| Reactome | 2 pathways, smallest: Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7RTN6](https://www.uniprot.org/uniprotkb/Q7RTN6) (STE20-related kinase adapter protein alpha):

> Pseudokinase which, in complex with CAB39/MO25 (CAB39/MO25alpha or CAB39L/MO25beta), binds to and activates STK11/LKB1. Adopts a closed conformation typical of active protein kinases and binds STK11/LKB1 as a pseudosubstrate, promoting conformational change of STK11/LKB1 in an active conformation.

**Summary**, from NCBI Gene [92335](https://www.ncbi.nlm.nih.gov/gene/92335):

> The protein encoded by this gene contains a STE20-like kinase domain, but lacks several residues that are critical for catalytic activity, so it is termed a 'pseudokinase'. The protein forms a heterotrimeric complex with serine/threonine kinase 11 (STK11, also known as LKB1) and the scaffolding protein calcium binding protein 39 (CAB39, also known as MO25). The protein activates STK11 leading to the phosphorylation of both proteins and excluding STK11 from the nucleus. The protein is necessary …

**Accessions** — [HGNC:30172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30172) · Entrez [92335](https://www.ncbi.nlm.nih.gov/gene/92335) · UniProt [Q7RTN6](https://www.uniprot.org/uniprotkb/Q7RTN6) · Ensembl [ENSG00000266173](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266173)

## Data

Gene col 15483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15483); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15483]; `tensor/DDL_lfc|DDL_z.npy` [15483]; `embed/gene_vectors.npy` [15483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15483 or target_col == 15483). Every well: [[STRADA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRADA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

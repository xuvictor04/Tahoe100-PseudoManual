---
symbol: "PPP1R11"
type: "gene"
col: 12904
ensembl_id: "ENSG00000204619"
name: "protein phosphatase 1 regulatory inhibitor subunit 11"
location: "6p22.1"
module: 33
arm: "-"
pooled_cpm: 29.55
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# PPP1R11

*protein phosphatase 1 regulatory inhibitor subunit 11* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.88× (z +9.9, q 3e-20, up in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +5.5, q 7e-06, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 3.29×, HOP62 3.20×, NCI-H1573 3.68×, PANC-1 2.33×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 2.89×, CFPAC-1 2.58×, PANC-1 1.95×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 4.37×, BT-474 7.42×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.685× (z -5.9, q 2e-06, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN31]] (+0.66, fdr 1e-05), [[LAMTOR3]] (+0.60, fdr 1e-05), [[HLA-A]] (+0.59, fdr 1e-05); moves opposite to [[HEATR3]] (-0.54, fdr 1e-05), [[CHST10]] (-0.54, fdr 1e-05), [[NAA25]] (-0.53, fdr 1e-05).
> It sits in the **-** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12904.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 3.29×, HOP62 3.20×, NCI-H1573 3.68×, PANC-1 2.33×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 2.89×, CFPAC-1 2.58×, PANC-1 1.95×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 4.37×, BT-474 7.42×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +9.9 | 3e-20 | 38/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +8.2 | 7e-14 | 25/35 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.5 | 7e-06 | 23/47 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +5.3 | 2e-05 | 21/39 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.8 | 0.019 | 0/48 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +3.7 | 0.019 | 20/47 (AsPC-1, CFPAC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.23×** | +3.2 | 0.099 | 16/47 (NCI-H460, BT-474, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.23×** | +3.2 | 0.099 | 17/44 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.2 | 0.100 | 19/44 (HepG2/C3A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.21× | +3.0 | 0.14 | 16/48 (NCI-H460, BT-474, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12904.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.685×** | -5.9 | 2e-06 | 32/48 (COLO 205, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.717×** | -5.2 | 5e-05 | 26/48 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.747×** | -4.6 | 9e-04 | 23/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.755×** | -4.4 | 0.001 | 22/48 (AsPC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.756×** | -4.4 | 0.001 | 27/47 (HOP62, J82, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.070 | 17/48 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.815× | -3.2 | 0.11 | 15/48 (MIA PaCa-2, hTERT-HPNE, …) | top dose only |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.869× | -3.1 | 0.12 | 8/48 (Hs 766T, HT-29, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | 0.688× | -3.1 | 0.13 | 12/48 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.811× | -3.0 | 0.13 | 11/48 (NCI-H23, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | 0.693× | -3.0 | 0.13 | 17/42 (AsPC-1, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.7 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.37× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[BT-474 (line)]] | alt | 18.4 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.42× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 37.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0955× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 41.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.180× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN31]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[LAMTOR3]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[HLA-A]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 | STRING 722 |
| [[TRAPPC6B]] | +0.57 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[FAM161B]] | +0.55 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[THAP9]] | +0.54 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[YIPF6]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ATP6V1D]] | +0.54 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[TOX4]] | +0.54 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[RSPRY1]] | +0.54 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[TRIM39]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 | STRING 520 |
| [[GPR108]] | +0.52 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR3]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[CHST10]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[NAA25]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[HERC2P9]] | -0.53 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[VWA8]] | -0.52 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MANEAL]] | -0.52 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[UCK2]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ACACA]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TMEM177]] | -0.50 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[KPNA3]] | -0.50 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[POLR3B]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[CASP2]] | -0.49 | -0.47 / -0.39 | both halves | 5e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PPP1R11's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **-** arm (projection on the module's main direction -0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (23.8, -36.1); signed map (14.7, -5.1). **Vector** length 80.9, 16.4% of its response variance represented; |z| ≥ 3 in 739 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +1.3 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.2 | +1.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.8 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | -0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory inhibitor subunit 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:30,066,709-30,070,333 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCGV, Tctex5, HCG-V, CFAP255; previously TCTE5 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [O60927](https://www.uniprot.org/uniprotkb/O60927) (E3 ubiquitin-protein ligase PPP1R11):

> Atypical E3 ubiquitin-protein ligase which ubiquitinates TLR2 at 'Lys-754' leading to its degradation by the proteasome. Plays a role in regulating inflammatory cytokine release and gram-positive bacterial clearance by functioning, in part, through the ubiquitination and degradation of TLR2. Inhibitor of protein phosphatase 1.

**Summary**, from NCBI Gene [6992](https://www.ncbi.nlm.nih.gov/gene/6992):

> This gene encodes a specific inhibitor of protein phosphatase-1 (PP1) with a differential sensitivity toward the metal-independent and metal-dependent forms of PP1. The gene is located within the major histocompatibility complex class I region on chromosome 6. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9285) · Entrez [6992](https://www.ncbi.nlm.nih.gov/gene/6992) · UniProt [O60927](https://www.uniprot.org/uniprotkb/O60927) · Ensembl [ENSG00000204619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204619)

## Data

Gene col 12904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12904); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12904]; `tensor/DDL_lfc|DDL_z.npy` [12904]; `embed/gene_vectors.npy` [12904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12904 or target_col == 12904). Every well: [[PPP1R11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

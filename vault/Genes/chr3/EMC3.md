---
symbol: "EMC3"
type: "gene"
col: 4583
ensembl_id: "ENSG00000125037"
name: "ER membrane protein complex subunit 3"
location: "3p25.3"
module: 118
arm: "+"
pooled_cpm: 39.74
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# EMC3

*ER membrane protein complex subunit 3* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.07× (z +13.5, q 1e-38, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.784× (z -4.5, q 0.004, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~20% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.188×, SK-MEL-2 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.0828×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (SK-MEL-2 0.141×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1E1]] (+0.67, fdr 7e-06), [[TMUB2]] (+0.66, fdr 1e-05), [[WDR83]] (+0.63, fdr 1e-05); moves opposite to [[ISOC1]] (-0.62, fdr 1e-05), [[PTP4A3]] (-0.55, fdr 4e-05), [[CEP83]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +13.5 | 1e-38 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +13.3 | 7e-38 | 44/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +12.3 | 1e-32 | 44/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +12.3 | 2e-32 | 46/48 (LoVo, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.75×** | +10.4 | 4e-23 | 44/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.58×** | +8.1 | 5e-14 | 24/37 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +8.1 | 6e-14 | 39/48 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +7.7 | 7e-13 | 35/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +7.7 | 1e-12 | 39/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +7.5 | 5e-12 | 38/49 (PANC-1, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +6.4 | 6e-09 | 31/47 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.38×** | +6.0 | 8e-08 | 29/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.7 | 4e-07 | 27/48 (HOP62, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.30×** | +4.7 | 1e-04 | 24/48 (SW480, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 2e-04 | 21/48 (HS-578T, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.001 | 21/47 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.057 | 9/47 (NCI-H1792, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.089 | 9/47 (A549, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4583.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.188×, SK-MEL-2 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.0828×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (SK-MEL-2 0.141×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.784×** | -4.5 | 0.004 | 24/48 (HCT15, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.853× | -4.1 | 0.009 | 17/48 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.810×** | -3.7 | 0.035 | 17/47 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 43.7 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +12.3) | — |
| [[A549 (line)]] | wt | 38.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 53.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 44.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 30.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 28.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 57.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 36.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0828× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 48.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +13.7) | — |
| [[J82 (line)]] | alt | 46.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.0) | — |
| [[KATO III (line)]] | alt | 44.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[LoVo (line)]] | wt | 22.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.33× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[SHP-77 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW1417 (line)]] | alt | 44.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +11.8) | — |
| [[A-172 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1E1]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[TMUB2]] | +0.66 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[WDR83]] | +0.63 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[IGBP1]] | +0.63 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MED31]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[UXT]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[TM2D1]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SLC25A17]] | +0.59 | +0.57 / +0.63 | both halves | 1e-05 | pathway: Protein localization |
| [[ATP6V1G1]] | +0.59 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[TBP]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ATP6V0E1]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[EMC4]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 999 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISOC1]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[PTP4A3]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[CEP83]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ECT2]] | -0.52 | -0.45 / -0.57 | both halves | 3e-05 | pathway: RHOA GTPase cycle |
| [[LRRC8B]] | -0.52 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[CD83]] | -0.51 | -0.39 / -0.55 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EMC3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.5, -10.1); signed map (-3.4, -5.1). **Vector** length 89.1, 21.0% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +12.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.0 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +7.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.5 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -2.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Lopinavir (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane protein complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,962,682-10,011,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TMEM111 |
| Gene groups (HGNC) | ER membrane protein complex subunits |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0I2](https://www.uniprot.org/uniprotkb/Q9P0I2) (ER membrane protein complex subunit 3):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [55831](https://www.ncbi.nlm.nih.gov/gene/55831):

> Contributes to membrane insertase activity. Involved in protein insertion into ER membrane by stop-transfer membrane-anchor sequence and tail-anchored membrane protein insertion into ER membrane. Located in endoplasmic reticulum membrane. Part of EMC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23999) · Entrez [55831](https://www.ncbi.nlm.nih.gov/gene/55831) · UniProt [Q9P0I2](https://www.uniprot.org/uniprotkb/Q9P0I2) · Ensembl [ENSG00000125037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125037)

## Data

Gene col 4583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4583); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4583]; `tensor/DDL_lfc|DDL_z.npy` [4583]; `embed/gene_vectors.npy` [4583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4583 or target_col == 4583). Every well: [[EMC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

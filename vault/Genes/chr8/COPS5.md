---
symbol: "COPS5"
type: "gene"
col: 4245
ensembl_id: "ENSG00000121022"
name: "COP9 signalosome subunit 5"
location: "8q13.1"
module: 28
arm: "+"
pooled_cpm: 33.14
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# COPS5

*COP9 signalosome subunit 5* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.40× (z +9.9, q 2e-20, up in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.60× (z +9.5, q 5e-19, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.811× (z -6.1, q 3e-07, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.209×; ⚠ cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.234×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA5]] (+0.76, fdr 7e-06), [[PHC3]] (+0.75, fdr 7e-06), [[AIMP1]] (+0.74, fdr 7e-06); moves opposite to [[BRI3BP]] (-0.61, fdr 1e-05), [[GATAD2A]] (-0.61, fdr 1e-05), [[DOCK9]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.40×** | +9.9 | 2e-20 | 32/47 (C32, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +9.5 | 5e-19 | 34/47 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +7.9 | 4e-13 | 33/49 (PANC-1, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +7.7 | 2e-12 | 33/48 (A-427, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.1 | 2e-10 | 24/48 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +6.9 | 5e-10 | 22/48 (NCI-H2347, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.38×** | +6.8 | 1e-09 | 30/46 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.3 | 2e-08 | 23/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +5.6 | 1e-06 | 26/45 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 4e-06 | 25/48 (PANC-1, NCI-H2030, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.8 | 7e-05 | 19/45 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 16/48 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.4 | 5e-04 | 17/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.002 | 19/47 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.002 | 14/48 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.011 | 15/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.031 | 8/47 (SW480, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4245.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.209×; ⚠ cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HCT15 0.234×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.811×** | -6.1 | 3e-07 | 26/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.811×** | -6.1 | 3e-07 | 24/48 (H4, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.767×** | -5.5 | 8e-06 | 26/48 (A498, KATO III, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.785×** | -5.0 | 9e-05 | 27/48 (KATO III, SW1417, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.797×** | -4.7 | 3e-04 | 17/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -3.9 | 0.008 | 0/48 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -3.3 | 0.086 | 14/48 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.895× | -3.2 | 0.096 | 9/48 (CFPAC-1, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 34.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[H4 (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | +0.76 | +0.78 / +0.69 | both halves | 7e-06 | STRING 537 |
| [[PHC3]] | +0.75 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[AIMP1]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 | STRING 463 |
| [[SMARCE1]] | +0.74 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[SLC25A46]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[CHURC1]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[CLK4]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[VPS72]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[MKS1]] | +0.69 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PMPCB]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ASB8]] | +0.68 | +0.79 / +0.63 | both halves | 7e-06 | pathway: Neddylation |
| [[FAM204A]] | +0.68 | +0.72 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRI3BP]] | -0.61 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[DOCK9]] | -0.60 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[SLC27A4]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[MAD1L1]] | -0.59 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[SMG1P2]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[PAQR4]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises COPS5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.2, 4.0); signed map (7.6, -25.3). **Vector** length 80.9, 16.1% of its response variance represented; |z| ≥ 3 in 767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +9.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.7 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.9 | +9.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.8 | +7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +5.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.4 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.8 | +1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | COP9 signalosome subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:67,043,079-67,083,783 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JAB1, SGN5, MOV-34, CSN5 |
| Gene groups (HGNC) | COP9 signalosome; JAMM/MPN+ metallopeptidase family |
| Hallmark sets | MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 17 pathways, smallest: DNA Damage Recognition in GG-NER; GSK3B-mediated proteasomal degradation of PD-L1(CD274); Formation of TC-NER Pre-Incision Complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92905](https://www.uniprot.org/uniprotkb/Q92905) (COP9 signalosome complex subunit 5):

> Metalloprotease and the catalytic component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, IkappaBalpha/NFKBIA, ITPK1 and IRF8/ICSBP, …

**Summary**, from NCBI Gene [10987](https://www.ncbi.nlm.nih.gov/gene/10987):

> The protein encoded by this gene is one of the eight subunits of COP9 signalosome, a highly conserved protein complex that functions as an important regulator in multiple signaling pathways. The structure and function of COP9 signalosome is similar to that of the 19S regulatory particle of 26S proteasome. COP9 signalosome has been shown to interact with SCF-type E3 ubiquitin ligases and act as a positive regulator of E3 ubiquitin ligases. This protein is reported to be involved in the …

**Accessions** — [HGNC:2240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2240) · Entrez [10987](https://www.ncbi.nlm.nih.gov/gene/10987) · UniProt [Q92905](https://www.uniprot.org/uniprotkb/Q92905) · Ensembl [ENSG00000121022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121022)

## Data

Gene col 4245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4245); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4245]; `tensor/DDL_lfc|DDL_z.npy` [4245]; `embed/gene_vectors.npy` [4245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4245 or target_col == 4245). Every well: [[COPS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

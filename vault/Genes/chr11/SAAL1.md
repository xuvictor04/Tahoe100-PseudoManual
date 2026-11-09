---
symbol: "SAAL1"
type: "gene"
col: 9356
ensembl_id: "ENSG00000166788"
name: "serum amyloid A like 1"
location: "11p15.1"
module: 17
arm: "+"
pooled_cpm: 15.62
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# SAAL1

*serum amyloid A like 1* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.75× (z +9.8, q 4e-20, up in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.61× (z +8.3, q 1e-14, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.633× (z -8.1, q 4e-13, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS31P4]] (+0.77, fdr 7e-06), [[TTC5]] (+0.71, fdr 7e-06), [[AGK]] (+0.71, fdr 7e-06); moves opposite to [[C2]] (-0.69, fdr 1e-05), [[CD63]] (-0.66, fdr 7e-06), [[SWT1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9356.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.75×** | +9.8 | 4e-20 | 39/47 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.69×** | +9.2 | 6e-18 | 34/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.69×** | +9.2 | 6e-18 | 37/47 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +8.3 | 1e-14 | 29/46 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +8.0 | 1e-13 | 26/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +7.7 | 1e-12 | 24/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.6 | 3e-12 | 28/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +7.2 | 4e-11 | 19/42 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.27×** | +6.0 | 2e-07 | 21/47 (RKO, LOX-IMVI, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +5.9 | 3e-07 | 17/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.5 | 2e-06 | 19/48 (A549, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +5.3 | 5e-06 | 18/45 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 1e-05 | 14/47 (HOP62, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.1 | 1e-05 | 14/48 (LoVo, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.0 | 2e-05 | 15/47 (LoVo, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 3e-04 | 18/45 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.001 | 18/48 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.002 | 13/48 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.022 | 4/48 (SW48, LoVo, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.028 | 2/47 (C-33 A, A549) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9356.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.633×** | -8.1 | 4e-13 | 27/47 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.772×** | -6.5 | 2e-08 | 26/47 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -6.1 | 2e-07 | 24/46 (AN3 CA, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -5.7 | 2e-06 | 21/48 (HEC-1-A, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -4.1 | 0.004 | 18/47 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.048 | 9/47 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.16 | 9/44 (MIA PaCa-2, HOP62, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.723× | -3.0 | 0.18 | 10/45 (HOP62, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 9.77 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.100× (z -8.6) |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0867× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.220× (z -10.6) |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | +0.77 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[TTC5]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[AGK]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[DLAT]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[COG2]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MDM1]] | +0.69 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[HARS2]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[BBS5]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[EXOSC9]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[QDPR]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[NDUFAF5]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2]] | -0.69 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[CD63]] | -0.66 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[SWT1]] | -0.61 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[AHCYL1]] | -0.61 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[CATSPERG]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[SLC25A53]] | -0.59 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[LINC02646]] | -0.58 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[TOB2]] | -0.58 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[SNX31]] | -0.58 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[STX5]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[PLA2G12B]] | -0.58 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[SMIM4]] | -0.57 | -0.60 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SAAL1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.4% of all compounds | 0.004 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises SAAL1's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TBC1D19]] | C | TBC1D19 activity raises SAAL1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without TBC1D19 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[DAGLA]] | C | DAGLA activity raises SAAL1's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without DAGLA | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.776). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.5, -1.8); signed map (-22.8, -16.2). **Vector** length 86.7, 17.2% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.9 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.5 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.3 | +3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +5.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -5.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | serum amyloid A like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,069,935-18,106,087 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41463, SPACIA1 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96ER3](https://www.uniprot.org/uniprotkb/Q96ER3) (Protein SAAL1):

> Plays a role in promoting the proliferation of synovial fibroblasts in response to pro-inflammatory stimuli.

**Summary**, from NCBI Gene [113174](https://www.ncbi.nlm.nih.gov/gene/113174):

> Acts upstream of or within positive regulation of synoviocyte proliferation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25158) · Entrez [113174](https://www.ncbi.nlm.nih.gov/gene/113174) · UniProt [Q96ER3](https://www.uniprot.org/uniprotkb/Q96ER3) · Ensembl [ENSG00000166788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166788)

## Data

Gene col 9356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9356); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9356]; `tensor/DDL_lfc|DDL_z.npy` [9356]; `embed/gene_vectors.npy` [9356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9356 or target_col == 9356). Every well: [[SAAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

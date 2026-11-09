---
symbol: "TSPAN7"
type: "gene"
col: 7968
ensembl_id: "ENSG00000156298"
name: "tetraspanin 7"
location: "Xp11.4"
module: 45
arm: "+"
pooled_cpm: 4.76
n_lines_expressing: 28
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# TSPAN7

*tetraspanin 7* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 7.63× (z +25.8, q 0e+00, up in 23 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.206×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.173×; ⚠ cell-cycle shift, explains ~13% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0913×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 0.196×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARRB2]] (+0.56, fdr 1e-05), [[ATP8A1]] (+0.55, fdr 4e-05), [[HMGN3]] (+0.54, fdr 9e-05); moves opposite to [[RPAP2]] (-0.48, fdr 3e-04), [[CDK12]] (-0.47, fdr 2e-04), [[ZNF621]] (-0.46, fdr 9e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPP1]] → it (grade C ⚠); 2 go from it, the strongest it → [[TMEM14A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **7.63×** | +25.8 | 0e+00 | 23/24 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **5.56×** | +15.4 | 0e+00 | 23/24 (BT-474, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **5.49×** | +15.3 | 0e+00 | 24/24 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.85×** | +14.2 | 1e-43 | 8/8 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.72×** | +13.9 | 4e-42 | 21/23 (BT-474, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.20×** | +12.9 | 4e-36 | 21/21 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.32×** | +12.7 | 9e-35 | 3/4 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.93×** | +12.3 | 6e-33 | 19/23 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.39×** | +10.2 | 2e-22 | 5/5 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.26×** | +6.8 | 5e-10 | 15/20 (SW480, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +6.6 | 3e-09 | 7/18 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.91×** | +5.8 | 4e-07 | 9/15 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +4.7 | 9e-05 | 4/13 (NCI-H1792, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.7 | 1e-04 | 0/10 | top dose only | cell-cycle shift (explains ~19% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.66×** | +4.6 | 2e-04 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.77×** | +3.6 | 0.009 | 1/23 (C32) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.015 | 3/23 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.020 | 2/20 (C32, KATO III) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.060 | 3/16 (HEC-1-A, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.86×** | +2.9 | 0.078 | 2/15 (NCI-H1573, NCI-H460) | rises with dose | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.57×** | +2.9 | 0.080 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7968.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.206×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.173×; ⚠ cell-cycle shift, explains ~13% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0913×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 0.196×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.689× | -3.4 | 0.40 | 1/24 (RKO) | inconsistent across doses | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | 0.520× | -3.1 | 0.56 | 3/23 (NCI-H1573, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 20.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.21× (z +9.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.196× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 1.61 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.75× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 9.48 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0913× (z -8.7) |
| [[LoVo (line)]] | wt | 1.99 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.10× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 2.74 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.63× (z +9.0) | — |
| [[SW480 (line)]] | alt | 1.29 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.7× (z +11.2) | — |
| [[A-172 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRB2]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ATP8A1]] | +0.55 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[HMGN3]] | +0.54 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[CDON]] | +0.53 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[OTUD7A]] | +0.53 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[APBA1]] | +0.53 | +0.31 / +0.65 | both halves | 2e-04 | pathway: Neuronal System |
| [[NR3C2]] | +0.53 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[ATP6V0E2]] | +0.52 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[SEMA6A]] | +0.52 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[TMEM14A]] | +0.52 | +0.23 / +0.53 | both halves | 5e-04 |  |
| [[RADX]] | +0.51 | +0.26 / +0.55 | both halves | 4e-04 |  |
| [[FKBP7]] | +0.51 | +0.38 / +0.50 | both halves | 6e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP2]] | -0.48 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[CDK12]] | -0.47 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[ZNF621]] | -0.46 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[RECQL5]] | -0.45 | -0.32 / -0.39 | both halves | 1e-04 |  |
| [[UPF3A]] | -0.45 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[ZNF888]] | -0.45 | -0.32 / -0.25 | both halves | 4e-04 |  |
| [[ZNF101]] | -0.44 | -0.28 / -0.26 | both halves | 3e-04 |  |
| [[ZNF689]] | -0.44 | -0.26 / -0.34 | both halves | 4e-04 |  |
| [[RPAP1]] | -0.44 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[NMNAT1]] | -0.44 | -0.21 / -0.34 | both halves | 6e-04 |  |
| [[MEPCE]] | -0.44 | -0.32 / -0.34 | both halves | 1e-04 |  |
| [[ZNF597]] | -0.44 | -0.28 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPP1]] | C | SPP1 activity raises TSPAN7's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without SPP1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM14A]] | B | TSPAN7 activity lowers TMEM14A's level | lines that do not express TSPAN7 (22) vs lines expressing it (28) | 1.25× higher at baseline in the lines without TSPAN7 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC02147, LINC00992, PINCR; maybe low, not absent |
| [[TRIM6]] | B | TSPAN7 activity lowers TRIM6's level | lines that do not express TSPAN7 (22) vs lines expressing it (28) | 1.58× higher at baseline in the lines without TSPAN7 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02147, LINC00992, PINCR; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.2, 5.3); signed map (20.6, 24.0). **Vector** length 43.6, 8.11% of its response variance represented; |z| ≥ 3 in 591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +25.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +12.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +15.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -1.5 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -0.9 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.6 | -0.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.6 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:38,561,542-38,688,920 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DXS1692E, TALLA-1, A15, CD231; previously MXS1, TM4SF2, MRX58 |
| Gene groups (HGNC) | CD molecules; Tetraspanin family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 8 pathways, smallest: Trafficking of GluR2-containing AMPA receptors; Glutamate binding, activation of AMPA receptors and synaptic plasticity; Trafficking of AMPA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P41732](https://www.uniprot.org/uniprotkb/P41732) (Tetraspanin-7):

> May be involved in cell proliferation and cell motility.

**Summary**, from NCBI Gene [7102](https://www.ncbi.nlm.nih.gov/gene/7102):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. This encoded protein is a cell surface glycoprotein and may have a role in the control of neurite outgrowth. It is known to …

**Accessions** — [HGNC:11854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11854) · Entrez [7102](https://www.ncbi.nlm.nih.gov/gene/7102) · UniProt [P41732](https://www.uniprot.org/uniprotkb/P41732) · Ensembl [ENSG00000156298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156298)

## Data

Gene col 7968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7968); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7968]; `tensor/DDL_lfc|DDL_z.npy` [7968]; `embed/gene_vectors.npy` [7968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7968 or target_col == 7968). Every well: [[TSPAN7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

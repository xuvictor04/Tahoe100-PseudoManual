---
symbol: "AGA"
type: "gene"
col: 448
ensembl_id: "ENSG00000038002"
name: "aspartylglucosaminidase"
location: "4q34.3"
module: 29
arm: "+"
pooled_cpm: 11.29
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# AGA

*aspartylglucosaminidase* — 4q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.63× (z +15.6, q 0e+00, up in 33 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +8.2, q 4e-14, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.659× (z -4.7, q 0.001, down in 20 of 44 measured lines) ⚠ cell-cycle shift, explains ~30% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 2 lines (NCI-H460 0.0963×, PANC-1 0.0876×; ⚠ toxic); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 900 0.0543×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (KATO III 0.159×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QPCT]] (+0.64, fdr 1e-05), [[PDIA3P1]] (+0.64, fdr 1e-05), [[ATRAID]] (+0.60, fdr 1e-05); moves opposite to [[RRP7BP-1]] (-0.64, fdr 3e-05), [[RRP7A]] (-0.54, fdr 2e-04), [[FPGS]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTSO]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.63×** | +15.6 | 0e+00 | 33/36 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.67×** | +15.2 | 0e+00 | 17/20 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +10.9 | 3e-25 | 29/33 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +8.2 | 4e-14 | 32/45 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.5 | 7e-09 | 30/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.58×** | +5.6 | 3e-06 | 17/41 (SW 900, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +4.8 | 2e-04 | 17/47 (BT-474, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.7 | 2e-04 | 15/36 (A498, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.001 | 16/44 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.006 | 13/46 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.011 | 18/46 (NCI-H2347, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +3.7 | 0.012 | 14/43 (LS 180, BT-474, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.013 | 15/43 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.22×** | +3.4 | 0.024 | 9/47 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.049 | 11/47 (AsPC-1, BT-474, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.063 | 10/47 (A-172, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 448.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 2 lines (NCI-H460 0.0963×, PANC-1 0.0876×; ⚠ toxic); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 900 0.0543×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (KATO III 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.659×** | -4.7 | 0.001 | 20/44 (KATO III, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.590× | -3.3 | 0.26 | 13/32 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 18.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +9.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.48 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.05× (z +9.6) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0876× (z -9.0) ⚠ toxic |
| [[J82 (line)]] | alt | 17.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.71× (z +10.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 17.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +9.0) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 0.5 µM 0.159× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 20.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.2) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0963× (z -9.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 23.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0543× (z -13.0) |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QPCT]] | +0.64 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PDIA3P1]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ATRAID]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ERAP1]] | +0.59 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[TMX4]] | +0.59 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PRCP]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[ZBED5-AS1]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ITM2B]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CCN3]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[HHLA3]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SH3BGRL]] | +0.57 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[BMI1]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP-1]] | -0.64 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[RRP7A]] | -0.54 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[FPGS]] | -0.54 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TRIM11]] | -0.54 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[RRP7BP]] | -0.53 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[PHRF1]] | -0.52 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[GPSM1]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RBAK-RBAKDN]] | -0.51 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[FBXL18]] | -0.50 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[ATAD3B]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MLXIP]] | -0.50 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[AAMP]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSO]] | B | CTSO activity raises AGA's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without CTSO | 0.089 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (3.4, -25.8); signed map (19.0, -35.1). **Vector** length 67.8, 11.7% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +15.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +1.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.0 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | aspartylglucosaminidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.3 — chr4:177,430,774-177,442,437 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASRG |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P20933](https://www.uniprot.org/uniprotkb/P20933) (N(4)-(beta-N-acetylglucosaminyl)-L-asparaginase):

> Cleaves the GlcNAc-Asn bond which joins oligosaccharides to the peptide of asparagine-linked glycoproteins.

**Summary**, from NCBI Gene [175](https://www.ncbi.nlm.nih.gov/gene/175):

> This gene encodes a member of the N-terminal nucleophile (Ntn) hydrolase family of proteins. The encoded preproprotein is proteolytically processed to generate alpha and beta chains that comprise the mature enzyme. This enzyme is involved in the catabolism of N-linked oligosaccharides of glycoproteins. It cleaves asparagine from N-acetylglucosamines as one of the final steps in the lysosomal breakdown of glycoproteins. Mutations in this gene are associated with the lysosomal storage disease …

**Accessions** — [HGNC:318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:318) · Entrez [175](https://www.ncbi.nlm.nih.gov/gene/175) · UniProt [P20933](https://www.uniprot.org/uniprotkb/P20933) · Ensembl [ENSG00000038002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038002)

## Data

Gene col 448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 448); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 448]; `tensor/DDL_lfc|DDL_z.npy` [448]; `embed/gene_vectors.npy` [448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 448 or target_col == 448). Every well: [[AGA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

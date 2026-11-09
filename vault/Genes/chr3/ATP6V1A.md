---
symbol: "ATP6V1A"
type: "gene"
col: 3566
ensembl_id: "ENSG00000114573"
name: "ATPase H+ transporting V1 subunit A"
location: "3q13.31"
module: 45
arm: "+"
pooled_cpm: 87.61
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 1
n_dd_up_clean: 29
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ATP6V1A

*ATPase H+ transporting V1 subunit A* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.87× (z +31.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.757× (z -5.9, q 2e-06, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.475×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCPEP1]] (+0.70, fdr 7e-06), [[ARL6IP5]] (+0.70, fdr 1e-05), [[SCP2]] (+0.68, fdr 7e-06); moves opposite to [[TLNRD1]] (-0.64, fdr 1e-05), [[SLC25A19]] (-0.61, fdr 1e-05), [[AXIN1]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[QPRT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 17 with an alert ⚠; shown: the 15 strongest. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.87×** | +31.5 | 0e+00 | 47/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.08×** | +23.8 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.03×** | +23.5 | 0e+00 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.65×** | +20.6 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.38×** | +18.3 | 0e+00 | 45/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.24×** | +17.1 | 0e+00 | 47/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.28×** | +16.8 | 0e+00 | 47/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +14.9 | 0e+00 | 42/49 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +14.1 | 2e-43 | 41/48 (HT-29, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.01×** | +13.9 | 3e-42 | 43/48 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +13.8 | 7e-42 | 41/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.91×** | +13.7 | 6e-41 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.07×** | +13.2 | 7e-38 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +11.3 | 8e-28 | 39/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +11.0 | 1e-26 | 44/49 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3566.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.475×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.757×** | -5.9 | 2e-06 | 35/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -4.7 | 7e-04 | 0/50 | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.853× | -3.4 | 0.10 | 18/48 (CHP-212, SW1417, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.854× | -3.4 | 0.10 | 18/47 (NCI-H2030, SW 900, …) | two highest doses | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | 0.742× | -3.3 | 0.10 | 15/46 (MIA PaCa-2, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.860× | -3.1 | 0.16 | 19/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.865× | -3.1 | 0.16 | 15/48 (CHP-212, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 67.5 | 17 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +33.9) | — |
| [[A-172 (line)]] | wt | 60.6 | 16 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +24.3) | — |
| [[KATO III (line)]] | alt | 75.3 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +18.3) | — |
| [[NCI-H460 (line)]] | wt | 58.0 | 14 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +26.0) | — |
| [[A-427 (line)]] | wt | 99.3 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +25.9) | — |
| [[HS-578T (line)]] | alt | 93.3 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +17.1) | — |
| [[HT-29 (line)]] | alt | 110 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +21.6) | — |
| [[HEC-1-A (line)]] | alt | 140 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +22.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.2 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +18.7) | — |
| [[HOP62 (line)]] | alt | 51.8 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +18.5) | — |
| [[LOX-IMVI (line)]] | wt | 62.7 | 10 | 0 | [[Belinostat (drug)]] 5 µM 4.45× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 92.8 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.8) | — |
| [[SW480 (line)]] | alt | 118 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +17.4) | — |
| [[SW1417 (line)]] | alt | 134 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +20.3) | — |
| [[COLO 205 (line)]] | alt | 108 | 8 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.58× (z +12.4) | — |
| [[J82 (line)]] | alt | 102 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +27.0) | — |
| [[LoVo (line)]] | wt | 54.6 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +17.4) | — |
| [[NCI-H1792 (line)]] | alt | 60.8 | 8 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.40× (z +14.8) | — |
| [[RKO (line)]] | wt | 58.7 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +17.0) | — |
| [[SK-MEL-2 (line)]] | alt | 53.0 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.36× (z +13.7) | — |
| [[SW48 (line)]] | wt | 62.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +15.4) | — |
| [[BT-474 (line)]] | alt | 99.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 78.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +14.8) | — |
| [[NCI-H23 (line)]] | alt | 65.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +17.2) | — |
| [[NCI-H2347 (line)]] | alt | 140 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +21.2) | — |
| [[A549 (line)]] | wt | 60.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +20.2) | — |
| [[C32 (line)]] | wt | 75.6 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.64× (z +14.1) | — |
| [[HepG2_C3A (line)]] | wt | 60.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 148 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +24.3) | [[Dinaciclib (drug)]] 5 µM 0.475× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[SNU-423 (line)]] | alt | 80.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 45.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 121 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +18.8) | — |
| [[hTERT-HPNE (line)]] | wt | 80.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 95.4 | 4 | 0 | [[Belinostat (drug)]] 5 µM 2.67× (z +10.1) | — |
| [[A498 (line)]] | wt | 123 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 110 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 105 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.69× (z +9.5) | — |
| [[H4 (line)]] | wt | 62.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +12.3) | — |
| [[AN3 CA (line)]] | alt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 58.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 78.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +14.5) | — |
| [[SHP-77 (line)]] | alt | 103 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 74.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 99.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.6) | — |
| [[CHP-212 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCPEP1]] | +0.70 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[ARL6IP5]] | +0.70 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SCP2]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[DENND4C]] | +0.67 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[ATP6V1H]] | +0.65 | +0.72 / +0.62 | both halves | 7e-06 | same gene group; pathway: Amino acids regulate mTORC1; STRING 999 |
| [[SH3BGRL]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[QPRT]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FBXO7]] | +0.60 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[PSMC6]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[LMBRD1]] | +0.58 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[MINDY1]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | -0.64 | -0.52 / -0.73 | both halves | 1e-05 |  |
| [[SLC25A19]] | -0.61 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[AXIN1]] | -0.60 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[SKI]] | -0.57 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[KCNJ14]] | -0.54 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[ATP6V0A2]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 | same gene group; pathway: Insulin receptor recycling; STRING 986 |
| [[EPOP]] | -0.54 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ENTR1]] | -0.54 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[PUS1]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[AGO2]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 | pathway: MITF-M-dependent gene expression |
| [[ZBED4]] | -0.52 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[MIR17HG]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QPRT]] | B | QPRT activity raises ATP6V1A's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without QPRT | 0.013 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[TOP2A]] | B | TOP2A activity lowers ATP6V1A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-2.1, -19.5); signed map (-25.0, -5.0). **Vector** length 96.3, 33.9% of its response variance represented; |z| ≥ 3 in 1,650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.1 | +14.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.5 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +17.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +18.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.3 | +7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.7 | +3.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -6.2 | -5.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.5 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | +23.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | -4.3 | +4.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.2 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.31 — chr3:113,746,770-113,812,056 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Vma1, VA68; previously VPP2, ATP6A1, ATP6V1A1 |
| Gene groups (HGNC) | V-type ATPase subunits; ATPase F1/V1 alpha/A and beta/B subunit family |
| Reactome | 16 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [P38606](https://www.uniprot.org/uniprotkb/P38606) (V-type proton ATPase catalytic subunit A):

> Catalytic subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment. The V-ATPase complex also acts as an activator for mTORC1 on …

**Summary**, from NCBI Gene [523](https://www.ncbi.nlm.nih.gov/gene/523):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A and three B subunits, two G …

**Accessions** — [HGNC:851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:851) · Entrez [523](https://www.ncbi.nlm.nih.gov/gene/523) · UniProt [P38606](https://www.uniprot.org/uniprotkb/P38606) · Ensembl [ENSG00000114573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114573)

## Data

Gene col 3566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3566); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3566]; `tensor/DDL_lfc|DDL_z.npy` [3566]; `embed/gene_vectors.npy` [3566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3566 or target_col == 3566). Every well: [[ATP6V1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

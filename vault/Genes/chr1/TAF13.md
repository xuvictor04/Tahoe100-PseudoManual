---
symbol: "TAF13"
type: "gene"
col: 12463
ensembl_id: "ENSG00000197780"
name: "TATA-box binding protein associated factor 13"
location: "1p13.3"
module: 52
arm: "+"
pooled_cpm: 46.87
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# TAF13

*TATA-box binding protein associated factor 13* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (17 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.35× (z +10.1, q 5e-21, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.660× (z -5.2, q 1e-04, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.675×; ⚠ position not correctable); [[18β-Glycyrrhetinic acid (drug)]] 5 µM in 1 line (NCI-H661 0.210×); [[Radotinib (drug)]] 0.5 µM in 1 line (COLO 205 0.141×); [[Palmatine (chloride) (drug)]] 5 µM in 1 line (SW 1271 0.123×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA3]] (+0.72, fdr 7e-06), [[YKT6]] (+0.66, fdr 7e-06), [[SRA1]] (+0.66, fdr 7e-06); moves opposite to [[KAT6A]] (-0.60, fdr 1e-05), [[PUM2]] (-0.59, fdr 6e-05), [[SPPL3]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SRA1]] → it (grade C ⚠); 1 goes from it, the strongest it → [[POLR3D]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.35×** | +10.1 | 5e-21 | 46/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.20×** | +9.8 | 2e-20 | 46/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +9.2 | 1e-17 | 38/47 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +8.8 | 2e-16 | 36/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +8.7 | 4e-16 | 44/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.90×** | +6.9 | 4e-10 | 41/49 (RPMI-7951, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +6.9 | 4e-10 | 37/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +6.9 | 5e-10 | 38/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.72×** | +6.7 | 9e-10 | 32/46 (SK-MEL-2, NCI-H23, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.66×** | +6.3 | 1e-08 | 37/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.65×** | +6.2 | 2e-08 | 37/48 (BT-474, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.54×** | +5.4 | 4e-06 | 27/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.55×** | +5.3 | 5e-06 | 24/39 (SK-MEL-2, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.50×** | +5.1 | 1e-05 | 31/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.46×** | +4.7 | 9e-05 | 29/48 (BT-474, RKO, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +4.2 | 7e-04 | 27/48 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +4.0 | 0.002 | 23/48 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.008 | 25/48 (RKO, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.029 | 18/48 (MIA PaCa-2, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.035 | 16/48 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.046 | 19/48 (HT-29, RKO, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.063 | 15/48 (RKO, NCI-H661, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12463.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.675×; ⚠ position not correctable); [[18β-Glycyrrhetinic acid (drug)]] 5 µM in 1 line (NCI-H661 0.210×); [[Radotinib (drug)]] 0.5 µM in 1 line (COLO 205 0.141×); [[Palmatine (chloride) (drug)]] 5 µM in 1 line (SW 1271 0.123×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.660×** | -5.2 | 1e-04 | 36/48 (NCI-H23, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.757× | -3.5 | 0.11 | 25/48 (A-427, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.753× | -3.4 | 0.11 | 19/48 (NCI-H23, RKO, …) | all doses, flat | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.763× | -3.4 | 0.11 | 21/47 (NCI-H23, RKO, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.831× | -3.2 | 0.11 | 20/48 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.696× | -3.2 | 0.11 | 22/48 (Hs 766T, A-427, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.764× | -3.2 | 0.11 | 22/48 (NCI-H1573, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.8 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 33.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 30.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 26.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 34.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.6) | — |
| [[SW480 (line)]] | alt | 26.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.2) | — |
| [[A-172 (line)]] | wt | 30.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.4) | — |
| [[A-427 (line)]] | wt | 34.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.75× (z +8.5) | — |
| [[C32 (line)]] | wt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.141× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.3) | — |
| [[J82 (line)]] | alt | 65.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 38.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 114 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.85× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 65.3 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 5 µM 0.210× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 90.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SNU-423 (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 37.8 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 5 µM 0.123× (z -8.8) |
| [[A498 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 107 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA3]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[YKT6]] | +0.66 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[SRA1]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[TMEM167A]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.64 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[BLZF1]] | +0.64 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[PMM2]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ARF4]] | +0.62 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[DHDDS]] | +0.61 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[RECQL]] | +0.60 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.60 | +0.64 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT6A]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 | pathway: Regulation of TP53 Activity |
| [[PUM2]] | -0.59 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[SPPL3]] | -0.56 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[MED13L]] | -0.55 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ZNF592]] | -0.55 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[LRIG3]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[USP24]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SETD2]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[GMNN]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[KCTD3]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRA1]] | C | SRA1's natural level weakens TAF13's drug response | SRA1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.68, reverse +0.03; direction clear | 0.018 | ⚠ tissue can mimic it; precision caveat |
| [[VWCE]] | C | VWCE's natural level weakens TAF13's drug response | VWCE's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.17; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLR3D]] | C | TAF13's natural level strengthens POLR3D's drug response | TAF13's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.48; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (12.6, -28.1); signed map (-50.6, 5.8). **Vector** length 97.6, 29.3% of its response variance represented; |z| ≥ 3 in 1,158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +2.5 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +6.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.9 | +2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +4.2 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -4.8 | +6.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | -4.8 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.0 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,062,496-109,076,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII18; previously TAF2K |
| Gene groups (HGNC) | General transcription factor IID complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 20 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15543](https://www.uniprot.org/uniprotkb/Q15543) (Transcription initiation factor TFIID subunit 13):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. TAF13, together with TAF11 and TBP, play key roles …

**Summary**, from NCBI Gene [6884](https://www.ncbi.nlm.nih.gov/gene/6884):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11546) · Entrez [6884](https://www.ncbi.nlm.nih.gov/gene/6884) · UniProt [Q15543](https://www.uniprot.org/uniprotkb/Q15543) · Ensembl [ENSG00000197780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197780)

## Data

Gene col 12463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12463); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12463]; `tensor/DDL_lfc|DDL_z.npy` [12463]; `embed/gene_vectors.npy` [12463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12463 or target_col == 12463). Every well: [[TAF13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

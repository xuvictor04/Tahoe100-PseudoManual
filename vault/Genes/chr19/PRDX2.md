---
symbol: "PRDX2"
type: "gene"
col: 9547
ensembl_id: "ENSG00000167815"
name: "peroxiredoxin 2"
location: "19p13.13"
module: 15
arm: "-"
pooled_cpm: 38.92
n_lines_expressing: 41
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PRDX2

*peroxiredoxin 2* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.65× (z +10.5, q 3e-23, up in 36 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (SW480 7.42×, NCI-H1792 11.7×, A498 6.67×, NCI-H460 5.82×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 6.03×, MIA PaCa-2 7.07×, A498 5.57×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.620× (z -4.6, q 0.002, down in 26 of 39 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCHFR]] (+0.55, fdr 4e-05), [[PRELID2]] (+0.52, fdr 5e-05), [[UQCRC1]] (+0.52, fdr 1e-04, ⚠ UQCRC1 in the vector space only through flagged drug-doses), [[HOXA13]] (+0.52, fdr 1e-04); moves opposite to [[ZNF778]] (-0.55, fdr 1e-04), [[HLCS-AS1]] (-0.53, fdr 3e-05), [[PPP1R26-AS1]] (-0.53, fdr 1e-04).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[ZDHHC12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9547.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (SW480 7.42×, NCI-H1792 11.7×, A498 6.67×, NCI-H460 5.82×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 6.03×, MIA PaCa-2 7.07×, A498 5.57×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **4.65×** | +10.5 | 3e-23 | 36/38 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.75×** | +8.7 | 8e-16 | 33/35 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.03×** | +7.0 | 4e-10 | 34/37 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.82×** | +4.1 | 0.005 | 30/38 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.80×** | +4.0 | 0.006 | 26/38 (HEC-1-A, KATO III, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.42×** | +3.4 | 0.055 | 34/39 (BT-474, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.620×** | -4.6 | 0.002 | 26/39 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.298×** | -4.3 | 0.004 | 35/39 (C-33 A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -3.9 | 0.017 | 27/38 (LoVo, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | **0.347×** | -3.8 | 0.022 | 34/39 (Hs 766T, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -3.3 | 0.093 | 25/38 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.641× | -3.0 | 0.22 | 19/38 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 45.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.07× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 24.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 43.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.1) |
| [[SNU-423 (line)]] | alt | 38.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 45.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.42× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 56.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -8.9) |
| [[C32 (line)]] | wt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.37× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 76.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HOP62 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.87× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[J82 (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.03× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1573 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.8× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2030 (line)]] | alt | 54.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 66.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW 900 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW1417 (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 250 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 54.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCHFR]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[PRELID2]] | +0.52 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[UQCRC1]] ⚠ | +0.52 | +0.35 / +0.42 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[HOXA13]] | +0.52 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[SPATA6]] | +0.51 | +0.35 / +0.37 | both halves | 1e-04 |  |
| [[ECH1]] | +0.51 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[DIXDC1]] | +0.51 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[CABIN1]] | +0.51 | +0.21 / +0.47 | both halves | 6e-04 |  |
| [[NRM]] | +0.51 | +0.40 / +0.44 | both halves | 4e-05 |  |
| [[RAD51B]] | +0.51 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[VWA1]] | +0.51 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[SLC25A11]] | +0.51 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[CYB5A]] | +0.51 | +0.35 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF778]] | -0.55 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[HLCS-AS1]] | -0.53 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PPP1R26-AS1]] | -0.53 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[PTPN9]] | -0.52 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[MICALL1]] | -0.51 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[MIATNB]] | -0.50 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[POU6F1]] | -0.50 | -0.25 / -0.41 | both halves | 4e-04 |  |
| [[TLNRD1]] | -0.49 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[TPD52L2]] | -0.49 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ST20-MTHFS]] | -0.48 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[SLC35D2]] | -0.48 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[LINC01772]] | -0.48 | -0.33 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZDHHC12]] | B | PRDX2 activity lowers ZDHHC12's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without PRDX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: RAB20 |
| [[ST20-MTHFS]] | B | PRDX2 activity lowers ST20-MTHFS's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.72× higher at baseline in the lines without PRDX2 | 0.057 | ⚠ within organs, on part of the lines; also absent: RAB20 |
| [[SSBP2]] | B | PRDX2 activity raises SSBP2's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.08× lower at baseline in the lines without PRDX2 | 0.058 | ⚠ within organs, on part of the lines; also absent: RAB20 |
| [[BLOC1S1]] | B | PRDX2 activity lowers BLOC1S1's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without PRDX2 | 0.087 | ⚠ within organs, on part of the lines; also absent: RAB20 |
| [[QRICH2]] | B | PRDX2 activity lowers QRICH2's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.40× higher at baseline in the lines without PRDX2 | 0.088 | ⚠ within organs, on part of the lines; also absent: RAB20 |
| [[TMEM106C]] | B | PRDX2 activity lowers TMEM106C's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without PRDX2 | 0.097 | ⚠ within organs, on part of the lines; also absent: RAB20 |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.432). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.9, 22.5); signed map (-37.6, 19.5). **Vector** length 53.2, 15.8% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.3 | +0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.7 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | peroxiredoxin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,796,820-12,801,800 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRP, NKEFB, TSA, PRXII, PRX2, MGC4104; previously TDPX1 |
| Gene groups (HGNC) | Peroxiredoxins |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, HEME_METABOLISM |
| Reactome | 10 pathways, smallest: Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models; Neurodegenerative Diseases; Defective Intrinsic Pathway for Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P32119](https://www.uniprot.org/uniprotkb/P32119) (Peroxiredoxin-2):

> Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides and as sensor of hydrogen peroxide-mediated signaling events. Might participate in the signaling cascades of growth factors and tumor necrosis factor-alpha by regulating the intracellular concentrations of H(2)O(2).

**Summary**, from NCBI Gene [7001](https://www.ncbi.nlm.nih.gov/gene/7001):

> This gene encodes a member of the peroxiredoxin family of antioxidant enzymes, which reduce hydrogen peroxide and alkyl hydroperoxides. The encoded protein plays an antioxidant protective role in cells, and it may contribute to the antiviral activity of CD8(+) T-cells. The crystal structure of this protein has been resolved to 2.7 angstroms. This protein prevents hemolytic anemia from oxidative stress by stabilizing hemoglobin, thus making this gene a therapeutic target for patients with …

**Accessions** — [HGNC:9353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9353) · Entrez [7001](https://www.ncbi.nlm.nih.gov/gene/7001) · UniProt [P32119](https://www.uniprot.org/uniprotkb/P32119) · Ensembl [ENSG00000167815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167815)

## Data

Gene col 9547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9547); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9547]; `tensor/DDL_lfc|DDL_z.npy` [9547]; `embed/gene_vectors.npy` [9547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9547 or target_col == 9547). Every well: [[PRDX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

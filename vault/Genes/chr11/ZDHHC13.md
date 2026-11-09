---
symbol: "ZDHHC13"
type: "gene"
col: 10785
ensembl_id: "ENSG00000177054"
name: "zDHHC palmitoyltransferase 13"
location: "11p15.1"
module: 6
arm: "+"
pooled_cpm: 42.25
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ZDHHC13

*zDHHC palmitoyltransferase 13* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.60× (z +7.6, q 2e-11, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.649× (z -9.8, q 6e-20, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYTL4]] (+0.60, fdr 1e-05), [[TBC1D1]] (+0.54, fdr 1e-05), [[MTMR8]] (+0.51, fdr 7e-05); moves opposite to [[IQCJ]] (-0.47, fdr 2e-04), [[SLC14A2]] (-0.47, fdr 6e-05), [[SYNM-AS1]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BSPRY]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +7.6 | 2e-11 | 36/47 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +7.4 | 3e-11 | 35/47 (LS 180, HS-578T, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 5e-05 | 34/46 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +4.7 | 5e-04 | 24/47 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.20×** | +4.2 | 0.003 | 20/47 (J82, LoVo, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.27×** | +3.7 | 0.022 | 18/46 (SW480, SK-MEL-2, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.029 | 15/46 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.050 | 11/48 (HT-29, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.22×** | +3.2 | 0.078 | 14/48 (SW1417, SW480, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -9.8 | 6e-20 | 39/47 (Panc 03.27, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.606×** | -8.0 | 3e-13 | 31/47 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.610×** | -7.9 | 4e-13 | 33/46 (COLO 205, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -7.5 | 1e-11 | 25/38 (SHP-77, HT-29, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -6.6 | 6e-09 | 31/43 (HEC-1-A, RKO, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.759×** | -6.3 | 4e-08 | 27/47 (NCI-H1792, Panc 03.27, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.723×** | -5.2 | 2e-05 | 29/44 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.737×** | -4.9 | 7e-05 | 27/46 (Panc 03.27, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.573×** | -4.7 | 2e-04 | 26/48 (Panc 03.27, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.755×** | -4.5 | 4e-04 | 22/47 (NCI-H460, LS 180, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.777×** | -4.0 | 0.003 | 20/47 (HEC-1-A, RKO, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.785×** | -3.7 | 0.009 | 22/46 (SW48, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.798×** | -3.6 | 0.013 | 21/46 (LS 180, Panc 03.27, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.036 | 21/48 (A-427, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 252 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 47.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -18.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 88.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -11.2) |
| [[RKO (line)]] | wt | 54.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -8.8) |
| [[A-427 (line)]] | wt | 47.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +10.1) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 32.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[Hs 766T (line)]] | wt | 34.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -12.6) |
| [[J82 (line)]] | alt | 54.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -11.3) |
| [[KATO III (line)]] | alt | 31.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 37.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -12.0) |
| [[PANC-1 (line)]] | alt | 42.7 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.365× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SW1417 (line)]] | alt | 60.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -11.2) |
| [[A549 (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.9) ⚠ cell-cycle shift, explains ~94% of this change |
| [[COLO 205 (line)]] | alt | 71.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.195× (z -8.9) |
| [[LoVo (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.248× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[NCI-H1792 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -19.1) ⚠ cell-cycle shift, explains ~94% of this change |
| [[NCI-H23 (line)]] | alt | 36.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 60.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -8.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -10.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 32.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.224× (z -11.7) |
| [[SW48 (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.65 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYTL4]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TBC1D1]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MTMR8]] | +0.51 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[DTNBP1]] | +0.50 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[IFNLR1]] | +0.48 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[MRTFB]] | +0.48 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[EXOG]] | +0.46 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[HDHD3]] | +0.46 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[RBL1]] | +0.46 | +0.47 / +0.43 | both halves | 4e-05 |  |
| [[PRSS12]] | +0.45 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[SRI]] | +0.45 | +0.36 / +0.42 | both halves | 9e-05 |  |
| [[ADGRF1]] | +0.45 | +0.49 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCJ]] | -0.47 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[SLC14A2]] | -0.47 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[SYNM-AS1]] | -0.46 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[SRGAP3]] | -0.41 | -0.35 / -0.23 | both halves | 5e-04 |  |
| [[FBXL8]] | -0.41 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[PRRT3-AS1]] | -0.41 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[DLG2]] | -0.40 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[KDM4C]] | -0.40 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[LINC00663]] | -0.40 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[RHCE]] | -0.40 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[PYY]] | -0.40 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[PRKN]] | -0.40 | -0.22 / -0.45 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSPRY]] | B | BSPRY activity raises ZDHHC13's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.53× lower at baseline in the lines without BSPRY | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[SYK]] | B | SYK activity raises ZDHHC13's level | lines that do not express SYK (30) vs lines expressing it (20) | 1.67× lower at baseline in the lines without SYK | 0.063 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[GPR87]] | B | GPR87 activity raises ZDHHC13's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 1.53× lower at baseline in the lines without GPR87 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ZDHHC13's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.289). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-2.4, 37.1); signed map (-2.3, 16.1). **Vector** length 85.0, 18.9% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.6 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +4.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -5.0 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.4 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.3 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -3.1 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -8.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[palbociclib (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:19,117,099-19,176,422 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10852, FLJ10941, HIP14L |
| Gene groups (HGNC) | Zinc fingers DHHC-type; Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUH4](https://www.uniprot.org/uniprotkb/Q8IUH4) (Palmitoyltransferase ZDHHC13):

> Palmitoyltransferase that could catalyze the addition of palmitate onto various protein substrates (By similarity). Palmitoyltransferase for HTT and GAD2. May play a role in Mg(2+) transport.

**Summary**, from NCBI Gene [54503](https://www.ncbi.nlm.nih.gov/gene/54503):

> Predicted to enable magnesium ion transmembrane transporter activity and palmitoyltransferase activity. Involved in positive regulation of canonical NF-kappaB signal transduction. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18413) · Entrez [54503](https://www.ncbi.nlm.nih.gov/gene/54503) · UniProt [Q8IUH4](https://www.uniprot.org/uniprotkb/Q8IUH4) · Ensembl [ENSG00000177054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177054)

## Data

Gene col 10785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10785); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10785]; `tensor/DDL_lfc|DDL_z.npy` [10785]; `embed/gene_vectors.npy` [10785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10785 or target_col == 10785). Every well: [[ZDHHC13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

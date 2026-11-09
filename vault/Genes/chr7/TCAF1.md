---
symbol: "TCAF1"
type: "gene"
col: 12588
ensembl_id: "ENSG00000198420"
name: "TRPM8 channel associated factor 1"
location: "7q35"
module: 17
arm: "+"
pooled_cpm: 53.06
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TCAF1

*TRPM8 channel associated factor 1* — 7q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.49× (z +9.5, q 8e-19, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.261× (z -11.8, q 1e-29, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPF1]] (+0.75, fdr 7e-06), [[TPR]] (+0.66, fdr 1e-05), [[SLC25A4]] (+0.63, fdr 1e-05); moves opposite to [[MFN2]] (-0.62, fdr 3e-05), [[ERVK13-1]] (-0.62, fdr 0.001, ⚠ one half only (not replicated)), [[LY6G5B]] (-0.60, fdr 3e-05), [[PSME3]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +9.5 | 8e-19 | 45/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +8.5 | 4e-15 | 39/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +7.3 | 7e-11 | 36/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +6.8 | 1e-09 | 34/48 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +5.5 | 4e-06 | 32/48 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.4 | 7e-06 | 27/48 (HT-29, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.005 | 25/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | 1.16× | +3.6 | 0.021 | 17/48 (HepG2/C3A, RKO, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.026 | 14/48 (SW1417, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.026 | 21/48 (HT-29, CFPAC-1, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.060 | 14/47 (BT-474, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.13× | +3.0 | 0.12 | 9/48 (SW480, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.261×** | -11.8 | 1e-29 | 47/49 (A-427, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.546×** | -10.2 | 6e-22 | 38/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.388×** | -8.4 | 1e-14 | 39/48 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.627×** | -7.9 | 5e-13 | 36/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.877× | -7.6 | 3e-12 | 6/49 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.650×** | -6.9 | 6e-10 | 36/48 (HCT15, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.666×** | -6.8 | 6e-10 | 33/48 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -6.0 | 1e-07 | 32/48 (C-33 A, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -5.9 | 2e-07 | 29/48 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.731×** | -5.3 | 7e-06 | 31/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.747×** | -4.9 | 5e-05 | 30/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -4.8 | 7e-05 | 25/48 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.812×** | -3.5 | 0.018 | 21/47 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.812×** | -3.5 | 0.018 | 19/48 (H4, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -3.5 | 0.019 | 20/48 (A498, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.831×** | -3.1 | 0.063 | 21/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ivermectin (drug)]] 5 µM |  | 0.834× | -3.1 | 0.073 | 10/48 (A498, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 77.9 | 3 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.68× (z +9.6) | [[TAK-901 (drug)]] 5 µM 0.202× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 72.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.192× (z -9.1) |
| [[SW480 (line)]] | alt | 72.0 | 0 | 4 | — | [[TAK-901 (drug)]] 5 µM 0.187× (z -10.6) |
| [[A498 (line)]] | wt | 86.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -11.6) |
| [[Hs 766T (line)]] | wt | 39.9 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -9.7) |
| [[HT-29 (line)]] | alt | 53.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.12× (z +10.1) | — |
| [[LoVo (line)]] | wt | 63.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 38.0 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.378× (z -9.9) |
| [[RKO (line)]] | wt | 52.2 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0492× (z -12.4) |
| [[AN3 CA (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 47.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +9.1) | — |
| [[C32 (line)]] | wt | 116 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.77× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.2) |
| [[KATO III (line)]] | alt | 59.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.1) | [[TAK-901 (drug)]] 5 µM 0.195× (z -8.9) |
| [[LS 180 (line)]] | wt | 62.1 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.121× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 72.3 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.136× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 26.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.308× (z -9.0) |
| [[SW48 (line)]] | wt | 76.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.320× (z -8.6) |
| [[A-427 (line)]] | wt | 41.6 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0394× (z -14.3) |
| [[BT-474 (line)]] | alt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -8.7) |
| [[C-33 A (line)]] | alt | 52.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.308× (z -8.6) |
| [[H4 (line)]] | wt | 51.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.286× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 52.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.207× (z -8.6) |
| [[HS-578T (line)]] | alt | 49.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.136× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 73.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.105× (z -11.2) |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0573× (z -9.2) |
| [[SW 1088 (line)]] | alt | 84.7 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.109× (z -8.6) |
| [[SW1417 (line)]] | alt | 83.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.91× (z +9.8) | — |
| [[A-172 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 9 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPF1]] | +0.75 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[TPR]] | +0.66 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SLC25A4]] | +0.63 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[ZC3H15]] | +0.62 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[GPATCH11]] | +0.62 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[CCDC112]] | +0.61 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[LEO1]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.59 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[MOSPD2]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SMC3]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.57 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[TIPRL]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFN2]] | -0.62 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[ERVK13-1]] | -0.62 | -0.16 / -0.62 | ⚠ one half (not replicated) | 0.001 |  |
| [[LY6G5B]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[PSME3]] | -0.60 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[LARP4B]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.57 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[TOR1A]] | -0.57 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[SENP3]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SSU72]] | -0.56 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[CERS2]] | -0.56 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[HCFC1]] | -0.56 | -0.32 / -0.63 | both halves | 2e-04 |  |
| [[DDX56]] | -0.56 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[NDUFA10]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TCAF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TCAF1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.1, 1.5); signed map (-19.0, -10.3). **Vector** length 101, 26.1% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | +2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +6.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.4 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.4 | -11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -4.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | TRPM8 channel associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q35 — chr7:143,851,375-143,902,198 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0738, GATD9A; previously FAM115A |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4C2](https://www.uniprot.org/uniprotkb/Q9Y4C2) (TRPM8 channel-associated factor 1):

> Positively regulates the plasma membrane cation channel TRPM8 activity. Involved in the recruitment of TRPM8 to the cell surface. Promotes prostate cancer cell migration inhibition in a TRPM8-dependent manner.

**Summary**, from NCBI Gene [9747](https://www.ncbi.nlm.nih.gov/gene/9747):

> Enables transmembrane transporter binding activity. Involved in negative regulation of cell migration; positive regulation of anion channel activity; and positive regulation of protein targeting to membrane. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22201) · Entrez [9747](https://www.ncbi.nlm.nih.gov/gene/9747) · UniProt [Q9Y4C2](https://www.uniprot.org/uniprotkb/Q9Y4C2) · Ensembl [ENSG00000198420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198420)

## Data

Gene col 12588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12588); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12588]; `tensor/DDL_lfc|DDL_z.npy` [12588]; `embed/gene_vectors.npy` [12588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12588 or target_col == 12588). Every well: [[TCAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

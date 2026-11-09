---
symbol: "CA8"
type: "gene"
col: 10936
ensembl_id: "ENSG00000178538"
name: "carbonic anhydrase 8 (inactive)"
location: "8q12.1"
module: 9
arm: "+"
pooled_cpm: 48.19
n_lines_expressing: 23
n_dd_up: 32
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 9
direction_downstream: 15
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CA8

*carbonic anhydrase 8 (inactive)* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.22× (z +30.0, q 0e+00, up in 18 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.678× (z -5.7, q 5e-06, down in 8 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAP25]] (+0.63, fdr 1e-05), [[CADM1]] (+0.60, fdr 3e-05), [[ELAVL2]] (+0.60, fdr 1e-05); moves opposite to [[CHFR]] (-0.52, fdr 5e-05), [[ZNF343]] (-0.52, fdr 6e-05), [[PSKH1]] (-0.50, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 15 go from it, the strongest it → [[CHST11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.22×** | +30.0 | 0e+00 | 18/21 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +19.9 | 0e+00 | 7/20 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.45×** | +18.6 | 0e+00 | 17/21 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.40×** | +12.9 | 6e-36 | 13/21 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +11.8 | 3e-30 | 19/21 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +10.7 | 1e-24 | 17/21 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.01×** | +10.3 | 6e-23 | 15/21 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.04×** | +10.1 | 3e-22 | 14/21 (HS-578T, CFPAC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.98×** | +10.1 | 5e-22 | 14/21 (BT-474, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.87×** | +9.3 | 1e-18 | 12/19 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +7.4 | 6e-12 | 16/21 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.68×** | +7.1 | 6e-11 | 1/15 (BT-474) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.56×** | +6.6 | 2e-09 | 14/21 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.51×** | +6.0 | 7e-08 | 8/20 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +5.4 | 2e-06 | 8/21 (NCI-H460, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 2e-05 | 10/21 (SW480, NCI-H460, …) | two highest doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 8e-05 | 0/20 | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.011 | 10/22 (NCI-H2030, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.045 | 4/21 (C32, NCI-H460, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.056 | 1/19 (NCI-H460) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.061 | 0/20 | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.678×** | -5.7 | 5e-06 | 8/20 (A549, CFPAC-1, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.722×** | -4.8 | 5e-04 | 9/20 (SW480, NCI-H2030, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.806×** | -4.5 | 0.001 | 12/21 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.750×** | -4.2 | 0.003 | 9/21 (A549, CFPAC-1, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.764×** | -4.0 | 0.008 | 8/20 (A549, H4, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.780×** | -3.7 | 0.023 | 7/20 (SK-MEL-2, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.798×** | -3.3 | 0.066 | 9/21 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.066 | 9/21 (A549, H4, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.787×** | -3.3 | 0.068 | 9/19 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.803×** | -3.1 | 0.097 | 6/20 (H4, SK-MEL-2, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.097 | 4/21 (H4, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 190 | 3 (1 ⚠) | 13 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +20.4) | [[Budesonide (drug)]] 0.5 µM 0.198× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 32.5 | 8 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.42× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 27.6 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +13.2) | — |
| [[J82 (line)]] | alt | 29.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +18.6) | — |
| [[NCI-H2030 (line)]] | alt | 74.1 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.49× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 55.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +20.5) | — |
| [[HS-578T (line)]] | alt | 36.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.5× (z +26.4) | — |
| [[PANC-1 (line)]] | alt | 295 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +19.3) | — |
| [[SK-MEL-2 (line)]] | alt | 370 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.7) |
| [[SW 900 (line)]] | alt | 18.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +20.0) | — |
| [[SW480 (line)]] | alt | 35.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 46.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +10.6) | [[Neratinib (maleate) (drug)]] 0.5 µM 0.169× (z -8.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 13.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.10× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 322 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[C-33 A (line)]] | alt | 21.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.15× (z +8.8) | — |
| [[C32 (line)]] | wt | 85.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 41.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +10.0) | — |
| [[SW 1088 (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.0× (z +9.6) | — |
| [[A-172 (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.56 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.40 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAP25]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CADM1]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ELAVL2]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[KLHL32]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[NCAM1]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[OR4F15]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[CGNL1]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ATP1B1]] | +0.57 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[OLFM1]] | +0.57 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[SLAIN1]] | +0.56 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[TENT5C]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SUSD4]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHFR]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[ZNF343]] | -0.52 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[PSKH1]] | -0.50 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[ZNF767P-1]] | -0.50 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[PEX26]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[POLDIP2]] | -0.49 | -0.22 / -0.49 | both halves | 6e-04 |  |
| [[RNF14]] | -0.48 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[EIF2B4]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ENTPD5]] | -0.48 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ANGEL2]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RALGAPB]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[PGS1]] | -0.47 | -0.46 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers CA8's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[NR4A3]] | B | NR4A3 activity lowers CA8's level | lines that do not express NR4A3 (6) vs lines expressing it (44) | 2.89× higher at baseline in the lines without NR4A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC4A7, SLC16A1; maybe low, not absent |
| [[MID1]] | B | MID1 activity raises CA8's level | lines that do not express MID1 (6) vs lines expressing it (44) | 4.04× lower at baseline in the lines without MID1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: TLE6, ENSG00000132832, ENSG00000243944; maybe low, not absent |
| [[CHST11]] | B | CHST11 activity raises CA8's level | lines that do not express CHST11 (13) vs lines expressing it (37) | 2.95× lower at baseline in the lines without CHST11 | 0.070 | ⚠ within organs, on part of the lines; also absent: SGCE, MAP9, BVES-AS1 |
| [[LMCD1]] | B | LMCD1 activity raises CA8's level | lines that do not express LMCD1 (11) vs lines expressing it (39) | 2.53× lower at baseline in the lines without LMCD1 | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TRPM8]] | B | TRPM8 activity raises CA8's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.13× lower at baseline in the lines without TRPM8 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent |
| [[SNAP25]] | C | SNAP25 activity raises CA8's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 3.44× lower at baseline in the lines without SNAP25 | 0.019 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3; co-absent with the target |
| [[NRXN3]] | C | NRXN3 activity raises CA8's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.98× lower at baseline in the lines without NRXN3 | 0.064 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises CA8's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 3.32× lower at baseline in the lines without LINC02506 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHST11]] | B | CA8 activity raises CHST11's level | lines that do not express CA8 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without CA8 | 0.010 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[CADM1]] | B | CA8 activity raises CADM1's level | lines that do not express CA8 (27) vs lines expressing it (23) | 3.78× lower at baseline in the lines without CA8 | 0.049 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[MYLIP]] | B | CA8 activity raises MYLIP's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.50× lower at baseline in the lines without CA8 | 0.057 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[MIR3142HG]] | B | CA8 activity raises MIR3142HG's level | lines that do not express CA8 (27) vs lines expressing it (23) | 2.12× lower at baseline in the lines without CA8 | 0.064 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[AMOT]] | B | CA8 activity raises AMOT's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without CA8 | 0.072 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[DNM3]] | B | CA8 activity raises DNM3's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.73× lower at baseline in the lines without CA8 | 0.075 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[LMCD1]] | B | CA8 activity raises LMCD1's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without CA8 | 0.078 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[TRPM8]] | B | CA8 activity raises TRPM8's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.42× lower at baseline in the lines without CA8 | 0.089 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[ARHGAP26]] | B | CA8 activity raises ARHGAP26's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.24× lower at baseline in the lines without CA8 | 0.089 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| cells under [[Bortezomib (drug)]] 0.05 µM | B | CA8 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express CA8 (27) vs lines expressing it (21) | the lines without CA8: 1.22× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[HSPA2]] | B | CA8 activity raises HSPA2's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without CA8 | 0.096 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[NCALD]] | B | CA8 activity raises NCALD's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.53× lower at baseline in the lines without CA8 | 0.098 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.0, 33.9); signed map (32.7, 29.5). **Vector** length 61.2, 14.4% of its response variance represented; |z| ≥ 3 in 683 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +18.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +30.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | +3.6 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +3.4 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | -0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +4.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | carbonic anhydrase 8 (inactive) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:60,185,412-60,281,400 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CARP, CA-RP, CA-VIII; previously CALS |
| Gene groups (HGNC) | Carbonic anhydrases |
| Matched by | ensembl_id |

**Function**, from UniProt [P35219](https://www.uniprot.org/uniprotkb/P35219) (Carbonic anhydrase-related protein):

> Does not have a carbonic anhydrase catalytic activity.

**Summary**, from NCBI Gene [767](https://www.ncbi.nlm.nih.gov/gene/767):

> The protein encoded by this gene was initially named CA-related protein because of sequence similarity to other known carbonic anhydrase genes. However, the gene product lacks carbonic anhydrase activity (i.e., the reversible hydration of carbon dioxide). The gene product continues to carry a carbonic anhydrase designation based on clear sequence identity to other members of the carbonic anhydrase gene family. The absence of CA8 gene transcription in the cerebellum of the lurcher mutant in mice …

**Accessions** — [HGNC:1382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1382) · Entrez [767](https://www.ncbi.nlm.nih.gov/gene/767) · UniProt [P35219](https://www.uniprot.org/uniprotkb/P35219) · Ensembl [ENSG00000178538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178538)

## Data

Gene col 10936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10936); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10936]; `tensor/DDL_lfc|DDL_z.npy` [10936]; `embed/gene_vectors.npy` [10936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10936 or target_col == 10936). Every well: [[CA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

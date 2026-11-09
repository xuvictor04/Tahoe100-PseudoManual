---
symbol: "SLC7A6"
type: "gene"
col: 2315
ensembl_id: "ENSG00000103064"
name: "solute carrier family 7 member 6"
location: "16q22.1"
module: 36
arm: "+"
pooled_cpm: 47.24
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SLC7A6

*solute carrier family 7 member 6* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.11× (z +8.1, q 3e-13, up in 0 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.40× (z +7.5, q 1e-11, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.810× (z -6.7, q 9e-09, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEAD4]] (+0.58, fdr 1e-05), [[B4GALT2]] (+0.56, fdr 2e-05), [[SRM]] (+0.55, fdr 1e-05); moves opposite to [[ARRDC3]] (-0.46, fdr 1e-04), [[CNOT4]] (-0.46, fdr 2e-04), [[OAZ2]] (-0.45, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +8.1 | 3e-13 | 0/47 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +8.0 | 5e-13 | 33/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +7.5 | 1e-11 | 27/47 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.8 | 1e-09 | 25/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.6 | 4e-09 | 22/46 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +6.4 | 1e-08 | 25/47 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.9 | 2e-07 | 25/46 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +5.5 | 3e-06 | 23/47 (NCI-H1792, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 3e-06 | 22/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.17× | +4.8 | 9e-05 | 20/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.8 | 9e-05 | 18/47 (PANC-1, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +4.7 | 1e-04 | 16/47 (MIA PaCa-2, SK-MEL-2, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +4.6 | 2e-04 | 18/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **1.24×** | +4.6 | 2e-04 | 13/38 (LoVo, SW1417, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +4.3 | 7e-04 | 21/47 (BT-474, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.1 | 0.002 | 18/47 (MIA PaCa-2, NCI-H460, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +3.5 | 0.012 | 16/46 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.020 | 8/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.030 | 11/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.054 | 13/46 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2315.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.810×** | -6.7 | 9e-09 | 27/47 (SW480, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.767×** | -6.0 | 5e-07 | 25/47 (HS-578T, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.789×** | -5.4 | 2e-05 | 23/47 (KATO III, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.810×** | -4.8 | 2e-04 | 21/47 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.828×** | -4.1 | 0.004 | 16/46 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -4.1 | 0.004 | 19/47 (SW480, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.840× | -4.0 | 0.006 | 14/46 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.9 | 0.006 | 14/47 (SW480, SNU-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.844× | -3.8 | 0.008 | 11/47 (KATO III, SW1417, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.850× | -3.5 | 0.022 | 14/46 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.5 | 0.022 | 17/47 (A498, HOP62, …) | all doses, flat |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.756×** | -3.3 | 0.046 | 12/47 (SW 1271, KATO III, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 60.1 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.82× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.29× (z +8.6) | — |
| [[A498 (line)]] | wt | 94.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -15.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 42.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.1× (z +25.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | — |
| [[NCI-H460 (line)]] | wt | 44.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.2) ⚠ cell-cycle shift, explains ~5% of this change | [[Dinaciclib (drug)]] 5 µM 0.341× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[SW1417 (line)]] | alt | 84.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | — |
| [[SW480 (line)]] | alt | 95.3 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.88× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.520× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.130× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mifepristone (drug)]] 0.05 µM 0.113× (z -9.2) |
| [[HOP62 (line)]] | alt | 53.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.336× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[RKO (line)]] | wt | 82.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[A-427 (line)]] | wt | 45.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | — |
| [[AsPC-1 (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | — |
| [[BT-474 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +9.1) ⚠ cell-cycle shift, explains ~7% of this change | — |
| [[C-33 A (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[KATO III (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 96.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEAD4]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[B4GALT2]] | +0.56 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[SRM]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ATAD3B]] | +0.55 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[VKORC1L1]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PPRC1]] | +0.54 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MYO19]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[EIF3B]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[GTPBP4]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[URB1]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TIMM23B]] | +0.52 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PUS1]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRDC3]] | -0.46 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[CNOT4]] | -0.46 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[OAZ2]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[KIDINS220]] | -0.45 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[VPS26A]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[DMXL1]] | -0.44 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[ZSCAN16]] | -0.44 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[MAT2B]] | -0.44 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[FMR1]] | -0.44 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[CCNG2]] | -0.44 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[USP9X]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[OSGIN2]] | -0.43 | -0.31 / -0.59 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-5.2, -28.8); signed map (-45.6, -18.5). **Vector** length 104, 24.3% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +3.6 | +4.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.3 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +4.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.7 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.8 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 7 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,264,516-68,301,823 (+) |
| Ensembl biotype | protein_coding |
| Also known as | y+LAT-2, KIAA0245, LAT3, LAT-2 |
| Gene groups (HGNC) | Solute carrier family 7 |
| Reactome | 7 pathways, smallest: Basigin interactions; Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92536](https://www.uniprot.org/uniprotkb/Q92536) (Y+L amino acid transporter 2):

> Heterodimer with SLC3A2, that functions as an antiporter which operates as an efflux route by exporting cationic amino acids such as L-arginine from inside the cells in exchange with neutral amino acids like L-leucine, L-glutamine and isoleucine, plus sodium ions and may participate in nitric oxide synthesis. Also exchanges L-arginine with L-lysine in a sodium-independent manner. The transport mechanism is electroneutral and operates with a stoichiometry of 1:1. Contributes to ammonia-induced …

**Summary**, from NCBI Gene [9057](https://www.ncbi.nlm.nih.gov/gene/9057):

> Enables L-lysine:L-arginine antiporter activity and arginine binding activity. Involved in amino acid import across plasma membrane and carboxylic acid transport. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11064) · Entrez [9057](https://www.ncbi.nlm.nih.gov/gene/9057) · UniProt [Q92536](https://www.uniprot.org/uniprotkb/Q92536) · Ensembl [ENSG00000103064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103064)

## Data

Gene col 2315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2315); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2315]; `tensor/DDL_lfc|DDL_z.npy` [2315]; `embed/gene_vectors.npy` [2315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2315 or target_col == 2315). Every well: [[SLC7A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

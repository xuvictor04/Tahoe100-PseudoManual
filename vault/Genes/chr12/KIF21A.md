---
symbol: "KIF21A"
type: "gene"
col: 6259
ensembl_id: "ENSG00000139116"
name: "kinesin family member 21A"
location: "12q12"
module: 76
arm: "+"
pooled_cpm: 117.6
n_lines_expressing: 48
n_dd_up: 34
n_dd_down: 5
n_dd_up_clean: 27
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# KIF21A

*kinesin family member 21A* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.55× (z +30.7, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.587× (z -12.4, q 2e-32, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHBDD3]] (+0.63, fdr 6e-05), [[CLIP1]] (+0.61, fdr 1e-04), [[MARK1]] (+0.59, fdr 4e-05); moves opposite to [[ELK1]] (-0.59, fdr 1e-05), [[MARF1]] (-0.58, fdr 2e-05), [[MTMR14]] (-0.57, fdr 5e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +30.7 | 0e+00 | 45/46 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.08×** | +26.1 | 0e+00 | 46/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.82×** | +22.7 | 0e+00 | 46/46 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.63×** | +22.4 | 0e+00 | 45/46 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +20.9 | 0e+00 | 44/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +15.5 | 0e+00 | 33/47 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +15.2 | 0e+00 | 44/46 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +13.8 | 2e-41 | 42/46 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +12.1 | 5e-32 | 39/46 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.82×** | +9.9 | 3e-21 | 39/47 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +9.7 | 1e-20 | 38/48 (LS 180, C32, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.16×** | +9.3 | 5e-19 | 35/42 (HEC-1-A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +9.2 | 2e-18 | 35/46 (C32, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +9.1 | 5e-18 | 32/46 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +8.9 | 2e-17 | 36/46 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.93×** | +8.0 | 5e-14 | 39/46 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.87×** | +7.6 | 8e-13 | 37/46 (AsPC-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.587×** | -12.4 | 2e-32 | 38/46 (SW480, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.622×** | -11.0 | 9e-26 | 35/46 (SW480, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -9.2 | 6e-18 | 38/47 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.609×** | -6.0 | 2e-07 | 26/46 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.786×** | -5.6 | 3e-06 | 23/46 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.960× | -3.2 | 0.13 | 0/48 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 263 | 12 (2 ⚠) | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 4.21× (z +23.6) | [[Panobinostat (drug)]] 0.5 µM 0.526× (z -10.5) |
| [[A498 (line)]] | wt | 238 | 9 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +32.4) | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -13.4) |
| [[LS 180 (line)]] | wt | 101 | 7 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.426× (z -11.5) |
| [[SW480 (line)]] | alt | 149 | 7 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +17.7) | [[Panobinostat (drug)]] 5 µM 0.264× (z -25.0) |
| [[A549 (line)]] | wt | 158 | 6 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +13.6) | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -13.9) |
| [[C32 (line)]] | wt | 74.5 | 9 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.73× (z +18.4) | — |
| [[HEC-1-A (line)]] | alt | 149 | 6 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 4.72× (z +25.7) | [[Panobinostat (drug)]] 0.5 µM 0.502× (z -11.4) |
| [[KATO III (line)]] | alt | 98.7 | 7 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.368× (z -12.5) |
| [[SW1417 (line)]] | alt | 147 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 136 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +31.4) | — |
| [[CFPAC-1 (line)]] | alt | 83.1 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +24.9) | — |
| [[LoVo (line)]] | wt | 137 | 7 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.559× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 89.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +17.9) | — |
| [[Panc 03.27 (line)]] | alt | 102 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +18.1) | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -12.0) |
| [[PANC-1 (line)]] | alt | 112 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +25.9) | [[TAK-901 (drug)]] 5 µM 0.267× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 88.4 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +16.0) | — |
| [[A-172 (line)]] | wt | 83.7 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.97× (z +14.8) | — |
| [[BT-474 (line)]] | alt | 84.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +14.6) | — |
| [[HOP62 (line)]] | alt | 34.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +17.4) | — |
| [[J82 (line)]] | alt | 80.2 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 102 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.24× (z +19.2) | — |
| [[NCI-H2030 (line)]] | alt | 133 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +20.5) | — |
| [[NCI-H23 (line)]] | alt | 79.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +16.0) | — |
| [[SHP-77 (line)]] | alt | 142 | 3 | 4 | [[Bortezomib (drug)]] 0.05 µM 2.78× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.364× (z -14.2) |
| [[COLO 205 (line)]] | alt | 61.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +23.8) | — |
| [[HS-578T (line)]] | alt | 51.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +15.8) | — |
| [[HT-29 (line)]] | alt | 131 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +18.6) | [[Panobinostat (drug)]] 5 µM 0.476× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 60.5 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.42× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 67.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +17.1) | — |
| [[SW 900 (line)]] | alt | 122 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.8) | — |
| [[A-427 (line)]] | wt | 126 | 4 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.85× (z +14.2) | [[PH-797804 (drug)]] 5 µM 0.216× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 471 | 1 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.03× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.323× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 104 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +20.5) | — |
| [[RKO (line)]] | wt | 121 | 3 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +10.8) | [[TAK-901 (drug)]] 5 µM 0.155× (z -11.4) |
| [[H4 (line)]] | wt | 107 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.3× (z +20.4) | — |
| [[C-33 A (line)]] | alt | 60.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 39.8 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.69× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 72.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 201 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 37.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.10× (z +10.6) | — |
| [[SW48 (line)]] | wt | 124 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 149 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHBDD3]] | +0.63 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[CLIP1]] | +0.61 | +0.68 / +0.34 | both halves | 1e-04 |  |
| [[MARK1]] | +0.59 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[GYG1]] | +0.59 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[TYW3]] | +0.57 | +0.63 / +0.30 | both halves | 2e-04 |  |
| [[MAPK6]] | +0.56 | +0.42 / +0.35 | both halves | 1e-04 |  |
| [[ST7]] | +0.56 | +0.45 / +0.36 | both halves | 1e-04 |  |
| [[BAG2]] | +0.56 | +0.62 / +0.27 | both halves | 3e-04 |  |
| [[ABCC2]] | +0.56 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[PBDC1]] | +0.56 | +0.56 / +0.20 | both halves | 7e-04 |  |
| [[BLTP3B]] | +0.55 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[HACD1]] | +0.55 | +0.52 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK1]] | -0.59 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[MARF1]] | -0.58 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[MTMR14]] | -0.57 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[FHIP1B]] | -0.56 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[PIH1D1]] | -0.55 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[TSFM]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[EPN1]] | -0.54 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[SNRNP200]] | -0.53 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[RAB40B]] | -0.53 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[GVQW3]] | -0.52 | -0.36 / -0.20 | both halves | 7e-04 |  |
| [[PAK4]] | -0.52 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[BRAT1]] | -0.51 | -0.52 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[FN3KRP]] | -0.51 | -0.36 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises KIF21A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AIFM2]] | C | AIFM2 activity raises KIF21A's level | lines that do not express AIFM2 (3) vs lines expressing it (47) | 2.51× lower at baseline in the lines without AIFM2 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: FLVCR2, FUCA2, SLC9A3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction -0.486). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.5, 11.9); signed map (11.7, -6.6). **Vector** length 131, 43.7% of its response variance represented; |z| ≥ 3 in 1,559 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.4 | +26.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.4 | +22.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.3 | +13.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.1 | +22.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +12.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +6.9 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +6.1 |
|  | [[EX229 (drug)]] 5 µM |  | +5.5 | +7.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.1 | +5.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -13.4 | -9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -12.6 | -12.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -11.7 | -11.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -11.6 | -6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -9.5 | -5.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 21A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:39,293,228-39,443,390 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20052; previously FEOM1 |
| Gene groups (HGNC) | WD repeat domain containing; Kinesins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4S6](https://www.uniprot.org/uniprotkb/Q7Z4S6) (Kinesin-like protein KIF21A):

> Processive microtubule plus-end directed motor protein involved in neuronal axon guidance. Is recruited by KANK1 to cortical microtubule stabilizing complexes (CMSCs) at focal adhesions (FAs) rims where it promotes microtubule capture and stability. Controls microtubule polymerization rate at axonal growth cones and suppresses microtubule growth without inducing microtubule disassembly once it reaches the cell cortex.

**Summary**, from NCBI Gene [55605](https://www.ncbi.nlm.nih.gov/gene/55605):

> This gene encodes a member of the KIF4 subfamily of kinesin-like motor proteins. The encoded protein is characterized by an N-terminal motor domain a coiled-coil stalk domain and a C-terminal WD-40 repeat domain. This protein may be involved in microtubule dependent transport. Mutations in this gene are the cause of congenital fibrosis of extraocular muscles-1. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:19349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19349) · Entrez [55605](https://www.ncbi.nlm.nih.gov/gene/55605) · UniProt [Q7Z4S6](https://www.uniprot.org/uniprotkb/Q7Z4S6) · Ensembl [ENSG00000139116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139116)

## Data

Gene col 6259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6259); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6259]; `tensor/DDL_lfc|DDL_z.npy` [6259]; `embed/gene_vectors.npy` [6259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6259 or target_col == 6259). Every well: [[KIF21A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF21A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

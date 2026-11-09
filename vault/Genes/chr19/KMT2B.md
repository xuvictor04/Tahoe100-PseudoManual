---
symbol: "KMT2B"
type: "gene"
col: 15717
ensembl_id: "ENSG00000272333"
name: "lysine methyltransferase 2B"
location: "19q13.12"
module: 11
arm: "+"
pooled_cpm: 38.54
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 21
n_dd_up_clean: 18
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# KMT2B

*lysine methyltransferase 2B* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.41× (z +14.3, q 2e-43, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.601× (z -8.3, q 6e-14, down in 30 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.674× (z -6.5, q 3e-08, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R37]] (+0.73, fdr 7e-06), [[CACTIN]] (+0.70, fdr 7e-06), [[GGA3]] (+0.69, fdr 7e-06); moves opposite to [[ACP1]] (-0.52, fdr 8e-05), [[SCOC]] (-0.50, fdr 3e-05), [[STARD4]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.41×** | +14.3 | 2e-43 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +13.5 | 4e-39 | 45/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.96×** | +10.9 | 2e-25 | 44/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +10.8 | 6e-25 | 39/48 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.88×** | +10.3 | 1e-22 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +7.7 | 2e-12 | 36/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +6.6 | 3e-09 | 40/48 (PANC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.7 | 1e-06 | 28/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +5.2 | 1e-05 | 29/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.7 | 1e-04 | 30/47 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +4.7 | 1e-04 | 27/48 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.005 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.022 | 18/47 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +3.4 | 0.023 | 16/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ataluren (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.023 | 18/48 (PANC-1, RKO, …) | inconsistent across doses | position effect removed |
| [[Asciminib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.023 | 16/48 (A-172, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Resveratrol (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.025 | 15/49 (A-427, C32, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.030 | 13/46 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.601×** | -8.3 | 6e-14 | 30/46 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.674×** | -6.5 | 3e-08 | 35/48 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.675×** | -6.4 | 3e-08 | 34/48 (SW 1271, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -6.2 | 6e-08 | 26/39 (hTERT-HPNE, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -6.0 | 2e-07 | 33/48 (SW 900, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.683×** | -5.8 | 8e-07 | 29/43 (KATO III, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.738×** | -5.0 | 5e-05 | 28/48 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.743×** | -4.9 | 8e-05 | 26/48 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.751×** | -4.7 | 2e-04 | 27/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.753×** | -4.6 | 2e-04 | 24/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -4.6 | 2e-04 | 27/48 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.761×** | -4.5 | 4e-04 | 30/48 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.782×** | -4.0 | 0.002 | 24/48 (NCI-H1573, LS 180, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[venetoclax (drug)]] 0.5 µM |  | **0.729×** | -3.7 | 0.009 | 17/49 (A498, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | **0.811×** | -3.6 | 0.011 | 20/48 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.038 | 16/48 (Panc 03.27, SHP-77, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.828×** | -3.1 | 0.055 | 17/48 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.826×** | -3.0 | 0.065 | 18/47 (SW 900, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.8 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 42.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.4) | — |
| [[H4 (line)]] | wt | 60.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 31.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -15.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 33.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.32× (z +14.1) | — |
| [[SW480 (line)]] | alt | 41.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +13.1) | — |
| [[A549 (line)]] | wt | 70.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 25.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 46.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -12.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 50.4 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +8.5) | [[Lonafarnib (drug)]] 5 µM 0.143× (z -9.5) ⚠ toxic |
| [[LS 180 (line)]] | wt | 32.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.23× (z +12.1) | — |
| [[A-427 (line)]] | wt | 37.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -10.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 34.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 29.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +12.5) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.234× (z -8.9) |
| [[HS-578T (line)]] | alt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -10.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0857× (z -15.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 47.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.10× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +10.1) | — |
| [[A-172 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -9.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -14.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0856× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -11.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -11.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 48.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.00× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -15.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R37]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CACTIN]] | +0.70 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GGA3]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ZCCHC3]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZC3H18]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SEMA4C]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PIAS4]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[GIGYF1]] | +0.63 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[EGLN2]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SETD1A]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes; STRING 821 |
| [[UBE2J2]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[TAOK2]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACP1]] | -0.52 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[SCOC]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[STARD4]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.6, 6.9); signed map (1.3, -9.2). **Vector** length 106, 28.0% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | +6.3 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.8 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +10.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.9 | +14.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.9 | +10.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.9 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.3 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +0.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +3.1 | +1.7 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -6.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.9 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.9 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | lysine methyltransferase 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,717,973-35,738,880 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0304, MLL2, TRX2, HRX2, WBP7, MLL1B, MLL4, CXXC10 |
| Gene groups (HGNC) | PHD finger proteins; Zinc fingers CXXC-type; Histone lysine methyltransferases; SET domain containing |
| Reactome | 12 pathways, smallest: Deactivation of the beta-catenin transactivating complex; Formation of WDR5-containing histone-modifying complexes; PKMTs methylate histone lysines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMN6](https://www.uniprot.org/uniprotkb/Q9UMN6) (Histone-lysine N-methyltransferase 2B):

> Histone methyltransferase that catalyzes methyl group transfer from S-adenosyl-L-methionine to the epsilon-amino group of 'Lys-4' of histone H3 (H3K4) via a non-processive mechanism. Part of chromatin remodeling machinery predominantly forms H3K4me1 and H3K4me2 methylation marks at active chromatin sites where transcription and DNA repair take place. Likely plays a redundant role with KMT2C in enriching H3K4me1 marks on primed and active enhancer elements. Plays a central role in beta-globin …

**Summary**, from NCBI Gene [9757](https://www.ncbi.nlm.nih.gov/gene/9757):

> This gene encodes a protein which contains multiple domains including a CXXC zinc finger, three PHD zinc fingers, two FY-rich domains, and a SET (suppressor of variegation, enhancer of zeste, and trithorax) domain. The SET domain is a conserved C-terminal domain that characterizes proteins of the MLL (mixed-lineage leukemia) family. This gene is ubiquitously expressed in adult tissues. It is also amplified in solid tumor cell lines, and may be involved in human cancer. Two alternatively spliced …

**Accessions** — [HGNC:15840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15840) · Entrez [9757](https://www.ncbi.nlm.nih.gov/gene/9757) · UniProt [Q9UMN6](https://www.uniprot.org/uniprotkb/Q9UMN6) · Ensembl [ENSG00000272333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272333)

## Data

Gene col 15717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15717); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15717]; `tensor/DDL_lfc|DDL_z.npy` [15717]; `embed/gene_vectors.npy` [15717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15717 or target_col == 15717). Every well: [[KMT2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMT2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

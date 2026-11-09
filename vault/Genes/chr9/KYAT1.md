---
symbol: "KYAT1"
type: "gene"
col: 10048
ensembl_id: "ENSG00000171097"
name: "kynurenine aminotransferase 1"
location: "9q34.11"
module: 10
arm: "-"
pooled_cpm: 27.88
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 26
n_dd_up_clean: 21
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KYAT1

*kynurenine aminotransferase 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.26× (z +15.7, q 0e+00, up in 45 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.10× (z +15.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.505× (z -8.7, q 2e-15, down in 21 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.620× (z -6.3, q 5e-08, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP1S1]] (+0.67, fdr 3e-05), [[FAM118A]] (+0.67, fdr 1e-05), [[B3GAT3]] (+0.66, fdr 1e-05); moves opposite to [[ZNF747]] (-0.72, fdr 7e-06), [[EIF4G2]] (-0.68, fdr 7e-06), [[TASOR]] (-0.68, fdr 1e-05).
> It sits in the **-** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +15.7 | 0e+00 | 45/47 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.10×** | +15.1 | 0e+00 | 47/48 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.68×** | +13.1 | 4e-37 | 43/47 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.38×** | +11.5 | 1e-28 | 45/47 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +11.3 | 2e-27 | 42/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.24×** | +10.8 | 5e-25 | 43/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.07×** | +9.7 | 3e-20 | 41/47 (BT-474, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.05×** | +9.5 | 1e-19 | 41/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.78×** | +7.7 | 9e-13 | 37/47 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +6.3 | 2e-08 | 28/48 (RKO, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +5.6 | 1e-06 | 26/47 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +5.4 | 3e-06 | 32/48 (A-172, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +4.4 | 5e-04 | 22/47 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.4 | 5e-04 | 20/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +4.3 | 6e-04 | 20/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 1e-03 | 22/47 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +4.0 | 0.002 | 21/48 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10048.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.505×** | -8.7 | 2e-15 | 21/32 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -6.7 | 7e-09 | 25/40 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.620×** | -6.3 | 5e-08 | 32/47 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.720×** | -6.1 | 1e-07 | 26/47 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.628×** | -5.9 | 4e-07 | 27/47 (COLO 205, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.648×** | -5.5 | 3e-06 | 26/47 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -4.2 | 0.002 | 24/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.726×** | -4.2 | 0.002 | 22/45 (CFPAC-1, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.730×** | -4.2 | 0.002 | 22/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.746×** | -3.9 | 0.006 | 19/48 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.751×** | -3.8 | 0.008 | 19/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.755×** | -3.7 | 0.009 | 15/48 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.755×** | -3.7 | 0.009 | 19/48 (A498, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.765×** | -3.5 | 0.017 | 16/48 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.711×** | -3.5 | 0.019 | 19/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.771×** | -3.4 | 0.021 | 15/48 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.772×** | -3.4 | 0.022 | 15/48 (NCI-H1573, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.798×** | -3.4 | 0.022 | 18/48 (CFPAC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.724×** | -3.3 | 0.029 | 16/47 (LoVo, hTERT-HPNE, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 13.3 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.7× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -8.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 35.3 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.7× (z +14.0) | — |
| [[LoVo (line)]] | wt | 8.69 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.93× (z +10.9) | — |
| [[A-172 (line)]] | wt | 27.1 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.3) |
| [[HOP62 (line)]] | alt | 15.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 80.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -10.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 50.5 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.476× (z -8.6) |
| [[Hs 766T (line)]] | wt | 53.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 45.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0416× (z -14.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -11.5) |
| [[PANC-1 (line)]] | alt | 19.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.46× (z +11.8) | — |
| [[RKO (line)]] | wt | 52.1 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.58× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -11.5) |
| [[SW1417 (line)]] | alt | 30.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.84× (z +12.2) | — |
| [[A-427 (line)]] | wt | 18.7 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.5) |
| [[A549 (line)]] | wt | 25.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 25.2 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.214× (z -10.0) ⚠ transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -8.5) |
| [[COLO 205 (line)]] | alt | 34.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.81× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 19.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.18× (z +10.8) | — |
| [[J82 (line)]] | alt | 37.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.35× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +8.5) | — |
| [[KATO III (line)]] | alt | 34.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.28× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -16.6) |
| [[C-33 A (line)]] | alt | 34.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +8.7) | — |
| [[C32 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -9.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0924× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.143× (z -9.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.40× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -12.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 50.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0565× (z -8.8) |
| [[A498 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1S1]] | +0.67 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[FAM118A]] | +0.67 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[B3GAT3]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MAP3K9]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CKLF]] | +0.64 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LPCAT4]] | +0.64 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[STK32C]] | +0.64 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.64 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[HEBP1]] | +0.63 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[UQCRH]] | +0.63 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[RPS21]] | +0.63 | +0.68 / +0.43 | both halves | 3e-05 | pathway: Metabolism of amino acids and derivatives |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF747]] | -0.72 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.68 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[TASOR]] | -0.68 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.67 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[ZXDA]] | -0.66 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[KRCC1]] | -0.65 | -0.70 / -0.35 | both halves | 1e-04 |  |
| [[GDAP1]] | -0.64 | -0.70 / -0.36 | both halves | 9e-05 |  |
| [[CTBP1-DT]] | -0.64 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[MOCS3]] | -0.63 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.63 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[BCLAF1]] | -0.63 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.63 | -0.67 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.9, 2.3); signed map (-32.2, 14.6). **Vector** length 126, 37.1% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +15.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.8 | +13.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +6.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.2 | +7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.1 | +9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.7 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.8 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.2 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.0 | -6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -4.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | kynurenine aminotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,832,942-128,882,494 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KATI, GTK; previously CCBL1 |
| Gene groups (HGNC) | Transaminases |
| Reactome | 5 pathways, smallest: Phenylalanine metabolism; Phenylalanine and tyrosine metabolism; Tryptophan catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16773](https://www.uniprot.org/uniprotkb/Q16773) (Kynurenine--oxoglutarate transaminase 1):

> Catalyzes the irreversible transamination of the L-tryptophan metabolite L-kynurenine to form kynurenic acid (KA), an intermediate in the tryptophan catabolic pathway which is also a broad spectrum antagonist of the three ionotropic excitatory amino acid receptors among others. Also metabolizes the cysteine conjugates of certain halogenated alkenes and alkanes to form reactive metabolites. Catalyzes the beta-elimination of S-conjugates and Se-conjugates of L-(seleno)cysteine, resulting in the …

**Summary**, from NCBI Gene [883](https://www.ncbi.nlm.nih.gov/gene/883):

> This gene encodes a cytosolic enzyme that is responsible for the metabolism of cysteine conjugates of certain halogenated alkenes and alkanes. This metabolism can form reactive metabolites leading to nephrotoxicity and neurotoxicity. Increased levels of this enzyme have been linked to schizophrenia. Multiple transcript variants that encode different isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1564) · Entrez [883](https://www.ncbi.nlm.nih.gov/gene/883) · UniProt [Q16773](https://www.uniprot.org/uniprotkb/Q16773) · Ensembl [ENSG00000171097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171097)

## Data

Gene col 10048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10048); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10048]; `tensor/DDL_lfc|DDL_z.npy` [10048]; `embed/gene_vectors.npy` [10048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10048 or target_col == 10048). Every well: [[KYAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KYAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

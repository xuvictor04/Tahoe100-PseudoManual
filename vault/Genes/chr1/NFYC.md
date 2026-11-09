---
symbol: "NFYC"
type: "gene"
col: 820
ensembl_id: "ENSG00000066136"
name: "nuclear transcription factor Y subunit gamma"
location: "1p34.2"
module: 51
arm: "+"
pooled_cpm: 47.09
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# NFYC

*nuclear transcription factor Y subunit gamma* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +22.3, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.465× (z -19.6, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAF8]] (+0.83, fdr 1e-05), [[LATS1]] (+0.78, fdr 7e-06), [[UNK]] (+0.76, fdr 1e-05); moves opposite to [[TPST2]] (-0.71, fdr 1e-05), [[HK1]] (-0.67, fdr 1e-05), [[ST6GALNAC4]] (-0.66, fdr 5e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TRIP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +22.3 | 0e+00 | 39/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +16.9 | 0e+00 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +14.5 | 4e-45 | 43/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +12.6 | 3e-34 | 38/47 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +10.9 | 1e-25 | 35/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +10.4 | 3e-23 | 34/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +9.6 | 1e-19 | 37/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +7.5 | 5e-12 | 29/49 (A498, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +6.8 | 5e-10 | 32/48 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +5.2 | 1e-05 | 20/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.5 | 4e-04 | 11/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 18/46 (RKO, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.12× | +4.2 | 0.001 | 14/48 (LS 180, KATO III, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.006 | 17/48 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.016 | 11/48 (A498, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 820.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.465×** | -19.6 | 0e+00 | 41/48 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.479×** | -18.9 | 0e+00 | 44/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.482×** | -18.7 | 0e+00 | 43/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.507×** | -17.4 | 0e+00 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.541×** | -15.7 | 0e+00 | 43/48 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.638×** | -11.5 | 1e-28 | 40/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.683×** | -9.8 | 1e-20 | 32/49 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -9.3 | 1e-18 | 27/42 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.713×** | -8.0 | 8e-14 | 26/43 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.879× | -4.7 | 2e-04 | 18/47 (A549, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.848× | -4.2 | 0.001 | 13/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.739×** | -3.8 | 0.006 | 14/48 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.902× | -3.7 | 0.009 | 9/48 (PANC-1, A-427, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.864× | -3.6 | 0.013 | 16/49 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.848× | -3.0 | 0.10 | 13/48 (C32, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 85.6 | 7 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.429× (z -14.0) |
| [[LoVo (line)]] | wt | 52.9 | 4 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.0726× (z -30.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.340× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 62.5 | 1 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.275× (z -12.5) |
| [[A-427 (line)]] | wt | 76.5 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.432× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 62.6 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +18.8) | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 36.8 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +16.3) | [[Auranofin (drug)]] 5 µM 0.468× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 95.1 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.377× (z -12.4) |
| [[LS 180 (line)]] | wt | 60.7 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 62.9 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.2) | [[Belinostat (drug)]] 0.5 µM 0.343× (z -11.6) |
| [[KATO III (line)]] | alt | 44.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0866× (z -21.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 67.1 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.276× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 73.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -11.7) |
| [[RKO (line)]] | wt | 40.6 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +16.2) | [[Belinostat (drug)]] 0.5 µM 0.316× (z -10.1) |
| [[A549 (line)]] | wt | 45.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 48.4 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.320× (z -15.1) |
| [[A-172 (line)]] | wt | 35.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.9) | [[Auranofin (drug)]] 5 µM 0.402× (z -9.4) |
| [[A498 (line)]] | wt | 38.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.5) | — |
| [[C32 (line)]] | wt | 42.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.318× (z -10.8) |
| [[HCT15 (line)]] | alt | 48.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.226× (z -12.1) |
| [[SW48 (line)]] | wt | 46.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.9) | [[Auranofin (drug)]] 5 µM 0.223× (z -10.6) |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 39.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 52.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -9.7) |
| [[H4 (line)]] | wt | 49.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.173× (z -12.7) |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.397× (z -8.6) |
| [[Hs 766T (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 5 µM 0.0626× (z -12.8) ⚠ toxic |
| [[HS-578T (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 44.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.319× (z -11.3) |
| [[J82 (line)]] | alt | 31.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 32.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF8]] | +0.83 | +0.54 / +0.81 | both halves | 1e-05 |  |
| [[LATS1]] | +0.78 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[UNK]] | +0.76 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[WARS2]] | +0.74 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[EPC1]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[CREBBP]] | +0.71 | +0.63 / +0.54 | both halves | 1e-05 | pathway: Activation of gene expression by SREBF (SREBP); STRING 531 |
| [[ZFX]] | +0.70 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[GTF3C6]] | +0.70 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TXNRD2]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[RNF115]] | +0.68 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LIPT1]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ZNF518A]] | +0.68 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.71 | -0.62 / -0.56 | both halves | 1e-05 | same gene group |
| [[HK1]] | -0.67 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | -0.66 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[ANKRD27]] | -0.66 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[LPCAT1]] | -0.64 | -0.61 / -0.43 | both halves | 3e-05 | same gene group |
| [[TMEM184B]] | -0.62 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ST6GALNAC6]] | -0.62 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[UBA6]] | -0.62 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[MBOAT2]] | -0.61 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[WASF3]] | -0.61 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[SIPA1]] | -0.61 | -0.46 / -0.38 | both halves | 6e-05 | same gene group |
| [[SGTB]] | -0.61 | -0.56 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity lowers NFYC's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.67× higher at baseline in the lines without TRIP6 | 0.002 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[HDAC6]] | B | HDAC6 activity raises NFYC's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.817). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (0.8, 10.2); signed map (21.6, -18.7). **Vector** length 108, 28.3% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +22.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +14.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +7.5 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +10.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +5.6 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +3.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.5 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.3 | -19.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.7 | -15.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.4 | -18.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.3 | -11.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -17.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.6 | -4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear transcription factor Y subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,691,648-40,771,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CBF-C, NF-YC |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Nuclear transcription factor Y |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 15 pathways, smallest: ATF6 (ATF6-alpha) activates chaperone genes; ATF6 (ATF6-alpha) activates chaperones; FOXO-mediated transcription of cell death genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13952](https://www.uniprot.org/uniprotkb/Q13952) (Nuclear transcription factor Y subunit gamma):

> Component of the sequence-specific heterotrimeric transcription factor (NF-Y) which specifically recognizes a 5'-CCAAT-3' box motif found in the promoters of its target genes. NF-Y can function as both an activator and a repressor, depending on its interacting cofactors.

**Summary**, from NCBI Gene [4802](https://www.ncbi.nlm.nih.gov/gene/4802):

> This gene encodes one subunit of a trimeric complex forming a highly conserved transcription factor that binds with high specificity to CCAAT motifs in the promoters of a variety of genes. The encoded protein, subunit C, forms a tight dimer with the B subunit, a prerequisite for subunit A association. The resulting trimer binds to DNA with high specificity and affinity. Subunits B and C each contain a histone-like motif. Multiple transcript variants encoding different isoforms have been found …

**Accessions** — [HGNC:7806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7806) · Entrez [4802](https://www.ncbi.nlm.nih.gov/gene/4802) · UniProt [Q13952](https://www.uniprot.org/uniprotkb/Q13952) · Ensembl [ENSG00000066136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066136)

## Data

Gene col 820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 820); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 820]; `tensor/DDL_lfc|DDL_z.npy` [820]; `embed/gene_vectors.npy` [820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 820 or target_col == 820). Every well: [[NFYC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFYC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

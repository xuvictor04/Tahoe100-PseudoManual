---
symbol: "SNX8"
type: "gene"
col: 2737
ensembl_id: "ENSG00000106266"
name: "sorting nexin 8"
location: "7p22.3"
module: 25
arm: "-"
pooled_cpm: 57.3
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SNX8

*sorting nexin 8* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +18.7, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.644× (z -7.8, q 2e-12, down in 32 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.806× (z -3.8, q 0.014, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SK-MEL-2 0.163×, SW48 0.144×, SW480 0.375×, SW1417 0.294×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.156×, SW480 0.311×, SW1417 0.349×, PANC-1 0.470×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LoVo 0.280×, SNU-1 0.209×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.350×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF185]] (+0.59, fdr 1e-05), [[CLTA]] (+0.57, fdr 1e-05), [[AP5Z1]] (+0.55, fdr 1e-05); moves opposite to [[EXOC5]] (-0.53, fdr 2e-05), [[DLD]] (-0.52, fdr 2e-05), [[G3BP1]] (-0.49, fdr 3e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +18.7 | 0e+00 | 37/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +16.0 | 0e+00 | 44/48 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +11.2 | 6e-27 | 35/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +11.2 | 9e-27 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +8.5 | 2e-15 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +8.2 | 2e-14 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +7.9 | 2e-13 | 34/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +7.5 | 5e-12 | 38/48 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.4 | 1e-11 | 31/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +7.0 | 2e-10 | 31/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +5.6 | 1e-06 | 25/48 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.5 | 1e-06 | 26/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +4.6 | 2e-04 | 23/49 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +3.9 | 0.003 | 18/49 (MIA PaCa-2, SNU-423, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.003 | 21/48 (SNU-423, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.34×** | +3.9 | 0.003 | 18/48 (HCT15, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +3.8 | 0.005 | 15/48 (J82, HOP62, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.018 | 15/48 (SW 900, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2737.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SK-MEL-2 0.163×, SW48 0.144×, SW480 0.375×, SW1417 0.294×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.156×, SW480 0.311×, SW1417 0.349×, PANC-1 0.470×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LoVo 0.280×, SNU-1 0.209×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.350×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -7.8 | 2e-12 | 32/41 (SK-MEL-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.658×** | -7.8 | 2e-12 | 35/49 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.715×** | -5.7 | 2e-06 | 32/45 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -5.2 | 3e-05 | 27/47 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.806×** | -3.8 | 0.014 | 18/47 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.832×** | -3.4 | 0.060 | 17/48 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.837× | -3.3 | 0.075 | 18/48 (LoVo, C32, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.833×** | -3.3 | 0.078 | 15/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.0 | 12 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +29.6) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -9.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 64.3 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 69.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.41× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -16.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 53.7 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +17.3) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -15.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 50.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +19.1) | — |
| [[LoVo (line)]] | wt | 68.2 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.212× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -9.4) |
| [[BT-474 (line)]] | alt | 45.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 35.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.2) | — |
| [[KATO III (line)]] | alt | 66.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 55.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -17.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 68.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +20.0) | — |
| [[AsPC-1 (line)]] | alt | 117 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -8.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 35.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.18× (z +15.1) | — |
| [[H4 (line)]] | wt | 75.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 45.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +11.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.424× (z -9.0) ⚠ toxic |
| [[HS-578T (line)]] | alt | 43.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.23× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 68.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.6) | — |
| [[J82 (line)]] | alt | 76.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 78.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.64× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 91.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 97.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.7) | — |
| [[SW1417 (line)]] | alt | 62.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 58.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.54× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 65.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.7) | — |
| [[A549 (line)]] | wt | 46.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +14.4) | — |
| [[COLO 205 (line)]] | alt | 57.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.91× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 50.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.203× (z -9.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 49.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 53.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +17.3) | — |
| [[NCI-H2347 (line)]] | alt | 43.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.9) | — |
| [[SNU-1 (line)]] | wt | 51.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.209× (z -10.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 68.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 52.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.4) | — |
| [[A498 (line)]] | wt | 84.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF185]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CLTA]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[AP5Z1]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MIRLET7A1HG]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[C19orf25]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ZNF816-ZNF321P]] | +0.54 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[NAGLU]] | +0.54 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[BRI3]] | +0.52 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[USP36]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ISG20L2]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PLEKHM1]] | +0.51 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[POLR1C]] | +0.50 | +0.37 / +0.54 | both halves | 9e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC5]] | -0.53 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[DLD]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[G3BP1]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SCCPDH]] | -0.47 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SSX2IP]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[MRPL19]] | -0.46 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TOP2B]] | -0.46 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[NSFL1C]] | -0.46 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RAD23B]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TWF1]] | -0.45 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[UBQLN1]] | -0.45 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[COX11]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-50.8, 12.2); signed map (6.8, 15.5). **Vector** length 116, 33.1% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.6 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +16.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.2 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | +2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.6 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +3.5 | +3.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.2 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,251,770-2,354,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Mvp1 |
| Gene groups (HGNC) | Sorting nexins; PX-BAR domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5X2](https://www.uniprot.org/uniprotkb/Q9Y5X2) (Sorting nexin-8):

> May be involved in several stages of intracellular trafficking. May play a role in intracellular protein transport from early endosomes to the trans-Golgi network.

**Summary**, from NCBI Gene [29886](https://www.ncbi.nlm.nih.gov/gene/29886):

> Enables phosphatidylinositol binding activity. Involved in early endosome to Golgi transport and intracellular protein transport. Located in early endosome membrane and retromer complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14972) · Entrez [29886](https://www.ncbi.nlm.nih.gov/gene/29886) · UniProt [Q9Y5X2](https://www.uniprot.org/uniprotkb/Q9Y5X2) · Ensembl [ENSG00000106266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106266)

## Data

Gene col 2737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2737); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2737]; `tensor/DDL_lfc|DDL_z.npy` [2737]; `embed/gene_vectors.npy` [2737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2737 or target_col == 2737). Every well: [[SNX8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

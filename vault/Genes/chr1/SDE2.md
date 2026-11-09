---
symbol: "SDE2"
type: "gene"
col: 6795
ensembl_id: "ENSG00000143751"
name: "spliceosome associated SDE2"
location: "1q42.12"
module: 41
arm: "+"
pooled_cpm: 45.82
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SDE2

*spliceosome associated SDE2* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.56× (z +19.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.508× (z -9.8, q 9e-20, down in 34 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Gallic acid (hydrate) (drug)]] 0.05 µM: 0.762× (z -4.1, q 0.006, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (Panc 03.27 0.0994×, SW 900 0.137×, HCT15 0.0807×, NCI-H1792 0.142×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.333×, CFPAC-1 0.291×, CHP-212 0.133×, NCI-H1573 0.330×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (AN3 CA 0.0618×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VIRMA]] (+0.70, fdr 7e-06), [[MPHOSPH10]] (+0.70, fdr 7e-06), [[MED8]] (+0.69, fdr 7e-06); moves opposite to [[PSPC1]] (-0.56, fdr 3e-05), [[VOPP1]] (-0.54, fdr 2e-05), [[SMAD2]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +19.8 | 0e+00 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **5.84×** | +13.7 | 2e-40 | 48/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +13.4 | 2e-38 | 46/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.17×** | +11.5 | 2e-28 | 45/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +11.3 | 1e-27 | 45/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +10.6 | 3e-24 | 44/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +10.4 | 3e-23 | 43/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +10.3 | 4e-23 | 43/48 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.00×** | +10.3 | 6e-23 | 44/48 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.59×** | +9.9 | 2e-21 | 41/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +9.9 | 2e-21 | 44/48 (SW480, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +9.1 | 4e-18 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.78×** | +8.6 | 4e-16 | 40/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +8.1 | 2e-14 | 41/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +7.3 | 1e-11 | 9/49 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +5.8 | 3e-07 | 34/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6795.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (Panc 03.27 0.0994×, SW 900 0.137×, HCT15 0.0807×, NCI-H1792 0.142×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.333×, CFPAC-1 0.291×, CHP-212 0.133×, NCI-H1573 0.330×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (AN3 CA 0.0618×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.508×** | -9.8 | 9e-20 | 34/39 (Panc 03.27, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.667×** | -6.1 | 3e-07 | 32/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.756×** | -4.2 | 0.005 | 26/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.762×** | -4.1 | 0.006 | 26/48 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.849× | -3.4 | 0.069 | 15/48 (A549, SW 900, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.805×** | -3.3 | 0.096 | 21/48 (H4, SW 1088, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.816× | -3.1 | 0.16 | 14/48 (J82, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 36.7 | 13 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.34× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 55.3 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 34.7 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +17.7) | — |
| [[LOX-IMVI (line)]] | wt | 31.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +14.9) | — |
| [[LS 180 (line)]] | wt | 41.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 48.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +16.1) | — |
| [[NCI-H1792 (line)]] | alt | 33.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 64.0 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 41.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 33.3 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 74.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -14.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 30.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.1) | — |
| [[KATO III (line)]] | alt | 34.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.3) | — |
| [[LoVo (line)]] | wt | 39.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 39.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -17.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 48.8 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.44× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +13.5) | — |
| [[A498 (line)]] | wt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 35.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0618× (z -13.4) |
| [[C-33 A (line)]] | alt | 36.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.0) | — |
| [[C32 (line)]] | wt | 32.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 38.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 36.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 33.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 37.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 94.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -17.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 40.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.91× (z +9.5) | — |
| [[A-172 (line)]] | wt | 52.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 40.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +11.3) | — |
| [[CHP-212 (line)]] | wt | 78.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 59.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0807× (z -17.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 55.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.8) | — |
| [[J82 (line)]] | alt | 43.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 43.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 43.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.0) | — |
| [[H4 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIRMA]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.70 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[MED8]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ZNF622]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[TFIP11]] | +0.67 | +0.58 / +0.61 | both halves | 8e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 620 |
| [[BRF2]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ERCC5]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RNF113A]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MRPL2]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZNF526]] | +0.64 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSPC1]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[VOPP1]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SMAD2]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[REEP3]] | -0.52 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[PKP4]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-39.6, -7.4); signed map (-12.5, -9.4). **Vector** length 75.4, 20.5% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +8.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +4.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.2 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.9 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | +9.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -4.4 | +6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | -4.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -3.4 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | spliceosome associated SDE2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:225,982,702-225,999,343 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35382; previously C1orf55 |
| Gene groups (HGNC) | Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IQ49](https://www.uniprot.org/uniprotkb/Q6IQ49) (Splicing regulator SDE2):

> Inhibits translesion DNA synthesis by preventing monoubiquitination of PCNA, this is necessary to counteract damage due to ultraviolet light-induced replication stress. SDE2 is cleaved following PCNA binding, and its complete degradation is necessary to allow S-phase progression following DNA damage.; Plays a role in pre-mRNA splicing by facilitating excision of relatively short introns featuring weak 3'-splice sites (ss) and high GC content. May recruit CACTIN to the spliceosome (By …

**Summary**, from NCBI Gene [163859](https://www.ncbi.nlm.nih.gov/gene/163859):

> Enables damaged DNA binding activity and snoRNA binding activity. Involved in several processes, including cellular response to UV; gene expression; and mitotic G1 DNA damage checkpoint signaling. Located in cytosol; nuclear speck; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26643) · Entrez [163859](https://www.ncbi.nlm.nih.gov/gene/163859) · UniProt [Q6IQ49](https://www.uniprot.org/uniprotkb/Q6IQ49) · Ensembl [ENSG00000143751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143751)

## Data

Gene col 6795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6795); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6795]; `tensor/DDL_lfc|DDL_z.npy` [6795]; `embed/gene_vectors.npy` [6795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6795 or target_col == 6795). Every well: [[SDE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "CGAS"
type: "gene"
col: 8947
ensembl_id: "ENSG00000164430"
name: "cyclic GMP-AMP synthase"
location: "6q13"
module: 2
arm: "-"
pooled_cpm: 35.23
n_lines_expressing: 33
n_dd_up: 36
n_dd_down: 12
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 11
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CGAS

*cyclic GMP-AMP synthase* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.79× (z +23.1, q 0e+00, up in 29 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.515× (z -10.1, q 2e-21, down in 19 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.568× (z -9.0, q 7e-17, down in 23 of 31 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF3]] (+0.56, fdr 3e-05), [[ZNF101]] (+0.56, fdr 1e-04), [[GINS3]] (+0.54, fdr 1e-04); moves opposite to [[EPN1]] (-0.57, fdr 3e-05), [[CYB5R3]] (-0.57, fdr 4e-05), [[NOMO1]] (-0.53, fdr 1e-04).
> It sits in the **-** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 11 go from it, the strongest it → [[NMI]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.79×** | +23.1 | 0e+00 | 29/31 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.68×** | +15.7 | 0e+00 | 30/30 (RKO, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +14.8 | 0e+00 | 28/31 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.40×** | +13.3 | 2e-38 | 28/31 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +11.5 | 2e-28 | 25/31 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +10.5 | 6e-24 | 26/30 (LoVo, A-427, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +10.5 | 8e-24 | 26/30 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.84×** | +9.7 | 3e-20 | 22/30 (A498, J82, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +8.4 | 3e-15 | 26/30 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +7.5 | 3e-12 | 25/31 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +7.5 | 4e-12 | 22/31 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +7.4 | 7e-12 | 20/31 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.32×** | +7.0 | 1e-10 | 18/28 (Panc 03.27, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.46×** | +6.0 | 8e-08 | 20/31 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.47×** | +5.8 | 2e-07 | 19/31 (J82, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.62×** | +5.5 | 2e-06 | 15/31 (A498, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.1 | 1e-05 | 17/31 (HOP62, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.79×** | +4.8 | 4e-05 | 19/31 (A498, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.76×** | +4.7 | 8e-05 | 20/30 (CFPAC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.003 | 14/30 (A498, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8947.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -10.1 | 2e-21 | 19/25 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.568×** | -9.0 | 7e-17 | 23/31 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.594×** | -8.3 | 2e-14 | 23/31 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -8.0 | 1e-13 | 20/28 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -7.5 | 9e-12 | 19/29 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.743×** | -4.7 | 2e-04 | 19/31 (NCI-H23, RKO, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.821×** | -4.4 | 7e-04 | 16/31 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.788×** | -3.8 | 0.010 | 14/30 (A-427, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.7 | 0.011 | 1/31 (hTERT-HPNE) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.792×** | -3.7 | 0.011 | 11/31 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.043 | 15/31 (RKO, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.864× | -3.3 | 0.044 | 13/31 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.675×** | -3.3 | 0.047 | 11/30 (NCI-H23, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.811×** | -3.2 | 0.065 | 7/31 (NCI-H23, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 81.8 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +30.1) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.471× (z -10.0) |
| [[A498 (line)]] | wt | 43.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +16.8) | — |
| [[A-427 (line)]] | wt | 62.5 | 3 (1 ⚠) | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.77× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.247× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 29.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -9.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 37.0 | 4 | 1 | [[Auranofin (drug)]] 5 µM 4.17× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.316× (z -9.9) |
| [[J82 (line)]] | alt | 74.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +16.3) | — |
| [[LoVo (line)]] | wt | 51.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -13.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 68.0 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.00× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.284× (z -12.0) |
| [[KATO III (line)]] | alt | 47.1 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.89× (z +13.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 42.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -11.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 23.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +16.5) | — |
| [[HT-29 (line)]] | alt | 21.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 36.4 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.80× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.405× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 125 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.34× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.352× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 34.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 76.9 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 29.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 75.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.6) | — |
| [[RKO (line)]] | wt | 96.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.23× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -21.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +14.4) | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.125× (z -9.1) |
| [[Hs 766T (line)]] | wt | 44.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 41.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.0) | — |
| [[A-172 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF3]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 | STRING 528 |
| [[ZNF101]] | +0.56 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[GINS3]] | +0.54 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[RHBDD3]] | +0.54 | +0.47 / +0.31 | both halves | 2e-04 |  |
| [[TIRAP-AS1]] | +0.53 | +0.37 / +0.40 | both halves | 9e-05 |  |
| [[ANKRD18B]] | +0.52 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[ZNF85]] | +0.52 | +0.34 / +0.40 | both halves | 1e-04 |  |
| [[ZCCHC8]] | +0.52 | +0.32 / +0.29 | both halves | 2e-04 |  |
| [[ZNF525]] | +0.52 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[NUP62]] | +0.51 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[SMAD1]] | +0.51 | +0.39 / +0.31 | both halves | 2e-04 |  |
| [[LRRC61]] | +0.51 | +0.26 / +0.45 | both halves | 4e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPN1]] | -0.57 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CYB5R3]] | -0.57 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[NOMO1]] | -0.53 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[GALNS]] | -0.53 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[RSU1]] | -0.51 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[HEMK1]] | -0.51 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[GNAI2]] | -0.50 | -0.36 / -0.21 | both halves | 6e-04 |  |
| [[CHP1]] | -0.50 | -0.09 / -0.49 | ⚠ not reproduced | 0.003 |  |
| [[ERGIC1]] | -0.49 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[PCMT1]] | -0.48 | -0.37 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[RAB40B]] | -0.47 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[PI4KA]] | -0.47 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[ADIPOR1]] | -0.46 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[RNF123]] | -0.46 | -0.28 / -0.31 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMI]] | B | CGAS activity raises NMI's level | lines that do not express CGAS (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without CGAS | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[SMAD1]] | B | CGAS activity lowers SMAD1's level | lines that do not express CGAS (17) vs lines expressing it (33) | 1.69× higher at baseline in the lines without CGAS | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[GCNT4]] | B | CGAS activity raises GCNT4's level | lines that do not express CGAS (17) vs lines expressing it (33) | 1.26× lower at baseline in the lines without CGAS | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| cells under [[Bendamustine (drug)]] 5 µM | B | CGAS activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express CGAS (17) vs lines expressing it (31) | the lines without CGAS: 0.82× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[DGKE]] | B | CGAS activity raises DGKE's level | lines that do not express CGAS (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without CGAS | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[MEX3A]] | B | CGAS activity lowers MEX3A's level | lines that do not express CGAS (17) vs lines expressing it (33) | 2.22× higher at baseline in the lines without CGAS | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| cells under [[Tranilast (drug)]] 0.5 µM | B | CGAS activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express CGAS (17) vs lines expressing it (31) | the lines without CGAS: 0.83× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[PAG1]] | B | CGAS activity weakens PAG1's drug response | lines that do not express CGAS (11) vs lines expressing it (23) | the lines without CGAS respond 1.09× as strongly (z diff -0.38); strongest at Tucidinostat 5 µM: 2.56x vs 1.50x (z diff -3.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP; target measured in part of the lines; both ways; artifact flags |
| [[IL15RA]] | B | CGAS activity raises IL15RA's level | lines that do not express CGAS (17) vs lines expressing it (33) | 1.29× lower at baseline in the lines without CGAS | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| cells under [[Posaconazole (drug)]] 0.5 µM | B | CGAS activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express CGAS (17) vs lines expressing it (31) | the lines without CGAS: 0.84× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | B | CGAS activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express CGAS (17) vs lines expressing it (31) | the lines without CGAS: 0.83× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **-** arm (projection on the module's main direction -0.395). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (14.2, 1.2); signed map (17.3, -18.2). **Vector** length 95.5, 26.7% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +15.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +14.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.4 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +23.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.8 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.3 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.9 | -8.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -4.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclic GMP-AMP synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:73,413,515-73,452,297 (-) |
| Ensembl biotype | protein_coding |
| Also known as | h-cGAS, D4; previously C6orf150, MB21D1 |
| Reactome | 7 pathways, smallest: STING mediated induction of host immune responses; Dengue virus activates/modulates innate and adaptive immune responses; Cytosolic sensors of pathogen-associated DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N884](https://www.uniprot.org/uniprotkb/Q8N884) (Cyclic GMP-AMP synthase):

> Nucleotidyltransferase that catalyzes the formation of cyclic GMP-AMP (2',3'-cGAMP) from ATP and GTP and plays a key role in innate immunity. Catalysis involves both the formation of a 2',5' phosphodiester linkage at the GpA step and the formation of a 3',5' phosphodiester linkage at the ApG step, producing c[G(2',5')pA(3',5')p]. Acts as a key DNA sensor: directly binds double-stranded DNA (dsDNA), inducing the formation of liquid-like droplets in which CGAS is activated, leading to synthesis …

**Summary**, from NCBI Gene [115004](https://www.ncbi.nlm.nih.gov/gene/115004):

> Enables several functions, including 2',3'-cyclic GMP-AMP synthase activity; molecular condensate scaffold activity; and phosphatidylinositol-4,5-bisphosphate binding activity. Involved in several processes, including negative regulation of double-strand break repair via homologous recombination; paracrine signaling; and regulation of defense response. Located in nuclear body; plasma membrane; and site of double-strand break. Is active in cytosol and nucleus. [provided by Alliance of Genome …

**Accessions** — [HGNC:21367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21367) · Entrez [115004](https://www.ncbi.nlm.nih.gov/gene/115004) · UniProt [Q8N884](https://www.uniprot.org/uniprotkb/Q8N884) · Ensembl [ENSG00000164430](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164430)

## Data

Gene col 8947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8947); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8947]; `tensor/DDL_lfc|DDL_z.npy` [8947]; `embed/gene_vectors.npy` [8947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8947 or target_col == 8947). Every well: [[CGAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CGAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

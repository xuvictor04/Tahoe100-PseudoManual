---
symbol: "EIF1AX"
type: "gene"
col: 10415
ensembl_id: "ENSG00000173674"
name: "eukaryotic translation initiation factor 1A X-linked"
location: "Xp22.12"
module: 111
arm: "+"
pooled_cpm: 63.77
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# EIF1AX

*eukaryotic translation initiation factor 1A X-linked* — Xp22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.99× (z +17.9, q 0e+00, up in 46 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.63× (z +8.0, q 7e-14, up in 39 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRPPRC]] (+0.56, fdr 3e-05), [[CHML]] (+0.55, fdr 2e-05), [[CDC42]] (+0.55, fdr 2e-05); moves opposite to [[GORASP1]] (-0.56, fdr 1e-04), [[THAP3]] (-0.53, fdr 1e-04), [[TMEM101]] (-0.52, fdr 9e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 24 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.99×** | +17.9 | 0e+00 | 46/48 (NCI-H1792, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.72×** | +15.1 | 0e+00 | 44/45 (KATO III, HS-578T, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.12×** | +12.3 | 2e-32 | 47/48 (NCI-H1792, HS-578T, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.28×** | +11.7 | 1e-29 | 37/42 (A549, NCI-H1573, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.95×** | +10.9 | 2e-25 | 46/48 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.93×** | +10.7 | 1e-24 | 45/48 (A498, NCI-H1792, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.71×** | +8.7 | 2e-16 | 41/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.67×** | +8.3 | 6e-15 | 40/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.43×** | +8.3 | 7e-15 | 33/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +8.0 | 7e-14 | 39/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +7.6 | 2e-12 | 43/49 (NCI-H1573, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +6.6 | 2e-09 | 33/46 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +6.5 | 3e-09 | 33/48 (BT-474, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +6.1 | 5e-08 | 36/48 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.52×** | +5.9 | 1e-07 | 34/48 (A498, NCI-H1792, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +5.2 | 6e-06 | 28/48 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.002 | 22/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.015 | 21/48 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.017 | 15/49 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Arbutin (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.018 | 14/48 (A498, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.025 | 19/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.070 | 16/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.070 | 14/48 (MIA PaCa-2, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +2.8 | 0.088 | 15/48 (HT-29, SNU-423, …) | rises with dose |  |
| [[Captopril (drug)]] 0.5 µM |  | 1.19× | +2.8 | 0.088 | 6/48 (NCI-H2347, CHP-212, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.38×** | +2.7 | 0.094 | 15/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +2.7 | 0.099 | 15/48 (NCI-H460, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 63.7 | 11 (11 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +15.1) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H1792 (line)]] | alt | 53.6 | 10 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.30× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 68.2 | 8 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 65.9 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.36× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 62.8 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A549 (line)]] | wt | 55.3 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 96.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +8.9) | — |
| [[KATO III (line)]] | alt | 77.8 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.90× (z +18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H1573 (line)]] | alt | 43.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW1417 (line)]] | alt | 90.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.3) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[SW480 (line)]] | alt | 107 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Hs 766T (line)]] | wt | 59.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 50.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 31.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LS 180 (line)]] | wt | 51.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 91.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 33.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 61.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.2) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 38.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 56.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[Panc 03.27 (line)]] | alt | 61.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[RKO (line)]] | wt | 81.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.09× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RPMI-7951 (line)]] | alt | 50.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[AsPC-1 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[C32 (line)]] | wt | 43.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.6) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[H4 (line)]] | wt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.31× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HCT15 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HEC-1-A (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H23 (line)]] | alt | 51.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SHP-77 (line)]] | alt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRPPRC]] | +0.56 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[CHML]] | +0.55 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[CDC42]] | +0.55 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[GNB1]] | +0.55 | +0.32 / +0.54 | both halves | 2e-04 |  |
| [[DHX9]] | +0.54 | +0.48 / +0.63 | both halves | 2e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[LYRM7]] | +0.53 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[DHX15]] | +0.53 | +0.35 / +0.64 | both halves | 1e-04 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[SYNCRIP]] | +0.53 | +0.53 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 494 |
| [[HNRNPC]] | +0.53 | +0.46 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PPA1]] | +0.51 | +0.39 / +0.58 | both halves | 6e-05 | STRING 410 |
| [[CCT2]] | +0.51 | +0.51 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[LINC00342]] | +0.50 | +0.41 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GORASP1]] | -0.56 | -0.32 / -0.56 | both halves | 1e-04 |  |
| [[THAP3]] | -0.53 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TMEM101]] | -0.52 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[LSM8]] | -0.51 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[GUCA1B]] | -0.51 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CDC37L1]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[DPF2]] | -0.50 | -0.22 / -0.54 | both halves | 6e-04 |  |
| [[ZFAND2B]] | -0.49 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[CASKIN2]] | -0.49 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[DOLPP1]] | -0.49 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[CCDC117]] | -0.49 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[COG7]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-51.0, -9.0); signed map (12.1, -4.2). **Vector** length 66.9, 17.6% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.0 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +2.4 | +17.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.2 | +12.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.2 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +3.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.2 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -2.5 | +8.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 1A X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.12 — chrX:20,124,525-20,141,838 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eIF-1A, eIF-4C; previously EIF4C, EIF1A |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P47813](https://www.uniprot.org/uniprotkb/P47813) (Eukaryotic translation initiation factor 1A, X-chromosomal):

> Component of the 43S pre-initiation complex (43S PIC), which binds to the mRNA cap-proximal region, scans mRNA 5'-untranslated region, and locates the initiation codon. This protein enhances formation of the cap-proximal complex. Together with EIF1, facilitates scanning, start codon recognition, promotion of the assembly of 48S complex at the initiation codon (43S PIC becomes 48S PIC after the start codon is reached), and dissociation of aberrant complexes. After start codon location, together …

**Summary**, from NCBI Gene [1964](https://www.ncbi.nlm.nih.gov/gene/1964):

> This gene encodes an essential eukaryotic translation initiation factor. The protein is required for the binding of the 43S complex (a 40S subunit, eIF2/GTP/Met-tRNAi and eIF3) to the 5' end of capped RNA. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3250) · Entrez [1964](https://www.ncbi.nlm.nih.gov/gene/1964) · UniProt [P47813](https://www.uniprot.org/uniprotkb/P47813) · Ensembl [ENSG00000173674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173674)

## Data

Gene col 10415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10415); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10415]; `tensor/DDL_lfc|DDL_z.npy` [10415]; `embed/gene_vectors.npy` [10415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10415 or target_col == 10415). Every well: [[EIF1AX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF1AX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

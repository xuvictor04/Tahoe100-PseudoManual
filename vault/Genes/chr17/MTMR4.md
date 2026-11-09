---
symbol: "MTMR4"
type: "gene"
col: 2941
ensembl_id: "ENSG00000108389"
name: "myotubularin related protein 4"
location: "17q22"
module: 17
arm: "+"
pooled_cpm: 39.21
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MTMR4

*myotubularin related protein 4* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.40× (z +7.0, q 2e-09, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.503× (z -10.2, q 2e-21, down in 36 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.568× (z -8.4, q 1e-14, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5A]] (+0.55, fdr 5e-05), [[EDN2]] (+0.55, fdr 3e-05), [[MAN1B1]] (+0.53, fdr 5e-05); moves opposite to [[REEP3]] (-0.57, fdr 1e-05), [[BICD1]] (-0.55, fdr 1e-05), [[DDX5]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +7.0 | 2e-09 | 27/48 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +5.5 | 1e-05 | 23/48 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +4.4 | 0.002 | 24/49 (PANC-1, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.23× | +3.1 | 0.26 | 14/48 (HOP62, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.503×** | -10.2 | 2e-21 | 36/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.525×** | -9.1 | 2e-17 | 34/40 (Panc 03.27, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -8.4 | 1e-14 | 34/48 (KATO III, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.570×** | -7.7 | 2e-12 | 28/44 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -7.7 | 2e-12 | 32/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.617×** | -7.1 | 1e-10 | 37/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.678×** | -5.7 | 7e-07 | 37/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.709×** | -5.1 | 2e-05 | 25/48 (SW480, HT-29, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.709×** | -5.1 | 2e-05 | 29/48 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.791×** | -4.9 | 5e-05 | 23/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -4.7 | 1e-04 | 31/47 (hTERT-HPNE, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.741×** | -4.4 | 4e-04 | 27/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.002 | 25/48 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.770×** | -3.9 | 0.005 | 23/48 (SNU-1, KATO III, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -3.8 | 0.006 | 20/48 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.788×** | -3.3 | 0.030 | 18/48 (KATO III, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -3.3 | 0.034 | 19/48 (KATO III, HT-29, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.808×** | -3.1 | 0.049 | 18/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.810×** | -3.1 | 0.054 | 15/48 (A-172, A498, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.810×** | -3.0 | 0.070 | 14/47 (NCI-H23, NCI-H1573, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 44.9 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -11.7) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.484× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 36.1 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -16.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 34.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 48.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.5) |
| [[A-172 (line)]] | wt | 50.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.151× (z -16.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 48.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 43.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 46.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.241× (z -9.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 65.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.308× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 35.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 36.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 32.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.311× (z -10.9) |
| [[A-427 (line)]] | wt | 42.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 38.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.1) | — |
| [[BT-474 (line)]] | alt | 69.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.9) |
| [[COLO 205 (line)]] | alt | 35.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 36.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -8.7) |
| [[KATO III (line)]] | alt | 53.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -13.5) |
| [[PANC-1 (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +25.4) | — |
| [[SW480 (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -19.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 58.8 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.144× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +16.1) | — |
| [[CHP-212 (line)]] | wt | 83.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -9.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 60.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +14.2) | — |
| [[LS 180 (line)]] | wt | 35.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 37.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.353× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.7) |
| [[SNU-1 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.238× (z -8.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SNU-423 (line)]] | alt | 36.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -12.1) |
| [[SW 900 (line)]] | alt | 39.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.278× (z -10.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5A]] | +0.55 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[EDN2]] | +0.55 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[MAN1B1]] | +0.53 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[PRPF39]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ILVBL]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[CEPT1]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 | pathway: Phospholipid metabolism |
| [[TYK2]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[RBBP9]] | +0.52 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[THYN1]] | +0.51 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[ZMYM3]] | +0.50 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PRRC1]] | +0.50 | +0.58 / +0.32 | both halves | 1e-04 |  |
| [[BAD]] | +0.50 | +0.54 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REEP3]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[BICD1]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[DDX5]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[NUP50-DT]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TBILA]] | -0.53 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[MIR31HG]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[SUSD1]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[S100A11]] | -0.51 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ATXN10]] | -0.51 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[EIF3J]] | -0.50 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ZNF83]] | -0.49 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[UBASH3B]] | -0.48 | -0.40 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (2.8, -23.6); signed map (-24.5, -12.1). **Vector** length 107, 27.4% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +7.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.7 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +3.2 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.2 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.5 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.8 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,489,529-58,517,905 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0647, ZFYVE11 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Myotubularins; Phosphoinositide phosphatases |
| Reactome | 9 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Synthesis of PIPs at the early endosome membrane; Downregulation of TGF-beta receptor signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYA4](https://www.uniprot.org/uniprotkb/Q9NYA4) (Phosphatidylinositol-3,5-bisphosphate 3-phosphatase MTMR4):

> Lipid phosphatase that specifically dephosphorylates the D-3 position of phosphatidylinositol 3-phosphate and phosphatidylinositol 3,5-bisphosphate, generating phosphatidylinositol and phosphatidylinositol 5-phosphate. Decreases the levels of phosphatidylinositol 3-phosphate, a phospholipid found in cell membranes where it acts as key regulator of both cell signaling and intracellular membrane traffic, in a subset of endosomal membranes to negatively regulate both endocytic recycling and …

**Summary**, from NCBI Gene [9110](https://www.ncbi.nlm.nih.gov/gene/9110):

> Enables several functions, including R-SMAD binding activity; phosphatidylinositol phosphate phosphatase activity; and protein phosphatase binding activity. Involved in several processes, including midbody abscission; negative regulation of transmembrane receptor protein serine/threonine kinase signaling pathway; and phosphatidylinositol dephosphorylation. Located in early endosome membrane; late endosome membrane; and recycling endosome membrane. Is active in early phagosome membrane and …

**Accessions** — [HGNC:7452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7452) · Entrez [9110](https://www.ncbi.nlm.nih.gov/gene/9110) · UniProt [Q9NYA4](https://www.uniprot.org/uniprotkb/Q9NYA4) · Ensembl [ENSG00000108389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108389)

## Data

Gene col 2941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2941); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2941]; `tensor/DDL_lfc|DDL_z.npy` [2941]; `embed/gene_vectors.npy` [2941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2941 or target_col == 2941). Every well: [[MTMR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

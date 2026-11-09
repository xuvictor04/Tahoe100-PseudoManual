---
symbol: "DCPS"
type: "gene"
col: 3109
ensembl_id: "ENSG00000110063"
name: "decapping enzyme, scavenger"
location: "11q24.2"
module: 1
arm: "+"
pooled_cpm: 15.65
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DCPS

*decapping enzyme, scavenger* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.41× (z +7.4, q 6e-11, up in 20 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +7.3, q 6e-11, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.650× (z -9.3, q 5e-18, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM26]] (+0.62, fdr 1e-05), [[MCCC2]] (+0.62, fdr 1e-05), [[DIS3L]] (+0.62, fdr 1e-05); moves opposite to [[FAM89B]] (-0.58, fdr 4e-05), [[GNB2]] (-0.56, fdr 5e-05), [[DNASE1L1]] (-0.55, fdr 9e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.4 | 6e-11 | 20/38 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.3 | 6e-11 | 19/47 (HEC-1-A, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +7.2 | 8e-11 | 13/26 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.34×** | +5.8 | 9e-07 | 17/46 (LOX-IMVI, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +5.4 | 7e-06 | 13/32 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +5.2 | 2e-05 | 12/43 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.001 | 10/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 0.002 | 11/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.005 | 8/47 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.026 | 6/47 (NCI-H2030, HT-29, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.060 | 6/45 (C32, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.087 | 5/47 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3109.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -9.3 | 5e-18 | 25/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.655×** | -9.2 | 1e-17 | 28/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -7.6 | 5e-12 | 20/48 (C-33 A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.720×** | -7.1 | 1e-10 | 18/48 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.722×** | -7.1 | 2e-10 | 20/48 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -6.9 | 4e-10 | 22/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.766×** | -5.8 | 6e-07 | 21/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -5.3 | 8e-06 | 15/46 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.791×** | -5.1 | 2e-05 | 18/47 (KATO III, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.792×** | -5.1 | 2e-05 | 19/46 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -4.9 | 4e-05 | 15/48 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.663×** | -4.7 | 1e-04 | 12/48 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.810×** | -4.6 | 2e-04 | 16/47 (HCT15, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.675×** | -4.5 | 3e-04 | 9/48 (SNU-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.806×** | -4.2 | 0.001 | 17/44 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.825×** | -4.2 | 0.001 | 13/47 (KATO III, C-33 A, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.815×** | -4.0 | 0.002 | 10/47 (HT-29, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.71 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -9.0) |
| [[H4 (line)]] | wt | 13.2 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0829× (z -9.1) |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.2) |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 1 | — | [[Trametinib (drug)]] 0.05 µM 0.276× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0447× (z -26.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -12.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM26]] | +0.62 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MCCC2]] | +0.62 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[DIS3L]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PYM1]] | +0.61 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[DUS3L]] | +0.60 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SMYD5]] | +0.60 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[UTP15]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MTREX]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[INTS14]] | +0.59 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[SLC5A6]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ICE2]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89B]] | -0.58 | -0.47 / -0.43 | both halves | 4e-05 |  |
| [[GNB2]] | -0.56 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[DNASE1L1]] | -0.55 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[SPAG9]] | -0.54 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[PINK1]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RAPGEF2]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SLC17A7]] | -0.52 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[ARSA]] | -0.52 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[CBL]] | -0.51 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[DUSP18]] | -0.51 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[NDRG1]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[RAP2A]] | -0.51 | -0.56 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.1, 5.9); signed map (9.9, -38.1). **Vector** length 67.2, 10.0% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +0.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.9 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | decapping enzyme, scavenger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:126,304,060-126,350,005 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC015, HINT-5, HSL1, HINT5, DCS-1, DCS1 |
| Gene groups (HGNC) | Histidine triad superfamily |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 3 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C86](https://www.uniprot.org/uniprotkb/Q96C86) (m7GpppX diphosphatase):

> Decapping scavenger enzyme that catalyzes the cleavage of a residual cap structure following the degradation of mRNAs by the 3'->5' exosome-mediated mRNA decay pathway. Hydrolyzes cap analog structures like 7-methylguanosine nucleoside triphosphate (m7GpppG) with up to 10 nucleotide substrates (small capped oligoribonucleotides) and specifically releases 5'-phosphorylated RNA fragments and 7-methylguanosine monophosphate (m7GMP). Cleaves cap analog structures like tri-methyl guanosine …

**Summary**, from NCBI Gene [28960](https://www.ncbi.nlm.nih.gov/gene/28960):

> This gene encodes a member of the histidine triad family of pyrophosphatases that removes short mRNA fragments containing the 5&#8242; mRNA cap structure, which appear in the 3&#8242; &#8594; 5&#8242; mRNA decay pathway, following deadenylation and exosome-mediated turnover. This enzyme hydrolyzes the triphosphate linkage of the cap structure (7-methylguanosine nucleoside triphosphate) to yield 7-methylguanosine monophosphate and nucleoside diphosphate. It protects the cell from the potentially …

**Accessions** — [HGNC:29812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29812) · Entrez [28960](https://www.ncbi.nlm.nih.gov/gene/28960) · UniProt [Q96C86](https://www.uniprot.org/uniprotkb/Q96C86) · Ensembl [ENSG00000110063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110063)

## Data

Gene col 3109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3109); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3109]; `tensor/DDL_lfc|DDL_z.npy` [3109]; `embed/gene_vectors.npy` [3109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3109 or target_col == 3109). Every well: [[DCPS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCPS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

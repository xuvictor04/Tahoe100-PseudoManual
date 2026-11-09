---
symbol: "MYLIP"
type: "gene"
col: 154
ensembl_id: "ENSG00000007944"
name: "myosin regulatory light chain interacting protein"
location: "6p22.3"
module: 59
arm: "+"
pooled_cpm: 45.96
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# MYLIP

*myosin regulatory light chain interacting protein* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.15× (z +24.2, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.520× (z -7.8, q 3e-12, down in 31 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clotrimazole (drug)]] 5 µM: 0.647× (z -7.3, q 6e-11, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L11]] (+0.72, fdr 7e-06), [[OSR2]] (+0.71, fdr 7e-06), [[VASN]] (+0.71, fdr 7e-06); moves opposite to [[TIMM23B-AGAP6]] (-0.65, fdr 1e-05), [[SEC14L1]] (-0.64, fdr 7e-06), [[NOM1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[RASGEF1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.15×** | +24.2 | 0e+00 | 42/46 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.22×** | +14.0 | 3e-42 | 47/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.94×** | +13.0 | 3e-36 | 42/47 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +11.6 | 5e-29 | 37/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.80×** | +11.1 | 2e-26 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.44×** | +10.7 | 7e-25 | 40/45 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.38×** | +10.4 | 2e-23 | 46/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.77×** | +9.8 | 7e-21 | 42/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +9.0 | 2e-17 | 38/47 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +8.9 | 4e-17 | 39/47 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +6.9 | 3e-10 | 41/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.9 | 1e-07 | 36/47 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.55×** | +4.7 | 9e-05 | 29/47 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 6e-04 | 28/47 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.56×** | +4.3 | 7e-04 | 22/45 (PANC-1, J82, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +3.6 | 0.008 | 21/46 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.010 | 19/47 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.017 | 22/48 (KATO III, RKO, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.520×** | -7.8 | 3e-12 | 31/45 (NCI-H2347, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clotrimazole (drug)]] 5 µM |  | **0.647×** | -7.3 | 6e-11 | 40/48 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.569×** | -6.2 | 8e-08 | 27/39 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -5.0 | 9e-05 | 25/37 (Panc 03.27, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bexarotene (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.023 | 26/47 (SK-MEL-2, A549, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.716×** | -3.7 | 0.023 | 21/47 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **0.755×** | -3.3 | 0.068 | 20/47 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.753× | -3.0 | 0.16 | 13/47 (LS 180, RKO, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.836× | -3.0 | 0.16 | 16/47 (NCI-H460, SW 1088, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.6 | 11 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.03× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 51.2 | 5 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -13.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 28.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +19.1) | — |
| [[LoVo (line)]] | wt | 39.0 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.83× (z +14.7) | — |
| [[SW480 (line)]] | alt | 36.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +17.8) | — |
| [[A-172 (line)]] | wt | 14.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.76× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 58.5 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 74.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 63.4 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -13.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 83.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -15.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 48.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 45.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.33× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 55.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.0911× (z -11.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.64× (z +11.5) | — |
| [[A549 (line)]] | wt | 20.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 63.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 20.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +11.5) | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.128× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 37.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +15.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 41.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +16.0) | — |
| [[SNU-423 (line)]] | alt | 43.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -11.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +21.7) | — |
| [[AsPC-1 (line)]] | alt | 33.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +20.1) | — |
| [[C32 (line)]] | wt | 80.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +22.1) | — |
| [[hTERT-HPNE (line)]] | wt | 34.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +19.2) | — |
| [[J82 (line)]] | alt | 67.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +13.7) | — |
| [[NCI-H23 (line)]] | alt | 49.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -13.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 62.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.6) | — |
| [[SW 900 (line)]] | alt | 61.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 72.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 67.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +16.3) | — |
| [[HCT15 (line)]] | alt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 68.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 55.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +14.9) | — |
| [[RKO (line)]] | wt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 38.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 130 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L11]] | +0.72 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[OSR2]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[VASN]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[FAM53C]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[IFRD1]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ID2]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TENT5C]] | +0.65 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[PIM2]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ADM]] | +0.61 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TRA2A]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[RYBP]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[NEDD9]] | +0.61 | +0.56 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | -0.65 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[SEC14L1]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[NOM1]] | -0.61 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.59 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[SDHC]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[TIMM23B]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[TOMM40]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[AGAP6]] | -0.56 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[MCM3AP]] | -0.56 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[TRNT1]] | -0.56 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[PUM3]] | -0.56 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[EFTUD2]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1B]] | B | RASGEF1B activity raises MYLIP's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without RASGEF1B | 0.027 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[FAM13A]] | B | FAM13A activity raises MYLIP's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without FAM13A | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[ATP1B1]] | B | ATP1B1 activity raises MYLIP's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without ATP1B1 | 0.042 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[CA8]] | B | CA8 activity raises MYLIP's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.50× lower at baseline in the lines without CA8 | 0.057 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[RASGEF1B]] | B | RASGEF1B activity weakens MYLIP's drug response | lines that do not express RASGEF1B (9) vs lines expressing it (38) | the lines without RASGEF1B respond 1.29× as strongly (z diff -1.15); strongest at Idarubicin (hydrochloride) 5 µM: 2.63x vs 1.76x (z diff -2.2) | 0.081 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MPZL3]] | B | MPZL3 activity raises MYLIP's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.37× lower at baseline in the lines without MPZL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (30.8, -29.0); signed map (0.1, 17.9). **Vector** length 100.0, 31.0% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members* (reactome, mean cos +0.55 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.0 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -0.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.3 | +2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | +0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | myosin regulatory light chain interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:16,129,086-16,148,248 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MIR, IDOL |
| Gene groups (HGNC) | Ring finger proteins; FERM domain containing; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 10 pathways, smallest: NR1H2 & NR1H3 regulate gene expression to limit cholesterol uptake; VLDLR internalisation and degradation; Plasma lipoprotein clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WY64](https://www.uniprot.org/uniprotkb/Q8WY64) (E3 ubiquitin-protein ligase MYLIP):

> E3 ubiquitin-protein ligase that mediates ubiquitination and subsequent proteasomal degradation of myosin regulatory light chain (MRLC), LDLR, VLDLR and LRP8. Activity depends on E2 enzymes of the UBE2D family. Proteasomal degradation of MRLC leads to inhibit neurite outgrowth in presence of NGF by counteracting the stabilization of MRLC by saposin-like protein (CNPY2/MSAP) and reducing CNPY2-stimulated neurite outgrowth. Acts as a sterol-dependent inhibitor of cellular cholesterol uptake by …

**Summary**, from NCBI Gene [29116](https://www.ncbi.nlm.nih.gov/gene/29116):

> The ERM protein family members ezrin, radixin, and moesin are cytoskeletal effector proteins linking actin to membrane-bound proteins at the cell surface. Myosin regulatory light chain interacting protein (MYLIP) is a novel ERM-like protein that interacts with myosin regulatory light chain and inhibits neurite outgrowth. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21155) · Entrez [29116](https://www.ncbi.nlm.nih.gov/gene/29116) · UniProt [Q8WY64](https://www.uniprot.org/uniprotkb/Q8WY64) · Ensembl [ENSG00000007944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007944)

## Data

Gene col 154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 154); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 154]; `tensor/DDL_lfc|DDL_z.npy` [154]; `embed/gene_vectors.npy` [154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 154 or target_col == 154). Every well: [[MYLIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYLIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

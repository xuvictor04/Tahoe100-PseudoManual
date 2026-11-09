---
symbol: "ARMH1"
type: "gene"
col: 12607
ensembl_id: "ENSG00000198520"
name: "armadillo like helical domain containing 1"
location: "1p34.1"
module: 35
arm: "+"
pooled_cpm: 9.59
n_lines_expressing: 47
n_dd_up: 43
n_dd_down: 20
n_dd_up_clean: 36
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ARMH1

*armadillo like helical domain containing 1* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.85× (z +12.1, q 4e-31, up in 11 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +9.1, q 2e-17, up in 29 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.283× (z -13.3, q 1e-37, down in 35 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFL1P1-1]] (+0.65, fdr 7e-06), [[SLC16A13]] (+0.60, fdr 1e-05), [[PACRG]] (+0.57, fdr 1e-05); moves opposite to [[PALD1]] (-0.50, fdr 3e-05), [[GEMIN4]] (-0.50, fdr 3e-05), [[SLC25A19]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[QPRT]] → it (grade B ⚠); 2 go from it, the strongest it → [[PRXL2A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.85×** | +12.1 | 4e-31 | 11/17 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +10.8 | 1e-24 | 16/32 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +10.2 | 3e-22 | 12/23 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +9.1 | 2e-17 | 29/44 (KATO III, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.34×** | +8.9 | 5e-17 | 30/43 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +8.1 | 6e-14 | 32/44 (A498, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +8.0 | 9e-14 | 28/44 (A498, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.14×** | +8.0 | 1e-13 | 31/44 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +7.9 | 2e-13 | 28/42 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +7.4 | 1e-11 | 26/44 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.58×** | +6.5 | 3e-09 | 23/44 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.98×** | +6.1 | 5e-08 | 21/42 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.9 | 2e-07 | 19/38 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.75×** | +5.9 | 2e-07 | 21/42 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.73×** | +5.7 | 4e-07 | 17/41 (A-427, KATO III, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.78×** | +5.6 | 7e-07 | 23/43 (BT-474, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.65×** | +5.5 | 1e-06 | 18/44 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.46×** | +5.5 | 1e-06 | 24/44 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.283×** | -13.3 | 1e-37 | 35/44 (COLO 205, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.471×** | -11.2 | 8e-27 | 30/41 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.374×** | -10.4 | 6e-23 | 34/43 (HCT15, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.418×** | -9.2 | 4e-18 | 29/43 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.438×** | -8.7 | 3e-16 | 25/39 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.520×** | -6.9 | 4e-10 | 23/38 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.497×** | -6.3 | 2e-08 | 22/42 (PANC-1, BT-474, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.550×** | -6.3 | 2e-08 | 20/44 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.578×** | -5.8 | 4e-07 | 22/44 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.420×** | -4.8 | 9e-05 | 17/38 (NCI-H1573, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.656×** | -4.5 | 4e-04 | 16/44 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.665×** | -4.3 | 7e-04 | 16/43 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.478×** | -4.1 | 0.002 | 17/42 (NCI-H23, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.687×** | -4.0 | 0.003 | 13/42 (MIA PaCa-2, SW48, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.655×** | -3.8 | 0.005 | 15/36 (NCI-H23, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.515×** | -3.7 | 0.009 | 7/41 (SK-MEL-2, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.621×** | -3.6 | 0.011 | 10/44 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.715×** | -3.6 | 0.012 | 12/40 (BT-474, NCI-H1573, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.709×** | -3.1 | 0.051 | 10/43 (NCI-H23, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 42.9 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.58× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -15.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0867× (z -13.1) |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0610× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -9.9) |
| [[SW480 (line)]] | alt | 10.5 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 12.7× (z +14.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.181× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 20.8 | 2 (1 ⚠) | 3 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.10× (z +13.7) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0338× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -9.9) |
| [[KATO III (line)]] | alt | 14.7 | 3 (2 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 5.48× (z +10.5) | [[Digitoxin (drug)]] 0.5 µM 0.0643× (z -12.1) |
| [[A549 (line)]] | wt | 10.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0524× (z -14.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.0) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.158× (z -9.2) |
| [[HT-29 (line)]] | alt | 14.1 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.15× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -12.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -15.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.176× (z -9.6) |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0939× (z -12.9) |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -11.3) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0635× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.14× (z +11.0) ⚠ position not correctable | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.48 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0701× (z -9.0) |
| [[A-172 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL1P1-1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[SLC16A13]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PACRG]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 | same gene group |
| [[RTCA-AS1]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[DMXL1-DT]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[C21orf62-AS1]] | +0.56 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[RAB21]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[WDR31]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[FBXO2]] | +0.54 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[PKIB]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CA11]] | +0.53 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[QPRT]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALD1]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[GEMIN4]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SLC25A19]] | -0.49 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[ATP6V0A2]] | -0.49 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[SLC30A7]] | -0.49 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[NIP7]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[POLR2D]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[TRMT6]] | -0.48 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[DHRS7B]] | -0.48 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[CNOT10]] | -0.47 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[HMGA2]] | -0.47 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[SPOUT1]] | -0.47 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QPRT]] | B | QPRT activity raises ARMH1's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.49× lower at baseline in the lines without QPRT | 0.031 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[FBXO2]] | B | FBXO2 activity raises ARMH1's level | lines that do not express FBXO2 (23) vs lines expressing it (27) | 1.91× lower at baseline in the lines without FBXO2 | 0.037 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, LAMP3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRXL2A]] | C | ARMH1 activity raises PRXL2A's level | lines that do not express ARMH1 (3) vs lines expressing it (47) | 5.14× lower at baseline in the lines without ARMH1 | 0.057 | ⚠ few lines (3 vs 47); across organs; also absent: MCF2L2, KIAA1522, ENSG00000257489; maybe low, not absent |
| [[OLMALINC]] | C | ARMH1 activity raises OLMALINC's level | lines that do not express ARMH1 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without ARMH1 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: MCF2L2, KIAA1522, ENSG00000257489; maybe low, not absent |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.293). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.9, 27.6); signed map (35.4, -2.1). **Vector** length 78.2, 16.2% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +8.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +6.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +5.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.0 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.5 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.2 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.9 | -4.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | armadillo like helical domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,674,692-44,725,591 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33556, p40; previously NCRNA00082, C1orf228 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

UniProt [Q6PIY5](https://www.uniprot.org/uniprotkb/Q6PIY5) carries no function annotation.

**Summary**, from NCBI Gene [339541](https://www.ncbi.nlm.nih.gov/gene/339541):

> Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34345) · Entrez [339541](https://www.ncbi.nlm.nih.gov/gene/339541) · UniProt [Q6PIY5](https://www.uniprot.org/uniprotkb/Q6PIY5) · Ensembl [ENSG00000198520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198520)

## Data

Gene col 12607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12607); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12607]; `tensor/DDL_lfc|DDL_z.npy` [12607]; `embed/gene_vectors.npy` [12607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12607 or target_col == 12607). Every well: [[ARMH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

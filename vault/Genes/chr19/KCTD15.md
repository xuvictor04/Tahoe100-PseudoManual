---
symbol: "KCTD15"
type: "gene"
col: 7745
ensembl_id: "ENSG00000153885"
name: "potassium channel tetramerization domain containing 15"
location: "19q13.11"
module: 133
arm: "+"
pooled_cpm: 5.94
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# KCTD15

*potassium channel tetramerization domain containing 15* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.12× (z +10.0, q 9e-21, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +9.5, q 6e-19, up in 17 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.189× (z -23.1, q 0e+00, down in 37 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM268]] (+0.74, fdr 7e-06), [[MOCOS]] (+0.72, fdr 7e-06), [[NSMAF]] (+0.67, fdr 1e-05); moves opposite to [[ETFB]] (-0.59, fdr 4e-05), [[PKN2]] (-0.57, fdr 1e-05), [[ISCA2]] (-0.56, fdr 5e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 8 go from it, the strongest it → [[SEPHS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +10.0 | 9e-21 | 6/8 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +9.5 | 6e-19 | 17/35 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.94×** | +8.9 | 8e-17 | 27/39 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +8.2 | 4e-14 | 17/39 (HOP62, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.9 | 4e-07 | 15/24 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.35×** | +5.8 | 5e-07 | 14/40 (NCI-H460, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.50×** | +5.6 | 1e-06 | 18/37 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.5 | 6e-04 | 10/16 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (drug)]] 5 µM |  | **1.37×** | +4.3 | 9e-04 | 9/39 (NCI-H460, BT-474, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 8/39 (NCI-H460, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 8/40 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.73×** | +4.0 | 0.003 | 6/28 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.005 | 10/39 (Hs 766T, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.8 | 0.007 | 4/27 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.007 | 5/32 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.008 | 5/39 (A-427, PANC-1, …) | top dose only | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.012 | 4/38 (HCT15, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.189×** | -23.1 | 0e+00 | 37/40 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.336×** | -21.3 | 0e+00 | 29/36 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.216×** | -21.2 | 0e+00 | 36/39 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.217×** | -21.1 | 0e+00 | 36/39 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.345×** | -14.2 | 2e-43 | 32/38 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.365×** | -13.9 | 4e-42 | 31/39 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.504×** | -9.5 | 2e-19 | 22/35 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.533×** | -8.7 | 3e-16 | 24/39 (NCI-H23, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -7.6 | 3e-12 | 18/38 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.682×** | -7.5 | 4e-12 | 22/39 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.400×** | -6.6 | 2e-09 | 19/38 (RPMI-7951, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.632×** | -6.3 | 1e-08 | 18/35 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.496×** | -5.1 | 2e-05 | 15/38 (A498, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.706×** | -4.8 | 6e-05 | 12/39 (LoVo, NCI-H23, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.514×** | -4.8 | 6e-05 | 14/36 (BT-474, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.577×** | -4.0 | 0.002 | 9/36 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.766×** | -3.7 | 0.007 | 15/38 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.63 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -16.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0793× (z -14.1) |
| [[J82 (line)]] | alt | 10.9 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0613× (z -15.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.120× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0565× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 5.47 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0612× (z -13.8) |
| [[PANC-1 (line)]] | alt | 8.71 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -18.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.260× (z -9.4) |
| [[RKO (line)]] | wt | 10.6 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0570× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0922× (z -11.4) |
| [[A498 (line)]] | wt | 13.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.161× (z -12.9) |
| [[H4 (line)]] | wt | 18.6 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0815× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 7.52 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0900× (z -10.7) |
| [[C32 (line)]] | wt | 11.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0722× (z -11.5) |
| [[HT-29 (line)]] | alt | 4.90 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0277× (z -13.3) |
| [[LoVo (line)]] | wt | 6.51 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0181× (z -20.6) |
| [[A549 (line)]] | wt | 6.92 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.142× (z -9.1) |
| [[BT-474 (line)]] | alt | 7.82 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0678× (z -14.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 5.23 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -10.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0948× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 7.67 | 0 | 2 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0693× (z -9.2) |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0599× (z -10.5) |
| [[SW48 (line)]] | wt | 13.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0904× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0575× (z -11.2) |
| [[A-427 (line)]] | wt | 8.34 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.130× (z -10.1) |
| [[HOP62 (line)]] | alt | 4.74 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0826× (z -10.4) |
| [[Hs 766T (line)]] | wt | 9.09 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 5.25 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.106× (z -9.4) |
| [[A-172 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM268]] | +0.74 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[MOCOS]] | +0.72 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[NSMAF]] | +0.67 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SETD7]] | +0.65 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[CAPN15]] | +0.64 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.64 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ADCY3]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[POU6F1]] | +0.62 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[SMG1P7]] | +0.62 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[GTF3C2-AS2]] | +0.61 | +0.27 / +0.62 | both halves | 3e-04 |  |
| [[GARS1-DT]] | +0.61 | +0.33 / +0.69 | both halves | 1e-04 |  |
| [[SLC38A1]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETFB]] | -0.59 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PKN2]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ISCA2]] | -0.56 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[DCTN3]] | -0.56 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[INIP]] | -0.56 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TMEM205]] | -0.55 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TPR]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[LIMA1]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[H3-3B]] | -0.52 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[CTR9]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TRAPPC5]] | -0.52 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[HCFC2]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises KCTD15's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without MSI1 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[NEDD9]] | B | NEDD9 activity lowers KCTD15's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.92× higher at baseline in the lines without NEDD9 | 0.037 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPHS1]] | B | KCTD15 activity raises SEPHS1's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without KCTD15 | 0.008 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[ABCF2]] | B | KCTD15 activity raises ABCF2's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without KCTD15 | 0.060 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[CERS2]] | B | KCTD15 activity raises CERS2's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without KCTD15 | 0.067 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[B3GALNT2]] | B | KCTD15 activity raises B3GALNT2's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without KCTD15 | 0.075 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[POLR3E]] | B | KCTD15 activity raises POLR3E's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without KCTD15 | 0.084 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[CCNJ]] | B | KCTD15 activity raises CCNJ's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without KCTD15 | 0.087 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[THAP4]] | B | KCTD15 activity raises THAP4's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without KCTD15 | 0.089 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[UBQLN4]] | B | KCTD15 activity raises UBQLN4's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without KCTD15 | 0.091 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.7, 14.8); signed map (12.0, -44.5). **Vector** length 75.1, 13.9% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.3 | -14.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -21.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -21.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -23.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Thymol (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -6.6 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:33,795,933-33,815,763 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC25497 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Reactome | 2 pathways, smallest: Negative regulation of activity of TFAP2 (AP-2) family transcription factors; Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SI1](https://www.uniprot.org/uniprotkb/Q96SI1) (BTB/POZ domain-containing protein KCTD15):

> During embryonic development, it is involved in neural crest formation (By similarity). Inhibits AP2 transcriptional activity by interaction with its activation domain.

**Summary**, from NCBI Gene [79047](https://www.ncbi.nlm.nih.gov/gene/79047):

> Enables identical protein binding activity. Predicted to be involved in negative regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23297) · Entrez [79047](https://www.ncbi.nlm.nih.gov/gene/79047) · UniProt [Q96SI1](https://www.uniprot.org/uniprotkb/Q96SI1) · Ensembl [ENSG00000153885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153885)

## Data

Gene col 7745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7745); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7745]; `tensor/DDL_lfc|DDL_z.npy` [7745]; `embed/gene_vectors.npy` [7745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7745 or target_col == 7745). Every well: [[KCTD15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

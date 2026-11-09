---
symbol: "LONRF3"
type: "gene"
col: 10621
ensembl_id: "ENSG00000175556"
name: "LON peptidase N-terminal domain and ring finger 3"
location: "Xq24"
module: 92
arm: "+"
pooled_cpm: 32.58
n_lines_expressing: 40
n_dd_up: 37
n_dd_down: 15
n_dd_up_clean: 28
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 6
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# LONRF3

*LON peptidase N-terminal domain and ring finger 3* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +20.9, q 0e+00, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.686× (z -6.9, q 2e-09, down in 25 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS17]] (+0.57, fdr 1e-05), [[RASGRF1]] (+0.56, fdr 2e-05), [[MCTP1]] (+0.53, fdr 1e-05); moves opposite to [[HTT]] (-0.53, fdr 2e-05), [[CDC23]] (-0.50, fdr 2e-05), [[ANAPC10]] (-0.49, fdr 4e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LRATD2]] → it (grade B ⚠); 6 go from it, the strongest it → [[DPH1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +20.9 | 0e+00 | 36/38 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.29×** | +18.5 | 0e+00 | 32/37 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +17.2 | 0e+00 | 35/37 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.86×** | +16.3 | 0e+00 | 30/36 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.48×** | +14.1 | 4e-43 | 32/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.45×** | +13.9 | 4e-42 | 30/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +13.0 | 6e-37 | 32/37 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +10.9 | 9e-26 | 32/38 (SW1417, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +10.2 | 1e-22 | 27/36 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +9.2 | 2e-18 | 31/37 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +9.2 | 3e-18 | 27/37 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +8.8 | 8e-17 | 23/37 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +7.8 | 2e-13 | 22/37 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +7.8 | 3e-13 | 25/37 (NCI-H460, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.59×** | +7.2 | 3e-11 | 22/37 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +7.1 | 3e-11 | 25/37 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +6.8 | 4e-10 | 22/38 (COLO 205, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +5.5 | 1e-06 | 22/36 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.686×** | -6.9 | 2e-09 | 25/38 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.717×** | -5.5 | 1e-05 | 19/39 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.702×** | -5.2 | 4e-05 | 23/37 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.735×** | -4.8 | 2e-04 | 20/37 (C32, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.752×** | -4.4 | 0.001 | 21/38 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.757×** | -4.3 | 0.001 | 19/37 (SNU-423, KATO III, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.590×** | -4.2 | 0.002 | 16/36 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.814×** | -4.0 | 0.005 | 12/38 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.836× | -3.9 | 0.006 | 16/38 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.772×** | -3.7 | 0.011 | 12/37 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.815×** | -3.5 | 0.029 | 12/38 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.741×** | -3.3 | 0.040 | 9/35 (C32, SW480, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.045 | 11/37 (SNU-423, NCI-H1573, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.667×** | -3.2 | 0.050 | 10/32 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.864× | -3.1 | 0.067 | 10/38 (SW480, C32, …) | all doses, flat |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.819×** | -3.1 | 0.067 | 12/37 (NCI-H1792, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.9 | 15 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +14.8) | — |
| [[SW480 (line)]] | alt | 51.2 | 10 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 6.02× (z +17.7) | — |
| [[C32 (line)]] | wt | 56.8 | 2 (1 ⚠) | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.37× (z +10.7) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.224× (z -10.3) |
| [[HOP62 (line)]] | alt | 11.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +18.4) | — |
| [[PANC-1 (line)]] | alt | 17.9 | 8 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.66× (z +11.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 3.75× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 37.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +22.9) | — |
| [[NCI-H2347 (line)]] | alt | 45.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +17.3) | — |
| [[SW 900 (line)]] | alt | 29.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 28.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +21.7) | — |
| [[HT-29 (line)]] | alt | 52.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +14.6) | — |
| [[BT-474 (line)]] | alt | 50.1 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.223× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 65.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +18.2) | — |
| [[COLO 205 (line)]] | alt | 106 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +14.3) | — |
| [[HepG2_C3A (line)]] | wt | 91.3 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 64.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +15.0) | — |
| [[KATO III (line)]] | alt | 60.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 64.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +13.7) | — |
| [[SK-MEL-2 (line)]] | alt | 45.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.27× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0993× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 32.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +16.0) | — |
| [[Hs 766T (line)]] | wt | 32.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 31.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.60× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.01× (z +8.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H1792 (line)]] | alt | 57.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.00× (z +8.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0607× (z -10.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 6.70 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS17]] | +0.57 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[RASGRF1]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MCTP1]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[AP3B2]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[KLHL29]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[PRKCE]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[KDSR]] | +0.52 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[NPTX2]] | +0.51 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[RASGRF2]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[SPRED1]] | +0.50 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[KDM7A-DT]] | +0.50 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[HAP1]] | +0.50 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HTT]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CDC23]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ANAPC10]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SACM1L]] | -0.49 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[LMO3]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[TNKS]] | -0.48 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[VTI1B]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[RAB18]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[LONP2]] | -0.46 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[HBS1L]] | -0.46 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[STX18]] | -0.46 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ATF6B]] | -0.46 | -0.48 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRATD2]] | B | LRATD2 activity raises LONRF3's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.93× lower at baseline in the lines without LRATD2 | 0.006 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[PHLDA2]] | B | PHLDA2 activity raises LONRF3's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 3.64× lower at baseline in the lines without PHLDA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises LONRF3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[KLF5]] | B | KLF5 activity raises LONRF3's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without KLF5 | 0.057 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[NPTX2]] | B | NPTX2 activity raises LONRF3's level | lines that do not express NPTX2 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without NPTX2 | 0.063 | ⚠ within organs, on part of the lines; also absent: TEX15, RUNX3, ZYG11A |
| [[CCL20]] | B | CCL20 activity raises LONRF3's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without CCL20 | 0.068 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[SDC4]] | B | SDC4 activity raises LONRF3's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 4.77× lower at baseline in the lines without SDC4 | 0.087 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |
| [[VDR]] | C | VDR activity raises LONRF3's level | lines that do not express VDR (8) vs lines expressing it (42) | 4.29× lower at baseline in the lines without VDR | 0.022 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPH1-AS1]] | B | LONRF3 activity lowers DPH1-AS1's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 1.32× higher at baseline in the lines without LONRF3 | 0.009 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64 |
| [[EPHA2]] | B | LONRF3 activity raises EPHA2's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 2.76× lower at baseline in the lines without LONRF3 | 0.028 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64 |
| [[SDC4]] | B | LONRF3 activity raises SDC4's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 2.54× lower at baseline in the lines without LONRF3 | 0.042 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64 |
| [[HAP1]] | B | LONRF3 activity raises HAP1's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without LONRF3 | 0.060 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64 |
| [[HMBOX1]] | B | LONRF3 activity lowers HMBOX1's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 1.43× higher at baseline in the lines without LONRF3 | 0.069 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64 |
| [[VDR]] | C | LONRF3 activity raises VDR's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 3.38× lower at baseline in the lines without LONRF3 | 0.016 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64; co-absent with the target |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.3, 6.0); signed map (11.6, 21.4). **Vector** length 103, 27.9% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +9.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +10.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +3.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -1.3 |
|  | [[NG25 (drug)]] 5 µM |  | -4.0 | -4.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.6 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | LON peptidase N-terminal domain and ring finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:118,974,614-119,018,355 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22612; previously RNF127 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

UniProt [Q496Y0](https://www.uniprot.org/uniprotkb/Q496Y0) carries no function annotation.

**Summary**, from NCBI Gene [79836](https://www.ncbi.nlm.nih.gov/gene/79836):

> The protein encoded by this gene contains a RING finger domain, a motif present in a variety of functionally distinct proteins and known to be involved in protein-protein and protein-DNA interactions. Multiple alternatively spliced transcript variants have been suggested, but their full length natures are not clear. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21152) · Entrez [79836](https://www.ncbi.nlm.nih.gov/gene/79836) · UniProt [Q496Y0](https://www.uniprot.org/uniprotkb/Q496Y0) · Ensembl [ENSG00000175556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175556)

## Data

Gene col 10621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10621); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10621]; `tensor/DDL_lfc|DDL_z.npy` [10621]; `embed/gene_vectors.npy` [10621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10621 or target_col == 10621). Every well: [[LONRF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LONRF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

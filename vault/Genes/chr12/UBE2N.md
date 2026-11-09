---
symbol: "UBE2N"
type: "gene"
col: 10875
ensembl_id: "ENSG00000177889"
name: "ubiquitin conjugating enzyme E2 N"
location: "12q22"
module: 74
arm: "+"
pooled_cpm: 78.59
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# UBE2N

*ubiquitin conjugating enzyme E2 N* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.24× (z +12.8, q 8e-35, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.745× (z -6.1, q 5e-07, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NME1]] (+0.63, fdr 7e-06), [[UTP4]] (+0.60, fdr 1e-05), [[TBRG4]] (+0.60, fdr 7e-06); moves opposite to [[GPX4]] (-0.61, fdr 1e-05), [[KLHL24]] (-0.60, fdr 7e-06), [[AKAP9]] (-0.60, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +12.8 | 8e-35 | 46/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +11.7 | 2e-29 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.67×** | +10.6 | 4e-24 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +10.1 | 1e-21 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +9.3 | 2e-18 | 45/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +8.7 | 3e-16 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +8.6 | 8e-16 | 30/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.14×** | +8.3 | 9e-15 | 39/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +7.6 | 3e-12 | 36/48 (HT-29, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +7.1 | 9e-11 | 29/37 (NCI-H1573, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +7.0 | 1e-10 | 35/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.39×** | +6.9 | 2e-10 | 32/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.39×** | +6.6 | 1e-09 | 31/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.39×** | +6.6 | 1e-09 | 29/47 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.7 | 3e-07 | 31/48 (SW480, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +4.8 | 4e-05 | 29/48 (A498, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +4.7 | 8e-05 | 29/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | **1.24×** | +4.4 | 3e-04 | 25/48 (SW480, LS 180, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.001 | 20/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.001 | 24/48 (SW48, SW 1271, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.002 | 20/48 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.006 | 20/48 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.009 | 18/48 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.745×** | -6.1 | 5e-07 | 35/48 (KATO III, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.777×** | -5.3 | 3e-05 | 31/50 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.776×** | -5.1 | 7e-05 | 27/47 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.826×** | -4.8 | 2e-04 | 26/48 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.819×** | -4.8 | 2e-04 | 26/48 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.808×** | -4.4 | 9e-04 | 26/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.860× | -4.3 | 0.001 | 16/49 (HEC-1-A, A498, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.817×** | -4.2 | 0.002 | 23/47 (A549, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.826×** | -4.0 | 0.004 | 21/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.703×** | -3.8 | 0.007 | 16/50 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.855× | -3.8 | 0.008 | 20/49 (SW480, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.848× | -3.4 | 0.028 | 15/49 (H4, LoVo, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.851× | -3.4 | 0.032 | 11/48 (KATO III, LoVo, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.844× | -3.4 | 0.032 | 18/48 (SK-MEL-2, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.901× | -3.0 | 0.10 | 5/48 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 86.4 | 9 (8 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +13.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.81× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 72.1 | 9 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +16.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.68× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 76.4 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +14.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.83× (z +10.7) | — |
| [[SW480 (line)]] | alt | 86.6 | 8 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.72× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.61× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 123 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.95× (z +8.8) | — |
| [[LoVo (line)]] | wt | 112 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.91× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.43× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 68.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 55.7 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.78× (z +10.0) ⚠ unreliable plate only | — |
| [[LS 180 (line)]] | wt | 84.3 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +12.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 80.6 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.65× (z +9.5) ⚠ toxic; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 91.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +8.5) | — |
| [[C32 (line)]] | wt | 58.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.07× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 45.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.90× (z +8.9) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 83.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SHP-77 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.31× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SNU-423 (line)]] | alt | 54.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW48 (line)]] | wt | 84.1 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.87× (z +11.2) | — |
| [[A-172 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 117 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 107 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 83.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME1]] | +0.63 | +0.66 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[UTP4]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TBRG4]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ADAT1]] | +0.56 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[NOP2]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[WDR77]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[BEND3]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PIGW]] | +0.54 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[DHRS11]] | +0.54 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PDSS1]] | +0.53 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[NSUN2]] | +0.53 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A10]] | +0.53 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPX4]] | -0.61 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[KLHL24]] | -0.60 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[AKAP9]] | -0.60 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[TCP11L2]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[UBXN1]] | -0.58 | -0.43 / -0.66 | both halves | 3e-05 | pathway: DNA Double Strand Break Response |
| [[GABARAP]] ⚠ | -0.57 | -0.50 / -0.57 | both halves | 1e-05 | pathway: Autophagy; ⚠ in the vector space only through flagged drug-doses |
| [[UBE2B]] | -0.56 | -0.46 / -0.60 | both halves | 3e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 929 |
| [[KIZ]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[RAB13]] | -0.55 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[GOLPH3L]] | -0.55 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[NUB1]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[UBN2]] | -0.54 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[WDR48]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises UBE2N's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises UBE2N's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction -0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.7, -47.1); signed map (-2.9, -47.4). **Vector** length 85.0, 23.1% of its response variance represented; |z| ≥ 3 in 1,257 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +6.0 | +5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +7.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.2 | +0.5 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.3 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.8 | +10.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 N |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:93,405,673-93,441,947 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UbcH-ben, UBC13, MGC8489 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, ALLOGRAFT_REJECTION |
| Reactome | 73 pathways, smallest: TRAF6 mediated IRF7 activation in TLR7/8 or 9 signaling; IRAK1 recruits IKK complex; IRAK1 recruits IKK complex upon TLR7/8 or 9 stimulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61088](https://www.uniprot.org/uniprotkb/P61088) (Ubiquitin-conjugating enzyme E2 N):

> The UBE2V1-UBE2N and UBE2V2-UBE2N heterodimers catalyze the synthesis of non-canonical 'Lys-63'-linked polyubiquitin chains. This type of polyubiquitination does not lead to protein degradation by the proteasome. Mediates transcriptional activation of target genes. Plays a role in the control of progress through the cell cycle and differentiation. Plays a role in the error-free DNA repair pathway and contributes to the survival of cells after DNA damage. Acts together with the E3 ligases, HLTF …

**Summary**, from NCBI Gene [7334](https://www.ncbi.nlm.nih.gov/gene/7334):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. Studies in mouse suggest that this protein plays a role in DNA postreplication repair. [provided by RefSeq, …

**Accessions** — [HGNC:12492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12492) · Entrez [7334](https://www.ncbi.nlm.nih.gov/gene/7334) · UniProt [P61088](https://www.uniprot.org/uniprotkb/P61088) · Ensembl [ENSG00000177889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177889)

## Data

Gene col 10875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10875); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10875]; `tensor/DDL_lfc|DDL_z.npy` [10875]; `embed/gene_vectors.npy` [10875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10875 or target_col == 10875). Every well: [[UBE2N — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2N.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

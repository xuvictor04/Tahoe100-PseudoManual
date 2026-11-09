---
symbol: "PISD"
type: "gene"
col: 14291
ensembl_id: "ENSG00000241878"
name: "phosphatidylserine decarboxylase"
location: "22q12.2"
module: 172
arm: "+"
pooled_cpm: 45.47
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# PISD

*phosphatidylserine decarboxylase* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +14.8, q 0e+00, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.781× (z -7.1, q 6e-10, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW48 0.126×, HCT15 0.256×, MIA PaCa-2 0.289×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.209×, NCI-H2347 0.388×, SK-MEL-2 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.432×, SW48 0.387×, HEC-1-A 0.576×; ⚠ cell-cycle shift, explains ~12% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHYKPL]] (+0.57, fdr 1e-05), [[PEX14]] (+0.54, fdr 3e-05), [[CCZ1P1]] (+0.53, fdr 1e-05); moves opposite to [[SCYL2]] (-0.51, fdr 5e-05), [[EDEM3]] (-0.48, fdr 2e-05), [[HNRNPLL]] (-0.48, fdr 2e-05).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +14.8 | 0e+00 | 33/47 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +14.1 | 9e-43 | 44/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +13.2 | 3e-37 | 43/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.14×** | +12.2 | 5e-32 | 41/49 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +12.1 | 2e-31 | 41/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +11.8 | 3e-30 | 37/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +9.4 | 5e-19 | 32/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.3 | 8e-19 | 34/47 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +9.2 | 3e-18 | 32/48 (A498, HCT15, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +9.1 | 5e-18 | 36/48 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +8.7 | 2e-16 | 41/48 (SW480, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +8.2 | 2e-14 | 33/48 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.2 | 3e-11 | 32/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +6.9 | 2e-10 | 27/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.39×** | +6.8 | 5e-10 | 29/48 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.50×** | +5.9 | 1e-07 | 29/48 (PANC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.4 | 2e-06 | 24/48 (C32, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14291.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW48 0.126×, HCT15 0.256×, MIA PaCa-2 0.289×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.209×, NCI-H2347 0.388×, SK-MEL-2 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.432×, SW48 0.387×, HEC-1-A 0.576×; ⚠ cell-cycle shift, explains ~12% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -7.1 | 6e-10 | 33/48 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.754×** | -5.8 | 2e-06 | 26/47 (NCI-H23, NCI-H2347, …) | two highest doses | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.790×** | -4.8 | 3e-04 | 22/48 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.788×** | -4.7 | 4e-04 | 19/39 (SW48, HCT15, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~18% of this change | **0.810×** | -4.3 | 0.002 | 23/46 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 0.842× | -3.5 | 0.043 | 7/48 (SW48, CHP-212, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.901× | -3.0 | 0.21 | 17/48 (RKO, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.0 | 26 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 50.4 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +17.8) | — |
| [[KATO III (line)]] | alt | 57.4 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 28.0 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +13.8) | — |
| [[SW480 (line)]] | alt | 33.8 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.39× (z +10.8) | — |
| [[A498 (line)]] | wt | 83.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +21.0) | [[Panobinostat (drug)]] 0.5 µM 0.412× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 43.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +16.9) | — |
| [[Hs 766T (line)]] | wt | 44.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.3) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.134× (z -8.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 67.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +16.1) | — |
| [[LS 180 (line)]] | wt | 51.3 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.51× (z +9.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -8.5) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SW48 (line)]] | wt | 69.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0974× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[COLO 205 (line)]] | alt | 45.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 39.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.90× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 43.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[SW 900 (line)]] | alt | 62.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.7) | — |
| [[A-172 (line)]] | wt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.3) | — |
| [[C32 (line)]] | wt | 42.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.09× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 50.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +15.8) | — |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.1) ⚠ cell-cycle shift, explains ~12% of this change |
| [[HS-578T (line)]] | alt | 53.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.4) | — |
| [[HT-29 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 53.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 67.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -11.4) ⚠ cell-cycle shift, explains ~12% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 87.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +8.8) | — |
| [[A-427 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHYKPL]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PEX14]] | +0.54 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[CCZ1P1]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ZNF493]] | +0.53 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[COMT]] | +0.53 | +0.47 / +0.61 | both halves | 2e-05 | same gene group |
| [[GPATCH3]] | +0.51 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[PEX10]] | +0.51 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[SLC25A17]] | +0.51 | +0.40 / +0.46 | both halves | 4e-05 | same gene group |
| [[SLC38A7]] | +0.51 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[TRUB2]] | +0.51 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[AP5Z1]] | +0.51 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[METAP1D]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCYL2]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[EDEM3]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[HNRNPLL]] | -0.48 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[RB1]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SYNJ1]] | -0.46 | -0.37 / -0.58 | both halves | 9e-05 | pathway: Phospholipid metabolism |
| [[ADAM10]] | -0.44 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[KMT5A]] | -0.43 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[SMAP2]] | -0.43 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[SRGAP2C]] | -0.42 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[MFSD2A]] | -0.42 | -0.33 / -0.47 | both halves | 1e-04 | pathway: Glycerophospholipid biosynthesis |
| [[TBC1D31]] | -0.42 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[STIM2]] | -0.42 | -0.36 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.4, 12.2); signed map (-8.3, -18.6). **Vector** length 81.2, 18.5% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.9 | +9.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.5 | +6.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | +4.8 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +6.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.0 | -2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.8 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.7 | -4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylserine decarboxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,618,491-31,662,221 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ858B16.2, PSDC |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Decarboxylases |
| Reactome | 4 pathways, smallest: Synthesis of PE; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UG56](https://www.uniprot.org/uniprotkb/Q9UG56) (Phosphatidylserine decarboxylase proenzyme, mitochondrial):

> Catalyzes the formation of phosphatidylethanolamine (PtdEtn) from phosphatidylserine (PtdSer). Plays a central role in phospholipid metabolism and in the interorganelle trafficking of phosphatidylserine. May be involved in lipid droplet biogenesis at the endoplasmic reticulum membrane (By similarity).

**Summary**, from NCBI Gene [23761](https://www.ncbi.nlm.nih.gov/gene/23761):

> The protein encoded by this gene catalyzes the conversion of phosphatidylserine to phosphatidylethanolamine in the inner mitochondrial membrane. The encoded protein is active in phospholipid metabolism and interorganelle trafficking of phosphatidylserine. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:8999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8999) · Entrez [23761](https://www.ncbi.nlm.nih.gov/gene/23761) · UniProt [Q9UG56](https://www.uniprot.org/uniprotkb/Q9UG56) · Ensembl [ENSG00000241878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241878)

## Data

Gene col 14291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14291); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14291]; `tensor/DDL_lfc|DDL_z.npy` [14291]; `embed/gene_vectors.npy` [14291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14291 or target_col == 14291). Every well: [[PISD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PISD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

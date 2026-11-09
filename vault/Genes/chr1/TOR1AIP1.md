---
symbol: "TOR1AIP1"
type: "gene"
col: 6717
ensembl_id: "ENSG00000143337"
name: "torsin 1A interacting protein 1"
location: "1q25.2"
module: 51
arm: "+"
pooled_cpm: 56.46
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# TOR1AIP1

*torsin 1A interacting protein 1* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +11.4, q 4e-27, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.497× (z -12.6, q 2e-33, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMO]] (+0.73, fdr 7e-06), [[COQ7]] (+0.71, fdr 1e-05), [[LYRM2]] (+0.68, fdr 1e-05); moves opposite to [[FOXK2]] (-0.61, fdr 1e-05), [[LRP5L]] (-0.60, fdr 1e-05), [[ATP7B]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +11.4 | 4e-27 | 36/48 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +9.1 | 3e-17 | 42/49 (SW480, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.9 | 1e-09 | 33/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.9 | 4e-07 | 31/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +5.6 | 2e-06 | 33/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.3 | 1e-05 | 26/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 2e-05 | 24/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.0 | 4e-05 | 27/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.65×** | +4.7 | 2e-04 | 28/49 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.088 | 13/49 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.1 | 0.090 | 18/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.13× | +3.1 | 0.095 | 14/48 (HEC-1-A, SNU-1, …) | top dose only | low cells (technical?) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.095 | 10/48 (J82, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.497×** | -12.6 | 2e-33 | 44/48 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.525×** | -11.6 | 2e-28 | 44/48 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.548×** | -10.8 | 7e-25 | 44/48 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.622×** | -8.5 | 2e-15 | 43/48 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.726×** | -8.1 | 5e-14 | 38/48 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.638×** | -8.0 | 8e-14 | 39/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.731×** | -7.9 | 2e-13 | 33/49 (A498, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.658×** | -7.2 | 3e-11 | 34/48 (NCI-H23, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -6.8 | 6e-10 | 34/49 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.554×** | -5.5 | 2e-06 | 31/49 (SHP-77, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.738×** | -5.4 | 3e-06 | 34/49 (CHP-212, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.788×** | -4.3 | 9e-04 | 29/48 (C32, CHP-212, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.745×** | -3.8 | 0.007 | 22/48 (H4, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.753×** | -3.6 | 0.012 | 19/48 (Hs 766T, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.824×** | -3.5 | 0.019 | 17/48 (LoVo, SW 900, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.763×** | -3.5 | 0.019 | 18/49 (MIA PaCa-2, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.044 | 11/48 (Hs 766T, SW48, …) | two highest doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.056 | 20/48 (SHP-77, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Drospirenone (drug)]] 0.5 µM |  | 0.845× | -3.0 | 0.069 | 11/48 (AN3 CA, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 112 | 0 | 7 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 60.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.2) | — |
| [[A498 (line)]] | wt | 74.5 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -12.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.405× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 88.8 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.319× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 62.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 91.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.407× (z -10.0) |
| [[SW480 (line)]] | alt | 49.1 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 7.28× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.498× (z -8.6) |
| [[SNU-423 (line)]] | alt | 62.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.243× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 87.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -9.4) |
| [[COLO 205 (line)]] | alt | 81.1 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.83× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.386× (z -8.5) |
| [[HOP62 (line)]] | alt | 55.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.396× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 62.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 59.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.444× (z -10.4) |
| [[RKO (line)]] | wt | 67.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[SNU-1 (line)]] | wt | 74.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 53.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.4) | — |
| [[A549 (line)]] | wt | 54.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 59.1 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0644× (z -10.4) |
| [[C32 (line)]] | wt | 54.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.6) | — |
| [[H4 (line)]] | wt | 51.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -8.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HT-29 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 45.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.4) | — |
| [[J82 (line)]] | alt | 43.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.6) | — |
| [[LoVo (line)]] | wt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -9.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H23 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -11.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 69.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -9.0) |
| [[SHP-77 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[A-427 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMO]] | +0.73 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[COQ7]] | +0.71 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[LYRM2]] | +0.68 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[EPC2]] | +0.67 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ZNF644]] | +0.67 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[RBM23]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.65 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[NUBP1]] | +0.65 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[UBQLN2]] | +0.63 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ELF1]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[HNRNPH2]] | +0.62 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[DDX6]] | +0.62 | +0.43 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXK2]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[LRP5L]] | -0.60 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ATP7B]] | -0.60 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[LPCAT4]] | -0.59 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[DNAJC5]] | -0.59 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[PDXP]] | -0.59 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[STK32C]] | -0.58 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[GNRH1]] | -0.58 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PIGF]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[PALS2]] | -0.57 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TRABD]] | -0.56 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[RALGPS1]] | -0.56 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.2, 11.1); signed map (11.8, -29.9). **Vector** length 95.8, 24.9% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +11.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +4.1 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +0.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | torsin 1A interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:179,882,042-179,920,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LAP1B, FLJ13142, LAP1, LAP1C |
| Reactome | 5 pathways, smallest: RHOF GTPase cycle; RHOD GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JTV8](https://www.uniprot.org/uniprotkb/Q5JTV8) (Torsin-1A-interacting protein 1):

> Required for nuclear membrane integrity. Induces TOR1A and TOR1B ATPase activity and is required for their location on the nuclear membrane. Binds to A- and B-type lamins. Possible role in membrane attachment and assembly of the nuclear lamina.

**Summary**, from NCBI Gene [26092](https://www.ncbi.nlm.nih.gov/gene/26092):

> This gene encodes a type 2 integral membrane protein that binds A- and B-type lamins. The encoded protein localizes to the inner nuclear membrane and may be involved in maintaining the attachment of the nuclear membrane to the nuclear lamina during cell division. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:29456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29456) · Entrez [26092](https://www.ncbi.nlm.nih.gov/gene/26092) · UniProt [Q5JTV8](https://www.uniprot.org/uniprotkb/Q5JTV8) · Ensembl [ENSG00000143337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143337)

## Data

Gene col 6717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6717); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6717]; `tensor/DDL_lfc|DDL_z.npy` [6717]; `embed/gene_vectors.npy` [6717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6717 or target_col == 6717). Every well: [[TOR1AIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOR1AIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

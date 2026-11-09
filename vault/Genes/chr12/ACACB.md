---
symbol: "ACACB"
type: "gene"
col: 1155
ensembl_id: "ENSG00000076555"
name: "acetyl-CoA carboxylase beta"
location: "12q24.11"
module: 45
arm: "+"
pooled_cpm: 18.96
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 41
n_dd_up_clean: 28
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ACACB

*acetyl-CoA carboxylase beta* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.27× (z +15.5, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.266× (z -17.2, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MNS1]] (+0.66, fdr 2e-05), [[SUFU]] (+0.66, fdr 2e-05), [[ALAD]] (+0.65, fdr 1e-05); moves opposite to [[LTO1]] (-0.63, fdr 5e-05), [[ZNF778]] (-0.60, fdr 9e-05), [[GCNT4]] (-0.59, fdr 3e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.27×** | +15.5 | 0e+00 | 41/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.04×** | +14.5 | 1e-45 | 41/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +11.1 | 3e-26 | 37/47 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +9.8 | 1e-20 | 36/46 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.12×** | +9.8 | 1e-20 | 35/47 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +6.3 | 3e-08 | 31/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +6.2 | 4e-08 | 29/47 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +6.1 | 8e-08 | 26/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.51×** | +4.9 | 5e-05 | 22/47 (C-33 A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.28×** | +4.6 | 2e-04 | 17/47 (J82, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +4.5 | 3e-04 | 21/47 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 19/47 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.003 | 16/47 (A-172, KATO III, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.38×** | +4.0 | 0.003 | 12/46 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.75×** | +3.8 | 0.005 | 9/47 (A549, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.005 | 17/46 (SW480, C32, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1155.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.266×** | -17.2 | 0e+00 | 44/47 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.346×** | -13.8 | 6e-41 | 40/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.346×** | -13.8 | 6e-41 | 41/46 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.431×** | -10.9 | 1e-25 | 36/46 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.455×** | -10.2 | 2e-22 | 35/47 (AN3 CA, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.483×** | -9.4 | 3e-19 | 34/46 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.471×** | -9.4 | 4e-19 | 27/43 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.605×** | -9.2 | 2e-18 | 26/45 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.494×** | -9.2 | 4e-18 | 29/46 (RPMI-7951, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.481×** | -9.1 | 4e-18 | 30/47 (COLO 205, A-172, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.506×** | -8.8 | 5e-17 | 34/45 (A549, COLO 205, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.510×** | -8.7 | 1e-16 | 30/47 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.538×** | -7.6 | 1e-12 | 28/47 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.660×** | -7.6 | 1e-12 | 33/47 (HT-29, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.567×** | -7.4 | 7e-12 | 32/46 (RKO, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.604×** | -6.3 | 1e-08 | 29/46 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -6.2 | 2e-08 | 28/45 (COLO 205, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.443×** | -5.5 | 9e-07 | 24/47 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.654×** | -5.5 | 1e-06 | 29/46 (NCI-H23, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.511×** | -4.6 | 1e-04 | 18/47 (Hs 766T, H4, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.9 | 2 | 12 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 4.49× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0510× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -15.3) |
| [[A549 (line)]] | wt | 49.7 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -16.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0909× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 48.1 | 1 (1 ⚠) | 10 (5 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.59× (z +10.6) ⚠ position not correctable | [[Niclosamide (olamine) (drug)]] 5 µM 0.0503× (z -19.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0988× (z -15.8) |
| [[SW 900 (line)]] | alt | 37.5 | 0 | 11 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.163× (z -11.5) |
| [[A-427 (line)]] | wt | 53.7 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -11.6) |
| [[COLO 205 (line)]] | alt | 65.5 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -22.3) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 48.1 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0676× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -11.1) |
| [[SW480 (line)]] | alt | 20.3 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.55× (z +9.1) | [[Digitoxin (drug)]] 0.5 µM 0.138× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 15.1 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.77× (z +10.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -12.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.243× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 5 (3 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0744× (z -11.8) ⚠ toxic; unreliable plate only · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0903× (z -10.1) |
| [[LoVo (line)]] | wt | 10.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 7.04× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.214× (z -8.9) |
| [[A498 (line)]] | wt | 18.0 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -8.7) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HCT15 (line)]] | alt | 32.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0881× (z -12.5) |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0779× (z -10.3) |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -10.4) |
| [[KATO III (line)]] | alt | 13.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -11.0) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.228× (z -8.7) |
| [[SNU-423 (line)]] | alt | 8.82 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.148× (z -8.5) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0568× (z -15.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 10.8 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0780× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 17.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -10.5) |
| [[HT-29 (line)]] | alt | 9.99 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.129× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 8.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0808× (z -12.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 9.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0424× (z -15.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 7.57 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0725× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.101× (z -10.6) |
| [[SW1417 (line)]] | alt | 19.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MNS1]] | +0.66 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SUFU]] | +0.66 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[ALAD]] | +0.65 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[TMEM14A]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[DOC2A]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[EHMT2]] | +0.63 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[RHOXF1]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[FAM13B]] | +0.62 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[GUSBP18]] | +0.62 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[HMGN3]] | +0.61 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ALDH7A1]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ADAM22]] | +0.60 | +0.50 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTO1]] | -0.63 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ZNF778]] | -0.60 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[GCNT4]] | -0.59 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[DESI1]] | -0.59 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SPON1-AS1]] | -0.58 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[AOC2]] | -0.56 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[UEVLD]] | -0.56 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[NUP50-DT]] | -0.54 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[FBXO30]] | -0.54 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[RNF217-AS1]] | -0.54 | -0.21 / -0.57 | both halves | 7e-04 |  |
| [[CPEB2-DT]] | -0.53 | -0.17 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[CSTF3]] | -0.53 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[PTPRG]] | -0.53 | -0.36 / -0.44 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.6, -7.3); signed map (-28.1, -8.0). **Vector** length 78.6, 19.3% of its response variance represented; |z| ≥ 3 in 1,497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +11.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +15.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +14.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +9.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +6.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -9.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.4 | -8.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -7.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -7.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | acetyl-CoA carboxylase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,116,587-109,268,226 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HACC275, ACC2, ACCB, ACC-beta, ACCbeta, ACACbeta |
| Gene groups (HGNC) | Acetyl-CoA carboxylase family; ATP-grasp fold containing |
| Reactome | 11 pathways, smallest: ChREBP activates metabolic gene expression; Biotin transport and metabolism; Carnitine shuttle |
| Matched by | ensembl_id |

**Function**, from UniProt [O00763](https://www.uniprot.org/uniprotkb/O00763) (Acetyl-CoA carboxylase 2):

> Mitochondrial enzyme that catalyzes the carboxylation of acetyl-CoA to malonyl-CoA and plays a central role in fatty acid metabolism. Catalyzes a 2 steps reaction starting with the ATP-dependent carboxylation of the biotin carried by the biotin carboxyl carrier (BCC) domain followed by the transfer of the carboxyl group from carboxylated biotin to acetyl-CoA. Through the production of malonyl-CoA that allosterically inhibits carnitine palmitoyltransferase 1 at the mitochondria, negatively …

**Summary**, from NCBI Gene [32](https://www.ncbi.nlm.nih.gov/gene/32):

> Acetyl-CoA carboxylase (ACC) is a complex multifunctional enzyme system. ACC is a biotin-containing enzyme which catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the rate-limiting step in fatty acid synthesis. ACC-beta is thought to control fatty acid oxidation by means of the ability of malonyl-CoA to inhibit carnitine-palmitoyl-CoA transferase I, the rate-limiting step in fatty acid uptake and oxidation by mitochondria. ACC-beta may be involved in the regulation of fatty acid …

**Accessions** — [HGNC:85](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:85) · Entrez [32](https://www.ncbi.nlm.nih.gov/gene/32) · UniProt [O00763](https://www.uniprot.org/uniprotkb/O00763) · Ensembl [ENSG00000076555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076555)

## Data

Gene col 1155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1155); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1155]; `tensor/DDL_lfc|DDL_z.npy` [1155]; `embed/gene_vectors.npy` [1155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1155 or target_col == 1155). Every well: [[ACACB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACACB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

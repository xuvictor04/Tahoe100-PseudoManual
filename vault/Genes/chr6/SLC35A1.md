---
symbol: "SLC35A1"
type: "gene"
col: 8945
ensembl_id: "ENSG00000164414"
name: "solute carrier family 35 member A1"
location: "6q15"
module: 65
arm: "+"
pooled_cpm: 25.95
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 25
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# SLC35A1

*solute carrier family 35 member A1* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.86× (z +12.1, q 4e-31, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.599× (z -9.9, q 1e-20, down in 28 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.385× (z -9.7, q 8e-20, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC4]] (+0.68, fdr 7e-06), [[ATG4C]] (+0.64, fdr 1e-05), [[PCTP]] (+0.64, fdr 1e-05); moves opposite to [[ITPR2-AS1]] (-0.66, fdr 2e-05), [[SEMA6A-AS1]] (-0.65, fdr 2e-05), [[PTOV1-AS1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[APPAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +12.1 | 4e-31 | 40/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +10.6 | 9e-24 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +9.3 | 2e-18 | 35/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +8.4 | 6e-15 | 30/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +7.3 | 4e-11 | 32/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.1 | 2e-10 | 26/43 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +6.7 | 1e-09 | 24/48 (COLO 205, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +5.3 | 9e-06 | 19/47 (C32, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 18/48 (HOP62, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.6 | 2e-04 | 16/48 (SW480, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.006 | 8/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.052 | 6/47 (KATO III, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.17× | +3.1 | 0.088 | 9/47 (C-33 A, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.599×** | -9.9 | 1e-20 | 28/42 (A-427, HCT15, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -9.7 | 8e-20 | 32/48 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -9.6 | 2e-19 | 35/47 (SNU-423, SHP-77, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -9.5 | 3e-19 | 34/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -9.5 | 3e-19 | 33/47 (HOP62, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.615×** | -9.4 | 4e-19 | 32/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -9.4 | 6e-19 | 32/46 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.598×** | -9.2 | 2e-18 | 24/38 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -8.6 | 5e-16 | 19/36 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.766×** | -7.3 | 2e-11 | 27/47 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -7.2 | 2e-11 | 28/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -7.0 | 1e-10 | 8/48 (SNU-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.717×** | -6.4 | 6e-09 | 28/47 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.702×** | -6.2 | 2e-08 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.752×** | -5.5 | 1e-06 | 17/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.780×** | -4.4 | 4e-04 | 23/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.826×** | -3.7 | 0.007 | 10/47 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.017 | 16/47 (C-33 A, SNU-423, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.838× | -3.4 | 0.017 | 12/48 (SW 1088, PANC-1, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.785×** | -3.3 | 0.020 | 11/47 (NCI-H661, NCI-H1792, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.836× | -3.3 | 0.021 | 14/48 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.854× | -3.0 | 0.053 | 6/48 (SW48, NCI-H2030, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.750×** | -2.9 | 0.074 | 10/44 (SNU-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.860× | -2.9 | 0.074 | 4/48 (NCI-H460, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.2 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -12.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.318× (z -10.6) |
| [[LS 180 (line)]] | wt | 55.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -13.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 39.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 14.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -11.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 29.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -16.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 31.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -14.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 39.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.375× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 26.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.1) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A549 (line)]] | wt | 19.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.1) ⚠ cell-cycle shift, explains ~78% of this change |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.317× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0700× (z -8.7) |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0546× (z -19.3) ⚠ toxic |
| [[A-427 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -14.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.0) ⚠ cell-cycle shift, explains ~78% of this change |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -10.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.125× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~66% of this change |
| [[LoVo (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0819× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC4]] | +0.68 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PCTP]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PRKRA]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[DENND6A]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[KLHL8]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[CMC1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ACTR10]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[ARNT]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MINDY3]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[NBPF3]] | +0.58 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPR2-AS1]] | -0.66 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[SEMA6A-AS1]] | -0.65 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[PTOV1-AS1]] | -0.63 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[DPYS]] | -0.63 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[GARIN1B]] | -0.62 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[MC1R]] | -0.62 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | -0.62 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[LINC00907]] | -0.61 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[MFSD1]] | -0.60 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[NR2F1-AS1]] | -0.60 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SLC7A9]] | -0.59 | -0.54 / -0.46 | both halves | 3e-05 | pathway: Disorders of transmembrane transporters |
| [[RNF32-AS1]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APPAT]] | B | APPAT activity raises SLC35A1's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.29× lower at baseline in the lines without APPAT | 0.086 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SLC35A1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SLC35A1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GARIN1B]] | C | GARIN1B activity weakens SLC35A1's drug response | lines that do not express GARIN1B (4) vs lines expressing it (44) | the lines without GARIN1B respond 1.88× as strongly (z diff -2.24); strongest at Digitoxin 5 µM: 0.32x vs 0.61x (z diff -5.6) | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[GARIN1B]] | C | GARIN1B activity lowers SLC35A1's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 1.73× higher at baseline in the lines without GARIN1B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (12.6, 8.0); signed map (-32.9, -8.2). **Vector** length 77.7, 15.4% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.2 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +6.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +4.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.6 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -4.7 | -7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -9.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:87,470,623-87,512,336 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CMPST, hCST, CMP-Sia-Tr |
| Gene groups (HGNC) | Solute carrier family 35 |
| Reactome | 13 pathways, smallest: Transport of nucleotide sugars; Matriglycan biosynthesis on DAG1; DAG1 glycosylations |
| Matched by | ensembl_id |

**Function**, from UniProt [P78382](https://www.uniprot.org/uniprotkb/P78382) (CMP-sialic acid transporter):

> Transports CMP-sialic acid from the cytosol into the Golgi apparatus, functioning as an antiporter that exchanges CMP-sialic acid for CMP. Binds both CMP-sialic acid and free CMP, but has higher affinity for free CMP (By similarity). Also able to exchange CMP-sialic acid for AMP and UMP. Also mediates the transport of CDP-ribitol (By similarity).

**Summary**, from NCBI Gene [10559](https://www.ncbi.nlm.nih.gov/gene/10559):

> The protein encoded by this gene is found in the membrane of the Golgi apparatus, where it transports nucleotide sugars into the Golgi. One such nucleotide sugar is CMP-sialic acid, which is imported into the Golgi by the encoded protein and subsequently glycosylated. Defects in this gene are a cause of congenital disorder of glycosylation type 2F (CDG2F). Two transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:11021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11021) · Entrez [10559](https://www.ncbi.nlm.nih.gov/gene/10559) · UniProt [P78382](https://www.uniprot.org/uniprotkb/P78382) · Ensembl [ENSG00000164414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164414)

## Data

Gene col 8945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8945); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8945]; `tensor/DDL_lfc|DDL_z.npy` [8945]; `embed/gene_vectors.npy` [8945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8945 or target_col == 8945). Every well: [[SLC35A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "GALNT14"
type: "gene"
col: 8130
ensembl_id: "ENSG00000158089"
name: "polypeptide N-acetylgalactosaminyltransferase 14"
location: "2p23.1"
module: 18
arm: "+"
pooled_cpm: 24.2
n_lines_expressing: 26
n_dd_up: 32
n_dd_down: 14
n_dd_up_clean: 17
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 19
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GALNT14

*polypeptide N-acetylgalactosaminyltransferase 14* — 2p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.47× (z +21.6, q 0e+00, up in 9 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.651× (z -7.3, q 2e-10, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY3]] (+0.66, fdr 7e-06), [[SMAGP]] (+0.65, fdr 1e-05), [[UCK2]] (+0.64, fdr 1e-05); moves opposite to [[GABARAP]] (-0.62, fdr 1e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[MMUT]] (-0.58, fdr 1e-05), [[SENP2]] (-0.58, fdr 1e-05), [[ETFRF1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 19 go from it, the strongest it → [[DLX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +21.6 | 0e+00 | 9/22 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.04×** | +12.0 | 6e-31 | 4/19 (CFPAC-1, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +11.7 | 4e-29 | 5/18 (NCI-H1573, SW 900, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.02×** | +11.4 | 4e-28 | 4/16 (NCI-H1573, SW 900, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +10.0 | 1e-21 | 14/24 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +9.2 | 3e-18 | 18/24 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +8.0 | 7e-14 | 6/21 (NCI-H1792, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.44×** | +7.9 | 3e-13 | 15/19 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +6.9 | 3e-10 | 18/24 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +6.4 | 8e-09 | 7/23 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +6.3 | 1e-08 | 13/23 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +6.0 | 1e-07 | 12/24 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.40×** | +5.4 | 3e-06 | 3/23 (NCI-H1792, BT-474, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.2 | 7e-06 | 6/24 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.80×** | +5.2 | 9e-06 | 11/22 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.76×** | +5.0 | 2e-05 | 11/22 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 7e-05 | 4/24 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 6e-04 | 7/23 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.003 | 5/20 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.003 | 3/23 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.004 | 8/23 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.009 | 9/23 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.651×** | -7.3 | 2e-10 | 14/24 (HEC-1-A, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.766×** | -6.4 | 4e-08 | 7/24 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.706×** | -5.9 | 7e-07 | 13/23 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.701×** | -5.8 | 1e-06 | 11/24 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.735×** | -5.2 | 2e-05 | 13/24 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.755×** | -4.8 | 2e-04 | 3/24 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.765×** | -4.6 | 4e-04 | 14/24 (HEC-1-A, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.749×** | -4.5 | 4e-04 | 3/24 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.764×** | -4.4 | 7e-04 | 11/24 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.791×** | -4.2 | 0.001 | 10/24 (A-427, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.838× | -3.6 | 0.014 | 12/23 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.670×** | -3.5 | 0.019 | 8/23 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.808×** | -3.5 | 0.021 | 9/23 (NCI-H2030, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.869× | -3.4 | 0.028 | 3/24 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.693×** | -3.2 | 0.045 | 10/23 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.828×** | -3.1 | 0.067 | 7/23 (NCI-H23, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.4 | 3 (1 ⚠) | 7 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.19× (z +14.1) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -22.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -18.7) |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -21.3) |
| [[NCI-H2030 (line)]] | alt | 73.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -19.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -12.0) |
| [[A-427 (line)]] | wt | 97.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -32.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -14.4) |
| [[A549 (line)]] | wt | 69.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.65× (z +8.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -16.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.00978× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 45.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 70.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -19.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.300× (z -8.7) |
| [[A498 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0804× (z -25.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HT-29 (line)]] | alt | 102 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 30.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.36× (z +8.9) | — |
| [[A-172 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY3]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SMAGP]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[UCK2]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[MEGF11]] | +0.61 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PCOLCE2]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[HS6ST2]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[CDIN1]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[BEND3]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[KANK1]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[ABCC4]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[NME1]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LRP8]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAP]] ⚠ | -0.62 | -0.55 / -0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MMUT]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[SENP2]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ETFRF1]] | -0.57 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ALDH6A1]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[WBP1]] | -0.57 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[DNAL4]] | -0.56 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[PLAG1]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[OGA]] | -0.54 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[DDAH2]] | -0.53 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[BBOF1]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[IK]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[TRIM23]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GALNT14's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises GALNT14's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CASC19]] | B | CASC19 activity raises GALNT14's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without CASC19 | 0.083 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[ZYG11A]] | C | ZYG11A activity raises GALNT14's level | lines that do not express ZYG11A (29) vs lines expressing it (21) | 4.07× lower at baseline in the lines without ZYG11A | 0.029 | ⚠ within organs, on part of the lines; also absent: ANOS1, LGSN, DAW1; co-absent with the target |
| [[KIAA1549]] | C | KIAA1549 activity lowers GALNT14's level | lines that do not express KIAA1549 (4) vs lines expressing it (46) | 2.23× higher at baseline in the lines without KIAA1549 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HHAT, WHRN, GNAL; maybe low, not absent; its own permutation p |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX1]] | B | GALNT14 activity lowers DLX1's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.95× higher at baseline in the lines without GALNT14 | 0.021 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[CAPN14]] | B | GALNT14 activity raises CAPN14's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without GALNT14 | 0.030 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[ANKRD13B]] | B | GALNT14 activity lowers ANKRD13B's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.33× higher at baseline in the lines without GALNT14 | 0.035 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[LINP1]] | B | GALNT14 activity raises LINP1's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.68× lower at baseline in the lines without GALNT14 | 0.040 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[GBX2-AS1]] | B | GALNT14 activity lowers GBX2-AS1's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.54× higher at baseline in the lines without GALNT14 | 0.045 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[TMEM201]] | B | GALNT14 activity lowers TMEM201's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.44× higher at baseline in the lines without GALNT14 | 0.055 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[MGAT5B]] | B | GALNT14 activity lowers MGAT5B's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.41× higher at baseline in the lines without GALNT14 | 0.055 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[CHD2]] | B | GALNT14 activity raises CHD2's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.23× lower at baseline in the lines without GALNT14 | 0.065 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[PPP1R7]] | B | GALNT14 activity raises PPP1R7's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.13× lower at baseline in the lines without GALNT14 | 0.068 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| cells under [[Ritonavir (drug)]] 0.5 µM | B | GALNT14 activity raises the cells' numbers under Ritonavir 0.5 µM (protects the cells) | lines that do not express GALNT14 (24) vs lines expressing it (24) | the lines without GALNT14: 0.90× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[TNFRSF10A]] | B | GALNT14 activity raises TNFRSF10A's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 2.10× lower at baseline in the lines without GALNT14 | 0.070 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[TYRO3]] | B | GALNT14 activity lowers TYRO3's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.30× higher at baseline in the lines without GALNT14 | 0.074 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (21.4, -24.1); signed map (-17.6, 46.1). **Vector** length 73.8, 19.1% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +21.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.1 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +6.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +6.0 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.7 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.1 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.1 — chr2:30,910,467-31,155,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GalNac-T10, FLJ12691, GalNac-T14 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FL9](https://www.uniprot.org/uniprotkb/Q96FL9) (Polypeptide N-acetylgalactosaminyltransferase 14):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. Displays activity toward mucin-derived peptide substrates such as Muc2, Muc5AC, Muc7, and Muc13 (-58). May be involved in O-glycosylation in kidney.

**Summary**, from NCBI Gene [79623](https://www.ncbi.nlm.nih.gov/gene/79623):

> This gene encodes a Golgi protein which is a member of the polypeptide N-acetylgalactosaminyltransferase (ppGalNAc-Ts) protein family. These enzymes catalyze the transfer of N-acetyl-D-galactosamine (GalNAc) to the hydroxyl groups on serines and threonines in target peptides. The encoded protein has been shown to transfer GalNAc to large proteins like mucins. Alterations in this gene may play a role in cancer progression and response to chemotherapy. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:22946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22946) · Entrez [79623](https://www.ncbi.nlm.nih.gov/gene/79623) · UniProt [Q96FL9](https://www.uniprot.org/uniprotkb/Q96FL9) · Ensembl [ENSG00000158089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158089)

## Data

Gene col 8130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8130); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8130]; `tensor/DDL_lfc|DDL_z.npy` [8130]; `embed/gene_vectors.npy` [8130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8130 or target_col == 8130). Every well: [[GALNT14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

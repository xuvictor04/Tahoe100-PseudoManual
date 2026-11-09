---
symbol: "TMEM154"
type: "gene"
col: 9892
ensembl_id: "ENSG00000170006"
name: "transmembrane protein 154"
location: "4q31.3"
module: 34
arm: "+"
pooled_cpm: 9.97
n_lines_expressing: 24
n_dd_up: 39
n_dd_down: 13
n_dd_up_clean: 26
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 26
direction_downstream: 25
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TMEM154

*transmembrane protein 154* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.93× (z +10.9, q 6e-25, up in 6 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.95× (z +9.6, q 1e-19, up in 17 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.489× (z -10.3, q 3e-22, down in 21 of 22 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.445× (z -8.3, q 4e-14, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2IP7]] (+0.61, fdr 1e-05), [[CSF2RA]] (+0.55, fdr 3e-05), [[LINP1]] (+0.54, fdr 2e-05); moves opposite to [[SAMD11]] (-0.47, fdr 1e-04), [[YY1]] (-0.42, fdr 6e-05), [[NFIX]] (-0.41, fdr 7e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[SDCBP2]] → it (grade B ⚠); 25 go from it, the strongest it → [[SCAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +10.9 | 6e-25 | 6/18 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +10.4 | 6e-23 | 7/10 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.95×** | +9.6 | 1e-19 | 17/22 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +8.9 | 8e-17 | 3/13 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.67×** | +7.4 | 2e-11 | 17/22 (HOP62, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +6.9 | 6e-10 | 14/21 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.7 | 2e-09 | 11/19 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.90×** | +6.5 | 6e-09 | 15/21 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.91×** | +6.2 | 3e-08 | 12/22 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.50×** | +5.8 | 4e-07 | 15/23 (HOP62, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +5.1 | 2e-05 | 11/21 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.59×** | +5.0 | 3e-05 | 7/15 (A498, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.42×** | +5.0 | 3e-05 | 11/22 (A498, NCI-H460, …) | rises with dose |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.4 | 4e-04 | 8/21 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.54×** | +4.3 | 5e-04 | 10/21 (A498, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.3 | 5e-04 | 3/21 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.3 | 6e-04 | 4/21 (A-172, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.57×** | +4.2 | 9e-04 | 6/20 (Panc 03.27, J82, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 9e-04 | 11/21 (A498, Panc 03.27, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.002 | 9/21 (A-172, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.003 | 12/21 (A498, RPMI-7951, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.003 | 5/20 (NCI-H1573, A-172, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9892.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.489×** | -10.3 | 3e-22 | 21/22 (NCI-H460, CFPAC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.445×** | -8.3 | 4e-14 | 17/21 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.454×** | -7.8 | 2e-12 | 21/22 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -5.0 | 8e-05 | 9/21 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.631×** | -4.7 | 3e-04 | 11/22 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.635×** | -4.6 | 3e-04 | 14/22 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.660×** | -4.6 | 3e-04 | 10/22 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.709×** | -4.1 | 0.002 | 12/22 (NCI-H460, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.760×** | -4.0 | 0.005 | 10/22 (NCI-H460, KATO III, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.689×** | -3.5 | 0.023 | 7/21 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.519×** | -3.5 | 0.026 | 10/22 (CFPAC-1, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.726×** | -3.3 | 0.048 | 10/21 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.563×** | -3.1 | 0.099 | 4/22 (KATO III, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.5 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0341× (z -32.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0320× (z -23.1) |
| [[KATO III (line)]] | alt | 19.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0189× (z -17.2) |
| [[COLO 205 (line)]] | alt | 51.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0926× (z -18.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0774× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 80.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -25.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0656× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0743× (z -11.6) |
| [[A-172 (line)]] | wt | 32.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 27.1 | 1 | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.77× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -11.0) |
| [[HOP62 (line)]] | alt | 9.33 | 1 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 4.22× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0942× (z -16.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -8.7) |
| [[J82 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 5.50 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 6.37 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 4.09 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0831× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IP7]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[CSF2RA]] | +0.55 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[LINP1]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PLEK2]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[THBD]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[PRSS3]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SH2D2A]] | +0.50 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[LINC01322]] | +0.50 | +0.43 / +0.46 | both halves | 4e-05 |  |
| [[CLDN10-AS1]] | +0.49 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[SH3TC2]] | +0.48 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[SLC46A3]] | +0.48 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[SERPIND1]] | +0.48 | +0.43 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD11]] | -0.47 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[YY1]] | -0.42 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[NFIX]] | -0.41 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[TNS3]] | -0.41 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[BBOF1]] | -0.40 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[UBR5]] | -0.40 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[PCM1]] | -0.39 | -0.41 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 11, C 15. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDCBP2]] | B | SDCBP2 activity raises TMEM154's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.14× lower at baseline in the lines without SDCBP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[GTF2IP7]] | B | GTF2IP7 activity raises TMEM154's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.70× lower at baseline in the lines without GTF2IP7 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[PLAC4]] | B | PLAC4 activity raises TMEM154's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.80× lower at baseline in the lines without PLAC4 | 0.048 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[LYPD3]] | B | LYPD3 activity raises TMEM154's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without LYPD3 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[ST3GAL1]] | B | ST3GAL1 activity raises TMEM154's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.71× lower at baseline in the lines without ST3GAL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[SCAT1]] | B | SCAT1 activity raises TMEM154's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.74× lower at baseline in the lines without SCAT1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[PLEK2]] | B | PLEK2 activity raises TMEM154's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without PLEK2 | 0.066 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[TNS3]] | B | TNS3 activity raises TMEM154's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without TNS3 | 0.069 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[IFNLR1]] | B | IFNLR1 activity raises TMEM154's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 1.37× lower at baseline in the lines without IFNLR1 | 0.071 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[LINC02320]] | B | LINC02320 activity raises TMEM154's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without LINC02320 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[SERPIND1]] | B | SERPIND1 activity raises TMEM154's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without SERPIND1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[CREG2]] | C | CREG2 activity raises TMEM154's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 2.96× lower at baseline in the lines without CREG2 | 0.004 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 15, C 10. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCAT1]] | B | TMEM154 activity raises SCAT1's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without TMEM154 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[MFSD9]] | B | TMEM154 activity raises MFSD9's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.19× lower at baseline in the lines without TMEM154 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[SAMD11]] | B | TMEM154 activity lowers SAMD11's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.66× higher at baseline in the lines without TMEM154 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[SLC35B4]] | B | TMEM154 activity lowers SLC35B4's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.49× higher at baseline in the lines without TMEM154 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[IFNLR1]] | B | TMEM154 activity raises IFNLR1's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.69× lower at baseline in the lines without TMEM154 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[CDCP1]] | B | TMEM154 activity raises CDCP1's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 2.23× lower at baseline in the lines without TMEM154 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[USB1]] | B | TMEM154 activity lowers USB1's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.21× higher at baseline in the lines without TMEM154 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[SDCBP2]] | B | TMEM154 activity raises SDCBP2's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 2.45× lower at baseline in the lines without TMEM154 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[LYPD3]] | B | TMEM154 activity raises LYPD3's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without TMEM154 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[ZG16B]] | B | TMEM154 activity raises ZG16B's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.39× lower at baseline in the lines without TMEM154 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[OCIAD2]] | B | TMEM154 activity raises OCIAD2's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without TMEM154 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[PRSS3]] | B | TMEM154 activity raises PRSS3's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 2.22× lower at baseline in the lines without TMEM154 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.1, 15.2); signed map (17.1, 55.6). **Vector** length 77.8, 23.1% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.8 | +7.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.6 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 154 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:152,618,628-152,680,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32028 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P9G4](https://www.uniprot.org/uniprotkb/Q6P9G4) (Galvanin):

> Electric-field sensor that links electrical cues to directed cell migration by transducing spatial information about the extracellular electric field to the intracellular migratory machinery. Required for electric-field-guided migration of rapidly moving immune and epithelial cells.

**Summary**, from NCBI Gene [201799](https://www.ncbi.nlm.nih.gov/gene/201799):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26489) · Entrez [201799](https://www.ncbi.nlm.nih.gov/gene/201799) · UniProt [Q6P9G4](https://www.uniprot.org/uniprotkb/Q6P9G4) · Ensembl [ENSG00000170006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170006)

## Data

Gene col 9892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9892); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9892]; `tensor/DDL_lfc|DDL_z.npy` [9892]; `embed/gene_vectors.npy` [9892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9892 or target_col == 9892). Every well: [[TMEM154 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM154.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

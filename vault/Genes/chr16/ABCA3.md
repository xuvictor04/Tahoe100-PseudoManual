---
symbol: "ABCA3"
type: "gene"
col: 9566
ensembl_id: "ENSG00000167972"
name: "ATP binding cassette subfamily A member 3"
location: "16p13.3"
module: 36
arm: "+"
pooled_cpm: 15.68
n_lines_expressing: 41
n_dd_up: 22
n_dd_down: 28
n_dd_up_clean: 18
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 6
direction_downstream: 26
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ABCA3

*ATP binding cassette subfamily A member 3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.77× (z +8.1, q 4e-13, up in 20 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.312× (z -16.3, q 0e+00, down in 35 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACS2]] (+0.67, fdr 1e-05), [[DOP1B]] (+0.57, fdr 9e-05), [[RASA2]] (+0.57, fdr 1e-04); moves opposite to [[BTN3A3]] (-0.55, fdr 4e-05), [[KLHL3]] (-0.53, fdr 1e-04), [[DNAJB4]] (-0.50, fdr 6e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 26 go from it, the strongest it → [[HMOX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +8.1 | 4e-13 | 20/38 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +7.3 | 6e-11 | 19/38 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +7.2 | 1e-10 | 22/38 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.1 | 2e-10 | 22/39 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +6.3 | 3e-08 | 18/36 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +6.0 | 2e-07 | 21/38 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.9 | 2e-07 | 11/19 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.6 | 1e-06 | 17/37 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.9 | 8e-05 | 11/32 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +4.8 | 9e-05 | 15/38 (LS 180, A549, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +4.3 | 0.001 | 10/39 (KATO III, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 13/38 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.006 | 13/38 (A549, PANC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.007 | 9/34 (SW48, CFPAC-1, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.009 | 8/38 (NCI-H2030, AN3 CA, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.6 | 0.010 | 6/39 (NCI-H2030, A498, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.021 | 7/38 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.312×** | -16.3 | 0e+00 | 35/38 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.440×** | -16.3 | 0e+00 | 29/36 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.384×** | -13.4 | 9e-39 | 32/36 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.410×** | -12.5 | 1e-33 | 30/38 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.518×** | -9.2 | 4e-18 | 28/38 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.523×** | -9.1 | 1e-17 | 25/38 (HEC-1-A, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.517×** | -8.9 | 6e-17 | 26/37 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.545×** | -8.5 | 1e-15 | 25/38 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.572×** | -7.8 | 4e-13 | 21/36 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.579×** | -7.2 | 3e-11 | 28/37 (Hs 766T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.626×** | -6.5 | 3e-09 | 23/38 (PANC-1, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.686×** | -5.3 | 7e-06 | 18/38 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -4.9 | 4e-05 | 19/35 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.515×** | -4.8 | 5e-05 | 20/38 (A549, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -4.6 | 1e-04 | 20/38 (A-172, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.722×** | -4.5 | 2e-04 | 19/38 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.755×** | -3.9 | 0.003 | 13/37 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.621×** | -3.5 | 0.015 | 8/35 (SNU-1, BT-474, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.7 | 0 | 11 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0412× (z -32.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -21.2) |
| [[HEC-1-A (line)]] | alt | 30.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -17.3) |
| [[LoVo (line)]] | wt | 19.2 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -13.5) |
| [[A-427 (line)]] | wt | 31.7 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0877× (z -20.4) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.296× (z -14.4) |
| [[A549 (line)]] | wt | 30.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -17.2) |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -12.6) |
| [[J82 (line)]] | alt | 20.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.4) |
| [[A-172 (line)]] | wt | 47.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -22.5) |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.191× (z -10.1) |
| [[SW480 (line)]] | alt | 9.46 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -11.9) |
| [[Hs 766T (line)]] | wt | 5.92 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0697× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0687× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 7.02 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0807× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.134× (z -8.8) |
| [[RKO (line)]] | wt | 33.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -12.0) |
| [[SNU-1 (line)]] | wt | 36.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -12.1) |
| [[A498 (line)]] | wt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.3) |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -8.8) |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 36.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.6) |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACS2]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[DOP1B]] | +0.57 | +0.36 / +0.62 | both halves | 9e-05 |  |
| [[RASA2]] | +0.57 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[PSEN2]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[B4GALT2]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[BMP2K]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SLC27A5]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_BILE_ACID_METABOLISM |
| [[ANKS6]] | +0.54 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[WSCD1]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[VKORC1L1]] | +0.54 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[SIMC1]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TMOD2]] | +0.53 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A3]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[KLHL3]] | -0.53 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[DNAJB4]] | -0.50 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[CHD3]] | -0.48 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[TET2]] | -0.48 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[MINDY1]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[RNASEL]] | -0.47 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ZNF436]] | -0.47 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[SUPT7L]] | -0.46 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[CASD1]] | -0.46 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[PNISR-AS1]] | -0.45 | -0.19 / -0.44 | ⚠ not reproduced | 8e-04 |  |
| [[ARFGAP2]] | -0.45 | -0.27 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises ABCA3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.55× lower at baseline in the lines without GNAZ | 0.005 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises ABCA3's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.94× lower at baseline in the lines without FAM78B | 0.005 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[KIF26A]] | B | KIF26A activity raises ABCA3's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.26× lower at baseline in the lines without KIF26A | 0.009 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[NFATC4]] | B | NFATC4 activity lowers ABCA3's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 1.87× higher at baseline in the lines without NFATC4 | 0.027 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[JAG2]] | B | JAG2 activity raises ABCA3's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 3.15× lower at baseline in the lines without JAG2 | 0.045 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[SRCIN1]] | B | SRCIN1 activity raises ABCA3's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 2.35× lower at baseline in the lines without SRCIN1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 25, C 1. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMOX2]] | B | ABCA3 activity raises HMOX2's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.42× lower at baseline in the lines without ABCA3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[PPM1G]] | B | ABCA3 activity raises PPM1G's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without ABCA3 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[BMP8B]] | B | ABCA3 activity raises BMP8B's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without ABCA3 | 0.024 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[NFATC4]] | B | ABCA3 activity lowers NFATC4's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 2.29× higher at baseline in the lines without ABCA3 | 0.025 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[GARNL3]] | B | ABCA3 activity raises GARNL3's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without ABCA3 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[VKORC1L1]] | B | ABCA3 activity raises VKORC1L1's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without ABCA3 | 0.039 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[MCF2L2]] | B | ABCA3 activity raises MCF2L2's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 2.16× lower at baseline in the lines without ABCA3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[LRRC20]] | B | ABCA3 activity raises LRRC20's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 2.01× lower at baseline in the lines without ABCA3 | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[DCAF4]] | B | ABCA3 activity raises DCAF4's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without ABCA3 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[RAB27A]] | B | ABCA3 activity weakens RAB27A's drug response | lines that do not express ABCA3 (9) vs lines expressing it (39) | the lines without ABCA3 respond 1.46× as strongly (z diff -1.68); strongest at Homoharringtonine 5 µM: 0.36x vs 0.61x (z diff -4.3) | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NLN]] | B | ABCA3 activity raises NLN's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.71× lower at baseline in the lines without ABCA3 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[PSEN2]] | B | ABCA3 activity raises PSEN2's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without ABCA3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.392). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-4.3, -24.2); signed map (-44.5, -7.8). **Vector** length 82.2, 17.9% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +7.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +4.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.4 | -9.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -8.9 |
|  | [[NG25 (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | +2.1 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,275,881-2,340,746 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ABC-C, EST111653, LBM180; previously ABC3 |
| Gene groups (HGNC) | ATP binding cassette subfamily A; ATPase phospholipid transporting |
| Hallmark sets | BILE_ACID_METABOLISM, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 8 pathways, smallest: Diseases associated with surfactant metabolism; ABC transporters in lipid homeostasis; Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99758](https://www.uniprot.org/uniprotkb/Q99758) (Phospholipid-transporting ATPase ABCA3):

> Catalyzes the ATP-dependent transport of phospholipids such as phosphatidylcholine and phosphoglycerol from the cytoplasm into the lumen side of lamellar bodies, in turn participates in the lamellar bodies biogenesis and homeostasis of pulmonary surfactant. Transports preferentially phosphatidylcholine containing short acyl chains. In addition plays a role as an efflux transporter of miltefosine across macrophage membranes and free cholesterol (FC) through intralumenal vesicles by removing FC …

**Summary**, from NCBI Gene [21](https://www.ncbi.nlm.nih.gov/gene/21):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intracellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ABC1 subfamily. Members of the ABC1 subfamily comprise the only major ABC subfamily found exclusively in multicellular eukaryotes. The full transporter …

**Accessions** — [HGNC:33](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33) · Entrez [21](https://www.ncbi.nlm.nih.gov/gene/21) · UniProt [Q99758](https://www.uniprot.org/uniprotkb/Q99758) · Ensembl [ENSG00000167972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167972)

## Data

Gene col 9566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9566); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9566]; `tensor/DDL_lfc|DDL_z.npy` [9566]; `embed/gene_vectors.npy` [9566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9566 or target_col == 9566). Every well: [[ABCA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

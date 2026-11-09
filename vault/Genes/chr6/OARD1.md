---
symbol: "OARD1"
type: "gene"
col: 4549
ensembl_id: "ENSG00000124596"
name: "O-acyl-ADP-ribose deacylase 1"
location: "6p21.1"
module: 15
arm: "+"
pooled_cpm: 35.07
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 23
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# OARD1

*O-acyl-ADP-ribose deacylase 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +19.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.546× (z -10.9, q 4e-25, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKN2-AS1]] (+0.74, fdr 1e-05), [[PRANCR]] (+0.72, fdr 3e-05), [[ERICH2-DT]] (+0.71, fdr 1e-05); moves opposite to [[SH3PXD2B]] (-0.71, fdr 1e-05), [[PACC1]] (-0.64, fdr 1e-05), [[LRFN3]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4549.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +19.5 | 0e+00 | 47/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.6 | 1e-11 | 27/45 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.5 | 2e-08 | 30/47 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.0 | 3e-07 | 31/48 (Hs 766T, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +5.0 | 6e-05 | 23/38 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.5 | 6e-04 | 16/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 7e-04 | 21/48 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.4 | 8e-04 | 18/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.001 | 22/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.25×** | +3.7 | 0.013 | 17/41 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.025 | 19/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.033 | 10/47 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.042 | 6/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.11 | 12/48 (KATO III, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4549.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.546×** | -10.9 | 4e-25 | 38/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -10.9 | 4e-25 | 35/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.585×** | -9.6 | 1e-19 | 34/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.648×** | -7.8 | 9e-13 | 37/48 (COLO 205, LoVo, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.446×** | -7.6 | 3e-12 | 34/47 (COLO 205, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -7.3 | 2e-11 | 31/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.655×** | -7.2 | 5e-11 | 33/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -6.4 | 9e-09 | 27/49 (COLO 205, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.713×** | -6.1 | 8e-08 | 26/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.720×** | -5.9 | 2e-07 | 25/48 (COLO 205, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.733×** | -5.6 | 1e-06 | 26/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.553×** | -5.6 | 1e-06 | 26/42 (SW480, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.811×** | -5.3 | 5e-06 | 20/48 (SW480, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.749×** | -5.2 | 9e-06 | 28/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.767×** | -4.8 | 7e-05 | 22/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -4.5 | 2e-04 | 21/48 (SW480, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -4.1 | 0.001 | 15/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.809×** | -3.8 | 0.005 | 16/48 (SW480, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.761×** | -3.5 | 0.013 | 16/48 (PANC-1, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.873× | -3.4 | 0.016 | 11/48 (MIA PaCa-2, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 363 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -18.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -16.9) |
| [[SW480 (line)]] | alt | 49.9 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.406× (z -11.8) |
| [[PANC-1 (line)]] | alt | 41.9 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +15.5) | [[Digitoxin (drug)]] 0.5 µM 0.376× (z -11.6) |
| [[HT-29 (line)]] | alt | 38.5 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.9) | [[Ixazomib citrate (drug)]] 5 µM 0.335× (z -10.6) |
| [[LoVo (line)]] | wt | 38.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -12.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 39.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.248× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 26.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.1) | — |
| [[H4 (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.248× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 34.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.391× (z -9.4) |
| [[HOP62 (line)]] | alt | 38.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +10.0) | — |
| [[J82 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 46.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 22.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H23 (line)]] | alt | 61.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.5) | — |
| [[RKO (line)]] | wt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.7) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SW1417 (line)]] | alt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +11.6) | — |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2-AS1]] | +0.74 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[PRANCR]] | +0.72 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[ERICH2-DT]] | +0.71 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.71 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | +0.71 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[AK9]] | +0.71 | +0.74 / +0.40 | both halves | 5e-05 |  |
| [[DICER1-AS1]] | +0.71 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[INO80D]] | +0.70 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[LINC00869-1]] | +0.70 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | +0.69 | +0.74 / +0.40 | both halves | 5e-05 |  |
| [[SPESP1]] | +0.69 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.69 | +0.75 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.71 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[PACC1]] | -0.64 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[LRFN3]] | -0.63 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PIP4K2A]] | -0.63 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[MAST3]] | -0.62 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | -0.61 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[PEDS1]] | -0.61 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[GPRIN1]] | -0.61 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ARRB2]] | -0.60 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[SLC39A3]] | -0.60 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[USP35]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[PRR5]] | -0.60 | -0.63 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OARD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FSD1L]] | C | FSD1L activity lowers OARD1's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 2.62× higher at baseline in the lines without FSD1L | 0.004 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[UNC5CL]] | C | UNC5CL activity raises OARD1's level | lines that do not express UNC5CL (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without UNC5CL | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MEGF11; maybe low, not absent; its own permutation p |
| [[MORN1]] | C | MORN1's natural level strengthens OARD1's drug response | MORN1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.23; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.1, 19.6); signed map (27.8, -7.7). **Vector** length 94.3, 22.6% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +19.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | -0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -7.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.2 | -5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.2 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | O-acyl-ADP-ribose deacylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,033,627-41,097,787 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC19570, dJ34B21.3, TARG1; previously C6orf130 |
| Gene groups (HGNC) | Macro domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y530](https://www.uniprot.org/uniprotkb/Q9Y530) (ADP-ribose glycohydrolase OARD1):

> ADP-ribose glycohydrolase that hydrolyzes ADP-ribose and acts on different substrates, such as proteins ADP-ribosylated on glutamate and O-acetyl-ADP-D-ribose. Specifically acts as a glutamate mono-ADP-ribosylhydrolase by mediating the removal of mono-ADP-ribose attached to glutamate residues on proteins. Does not act on poly-ADP-ribosylated proteins: the poly-ADP-ribose chain of poly-ADP-ribosylated glutamate residues must by hydrolyzed into mono-ADP-ribosylated glutamate by PARG to become a …

**Summary**, from NCBI Gene [221443](https://www.ncbi.nlm.nih.gov/gene/221443):

> The protein encoded by this gene is a deacylase that can convert O-acetyl-ADP-ribose to ADP-ribose and acetate, O-propionyl-ADP-ribose to ADP-ribose and propionate, and O-butyryl-ADP-ribose to ADP-ribose and butyrate. The ADP-ribose product is able to inhibit these reactions through a competitive feedback loop. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:21257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21257) · Entrez [221443](https://www.ncbi.nlm.nih.gov/gene/221443) · UniProt [Q9Y530](https://www.uniprot.org/uniprotkb/Q9Y530) · Ensembl [ENSG00000124596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124596)

## Data

Gene col 4549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4549); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4549]; `tensor/DDL_lfc|DDL_z.npy` [4549]; `embed/gene_vectors.npy` [4549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4549 or target_col == 4549). Every well: [[OARD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OARD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "OMA1"
type: "gene"
col: 8538
ensembl_id: "ENSG00000162600"
name: "OMA1 zinc metallopeptidase"
location: "1p32.2-p32.1"
module: 10
arm: "+"
pooled_cpm: 29.84
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 32
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# OMA1

*OMA1 zinc metallopeptidase* — 1p32.2-p32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.26× (z +4.1, q 0.011, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.183× (z -20.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[R3HDM2]] (+0.73, fdr 7e-06), [[LEKR1]] (+0.66, fdr 3e-05), [[TAPT1-AS1]] (+0.63, fdr 2e-05); moves opposite to [[NTAN1]] (-0.62, fdr 7e-06), [[FCHSD1]] (-0.59, fdr 1e-05), [[HSPB11]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Gemcitabine (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.011 | 20/48 (A498, LS 180, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.011 | 25/47 (RKO, C32, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.011 | 21/46 (RKO, Hs 766T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.012 | 19/48 (SW480, LS 180, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.30× | +3.2 | 0.14 | 11/48 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.25× | +3.2 | 0.14 | 9/48 (Hs 766T, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.14 | 16/48 (RKO, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.14 | 10/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.28× | +3.0 | 0.14 | 15/47 (H4, A498, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.30× | +3.0 | 0.14 | 8/47 (Hs 766T, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.183×** | -20.9 | 0e+00 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.226×** | -18.3 | 0e+00 | 44/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.250×** | -17.0 | 0e+00 | 47/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.294×** | -15.0 | 0e+00 | 44/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.327×** | -13.7 | 7e-41 | 43/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.477×** | -8.7 | 2e-16 | 36/46 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.520×** | -8.0 | 8e-14 | 38/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.536×** | -7.6 | 2e-12 | 36/48 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.309×** | -7.5 | 3e-12 | 34/46 (HEC-1-A, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.313×** | -7.5 | 5e-12 | 40/48 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.526×** | -7.4 | 5e-12 | 36/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.388×** | -6.1 | 6e-08 | 33/41 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.657×** | -4.9 | 3e-05 | 21/43 (SNU-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.754×** | -4.9 | 4e-05 | 22/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.767×** | -4.6 | 2e-04 | 22/47 (SW1417, A498, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.704×** | -4.3 | 6e-04 | 24/48 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.596×** | -4.3 | 6e-04 | 20/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.629×** | -4.0 | 0.001 | 21/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.006 | 22/48 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.662×** | -3.6 | 0.007 | 20/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 67.6 | 0 | 12 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0570× (z -30.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0771× (z -27.5) |
| [[A-427 (line)]] | wt | 40.0 | 0 | 9 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -17.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -12.0) |
| [[HT-29 (line)]] | alt | 29.4 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0977× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 65.9 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0575× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0753× (z -23.2) |
| [[SW480 (line)]] | alt | 20.7 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.160× (z -15.0) |
| [[C32 (line)]] | wt | 43.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0909× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.202× (z -10.2) |
| [[LoVo (line)]] | wt | 26.6 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 51.0 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -16.0) |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0978× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 49.1 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.174× (z -12.1) |
| [[SHP-77 (line)]] | alt | 21.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -11.5) |
| [[SW1417 (line)]] | alt | 38.9 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0622× (z -19.7) |
| [[A549 (line)]] | wt | 18.8 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.194× (z -9.5) |
| [[COLO 205 (line)]] | alt | 58.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.156× (z -13.2) |
| [[KATO III (line)]] | alt | 32.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0521× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 26.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0639× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0698× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -10.9) |
| [[SNU-423 (line)]] | alt | 28.3 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.127× (z -11.1) |
| [[C-33 A (line)]] | alt | 54.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 43.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.124× (z -9.8) |
| [[Hs 766T (line)]] | wt | 29.0 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +8.6) ⚠ cell-cycle shift, explains ~2% of this change | [[Digitoxin (drug)]] 0.5 µM 0.188× (z -10.1) |
| [[LS 180 (line)]] | wt | 38.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0567× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 30.8 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -12.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.181× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 27.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0380× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0693× (z -13.8) |
| [[SNU-1 (line)]] | wt | 48.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0204× (z -21.2) |
| [[A498 (line)]] | wt | 24.0 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.142× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 20.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -8.9) |
| [[HCT15 (line)]] | alt | 33.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.162× (z -10.2) |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.143× (z -10.9) |
| [[HS-578T (line)]] | alt | 22.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0520× (z -15.1) |
| [[J82 (line)]] | alt | 13.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.120× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.103× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.193× (z -10.8) |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -10.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HDM2]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[LEKR1]] | +0.66 | +0.79 / +0.43 | both halves | 3e-05 |  |
| [[TAPT1-AS1]] | +0.63 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[LINC00886]] | +0.61 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[RAP2C-AS1]] | +0.60 | +0.72 / +0.42 | both halves | 4e-05 |  |
| [[KRCC1]] | +0.58 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[GMDS-DT]] | +0.58 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[LINC02340]] | +0.58 | +0.72 / +0.36 | both halves | 1e-04 |  |
| [[LINC00174]] | +0.57 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[TASOR]] | +0.57 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[BDNF-AS]] | +0.56 | +0.72 / +0.40 | both halves | 5e-05 |  |
| [[PDCL3P4]] | +0.56 | +0.70 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTAN1]] | -0.62 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[FCHSD1]] | -0.59 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.58 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[ABCD4]] | -0.58 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[SEMA6C]] | -0.58 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[LSP1P5-1]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[LSP1P4]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZNF823]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.55 | -0.64 / -0.39 | both halves | 6e-05 |  |
| [[KLHL7]] | -0.55 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[USP35]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[LMBR1L]] | -0.54 | -0.61 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Gemcitabine (drug)]] 5 µM | C | OMA1's natural level raises the cells' numbers under Gemcitabine 5 µM (protects the cells) | OMA1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.268 over the table, 0.025 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.1, 14.6); signed map (28.1, -11.9). **Vector** length 72.1, 17.9% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.6 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.4 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +2.1 |
|  | [[Omeprazole (drug)]] 5 µM |  | +1.2 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.1 | -7.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.7 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -8.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | OMA1 zinc metallopeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.2-p32.1 — chr1:58,415,384-58,546,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MPRP-1, YKR087C, ZMPOMA1, FLJ33782 |
| Gene groups (HGNC) | M48 metallopeptidase family |
| Reactome | 7 pathways, smallest: Cellular response to mitochondrial stress; Regulation of Apoptosis; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E52](https://www.uniprot.org/uniprotkb/Q96E52) (Metalloendopeptidase OMA1, mitochondrial):

> Metalloprotease that is part of the quality control system in the inner membrane of mitochondria. Activated in response to various mitochondrial stress, leading to the proteolytic cleavage of target proteins, such as OPA1, UQCC3 and DELE1. Involved in the fusion of the mitochondrial inner membranes by mediating cleavage of OPA1 at S1 position, generating the soluble OPA1 (S-OPA1), which cooperates with the membrane form (L-OPA1) to coordinate the fusion of mitochondrial inner membranes. …

**Summary**, from NCBI Gene [115209](https://www.ncbi.nlm.nih.gov/gene/115209):

> Enables metalloendopeptidase activity. Involved in several processes, including HRI-mediated signaling; mitochondrial protein processing; and regulation of mitochondrion organization. Located in mitochondrial inner membrane. Is active in mitochondrial intermembrane space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29661) · Entrez [115209](https://www.ncbi.nlm.nih.gov/gene/115209) · UniProt [Q96E52](https://www.uniprot.org/uniprotkb/Q96E52) · Ensembl [ENSG00000162600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162600)

## Data

Gene col 8538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8538); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8538]; `tensor/DDL_lfc|DDL_z.npy` [8538]; `embed/gene_vectors.npy` [8538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8538 or target_col == 8538). Every well: [[OMA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OMA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

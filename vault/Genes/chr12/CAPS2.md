---
symbol: "CAPS2"
type: "gene"
col: 11142
ensembl_id: "ENSG00000180881"
name: "calcyphosine 2"
location: "12q21.1-q21.2"
module: 117
arm: "+"
pooled_cpm: 31.37
n_lines_expressing: 39
n_dd_up: 36
n_dd_down: 24
n_dd_up_clean: 32
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# CAPS2

*calcyphosine 2* — 12q21.1-q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +10.6, q 1e-23, up in 19 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.354× (z -12.3, q 4e-32, down in 33 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.365× (z -12.0, q 2e-30, down in 33 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALOX12P2-1]] (+0.76, fdr 8e-06), [[EGF]] (+0.72, fdr 7e-06), [[TLR1]] (+0.70, fdr 1e-05); moves opposite to [[FANCE]] (-0.62, fdr 3e-05), [[PACS2]] (-0.59, fdr 1e-05), [[SPATA33]] (-0.57, fdr 5e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PCDHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +10.6 | 1e-23 | 19/37 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.35×** | +10.1 | 1e-21 | 24/37 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **2.06×** | +8.2 | 3e-14 | 31/36 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.99×** | +7.7 | 2e-12 | 29/37 (COLO 205, C32, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +7.5 | 1e-11 | 23/37 (COLO 205, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.84×** | +7.2 | 5e-11 | 28/37 (A-172, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +6.9 | 6e-10 | 23/37 (HT-29, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.5 | 7e-09 | 22/37 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.64×** | +5.9 | 3e-07 | 27/36 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.63×** | +5.6 | 1e-06 | 25/36 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +5.3 | 5e-06 | 20/37 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.3 | 6e-06 | 24/37 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.48×** | +5.3 | 6e-06 | 22/37 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 2e-05 | 20/37 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +5.0 | 2e-05 | 16/37 (AsPC-1, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.47×** | +5.0 | 2e-05 | 20/37 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.354×** | -12.3 | 4e-32 | 33/36 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.365×** | -12.0 | 2e-30 | 33/37 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.375×** | -11.6 | 5e-29 | 32/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.449×** | -9.5 | 2e-19 | 27/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.466×** | -8.7 | 3e-16 | 25/35 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.524×** | -5.2 | 2e-05 | 20/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.667×** | -4.8 | 1e-04 | 24/37 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.762×** | -4.6 | 3e-04 | 20/37 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.689×** | -4.4 | 6e-04 | 17/36 (Panc 03.27, NCI-H460, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.697×** | -4.3 | 1e-03 | 18/37 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.689×** | -4.3 | 0.001 | 17/36 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.712×** | -4.0 | 0.002 | 19/37 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.531×** | -3.9 | 0.004 | 20/37 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.710×** | -3.9 | 0.004 | 15/37 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.722×** | -3.9 | 0.004 | 17/37 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.724×** | -3.9 | 0.004 | 19/36 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.747×** | -3.5 | 0.016 | 13/36 (NCI-H661, SK-MEL-2, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.668×** | -3.4 | 0.018 | 14/37 (NCI-H1792, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.661×** | -3.3 | 0.024 | 14/36 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 137 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0848× (z -28.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 77.8 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -15.3) |
| [[COLO 205 (line)]] | alt | 44.0 | 3 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 6.38× (z +12.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0286× (z -22.1) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.131× (z -13.2) |
| [[PANC-1 (line)]] | alt | 63.7 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.122× (z -20.4) |
| [[LOX-IMVI (line)]] | wt | 29.9 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +15.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.206× (z -9.8) |
| [[LS 180 (line)]] | wt | 33.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0615× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.147× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 50.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +21.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -10.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 57.0 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.188× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.237× (z -12.1) |
| [[RKO (line)]] | wt | 82.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.233× (z -13.1) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 9.28 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 76.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -11.5) |
| [[C32 (line)]] | wt | 29.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +10.6) | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0246× (z -15.1) |
| [[J82 (line)]] | alt | 13.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 66.6 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.09× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.246× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 24.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +8.7) | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0607× (z -10.9) |
| [[A-172 (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.4) | — |
| [[A498 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.240× (z -9.9) ⚠ toxic |
| [[A549 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 8.26 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.88× (z +12.2) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0964× (z -8.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 9.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.275× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 31.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALOX12P2-1]] | +0.76 | +0.76 / +0.58 | both halves | 8e-06 |  |
| [[EGF]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[TLR1]] | +0.70 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TLR6]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[ZSCAN31]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[TRIM16L]] | +0.67 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[HTATIP2]] | +0.67 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[GNGT1]] | +0.67 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ABCC2]] | +0.67 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[LINC02328]] | +0.66 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[LRP1B]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[GCNT2]] | +0.63 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCE]] | -0.62 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[PACS2]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[SPATA33]] | -0.57 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TSEN54]] | -0.56 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[SNX25]] | -0.55 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[MCRIP1]] | -0.55 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ZMYND19]] | -0.54 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[CCNQ]] | -0.54 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[NPHP4]] | -0.53 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[ADCK5]] | -0.53 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[TMEM120B]] | -0.52 | -0.64 / -0.23 | both halves | 5e-04 |  |
| [[AXIN1]] | -0.52 | -0.59 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHA6]] | B | PCDHA6 activity raises CAPS2's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.60× lower at baseline in the lines without PCDHA6 | 0.028 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[TOP2A]] | B | TOP2A activity lowers CAPS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CYP4F11]] | B | CYP4F11 activity weakens CAPS2's drug response | lines that do not express CYP4F11 (24) vs lines expressing it (13) | the lines without CYP4F11 respond 1.01× as strongly (z diff -0.01); strongest at Homoharringtonine 5 µM: 2.61x vs 0.79x (z diff -8.2) | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; target measured in part of the lines; both ways; artifact flags |
| [[VEGFD]] | B | VEGFD activity raises CAPS2's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.49× lower at baseline in the lines without VEGFD | 0.089 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.3, 48.1); signed map (50.2, -8.4). **Vector** length 107, 31.1% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.9 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +10.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +6.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.7 | +5.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -12.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -4.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | calcyphosine 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1-q21.2 — chr12:75,275,979-75,390,928 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Calcyphosine family |
| Matched by | ensembl_id |

UniProt [Q9BXY5](https://www.uniprot.org/uniprotkb/Q9BXY5) carries no function annotation.

**Summary**, from NCBI Gene [84698](https://www.ncbi.nlm.nih.gov/gene/84698):

> Calcyphosine-2 is a calcium-binding protein with 2 EF-hand motifs (Wang et al., 2002 [PubMed 11846421]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16471) · Entrez [84698](https://www.ncbi.nlm.nih.gov/gene/84698) · UniProt [Q9BXY5](https://www.uniprot.org/uniprotkb/Q9BXY5) · Ensembl [ENSG00000180881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180881)

## Data

Gene col 11142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11142); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11142]; `tensor/DDL_lfc|DDL_z.npy` [11142]; `embed/gene_vectors.npy` [11142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11142 or target_col == 11142). Every well: [[CAPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

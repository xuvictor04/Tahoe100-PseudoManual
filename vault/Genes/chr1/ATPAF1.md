---
symbol: "ATPAF1"
type: "gene"
col: 4436
ensembl_id: "ENSG00000123472"
name: "ATP synthase mitochondrial F1 complex assembly factor 1"
location: "1p33"
module: 175
arm: "+"
pooled_cpm: 38.03
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# ATPAF1

*ATP synthase mitochondrial F1 complex assembly factor 1* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.46× (z +10.3, q 2e-22, up in 24 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.21× (z +5.4, q 1e-05, up in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 2.72×, J82 2.40×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.80×; ⚠ toxic; cell-cycle shift, explains <1% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 2.75×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.570× (z -22.5, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMM50]] (+0.63, fdr 1e-05), [[SEC23A]] (+0.63, fdr 7e-06), [[OSTC]] (+0.61, fdr 1e-05); moves opposite to [[TSC22D1]] (-0.61, fdr 1e-05), [[SVIL]] (-0.61, fdr 1e-05), [[ADNP2]] (-0.56, fdr 1e-05).
> It is in [[Module 175]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4436.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 2.72×, J82 2.40×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.80×; ⚠ toxic; cell-cycle shift, explains <1% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 2.75×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +10.3 | 2e-22 | 24/38 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +9.7 | 1e-19 | 27/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +7.5 | 2e-11 | 23/42 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.20× | +7.2 | 9e-11 | 18/48 (A498, A-427, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +5.4 | 1e-05 | 18/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +4.6 | 5e-04 | 7/48 (HOP62, AN3 CA, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains <1% of this change | 1.16× | +4.0 | 0.005 | 17/45 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.081 | 7/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.12× | +3.2 | 0.081 | 6/48 (Panc 03.27, CHP-212, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.08× | +3.2 | 0.081 | 6/48 (NCI-H1792, HCT15, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.083 | 7/48 (H4, NCI-H2030, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.09× | +3.1 | 0.083 | 8/48 (NCI-H2347, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.10 | 8/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.570×** | -22.5 | 0e+00 | 36/47 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.571×** | -15.8 | 0e+00 | 36/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -15.0 | 0e+00 | 35/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.612×** | -13.9 | 1e-41 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -10.0 | 3e-21 | 33/47 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.733×** | -8.8 | 2e-16 | 29/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.735×** | -8.7 | 3e-16 | 32/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.560×** | -8.6 | 9e-16 | 28/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.744×** | -8.3 | 5e-15 | 29/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.754×** | -7.9 | 1e-13 | 28/48 (PANC-1, SW48, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.777×** | -7.1 | 6e-11 | 28/47 (A498, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.634×** | -6.7 | 9e-10 | 26/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.821×** | -5.5 | 1e-06 | 20/48 (SK-MEL-2, C-33 A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.857× | -4.3 | 6e-04 | 10/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -4.2 | 1e-03 | 12/47 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.859× | -4.1 | 0.001 | 15/48 (SNU-423, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.903× | -4.0 | 0.002 | 10/48 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.875× | -3.6 | 0.009 | 6/48 (MIA PaCa-2, A498, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | 0.882× | -3.4 | 0.019 | 8/48 (C32, SNU-423, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.887× | -3.2 | 0.038 | 11/47 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.894× | -3.0 | 0.057 | 10/48 (SW 900, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.6 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -16.4) |
| [[NCI-H460 (line)]] | wt | 38.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -13.6) |
| [[SW480 (line)]] | alt | 39.4 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.412× (z -11.5) |
| [[A498 (line)]] | wt | 36.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -19.6) |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.343× (z -11.5) |
| [[C32 (line)]] | wt | 34.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.3) |
| [[HOP62 (line)]] | alt | 37.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -10.0) |
| [[HS-578T (line)]] | alt | 50.4 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.296× (z -12.0) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.439× (z -11.4) |
| [[J82 (line)]] | alt | 37.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -10.0) |
| [[LoVo (line)]] | wt | 39.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -11.6) |
| [[LS 180 (line)]] | wt | 53.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.407× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.464× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 47.0 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.80× (z +9.9) ⚠ toxic; cell-cycle shift, explains <1% of this change | — |
| [[NCI-H1573 (line)]] | alt | 37.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.221× (z -12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.3) |
| [[A-172 (line)]] | wt | 36.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.3) |
| [[A-427 (line)]] | wt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.2) |
| [[A549 (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.8) |
| [[AN3 CA (line)]] | alt | 40.1 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0843× (z -11.0) |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -11.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -13.0) |
| [[HT-29 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -15.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.4) |
| [[KATO III (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.75× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.316× (z -10.3) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H661 (line)]] | alt | 35.4 | 0 | 1 | — | [[Bicalutamide (drug)]] 0.5 µM 0.0792× (z -8.6) |
| [[SNU-423 (line)]] | alt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.2) |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMM50]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SEC23A]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[OSTC]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[UBA5]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[VDAC1P8]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[COPG1]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[GK5]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CIZ1]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[MRS2]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[DDHD2]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[RWDD4]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[DNAJC24]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D1]] | -0.61 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[SVIL]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ADNP2]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[HES1]] | -0.56 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[CENPB]] | -0.56 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[FOXP1]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[NEDD4L]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[RASAL2]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[GASAL1]] | -0.54 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[FJX1]] | -0.53 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[MIDN]] | -0.53 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[ZDHHC14]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.4, -11.8); signed map (-35.5, -21.9). **Vector** length 76.6, 14.3% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.5 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +3.1 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains <1% of this change | +2.9 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +3.2 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | +1.4 | -0.2 |
|  | [[Capivasertib (drug)]] 0.5 µM |  | +1.4 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -15.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -22.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.7 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase mitochondrial F1 complex assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:46,632,737-46,673,867 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22351, Atp11p, ATP11 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TC12](https://www.uniprot.org/uniprotkb/Q5TC12) (ATP synthase mitochondrial F1 complex assembly factor 1):

> Has a complex stabilizing activity in the assembly of the mitochondrial F1-F0 complex.

**Summary**, from NCBI Gene [64756](https://www.ncbi.nlm.nih.gov/gene/64756):

> This gene encodes an assembly factor for the F(1) component of the mitochondrial ATP synthase. This protein binds specifically to the F1 beta subunit and is thought to prevent this subunit from forming nonproductive homooligomers during enzyme assembly. Alternatively spliced transcript variants have been identified. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:18803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18803) · Entrez [64756](https://www.ncbi.nlm.nih.gov/gene/64756) · UniProt [Q5TC12](https://www.uniprot.org/uniprotkb/Q5TC12) · Ensembl [ENSG00000123472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123472)

## Data

Gene col 4436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4436); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4436]; `tensor/DDL_lfc|DDL_z.npy` [4436]; `embed/gene_vectors.npy` [4436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4436 or target_col == 4436). Every well: [[ATPAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATPAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

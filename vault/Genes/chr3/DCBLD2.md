---
symbol: "DCBLD2"
type: "gene"
col: 643
ensembl_id: "ENSG00000057019"
name: "discoidin, CUB and LCCL domain containing 2"
location: "3q12.1"
module: 151
arm: "+"
pooled_cpm: 648.77
n_lines_expressing: 41
n_dd_up: 15
n_dd_down: 58
n_dd_up_clean: 8
n_dd_down_clean: 55
in_vector_space: true
direction_upstream: 15
direction_downstream: 3
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# DCBLD2

*discoidin, CUB and LCCL domain containing 2* — 3q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.06× (z +10.8, q 1e-24, up in 31 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM: 1.28× (z +3.7, q 0.021, up in 26 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 58 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.469× (z -11.6, q 1e-28, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NT5E]] (+0.78, fdr 7e-06), [[ITGA2]] (+0.76, fdr 7e-06), [[PHLDA1]] (+0.72, fdr 7e-06); moves opposite to [[EDN2]] (-0.68, fdr 7e-06), [[FLVCR2]] (-0.61, fdr 7e-06), [[TSC22D3]] (-0.61, fdr 7e-06).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[LINC00973]] → it (grade B ⚠); 3 go from it, the strongest it → [[ADAM19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +10.8 | 1e-24 | 31/40 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +10.2 | 6e-22 | 31/37 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +8.0 | 3e-13 | 28/37 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.2 | 0.005 | 21/39 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +3.7 | 0.021 | 21/38 (HT-29, LS 180, …) | rises with dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.021 | 26/40 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.022 | 26/40 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.032 | 21/38 (HT-29, LS 180, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +3.4 | 0.038 | 21/39 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.038 | 22/39 (HS-578T, Panc 03.27, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.038 | 21/39 (SK-MEL-2, NCI-H2347, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.046 | 23/39 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +3.2 | 0.054 | 17/39 (HT-29, LS 180, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.075 | 19/39 (RPMI-7951, Panc 03.27, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.075 | 16/40 (CFPAC-1, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 4 with an alert ⚠; shown: the 15 strongest. 58 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 643.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.469×** | -11.6 | 1e-28 | 37/41 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -11.3 | 3e-27 | 31/40 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.549×** | -10.7 | 3e-24 | 37/39 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.551×** | -10.5 | 2e-23 | 33/39 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.519×** | -9.8 | 2e-20 | 36/40 (HepG2/C3A, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.540×** | -9.2 | 2e-18 | 33/40 (HepG2/C3A, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.549×** | -8.6 | 7e-16 | 35/39 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.566×** | -8.5 | 1e-15 | 32/39 (A-172, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.595×** | -7.2 | 5e-11 | 31/39 (SK-MEL-2, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.607×** | -7.0 | 1e-10 | 30/39 (HepG2/C3A, SK-MEL-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.617×** | -6.9 | 2e-10 | 31/38 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.721×** | -6.7 | 9e-10 | 26/40 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.736×** | -6.4 | 5e-09 | 25/39 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.746×** | -6.2 | 3e-08 | 30/39 (C32, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -6.1 | 5e-08 | 24/39 (HEC-1-A, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 1,036 | 0 | 19 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0649× (z -32.3) |
| [[NCI-H460 (line)]] | wt | 697 | 0 | 17 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 622 | 0 | 16 (2 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.322× (z -14.1) |
| [[SW480 (line)]] | alt | 1,056 | 0 | 16 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -17.6) |
| [[C32 (line)]] | wt | 685 | 1 (1 ⚠) | 14 | [[Harringtonine (drug)]] 0.5 µM 3.36× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Binimetinib (drug)]] 0.5 µM 0.199× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 1,986 | 0 | 15 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -23.3) |
| [[HT-29 (line)]] | alt | 347 | 15 (7 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.89× (z +20.5) | — |
| [[A-427 (line)]] | wt | 1,295 | 1 (1 ⚠) | 13 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.34× (z +11.1) ⚠ toxic; transcription drop | [[Binimetinib (drug)]] 5 µM 0.317× (z -15.2) |
| [[HOP62 (line)]] | alt | 1,404 | 0 | 14 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.615× (z -14.7) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 483 | 2 (1 ⚠) | 11 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +17.8) | [[Trametinib (drug)]] 5 µM 0.267× (z -13.8) |
| [[LoVo (line)]] | wt | 187 | 5 (3 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +19.8) | [[Binimetinib (drug)]] 0.5 µM 0.411× (z -10.9) |
| [[A-172 (line)]] | wt | 2,336 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -19.4) |
| [[LS 180 (line)]] | wt | 269 | 0 | 9 | — | [[Binimetinib (drug)]] 0.5 µM 0.372× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 935 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -8.9) |
| [[SW48 (line)]] | wt | 462 | 2 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 0.5 µM 3.44× (z +11.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.9) | [[Binimetinib (drug)]] 5 µM 0.331× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 431 | 0 | 7 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.603× (z -14.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -12.0) |
| [[Hs 766T (line)]] | wt | 328 | 0 | 5 | — | [[Binimetinib (drug)]] 0.5 µM 0.417× (z -9.7) |
| [[A549 (line)]] | wt | 790 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +10.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -16.1) |
| [[SW1417 (line)]] | alt | 1,323 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -15.5) |
| [[CHP-212 (line)]] | wt | 221 | 3 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.65× (z +10.1) | — |
| [[J82 (line)]] | alt | 678 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 185 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.490× (z -20.8) ⚠ position not correctable · without an alert: [[Radotinib (drug)]] 5 µM 0.469× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 569 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.4) |
| [[A498 (line)]] | wt | 493 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 202 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 262 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 240 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 186 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 863 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -11.9) |
| [[HS-578T (line)]] | alt | 565 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 249 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.657× (z -15.4) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 636 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.4) |
| [[SNU-423 (line)]] | alt | 1,436 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -12.6) |
| [[SW 900 (line)]] | alt | 906 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -14.9) |
| [[BT-474 (line)]] | alt | 88.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 105 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 140 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 270 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 780 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 112 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 122 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 434 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 553 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 151 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 128 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 113 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 510 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 308 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5E]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.76 | +0.78 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[PHLDA1]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ADAM19]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SLC4A7]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CD44]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[MACF1]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[CAPN2]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[MANCR]] | +0.66 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[MIR222HG]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.65 | +0.68 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDN2]] | -0.68 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[FLVCR2]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[TSC22D3]] | -0.61 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[ZCCHC8]] | -0.56 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[NUPR1]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00973]] | B | LINC00973 activity raises DCBLD2's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 3.57× lower at baseline in the lines without LINC00973 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1 |
| [[ADAM19]] | B | ADAM19 activity raises DCBLD2's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.88× lower at baseline in the lines without ADAM19 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[IL11]] | B | IL11 activity raises DCBLD2's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.63× lower at baseline in the lines without IL11 | 0.009 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[AMOTL1]] | B | AMOTL1 activity raises DCBLD2's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without AMOTL1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[EVA1A]] | B | EVA1A activity raises DCBLD2's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.78× lower at baseline in the lines without EVA1A | 0.022 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[NES]] | B | NES activity raises DCBLD2's level | lines that do not express NES (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without NES | 0.041 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490 |
| [[PALM2AKAP2]] | B | PALM2AKAP2 activity raises DCBLD2's level | lines that do not express PALM2AKAP2 (9) vs lines expressing it (41) | 2.97× lower at baseline in the lines without PALM2AKAP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MPP1, LIX1L |
| [[DLC1]] | B | DLC1 activity raises DCBLD2's level | lines that do not express DLC1 (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without DLC1 | 0.051 | ⚠ within organs, on part of the lines; also absent: AXL, LGALS1, VCAN |
| [[FAM3C2P]] | B | FAM3C2P activity raises DCBLD2's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without FAM3C2P | 0.051 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[UBASH3B]] | B | UBASH3B activity raises DCBLD2's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.73× lower at baseline in the lines without UBASH3B | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[ARHGAP29]] | B | ARHGAP29 activity raises DCBLD2's level | lines that do not express ARHGAP29 (10) vs lines expressing it (40) | 2.58× lower at baseline in the lines without ARHGAP29 | 0.068 | ⚠ within organs, on part of the lines; also absent: HTATIP2, CTSZ, TBILA |
| [[LINC02813]] | B | LINC02813 activity raises DCBLD2's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without LINC02813 | 0.079 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM19]] | B | DCBLD2 activity raises ADAM19's level | lines that do not express DCBLD2 (9) vs lines expressing it (41) | 4.51× lower at baseline in the lines without DCBLD2 | 0.032 | ⚠ within organs, on part of the lines; also absent: C12orf75, ST3GAL6, OSBPL6; maybe low, not absent |
| [[KIF13A]] | B | DCBLD2 activity strengthens KIF13A's drug response | lines that do not express DCBLD2 (9) vs lines expressing it (40) | the lines without DCBLD2 respond 0.81× as strongly (z diff +1.73); strongest at Dinaciclib 5 µM: 0.56x vs 0.41x (z diff +3.0) | 0.065 | ⚠ within organs, on part of the lines; also absent: C12orf75, ST3GAL6, OSBPL6; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Belumosudil (drug)]] 5 µM | B | DCBLD2 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express DCBLD2 (9) vs lines expressing it (39) | the lines without DCBLD2: 0.58× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: C12orf75, ST3GAL6, OSBPL6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.0, 6.8); signed map (5.9, 45.7). **Vector** length 157, 56.7% of its response variance represented; |z| ≥ 3 in 1,974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.3 | +3.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.9 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.4 | +2.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +4.1 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +3.7 | +3.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.6 | +3.4 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -10.9 | -10.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -10.3 | -11.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -10.2 | -9.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -9.5 | -9.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -9.5 | -8.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -9.4 | -10.5 |

## What is on record

|  |  |
|---|---|
| Name | discoidin, CUB and LCCL domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.1 — chr3:98,795,941-98,901,695 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLCP1, ESDN |
| Hallmark sets | APICAL_SURFACE, INFLAMMATORY_RESPONSE, KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

UniProt [Q96PD2](https://www.uniprot.org/uniprotkb/Q96PD2) carries no function annotation.

**Summary**, from NCBI Gene [131566](https://www.ncbi.nlm.nih.gov/gene/131566):

> Predicted to enable signaling receptor activity. Involved in negative regulation of cell growth and wound healing. Located in cell surface and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24627) · Entrez [131566](https://www.ncbi.nlm.nih.gov/gene/131566) · UniProt [Q96PD2](https://www.uniprot.org/uniprotkb/Q96PD2) · Ensembl [ENSG00000057019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057019)

## Data

Gene col 643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 643); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 643]; `tensor/DDL_lfc|DDL_z.npy` [643]; `embed/gene_vectors.npy` [643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 643 or target_col == 643). Every well: [[DCBLD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCBLD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

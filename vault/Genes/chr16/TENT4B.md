---
symbol: "TENT4B"
type: "gene"
col: 4262
ensembl_id: "ENSG00000121274"
name: "terminal nucleotidyltransferase 4B"
location: "16q12.1"
module: 3
arm: "+"
pooled_cpm: 56.19
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TENT4B

*terminal nucleotidyltransferase 4B* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.06× (z +21.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.755× (z -4.9, q 7e-04, down in 25 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A-427 0.160×, AN3 CA 0.114×, SK-MEL-2 0.262×, CHP-212 0.141×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.193×, LS 180 0.303×, NCI-H460 0.350×, CHP-212 0.146×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.109×, C32 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C15orf61]] (+0.63, fdr 5e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[ARL8A]] (+0.61, fdr 7e-05), [[UBR2]] (+0.60, fdr 3e-05), [[DSTYK]] (+0.60, fdr 1e-05); moves opposite to [[ARPC4]] (-0.63, fdr 1e-05), [[SPTLC1]] (-0.61, fdr 1e-05), [[SSU72]] (-0.56, fdr 9e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP3K21]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.06×** | +21.0 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.98×** | +20.5 | 0e+00 | 47/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +19.7 | 0e+00 | 43/48 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.57×** | +17.7 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +13.4 | 3e-39 | 41/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +12.5 | 7e-34 | 42/48 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +11.3 | 9e-28 | 43/48 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.70×** | +10.0 | 1e-21 | 38/47 (LoVo, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +10.0 | 1e-21 | 42/48 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.70×** | +9.9 | 2e-21 | 37/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.73×** | +9.4 | 2e-19 | 44/48 (SW480, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +8.9 | 2e-17 | 36/48 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +8.6 | 2e-16 | 37/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.56×** | +7.6 | 9e-13 | 36/47 (COLO 205, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.15×** | +7.5 | 2e-12 | 42/49 (SW480, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +6.8 | 3e-10 | 34/48 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +6.2 | 1e-08 | 33/48 (A498, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.3 | 3e-06 | 25/48 (SW480, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +5.0 | 1e-05 | 30/49 (A498, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4262.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A-427 0.160×, AN3 CA 0.114×, SK-MEL-2 0.262×, CHP-212 0.141×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.193×, LS 180 0.303×, NCI-H460 0.350×, CHP-212 0.146×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.109×, C32 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -4.9 | 7e-04 | 25/45 (A-427, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.787×** | -4.1 | 0.010 | 20/42 (A-427, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 57.5 | 13 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.50× (z +18.7) | — |
| [[KATO III (line)]] | alt | 66.6 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.9) | — |
| [[LoVo (line)]] | wt | 48.7 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.3) | — |
| [[RKO (line)]] | wt | 46.8 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.73× (z +15.4) | — |
| [[SW1417 (line)]] | alt | 74.9 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 53.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.6) | — |
| [[hTERT-HPNE (line)]] | wt | 42.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 80.2 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.59× (z +14.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[NCI-H1792 (line)]] | alt | 33.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +18.4) | — |
| [[NCI-H460 (line)]] | wt | 50.9 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 52.2 | 5 | 0 | [[Belinostat (drug)]] 5 µM 4.00× (z +13.4) | — |
| [[A-427 (line)]] | wt | 50.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -16.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 50.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 42.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +13.5) | — |
| [[RPMI-7951 (line)]] | alt | 41.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +10.4) | — |
| [[C32 (line)]] | wt | 67.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 29.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 25.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 80.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -9.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 52.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.35× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 41.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.15× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 56.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 44.7 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.66× (z +12.2) | — |
| [[A498 (line)]] | wt | 118 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +15.6) | — |
| [[HepG2_C3A (line)]] | wt | 74.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.8) | — |
| [[J82 (line)]] | alt | 55.0 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.15× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 96.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +12.4) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.303× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 33.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.02× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 43.5 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.89× (z +11.8) | — |
| [[CHP-212 (line)]] | wt | 71.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 95.5 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.28× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 44.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 43.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 51.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -11.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 43.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.32× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 76.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 34.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.16× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 73.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 36.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.2) | — |
| [[SW48 (line)]] | wt | 72.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 15 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf61]] ⚠ | +0.63 | +0.40 / +0.61 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARL8A]] | +0.61 | +0.37 / +0.52 | both halves | 7e-05 |  |
| [[UBR2]] | +0.60 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[DSTYK]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.59 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[MALSU1]] | +0.58 | +0.22 / +0.60 | both halves | 6e-04 |  |
| [[RAB40C]] | +0.57 | +0.24 / +0.49 | both halves | 5e-04 |  |
| [[VPS37D]] | +0.57 | +0.27 / +0.52 | both halves | 3e-04 |  |
| [[KIF13A]] | +0.57 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[THAP3]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[YY1]] | +0.57 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[FAM193B]] | +0.56 | +0.32 / +0.40 | both halves | 2e-04 |  |
| [[CAPN7]] | +0.56 | +0.36 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC4]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[SPTLC1]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[SSU72]] | -0.56 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[DHFR]] | -0.54 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[LY6G5B]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PSME3]] | -0.52 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[DPY19L3-DT]] | -0.52 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[ARF3]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TM9SF3]] | -0.52 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NRAS]] | -0.52 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[CA5BP1-1]] | -0.52 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[NUP188]] | -0.51 | -0.39 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K21]] | B | MAP3K21 activity lowers TENT4B's level | lines that do not express MAP3K21 (11) vs lines expressing it (39) | 1.23× higher at baseline in the lines without MAP3K21 | 0.090 | ⚠ within organs, on part of the lines; also absent: PRSS16, KRT8, CHMP4C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.1, -17.1); signed map (-22.5, 5.3). **Vector** length 80.8, 21.6% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.7 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.4 | +6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +2.9 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +13.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +5.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -4.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.4 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.0 | -0.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.9 | -1.4 |
|  | [[Ivermectin (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Ivermectin (drug)]] 0.5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | terminal nucleotidyltransferase 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:50,152,911-50,235,310 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRF4-2, TUT3; previously PAPD5 |
| Gene groups (HGNC) | Non-canonical poly(A) polymerases; Terminal nucleotidyltransferases |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDF8](https://www.uniprot.org/uniprotkb/Q8NDF8) (Terminal nucleotidyltransferase 4B):

> Terminal nucleotidyltransferase that catalyzes preferentially the transfer of ATP and GTP on RNA 3' poly(A) tail creating a heterogeneous 3' poly(A) tail leading to mRNAs stabilization by protecting mRNAs from active deadenylation. Also functions as a catalytic subunit of a TRAMP-like complex which has a poly(A) RNA polymerase activity and is involved in a post-transcriptional quality control mechanism. Polyadenylation with short oligo(A) tails is required for the degradative activity of the …

**Summary**, from NCBI Gene [64282](https://www.ncbi.nlm.nih.gov/gene/64282):

> Enables guanylyltransferase activity; poly(A) RNA polymerase activity; and telomerase RNA binding activity. Involved in several processes, including RNA metabolic process; negative regulation of telomere maintenance via telomerase; and regulation of mRNA stability. Located in cytosol and nucleolus. Part of TRAMP complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30758) · Entrez [64282](https://www.ncbi.nlm.nih.gov/gene/64282) · UniProt [Q8NDF8](https://www.uniprot.org/uniprotkb/Q8NDF8) · Ensembl [ENSG00000121274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121274)

## Data

Gene col 4262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4262); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4262]; `tensor/DDL_lfc|DDL_z.npy` [4262]; `embed/gene_vectors.npy` [4262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4262 or target_col == 4262). Every well: [[TENT4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENT4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

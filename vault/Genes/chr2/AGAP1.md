---
symbol: "AGAP1"
type: "gene"
col: 8120
ensembl_id: "ENSG00000157985"
name: "ArfGAP with GTPase domain, ankyrin repeat and PH domain 1"
location: "2q37.2"
module: 134
arm: "+"
pooled_cpm: 692.4
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# AGAP1

*ArfGAP with GTPase domain, ankyrin repeat and PH domain 1* — 2q37.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.281× (z -33.8, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE28]] (+0.60, fdr 3e-05), [[HK1]] (+0.59, fdr 1e-05), [[SMYD3]] (+0.59, fdr 2e-05); moves opposite to [[MR1]] (-0.58, fdr 6e-05), [[ACCS]] (-0.56, fdr 6e-05), [[BTN2A1]] (-0.55, fdr 4e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | 1.42× | +3.5 | 0.28 | 30/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.55 | 20/48 (SW48, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8120.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.281×** | -33.8 | 0e+00 | 45/48 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.274×** | -23.5 | 0e+00 | 46/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.322×** | -20.5 | 0e+00 | 43/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.325×** | -20.4 | 0e+00 | 47/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.322×** | -19.0 | 0e+00 | 48/49 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.394×** | -17.5 | 0e+00 | 45/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.369×** | -17.4 | 0e+00 | 44/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.526×** | -17.1 | 0e+00 | 47/49 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.518×** | -12.4 | 2e-33 | 41/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.570×** | -10.6 | 2e-24 | 37/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.560×** | -10.5 | 6e-24 | 36/47 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.560×** | -9.7 | 1e-20 | 38/48 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.577×** | -9.2 | 1e-18 | 45/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -7.1 | 7e-11 | 37/50 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.689×** | -7.0 | 1e-10 | 38/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **0.772×** | -6.9 | 2e-10 | 33/48 (A-172, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -6.8 | 4e-10 | 34/48 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.709×** | -6.5 | 3e-09 | 36/48 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.720×** | -6.2 | 2e-08 | 34/48 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.776×** | -4.4 | 3e-04 | 36/47 (LOX-IMVI, J82, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.798×** | -4.2 | 5e-04 | 27/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.816×** | -3.8 | 0.003 | 24/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.798×** | -3.7 | 0.003 | 29/48 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 679 | 0 | 20 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -41.4) |
| [[LOX-IMVI (line)]] | wt | 536 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -38.2) |
| [[NCI-H460 (line)]] | wt | 1,174 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -42.1) |
| [[PANC-1 (line)]] | alt | 599 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -40.1) |
| [[HOP62 (line)]] | alt | 985 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -35.2) |
| [[A-172 (line)]] | wt | 570 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -31.9) |
| [[SK-MEL-2 (line)]] | alt | 633 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -46.8) |
| [[SNU-423 (line)]] | alt | 944 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -30.4) |
| [[A-427 (line)]] | wt | 516 | 0 | 14 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -31.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.196× (z -26.0) |
| [[MIA PaCa-2 (line)]] | alt | 712 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -29.7) |
| [[NCI-H1792 (line)]] | alt | 1,200 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -39.7) |
| [[C-33 A (line)]] | alt | 726 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -17.3) |
| [[KATO III (line)]] | alt | 839 | 0 | 13 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -23.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 815 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -35.9) |
| [[HT-29 (line)]] | alt | 1,018 | 0 | 12 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.170× (z -23.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.469× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 596 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -25.6) |
| [[SNU-1 (line)]] | wt | 796 | 0 | 12 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -26.4) |
| [[SW 900 (line)]] | alt | 556 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -23.5) |
| [[A549 (line)]] | wt | 637 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -38.2) |
| [[LoVo (line)]] | wt | 617 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -22.7) |
| [[NCI-H1573 (line)]] | alt | 763 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -43.0) |
| [[NCI-H23 (line)]] | alt | 796 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0922× (z -37.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -29.5) |
| [[SW480 (line)]] | alt | 546 | 0 | 11 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.278× (z -24.6) |
| [[J82 (line)]] | alt | 471 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -26.5) |
| [[RKO (line)]] | wt | 617 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -32.3) |
| [[CFPAC-1 (line)]] | alt | 544 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -18.2) |
| [[HS-578T (line)]] | alt | 556 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -29.8) |
| [[NCI-H2030 (line)]] | alt | 535 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -29.9) |
| [[AN3 CA (line)]] | alt | 599 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.294× (z -13.5) |
| [[H4 (line)]] | wt | 544 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -27.3) |
| [[Panc 03.27 (line)]] | alt | 664 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -12.0) |
| [[SW 1271 (line)]] | alt | 695 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.5) |
| [[SW1417 (line)]] | alt | 938 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.191× (z -22.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -17.7) |
| [[SW48 (line)]] | wt | 810 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -26.5) |
| [[HEC-1-A (line)]] | alt | 862 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -18.3) |
| [[Hs 766T (line)]] | wt | 257 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -21.8) |
| [[HCT15 (line)]] | alt | 917 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.498× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 798 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.186× (z -20.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.549× (z -10.5) |
| [[A498 (line)]] | wt | 538 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -10.5) |
| [[CHP-212 (line)]] | wt | 414 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -21.3) |
| [[LS 180 (line)]] | wt | 1,165 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.467× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 478 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -11.7) |
| [[BT-474 (line)]] | alt | 731 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -17.0) |
| [[COLO 205 (line)]] | alt | 623 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.391× (z -13.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.438× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 297 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -15.0) |
| [[SHP-77 (line)]] | alt | 448 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.517× (z -11.0) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 780 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.3) |
| [[NCI-H2122 (line)]] | alt | 699 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 699 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 222 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE28]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[HK1]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SMYD3]] | +0.59 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[MGAT5]] | +0.57 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CMIP]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[GMDS]] | +0.55 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[ADARB1]] | +0.54 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[NAA10]] ⚠ | +0.54 | +0.34 / +0.41 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[KIAA1958]] | +0.54 | +0.63 / +0.31 | both halves | 2e-04 |  |
| [[SNX25]] | +0.53 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[TRAPPC9]] | +0.53 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[ARFGEF3]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[SLC2A13]] | +0.53 | +0.50 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MR1]] | -0.58 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[ACCS]] | -0.56 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[BTN2A1]] | -0.55 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[FBXO8]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ZNF226]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[CCNT2]] | -0.53 | -0.54 / -0.24 | both halves | 5e-04 |  |
| [[RNF146]] | -0.52 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[PLEKHF2]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[C3orf38]] | -0.51 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[RAB21]] | -0.51 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[RBM48]] | -0.50 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[ZNF44]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity raises AGAP1's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLCO4A1]] | B | SLCO4A1 activity raises AGAP1's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without SLCO4A1 | 0.086 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[ADARB1]] | C | ADARB1 activity strengthens AGAP1's drug response | lines that do not express ADARB1 (4) vs lines expressing it (45) | the lines without ADARB1 respond 0.80× as strongly (z diff +2.06); strongest at Homoharringtonine 5 µM: 0.56x vs 0.28x (z diff +6.6) | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC16A1-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.0, 14.6); signed map (-38.9, 28.8). **Vector** length 98.4, 45.5% of its response variance represented; |z| ≥ 3 in 1,672 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.8 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +5.8 | -4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +5.7 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +5.1 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | -0.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | -0.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.2 | -6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.1 | -20.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.0 | -9.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -17.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -1.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.3 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with GTPase domain, ankyrin repeat and PH domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.2 — chr2:235,494,043-236,131,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1099, GGAP1; previously CENTG2 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPQ3](https://www.uniprot.org/uniprotkb/Q9UPQ3) (Arf-GAP with GTPase, ANK repeat and PH domain-containing protein 1):

> GTPase-activating protein for ARF1 and, to a lesser extent, ARF5. Directly and specifically regulates the adapter protein 3 (AP-3)-dependent trafficking of proteins in the endosomal-lysosomal system.

**Summary**, from NCBI Gene [116987](https://www.ncbi.nlm.nih.gov/gene/116987):

> This gene encodes a member of an ADP-ribosylation factor GTPase-activating protein family involved in membrane trafficking and cytoskeleton dynamics. This gene functions as a direct regulator of the adaptor-related protein complex 3 on endosomes. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:16922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16922) · Entrez [116987](https://www.ncbi.nlm.nih.gov/gene/116987) · UniProt [Q9UPQ3](https://www.uniprot.org/uniprotkb/Q9UPQ3) · Ensembl [ENSG00000157985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157985)

## Data

Gene col 8120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8120); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8120]; `tensor/DDL_lfc|DDL_z.npy` [8120]; `embed/gene_vectors.npy` [8120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8120 or target_col == 8120). Every well: [[AGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

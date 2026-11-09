---
symbol: "MYO1E"
type: "gene"
col: 8075
ensembl_id: "ENSG00000157483"
name: "myosin IE"
location: "15q22.2"
module: 113
arm: "+"
pooled_cpm: 735.32
n_lines_expressing: 45
n_dd_up: 1
n_dd_down: 40
n_dd_up_clean: 1
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 17
direction_downstream: 33
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# MYO1E

*myosin IE* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.24× (z +3.8, q 0.071, up in 24 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 1.63×).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -15.1, q 0e+00, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASL]] (+0.62, fdr 3e-05), [[ZSWIM6]] (+0.61, fdr 1e-05), [[JPT1]] (+0.60, fdr 2e-05); moves opposite to [[UNC50]] (-0.55, fdr 3e-05), [[RAB11FIP2]] (-0.55, fdr 5e-05), [[GPRASP1]] (-0.54, fdr 3e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[LAMA3]] → it (grade B ⚠); 33 go from it, the strongest it → [[USP46]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8075.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 1.63×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.071 | 24/42 (NCI-H460, AsPC-1, …) | two highest doses | low cells (technical?) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.53 | 14/43 (A-172, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8075.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -15.1 | 0e+00 | 34/44 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.424×** | -15.0 | 0e+00 | 41/43 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.549×** | -14.8 | 0e+00 | 35/43 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.435×** | -14.0 | 2e-42 | 39/42 (HepG2/C3A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.459×** | -13.6 | 4e-40 | 42/44 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.450×** | -13.4 | 3e-39 | 35/39 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.461×** | -13.0 | 6e-37 | 36/43 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.480×** | -12.9 | 6e-36 | 40/43 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -12.8 | 1e-35 | 41/43 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.486×** | -12.1 | 4e-32 | 41/42 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.431×** | -11.5 | 1e-28 | 36/40 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.536×** | -10.9 | 5e-26 | 37/43 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -7.5 | 3e-12 | 33/43 (RPMI-7951, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.747×** | -7.2 | 3e-11 | 26/43 (NCI-H1792, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -7.1 | 5e-11 | 35/43 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -6.8 | 5e-10 | 38/44 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.685×** | -6.6 | 1e-09 | 37/43 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.751×** | -4.7 | 6e-05 | 26/43 (LS 180, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.782×** | -4.3 | 4e-04 | 29/43 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.782×** | -4.1 | 9e-04 | 22/43 (NCI-H1792, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -4.0 | 0.001 | 24/43 (CFPAC-1, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 1,938 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -18.9) |
| [[NCI-H1792 (line)]] | alt | 951 | 0 | 15 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -19.7) |
| [[A549 (line)]] | wt | 1,814 | 0 | 14 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -23.4) |
| [[C32 (line)]] | wt | 674 | 0 | 14 (8 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.225× (z -18.0) |
| [[HOP62 (line)]] | alt | 473 | 0 | 14 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.346× (z -13.5) |
| [[J82 (line)]] | alt | 617 | 0 | 13 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.462× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 786 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -18.2) |
| [[A-172 (line)]] | wt | 355 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -23.0) |
| [[AsPC-1 (line)]] | alt | 972 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -20.8) |
| [[NCI-H1573 (line)]] | alt | 1,257 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -20.6) |
| [[PANC-1 (line)]] | alt | 548 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 759 | 0 | 12 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.318× (z -14.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.468× (z -14.0) |
| [[LoVo (line)]] | wt | 2,514 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.9) |
| [[CFPAC-1 (line)]] | alt | 1,894 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -22.0) |
| [[HS-578T (line)]] | alt | 433 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -16.1) |
| [[SNU-423 (line)]] | alt | 504 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -20.3) |
| [[SW1417 (line)]] | alt | 975 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -18.0) |
| [[A498 (line)]] | wt | 758 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.9) |
| [[HepG2_C3A (line)]] | wt | 717 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -19.4) |
| [[HT-29 (line)]] | alt | 1,394 | 0 | 8 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.205× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 324 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.407× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 438 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -25.5) |
| [[Panc 03.27 (line)]] | alt | 1,200 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -17.5) |
| [[COLO 205 (line)]] | alt | 1,675 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.3) |
| [[SW 900 (line)]] | alt | 464 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -11.6) |
| [[SW480 (line)]] | alt | 424 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.63× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.1) |
| [[Hs 766T (line)]] | wt | 350 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 515 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -14.4) |
| [[C-33 A (line)]] | alt | 276 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 597 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.8) |
| [[KATO III (line)]] | alt | 719 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 303 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.461× (z -10.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 360 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.374× (z -12.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -9.0) |
| [[SW48 (line)]] | wt | 316 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -9.1) |
| [[CHP-212 (line)]] | wt | 332 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.173× (z -11.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.9) |
| [[H4 (line)]] | wt | 246 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.276× (z -12.2) |
| [[HCT15 (line)]] | alt | 464 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 471 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.466× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 258 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.388× (z -10.0) |
| [[A-427 (line)]] | wt | 114 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 173 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 379 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1,400 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 175 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 680 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 46.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 317 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 537 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASL]] | +0.62 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[ZSWIM6]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[JPT1]] | +0.60 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[KIF13B]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[RHPN2]] | +0.57 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[LMCD1]] | +0.57 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[ARIH1]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ADRB2]] | +0.56 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[EZR]] | +0.55 | +0.50 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[PDLIM5]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[PSEN1]] | +0.55 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SERPINB1]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC50]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RAB11FIP2]] | -0.55 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[GPRASP1]] | -0.54 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[MYLK-AS1]] | -0.52 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[THBS4]] | -0.51 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[MTPAP]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[POMK]] | -0.51 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TSSK3]] | -0.51 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[ATXN2L]] | -0.50 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[ZBED3]] | -0.50 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[OTUD4]] | -0.50 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[ABHD13]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA3]] | B | LAMA3 activity raises MYO1E's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.60× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[LINC00511]] | B | LINC00511 activity raises MYO1E's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 2.90× lower at baseline in the lines without LINC00511 | 0.002 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[TMEM92]] | B | TMEM92 activity raises MYO1E's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without TMEM92 | 0.003 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[GPRC5A]] | B | GPRC5A activity raises MYO1E's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.52× lower at baseline in the lines without GPRC5A | 0.005 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[ABTB2]] | B | ABTB2 activity raises MYO1E's level | lines that do not express ABTB2 (7) vs lines expressing it (43) | 3.32× lower at baseline in the lines without ABTB2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ZNF341-AS1, ENSG00000283511, CD59; maybe low, not absent |
| [[CDH1]] | B | CDH1 activity raises MYO1E's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.54× lower at baseline in the lines without CDH1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[FA2H]] | B | FA2H activity raises MYO1E's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without FA2H | 0.012 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[CLMN]] | B | CLMN activity raises MYO1E's level | lines that do not express CLMN (7) vs lines expressing it (43) | 3.03× lower at baseline in the lines without CLMN | 0.012 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[LINC00511]] | B | LINC00511 activity strengthens MYO1E's drug response | lines that do not express LINC00511 (8) vs lines expressing it (36) | the lines without LINC00511 respond 0.53× as strongly (z diff +3.38); strongest at Idarubicin (hydrochloride) 5 µM: 1.09x vs 0.48x (z diff +8.7) | 0.014 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18; target measured in part of the lines; artifact flags |
| [[TBC1D8]] | B | TBC1D8 activity raises MYO1E's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 2.49× lower at baseline in the lines without TBC1D8 | 0.032 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[KRT19]] | B | KRT19 activity raises MYO1E's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without KRT19 | 0.049 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[SERPINB1]] | B | SERPINB1 activity raises MYO1E's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.62× lower at baseline in the lines without SERPINB1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 32, C 1. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP46]] | B | MYO1E activity lowers USP46's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.06× higher at baseline in the lines without MYO1E | 0.006 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[OXSR1]] | B | MYO1E activity raises OXSR1's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without MYO1E | 0.011 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[GPRC5A]] | B | MYO1E activity raises GPRC5A's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 4.74× lower at baseline in the lines without MYO1E | 0.011 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[SERPINB1]] | B | MYO1E activity raises SERPINB1's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 5.76× lower at baseline in the lines without MYO1E | 0.013 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[EHD4]] | B | MYO1E activity raises EHD4's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without MYO1E | 0.014 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[TBC1D8]] | B | MYO1E activity raises TBC1D8's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without MYO1E | 0.016 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[ABTB2]] | B | MYO1E activity raises ABTB2's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 3.05× lower at baseline in the lines without MYO1E | 0.019 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[AKAP13]] | B | MYO1E activity raises AKAP13's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without MYO1E | 0.019 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[CLMN]] | B | MYO1E activity raises CLMN's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 3.18× lower at baseline in the lines without MYO1E | 0.021 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[DUSP5]] | B | MYO1E activity raises DUSP5's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.62× lower at baseline in the lines without MYO1E | 0.024 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[TSSK3]] | B | MYO1E activity lowers TSSK3's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.52× higher at baseline in the lines without MYO1E | 0.025 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[VCL]] | B | MYO1E activity raises VCL's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without MYO1E | 0.028 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.7, 28.0); signed map (1.6, 25.3). **Vector** length 117, 46.6% of its response variance represented; |z| ≥ 3 in 1,652 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +6.4 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +1.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.4 | +2.1 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -8.7 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.3 | -7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -13.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -5.5 | -3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -4.0 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | myosin IE |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:59,132,434-59,372,871 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MYO1C, HuncM-IC, MGC104638 |
| Gene groups (HGNC) | Myosin heavy chains, class I; MicroRNA protein coding host genes; SH3 domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12965](https://www.uniprot.org/uniprotkb/Q12965) (Unconventional myosin-Ie):

> Actin-based motor molecule with ATPase activity. Unconventional myosins serve in intracellular movements. Their highly divergent tails bind to membranous compartments, which are then moved relative to actin filaments. Binds to membranes containing anionic phospholipids via its tail domain. Involved in clathrin-mediated endocytosis and intracellular movement of clathrin-coated vesicles. Required for normal morphology of the glomerular basement membrane, normal development of foot processes by …

**Summary**, from NCBI Gene [4643](https://www.ncbi.nlm.nih.gov/gene/4643):

> This gene encodes a member of the nonmuscle class I myosins which are a subgroup of the unconventional myosin protein family. The unconventional myosin proteins function as actin-based molecular motors. Class I myosins are characterized by a head (motor) domain, a regulatory domain and a either a short or long tail domain. Among the class I myosins, this protein is distinguished by a long tail domain that is involved in crosslinking actin filaments. This protein localizes to the cytoplasm and …

**Accessions** — [HGNC:7599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7599) · Entrez [4643](https://www.ncbi.nlm.nih.gov/gene/4643) · UniProt [Q12965](https://www.uniprot.org/uniprotkb/Q12965) · Ensembl [ENSG00000157483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157483)

## Data

Gene col 8075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8075); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8075]; `tensor/DDL_lfc|DDL_z.npy` [8075]; `embed/gene_vectors.npy` [8075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8075 or target_col == 8075). Every well: [[MYO1E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO1E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

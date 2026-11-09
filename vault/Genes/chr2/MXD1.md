---
symbol: "MXD1"
type: "gene"
col: 677
ensembl_id: "ENSG00000059728"
name: "MAX dimerization protein 1"
location: "2p13.3"
module: 1
arm: "-"
pooled_cpm: 123.1
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MXD1

*MAX dimerization protein 1* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.36× (z +15.8, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.713× (z -4.4, q 0.004, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H2347 0.218×, CFPAC-1 0.218×, SK-MEL-2 0.178×, AsPC-1 0.295×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2347 0.175×, CFPAC-1 0.313×, AsPC-1 0.320×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.218×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 0.261×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H2347 0.355×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H2347 0.382×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPLA8]] (+0.68, fdr 7e-06), [[ATG9B]] (+0.64, fdr 7e-06), [[RIOK3]] (+0.63, fdr 7e-06); moves opposite to [[ABCE1]] (-0.72, fdr 7e-06), [[LTV1]] (-0.71, fdr 7e-06), [[ZZZ3]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RNF39]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +15.8 | 0e+00 | 43/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.67×** | +12.8 | 7e-35 | 44/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +10.7 | 8e-25 | 44/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.28×** | +10.7 | 8e-25 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +10.7 | 8e-25 | 44/48 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +9.4 | 5e-19 | 40/48 (HT-29, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +9.4 | 5e-19 | 43/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +8.0 | 7e-14 | 43/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +7.8 | 4e-13 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.81×** | +7.7 | 7e-13 | 41/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.5 | 3e-12 | 39/49 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +7.3 | 2e-11 | 35/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +7.0 | 8e-11 | 38/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.61×** | +6.5 | 3e-09 | 45/49 (NCI-H460, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +6.5 | 3e-09 | 41/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +6.0 | 7e-08 | 34/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 677.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H2347 0.218×, CFPAC-1 0.218×, SK-MEL-2 0.178×, AsPC-1 0.295×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2347 0.175×, CFPAC-1 0.313×, AsPC-1 0.320×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.218×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 0.261×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H2347 0.355×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H2347 0.382×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.713×** | -4.4 | 0.004 | 31/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -4.3 | 0.004 | 2/50 (NCI-H1792, SW 1088) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.724×** | -4.2 | 0.005 | 30/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.750×** | -3.6 | 0.046 | 23/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.628× | -3.2 | 0.17 | 20/48 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.780× | -3.1 | 0.17 | 19/43 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.0 | 0.21 | 18/48 (CFPAC-1, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.6 | 15 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +21.4) | — |
| [[PANC-1 (line)]] | alt | 58.8 | 14 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +16.5) | — |
| [[A549 (line)]] | wt | 84.1 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +15.8) | — |
| [[LoVo (line)]] | wt | 111 | 7 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.38× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +12.4) | [[Tucidinostat (drug)]] 5 µM 0.544× (z -8.9) |
| [[A-172 (line)]] | wt | 74.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 56.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 125 | 7 | 0 | [[Auranofin (drug)]] 5 µM 3.56× (z +12.8) | — |
| [[KATO III (line)]] | alt | 90.3 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +18.3) | — |
| [[NCI-H2347 (line)]] | alt | 328 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.355× (z -9.3) |
| [[SW480 (line)]] | alt | 148 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +13.3) | — |
| [[A-427 (line)]] | wt | 63.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 145 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.84× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 66.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 138 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.37× (z +14.2) | — |
| [[J82 (line)]] | alt | 59.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 499 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 319 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -12.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 75.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 76.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 141 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 117 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.1) | — |
| [[RKO (line)]] | wt | 110 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 71.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.8) | — |
| [[A498 (line)]] | wt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +14.4) | — |
| [[C32 (line)]] | wt | 55.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +15.3) | — |
| [[COLO 205 (line)]] | alt | 231 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.98× (z +11.4) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 55.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 134 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +9.6) | — |
| [[SW48 (line)]] | wt | 49.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 87.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 58.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 66.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 195 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 99.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 377 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPLA8]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ATG9B]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RIOK3]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[JUP]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DEDD2]] | +0.62 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[UBE2H]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CSTB]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[CRIPT]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CALCOCO1]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[WASF2]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FA2H]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |

## Genes that move opposite

*69 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCE1]] | -0.72 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[LTV1]] | -0.71 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[ZZZ3]] | -0.66 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[NAA15]] | -0.65 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[URB2]] | -0.64 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[CEP83]] | -0.64 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.63 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[MDN1]] | -0.63 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[TCERG1]] | -0.63 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[UTP20]] | -0.62 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[XPO4]] | -0.62 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[POLR1A]] | -0.61 | -0.60 / -0.68 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF39]] | B | RNF39 activity raises MXD1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without RNF39 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[IRF6]] | B | IRF6 activity raises MXD1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without IRF6 | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MPZL3]] | B | MPZL3 activity raises MXD1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without MPZL3 | 0.007 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[BARX2]] | B | BARX2 activity raises MXD1's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without BARX2 | 0.027 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[TMCC3]] | B | TMCC3 activity raises MXD1's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without TMCC3 | 0.051 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[ADAM8]] | B | ADAM8 activity raises MXD1's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without ADAM8 | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[KCNK1]] | B | KCNK1 activity raises MXD1's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without KCNK1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.6, -36.4); signed map (-23.4, 13.5). **Vector** length 102, 37.2% of its response variance represented; |z| ≥ 3 in 1,370 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +9.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +12.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +10.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.0 | +10.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +7.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.1 | -4.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | +7.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | MAX dimerization protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:69,897,688-69,942,945 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAD1, bHLHc58; previously MAD |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; MAX dimerization proteins |
| Hallmark sets | INFLAMMATORY_RESPONSE, IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05195](https://www.uniprot.org/uniprotkb/Q05195) (Max dimerization protein 1):

> Component of a transcriptional repressor complex together with MAX. In complex with MAX binds to the core DNA sequence 5'-CAC[GA]TG-3'. Antagonizes MYC transcriptional activity by competing with MYC for MAX binding. Binds to the TERT promoter and represses telomerase expression, possibly by interfering with MYC binding.

**Summary**, from NCBI Gene [4084](https://www.ncbi.nlm.nih.gov/gene/4084):

> This gene encodes a member of the MYC/MAX/MAD network of basic helix-loop-helix leucine zipper transcription factors. The MYC/MAX/MAD transcription factors mediate cellular proliferation, differentiation and apoptosis. The encoded protein antagonizes MYC-mediated transcriptional activation of target genes by competing for the binding partner MAX and recruiting repressor complexes containing histone deacetylases. Mutations in this gene may play a role in acute leukemia, and the encoded protein …

**Accessions** — [HGNC:6761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6761) · Entrez [4084](https://www.ncbi.nlm.nih.gov/gene/4084) · UniProt [Q05195](https://www.uniprot.org/uniprotkb/Q05195) · Ensembl [ENSG00000059728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059728)

## Data

Gene col 677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 677); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 677]; `tensor/DDL_lfc|DDL_z.npy` [677]; `embed/gene_vectors.npy` [677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 677 or target_col == 677). Every well: [[MXD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MXD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

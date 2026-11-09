---
symbol: "SQSTM1"
type: "gene"
col: 8408
ensembl_id: "ENSG00000161011"
name: "sequestosome 1"
location: "5q35.3"
module: 93
arm: "+"
pooled_cpm: 486.59
n_lines_expressing: 49
n_dd_up: 40
n_dd_down: 11
n_dd_up_clean: 32
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# SQSTM1

*sequestosome 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.39× (z +36.8, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.684× (z -5.5, q 3e-05, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMOX1]] (+0.62, fdr 7e-06), [[WBP2]] (+0.62, fdr 1e-05), [[PPP1R15A]] (+0.60, fdr 1e-05); moves opposite to [[ZHX3]] (-0.62, fdr 7e-06), [[MCMBP]] (-0.58, fdr 1e-05), [[AUNIP]] (-0.58, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.39×** | +36.8 | 0e+00 | 47/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.24×** | +23.9 | 0e+00 | 47/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.92×** | +22.1 | 0e+00 | 47/47 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.94×** | +15.6 | 0e+00 | 44/47 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.91×** | +15.4 | 0e+00 | 44/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +13.5 | 2e-39 | 47/47 (Panc 03.27, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +13.2 | 6e-38 | 45/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.42×** | +12.8 | 2e-35 | 46/47 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.38×** | +12.5 | 3e-34 | 45/47 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.22×** | +10.9 | 7e-26 | 46/47 (HEC-1-A, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.10×** | +10.7 | 6e-25 | 42/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.05×** | +10.3 | 2e-23 | 42/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +9.3 | 6e-19 | 43/46 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.87×** | +9.1 | 5e-18 | 42/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.7 | 1e-09 | 33/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +5.9 | 1e-07 | 30/47 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 2e-04 | 32/47 (J82, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.55×** | +4.5 | 2e-04 | 39/48 (HEC-1-A, H4, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.684×** | -5.5 | 3e-05 | 39/47 (SW 900, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.724×** | -4.7 | 9e-04 | 33/47 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.728×** | -4.6 | 9e-04 | 33/47 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.742×** | -4.3 | 0.002 | 31/47 (NCI-H1573, SW 900, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.744×** | -4.3 | 0.002 | 29/47 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.745×** | -4.2 | 0.002 | 32/47 (A549, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.746×** | -4.2 | 0.002 | 27/47 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.748×** | -4.2 | 0.002 | 30/47 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.739×** | -4.0 | 0.003 | 29/46 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.765×** | -3.9 | 0.006 | 29/47 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.805×** | -3.1 | 0.092 | 26/47 (HT-29, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 439 | 19 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +38.0) | — |
| [[KATO III (line)]] | alt | 385 | 15 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +28.5) | — |
| [[SW480 (line)]] | alt | 306 | 15 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +18.9) | — |
| [[HS-578T (line)]] | alt | 392 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +25.0) | — |
| [[A-427 (line)]] | wt | 439 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +19.5) | — |
| [[hTERT-HPNE (line)]] | wt | 381 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +29.4) | — |
| [[LOX-IMVI (line)]] | wt | 156 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +27.6) | — |
| [[LS 180 (line)]] | wt | 273 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +27.8) | — |
| [[HEC-1-A (line)]] | alt | 531 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +35.4) | — |
| [[HT-29 (line)]] | alt | 721 | 11 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +29.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.404× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~60% of this change |
| [[LoVo (line)]] | wt | 569 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +38.4) | — |
| [[BT-474 (line)]] | alt | 304 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +20.4) | — |
| [[H4 (line)]] | wt | 525 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +23.2) | — |
| [[HepG2_C3A (line)]] | wt | 365 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +23.5) | — |
| [[SW1417 (line)]] | alt | 595 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +34.1) | — |
| [[J82 (line)]] | alt | 479 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +26.3) | — |
| [[PANC-1 (line)]] | alt | 563 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +31.3) | — |
| [[SNU-1 (line)]] | wt | 534 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +21.4) | — |
| [[SW48 (line)]] | wt | 552 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +24.2) | — |
| [[A-172 (line)]] | wt | 838 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +27.3) | — |
| [[C32 (line)]] | wt | 281 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +37.0) | — |
| [[CFPAC-1 (line)]] | alt | 458 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +30.6) | — |
| [[Panc 03.27 (line)]] | alt | 745 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +30.5) | — |
| [[RPMI-7951 (line)]] | alt | 360 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +23.7) | — |
| [[A498 (line)]] | wt | 401 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +25.2) | — |
| [[A549 (line)]] | wt | 424 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +28.9) | — |
| [[HOP62 (line)]] | alt | 274 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +25.0) | — |
| [[NCI-H1573 (line)]] | alt | 332 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +27.5) | [[Dexamethasone (drug)]] 0.5 µM 0.299× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 877 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +26.6) | — |
| [[SNU-423 (line)]] | alt | 678 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +25.4) | — |
| [[SW 900 (line)]] | alt | 1,373 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +20.0) | — |
| [[NCI-H1792 (line)]] | alt | 397 | 7 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.90× (z +19.0) | — |
| [[NCI-H23 (line)]] | alt | 271 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +23.2) | — |
| [[SHP-77 (line)]] | alt | 184 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.79× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 884 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 561 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +31.1) | — |
| [[HCT15 (line)]] | alt | 416 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.90× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 551 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +26.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 648 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +23.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.479× (z -8.9) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 851 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +25.3) | — |
| [[NCI-H2030 (line)]] | alt | 374 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +30.8) | — |
| [[RKO (line)]] | wt | 306 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +17.5) | — |
| [[CHP-212 (line)]] | wt | 347 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +10.6) | — |
| [[SW 1271 (line)]] | alt | 614 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +17.0) | — |
| [[AN3 CA (line)]] | alt | 408 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +21.4) | — |
| [[SW 1088 (line)]] | alt | 365 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +16.9) | — |
| [[C-33 A (line)]] | alt | 121 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 544 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 466 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 273 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMOX1]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS; STRING 684 |
| [[WBP2]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[PPP1R15A]] | +0.60 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[JUN]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 589 |
| [[OSGIN1]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ATF3]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 522 |
| [[LITAF]] | +0.55 | +0.46 / +0.62 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[RNF103-CHMP3]] | +0.55 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[GABARAPL1]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 | pathway: Autophagy; STRING 999 |
| [[LYST]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.54 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SDCBP]] | +0.53 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZHX3]] | -0.62 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[MCMBP]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[AUNIP]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PDSS1]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ERI1]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[RANBP1]] | -0.54 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[NUP93]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MFSD14CP]] | -0.52 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PPIH]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[DSCC1]] | -0.51 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RAD51]] | -0.50 | -0.48 / -0.53 | both halves | 2e-05 | STRING 839 |
| [[ARMC8]] | -0.50 | -0.41 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers SQSTM1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 1.7% of all compounds | 0.014 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.336). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.6, 5.1); signed map (4.2, 20.4). **Vector** length 140, 57.5% of its response variance represented; |z| ≥ 3 in 1,998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.8 | +15.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +13.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +12.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +10.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +10.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +4.4 | +2.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -10.1 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.8 | -5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | -8.2 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.0 | -0.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -5.3 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.8 | -4.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.8 | -4.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.8 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | sequestosome 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,806,398-179,838,078 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p62, p60, p62B, A170; previously PDB3, OSIL |
| Gene groups (HGNC) | Zinc fingers ZZ-type |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, APOPTOSIS, UV_RESPONSE_UP, TNFA_SIGNALING_VIA_NFKB, MTORC1_SIGNALING |
| Reactome | 26 pathways, smallest: Pexophagy; NF-kB is activated and signals survival; p75NTR recruits signalling complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13501](https://www.uniprot.org/uniprotkb/Q13501) (Sequestosome-1):

> Molecular adapter required for selective macroautophagy (aggrephagy) by acting as a bridge between polyubiquitinated proteins and autophagosomes. Promotes the recruitment of ubiquitinated cargo proteins to autophagosomes via multiple domains that bridge proteins and organelles in different steps. SQSTM1 first mediates the assembly and removal of ubiquitinated proteins by undergoing liquid-liquid phase separation upon binding to ubiquitinated proteins via its UBA domain, leading to the formation …

**Summary**, from NCBI Gene [8878](https://www.ncbi.nlm.nih.gov/gene/8878):

> This gene encodes a multifunctional protein that binds ubiquitin and regulates activation of the nuclear factor kappa-B (NF-kB) signaling pathway. The protein functions as a scaffolding/adaptor protein in concert with TNF receptor-associated factor 6 to mediate activation of NF-kB in response to upstream signals. Alternatively spliced transcript variants encoding either the same or different isoforms have been identified for this gene. Mutations in this gene result in sporadic and familial …

**Accessions** — [HGNC:11280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11280) · Entrez [8878](https://www.ncbi.nlm.nih.gov/gene/8878) · UniProt [Q13501](https://www.uniprot.org/uniprotkb/Q13501) · Ensembl [ENSG00000161011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161011)

## Data

Gene col 8408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8408); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8408]; `tensor/DDL_lfc|DDL_z.npy` [8408]; `embed/gene_vectors.npy` [8408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8408 or target_col == 8408). Every well: [[SQSTM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SQSTM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

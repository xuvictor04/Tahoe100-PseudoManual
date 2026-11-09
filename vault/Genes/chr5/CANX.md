---
symbol: "CANX"
type: "gene"
col: 4784
ensembl_id: "ENSG00000127022"
name: "calnexin"
location: "5q35.3"
module: 42
arm: "+"
pooled_cpm: 689.38
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# CANX

*calnexin* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +21.2, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +7.4, q 2e-11, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.762× (z -7.7, q 7e-12, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA3]] (+0.78, fdr 7e-06), [[HYOU1]] (+0.77, fdr 7e-06), [[HDLBP]] (+0.75, fdr 7e-06); moves opposite to [[PPP1R35]] (-0.60, fdr 1e-05, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[ORAI1]] (-0.55, fdr 3e-05), [[KRI1]] (-0.55, fdr 3e-05), [[NSUN5]] (-0.52, fdr 1e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +21.2 | 0e+00 | 49/49 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +19.6 | 0e+00 | 44/44 (A549, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +14.3 | 5e-44 | 44/45 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.4 | 2e-11 | 35/49 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +6.8 | 1e-09 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.4 | 2e-08 | 41/48 (SHP-77, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.5 | 2e-06 | 37/50 (LOX-IMVI, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.002 | 31/48 (A-427, LOX-IMVI, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.23×** | +4.1 | 0.002 | 29/48 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.006 | 36/49 (SW48, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.008 | 25/48 (NCI-H2030, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.7 | 0.012 | 24/48 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.012 | 36/48 (NCI-H1792, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.015 | 26/48 (A-172, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.762×** | -7.7 | 7e-12 | 31/48 (CFPAC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.755×** | -5.4 | 2e-05 | 40/49 (J82, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.772×** | -5.0 | 1e-04 | 36/48 (C-33 A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.781×** | -5.0 | 1e-04 | 37/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.793×** | -4.7 | 4e-04 | 26/48 (SW 900, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.842× | -3.4 | 0.057 | 20/47 (HS-578T, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~2% of this change | 0.846× | -3.2 | 0.10 | 22/47 (KATO III, HCT15, …) | all doses, stronger at high dose |  |
| [[Olanzapine (drug)]] 5 µM |  | 0.893× | -3.2 | 0.10 | 2/48 (SHP-77, SW 1271) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 433 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +19.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.612× (z -10.2) |
| [[HS-578T (line)]] | alt | 1,039 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +8.9) | [[Verteporfin (drug)]] 5 µM 0.474× (z -10.2) |
| [[A-427 (line)]] | wt | 469 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +19.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -10.2) |
| [[C-33 A (line)]] | alt | 373 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +21.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -12.5) |
| [[KATO III (line)]] | alt | 674 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +18.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.641× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 1,047 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +18.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 394 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +19.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.23× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.589× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 429 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +13.1) | — |
| [[C32 (line)]] | wt | 503 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 736 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -13.3) |
| [[H4 (line)]] | wt | 1,472 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 533 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 830 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.5) | — |
| [[J82 (line)]] | alt | 835 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +18.2) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.527× (z -10.9) |
| [[LoVo (line)]] | wt | 772 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.87× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 623 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +17.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.657× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 886 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +15.9) | — |
| [[SW 900 (line)]] | alt | 1,357 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +17.7) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.524× (z -10.0) |
| [[SW48 (line)]] | wt | 603 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +10.3) | — |
| [[A498 (line)]] | wt | 609 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +19.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 540 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +19.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 847 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.637× (z -8.5) |
| [[CHP-212 (line)]] | wt | 551 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +12.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 604 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +15.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 727 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +15.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 625 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.93× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 671 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +13.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 637 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +15.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 454 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +20.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 486 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -10.4) |
| [[PANC-1 (line)]] | alt | 628 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +18.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 508 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +14.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 703 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 699 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 611 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +18.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 531 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +20.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1,104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +11.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 522 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 893 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +10.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 865 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 621 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 910 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +16.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 372 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +14.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 682 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 413 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -8.9) |
| [[RKO (line)]] | wt | 582 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +14.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 558 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 626 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1,030 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 662 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA3]] | +0.78 | +0.74 / +0.79 | both halves | 7e-06 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[HYOU1]] | +0.77 | +0.80 / +0.76 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 869 |
| [[HDLBP]] | +0.75 | +0.73 / +0.80 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication |
| [[TMED2]] | +0.75 | +0.74 / +0.80 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 538 |
| [[RPN1]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 841 |
| [[SEL1L]] | +0.71 | +0.77 / +0.79 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 918 |
| [[PDIA6]] | +0.68 | +0.64 / +0.74 | both halves | 7e-06 | STRING 725 |
| [[DDOST]] | +0.68 | +0.62 / +0.71 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 886 |
| [[OS9]] | +0.68 | +0.69 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 958 |
| [[COPB2]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 459 |
| [[STT3A]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 730 |
| [[LMAN2]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 625 |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R35]] ⚠ | -0.60 | -0.52 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ORAI1]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[KRI1]] | -0.55 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[NSUN5]] | -0.52 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[EID2]] | -0.51 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[TMEM70]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.4, -19.0); signed map (-55.8, 7.5). **Vector** length 157, 60.5% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.61 to 11); *Cargo concentration in the ER* (reactome, mean cos +0.54 to 7); *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.51 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.1 | +1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.5 | +1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +3.4 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~2% of this change | -7.9 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.4 | -5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -6.0 | -2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -5.1 | -1.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -4.5 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -4.4 | -2.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -4.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | calnexin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,678,628-179,731,641 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CNX, IP90, P90 |
| Gene groups (HGNC) | Calnexin/calreticulin family |
| Hallmark sets | MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 35 pathways, smallest: Assembly of Viral Components at the Budding Site; Maturation of spike protein_9683686; Virus Assembly and Release |
| Matched by | ensembl_id |

**Function**, from UniProt [P27824](https://www.uniprot.org/uniprotkb/P27824) (Calnexin):

> Calcium-binding protein that interacts with newly synthesized monoglucosylated glycoproteins in the endoplasmic reticulum. It may act in assisting protein assembly and/or in the retention within the ER of unassembled protein subunits. It seems to play a major role in the quality control apparatus of the ER by the retention of incorrectly folded proteins. Associated with partial T-cell antigen receptor complexes that escape the ER of immature thymocytes, it may function as a signaling complex …

**Summary**, from NCBI Gene [821](https://www.ncbi.nlm.nih.gov/gene/821):

> This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subunits within the ER for degradation. Alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:1473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1473) · Entrez [821](https://www.ncbi.nlm.nih.gov/gene/821) · UniProt [P27824](https://www.uniprot.org/uniprotkb/P27824) · Ensembl [ENSG00000127022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127022)

## Data

Gene col 4784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4784); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4784]; `tensor/DDL_lfc|DDL_z.npy` [4784]; `embed/gene_vectors.npy` [4784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4784 or target_col == 4784). Every well: [[CANX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CANX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

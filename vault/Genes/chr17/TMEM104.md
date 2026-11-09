---
symbol: "TMEM104"
type: "gene"
col: 3022
ensembl_id: "ENSG00000109066"
name: "solute carrier family 38 member 12"
location: "17q25.1"
module: 52
arm: "+"
pooled_cpm: 19.42
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# TMEM104

*solute carrier family 38 member 12* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 5.34× (z +24.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.479× (z -10.2, q 1e-21, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RER1]] (+0.74, fdr 7e-06), [[ATG101]] (+0.73, fdr 7e-06), [[TMEM184B]] (+0.71, fdr 1e-05); moves opposite to [[THOC7]] (-0.65, fdr 1e-05), [[DPH6-DT]] (-0.62, fdr 9e-05), [[RAB21]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **5.34×** | +24.0 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **5.33×** | +24.0 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.13×** | +20.3 | 0e+00 | 47/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +7.8 | 1e-12 | 32/47 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +7.7 | 2e-12 | 29/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +7.2 | 6e-11 | 36/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +6.4 | 1e-08 | 25/46 (SW480, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +5.9 | 3e-07 | 26/47 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +4.3 | 0.001 | 16/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.022 | 11/47 (A498, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.056 | 19/47 (NCI-H1792, NCI-H460, …) | top dose only | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.098 | 5/45 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.098 | 6/48 (LoVo, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3022.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.479×** | -10.2 | 1e-21 | 36/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -9.4 | 2e-18 | 24/39 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.599×** | -7.4 | 3e-11 | 26/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.732×** | -6.3 | 3e-08 | 28/48 (HS-578T, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -5.2 | 3e-05 | 25/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.508×** | -5.1 | 3e-05 | 22/44 (C32, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.739×** | -4.4 | 0.001 | 19/48 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.742×** | -4.3 | 0.001 | 21/48 (AN3 CA, A498, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.755×** | -3.9 | 0.006 | 14/47 (CFPAC-1, RPMI-7951, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.773×** | -3.7 | 0.012 | 18/48 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -3.7 | 0.013 | 13/30 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.780×** | -3.6 | 0.015 | 19/46 (HepG2/C3A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.850× | -3.3 | 0.039 | 15/48 (AsPC-1, HCT15, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.05 µM |  | **0.811×** | -3.0 | 0.092 | 6/47 (SHP-77, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.797×** | -3.0 | 0.092 | 18/46 (A549, HCT15, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 60.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.240× (z -13.7) |
| [[HS-578T (line)]] | alt | 40.2 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.280× (z -13.0) |
| [[A549 (line)]] | wt | 18.5 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.29× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.213× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 17.0 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 10.3× (z +10.8) | [[Menadione (drug)]] 5 µM 0.0600× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 10.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.28× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -11.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 20.0 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 8.22× (z +13.7) | — |
| [[A-427 (line)]] | wt | 23.1 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.68× (z +9.3) | [[Harringtonine (drug)]] 5 µM 0.176× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 20.9 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.64× (z +9.5) | [[Selinexor (drug)]] 5 µM 0.197× (z -12.7) |
| [[KATO III (line)]] | alt | 20.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.20× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 27.6 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.209× (z -13.4) |
| [[SW480 (line)]] | alt | 16.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.76× (z +18.0) | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.24× (z +13.4) | — |
| [[HOP62 (line)]] | alt | 21.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.70× (z +12.9) | — |
| [[J82 (line)]] | alt | 18.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.32× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.182× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.63× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 9.98 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.75× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.88 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 16.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.29× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -12.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 12.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.20× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 26.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.39× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.03× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 11.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 12.9× (z +12.6) | — |
| [[C32 (line)]] | wt | 12.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 6.27× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 7.23 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.66× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 13.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.23× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 11.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.38× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.150× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 13.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.99× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 5.46× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.150× (z -9.1) |
| [[SW 900 (line)]] | alt | 29.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.288× (z -10.2) |
| [[HCT15 (line)]] | alt | 13.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.72× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.160× (z -9.6) |
| [[SW48 (line)]] | wt | 12.3 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0737× (z -9.7) |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RER1]] | +0.74 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[ATG101]] | +0.73 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[TMEM184B]] | +0.71 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[BET1L]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[GAK]] | +0.69 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NAT9]] | +0.69 | +0.60 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[ATAD3B]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[HM13]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[FBXL18]] | +0.67 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[DHDDS]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[YKT6]] | +0.67 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[WIPI1]] | +0.66 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[BLCAP]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC7]] | -0.65 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[DPH6-DT]] | -0.62 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[RAB21]] | -0.61 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[USP24]] | -0.61 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[ZFR]] | -0.60 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ATRX]] | -0.60 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[FAM227B]] | -0.59 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[DHFR2]] | -0.59 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CC2D2A]] | -0.58 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[PATL2]] | -0.58 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[DCUN1D1]] | -0.58 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[U2SURP]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (11.1, -27.4); signed map (-49.5, 4.1). **Vector** length 108, 27.7% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +24.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +24.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +20.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.9 | +2.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.4 | +3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.6 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.6 | -7.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.1 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 38 member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:74,776,499-74,839,753 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20255, FLJ00021; previously TMEM104 |
| Gene groups (HGNC) | Solute carrier family 38 |
| Matched by | ensembl_id |

UniProt [Q8NE00](https://www.uniprot.org/uniprotkb/Q8NE00) carries no function annotation.

**Summary**, from NCBI Gene [54868](https://www.ncbi.nlm.nih.gov/gene/54868):

> Predicted to be involved in amino acid transport and sodium ion transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25984) · Entrez [54868](https://www.ncbi.nlm.nih.gov/gene/54868) · UniProt [Q8NE00](https://www.uniprot.org/uniprotkb/Q8NE00) · Ensembl [ENSG00000109066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109066)

## Data

Gene col 3022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3022); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3022]; `tensor/DDL_lfc|DDL_z.npy` [3022]; `embed/gene_vectors.npy` [3022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3022 or target_col == 3022). Every well: [[TMEM104 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM104.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "INTS14"
type: "gene"
col: 6194
ensembl_id: "ENSG00000138614"
name: "integrator complex subunit 14"
location: "15q22.31"
module: 11
arm: "+"
pooled_cpm: 26.81
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# INTS14

*integrator complex subunit 14* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +26.5, q 0e+00, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.448× (z -19.9, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FIZ1]] (+0.79, fdr 1e-05), [[FEM1A]] (+0.73, fdr 1e-05), [[YJU2]] (+0.73, fdr 3e-05); moves opposite to [[HDAC3]] (-0.69, fdr 1e-05), [[STRN]] (-0.67, fdr 2e-04), [[PDZD7]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +26.5 | 0e+00 | 35/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +8.8 | 3e-16 | 30/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +8.4 | 9e-15 | 1/48 (NCI-H1792) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +7.1 | 2e-10 | 26/48 (LoVo, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +5.9 | 3e-07 | 17/48 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.17× | +5.6 | 2e-06 | 17/48 (HT-29, A549, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +4.7 | 2e-04 | 16/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.003 | 5/47 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.17× | +3.8 | 0.008 | 7/48 (SW 900, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.010 | 13/46 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6194.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.448×** | -19.9 | 0e+00 | 45/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.463×** | -19.1 | 0e+00 | 46/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.497×** | -17.3 | 0e+00 | 45/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.568×** | -14.0 | 1e-42 | 44/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.570×** | -12.9 | 4e-36 | 30/41 (SHP-77, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.717×** | -11.7 | 2e-29 | 32/48 (RKO, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.625×** | -11.7 | 2e-29 | 35/47 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.738×** | -7.3 | 3e-11 | 22/37 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.820×** | -7.0 | 2e-10 | 24/48 (NCI-H460, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.770×** | -6.5 | 4e-09 | 25/48 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.621×** | -6.2 | 3e-08 | 22/48 (RKO, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.787×** | -5.9 | 1e-07 | 19/47 (J82, SNU-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.790×** | -5.9 | 2e-07 | 18/45 (COLO 205, SW1417, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.810×** | -5.0 | 2e-05 | 21/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.843× | -4.3 | 8e-04 | 17/48 (NCI-H460, LS 180, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.902× | -3.6 | 0.011 | 16/48 (A-172, HOP62, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.765×** | -3.5 | 0.017 | 8/48 (CFPAC-1, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tolcapone (drug)]] 5 µM |  | 0.906× | -3.5 | 0.017 | 1/48 (SNU-1) | top dose only | position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.909× | -3.4 | 0.024 | 10/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.785×** | -3.1 | 0.044 | 7/48 (A498, H4, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.887× | -3.0 | 0.072 | 6/48 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.920× | -2.9 | 0.084 | 9/48 (RKO, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.1 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +22.0) | [[Belinostat (drug)]] 5 µM 0.337× (z -12.8) |
| [[RKO (line)]] | wt | 55.7 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.243× (z -14.6) |
| [[HOP62 (line)]] | alt | 21.7 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.8) | [[Belinostat (drug)]] 5 µM 0.336× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 40.2 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.421× (z -9.4) |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.330× (z -10.7) |
| [[SW480 (line)]] | alt | 32.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0870× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H1573 (line)]] | alt | 25.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +25.2) | — |
| [[A498 (line)]] | wt | 25.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.0) | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0717× (z -10.4) |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -11.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 25.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +11.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[J82 (line)]] | alt | 22.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.326× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 35.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -11.6) |
| [[LoVo (line)]] | wt | 38.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 34.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +18.8) | [[Panobinostat (drug)]] 5 µM 0.325× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 25.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -12.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 21.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.301× (z -9.0) |
| [[PANC-1 (line)]] | alt | 27.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -14.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SW 900 (line)]] | alt | 17.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +18.7) | — |
| [[COLO 205 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -12.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SNU-423 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 1 | — | [[Clopidogrel (drug)]] 0.5 µM 0.0599× (z -8.5) |
| [[SW48 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[A-172 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIZ1]] | +0.79 | +0.80 / +0.55 | both halves | 1e-05 |  |
| [[FEM1A]] | +0.73 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[YJU2]] | +0.73 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[ZNF268]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[ZNF689]] | +0.73 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[ZNF507]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[MTHFSD]] | +0.71 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[RPL7L1]] | +0.71 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[NME6]] | +0.71 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[POLR3C]] | +0.71 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TACO1]] | +0.71 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[RBM23]] | +0.70 | +0.71 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC3]] | -0.69 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[STRN]] | -0.67 | -0.72 / -0.31 | both halves | 2e-04 |  |
| [[PDZD7]] | -0.65 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[F11R]] | -0.65 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[NPTN]] | -0.64 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[PCMT1]] | -0.62 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[TMEM65]] | -0.62 | -0.63 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.685). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.4, 8.4); signed map (2.9, -24.9). **Vector** length 91.3, 18.9% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +12.3 | +26.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.7 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +6.9 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +6.3 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +0.7 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -6.1 | -14.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -19.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -6.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,578,753-65,611,289 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564O1664; previously C15orf44, VWA9 |
| Gene groups (HGNC) | Integrator complex |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SY0](https://www.uniprot.org/uniprotkb/Q96SY0) (Integrator complex subunit 14):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [81556](https://www.ncbi.nlm.nih.gov/gene/81556):

> Predicted to enable metal ion binding activity. Involved in RNA polymerase II transcription initiation surveillance; regulation of transcription elongation by RNA polymerase II; and snRNA processing. Located in cytoplasm. Part of INTAC complex and integrator complex. Is active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25372](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25372) · Entrez [81556](https://www.ncbi.nlm.nih.gov/gene/81556) · UniProt [Q96SY0](https://www.uniprot.org/uniprotkb/Q96SY0) · Ensembl [ENSG00000138614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138614)

## Data

Gene col 6194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6194); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6194]; `tensor/DDL_lfc|DDL_z.npy` [6194]; `embed/gene_vectors.npy` [6194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6194 or target_col == 6194). Every well: [[INTS14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

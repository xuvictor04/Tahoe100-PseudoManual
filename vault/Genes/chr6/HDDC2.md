---
symbol: "HDDC2"
type: "gene"
col: 3304
ensembl_id: "ENSG00000111906"
name: "HD domain containing 2"
location: "6q22.31"
module: 18
arm: "+"
pooled_cpm: 18.37
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# HDDC2

*HD domain containing 2* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +18.0, q 0e+00, up in 41 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.50× (z +9.3, q 2e-18, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.576× (z -12.7, q 3e-34, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM136A]] (+0.68, fdr 1e-05), [[SLC35G1]] (+0.67, fdr 4e-05), [[RAB11FIP2]] (+0.65, fdr 2e-05); moves opposite to [[FAM89B]] (-0.63, fdr 2e-05), [[CDKN2D]] (-0.61, fdr 2e-05), [[CARHSP1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STEAP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +18.0 | 0e+00 | 41/43 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +15.7 | 0e+00 | 30/32 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +9.6 | 2e-19 | 27/38 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +9.3 | 2e-18 | 35/48 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +6.8 | 9e-10 | 27/47 (HT-29, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +6.1 | 1e-07 | 22/45 (SNU-423, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.3 | 8e-06 | 19/45 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.3 | 9e-06 | 25/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.65×** | +4.1 | 0.003 | 14/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.5 | 0.028 | 8/35 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.044 | 4/48 (C32, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.047 | 6/46 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.2 | 0.064 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.576×** | -12.7 | 3e-34 | 34/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.489×** | -11.7 | 4e-29 | 35/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.489×** | -11.6 | 4e-29 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.530×** | -10.4 | 5e-23 | 35/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.483×** | -5.9 | 5e-07 | 24/48 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.710×** | -5.6 | 2e-06 | 20/47 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.509×** | -5.5 | 4e-06 | 24/46 (SNU-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.719×** | -5.4 | 6e-06 | 21/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.755×** | -4.6 | 3e-04 | 22/47 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.769×** | -4.3 | 0.001 | 19/46 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.625×** | -3.8 | 0.008 | 16/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.795×** | -3.7 | 0.009 | 18/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.823×** | -3.2 | 0.066 | 11/46 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **0.829×** | -3.1 | 0.092 | 18/47 (SW48, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.8 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -16.0) |
| [[PANC-1 (line)]] | alt | 32.9 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.327× (z -11.2) |
| [[SW480 (line)]] | alt | 18.9 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.251× (z -12.7) |
| [[RKO (line)]] | wt | 28.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.0) |
| [[A-172 (line)]] | wt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +19.9) | — |
| [[A498 (line)]] | wt | 15.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 18.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +11.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 16.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -9.6) |
| [[LoVo (line)]] | wt | 15.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 20.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 24.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -18.2) |
| [[NCI-H1792 (line)]] | alt | 15.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 26.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -12.5) |
| [[A549 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -9.7) ⚠ cell-cycle shift, explains ~5% of this change |
| [[C32 (line)]] | wt | 26.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.00× (z +10.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 9.52 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +8.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -8.9) |
| [[H4 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -10.6) ⚠ cell-cycle shift, explains ~3% of this change |
| [[HEC-1-A (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.112× (z -9.1) |
| [[HS-578T (line)]] | alt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 15.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 30.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.7) |
| [[SW48 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0790× (z -14.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM136A]] | +0.68 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SLC35G1]] | +0.67 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[RAB11FIP2]] | +0.65 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SLC9B2]] | +0.65 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[NSMAF]] | +0.63 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[USP46]] | +0.62 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ZC3HAV1L]] | +0.62 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TMEM268]] | +0.61 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TRMT11]] | +0.61 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[GCFC2]] | +0.60 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ATIC]] | +0.60 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[METTL3]] | +0.60 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89B]] | -0.63 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CDKN2D]] | -0.61 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CARHSP1]] | -0.59 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[GNAI2]] | -0.59 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[C1QL1]] | -0.58 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[COX6A1]] | -0.57 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[LGALS1]] | -0.57 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[RPA3]] | -0.57 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[RASSF7]] | -0.56 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[ZNF324]] | -0.56 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[PRADC1]] | -0.55 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[GPN3]] | -0.55 | -0.37 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP2]] | B | STEAP2 activity lowers HDDC2's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 1.18× higher at baseline in the lines without STEAP2 | 0.090 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.7, 12.6); signed map (-12.9, -40.8). **Vector** length 74.0, 13.9% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.2 | +9.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.0 | -10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -11.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -5.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -5.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | HD domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:125,219,962-125,302,078 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-130, dJ167O5.2; previously C6orf74 |
| Hallmark sets | MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4H3](https://www.uniprot.org/uniprotkb/Q7Z4H3) (5'-deoxynucleotidase HDDC2):

> Catalyzes the dephosphorylation of the nucleoside 5'-monophosphates deoxyadenosine monophosphate (dAMP), deoxycytidine monophosphate (dCMP), deoxyguanosine monophosphate (dGMP) and deoxythymidine monophosphate (dTMP).

**Summary**, from NCBI Gene [51020](https://www.ncbi.nlm.nih.gov/gene/51020):

> Predicted to enable 5'-deoxynucleotidase activity. Predicted to be involved in deoxyribonucleoside monophosphate catabolic process. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21078) · Entrez [51020](https://www.ncbi.nlm.nih.gov/gene/51020) · UniProt [Q7Z4H3](https://www.uniprot.org/uniprotkb/Q7Z4H3) · Ensembl [ENSG00000111906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111906)

## Data

Gene col 3304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3304); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3304]; `tensor/DDL_lfc|DDL_z.npy` [3304]; `embed/gene_vectors.npy` [3304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3304 or target_col == 3304). Every well: [[HDDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

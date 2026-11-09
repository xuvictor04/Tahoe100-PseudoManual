---
symbol: "HMG20B"
type: "gene"
col: 764
ensembl_id: "ENSG00000064961"
name: "high mobility group 20B"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 31.03
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# HMG20B

*high mobility group 20B* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +16.1, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.11× (z +12.4, q 3e-33, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.714× (z -5.6, q 1e-05, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.176×, LOX-IMVI 0.305×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.224×, LS 180 0.400×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.175×; ⚠ cell-cycle shift, explains ~0% of this change); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.0799×); [[Belinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.441×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP2R5D]] (+0.70, fdr 7e-06), [[CRAT]] (+0.64, fdr 2e-05), [[SUN1]] (+0.63, fdr 2e-05); moves opposite to [[BMS1P4-1]] (-0.56, fdr 4e-05), [[ZCCHC10]] (-0.54, fdr 8e-05), [[MTG2]] (-0.52, fdr 7e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +16.1 | 0e+00 | 42/43 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +15.3 | 0e+00 | 34/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +12.4 | 3e-33 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +12.4 | 3e-33 | 38/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +9.7 | 5e-20 | 38/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Minodronic acid (drug)]] 5 µM | ⚠ position correction uncertain | **2.71×** | +8.7 | 4e-16 | 42/48 (SK-MEL-2, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +8.4 | 3e-15 | 30/41 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Minodronic acid (drug)]] 0.05 µM | ⚠ position correction uncertain | **1.71×** | +8.4 | 3e-15 | 42/48 (SK-MEL-2, SW1417, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.64×** | +8.3 | 6e-15 | 35/46 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Minodronic acid (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.93×** | +7.8 | 3e-13 | 43/48 (SK-MEL-2, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.3 | 1e-08 | 25/47 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.8 | 4e-07 | 23/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.38×** | +5.0 | 3e-05 | 25/47 (LS 180, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +4.8 | 7e-05 | 22/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.1 | 0.002 | 0/48 | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.005 | 14/47 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.005 | 7/48 (HEC-1-A, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.005 | 15/47 (SW1417, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.011 | 13/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.050 | 3/47 (NCI-H23, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 764.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.176×, LOX-IMVI 0.305×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.224×, LS 180 0.400×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.175×; ⚠ cell-cycle shift, explains ~0% of this change); [[Silodosin (drug)]] 5 µM in 1 line (AN3 CA 0.0799×); [[Belinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.441×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.714×** | -5.6 | 1e-05 | 24/47 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.750×** | -4.8 | 4e-04 | 24/48 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 0.812× | -3.4 | 0.15 | 7/48 (LS 180, HT-29, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.822× | -3.3 | 0.15 | 17/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.832× | -3.1 | 0.23 | 3/48 (SNU-1, SW480, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 82.2 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +13.1) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[LoVo (line)]] | wt | 13.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.26× (z +10.0) | — |
| [[SW480 (line)]] | alt | 21.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.09× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 22.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.86× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 36.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.08× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 18.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 24.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 47.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -12.8) |
| [[A498 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 35.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0799× (z -10.2) |
| [[C32 (line)]] | wt | 78.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 9.13 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0917× (z -8.5) |
| [[HOP62 (line)]] | alt | 21.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.36× (z +8.6) | — |
| [[KATO III (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 50.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.25× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -20.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 150 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.441× (z -8.9) |
| [[SW48 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5D]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CRAT]] | +0.64 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SUN1]] | +0.63 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PNPLA6]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CALM3]] | +0.61 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CEP131]] | +0.61 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[NUMA1]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[FGFRL1]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CDK16]] | +0.58 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[CDC25B]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.57 | +0.39 / +0.51 | both halves | 5e-05 | pathway: Factors involved in megakaryocyte development and platelet production |
| [[INTS1]] | +0.56 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P4-1]] | -0.56 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[ZCCHC10]] | -0.54 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[MTG2]] | -0.52 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[AASDH]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ARL14EP]] | -0.51 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[DNAJC2]] | -0.51 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[GADD45A]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[CNPY2]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[YTHDF2]] | -0.50 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[THUMPD2]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[RPAP1]] | -0.50 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[MTHFS]] | -0.50 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-33.5, -37.4); signed map (-47.9, -12.7). **Vector** length 93.0, 20.1% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +16.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | +4.4 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +12.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +0.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group 20B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,572,777-3,579,088 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SOXL, HMGX2, BRAF35, SMARCE1r, BRAF25, HMGXB2 |
| Gene groups (HGNC) | Non-canonical high mobility group; CoREST complex subunits |
| Reactome | 8 pathways, smallest: HDACs deacetylate histones; Potential therapeutics for SARS; Factors involved in megakaryocyte development and platelet production |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0W2](https://www.uniprot.org/uniprotkb/Q9P0W2) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily E member 1-related):

> Required for correct progression through G2 phase of the cell cycle and entry into mitosis. Required for RCOR1/CoREST mediated repression of neuronal specific gene promoters.

**Summary**, from NCBI Gene [10362](https://www.ncbi.nlm.nih.gov/gene/10362):

> Predicted to enable DNA binding activity. Predicted to be involved in regulation of gene expression. Predicted to act upstream of or within negative regulation of protein sumoylation; positive regulation of neuron differentiation; and skeletal muscle cell differentiation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5002) · Entrez [10362](https://www.ncbi.nlm.nih.gov/gene/10362) · UniProt [Q9P0W2](https://www.uniprot.org/uniprotkb/Q9P0W2) · Ensembl [ENSG00000064961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064961)

## Data

Gene col 764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 764); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 764]; `tensor/DDL_lfc|DDL_z.npy` [764]; `embed/gene_vectors.npy` [764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 764 or target_col == 764). Every well: [[HMG20B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMG20B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

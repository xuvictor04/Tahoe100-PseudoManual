---
symbol: "ELMO2"
type: "gene"
col: 713
ensembl_id: "ENSG00000062598"
name: "engulfment and cell motility 2"
location: "20q13.12"
module: 214
arm: "+"
pooled_cpm: 31.92
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# ELMO2

*engulfment and cell motility 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.00× (z +10.9, q 4e-25, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.409× (z -10.0, q 1e-20, down in 37 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Estrone sulfate (potassium) (drug)]] 5 µM: 0.731× (z -3.5, q 0.065, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 0.0715×, NCI-H2030 0.145×, NCI-H1573 0.139×, C32 0.179×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2030 0.0992×, Hs 766T 0.0871×, KATO III 0.124×, SW1417 0.161×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.0956×, KATO III 0.120×, SW1417 0.151×, C32 0.180×; ⚠ toxic; transcription drop); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0695×); [[Bicalutamide (drug)]] 0.5 µM in 1 line (NCI-H661 0.0743×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC61A2]] (+0.65, fdr 1e-05), [[HSF2]] (+0.60, fdr 1e-05), [[ARHGAP17]] (+0.58, fdr 1e-05); moves opposite to [[IDI2-AS1]] (-0.60, fdr 9e-06), [[ZNF432]] (-0.58, fdr 7e-06), [[LAT2]] (-0.58, fdr 1e-05).
> It is in [[Module 214]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +10.9 | 4e-25 | 36/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.65×** | +10.9 | 4e-25 | 45/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.58×** | +10.6 | 6e-24 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.43×** | +9.9 | 6e-21 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.27×** | +9.2 | 5e-18 | 46/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +8.5 | 2e-15 | 37/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.20×** | +8.5 | 2e-15 | 40/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +7.9 | 3e-13 | 34/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.96×** | +7.5 | 4e-12 | 36/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.87×** | +7.0 | 1e-10 | 35/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +5.3 | 5e-06 | 28/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +5.3 | 5e-06 | 38/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +5.2 | 8e-06 | 35/48 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.001 | 24/48 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +4.0 | 0.002 | 29/48 (AsPC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.003 | 27/48 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +3.6 | 0.012 | 21/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 713.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 0.0715×, NCI-H2030 0.145×, NCI-H1573 0.139×, C32 0.179×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2030 0.0992×, Hs 766T 0.0871×, KATO III 0.124×, SW1417 0.161×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.0956×, KATO III 0.120×, SW1417 0.151×, C32 0.180×; ⚠ toxic; transcription drop); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0695×); [[Bicalutamide (drug)]] 0.5 µM in 1 line (NCI-H661 0.0743×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.409×** | -10.0 | 1e-20 | 37/43 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.455×** | -8.5 | 7e-15 | 28/36 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.503×** | -7.1 | 2e-10 | 30/42 (NCI-H2030, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.731×** | -3.5 | 0.065 | 21/48 (Panc 03.27, COLO 205, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.760× | -3.1 | 0.22 | 22/48 (A-172, BT-474, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.761× | -3.0 | 0.22 | 15/48 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.7 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.62× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 25.1 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 74.4 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.151× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 32.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 24.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 58.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 18.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.69× (z +10.7) | — |
| [[KATO III (line)]] | alt | 22.2 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.49× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -14.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 30.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 32.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -9.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 33.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 16.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 51.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0871× (z -14.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 50.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 45.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0992× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 47.4 | 0 | 2 (1 ⚠) | — | [[Bicalutamide (drug)]] 0.5 µM 0.0743× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 36.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0956× (z -14.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0715× (z -17.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0695× (z -11.1) |
| [[BT-474 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 19.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 27.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.1) | — |
| [[RKO (line)]] | wt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -11.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | +0.65 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[HSF2]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ARHGAP17]] | +0.58 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[ZNF592]] | +0.56 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.55 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[TFEB]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[STRN]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CYB5A]] | +0.55 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PPP4R1]] | +0.55 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[PXK]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[TSPAN15]] | +0.54 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.54 | +0.61 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDI2-AS1]] | -0.60 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[ZNF432]] | -0.58 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[LAT2]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MYSM1]] | -0.56 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[NABP1]] | -0.56 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[PPIEL]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[PARD6G-AS1]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[DDX18]] | -0.55 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MPDU1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[GCNA]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LRIF1]] | -0.54 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[TAF2]] | -0.53 | -0.58 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.7, -12.1); signed map (-28.7, -15.9). **Vector** length 84.9, 23.0% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.8 | +7.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.2 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +1.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +8.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.5 | +10.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.4 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | engulfment and cell motility 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:46,366,050-46,432,985 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CED12, ELMO-2, CED-12, KIAA1834, FLJ11656 |
| Gene groups (HGNC) | Engulfment and cell motility proteins |
| Reactome | 18 pathways, smallest: PTK6 Regulates RHO GTPases, RAS GTPase and MAP kinases; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JJ3](https://www.uniprot.org/uniprotkb/Q96JJ3) (Engulfment and cell motility protein 2):

> Regulates the activity of DOCK guanine nucleotide exchange factors (GEFs). Acts in association with DOCK1, DOCK2, DOCK4 and CRK. Involved in cytoskeletal rearrangements required for phagocytosis of apoptotic cells and cell motility.

**Summary**, from NCBI Gene [63916](https://www.ncbi.nlm.nih.gov/gene/63916):

> The protein encoded by this gene interacts with the dedicator of cyto-kinesis 1 protein. Similarity to a C. elegans protein suggests that this protein may function in phagocytosis of apoptotic cells and in cell migration. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:17233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17233) · Entrez [63916](https://www.ncbi.nlm.nih.gov/gene/63916) · UniProt [Q96JJ3](https://www.uniprot.org/uniprotkb/Q96JJ3) · Ensembl [ENSG00000062598](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062598)

## Data

Gene col 713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 713); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 713]; `tensor/DDL_lfc|DDL_z.npy` [713]; `embed/gene_vectors.npy` [713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 713 or target_col == 713). Every well: [[ELMO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELMO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

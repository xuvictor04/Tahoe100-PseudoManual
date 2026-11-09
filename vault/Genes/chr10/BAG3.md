---
symbol: "BAG3"
type: "gene"
col: 7582
ensembl_id: "ENSG00000151929"
name: "BAG cochaperone 3"
location: "10q26.11"
module: 60
arm: "+"
pooled_cpm: 53.44
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# BAG3

*BAG cochaperone 3* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 13.1× (z +46.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.550× (z -10.6, q 1e-23, down in 34 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.719× (z -5.9, q 6e-07, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL18]] (+0.71, fdr 7e-06), [[UBB]] (+0.65, fdr 1e-05), [[DEDD2]] (+0.65, fdr 7e-06); moves opposite to [[YEATS4]] (-0.53, fdr 4e-05), [[ARL6IP6]] (-0.53, fdr 8e-05), [[SMAD2]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **13.1×** | +46.0 | 0e+00 | 48/48 (SNU-423, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **8.62×** | +38.4 | 0e+00 | 48/48 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **9.56×** | +38.0 | 0e+00 | 48/48 (A498, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **6.72×** | +29.8 | 0e+00 | 48/48 (A498, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **6.28×** | +23.4 | 0e+00 | 48/49 (A498, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **10.1×** | +21.5 | 0e+00 | 45/45 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.76×** | +14.2 | 4e-44 | 36/48 (PANC-1, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **3.93×** | +12.8 | 2e-35 | 47/48 (AsPC-1, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +12.4 | 2e-33 | 36/49 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.61×** | +8.2 | 2e-14 | 32/48 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.54×** | +7.7 | 5e-13 | 30/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.78×** | +7.3 | 1e-11 | 32/47 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.13×** | +7.1 | 7e-11 | 29/49 (C32, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.4 | 7e-09 | 28/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.4 | 7e-09 | 29/47 (A498, COLO 205, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Hydroxyfasudil (drug)]] 0.5 µM |  | **1.50×** | +5.1 | 9e-06 | 28/49 (A498, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 13/48 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.013 | 17/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.015 | 15/48 (MIA PaCa-2, HEC-1-A, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.016 | 17/48 (HT-29, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.030 | 15/49 (HT-29, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.550×** | -10.6 | 1e-23 | 34/49 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -8.6 | 3e-15 | 27/38 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.683×** | -6.3 | 6e-08 | 24/44 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.719×** | -5.9 | 6e-07 | 25/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **0.800×** | -3.9 | 0.010 | 19/48 (HepG2/C3A, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.853× | -3.9 | 0.011 | 16/49 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.839× | -3.4 | 0.045 | 17/48 (SK-MEL-2, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.070 | 11/47 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.881× | -3.1 | 0.099 | 15/48 (SK-MEL-2, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.859× | -3.1 | 0.099 | 11/48 (NCI-H1792, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.820×** | -3.1 | 0.099 | 10/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Clotrimazole (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.099 | 15/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 44.6 | 11 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.8× (z +22.0) | — |
| [[LS 180 (line)]] | wt | 35.1 | 9 (3 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 17.5× (z +21.5) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 37.5 | 10 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 34.4× (z +26.3) | — |
| [[NCI-H2347 (line)]] | alt | 111 | 6 (1 ⚠) | 4 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 9.22× (z +23.6) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.7) |
| [[PANC-1 (line)]] | alt | 70.7 | 9 (4 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.26× (z +22.9) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 73.4 | 9 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 17.3× (z +33.3) | — |
| [[LoVo (line)]] | wt | 40.9 | 9 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 23.6× (z +28.4) | — |
| [[LOX-IMVI (line)]] | wt | 45.9 | 8 (3 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 17.0× (z +27.1) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 43.5 | 9 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.12× (z +20.2) | — |
| [[COLO 205 (line)]] | alt | 37.0 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 12.3× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.1 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 25.9× (z +27.8) | — |
| [[HT-29 (line)]] | alt | 41.6 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 24.0× (z +28.4) | — |
| [[RKO (line)]] | wt | 51.8 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 13.9× (z +25.4) | — |
| [[SK-MEL-2 (line)]] | alt | 69.4 | 6 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 19.2× (z +26.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0681× (z -22.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 69.4 | 7 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 23.1× (z +32.0) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 99.5 | 5 (1 ⚠) | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 9.46× (z +19.6) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -12.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 27.4 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 28.8× (z +29.4) | — |
| [[A-427 (line)]] | wt | 33.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 29.7× (z +28.7) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -9.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.4 | 7 (2 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 12.1× (z +20.8) | — |
| [[CFPAC-1 (line)]] | alt | 88.4 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 10.0× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 69.2 | 6 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 15.9× (z +20.8) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 58.6 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 17.4× (z +25.6) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -9.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 52.2 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 15.4× (z +20.5) | — |
| [[KATO III (line)]] | alt | 35.2 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 12.6× (z +22.0) | — |
| [[Panc 03.27 (line)]] | alt | 89.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 9.93× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 39.7 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 14.7× (z +20.9) | — |
| [[A-172 (line)]] | wt | 106 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 20.0× (z +31.5) | — |
| [[HEC-1-A (line)]] | alt | 30.2 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 21.0× (z +22.7) | — |
| [[Hs 766T (line)]] | wt | 73.6 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.57× (z +17.7) | — |
| [[J82 (line)]] | alt | 43.0 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 12.0× (z +21.0) | — |
| [[H4 (line)]] | wt | 55.5 | 5 | 0 | [[Auranofin (drug)]] 5 µM 15.6× (z +19.7) | — |
| [[HepG2_C3A (line)]] | wt | 50.3 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.36× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 5 | 0 | [[Bortezomib (drug)]] 0.05 µM 9.40× (z +13.7) | — |
| [[NCI-H2030 (line)]] | alt | 59.2 | 4 | 0 | [[Auranofin (drug)]] 5 µM 8.21× (z +21.6) | — |
| [[RPMI-7951 (line)]] | alt | 59.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 12.2× (z +19.1) | — |
| [[SW48 (line)]] | wt | 28.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 20.7× (z +16.0) | — |
| [[BT-474 (line)]] | alt | 14.0 | 3 | 0 | [[Auranofin (drug)]] 5 µM 32.4× (z +17.0) | — |
| [[C32 (line)]] | wt | 82.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 14.1× (z +22.3) | — |
| [[NCI-H23 (line)]] | alt | 56.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.79× (z +18.8) | — |
| [[SNU-1 (line)]] | wt | 32.2 | 3 | 0 | [[Auranofin (drug)]] 5 µM 22.9× (z +16.5) | — |
| [[SW 1271 (line)]] | alt | 53.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 25.5× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 36.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 17.1× (z +18.1) | — |
| [[CHP-212 (line)]] | wt | 43.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 10.4× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 71.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 17.2× (z +14.5) | — |
| [[NCI-H1792 (line)]] | alt | 54.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.17× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 34.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.6× (z +13.3) | — |
| [[NCI-H2122 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL18]] | +0.71 | +0.63 / +0.74 | both halves | 7e-06 | pathway: Cellular response to heat stress |
| [[UBB]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 | pathway: Cellular response to heat stress |
| [[DEDD2]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 | pathway: Cellular response to heat stress |
| [[PSMD8]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ZFAND2A]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SERPINH1]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 | pathway: Cellular response to heat stress |
| [[HSP90AA2P]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TUBA4A]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[DNAJB1]] | +0.60 | +0.67 / +0.76 | both halves | 7e-06 | pathway: Cellular response to heat stress; STRING 891 |
| [[UBC]] | +0.60 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[BRF2]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[HSPA1B]] | +0.59 | +0.44 / +0.68 | both halves | 3e-05 | pathway: Cellular response to heat stress; STRING 983 |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YEATS4]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ARL6IP6]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[SMAD2]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[NHLRC2]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TMEM14C]] | -0.49 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[SUMO2]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SLC12A2-DT]] | -0.46 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[HNRNPD]] | -0.46 | -0.18 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[CASC3]] | -0.46 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[DOP1A]] | -0.46 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.2, -9.7); signed map (-24.3, -26.8). **Vector** length 113, 33.2% of its response variance represented; |z| ≥ 3 in 1,289 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Attenuation phase* (reactome, mean cos +0.52 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.51 to 14); *HSF1 activation* (reactome, mean cos +0.53 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.9 | +46.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.2 | +38.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.1 | +38.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +29.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.8 | +21.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.6 | +23.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | +3.2 | +12.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +0.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -5.4 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -10.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.1 | +7.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | BAG cochaperone 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,651,380-119,677,819 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BAG cochaperones |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O95817](https://www.uniprot.org/uniprotkb/O95817) (BAG family molecular chaperone regulator 3):

> Co-chaperone and adapter protein that connects different classes of molecular chaperones including heat shock proteins 70 (HSP70s), e.g. HSPA1A/HSP70 or HSPA8/HSC70, and small heat shock proteins (sHSPs), e.g. HSPB8. Acts as a nucleotide-exchange factor (NEF) promoting the release of ADP from HSP70s, thereby triggering client protein release. Nucleotide release is mediated via BAG3 binding to the nucleotide-binding domain (NBD) of HSP70s, whereas client release is mediated via binding to the …

**Summary**, from NCBI Gene [9531](https://www.ncbi.nlm.nih.gov/gene/9531):

> BAG proteins compete with Hip for binding to the Hsc70/Hsp70 ATPase domain and promote substrate release. All the BAG proteins have an approximately 45-amino acid BAG domain near the C terminus but differ markedly in their N-terminal regions. The protein encoded by this gene contains a WW domain in the N-terminal region and a BAG domain in the C-terminal region. The BAG domains of BAG1, BAG2, and BAG3 interact specifically with the Hsc70 ATPase domain in vitro and in mammalian cells. All 3 …

**Accessions** — [HGNC:939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:939) · Entrez [9531](https://www.ncbi.nlm.nih.gov/gene/9531) · UniProt [O95817](https://www.uniprot.org/uniprotkb/O95817) · Ensembl [ENSG00000151929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151929)

## Data

Gene col 7582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7582); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7582]; `tensor/DDL_lfc|DDL_z.npy` [7582]; `embed/gene_vectors.npy` [7582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7582 or target_col == 7582). Every well: [[BAG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

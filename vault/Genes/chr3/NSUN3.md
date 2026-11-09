---
symbol: "NSUN3"
type: "gene"
col: 10948
ensembl_id: "ENSG00000178694"
name: "NOP2/Sun RNA methyltransferase 3"
location: "3q11.2"
module: 51
arm: "+"
pooled_cpm: 37.85
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 21
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# NSUN3

*NOP2/Sun RNA methyltransferase 3* — 3q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +5.8, q 5e-06, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.472× (z -12.4, q 1e-32, down in 40 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.595× (z -8.6, q 1e-15, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LANCL2]] (+0.71, fdr 1e-05), [[MTREX]] (+0.71, fdr 1e-05), [[ZNF189]] (+0.70, fdr 5e-05); moves opposite to [[TNK2]] (-0.59, fdr 1e-04), [[STX2]] (-0.58, fdr 6e-05), [[PLCB3]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.8 | 5e-06 | 21/48 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.2 | 6e-05 | 25/48 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +5.1 | 6e-05 | 23/47 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.24×** | +5.0 | 1e-04 | 24/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +4.8 | 2e-04 | 19/47 (A-172, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 0.002 | 21/47 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.006 | 21/47 (HEC-1-A, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.26×** | +3.8 | 0.010 | 18/48 (RKO, KATO III, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.010 | 14/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.010 | 16/48 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.013 | 17/47 (AsPC-1, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.017 | 14/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.024 | 17/48 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.027 | 13/48 (HEC-1-A, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.029 | 14/48 (Hs 766T, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.038 | 12/47 (AsPC-1, C-33 A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.038 | 16/48 (AsPC-1, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.472×** | -12.4 | 1e-32 | 40/47 (SW480, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -10.2 | 5e-22 | 35/47 (SNU-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.554×** | -9.8 | 3e-20 | 38/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.595×** | -8.6 | 1e-15 | 32/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.602×** | -7.8 | 1e-12 | 29/44 (H4, C-33 A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.594×** | -7.7 | 1e-12 | 30/46 (A-427, KATO III, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.659×** | -6.9 | 5e-10 | 29/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.688×** | -6.2 | 4e-08 | 27/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.707×** | -5.7 | 6e-07 | 27/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.709×** | -5.7 | 8e-07 | 30/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.727×** | -5.3 | 7e-06 | 23/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.739×** | -4.8 | 7e-05 | 22/39 (A-427, SW480, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.749×** | -4.8 | 8e-05 | 26/46 (LS 180, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | **0.743×** | -4.7 | 9e-05 | 29/48 (CFPAC-1, A549, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.818×** | -4.7 | 9e-05 | 21/48 (NCI-H23, NCI-H661, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.791×** | -3.5 | 0.016 | 16/47 (CFPAC-1, H4, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.085 | 17/48 (A549, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.831×** | -3.0 | 0.085 | 14/47 (CFPAC-1, MIA PaCa-2, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.700×** | -2.9 | 0.097 | 11/48 (RPMI-7951, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.6 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.301× (z -13.2) |
| [[PANC-1 (line)]] | alt | 47.0 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.313× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 61.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0866× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -10.3) |
| [[LS 180 (line)]] | wt | 42.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 50.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.315× (z -11.2) |
| [[SNU-1 (line)]] | wt | 48.5 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0774× (z -16.5) ⚠ toxic |
| [[SW1417 (line)]] | alt | 39.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.291× (z -9.0) |
| [[HCT15 (line)]] | alt | 36.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0990× (z -13.9) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0931× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.192× (z -9.0) |
| [[NCI-H661 (line)]] | alt | 40.1 | 0 | 2 | — | [[Fluvoxamine (maleate) (drug)]] 0.05 µM 0.0589× (z -10.0) |
| [[RKO (line)]] | wt | 30.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.202× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 41.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.119× (z -9.0) |
| [[C32 (line)]] | wt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[CHP-212 (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 91.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.319× (z -8.9) ⚠ toxic |
| [[H4 (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 54.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.342× (z -9.7) |
| [[J82 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.296× (z -9.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[LoVo (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.334× (z -9.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 44.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SW48 (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0823× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL2]] | +0.71 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[MTREX]] | +0.71 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[ZNF189]] | +0.70 | +0.77 / +0.40 | both halves | 5e-05 |  |
| [[WARS2]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PSMC2]] | +0.67 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[POLR3C]] | +0.66 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FIZ1]] | +0.65 | +0.65 / +0.36 | both halves | 9e-05 |  |
| [[POLR2M]] | +0.65 | +0.70 / +0.37 | both halves | 9e-05 |  |
| [[FRS2]] | +0.65 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PEF1]] | +0.64 | +0.69 / +0.27 | both halves | 3e-04 |  |
| [[FUNDC1]] | +0.64 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[ZC3HC1]] | +0.64 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNK2]] | -0.59 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[STX2]] | -0.58 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[PLCB3]] | -0.58 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[TPST2]] | -0.56 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[INPP5F]] | -0.56 | -0.62 / -0.20 | both halves | 7e-04 |  |
| [[PACS2]] | -0.55 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[STK32C]] | -0.55 | -0.62 / -0.23 | both halves | 5e-04 |  |
| [[MXRA7]] | -0.55 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[DNAAF3]] | -0.54 | -0.41 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-21.2, 10.5); signed map (13.6, -25.0). **Vector** length 100, 25.7% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | +5.6 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +5.5 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.8 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.9 | -5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.8 | -5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.4 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -10.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.9 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -8.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | NOP2/Sun RNA methyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.2 — chr3:94,062,980-94,131,832 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22609 |
| Gene groups (HGNC) | NOP2/Sun RNA methyltransferase family; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H649](https://www.uniprot.org/uniprotkb/Q9H649) (tRNA):

> Mitochondrial tRNA methyltransferase that mediates methylation of cytosine to 5-methylcytosine (m5C) at position 34 of mt-tRNA(Met). mt-tRNA(Met) methylation at cytosine(34) takes place at the wobble position of the anticodon and initiates the formation of 5-formylcytosine (f(5)c) at this position. mt-tRNA(Met) containing the f(5)c modification at the wobble position enables recognition of the AUA codon in addition to the AUG codon, expanding codon recognition in mitochondrial translation.

**Summary**, from NCBI Gene [63899](https://www.ncbi.nlm.nih.gov/gene/63899):

> Enables tRNA (cytidine-N5)-methyltransferase activity. Involved in regulation of mitochondrial translation and tRNA wobble base cytosine methylation. Located in mitochondrial matrix. Implicated in combined oxidative phosphorylation deficiency 48. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26208) · Entrez [63899](https://www.ncbi.nlm.nih.gov/gene/63899) · UniProt [Q9H649](https://www.uniprot.org/uniprotkb/Q9H649) · Ensembl [ENSG00000178694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178694)

## Data

Gene col 10948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10948); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10948]; `tensor/DDL_lfc|DDL_z.npy` [10948]; `embed/gene_vectors.npy` [10948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10948 or target_col == 10948). Every well: [[NSUN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSUN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

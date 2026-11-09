---
symbol: "SGSM2"
type: "gene"
col: 6497
ensembl_id: "ENSG00000141258"
name: "small G protein signaling modulator 2"
location: "17p13.3"
module: 126
arm: "+"
pooled_cpm: 23.97
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# SGSM2

*small G protein signaling modulator 2* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +10.6, q 2e-23, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.535× (z -16.1, q 0e+00, down in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.494× (z -12.8, q 3e-35, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA8A]] (+0.60, fdr 3e-05), [[TMEM94]] (+0.58, fdr 1e-05), [[INPPL1]] (+0.57, fdr 1e-05); moves opposite to [[AREG]] (-0.49, fdr 3e-04), [[SMIM30]] (-0.45, fdr 0.001, ⚠ one half only (not replicated)), [[INIP]] (-0.45, fdr 1e-04), [[MT2A]] (-0.45, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MT2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +10.6 | 2e-23 | 30/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.051 | 12/47 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.058 | 11/44 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.067 | 15/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.067 | 10/47 (HEC-1-A, SW480, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.067 | 11/47 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.20× | +3.3 | 0.074 | 10/47 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.098 | 6/46 (BT-474, KATO III, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.098 | 4/47 (CFPAC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.098 | 8/47 (NCI-H1573, NCI-H23, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.15× | +3.1 | 0.098 | 8/47 (LOX-IMVI, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Sonidegib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.098 | 6/47 (KATO III, LOX-IMVI, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.11 | 7/47 (SW480, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.535×** | -16.1 | 0e+00 | 39/46 (LOX-IMVI, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -12.8 | 3e-35 | 36/46 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.524×** | -11.7 | 2e-29 | 35/47 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.523×** | -11.1 | 2e-26 | 38/47 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -10.4 | 3e-23 | 39/47 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.573×** | -10.1 | 5e-22 | 38/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.601×** | -9.3 | 2e-18 | 32/46 (J82, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.604×** | -9.2 | 3e-18 | 35/47 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.616×** | -8.8 | 9e-17 | 37/47 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.643×** | -8.0 | 7e-14 | 30/46 (SW48, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -7.7 | 7e-13 | 28/44 (RPMI-7951, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.673×** | -7.2 | 3e-11 | 27/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.672×** | -6.8 | 5e-10 | 24/45 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.710×** | -6.2 | 2e-08 | 25/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.742×** | -5.4 | 2e-06 | 22/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.591×** | -5.0 | 2e-05 | 21/47 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.633×** | -4.3 | 5e-04 | 15/46 (RPMI-7951, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.791×** | -4.2 | 7e-04 | 18/46 (LOX-IMVI, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.850× | -4.2 | 1e-03 | 9/47 (HCT15, NCI-H661, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -4.0 | 0.002 | 18/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.803×** | -4.0 | 0.002 | 13/47 (HCT15, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.812×** | -3.8 | 0.005 | 18/47 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.819×** | -3.6 | 0.008 | 16/46 (SW1417, SNU-423, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.823×** | -3.3 | 0.021 | 9/47 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 42.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -19.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.241× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 52.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.418× (z -9.8) |
| [[PANC-1 (line)]] | alt | 18.6 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -10.9) |
| [[A-172 (line)]] | wt | 26.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 36.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 24.2 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0961× (z -15.8) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.226× (z -10.6) |
| [[A-427 (line)]] | wt | 17.8 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.391× (z -9.2) |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -9.3) |
| [[HCT15 (line)]] | alt | 51.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 23.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.159× (z -10.8) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.0383× (z -10.6) |
| [[SW480 (line)]] | alt | 29.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -9.0) |
| [[A549 (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 21.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.210× (z -8.6) |
| [[H4 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0941× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.101× (z -9.9) |
| [[HOP62 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.3) | — |
| [[RKO (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0833× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0514× (z -13.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 5.91 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA8A]] | +0.60 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[TMEM94]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[INPPL1]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[BCL2L2]] | +0.56 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[LDB1]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[CHD3]] | +0.54 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[AJM1]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MAN2A2]] | +0.52 | +0.36 / +0.49 | both halves | 9e-05 |  |
| [[ANP32A]] | +0.52 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[ADCY6]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[MTCH1]] | +0.51 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[HDAC10]] | +0.50 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AREG]] | -0.49 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[SMIM30]] | -0.45 | -0.15 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[INIP]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[MT2A]] | -0.45 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[MYL12A]] | -0.45 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[MRPL57]] | -0.44 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[GTF2H5]] | -0.44 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[ZMYM1]] | -0.44 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[H3-3B]] | -0.43 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[MRPL12]] | -0.42 | -0.22 / -0.35 | both halves | 6e-04 |  |
| [[NOP10]] ⚠ | -0.42 | -0.34 / -0.32 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[POLM]] | -0.41 | -0.17 / -0.43 | ⚠ not reproduced | 0.001 |  |
| [[ZNF699]] | -0.41 | -0.32 / -0.34 | both halves | 1e-04 |  |
| [[TANK]] | -0.41 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[WDR70]] | -0.41 | -0.27 / -0.34 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT2A]] | B | MT2A activity raises SGSM2's level | lines that do not express MT2A (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without MT2A | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.1, -22.0); signed map (1.6, 2.5). **Vector** length 66.0, 11.5% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.1 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | -3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -12.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | small G protein signaling modulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,337,498-2,381,058 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0397; previously RUTBC1 |
| Gene groups (HGNC) | Small G protein signaling modulators; TBC1 domain family members; RUN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43147](https://www.uniprot.org/uniprotkb/O43147) (Small G protein signaling modulator 2):

> Possesses GTPase activator activity towards RAB32, RAB33B and RAB38. Regulates the trafficking of melanogenic enzymes TYR, TYRP1 and DCT/TYRP2 to melanosomes in melanocytes by inactivating RAB32 and RAB38. Inhibits RAB32 and RAB38 activation both directly by promoting their GTPase activity and indirectly by disrupting the RAB9A-HPS4 interaction which is required for RAB32/38 activation.

**Summary**, from NCBI Gene [9905](https://www.ncbi.nlm.nih.gov/gene/9905):

> The protein encoded by this gene is a GTPase activator with activity towards RAB32 and RAB33B, which are regulators of membrane trafficking. The encoded protein inactivates RAB32 and can bind RAB9A-GTP, a protein required for RAB32 activation. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:29026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29026) · Entrez [9905](https://www.ncbi.nlm.nih.gov/gene/9905) · UniProt [O43147](https://www.uniprot.org/uniprotkb/O43147) · Ensembl [ENSG00000141258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141258)

## Data

Gene col 6497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6497); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6497]; `tensor/DDL_lfc|DDL_z.npy` [6497]; `embed/gene_vectors.npy` [6497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6497 or target_col == 6497). Every well: [[SGSM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGSM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

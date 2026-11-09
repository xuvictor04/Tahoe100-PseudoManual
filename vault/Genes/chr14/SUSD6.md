---
symbol: "SUSD6"
type: "gene"
col: 2008
ensembl_id: "ENSG00000100647"
name: "sushi domain containing 6"
location: "14q24.1"
module: 60
arm: "-"
pooled_cpm: 44.52
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# SUSD6

*sushi domain containing 6* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +17.7, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.438× (z -14.6, q 1e-45, down in 39 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.615× (z -8.6, q 1e-15, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPM1D]] (+0.59, fdr 7e-06), [[BBC3]] (+0.58, fdr 1e-05), [[DEPP1]] (+0.54, fdr 4e-05); moves opposite to [[CCT4]] (-0.56, fdr 1e-05), [[HSPD1]] (-0.56, fdr 1e-05), [[CCT5]] (-0.55, fdr 2e-05).
> It sits in the **-** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GRAMD2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +17.7 | 0e+00 | 40/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +16.1 | 0e+00 | 45/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.22×** | +14.2 | 3e-43 | 45/48 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.48×** | +13.9 | 1e-41 | 45/49 (A498, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +13.8 | 2e-41 | 45/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +10.2 | 2e-22 | 36/48 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +8.0 | 7e-14 | 36/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +7.3 | 2e-11 | 35/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +7.3 | 2e-11 | 25/48 (BT-474, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +6.7 | 1e-09 | 30/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +5.9 | 1e-07 | 31/48 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.5 | 2e-06 | 24/48 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 2e-06 | 26/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +5.3 | 4e-06 | 27/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.2 | 8e-06 | 29/48 (SW480, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 1e-04 | 24/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.58×** | +4.2 | 8e-04 | 17/48 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.438×** | -14.6 | 1e-45 | 39/46 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -13.8 | 1e-40 | 30/37 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.615×** | -8.6 | 1e-15 | 33/48 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.476×** | -6.9 | 9e-10 | 28/44 (A498, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.711×** | -5.6 | 3e-06 | 21/40 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.594×** | -4.8 | 1e-04 | 24/47 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.785×** | -4.3 | 0.002 | 22/48 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.852× | -4.0 | 0.004 | 20/48 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.838× | -3.1 | 0.11 | 7/48 (NCI-H1573, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.4 | 11 (6 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +17.6) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 39.7 | 9 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -23.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 69.9 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -14.1) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H23 (line)]] | alt | 29.2 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.48× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 24.8 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +15.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -10.8) |
| [[LS 180 (line)]] | wt | 48.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.4× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 110 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.368× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 46.6 | 4 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.71× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 81.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -12.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 75.5 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.84× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -15.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 110 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.3× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.233× (z -11.4) |
| [[KATO III (line)]] | alt | 33.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -9.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 46.0 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.95× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -10.8) ⚠ cell-cycle shift, explains ~16% of this change |
| [[BT-474 (line)]] | alt | 104 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 23.8× (z +12.1) | — |
| [[C32 (line)]] | wt | 43.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.9× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.0694× (z -20.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 77.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -13.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 20.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 50.6 | 2 | 1 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.31× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 45.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 18.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +10.4) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.44× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.259× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 29.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.2) | — |
| [[RKO (line)]] | wt | 36.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.81× (z +9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 28.0 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +9.2) ⚠ cell-cycle shift, explains ~16% of this change | — |
| [[A549 (line)]] | wt | 48.0 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.98× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 56.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.90× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 38.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -10.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 58.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.276× (z -9.8) |
| [[SHP-77 (line)]] | alt | 49.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -13.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 63.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 41.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.3) | — |
| [[SW48 (line)]] | wt | 42.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 25.5× (z +9.4) | — |
| [[A-172 (line)]] | wt | 27.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 17.8× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0965× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 68.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.295× (z -9.5) |
| [[Hs 766T (line)]] | wt | 40.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.39× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 48.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.224× (z -11.8) |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPM1D]] | +0.59 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[BBC3]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[DEPP1]] | +0.54 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[BTG2]] | +0.54 | +0.51 / +0.64 | both halves | 1e-05 | STRING 411 |
| [[RNF19B]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PER1]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[STAT3]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PHPT1]] | +0.52 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[PSTPIP2]] | +0.50 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[GOLPH3]] | +0.50 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[FDXR]] | +0.49 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SAA1]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT4]] | -0.56 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[HSPD1]] | -0.56 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[CCT5]] | -0.55 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[FKBP4]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CCT3]] | -0.52 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[L3HYPDH]] | -0.52 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[HSP90AB1]] | -0.50 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[AHSA1]] | -0.50 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[PTGES3]] | -0.48 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[GPR135]] | -0.48 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[ATPSCKMT]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRAMD2B]] | B | GRAMD2B activity raises SUSD6's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without GRAMD2B | 0.011 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[TLR2]] | B | TLR2 activity raises SUSD6's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without TLR2 | 0.068 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[PSMB5]] | B | PSMB5 activity raises SUSD6's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TLR2]] | B | TLR2 activity weakens SUSD6's drug response | lines that do not express TLR2 (26) vs lines expressing it (23) | the lines without TLR2 respond 1.14× as strongly (z diff -0.43); strongest at Belinostat 5 µM: 2.71x vs 1.86x (z diff -2.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; target measured in part of the lines; artifact flags |
| [[DEPP1]] | B | DEPP1 activity raises SUSD6's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.39× lower at baseline in the lines without DEPP1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **-** arm (projection on the module's main direction -0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (23.3, -1.5); signed map (46.9, -1.5). **Vector** length 117, 35.6% of its response variance represented; |z| ≥ 3 in 1,605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +13.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +5.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.0 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +0.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.7 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.4 | -8.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.8 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.7 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | sushi domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:69,611,596-69,715,144 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0247 |
| Gene groups (HGNC) | Sushi domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92537](https://www.uniprot.org/uniprotkb/Q92537) (Sushi domain-containing protein 6):

> May play a role in growth-suppressive activity and cell death. May be involved in the production of chemokine molecules in umbilical vein endothelial cells (HUVECs) cultured in THP1 monocyte LPS-induced medium. Plays a role in preventing tumor onset (By similarity).

**Summary**, from NCBI Gene [9766](https://www.ncbi.nlm.nih.gov/gene/9766):

> Involved in DNA damage response. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19956) · Entrez [9766](https://www.ncbi.nlm.nih.gov/gene/9766) · UniProt [Q92537](https://www.uniprot.org/uniprotkb/Q92537) · Ensembl [ENSG00000100647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100647)

## Data

Gene col 2008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2008); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2008]; `tensor/DDL_lfc|DDL_z.npy` [2008]; `embed/gene_vectors.npy` [2008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2008 or target_col == 2008). Every well: [[SUSD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUSD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

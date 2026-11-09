---
symbol: "BMP2K"
type: "gene"
col: 6225
ensembl_id: "ENSG00000138756"
name: "BMP2 inducible kinase"
location: "4q21.21"
module: 193
arm: "+"
pooled_cpm: 80.43
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# BMP2K

*BMP2 inducible kinase* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.86× (z +10.0, q 9e-21, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.540× (z -10.1, q 5e-21, down in 39 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-1 0.0977×, A-427 0.100×, SW48 0.0587×, C-33 A 0.158×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-1 0.254×, H4 0.169×, A-427 0.303×, SW480 0.389×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.259×, AsPC-1 0.322×; ⚠ cell-cycle shift, explains ~64% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.339×); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.385×); [[Auranofin (drug)]] 5 µM in 1 line (SNU-1 0.422×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASA2]] (+0.64, fdr 1e-05), [[LYPLA1]] (+0.60, fdr 1e-05), [[CCM2]] (+0.58, fdr 1e-05); moves opposite to [[BTN3A3]] (-0.53, fdr 3e-05), [[TET2]] (-0.53, fdr 2e-05), [[CHD3]] (-0.50, fdr 3e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GFOD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +10.0 | 9e-21 | 41/47 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +9.0 | 8e-17 | 40/47 (LOX-IMVI, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +8.5 | 3e-15 | 31/47 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +8.2 | 3e-14 | 38/47 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +7.5 | 8e-12 | 36/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.7 | 2e-09 | 31/47 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.7 | 2e-09 | 30/46 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.49×** | +6.4 | 1e-08 | 34/47 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +6.1 | 6e-08 | 33/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.8 | 4e-07 | 35/47 (BT-474, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.7 | 6e-07 | 25/47 (LOX-IMVI, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.5 | 2e-06 | 29/47 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +5.4 | 3e-06 | 30/47 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.1 | 2e-05 | 30/47 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.7 | 8e-05 | 35/48 (LOX-IMVI, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 1e-04 | 31/47 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +4.5 | 2e-04 | 30/46 (SW480, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +4.2 | 6e-04 | 25/46 (A-172, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6225.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-1 0.0977×, A-427 0.100×, SW48 0.0587×, C-33 A 0.158×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-1 0.254×, H4 0.169×, A-427 0.303×, SW480 0.389×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.259×, AsPC-1 0.322×; ⚠ cell-cycle shift, explains ~64% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.339×); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.385×); [[Auranofin (drug)]] 5 µM in 1 line (SNU-1 0.422×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.540×** | -10.1 | 5e-21 | 39/47 (SNU-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -8.0 | 4e-13 | 27/42 (SNU-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.618×** | -7.3 | 7e-11 | 31/44 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | 0.817× | -3.3 | 0.11 | 22/46 (SW1417, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.869× | -3.3 | 0.11 | 7/47 (Hs 766T, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 580 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.339× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 35.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 46.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 112 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 46.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.9) | — |
| [[A-427 (line)]] | wt | 80.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -22.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 153 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -13.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[C32 (line)]] | wt | 42.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +15.2) | — |
| [[Hs 766T (line)]] | wt | 82.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.98× (z +9.2) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.243× (z -11.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.0) | — |
| [[LoVo (line)]] | wt | 76.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 118 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.5) | — |
| [[A549 (line)]] | wt | 72.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -9.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 25.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 76.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -11.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 90.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[MIA PaCa-2 (line)]] | alt | 64.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.6) | — |
| [[SW480 (line)]] | alt | 97.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -12.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 43.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -15.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -12.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 61.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 66.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.40× (z +9.1) ⚠ unreliable plate only | — |
| [[NCI-H596 (line)]] | alt | 82.3 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.169× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 47.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 67.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.332× (z -10.4) ⚠ transcription drop; cell-cycle shift, explains ~13% of this change |
| [[SW48 (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0587× (z -18.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASA2]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[LYPLA1]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CCM2]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[DUSP7]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[BCAR3]] | +0.57 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[FMNL2]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DOCK9]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[PSEN2]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[APBB2]] | +0.55 | +0.49 / +0.56 | both halves | 2e-05 |  |
| [[ABCA3]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SPIRE1]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A3]] | -0.53 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TET2]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CHD3]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[RBKS]] | -0.50 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[FAXDC2]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[BTN3A1]] | -0.49 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[SUPT6H]] | -0.49 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[BTN3A2]] | -0.48 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[KLHL3]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 | same gene group |
| [[CWC25]] | -0.48 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[FMO5]] | -0.47 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[EFCAB7]] | -0.47 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GFOD1]] | B | GFOD1 activity raises BMP2K's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without GFOD1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[PALS2]] | C | PALS2 activity raises BMP2K's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 3.89× lower at baseline in the lines without PALS2 | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.2, 5.7); signed map (-1.0, 50.9). **Vector** length 97.5, 26.9% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.6 | +6.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.5 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.4 | +6.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.8 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.7 | +4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.6 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -3.3 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | BMP2 inducible kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:78,776,342-78,916,365 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434K0614, BIKe |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Numb-associated kinase family |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSY1](https://www.uniprot.org/uniprotkb/Q9NSY1) (BMP-2-inducible protein kinase):

> May be involved in osteoblast differentiation.

**Summary**, from NCBI Gene [55589](https://www.ncbi.nlm.nih.gov/gene/55589):

> This gene is the human homolog of mouse BMP-2-inducible kinase. Bone morphogenic proteins (BMPs) play a key role in skeletal development and patterning. Expression of the mouse gene is increased during BMP-2 induced differentiation and the gene product is a putative serine/threonine protein kinase containing a nuclear localization signal. Therefore, the protein encoded by this human homolog is thought to be a protein kinase with a putative regulatory role in attenuating the program of …

**Accessions** — [HGNC:18041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18041) · Entrez [55589](https://www.ncbi.nlm.nih.gov/gene/55589) · UniProt [Q9NSY1](https://www.uniprot.org/uniprotkb/Q9NSY1) · Ensembl [ENSG00000138756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138756)

## Data

Gene col 6225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6225); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6225]; `tensor/DDL_lfc|DDL_z.npy` [6225]; `embed/gene_vectors.npy` [6225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6225 or target_col == 6225). Every well: [[BMP2K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP2K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

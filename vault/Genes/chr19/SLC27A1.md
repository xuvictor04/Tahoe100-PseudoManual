---
symbol: "SLC27A1"
type: "gene"
col: 5047
ensembl_id: "ENSG00000130304"
name: "solute carrier family 27 member 1"
location: "19p13.11"
module: 85
arm: "+"
pooled_cpm: 24.69
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 46
n_dd_up_clean: 8
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# SLC27A1

*solute carrier family 27 member 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.15× (z +13.4, q 2e-38, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.276× (z -32.0, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.81, fdr 7e-06), [[FAM13B]] (+0.79, fdr 1e-05), [[MAST3]] (+0.79, fdr 1e-05); moves opposite to [[DECR1]] (-0.76, fdr 1e-05), [[ST7L]] (-0.72, fdr 1e-05), [[MMADHC-DT]] (-0.72, fdr 0.002, ⚠ one half only (not replicated)), [[ZMYND11]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SLC2A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +13.4 | 2e-38 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +13.2 | 3e-37 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +13.0 | 2e-36 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +8.4 | 5e-15 | 36/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +7.9 | 4e-13 | 32/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +6.4 | 1e-08 | 35/48 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +5.9 | 3e-07 | 25/48 (LoVo, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +4.7 | 2e-04 | 26/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.057 | 7/48 (C32, BT-474, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.12 | 6/48 (LS 180, HT-29, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.276×** | -32.0 | 0e+00 | 44/47 (Panc 03.27, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.206×** | -27.8 | 0e+00 | 45/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.217×** | -25.8 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.282×** | -22.3 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.307×** | -20.8 | 0e+00 | 44/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.349×** | -17.8 | 0e+00 | 42/47 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.402×** | -16.0 | 0e+00 | 38/47 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.414×** | -15.5 | 0e+00 | 42/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.435×** | -14.6 | 0e+00 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.441×** | -13.9 | 7e-42 | 41/48 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -13.4 | 3e-39 | 35/47 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.521×** | -11.0 | 1e-26 | 23/33 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.537×** | -10.9 | 3e-26 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.538×** | -10.9 | 4e-26 | 30/44 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.540×** | -10.4 | 7e-24 | 31/43 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.336×** | -10.0 | 5e-22 | 35/48 (Hs 766T, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.595×** | -9.1 | 2e-18 | 29/48 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.726×** | -8.0 | 4e-14 | 30/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.670×** | -7.0 | 5e-11 | 26/47 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.1 | 3 | 15 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +10.7) | [[Harringtonine (drug)]] 5 µM 0.119× (z -19.9) |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 27.2 | 0 | 13 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0974× (z -21.8) |
| [[CFPAC-1 (line)]] | alt | 38.3 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -21.5) |
| [[A-172 (line)]] | wt | 49.0 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -26.4) |
| [[MIA PaCa-2 (line)]] | alt | 41.1 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0634× (z -22.2) |
| [[SNU-1 (line)]] | wt | 53.5 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0668× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 61.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0911× (z -28.9) |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0573× (z -23.0) |
| [[H4 (line)]] | wt | 44.5 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -16.7) |
| [[hTERT-HPNE (line)]] | wt | 40.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -16.4) |
| [[Hs 766T (line)]] | wt | 25.2 | 1 | 6 (1 ⚠) | [[Isocorydine (drug)]] 0.5 µM 4.17× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.9) |
| [[HS-578T (line)]] | alt | 46.0 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -24.1) |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.8) |
| [[RPMI-7951 (line)]] | alt | 41.9 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.227× (z -10.5) |
| [[SNU-423 (line)]] | alt | 28.3 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -16.7) |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0791× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 22.9 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -12.0) |
| [[A549 (line)]] | wt | 14.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -14.5) |
| [[HCT15 (line)]] | alt | 33.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 65.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -16.1) |
| [[A498 (line)]] | wt | 20.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -17.0) |
| [[LoVo (line)]] | wt | 12.8 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 4.05× (z +9.4) | [[Harringtonine (drug)]] 0.5 µM 0.179× (z -11.6) |
| [[LS 180 (line)]] | wt | 10.1 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 5.85× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.0599× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -15.5) |
| [[SW1417 (line)]] | alt | 23.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.3) |
| [[C32 (line)]] | wt | 48.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.3) |
| [[A-427 (line)]] | wt | 22.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.186× (z -11.8) |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 2 | — | [[Naproxen (drug)]] 5 µM 0.0858× (z -9.2) |
| [[J82 (line)]] | alt | 22.1 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -10.6) |
| [[KATO III (line)]] | alt | 9.00 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0749× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 9.71 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0668× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.5) |
| [[RKO (line)]] | wt | 15.1 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 5.17× (z +8.9) | [[Digitoxin (drug)]] 0.5 µM 0.207× (z -8.5) |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.9) |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -10.4) |
| [[SW48 (line)]] | wt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -8.5) |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.81 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[FAM13B]] | +0.79 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[MAST3]] | +0.79 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.75 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.75 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[CARHSP1]] | +0.74 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.74 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[SUFU]] | +0.74 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MGST3]] | +0.73 | +0.63 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[PEDS1]] | +0.73 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.72 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[CARD19]] | +0.72 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.76 | -0.64 / -0.54 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[ST7L]] | -0.72 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.72 | -0.69 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[PBLD]] | -0.71 | -0.62 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZMYND11]] | -0.71 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[CRPPA]] | -0.71 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[RFX3-DT]] | -0.71 | -0.67 / -0.25 | both halves | 4e-04 |  |
| [[NIPAL2]] | -0.70 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[ZNF337-AS1]] | -0.70 | -0.68 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PSME3IP1]] | -0.69 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CSTF3]] | -0.69 | -0.64 / -0.29 | both halves | 2e-04 |  |
| [[EIF4G2]] | -0.69 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MCTS1]] | -0.69 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[CPSF2]] | -0.68 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[ZNF564]] | -0.68 | -0.61 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A3]] | B | SLC2A3 activity raises SLC27A1's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without SLC2A3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SLC27A1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SLC27A1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDGFL3]] | B | HDGFL3 activity raises SLC27A1's level | lines that do not express HDGFL3 (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without HDGFL3 | 0.073 | ⚠ within organs, on part of the lines; also absent: HLTF, GAMT, TIGD7 |
| [[TOP2A]] | B | TOP2A activity raises SLC27A1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HNF4G]] | B | HNF4G activity lowers SLC27A1's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 1.56× higher at baseline in the lines without HNF4G | 0.090 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[SPATC1L]] | B | SPATC1L activity raises SLC27A1's level | lines that do not express SPATC1L (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without SPATC1L | 0.091 | ⚠ within organs, on part of the lines; also absent: TIAM1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.897). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.4, -1.7); signed map (-28.6, 19.4). **Vector** length 111, 34.1% of its response variance represented; |z| ≥ 3 in 1,565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +9.6 | +13.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +9.4 | +13.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +9.3 | +13.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.2 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.2 | +8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | -3.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -17.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.6 | -22.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -27.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.1 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -10.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.2 | -6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 27 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,468,769-17,506,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FATP1, FATP, MGC71751, FLJ00336, ACSVL5 |
| Gene groups (HGNC) | Acyl-CoA synthetase family; Solute carrier family 27 |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 9 pathways, smallest: Transport of fatty acids; Transport of vitamins, nucleosides, and related molecules; Arachidonate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PCB7](https://www.uniprot.org/uniprotkb/Q6PCB7) (Long-chain fatty acid transport protein 1):

> Mediates the import of long-chain fatty acids (LCFA) into the cell by facilitating their transport at the plasma membrane. Also functions as an acyl-CoA ligase catalyzing the ATP-dependent formation of fatty acyl-CoA using LCFA and very-long-chain fatty acids (VLCFA) as substrates, which prevents fatty acid efflux from cells and might drive more fatty acid uptake. May act directly as a bona fide transporter, or alternatively, in a cytoplasmic or membrane-associated multimeric protein complex to …

**Summary**, from NCBI Gene [376497](https://www.ncbi.nlm.nih.gov/gene/376497):

> Enables biotin transmembrane transporter activity; efflux transmembrane transporter activity; and long-chain fatty acid transmembrane transporter activity. Involved in export across plasma membrane; import across plasma membrane; and lipid transport across blood-brain barrier. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10995) · Entrez [376497](https://www.ncbi.nlm.nih.gov/gene/376497) · UniProt [Q6PCB7](https://www.uniprot.org/uniprotkb/Q6PCB7) · Ensembl [ENSG00000130304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130304)

## Data

Gene col 5047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5047); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5047]; `tensor/DDL_lfc|DDL_z.npy` [5047]; `embed/gene_vectors.npy` [5047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5047 or target_col == 5047). Every well: [[SLC27A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC27A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

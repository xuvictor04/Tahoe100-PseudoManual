---
symbol: "TSHZ1"
type: "gene"
col: 11073
ensembl_id: "ENSG00000179981"
name: "teashirt zinc finger homeobox 1"
location: "18q22.3"
module: 201
arm: "+"
pooled_cpm: 29.21
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 38
n_dd_up_clean: 8
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# TSHZ1

*teashirt zinc finger homeobox 1* — 18q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.31× (z +23.3, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.399× (z -18.1, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTCH1]] (+0.60, fdr 3e-05), [[CNOT6L]] (+0.56, fdr 2e-05), [[PPP3R1]] (+0.54, fdr 1e-05); moves opposite to [[ACOT9]] (-0.55, fdr 4e-05), [[FAM50A]] (-0.48, fdr 1e-04), [[SNX12]] (-0.45, fdr 4e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PDE3B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +23.3 | 0e+00 | 38/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +7.7 | 4e-12 | 27/46 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +7.6 | 6e-12 | 26/48 (NCI-H1792, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.69×** | +5.4 | 7e-06 | 24/48 (HEC-1-A, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.1 | 4e-05 | 20/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.9 | 1e-04 | 23/47 (RKO, HEC-1-A, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.52×** | +4.3 | 0.001 | 14/45 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.021 | 9/48 (LoVo, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.083 | 14/46 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.16× | +3.0 | 0.14 | 9/48 (LoVo, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11073.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.399×** | -18.1 | 0e+00 | 41/48 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.444×** | -16.0 | 0e+00 | 36/46 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.526×** | -12.6 | 2e-34 | 33/48 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.529×** | -12.5 | 1e-33 | 33/47 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.536×** | -12.3 | 2e-32 | 31/44 (SHP-77, LS 180, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.543×** | -12.0 | 4e-31 | 39/47 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.553×** | -11.6 | 2e-29 | 30/47 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -11.0 | 3e-26 | 33/48 (PANC-1, C32, …) | two highest doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.550×** | -10.8 | 1e-25 | 30/40 (C32, SW48, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.710×** | -9.5 | 1e-19 | 31/48 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -8.0 | 9e-14 | 29/47 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.687×** | -7.1 | 7e-11 | 18/36 (C32, H4, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.700×** | -7.0 | 1e-10 | 24/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -6.7 | 1e-09 | 25/48 (A-427, PANC-1, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.787×** | -6.6 | 1e-09 | 25/48 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.715×** | -6.6 | 2e-09 | 22/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.721×** | -6.4 | 5e-09 | 22/46 (H4, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.726×** | -6.3 | 1e-08 | 22/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.743×** | -5.8 | 2e-07 | 19/47 (RPMI-7951, COLO 205, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.745×** | -5.5 | 8e-07 | 23/47 (AN3 CA, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 99.9 | 0 | 15 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0285× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -15.5) |
| [[PANC-1 (line)]] | alt | 45.0 | 1 | 13 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 20.7 | 1 | 10 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +14.2) | [[Digitoxin (drug)]] 5 µM 0.153× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -14.7) |
| [[SHP-77 (line)]] | alt | 118 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.227× (z -13.5) |
| [[SW480 (line)]] | alt | 21.3 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.257× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 31.6 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +13.6) | [[Digitoxin (drug)]] 5 µM 0.189× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.8) |
| [[COLO 205 (line)]] | alt | 61.1 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.231× (z -9.5) |
| [[LS 180 (line)]] | wt | 44.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 39.2 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.189× (z -9.5) |
| [[A498 (line)]] | wt | 18.2 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.157× (z -11.1) |
| [[SW1417 (line)]] | alt | 60.8 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 4.71× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.459× (z -8.6) |
| [[A-427 (line)]] | wt | 32.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -13.3) |
| [[BT-474 (line)]] | alt | 33.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.35× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.215× (z -10.8) ⚠ toxic |
| [[C-33 A (line)]] | alt | 28.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -11.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 45.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.105× (z -13.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 41.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 17.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 34.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -9.9) |
| [[LoVo (line)]] | wt | 34.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 30.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 13.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -9.6) |
| [[RKO (line)]] | wt | 21.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.3) | — |
| [[A-172 (line)]] | wt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -10.2) |
| [[Hs 766T (line)]] | wt | 70.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.9) |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +9.2) | — |
| [[J82 (line)]] | alt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.6) | — |
| [[KATO III (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0711× (z -20.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.226× (z -9.1) |
| [[SNU-423 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +10.6) | — |
| [[SW48 (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -11.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCH1]] | +0.60 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[CNOT6L]] | +0.56 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[PPP3R1]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[P3H3]] | +0.52 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[HOXB3]] | +0.51 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ABHD17B]] | +0.50 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[PAX6]] | +0.50 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[HOXB4]] | +0.49 | +0.40 / +0.42 | both halves | 4e-05 |  |
| [[PTGR3]] | +0.48 | +0.34 / +0.54 | both halves | 1e-04 | STRING 659; ⚠ same locus (1.6 kb: neighbours can correlate without regulation) |
| [[HOXB6]] | +0.48 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[EPB41L4B]] | +0.47 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[PPIL3]] | +0.47 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[HOXB5]] | +0.47 | +0.46 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT9]] | -0.55 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[FAM50A]] | -0.48 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[SNX12]] | -0.45 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[GGACT]] | -0.45 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[DHRS12]] | -0.44 | -0.27 / -0.59 | both halves | 3e-04 |  |
| [[PTPN21]] | -0.44 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[PIGL]] | -0.44 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[MYPN]] | -0.42 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[PBRM1]] | -0.42 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[NEK1]] | -0.42 | -0.21 / -0.42 | both halves | 6e-04 |  |
| [[RHOB]] | -0.41 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[PITPNB]] | -0.41 | -0.44 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE3B]] | B | PDE3B activity raises TSHZ1's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.72× lower at baseline in the lines without PDE3B | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[PDE3B]] | B | PDE3B activity strengthens TSHZ1's drug response | lines that do not express PDE3B (20) vs lines expressing it (28) | the lines without PDE3B respond 0.67× as strongly (z diff +1.74); strongest at Dinaciclib 0.5 µM: 0.74x vs 0.42x (z diff +4.3) | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4; target measured in part of the lines; artifact flags |
| [[DUSP8]] | C | DUSP8 activity lowers TSHZ1's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 2.45× higher at baseline in the lines without DUSP8 | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.3, -21.9); signed map (-19.3, 17.3). **Vector** length 101, 24.4% of its response variance represented; |z| ≥ 3 in 1,353 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.8 | +23.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +4.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.4 | +7.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +1.5 |
|  | [[NG25 (drug)]] 5 µM |  | +4.4 | +4.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -4.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.3 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -12.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -6.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.8 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | teashirt zinc finger homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.3 — chr18:75,210,755-75,289,950 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-CO-33, TSH1; previously SDCCAG33 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZSZ6](https://www.uniprot.org/uniprotkb/Q6ZSZ6) (Teashirt homolog 1):

> Probable transcriptional regulator involved in developmental processes. May act as a transcriptional repressor (Potential).

**Summary**, from NCBI Gene [10194](https://www.ncbi.nlm.nih.gov/gene/10194):

> This gene encodes a colon cancer antigen that was defined by serological analysis of recombinant cDNA expression libraries. The encoded protein is a member of the teashirt C2H2-type zinc-finger protein family and may be involved in transcriptional regulation of developmental processes. Mutations in this gene may be associated with congenital aural atresia syndrome. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:10669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10669) · Entrez [10194](https://www.ncbi.nlm.nih.gov/gene/10194) · UniProt [Q6ZSZ6](https://www.uniprot.org/uniprotkb/Q6ZSZ6) · Ensembl [ENSG00000179981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179981)

## Data

Gene col 11073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11073); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11073]; `tensor/DDL_lfc|DDL_z.npy` [11073]; `embed/gene_vectors.npy` [11073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11073 or target_col == 11073). Every well: [[TSHZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSHZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "TBC1D2B"
type: "gene"
col: 9435
ensembl_id: "ENSG00000167202"
name: "TBC1 domain family member 2B"
location: "15q24.3-q25.1"
module: 57
arm: "+"
pooled_cpm: 33.75
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# TBC1D2B

*TBC1 domain family member 2B* — 15q24.3-q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.58× (z +9.4, q 3e-18, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.400× (z -26.5, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAF3]] (+0.66, fdr 7e-06), [[RPA1]] (+0.66, fdr 1e-05), [[EPB41L4B]] (+0.66, fdr 7e-06); moves opposite to [[GGPS1]] (-0.64, fdr 1e-05), [[TTC6]] (-0.64, fdr 2e-05), [[BOLA1]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +9.4 | 3e-18 | 38/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +8.6 | 3e-15 | 31/48 (A498, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +6.9 | 8e-10 | 28/48 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.8 | 2e-09 | 28/48 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +6.4 | 2e-08 | 33/48 (A498, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +5.9 | 4e-07 | 26/48 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +5.5 | 4e-06 | 21/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +5.1 | 3e-05 | 20/48 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 4e-04 | 19/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.033 | 9/48 (KATO III, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.046 | 11/48 (KATO III, SW48, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.18× | +3.3 | 0.047 | 12/48 (J82, A498, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.080 | 5/48 (C32, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.400×** | -26.5 | 0e+00 | 38/47 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.514×** | -13.7 | 6e-40 | 34/47 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.569×** | -11.1 | 2e-26 | 34/48 (COLO 205, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.598×** | -10.5 | 1e-23 | 34/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -8.1 | 6e-14 | 30/48 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.778×** | -7.3 | 4e-11 | 27/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -7.1 | 8e-11 | 26/47 (SW1417, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -7.0 | 2e-10 | 29/48 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -7.0 | 2e-10 | 27/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.738×** | -6.2 | 3e-08 | 30/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.751×** | -5.9 | 2e-07 | 23/48 (SNU-1, NCI-H460, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -5.2 | 7e-06 | 22/48 (KATO III, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.779×** | -5.1 | 1e-05 | 24/46 (A-427, SNU-1, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.776×** | -4.8 | 7e-05 | 20/41 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.782×** | -4.7 | 8e-05 | 21/48 (H4, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.825×** | -3.9 | 0.003 | 20/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.776×** | -3.7 | 0.006 | 18/48 (KATO III, LOX-IMVI, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.711×** | -3.6 | 0.008 | 19/48 (SK-MEL-2, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.839× | -3.6 | 0.009 | 11/47 (MIA PaCa-2, SNU-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 17.7 | 7 | 2 | [[Belinostat (drug)]] 5 µM 3.82× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 15.1 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -17.7) |
| [[SW480 (line)]] | alt | 46.2 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.419× (z -15.9) |
| [[C32 (line)]] | wt | 41.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -19.4) |
| [[SNU-1 (line)]] | wt | 38.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.147× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 28.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -19.7) |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 50.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -12.3) |
| [[A-427 (line)]] | wt | 24.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -12.3) |
| [[HOP62 (line)]] | alt | 28.7 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.453× (z -10.9) |
| [[LoVo (line)]] | wt | 36.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -21.0) |
| [[SW1417 (line)]] | alt | 51.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -20.0) |
| [[A549 (line)]] | wt | 37.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0802× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 33.6 | 1 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 2.59× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.2) |
| [[COLO 205 (line)]] | alt | 37.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0845× (z -14.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.193× (z -14.5) |
| [[HCT15 (line)]] | alt | 27.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 31.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -16.1) |
| [[HepG2_C3A (line)]] | wt | 46.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.2) |
| [[LS 180 (line)]] | wt | 30.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 51.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.6) |
| [[PANC-1 (line)]] | alt | 37.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -13.9) |
| [[RKO (line)]] | wt | 26.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -12.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 27.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -12.4) |
| [[SW48 (line)]] | wt | 28.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.7) |
| [[A-172 (line)]] | wt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -8.6) |
| [[A498 (line)]] | wt | 35.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.38× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -10.9) |
| [[J82 (line)]] | alt | 52.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -19.8) |
| [[Panc 03.27 (line)]] | alt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.0) |
| [[AN3 CA (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[RPA1]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[EPB41L4B]] | +0.66 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.66 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[ZDHHC20]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CYB5A]] | +0.65 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[PAPSS1]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[RAB4A]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SKP2]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[METAP1]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SNRPA1]] | +0.60 | +0.69 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGPS1]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[TTC6]] | -0.64 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[BOLA1]] | -0.61 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[LINC00571]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[CDK12]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[C6orf62]] | -0.60 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.59 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[LINC02542]] | -0.59 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[SON]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.58 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.58 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TBC1D2B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TBC1D2B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DAB2IP]] | C | DAB2IP activity raises TBC1D2B's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without DAB2IP | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.0, -5.9); signed map (-36.0, -12.2). **Vector** length 99.5, 23.9% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +4.8 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +9.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +5.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.5 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -26.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.5 | -11.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.3-q25.1 — chr15:77,984,036-78,077,724 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1055 |
| Gene groups (HGNC) | TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPU7](https://www.uniprot.org/uniprotkb/Q9UPU7) (TBC1 domain family member 2B):

> GTPase-activating protein that plays a role in the early steps of endocytosis.

**Summary**, from NCBI Gene [23102](https://www.ncbi.nlm.nih.gov/gene/23102):

> Predicted to enable GTPase activator activity. Involved in endocytosis. Located in cytosol and early endosome. Implicated in neurodevelopmental disorder with seizures and gingival overgrowth. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29183) · Entrez [23102](https://www.ncbi.nlm.nih.gov/gene/23102) · UniProt [Q9UPU7](https://www.uniprot.org/uniprotkb/Q9UPU7) · Ensembl [ENSG00000167202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167202)

## Data

Gene col 9435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9435); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9435]; `tensor/DDL_lfc|DDL_z.npy` [9435]; `embed/gene_vectors.npy` [9435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9435 or target_col == 9435). Every well: [[TBC1D2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

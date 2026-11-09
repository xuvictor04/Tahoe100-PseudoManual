---
symbol: "GRAMD1C"
type: "gene"
col: 10894
ensembl_id: "ENSG00000178075"
name: "GRAM domain containing 1C"
location: "3q13.31"
module: 135
arm: "-"
pooled_cpm: 17.89
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 36
n_dd_up_clean: 9
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# GRAMD1C

*GRAM domain containing 1C* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.01× (z +16.4, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.324× (z -26.4, q 0e+00, down in 38 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAC2]] (+0.65, fdr 1e-05), [[PPP1R14C]] (+0.62, fdr 2e-05), [[FAM102B]] (+0.58, fdr 3e-05); moves opposite to [[PEF1]] (-0.58, fdr 1e-05), [[CLIP1]] (-0.56, fdr 4e-05), [[ARFGAP2]] (-0.53, fdr 7e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +16.4 | 0e+00 | 41/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.26×** | +13.5 | 4e-39 | 40/42 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +10.1 | 8e-22 | 29/44 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +9.6 | 1e-19 | 31/44 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +9.3 | 1e-18 | 30/44 (J82, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +9.1 | 1e-17 | 30/43 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.46×** | +6.3 | 3e-08 | 26/44 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +5.8 | 6e-07 | 23/43 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.31×** | +4.5 | 5e-04 | 14/43 (SW480, NCI-H2347, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.036 | 6/42 (HEC-1-A, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.15× | +3.3 | 0.048 | 14/44 (LoVo, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.42× | +3.1 | 0.10 | 9/44 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.11 | 2/43 (LOX-IMVI, SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.324×** | -26.4 | 0e+00 | 38/43 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.326×** | -18.6 | 0e+00 | 35/43 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.359×** | -17.0 | 0e+00 | 38/44 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -12.4 | 2e-33 | 32/43 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.483×** | -12.1 | 2e-31 | 31/43 (PANC-1, HOP62, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.492×** | -11.8 | 6e-30 | 36/43 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.480×** | -11.7 | 9e-30 | 27/40 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -11.7 | 9e-30 | 30/41 (COLO 205, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.519×** | -10.9 | 9e-26 | 34/43 (PANC-1, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.541×** | -9.8 | 7e-21 | 31/43 (RPMI-7951, COLO 205, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.553×** | -9.3 | 1e-18 | 31/43 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.587×** | -8.8 | 5e-17 | 29/43 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.380×** | -8.4 | 2e-15 | 30/43 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -7.9 | 2e-13 | 26/44 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.640×** | -7.4 | 6e-12 | 24/43 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.456×** | -6.8 | 4e-10 | 21/42 (HOP62, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.694×** | -6.0 | 5e-08 | 20/44 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -5.3 | 3e-06 | 18/42 (LOX-IMVI, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.798×** | -5.3 | 4e-06 | 19/43 (PANC-1, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.9 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -20.6) |
| [[LOX-IMVI (line)]] | wt | 34.0 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -18.5) |
| [[HOP62 (line)]] | alt | 24.4 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -19.0) |
| [[COLO 205 (line)]] | alt | 32.3 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0397× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0502× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 25.2 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 3.45× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 26.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 22.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 24.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.2) |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -10.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.3) |
| [[A498 (line)]] | wt | 19.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -18.4) |
| [[HS-578T (line)]] | alt | 33.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.7) |
| [[J82 (line)]] | alt | 16.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0409× (z -13.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.138× (z -8.5) |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0849× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.0883× (z -10.9) |
| [[SW480 (line)]] | alt | 6.16 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 4.75× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.201× (z -9.0) |
| [[H4 (line)]] | wt | 17.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -10.5) |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 11.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.34× (z +11.3) | — |
| [[A549 (line)]] | wt | 9.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -12.5) |
| [[C32 (line)]] | wt | 12.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.169× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.2) |
| [[HT-29 (line)]] | alt | 6.21 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.44× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.5) |
| [[LoVo (line)]] | wt | 6.92 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.53× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0716× (z -26.2) |
| [[SW1417 (line)]] | alt | 6.57 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.36× (z +9.0) | — |
| [[A-172 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAC2]] | +0.65 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PPP1R14C]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[FAM102B]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[INPP5F]] | +0.55 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[ATG16L2]] | +0.55 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TMOD2]] | +0.55 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[RGS9]] | +0.54 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[ST3GAL5]] | +0.54 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[RNF168]] | +0.54 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[HPSE]] | +0.53 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[RGS17]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[TOX2]] | +0.53 | +0.35 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEF1]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CLIP1]] | -0.56 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ARFGAP2]] | -0.53 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[RNF6]] | -0.52 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[MTHFSD]] | -0.52 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[UBE3B]] | -0.51 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[LINC00571]] | -0.50 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[CPSF2]] | -0.50 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[AKT1S1]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CDK12]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[SNAPC5]] | -0.48 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[FBXO30]] | -0.48 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GRAMD1C's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers GRAMD1C's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NLRP3]] | B | NLRP3 activity raises GRAMD1C's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 1.58× lower at baseline in the lines without NLRP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (35.7, 14.1); signed map (1.0, 29.2). **Vector** length 85.3, 19.3% of its response variance represented; |z| ≥ 3 in 1,393 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +16.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +13.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +9.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.3 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -26.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -18.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -9.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | GRAM domain containing 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.31 — chr3:113,828,182-113,947,174 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LAMc, DKFZp434C0328 |
| Gene groups (HGNC) | GRAM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYS0](https://www.uniprot.org/uniprotkb/Q8IYS0) (Protein Aster-C):

> Cholesterol transporter that mediates non-vesicular transport of cholesterol from the plasma membrane (PM) to the endoplasmic reticulum (ER) (By similarity). Contains unique domains for binding cholesterol and the PM, thereby serving as a molecular bridge for the transfer of cholesterol from the PM to the ER (By similarity). Plays a crucial role in cholesterol homeostasis and has the unique ability to localize to the PM based on the level of membrane cholesterol (By similarity). In lipid-poor …

**Summary**, from NCBI Gene [54762](https://www.ncbi.nlm.nih.gov/gene/54762):

> Predicted to enable cholesterol binding activity and cholesterol transfer activity. Predicted to be involved in cellular response to cholesterol and intracellular sterol transport. Predicted to be located in membrane and organelle membrane contact site. Predicted to be active in endoplasmic reticulum membrane; endoplasmic reticulum-plasma membrane contact site; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25252](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25252) · Entrez [54762](https://www.ncbi.nlm.nih.gov/gene/54762) · UniProt [Q8IYS0](https://www.uniprot.org/uniprotkb/Q8IYS0) · Ensembl [ENSG00000178075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178075)

## Data

Gene col 10894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10894); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10894]; `tensor/DDL_lfc|DDL_z.npy` [10894]; `embed/gene_vectors.npy` [10894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10894 or target_col == 10894). Every well: [[GRAMD1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRAMD1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

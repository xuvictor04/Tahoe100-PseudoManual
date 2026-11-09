---
symbol: "SASH1"
type: "gene"
col: 3309
ensembl_id: "ENSG00000111961"
name: "SAM and SH3 domain containing 1"
location: "6q24.3-q25.1"
module: 84
arm: "+"
pooled_cpm: 92.18
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 36
n_dd_up_clean: 4
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# SASH1

*SAM and SH3 domain containing 1* — 6q24.3-q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +9.1, q 7e-17, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.466× (z -19.3, q 0e+00, down in 42 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.616× (z -17.3, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP170]] (+0.54, fdr 2e-05), [[MITF]] (+0.54, fdr 5e-05), [[WDFY2]] (+0.52, fdr 4e-05); moves opposite to [[ATXN1L]] (-0.48, fdr 5e-05), [[RNASEH1]] (-0.45, fdr 1e-04), [[SELENOI]] (-0.43, fdr 1e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +9.1 | 7e-17 | 29/46 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +6.5 | 3e-08 | 25/47 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +6.0 | 4e-07 | 25/47 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +5.1 | 5e-05 | 22/46 (NCI-H23, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.8 | 0.020 | 6/46 (PANC-1, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.7 | 0.020 | 17/46 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.085 | 6/46 (HT-29, CFPAC-1, …) | all doses, flat |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.26× | +3.1 | 0.13 | 14/46 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.13 | 4/47 (BT-474, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.0 | 0.13 | 9/46 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.13 | 5/46 (HT-29, KATO III, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.466×** | -19.3 | 0e+00 | 42/46 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.616×** | -17.3 | 0e+00 | 36/47 (SHP-77, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.569×** | -14.2 | 1e-43 | 38/46 (SHP-77, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.677×** | -13.9 | 8e-42 | 28/46 (SHP-77, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.588×** | -13.4 | 9e-39 | 36/46 (SHP-77, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -12.2 | 4e-32 | 32/41 (HEC-1-A, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.630×** | -11.6 | 2e-29 | 32/47 (A-172, C32, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.611×** | -11.5 | 1e-28 | 28/43 (SHP-77, C32, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.427×** | -11.2 | 2e-27 | 37/46 (C32, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -10.8 | 3e-25 | 27/46 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.445×** | -10.7 | 6e-25 | 38/46 (C32, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.661×** | -10.4 | 7e-24 | 36/46 (SHP-77, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.653×** | -10.3 | 2e-23 | 28/45 (HT-29, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.464×** | -10.1 | 2e-22 | 36/46 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -9.9 | 2e-21 | 32/46 (SHP-77, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -9.8 | 3e-21 | 33/46 (SHP-77, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.481×** | -9.7 | 1e-20 | 35/46 (C32, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.698×** | -9.0 | 5e-18 | 29/46 (SHP-77, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -8.6 | 2e-16 | 32/46 (HT-29, NCI-H2030, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.524×** | -8.5 | 4e-16 | 35/46 (C32, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.720×** | -8.3 | 4e-15 | 25/46 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 525 | 0 | 23 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -31.2) |
| [[H4 (line)]] | wt | 133 | 0 | 15 (7 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -12.9) |
| [[SW480 (line)]] | alt | 76.6 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 363 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -21.1) |
| [[NCI-H2030 (line)]] | alt | 99.8 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -18.9) |
| [[C32 (line)]] | wt | 219 | 0 | 10 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.170× (z -23.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.4) |
| [[SNU-423 (line)]] | alt | 121 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -19.3) |
| [[A-172 (line)]] | wt | 149 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -12.5) |
| [[Hs 766T (line)]] | wt | 142 | 1 | 6 (4 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.59× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.5) |
| [[HT-29 (line)]] | alt | 135 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -17.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -12.8) |
| [[SNU-1 (line)]] | wt | 120 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.316× (z -10.8) |
| [[HOP62 (line)]] | alt | 45.6 | 0 | 6 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 486 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -14.6) |
| [[PANC-1 (line)]] | alt | 54.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 44.2 | 1 | 4 | [[Tucidinostat (drug)]] 5 µM 2.04× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 121 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.284× (z -9.9) |
| [[J82 (line)]] | alt | 78.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.406× (z -8.9) |
| [[A498 (line)]] | wt | 44.3 | 1 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.421× (z -9.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.567× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 41.4 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -14.1) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -13.2) |
| [[SW 1271 (line)]] | alt | 220 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.5) |
| [[A549 (line)]] | wt | 49.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 150 | 1 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.65× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.396× (z -10.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 72.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.497× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.505× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 43.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -11.6) |
| [[A-427 (line)]] | wt | 67.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.9) |
| [[BT-474 (line)]] | alt | 63.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.5) |
| [[C-33 A (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -12.3) |
| [[HS-578T (line)]] | alt | 63.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.8) |
| [[KATO III (line)]] | alt | 83.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.93× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 73.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0658× (z -8.8) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.270× (z -9.7) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 91.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 130 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 95.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP170]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[MITF]] | +0.54 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[WDFY2]] | +0.52 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[APBA1]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[CLEC11A]] | +0.51 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[KCNN2]] | +0.51 | +0.24 / +0.57 | both halves | 4e-04 |  |
| [[NEDD4L]] | +0.51 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[PPP1R14C]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[LPCAT2]] | +0.50 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[NTM]] | +0.49 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[HACL1]] | +0.49 | +0.22 / +0.53 | both halves | 6e-04 |  |
| [[ADAMTS18]] | +0.49 | +0.54 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1L]] | -0.48 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[RNASEH1]] | -0.45 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[SELENOI]] | -0.43 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[DESI1]] | -0.42 | -0.35 / -0.32 | both halves | 1e-04 |  |
| [[IL18BP]] | -0.42 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[STXBP2]] | -0.42 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[ACAD9]] | -0.41 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[RCC1L]] | -0.41 | -0.37 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SASH1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.2, 11.8); signed map (20.1, 24.9). **Vector** length 94.7, 23.1% of its response variance represented; |z| ≥ 3 in 1,638 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.4 | +5.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +0.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.5 | -19.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.8 | -10.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -10.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.9 | -9.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -11.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.2 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | SAM and SH3 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.3-q25.1 — chr6:148,272,304-148,552,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0790, dJ323M4.1, SH3D6A |
| Gene groups (HGNC) | SAM and SH3 domain containing; Sterile alpha motif domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O94885](https://www.uniprot.org/uniprotkb/O94885) (SAM and SH3 domain-containing protein 1):

> Is a positive regulator of NF-kappa-B signaling downstream of TLR4 activation. It acts as a scaffold molecule to assemble a molecular complex that includes TRAF6, MAP3K7, CHUK and IKBKB, thereby facilitating NF-kappa-B signaling activation. Regulates TRAF6 and MAP3K7 ubiquitination. Involved in the regulation of cell mobility. Regulates lipolysaccharide (LPS)-induced endothelial cell migration. Is involved in the regulation of skin pigmentation through the control of melanocyte migration in the …

**Summary**, from NCBI Gene [23328](https://www.ncbi.nlm.nih.gov/gene/23328):

> This gene encodes a scaffold protein involved in the TLR4 signaling pathway that may stimulate cytokine production and endothelial cell migration in response to invading pathogens. The encoded protein has also been described as a potential tumor suppressor that may negatively regulate proliferation, apoptosis, and invasion of cancer cells, and reduced expression of this gene has been observed in multiple human cancers. Mutations in this gene may be associated with abnormal skin pigmentation in …

**Accessions** — [HGNC:19182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19182) · Entrez [23328](https://www.ncbi.nlm.nih.gov/gene/23328) · UniProt [O94885](https://www.uniprot.org/uniprotkb/O94885) · Ensembl [ENSG00000111961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111961)

## Data

Gene col 3309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3309); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3309]; `tensor/DDL_lfc|DDL_z.npy` [3309]; `embed/gene_vectors.npy` [3309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3309 or target_col == 3309). Every well: [[SASH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SASH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

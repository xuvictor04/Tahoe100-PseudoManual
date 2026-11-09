---
symbol: "CPT1A"
type: "gene"
col: 3114
ensembl_id: "ENSG00000110090"
name: "carnitine palmitoyltransferase 1A"
location: "11q13.3"
module: 179
arm: "-"
pooled_cpm: 56.16
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 10
n_dd_up_clean: 27
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# CPT1A

*carnitine palmitoyltransferase 1A* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +16.6, q 0e+00, up in 42 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.62× (z +13.2, q 4e-37, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.435× (z -8.3, q 4e-14, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROCK2]] (+0.55, fdr 2e-05), [[G3BP1]] (+0.53, fdr 1e-04), [[MCUR1]] (+0.53, fdr 3e-05, ⚠ MCUR1 in the vector space only through flagged drug-doses), [[GSPT1]] (+0.52, fdr 3e-05); moves opposite to [[SPAG4]] (-0.57, fdr 4e-05), [[KBTBD4]] (-0.53, fdr 6e-05), [[ZFPL1]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WFDC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +16.6 | 0e+00 | 42/46 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +13.2 | 4e-37 | 37/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +12.8 | 6e-35 | 35/42 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.72×** | +10.5 | 2e-23 | 43/46 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +10.3 | 8e-23 | 32/43 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +9.1 | 7e-18 | 29/47 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mifepristone (drug)]] 5 µM |  | **1.63×** | +9.0 | 1e-17 | 39/46 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +8.1 | 5e-14 | 35/46 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +7.4 | 1e-11 | 30/47 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Bexarotene (drug)]] 5 µM |  | **1.44×** | +7.0 | 1e-10 | 33/47 (LS 180, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +7.0 | 1e-10 | 26/47 (NCI-H1573, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.42×** | +6.4 | 6e-09 | 30/46 (SW480, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.1 | 4e-08 | 31/46 (NCI-H1573, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Mifepristone (drug)]] 0.05 µM |  | **1.41×** | +6.1 | 6e-08 | 26/46 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **1.30×** | +5.0 | 2e-05 | 26/46 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.28×** | +4.8 | 5e-05 | 18/46 (SW1417, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 6e-05 | 24/46 (NCI-H1573, C-33 A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.8 | 6e-05 | 27/47 (NCI-H1573, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.7 | 6e-05 | 22/46 (HS-578T, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -8.3 | 4e-14 | 38/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.499×** | -7.0 | 9e-10 | 30/46 (A-427, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -4.5 | 0.001 | 22/47 (LS 180, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.805×** | -4.2 | 0.005 | 20/46 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.820×** | -3.8 | 0.016 | 18/46 (NCI-H23, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.826×** | -3.7 | 0.023 | 18/46 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.025 | 20/46 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.025 | 10/46 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.827×** | -3.5 | 0.031 | 21/46 (RKO, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | **0.829×** | -3.4 | 0.038 | 18/47 (LS 180, SNU-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.839× | -3.4 | 0.038 | 16/46 (LS 180, COLO 205, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.038 | 14/47 (PANC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.070 | 17/46 (LS 180, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 163 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.294× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 92.5 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -25.3) |
| [[NCI-H1573 (line)]] | alt | 41.4 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 4.21× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 32.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +14.4) | — |
| [[SW480 (line)]] | alt | 88.7 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +13.8) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 5 µM 0.263× (z -9.9) |
| [[HS-578T (line)]] | alt | 39.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +13.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 122 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +10.5) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.553× (z -8.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 37.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 113 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.115× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 18.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.66× (z +12.9) | — |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +9.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 121 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.426× (z -9.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 23.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.21× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 99.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.208× (z -12.0) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.112× (z -9.1) |
| [[SW 1271 (line)]] | alt | 90.4 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.135× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~5% of this change · without an alert: [[Bergenin (drug)]] 0.5 µM 0.136× (z -8.7) |
| [[A549 (line)]] | wt | 40.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 14.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.69× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 77.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 97.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -9.1) ⚠ toxic |
| [[J82 (line)]] | alt | 46.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 65.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 20.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.73× (z +8.7) | — |
| [[RKO (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.146× (z -15.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 72.6 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.291× (z -8.5) |
| [[A-172 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 81.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROCK2]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[G3BP1]] | +0.53 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[MCUR1]] ⚠ | +0.53 | +0.45 / +0.51 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GSPT1]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[COBL]] | +0.52 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[PPP1R9A]] | +0.52 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SPTBN1]] | +0.52 | +0.24 / +0.49 | both halves | 4e-04 |  |
| [[XK]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TBL1XR1]] | +0.51 | +0.30 / +0.53 | both halves | 2e-04 | pathway: Circadian clock; STRING 403 |
| [[SEPTIN11]] | +0.51 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[VPS13A]] | +0.51 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[TACC1]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PLPP2]] | +0.50 | +0.35 / +0.38 | both halves | 1e-04 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG4]] | -0.57 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[KBTBD4]] | -0.53 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[ZFPL1]] | -0.52 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ZSWIM3]] | -0.51 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[OGFOD2]] | -0.51 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[TMEM208]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NUDT22]] | -0.50 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[COG7]] | -0.49 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[WDR20]] | -0.49 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SYNRG]] | -0.49 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[NOXRED1]] | -0.49 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[BLZF1]] | -0.49 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC3]] | B | WFDC3 activity lowers CPT1A's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.72× higher at baseline in the lines without WFDC3 | 0.016 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[SOAT1]] | C | SOAT1 activity strengthens CPT1A's drug response | lines that do not express SOAT1 (3) vs lines expressing it (45) | the lines without SOAT1 respond 0.57× as strongly (z diff +2.13); strongest at Dinaciclib 5 µM: 0.92x vs 2.09x (z diff +6.1) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **-** arm (projection on the module's main direction -0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-31.7, 31.6); signed map (15.2, -51.4). **Vector** length 109, 28.8% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +16.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.8 | +8.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.2 | +6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.6 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.4 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -7.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | carnitine palmitoyltransferase 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:68,754,620-68,844,410 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPT1-L, L-CPT1; previously CPT1 |
| Gene groups (HGNC) | Carnitine palmitoyltransferase family |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 7 pathways, smallest: Carnitine shuttle; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression; PPARA activates gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P50416](https://www.uniprot.org/uniprotkb/P50416) (Carnitine O-palmitoyltransferase 1, liver isoform):

> Catalyzes the transfer of the acyl group of long-chain fatty acid-CoA conjugates onto carnitine, an essential step for the mitochondrial uptake of long-chain fatty acids and their subsequent beta-oxidation in the mitochondrion. Also possesses a lysine succinyltransferase activity that can regulate enzymatic activity of substrate proteins such as ENO1 and metabolism independent of its classical carnitine O-palmitoyltransferase activity. Plays an important role in hepatic triglyceride metabolism …

**Summary**, from NCBI Gene [1374](https://www.ncbi.nlm.nih.gov/gene/1374):

> The mitochondrial oxidation of long-chain fatty acids is initiated by the sequential action of carnitine palmitoyltransferase I (which is located in the outer membrane and is detergent-labile) and carnitine palmitoyltransferase II (which is located in the inner membrane and is detergent-stable), together with a carnitine-acylcarnitine translocase. CPT I is the key enzyme in the carnitine-dependent transport across the mitochondrial inner membrane and its deficiency results in a decreased rate …

**Accessions** — [HGNC:2328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2328) · Entrez [1374](https://www.ncbi.nlm.nih.gov/gene/1374) · UniProt [P50416](https://www.uniprot.org/uniprotkb/P50416) · Ensembl [ENSG00000110090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110090)

## Data

Gene col 3114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3114); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3114]; `tensor/DDL_lfc|DDL_z.npy` [3114]; `embed/gene_vectors.npy` [3114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3114 or target_col == 3114). Every well: [[CPT1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPT1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

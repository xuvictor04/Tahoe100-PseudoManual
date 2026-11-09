---
symbol: "PCF11"
type: "gene"
col: 9130
ensembl_id: "ENSG00000165494"
name: "PCF11 cleavage and polyadenylation factor subunit"
location: "11q14.1"
module: 23
arm: "+"
pooled_cpm: 88.38
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PCF11

*PCF11 cleavage and polyadenylation factor subunit* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.11× (z +36.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.652× (z -7.8, q 5e-12, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST7L]] (+0.75, fdr 1e-05), [[WARS2-AS1]] (+0.73, fdr 4e-05), [[PPP1R3F]] (+0.73, fdr 1e-05); moves opposite to [[HACE1]] (-0.72, fdr 7e-05), [[ECI2]] (-0.72, fdr 1e-05), [[VDAC3]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.11×** | +36.2 | 0e+00 | 48/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.33×** | +21.8 | 0e+00 | 48/48 (HS-578T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.21×** | +13.8 | 6e-41 | 40/48 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +11.1 | 2e-26 | 42/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +10.4 | 3e-23 | 38/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.74×** | +10.0 | 2e-21 | 40/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +8.2 | 2e-14 | 33/48 (SW480, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.6 | 2e-12 | 34/49 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +7.2 | 3e-11 | 29/45 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.8 | 4e-10 | 31/47 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.8 | 5e-10 | 32/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +6.4 | 9e-09 | 32/48 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.0 | 9e-08 | 29/47 (KATO III, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.8 | 2e-07 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +5.6 | 9e-07 | 33/49 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 6e-04 | 28/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dexmedetomidine (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 9e-04 | 26/49 (RPMI-7951, SW1417, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 25/48 (PANC-1, A498, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 17/48 (NCI-H460, SW 900, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.004 | 27/47 (SW1417, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.652×** | -7.8 | 5e-12 | 40/48 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.753×** | -5.2 | 7e-05 | 32/48 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.780×** | -4.5 | 0.001 | 24/49 (NCI-H23, KATO III, …) | two highest doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.780×** | -4.3 | 0.002 | 25/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.645×** | -4.1 | 0.004 | 20/49 (COLO 205, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.796×** | -4.0 | 0.007 | 22/42 (A-427, NCI-H1573, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.810×** | -3.8 | 0.011 | 21/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.870× | -3.6 | 0.026 | 14/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.031 | 21/47 (NCI-H2030, C-33 A, …) | rises with dose |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.828×** | -3.2 | 0.068 | 17/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.885× | -3.1 | 0.083 | 10/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 0.836× | -3.1 | 0.083 | 19/48 (J82, AsPC-1, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.843× | -3.1 | 0.083 | 18/48 (RKO, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.6 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +28.0) | — |
| [[KATO III (line)]] | alt | 92.8 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +25.5) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 113 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +23.9) | — |
| [[A-172 (line)]] | wt | 95.7 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +24.2) | — |
| [[HS-578T (line)]] | alt | 67.7 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +30.6) | — |
| [[LoVo (line)]] | wt | 97.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +35.4) | — |
| [[NCI-H2347 (line)]] | alt | 49.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +20.7) | — |
| [[COLO 205 (line)]] | alt | 93.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +21.6) | — |
| [[hTERT-HPNE (line)]] | wt | 89.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.95× (z +26.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 101 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +19.1) | — |
| [[RPMI-7951 (line)]] | alt | 86.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +25.0) | — |
| [[SW 900 (line)]] | alt | 100.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +16.5) | — |
| [[AsPC-1 (line)]] | alt | 85.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.7) | — |
| [[H4 (line)]] | wt | 124 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +19.6) | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 117 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +20.8) | [[Dinaciclib (drug)]] 0.05 µM 0.488× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 110 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +28.8) | — |
| [[LS 180 (line)]] | wt | 81.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +19.5) | — |
| [[NCI-H1573 (line)]] | alt | 128 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +28.0) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H1792 (line)]] | alt | 76.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +26.7) | — |
| [[PANC-1 (line)]] | alt | 108 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +22.9) | — |
| [[A-427 (line)]] | wt | 105 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A498 (line)]] | wt | 58.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +21.5) | — |
| [[C32 (line)]] | wt | 97.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +25.3) | — |
| [[CFPAC-1 (line)]] | alt | 48.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +20.9) | — |
| [[HepG2_C3A (line)]] | wt | 76.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +15.0) | — |
| [[J82 (line)]] | alt | 86.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +24.8) | — |
| [[NCI-H23 (line)]] | alt | 96.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[Panc 03.27 (line)]] | alt | 76.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +17.7) | — |
| [[SK-MEL-2 (line)]] | alt | 43.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +24.2) | — |
| [[SNU-1 (line)]] | wt | 53.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 65.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +24.8) | — |
| [[SW1417 (line)]] | alt | 101 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +14.5) | — |
| [[AN3 CA (line)]] | alt | 95.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 97.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 63.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +24.9) | — |
| [[HT-29 (line)]] | alt | 129 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +15.9) | — |
| [[NCI-H2030 (line)]] | alt | 95.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +19.5) | — |
| [[SW48 (line)]] | wt | 95.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.7) | — |
| [[A549 (line)]] | wt | 74.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 85.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 84.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.1) | — |
| [[RKO (line)]] | wt | 88.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 53.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[SW 1088 (line)]] | alt | 85.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 88.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | +0.75 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.73 | +0.72 / +0.42 | both halves | 4e-05 |  |
| [[PPP1R3F]] | +0.73 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.72 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.72 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.72 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[GRK7]] | +0.71 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[C19orf18]] | +0.71 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[MIRLET7IHG]] | +0.70 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[CDKL3]] | +0.70 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.69 | +0.67 / +0.50 | both halves | 1e-05 | STRING 605 |
| [[SMIM15-AS1]] | +0.69 | +0.65 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | -0.72 | -0.75 / -0.38 | both halves | 7e-05 |  |
| [[ECI2]] | -0.72 | -0.73 / -0.49 | both halves | 1e-05 |  |
| [[VDAC3]] | -0.65 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[KIF3A]] | -0.64 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[WASF3]] | -0.62 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[TSPAN33]] | -0.62 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[ATG4C]] | -0.62 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[LCMT1]] | -0.62 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[ARHGAP44]] | -0.61 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[GRB2]] | -0.60 | -0.60 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PCF11's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.1, 8.5); signed map (17.1, -0.2). **Vector** length 130, 39.6% of its response variance represented; |z| ≥ 3 in 1,160 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +21.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +36.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +7.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +3.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.9 | +1.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.0 | -7.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.7 | -5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -6.8 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | PCF11 cleavage and polyadenylation factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:83,156,988-83,187,451 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0824 |
| Gene groups (HGNC) | CTD interacting domain containing |
| Reactome | 11 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [O94913](https://www.uniprot.org/uniprotkb/O94913) (Pre-mRNA cleavage complex 2 protein Pcf11):

> Component of pre-mRNA cleavage complex II, which promotes transcription termination by RNA polymerase II.

**Summary**, from NCBI Gene [51585](https://www.ncbi.nlm.nih.gov/gene/51585):

> The protein encoded by this gene binds to CLP1 to form pre-mRNA cleavage factor IIm. The encoded protein is necessary for efficient Pol II transcription termination and may be involved in degradation of the 3' product of polyA site cleavage. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:30097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30097) · Entrez [51585](https://www.ncbi.nlm.nih.gov/gene/51585) · UniProt [O94913](https://www.uniprot.org/uniprotkb/O94913) · Ensembl [ENSG00000165494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165494)

## Data

Gene col 9130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9130); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9130]; `tensor/DDL_lfc|DDL_z.npy` [9130]; `embed/gene_vectors.npy` [9130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9130 or target_col == 9130). Every well: [[PCF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

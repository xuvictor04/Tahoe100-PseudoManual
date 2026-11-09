---
symbol: "KHDRBS3"
type: "gene"
col: 5243
ensembl_id: "ENSG00000131773"
name: "KH RNA binding domain containing, signal transduction associated 3"
location: "8q24.23"
module: 154
arm: "+"
pooled_cpm: 65.38
n_lines_expressing: 39
n_dd_up: 44
n_dd_down: 23
n_dd_up_clean: 35
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# KHDRBS3

*KH RNA binding domain containing, signal transduction associated 3* — 8q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +15.3, q 0e+00, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.477× (z -10.1, q 2e-21, down in 24 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Binimetinib (drug)]] 0.5 µM: 0.748× (z -4.7, q 6e-04, down in 17 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT12]] (+0.71, fdr 7e-06), [[TNFRSF11A]] (+0.63, fdr 1e-05), [[PKIA]] (+0.62, fdr 1e-05); moves opposite to [[NDUFS1]] (-0.59, fdr 2e-05), [[LSM1]] (-0.57, fdr 3e-05), [[PPWD1]] (-0.56, fdr 3e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +15.3 | 0e+00 | 29/37 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.84×** | +14.8 | 0e+00 | 32/37 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +14.3 | 8e-44 | 34/37 (SW480, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.45×** | +12.7 | 8e-35 | 33/37 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +10.6 | 4e-24 | 31/37 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.92×** | +9.2 | 3e-18 | 29/37 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +9.0 | 1e-17 | 22/36 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +8.4 | 2e-15 | 24/37 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +8.4 | 2e-15 | 31/38 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +8.4 | 3e-15 | 29/37 (NCI-H23, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +8.2 | 1e-14 | 21/37 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.5 | 3e-09 | 18/38 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +6.4 | 6e-09 | 21/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +6.3 | 2e-08 | 22/37 (LS 180, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.56×** | +6.2 | 2e-08 | 21/35 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +5.8 | 2e-07 | 20/37 (SW1417, C32, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +5.4 | 2e-06 | 20/37 (LS 180, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.45×** | +5.0 | 1e-05 | 21/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -10.1 | 2e-21 | 24/32 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.748×** | -4.7 | 6e-04 | 17/37 (C32, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.714×** | -4.7 | 6e-04 | 20/37 (HOP62, NCI-H2347, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.745×** | -4.2 | 0.004 | 20/36 (NCI-H2347, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.751×** | -4.1 | 0.005 | 20/37 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.756×** | -4.0 | 0.006 | 18/36 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.752×** | -3.9 | 0.006 | 20/36 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.825×** | -3.9 | 0.006 | 15/37 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.821×** | -3.8 | 0.008 | 16/38 (HEC-1-A, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.008 | 14/36 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.768×** | -3.8 | 0.008 | 16/37 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.603×** | -3.8 | 0.008 | 16/35 (C32, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.799×** | -3.5 | 0.017 | 15/37 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.774×** | -3.5 | 0.021 | 15/37 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.788×** | -3.4 | 0.024 | 17/37 (HOP62, NCI-H2347, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.025 | 13/37 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.767×** | -3.3 | 0.025 | 20/37 (HOP62, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.843× | -3.3 | 0.025 | 12/37 (C32, SK-MEL-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 290 | 5 | 12 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 18.4× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.258× (z -12.0) |
| [[SW1417 (line)]] | alt | 171 | 9 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -14.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 28.5 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +15.9) | — |
| [[HOP62 (line)]] | alt | 232 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0936× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.138× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 205 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 28.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 20.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 12.3× (z +17.2) | — |
| [[NCI-H23 (line)]] | alt | 24.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.31× (z +13.8) | — |
| [[A498 (line)]] | wt | 57.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +17.8) | — |
| [[KATO III (line)]] | alt | 38.9 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.80× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 79.6 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 187 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0881× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 25.5 | 4 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.30× (z +12.2) ⚠ unreliable plate only · without an alert: [[Tucidinostat (drug)]] 5 µM 3.05× (z +10.4) | — |
| [[A-427 (line)]] | wt | 34.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +12.5) | — |
| [[LoVo (line)]] | wt | 114 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -9.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 208 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 82.8 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.17× (z +12.2) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 2.29× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 63.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -8.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 64.1 | 2 | 0 | [[Ponatinib (drug)]] 5 µM 5.31× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 19.3 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.74× (z +9.4) ⚠ unreliable plate only · without an alert: [[Tucidinostat (drug)]] 5 µM 3.10× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 61.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 41.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +11.2) | — |
| [[A549 (line)]] | wt | 28.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.22× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 17.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.38× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 77.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 22.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.75× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 58.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 31.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.49× (z +10.5) | — |
| [[A-172 (line)]] | wt | 8.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 110 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.64 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT12]] | +0.71 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TNFRSF11A]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PKIA]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.62 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[C3orf52]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[KCNK13]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CELSR1]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[GDPD5]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SEMA7A]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[WSCD1]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NRIP3]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ITPR1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFS1]] | -0.59 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[LSM1]] | -0.57 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PPWD1]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[HECTD1]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TAF8]] | -0.53 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TRAPPC8]] | -0.52 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[ARFGEF2]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises KHDRBS3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[TMEM51]] | C | TMEM51 activity raises KHDRBS3's level | lines that do not express TMEM51 (4) vs lines expressing it (46) | 3.46× lower at baseline in the lines without TMEM51 | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ANKEF1, CEMIP2, AHR; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | B | KHDRBS3 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express KHDRBS3 (11) vs lines expressing it (37) | the lines without KHDRBS3: 0.86× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: AHR, STC2 |
| [[PKIA]] | B | KHDRBS3 activity raises PKIA's level | lines that do not express KHDRBS3 (11) vs lines expressing it (39) | 3.80× lower at baseline in the lines without KHDRBS3 | 0.052 | ⚠ within organs, on part of the lines; also absent: AHR, STC2 |
| [[MYO1D]] | B | KHDRBS3 activity raises MYO1D's level | lines that do not express KHDRBS3 (11) vs lines expressing it (39) | 1.93× lower at baseline in the lines without KHDRBS3 | 0.061 | ⚠ within organs, on part of the lines; also absent: AHR, STC2 |
| [[DYNLT3]] | B | KHDRBS3 activity raises DYNLT3's level | lines that do not express KHDRBS3 (11) vs lines expressing it (39) | 2.03× lower at baseline in the lines without KHDRBS3 | 0.064 | ⚠ within organs, on part of the lines; also absent: AHR, STC2 |
| cells under [[Celecoxib (drug)]] 0.5 µM | B | KHDRBS3 activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express KHDRBS3 (11) vs lines expressing it (37) | the lines without KHDRBS3: 1.22× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: AHR, STC2 |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.3, -1.3); signed map (-2.9, 49.1). **Vector** length 110, 31.8% of its response variance represented; |z| ≥ 3 in 1,244 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +14.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +14.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +8.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +12.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +5.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.9 | -4.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.3 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.5 | +3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.0 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | KH RNA binding domain containing, signal transduction associated 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.23 — chr8:135,457,456-135,656,722 (+) |
| Ensembl biotype | protein_coding |
| Also known as | T-STAR, Etle, etoile, SALP, SLM2, SLM-2 |
| Gene groups (HGNC) | Signal transduction and activation of RNA metabolism family |
| Reactome | 3 pathways, smallest: PTK6 Regulates Proteins Involved in RNA Processing; Signaling by Non-Receptor Tyrosine Kinases; Signaling by PTK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75525](https://www.uniprot.org/uniprotkb/O75525) (KH domain-containing, RNA-binding, signal transduction-associated protein 3):

> RNA-binding protein that plays a role in the regulation of alternative splicing and influences mRNA splice site selection and exon inclusion. Binds preferentially to the 5'-[AU]UAAA-3' motif in vitro. Binds optimally to RNA containing 5'-[AU]UAA-3' as a bipartite motif spaced by more than 15 nucleotides. Binds poly(A). RNA-binding abilities are down-regulated by tyrosine kinase PTK6. Involved in splice site selection of vascular endothelial growth factor. In vitro regulates CD44 alternative …

**Summary**, from NCBI Gene [10656](https://www.ncbi.nlm.nih.gov/gene/10656):

> Enables RNA binding activity; identical protein binding activity; and protein domain specific binding activity. Predicted to be involved in regulation of alternative mRNA splicing, via spliceosome and spermatogenesis. Located in nucleoplasm. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18117) · Entrez [10656](https://www.ncbi.nlm.nih.gov/gene/10656) · UniProt [O75525](https://www.uniprot.org/uniprotkb/O75525) · Ensembl [ENSG00000131773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131773)

## Data

Gene col 5243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5243); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5243]; `tensor/DDL_lfc|DDL_z.npy` [5243]; `embed/gene_vectors.npy` [5243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5243 or target_col == 5243). Every well: [[KHDRBS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KHDRBS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

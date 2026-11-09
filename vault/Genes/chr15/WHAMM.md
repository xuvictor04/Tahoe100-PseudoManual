---
symbol: "WHAMM"
type: "gene"
col: 7959
ensembl_id: "ENSG00000156232"
name: "WASP homolog associated with actin, golgi membranes and microtubules"
location: "15q25.2"
module: 20
arm: "-"
pooled_cpm: 50.54
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 8
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# WHAMM

*WASP homolog associated with actin, golgi membranes and microtubules* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.99× (z +36.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.579× (z -8.3, q 4e-14, down in 29 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.731× (z -5.0, q 9e-05, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN2A1]] (+0.72, fdr 7e-06), [[FBXO6]] (+0.69, fdr 3e-05), [[FNBP4]] (+0.69, fdr 1e-05); moves opposite to [[RPSA]] (-0.66, fdr 1e-05), [[AHCY]] (-0.64, fdr 1e-05), [[CHID1]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CHMP4C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.99×** | +36.0 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.84×** | +28.0 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.49×** | +19.0 | 0e+00 | 47/48 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.49×** | +14.5 | 3e-45 | 47/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +12.8 | 1e-35 | 45/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.19×** | +12.0 | 3e-31 | 41/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.91×** | +10.2 | 1e-22 | 37/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +9.1 | 1e-17 | 39/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.1 | 4e-14 | 32/49 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +7.9 | 1e-13 | 38/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +7.7 | 6e-13 | 40/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +7.1 | 5e-11 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +6.7 | 6e-10 | 39/49 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +6.3 | 2e-08 | 35/48 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +5.7 | 4e-07 | 33/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +5.6 | 7e-07 | 27/48 (RKO, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.006 | 23/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7959.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -8.3 | 4e-14 | 29/38 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.652×** | -6.6 | 1e-08 | 30/48 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.685×** | -5.6 | 5e-06 | 29/43 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.731×** | -5.0 | 9e-05 | 32/49 (HEC-1-A, BT-474, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.770×** | -4.2 | 0.004 | 27/48 (NCI-H1573, SW 1088, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -3.8 | 0.012 | 24/48 (COLO 205, NCI-H2347, …) | two highest doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.795×** | -3.7 | 0.021 | 21/49 (hTERT-HPNE, CFPAC-1, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.029 | 15/48 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.097 | 14/48 (NCI-H1792, HT-29, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.7 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +30.9) | — |
| [[HEC-1-A (line)]] | alt | 56.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +23.1) | — |
| [[LoVo (line)]] | wt | 66.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +30.9) | — |
| [[A549 (line)]] | wt | 74.2 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +21.5) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -12.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 45.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +15.2) | — |
| [[NCI-H2347 (line)]] | alt | 95.2 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +26.0) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -12.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 40.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +22.8) | — |
| [[SW1417 (line)]] | alt | 74.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +21.6) | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 54.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +20.2) | — |
| [[A498 (line)]] | wt | 81.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -11.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 61.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -8.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 35.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +25.1) | — |
| [[HT-29 (line)]] | alt | 65.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +27.9) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 54.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +23.3) | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -9.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +24.2) | — |
| [[LS 180 (line)]] | wt | 36.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +27.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +20.9) | — |
| [[NCI-H1573 (line)]] | alt | 55.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +24.9) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -17.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 77.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +17.8) | — |
| [[SW480 (line)]] | alt | 46.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +24.1) | — |
| [[CFPAC-1 (line)]] | alt | 63.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +20.7) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 87.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -19.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 37.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +19.2) | — |
| [[Panc 03.27 (line)]] | alt | 50.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +16.6) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -13.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 53.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +16.6) | — |
| [[A-427 (line)]] | wt | 26.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +16.2) | — |
| [[HOP62 (line)]] | alt | 26.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +20.6) | — |
| [[Hs 766T (line)]] | wt | 50.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +18.0) | — |
| [[HS-578T (line)]] | alt | 30.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 39.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +19.2) | — |
| [[NCI-H2030 (line)]] | alt | 53.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +18.9) | — |
| [[RPMI-7951 (line)]] | alt | 60.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +16.7) | — |
| [[SNU-1 (line)]] | wt | 42.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 44.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +21.8) | — |
| [[AN3 CA (line)]] | alt | 51.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 37.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.5) | — |
| [[H4 (line)]] | wt | 38.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +17.4) | — |
| [[hTERT-HPNE (line)]] | wt | 33.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +17.7) | — |
| [[NCI-H23 (line)]] | alt | 29.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +13.5) | — |
| [[SHP-77 (line)]] | alt | 31.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.05× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 41.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +17.2) | — |
| [[HCT15 (line)]] | alt | 57.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.2) | — |
| [[HepG2_C3A (line)]] | wt | 46.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A1]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[FBXO6]] | +0.69 | +0.44 / +0.75 | both halves | 3e-05 |  |
| [[FNBP4]] | +0.69 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MITD1]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[GATAD1]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[PPCS]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NKAP]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[PPIG]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | -0.66 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[AHCY]] | -0.64 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[CHID1]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.62 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.62 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.61 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[AGO1]] | -0.61 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[BANF1]] | -0.61 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[ITGB1]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.60 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[C1QBP]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHMP4C]] | B | CHMP4C activity raises WHAMM's level | lines that do not express CHMP4C (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without CHMP4C | 0.074 | ⚠ within organs, on part of the lines; also absent: TSTD1, BTC, TNK1 |
| [[IL15]] | B | IL15 activity raises WHAMM's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without IL15 | 0.089 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.4, -16.3); signed map (1.6, -14.6). **Vector** length 97.4, 29.9% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +28.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +19.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +8.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | -1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -4.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | WASP homolog associated with actin, golgi membranes and microtubules |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:82,809,628-82,836,108 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1971, WHAMM1; previously WHDC1 |
| Gene groups (HGNC) | Wiskott-Aldrich Syndrome protein family |
| Reactome | 4 pathways, smallest: RHOD GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TF30](https://www.uniprot.org/uniprotkb/Q8TF30) (WASP homolog-associated protein with actin, membranes and microtubules):

> Acts as a nucleation-promoting factor (NPF) that stimulates Arp2/3-mediated actin polymerization both at the Golgi apparatus and along tubular membranes. Its activity in membrane tubulation requires F-actin and interaction with microtubules. Proposed to use coordinated actin-nucleating and microtubule-binding activities of distinct WHAMM molecules to drive membrane tubule elongation; when MT-bound can recruit and remodel membrane vesicles but is prevented to activate the Arp2/3 complex. …

**Summary**, from NCBI Gene [123720](https://www.ncbi.nlm.nih.gov/gene/123720):

> This gene encodes a protein that plays a role in actin nucleation, Golgi membrane association and microtubule binding. The encoded protein is a nucleation-promoting factor that regulates the Actin-related protein 2/3 complex. The activated complex initiates growth of new actin filaments by binding to existing actin filaments. The encoded protein also functions in regulation of transport from the endoplasmic reticulum to the Golgi complex and in maintenance of the Golgi complex near the …

**Accessions** — [HGNC:30493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30493) · Entrez [123720](https://www.ncbi.nlm.nih.gov/gene/123720) · UniProt [Q8TF30](https://www.uniprot.org/uniprotkb/Q8TF30) · Ensembl [ENSG00000156232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156232)

## Data

Gene col 7959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7959); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7959]; `tensor/DDL_lfc|DDL_z.npy` [7959]; `embed/gene_vectors.npy` [7959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7959 or target_col == 7959). Every well: [[WHAMM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WHAMM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

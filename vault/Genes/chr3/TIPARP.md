---
symbol: "TIPARP"
type: "gene"
col: 8746
ensembl_id: "ENSG00000163659"
name: "TCDD inducible poly(ADP-ribose) polymerase"
location: "3q25.31"
module: 113
arm: "+"
pooled_cpm: 115.97
n_lines_expressing: 49
n_dd_up: 33
n_dd_down: 9
n_dd_up_clean: 29
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# TIPARP

*TCDD inducible poly(ADP-ribose) polymerase* — 3q25.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.04× (z +19.4, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.524× (z -7.7, q 6e-12, down in 31 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.681× (z -6.8, q 4e-09, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP1]] (+0.68, fdr 7e-06), [[HES1]] (+0.65, fdr 7e-06), [[FOS]] (+0.64, fdr 7e-06); moves opposite to [[KLC1]] (-0.54, fdr 1e-05), [[KCTD13]] (-0.54, fdr 1e-04), [[MFSD8]] (-0.53, fdr 2e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNK5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.04×** | +19.4 | 0e+00 | 45/47 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **16.7×** | +18.2 | 0e+00 | 48/48 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.38×** | +10.2 | 2e-22 | 41/47 (HS-578T, A-427, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +9.9 | 7e-21 | 40/47 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +8.7 | 2e-16 | 42/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.87×** | +8.7 | 3e-16 | 40/47 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.50×** | +6.6 | 3e-09 | 38/47 (HS-578T, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +6.1 | 8e-08 | 39/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.0 | 1e-07 | 32/47 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Menadione (drug)]] 5 µM |  | **1.58×** | +5.4 | 5e-06 | 35/46 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.48×** | +4.8 | 7e-05 | 29/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +4.4 | 4e-04 | 24/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +4.2 | 0.001 | 30/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.90×** | +4.1 | 0.002 | 33/47 (HS-578T, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.005 | 32/47 (SK-MEL-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD1390 (drug)]] 5 µM |  | **1.77×** | +3.7 | 0.009 | 22/47 (LoVo, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.014 | 24/47 (LS 180, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -7.7 | 6e-12 | 31/42 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.681×** | -6.8 | 4e-09 | 28/48 (SW 900, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.610×** | -6.2 | 1e-07 | 31/47 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.652×** | -5.3 | 1e-05 | 27/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.673×** | -4.9 | 8e-05 | 35/47 (A-427, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -4.5 | 5e-04 | 27/47 (HT-29, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -3.8 | 0.011 | 24/46 (HT-29, SHP-77, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.061 | 22/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.752×** | -3.3 | 0.061 | 22/44 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 69.2 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.39× (z +20.5) | — |
| [[NCI-H2347 (line)]] | alt | 194 | 7 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 14.5× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.9) |
| [[A-427 (line)]] | wt | 164 | 5 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 43.7× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.392× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 177 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 211 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +20.9) | [[Ponatinib (drug)]] 5 µM 0.310× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 176 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 43.3× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 181 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 219 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +19.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -12.3) |
| [[C32 (line)]] | wt | 103 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +17.8) | — |
| [[LS 180 (line)]] | wt | 260 | 3 | 2 | [[TAK-901 (drug)]] 5 µM 24.3× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -12.6) |
| [[PANC-1 (line)]] | alt | 42.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +18.5) | — |
| [[A498 (line)]] | wt | 93.7 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 179 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +23.8) | — |
| [[HEC-1-A (line)]] | alt | 50.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +18.1) | — |
| [[HS-578T (line)]] | alt | 73.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +24.3) | — |
| [[SW 900 (line)]] | alt | 244 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 18.8× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.9) |
| [[SW480 (line)]] | alt | 99.9 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 27.2× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -12.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 81.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +19.3) | — |
| [[HOP62 (line)]] | alt | 54.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +16.5) | — |
| [[HT-29 (line)]] | alt | 245 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 58.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +18.1) | — |
| [[J82 (line)]] | alt | 80.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.1) | — |
| [[LoVo (line)]] | wt | 151 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 35.6× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.429× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 43.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 114 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 35.3× (z +16.6) | — |
| [[RKO (line)]] | wt | 70.0 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.23× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -16.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 101 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.0) |
| [[SNU-1 (line)]] | wt | 69.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 24.0× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 165 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.9× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -12.0) |
| [[COLO 205 (line)]] | alt | 160 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 47.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 93.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 17.5× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 114 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 13.6× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 233 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 44.5× (z +16.9) | [[Ponatinib (drug)]] 5 µM 0.330× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 90.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +13.3) | — |
| [[SK-MEL-2 (line)]] | alt | 46.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +14.9) | — |
| [[A-172 (line)]] | wt | 46.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.9× (z +10.5) | — |
| [[A549 (line)]] | wt | 81.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.8× (z +10.9) | — |
| [[CHP-212 (line)]] | wt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +13.4) | — |
| [[SW 1088 (line)]] | alt | 69.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +11.5) | — |
| [[SW 1271 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +8.9) | — |
| [[SW48 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP1]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[HES1]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[FOS]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[TRIB1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TNFAIP3]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[BIRC3]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ZC3H12A]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KLF4]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[BCL6]] | +0.62 | +0.58 / +0.62 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ZFP36]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 | same gene group; pathway: HALLMARK_HYPOXIA; STRING 493 |
| [[JUNB]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PDK4]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC1]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[KCTD13]] | -0.54 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[MFSD8]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PPP1R26-AS1]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[STX16-NPEPL1]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PTPN9]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[GPR161]] | -0.49 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[DIP2A]] | -0.49 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ZNF250]] | -0.48 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[LSP1P4]] | -0.48 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[SANBR]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK5]] | B | KCNK5 activity raises TIPARP's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without KCNK5 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.9, 10.2); signed map (11.3, 29.3). **Vector** length 115, 34.7% of its response variance represented; |z| ≥ 3 in 1,474 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +10.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.2 | +1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +3.7 | +2.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.6 | +0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.6 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.5 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.3 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | TCDD inducible poly(ADP-ribose) polymerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31 — chr3:156,673,235-156,706,770 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434J214, DKFZp686N0351, DDF1, PARP7, PARP-7, PARP-1, pART14, RM1 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Poly(ADP-ribose) polymerases |
| Hallmark sets | HYPOXIA, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3E1](https://www.uniprot.org/uniprotkb/Q7Z3E1) (Protein mono-ADP-ribosyltransferase TIPARP):

> ADP-ribosyltransferase that mediates mono-ADP-ribosylation of glutamate, aspartate and cysteine residues on target proteins. Acts as a negative regulator of AHR by mediating mono-ADP-ribosylation of AHR, leading to inhibit transcription activator activity of AHR.

**Summary**, from NCBI Gene [25976](https://www.ncbi.nlm.nih.gov/gene/25976):

> This gene encodes a member of the poly(ADP-ribose) polymerase superfamily. Studies of the mouse ortholog have shown that the encoded protein catalyzes histone poly(ADP-ribosyl)ation and may be involved in T-cell function. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:23696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23696) · Entrez [25976](https://www.ncbi.nlm.nih.gov/gene/25976) · UniProt [Q7Z3E1](https://www.uniprot.org/uniprotkb/Q7Z3E1) · Ensembl [ENSG00000163659](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163659)

## Data

Gene col 8746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8746); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8746]; `tensor/DDL_lfc|DDL_z.npy` [8746]; `embed/gene_vectors.npy` [8746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8746 or target_col == 8746). Every well: [[TIPARP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIPARP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

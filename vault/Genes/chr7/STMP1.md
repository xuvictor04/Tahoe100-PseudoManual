---
symbol: "STMP1"
type: "gene"
col: 14352
ensembl_id: "ENSG00000243317"
name: "short transmembrane mitochondrial protein 1"
location: "7q33"
module: 25
arm: "+"
pooled_cpm: 38.81
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# STMP1

*short transmembrane mitochondrial protein 1* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.87× (z +24.8, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +9.7, q 6e-20, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.542× (z -15.8, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMC1]] (+0.66, fdr 2e-05), [[UBE2V1]] (+0.66, fdr 2e-05), [[ZMPSTE24]] (+0.65, fdr 2e-05); moves opposite to [[KLHL26]] (-0.65, fdr 1e-05), [[INAFM1]] (-0.63, fdr 1e-05), [[RPAIN]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.87×** | +24.8 | 0e+00 | 45/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +24.2 | 0e+00 | 39/40 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.70×** | +16.8 | 0e+00 | 40/42 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.7 | 6e-20 | 37/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.6 | 9e-20 | 40/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.8 | 8e-07 | 26/48 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +5.1 | 3e-05 | 23/48 (HS-578T, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.9 | 5e-05 | 25/48 (C32, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **1.31×** | +4.8 | 9e-05 | 23/46 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.8 | 9e-05 | 21/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +4.6 | 2e-04 | 24/48 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +4.3 | 8e-04 | 21/47 (SW1417, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 1e-03 | 13/48 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.007 | 20/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.027 | 12/34 (HT-29, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.542×** | -15.8 | 0e+00 | 41/47 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.591×** | -9.6 | 2e-19 | 37/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -6.5 | 1e-08 | 28/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.691×** | -6.5 | 1e-08 | 27/48 (A-427, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -6.3 | 3e-08 | 29/48 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.773×** | -4.7 | 2e-04 | 23/48 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.637×** | -4.3 | 0.001 | 22/48 (NCI-H23, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.807×** | -3.9 | 0.006 | 20/47 (A-427, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.673×** | -3.8 | 0.010 | 21/48 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.818×** | -3.7 | 0.014 | 11/48 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.713×** | -3.2 | 0.064 | 17/47 (NCI-H1792, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.840× | -3.1 | 0.11 | 7/48 (SNU-423, HCT15, …) | rises with dose | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 120 | 2 (2 ⚠) | 11 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.35× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -25.7) |
| [[J82 (line)]] | alt | 29.0 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 44.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.9) | — |
| [[A498 (line)]] | wt | 68.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -12.9) |
| [[C32 (line)]] | wt | 77.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.4) |
| [[HOP62 (line)]] | alt | 38.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +15.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -8.5) |
| [[HT-29 (line)]] | alt | 33.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 31.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.40× (z +17.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 27.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 63.5 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.286× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 32.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -17.3) |
| [[PANC-1 (line)]] | alt | 39.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +17.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -11.3) |
| [[SW480 (line)]] | alt | 39.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +17.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.424× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 18.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.44× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -14.5) |
| [[KATO III (line)]] | alt | 47.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 44.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.43× (z +15.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 21.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.36× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.3) |
| [[SW 900 (line)]] | alt | 28.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.68× (z +12.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 31.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.2) |
| [[A-172 (line)]] | wt | 53.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +12.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 28.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.78× (z +13.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 26.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.04× (z +12.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 37.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.61× (z +9.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.37× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 33.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +17.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 44.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 26.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +12.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 31.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.297× (z -8.7) |
| [[HCT15 (line)]] | alt | 30.4 | 0 | 1 | — | [[LJI308 (drug)]] 5 µM 0.0695× (z -9.0) |
| [[HS-578T (line)]] | alt | 45.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 44.0 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0769× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.5 µM 0.0503× (z -8.7) |
| [[AN3 CA (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMC1]] | +0.66 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[UBE2V1]] | +0.66 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ZMPSTE24]] | +0.65 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[MOB1A]] | +0.64 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MSL3]] | +0.62 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ARPP19]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[FGD5-AS1]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TWF1]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[EMB]] | +0.58 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[MAPKAP1]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ATL3]] | +0.58 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ZNF514]] | +0.58 | +0.39 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL26]] | -0.65 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.63 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RPAIN]] | -0.62 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[LEO1]] | -0.61 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[RASSF7]] | -0.60 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ENKD1]] | -0.60 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[SAT2]] | -0.60 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[TARS2]] | -0.60 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[ZNF10]] | -0.59 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CROCCP2-1]] | -0.58 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[PIM2]] | -0.57 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[BIK]] | -0.57 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STMP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIM2]] | C | PIM2 activity lowers STMP1's level | lines that do not express PIM2 (3) vs lines expressing it (47) | 1.88× higher at baseline in the lines without PIM2 | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: JMJD8, CHD7, CYP2R1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.1, -20.8); signed map (-17.4, -36.9). **Vector** length 73.8, 15.5% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +16.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +24.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +24.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | +0.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.8 | -0.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -15.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -0.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -2.2 | +4.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -0.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.7 | +0.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.6 | -0.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | short transmembrane mitochondrial protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:135,662,496-135,693,418 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PL-5283, Mm47, Mtlbn; previously C7orf73 |
| Matched by | ensembl_id |

**Function**, from UniProt [E0CX11](https://www.uniprot.org/uniprotkb/E0CX11) (Short transmembrane mitochondrial protein 1):

> Microprotein involved in mitochondrial respiratory chain complex III (ubiquinol-cytochrome c oxidoreductase) and complex IV (mitochondrial cytochrome c oxidase complex) assembly. Required for the formation of mitochondrial supercomplexes (SCs). Also required for the activation of the NLRP3 inflammasome (By similarity).

**Summary**, from NCBI Gene [647087](https://www.ncbi.nlm.nih.gov/gene/647087):

> Involved in mitochondrial respirasome assembly and mitochondrial respiratory chain complex IV assembly. Located in mitochondrion. Is active in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:41909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41909) · Entrez [647087](https://www.ncbi.nlm.nih.gov/gene/647087) · UniProt [E0CX11](https://www.uniprot.org/uniprotkb/E0CX11) · Ensembl [ENSG00000243317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243317)

## Data

Gene col 14352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14352); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14352]; `tensor/DDL_lfc|DDL_z.npy` [14352]; `embed/gene_vectors.npy` [14352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14352 or target_col == 14352). Every well: [[STMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

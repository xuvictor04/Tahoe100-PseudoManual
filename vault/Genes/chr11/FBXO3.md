---
symbol: "FBXO3"
type: "gene"
col: 3138
ensembl_id: "ENSG00000110429"
name: "F-box protein 3"
location: "11p13"
module: 45
arm: "+"
pooled_cpm: 34.78
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 14
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# FBXO3

*F-box protein 3* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.10× (z +18.2, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.609× (z -7.9, q 1e-12, down in 36 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.631× (z -7.4, q 3e-11, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSBPL9]] (+0.72, fdr 7e-06), [[MED30]] (+0.72, fdr 7e-06), [[AUH]] (+0.70, fdr 7e-06); moves opposite to [[PPIEL]] (-0.64, fdr 1e-05), [[IDI2-AS1]] (-0.62, fdr 2e-05), [[MPDU1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.10×** | +18.2 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +15.0 | 0e+00 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.90×** | +10.3 | 2e-22 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +9.9 | 6e-21 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +9.8 | 1e-20 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.13×** | +9.6 | 1e-19 | 41/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +8.5 | 1e-15 | 42/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +8.4 | 4e-15 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +6.3 | 2e-08 | 28/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.3 | 2e-08 | 31/47 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +5.6 | 1e-06 | 26/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 2e-05 | 25/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.9 | 4e-05 | 25/47 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.8 | 7e-05 | 25/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.22×** | +4.5 | 2e-04 | 21/47 (A498, RKO, …) | top dose only | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.5 | 3e-04 | 21/48 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 8e-04 | 21/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.001 | 19/48 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.609×** | -7.9 | 1e-12 | 36/48 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -7.4 | 3e-11 | 26/37 (Hs 766T, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.631×** | -7.4 | 3e-11 | 34/48 (SW48, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.649×** | -6.9 | 7e-10 | 26/45 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.545×** | -5.1 | 4e-05 | 29/47 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.597×** | -4.3 | 0.002 | 22/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.643×** | -3.7 | 0.018 | 17/48 (A-172, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.796×** | -3.6 | 0.019 | 12/48 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.660×** | -3.5 | 0.032 | 17/48 (PANC-1, H4, …) | rises with dose | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.806×** | -3.4 | 0.033 | 11/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.034 | 15/47 (J82, HEC-1-A, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.811×** | -3.3 | 0.039 | 11/48 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.812×** | -3.3 | 0.039 | 9/48 (SW48, C-33 A, …) | two highest doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.866× | -3.3 | 0.046 | 12/48 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.054 | 12/48 (SW1417, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.4 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.80× (z +20.9) | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.00× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 34.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.80× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SW480 (line)]] | alt | 38.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +17.7) | — |
| [[AsPC-1 (line)]] | alt | 54.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -8.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 38.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.15× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.313× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 24.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.47× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 54.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -10.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 33.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.57× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 33.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 41.2 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0669× (z -20.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 18.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.13× (z +12.3) | — |
| [[LoVo (line)]] | wt | 28.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.85× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 36.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.75× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 28.2 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 27.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 52.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SHP-77 (line)]] | alt | 39.1 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 38.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[COLO 205 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -13.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 36.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.0) | — |
| [[J82 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.188× (z -9.3) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 48.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +8.5) | — |
| [[SW48 (line)]] | wt | 40.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.203× (z -8.5) |
| [[A-172 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBPL9]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[MED30]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[AUH]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[SNX1]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[USP33]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[NENF]] | +0.65 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.64 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[ZFP14]] | +0.63 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[COPS4]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CAT]] | +0.63 | +0.58 / +0.60 | both halves | 8e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIEL]] | -0.64 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | -0.62 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[MPDU1]] | -0.62 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | -0.61 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[ERI2]] | -0.60 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[PARD6G-AS1]] | -0.60 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[CYREN]] | -0.59 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[PPIEL-1]] | -0.59 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[FBXW10B]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[HCG18]] | -0.58 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[METTL1]] | -0.57 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[MIS12]] | -0.57 | -0.62 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.8, -47.0); signed map (-30.2, -8.3). **Vector** length 93.4, 24.1% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +15.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +9.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.7 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.2 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.9 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:33,740,939-33,774,543 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBX3, FBA |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK99](https://www.uniprot.org/uniprotkb/Q9UK99) (F-box only protein 3):

> Substrate recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex, SCF(FBXO3), which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Mediates the ubiquitination of HIPK2 and probably that of EP300, leading to rapid degradation by the proteasome. In the presence of PML, HIPK2 ubiquitination still occurs, but degradation is prevented. PML, HIPK2 and FBXO3 may act synergically to activate p53/TP53-dependent transactivation. …

**Summary**, from NCBI Gene [26273](https://www.ncbi.nlm.nih.gov/gene/26273):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13582) · Entrez [26273](https://www.ncbi.nlm.nih.gov/gene/26273) · UniProt [Q9UK99](https://www.uniprot.org/uniprotkb/Q9UK99) · Ensembl [ENSG00000110429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110429)

## Data

Gene col 3138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3138); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3138]; `tensor/DDL_lfc|DDL_z.npy` [3138]; `embed/gene_vectors.npy` [3138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3138 or target_col == 3138). Every well: [[FBXO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

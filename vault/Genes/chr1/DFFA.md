---
symbol: "DFFA"
type: "gene"
col: 8291
ensembl_id: "ENSG00000160049"
name: "DNA fragmentation factor subunit alpha"
location: "1p36.22"
module: 4
arm: "+"
pooled_cpm: 53.36
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DFFA

*DNA fragmentation factor subunit alpha* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.91× (z +16.1, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.638× (z -9.6, q 6e-19, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP1]] (+0.69, fdr 7e-06), [[NEIL2]] (+0.69, fdr 7e-06), [[TMEM161A]] (+0.69, fdr 7e-06); moves opposite to [[TAPT1]] (-0.62, fdr 3e-05), [[CDKN1B]] (-0.60, fdr 2e-05), [[CMC4]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +16.1 | 0e+00 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +15.6 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +15.4 | 0e+00 | 46/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +13.8 | 4e-41 | 39/42 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.34×** | +12.8 | 1e-35 | 45/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +10.2 | 1e-22 | 40/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +10.1 | 4e-22 | 40/44 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +8.4 | 4e-15 | 38/48 (HEC-1-A, RKO, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +8.0 | 1e-13 | 40/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +7.9 | 1e-13 | 37/48 (RKO, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.63×** | +7.1 | 8e-11 | 41/47 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +6.9 | 2e-10 | 37/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +6.6 | 2e-09 | 36/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +6.6 | 2e-09 | 34/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +6.4 | 6e-09 | 38/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.4 | 3e-06 | 28/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.2 | 7e-06 | 26/48 (NCI-H1573, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.76×** | +4.5 | 2e-04 | 29/48 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +4.3 | 6e-04 | 29/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.2 | 6e-04 | 20/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.638×** | -9.6 | 6e-19 | 35/48 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -4.7 | 7e-04 | 28/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -4.6 | 7e-04 | 28/49 (PANC-1, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.644×** | -3.5 | 0.073 | 20/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.660× | -3.3 | 0.12 | 17/48 (COLO 205, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.863× | -3.1 | 0.14 | 11/48 (NCI-H2030, SNU-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.812× | -3.1 | 0.14 | 21/48 (NCI-H23, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 38.6 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.27× (z +13.3) | — |
| [[NCI-H23 (line)]] | alt | 178 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -19.1) |
| [[SW480 (line)]] | alt | 61.2 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +15.2) | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.09× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 66.6 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.81× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 43.6 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 87.8 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.05 µM 2.08× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -11.4) |
| [[A498 (line)]] | wt | 29.0 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.77× (z +9.4) | — |
| [[A549 (line)]] | wt | 29.9 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.87× (z +9.6) | — |
| [[KATO III (line)]] | alt | 37.8 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 31.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.30× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.82× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 33.1 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.82× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -11.7) |
| [[RKO (line)]] | wt | 74.4 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.57× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.4) |
| [[A-172 (line)]] | wt | 23.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.45× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 34.4 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 5.14× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.1) |
| [[Hs 766T (line)]] | wt | 40.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.83× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 191 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.33× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -17.3) |
| [[SNU-423 (line)]] | alt | 41.6 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.27× (z +9.9) | — |
| [[A-427 (line)]] | wt | 95.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 17.9 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.99× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 38.9 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.20× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.7) |
| [[H4 (line)]] | wt | 39.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 39.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.64× (z +10.0) | — |
| [[J82 (line)]] | alt | 49.3 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.18× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.7) |
| [[LoVo (line)]] | wt | 57.1 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.77× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.2) |
| [[LS 180 (line)]] | wt | 37.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.31× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.63× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 48.7 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.45× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 66.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.58× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.03× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 44.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 22.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.1) |
| [[C32 (line)]] | wt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP1]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NEIL2]] | +0.69 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[BCCIP]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[CCT2]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[NUDC]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CCT3]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[NCLN]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.64 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CCT4]] | +0.62 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAPT1]] | -0.62 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[CDKN1B]] | -0.60 | -0.48 / -0.64 | both halves | 2e-05 | pathway: HALLMARK_APOPTOSIS |
| [[CMC4]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[LNX2]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[FBXO8]] | -0.55 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[HLA-A]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.55 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[DLEU2]] | -0.55 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[CGGBP1]] | -0.55 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[IKZF4]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CDKN2C]] | -0.54 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[ATP23]] | -0.53 | -0.43 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.5, -39.3); signed map (-10.7, -55.5). **Vector** length 100, 31.4% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.55 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.53 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.8 | +10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.6 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +6.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.1 | -9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | +0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -0.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | DNA fragmentation factor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:10,456,522-10,472,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DFF-45, DFF45, ICAD, DFF1 |
| Gene groups (HGNC) | DNA fragmentation factor subunits |
| Hallmark sets | APOPTOSIS |
| Reactome | 4 pathways, smallest: Apoptosis induced DNA fragmentation; Apoptotic execution phase; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O00273](https://www.uniprot.org/uniprotkb/O00273) (DNA fragmentation factor subunit alpha):

> Inhibitor of the caspase-activated DNase (DFF40).

**Summary**, from NCBI Gene [1676](https://www.ncbi.nlm.nih.gov/gene/1676):

> Apoptosis is a cell death process that removes toxic and/or useless cells during mammalian development. The apoptotic process is accompanied by shrinkage and fragmentation of the cells and nuclei and degradation of the chromosomal DNA into nucleosomal units. DNA fragmentation factor (DFF) is a heterodimeric protein of 40-kD (DFFB) and 45-kD (DFFA) subunits. DFFA is the substrate for caspase-3 and triggers DNA fragmentation during apoptosis. DFF becomes activated when DFFA is cleaved by …

**Accessions** — [HGNC:2772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2772) · Entrez [1676](https://www.ncbi.nlm.nih.gov/gene/1676) · UniProt [O00273](https://www.uniprot.org/uniprotkb/O00273) · Ensembl [ENSG00000160049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160049)

## Data

Gene col 8291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8291); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8291]; `tensor/DDL_lfc|DDL_z.npy` [8291]; `embed/gene_vectors.npy` [8291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8291 or target_col == 8291). Every well: [[DFFA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DFFA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

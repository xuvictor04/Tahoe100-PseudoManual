---
symbol: "CCDC66"
type: "gene"
col: 11104
ensembl_id: "ENSG00000180376"
name: "coiled-coil domain containing 66"
location: "3p14.3"
module: 36
arm: "+"
pooled_cpm: 45.61
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# CCDC66

*coiled-coil domain containing 66* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +11.7, q 5e-29, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.566× (z -12.5, q 7e-33, down in 39 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.675× (z -8.6, q 2e-15, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP3S2]] (+0.58, fdr 3e-05), [[DHX29]] (+0.57, fdr 1e-05), [[PTPMT1]] (+0.57, fdr 5e-05); moves opposite to [[SLC6A8]] (-0.56, fdr 1e-05), [[HAPSTR1]] (-0.55, fdr 3e-05), [[TUBB3]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +11.7 | 5e-29 | 32/47 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +11.6 | 2e-28 | 35/47 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +9.0 | 4e-17 | 32/47 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +8.7 | 3e-16 | 31/47 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +7.9 | 3e-13 | 35/47 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.7 | 1e-12 | 31/46 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.39×** | +7.2 | 4e-11 | 27/47 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.38×** | +7.0 | 2e-10 | 32/47 (A-172, AsPC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +6.6 | 2e-09 | 29/47 (NCI-H2347, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +6.5 | 4e-09 | 28/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 1e-06 | 28/47 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +5.4 | 4e-06 | 26/47 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +5.3 | 4e-06 | 25/47 (AsPC-1, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.23×** | +4.4 | 4e-04 | 17/46 (RKO, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 5e-04 | 21/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.2 | 8e-04 | 18/47 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.003 | 13/47 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.034 | 9/47 (SNU-423, KATO III, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.043 | 10/48 (RKO, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.566×** | -12.5 | 7e-33 | 39/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -8.6 | 2e-15 | 33/47 (A-427, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.587×** | -6.1 | 2e-07 | 31/47 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.748×** | -5.9 | 7e-07 | 25/44 (A-427, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.807×** | -4.5 | 7e-04 | 22/43 (A-172, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.806×** | -4.5 | 8e-04 | 22/47 (SW 900, HCT15, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.842× | -3.8 | 0.014 | 18/46 (RKO, SW480, …) | two highest doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.789×** | -3.7 | 0.014 | 12/47 (Hs 766T, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.845× | -3.7 | 0.014 | 10/47 (NCI-H1573, RKO, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.730×** | -3.6 | 0.018 | 14/47 (HEC-1-A, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.032 | 8/47 (SW480, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.956× | -3.4 | 0.032 | 0/48 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.861× | -3.3 | 0.048 | 20/46 (RKO, SHP-77, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.754×** | -3.2 | 0.049 | 15/47 (HEC-1-A, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Hesperidin (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.077 | 9/47 (A-172, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 87.6 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +16.0) | [[Lonafarnib (drug)]] 5 µM 0.194× (z -11.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.498× (z -9.0) |
| [[RKO (line)]] | wt | 84.2 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 63.9 | 3 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.00× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.533× (z -9.2) |
| [[LoVo (line)]] | wt | 53.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 35.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 36.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.7) | — |
| [[A-427 (line)]] | wt | 60.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.407× (z -10.2) |
| [[HCT15 (line)]] | alt | 41.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 38.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 64.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 75.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -21.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 66.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.4) | — |
| [[A-172 (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -22.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -19.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 94.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -11.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 47.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.359× (z -9.1) |
| [[H4 (line)]] | wt | 21.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0933× (z -11.5) |
| [[HOP62 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.100× (z -11.6) ⚠ toxic |
| [[J82 (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 39.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 73.0 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.131× (z -9.0) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 72.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.117× (z -8.6) |
| [[A498 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3S2]] | +0.58 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[DHX29]] | +0.57 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PTPMT1]] | +0.57 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[AGO4]] | +0.56 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[TRAPPC13]] | +0.56 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[RSBN1L]] | +0.55 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[PCGF6]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[C15orf61]] ⚠ | +0.54 | +0.50 / +0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC38A9]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LIN9]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[NSMCE4A]] | +0.52 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[NDUFS6]] | +0.52 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[MTFMT]] | +0.52 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A8]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[HAPSTR1]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[TUBB3]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CTSB]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PFKP]] | -0.51 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[PKM]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[IDS]] | -0.49 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[FLNA]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[BAIAP2]] | -0.47 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[YWHAZ]] | -0.47 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[MARCKSL1]] | -0.47 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[RALY]] | -0.47 | -0.58 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.323). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-19.0, -47.8); signed map (-16.3, -11.3). **Vector** length 98.2, 23.4% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.1 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.9 | -8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -6.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | +0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 66 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:56,557,161-56,621,837 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686C0433 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [A2RUB6](https://www.uniprot.org/uniprotkb/A2RUB6) (Coiled-coil domain-containing protein 66):

> Microtubule-binding protein required for ciliogenesis. May function in ciliogenesis by mediating the transport of proteins like BBS4 to the cilium, but also through the organization of the centriolar satellites. Required for the assembly of signaling-competent cilia with proper structure and length. Mediates this function in part by regulating transition zone assembly and basal body recruitment of the IFT-B complex. Cooperates with the ciliopathy proteins CSPP1 and CEP104 during cilium length …

**Summary**, from NCBI Gene [285331](https://www.ncbi.nlm.nih.gov/gene/285331):

> Enables identical protein binding activity and microtubule binding activity. Involved in several processes, including ciliary transition zone assembly; microtubule cytoskeleton organization; and mitotic metaphase chromosome alignment. Located in cytoskeleton; midbody; and photoreceptor inner segment. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27709) · Entrez [285331](https://www.ncbi.nlm.nih.gov/gene/285331) · UniProt [A2RUB6](https://www.uniprot.org/uniprotkb/A2RUB6) · Ensembl [ENSG00000180376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180376)

## Data

Gene col 11104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11104); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11104]; `tensor/DDL_lfc|DDL_z.npy` [11104]; `embed/gene_vectors.npy` [11104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11104 or target_col == 11104). Every well: [[CCDC66 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC66.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

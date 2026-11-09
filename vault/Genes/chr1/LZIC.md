---
symbol: "LZIC"
type: "gene"
col: 8521
ensembl_id: "ENSG00000162441"
name: "leucine zipper and CTNNBIP1 domain containing"
location: "1p36.22"
module: 88
arm: "+"
pooled_cpm: 31.42
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# LZIC

*leucine zipper and CTNNBIP1 domain containing* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +14.6, q 1e-45, up in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.72× (z +7.3, q 4e-11, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.778× (z -4.7, q 7e-04, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF764]] (+0.76, fdr 7e-06), [[BPTF]] (+0.76, fdr 7e-06), [[LARP7]] (+0.76, fdr 7e-06); moves opposite to [[SDHAP1]] (-0.71, fdr 1e-05), [[SDHAP4]] (-0.70, fdr 1e-05), [[IGSF8]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR2F1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.15×** | +14.6 | 1e-45 | 39/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +14.1 | 1e-42 | 42/45 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +13.6 | 1e-39 | 34/38 (Hs 766T, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +8.3 | 2e-14 | 32/42 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +7.3 | 4e-11 | 37/47 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.64×** | +6.4 | 1e-08 | 30/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.3 | 1e-05 | 34/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +5.1 | 3e-05 | 28/48 (C32, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.6 | 3e-04 | 25/48 (SW480, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.30×** | +3.5 | 0.023 | 22/45 (A498, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.19× | +3.4 | 0.039 | 16/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.040 | 19/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8521.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.778×** | -4.7 | 7e-04 | 28/48 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -4.7 | 7e-04 | 32/48 (SNU-1, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.717×** | -4.4 | 0.002 | 26/48 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.720×** | -4.4 | 0.002 | 27/48 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -3.7 | 0.021 | 24/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.590×** | -3.7 | 0.021 | 17/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -3.5 | 0.034 | 21/48 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.5 | 0.036 | 2/48 (CHP-212, SW 1088) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.775×** | -3.4 | 0.042 | 23/48 (RPMI-7951, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tadalafil (drug)]] 5 µM |  | **0.783×** | -3.1 | 0.096 | 17/48 (LoVo, AsPC-1, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.786× | -3.1 | 0.10 | 18/48 (HOP62, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 57.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +16.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 41.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 30.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +18.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-423 (line)]] | alt | 24.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +14.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 11.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 20.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 23.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 28.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 31.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 31.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 43.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +10.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 31.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 19.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +14.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 42.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 39.3 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0904× (z -9.4) |
| [[C-33 A (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 66.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +8.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.20× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +11.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF764]] | +0.76 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[BPTF]] | +0.76 | +0.82 / +0.67 | both halves | 7e-06 |  |
| [[LARP7]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.75 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[DARS1]] | +0.75 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[ST7L]] | +0.75 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[LYRM2]] | +0.74 | +0.82 / +0.54 | both halves | 1e-05 |  |
| [[OCIAD1]] | +0.74 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.74 | +0.80 / +0.57 | both halves | 9e-06 |  |
| [[TRMT13]] | +0.73 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[GTF2H1]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | +0.73 | +0.80 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | -0.71 | -0.77 / -0.53 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.70 | -0.79 / -0.51 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.69 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.68 | -0.73 / -0.46 | both halves | 2e-05 |  |
| [[METAP1]] | -0.67 | -0.73 / -0.47 | both halves | 2e-05 |  |
| [[LPCAT4]] | -0.67 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.67 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[NME2]] | -0.67 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[PMS2P3-1]] | -0.67 | -0.75 / -0.55 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.67 | -0.73 / -0.40 | both halves | 5e-05 |  |
| [[RNF4]] | -0.66 | -0.76 / -0.51 | both halves | 1e-05 |  |
| [[SMARCD2]] | -0.66 | -0.69 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2F1-AS1]] | B | NR2F1-AS1 activity raises LZIC's level | lines that do not express NR2F1-AS1 (8) vs lines expressing it (42) | 1.16× lower at baseline in the lines without NR2F1-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: TGFB1, NR2F1, PCDH15 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises LZIC's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises LZIC's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-24.5, 8.6); signed map (11.5, -25.2). **Vector** length 91.3, 22.9% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +12.4 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.0 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +8.2 | +6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine zipper and CTNNBIP1 domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:9,922,113-9,943,407 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15436 |
| Matched by | ensembl_id |

UniProt [Q8WZA0](https://www.uniprot.org/uniprotkb/Q8WZA0) carries no function annotation.

**Summary**, from NCBI Gene [84328](https://www.ncbi.nlm.nih.gov/gene/84328):

> Predicted to enable beta-catenin binding activity. Predicted to be involved in response to ionizing radiation. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17497) · Entrez [84328](https://www.ncbi.nlm.nih.gov/gene/84328) · UniProt [Q8WZA0](https://www.uniprot.org/uniprotkb/Q8WZA0) · Ensembl [ENSG00000162441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162441)

## Data

Gene col 8521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8521); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8521]; `tensor/DDL_lfc|DDL_z.npy` [8521]; `embed/gene_vectors.npy` [8521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8521 or target_col == 8521). Every well: [[LZIC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LZIC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

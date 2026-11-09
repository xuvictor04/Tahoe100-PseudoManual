---
symbol: "TRIM23"
type: "gene"
col: 3480
ensembl_id: "ENSG00000113595"
name: "tripartite motif containing 23"
location: "5q12.3"
module: 74
arm: "+"
pooled_cpm: 40.84
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# TRIM23

*tripartite motif containing 23* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.64× (z +10.5, q 5e-23, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.388× (z -20.1, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.479× (z -8.2, q 3e-14, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIR1]] (+0.87, fdr 7e-06), [[ZNHIT3]] (+0.80, fdr 7e-06), [[ASB8]] (+0.79, fdr 7e-06); moves opposite to [[SMG1P3]] (-0.63, fdr 1e-05), [[UBE2G2]] (-0.61, fdr 1e-05), [[AHCY]] (-0.59, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00888-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +10.5 | 5e-23 | 36/48 (RKO, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +9.0 | 6e-17 | 28/48 (HT-29, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +8.7 | 7e-16 | 32/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +7.4 | 2e-11 | 32/48 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +6.5 | 7e-09 | 28/48 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +5.3 | 1e-05 | 24/48 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +5.2 | 2e-05 | 20/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.9 | 6e-05 | 20/48 (C-33 A, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.16× | +4.5 | 5e-04 | 20/48 (Panc 03.27, RKO, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 7e-04 | 23/48 (RKO, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +4.3 | 8e-04 | 22/49 (LoVo, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.013 | 16/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.12× | +3.5 | 0.020 | 2/48 (A498, HT-29) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.099 | 7/48 (PANC-1, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3480.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.388×** | -20.1 | 0e+00 | 47/48 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.480×** | -15.6 | 0e+00 | 41/47 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -13.2 | 1e-37 | 29/39 (Panc 03.27, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.553×** | -11.7 | 3e-29 | 34/44 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.479×** | -8.2 | 3e-14 | 35/48 (CFPAC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.484×** | -8.1 | 7e-14 | 37/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.485×** | -8.0 | 7e-14 | 35/48 (NCI-H460, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -7.2 | 6e-11 | 27/48 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.529×** | -7.1 | 9e-11 | 30/48 (NCI-H2347, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -6.9 | 2e-10 | 3/49 (NCI-H661, COLO 205, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.579×** | -6.1 | 6e-08 | 27/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.756×** | -6.0 | 1e-07 | 25/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.797×** | -4.8 | 6e-05 | 22/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 0.5 µM |  | **0.758×** | -4.2 | 0.001 | 19/48 (A498, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.786×** | -3.7 | 0.009 | 15/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.846× | -3.4 | 0.024 | 15/48 (SNU-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.900× | -3.2 | 0.046 | 7/48 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.817×** | -3.1 | 0.060 | 12/48 (NCI-H460, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.081 | 6/48 (A498, HCT15, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.908× | -2.9 | 0.091 | 13/48 (HS-578T, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.5 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.409× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 37.5 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.211× (z -14.4) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 55.4 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -13.6) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 49.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 80.4 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.326× (z -13.9) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 50.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -9.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -10.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 53.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -12.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 38.2 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.375× (z -11.9) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 53.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 50.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.4 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.325× (z -11.2) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 37.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 61.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0797× (z -22.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 34.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +9.0) | — |
| [[SW480 (line)]] | alt | 37.5 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.439× (z -9.5) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -12.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -12.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -11.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.211× (z -13.5) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.323× (z -9.2) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 42.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.314× (z -10.2) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -8.5) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -8.9) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.148× (z -10.9) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIR1]] | +0.87 | +0.84 / +0.85 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.80 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[ASB8]] | +0.79 | +0.82 / +0.73 | both halves | 7e-06 |  |
| [[ACOT8]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[FRG1]] | +0.76 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[CRBN]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[SECISBP2L]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[IK]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[SYF2]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[EAPP]] | +0.72 | +0.66 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P3]] | -0.63 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[AHCY]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.59 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[NUP188]] | -0.58 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[LRP8]] | -0.58 | -0.57 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00888-1]] | B | LINC00888-1 activity raises TRIM23's level | lines that do not express LINC00888-1 (7) vs lines expressing it (43) | 1.37× lower at baseline in the lines without LINC00888-1 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers TRIM23's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.0, -28.3); signed map (-15.0, -5.9). **Vector** length 117, 31.7% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.0 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.4 | -20.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.7 | -11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -15.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.2 | -8.0 |
|  | [[EX229 (drug)]] 5 µM |  | -5.9 | -6.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.8 | -8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.7 | -8.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.4 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:65,589,690-65,625,975 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARD1, RNF46; previously ARFD1 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; ARF GTPase family; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [P36406](https://www.uniprot.org/uniprotkb/P36406) (E3 ubiquitin-protein ligase TRIM23):

> E3 ubiquitin ligase that harbors GTPase activity encoded by the C-terminal ARF domain. Plays an essential role in autophagy activation during viral infection. Mechanistically, activates TANK-binding kinase 1/TBK1 by facilitating its dimerization and ability to phosphorylate the selective autophagy receptor SQSTM1. In order to achieve this function, TRIM23 mediates 'Lys-27'-linked auto-ubiquitination of its ADP-ribosylation factor (ARF) domain to induce its GTPase activity and its recruitment to …

**Summary**, from NCBI Gene [373](https://www.ncbi.nlm.nih.gov/gene/373):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This protein is also a member of the ADP ribosylation factor family of guanine nucleotide-binding family of proteins. Its carboxy terminus contains an ADP-ribosylation factor domain and a guanine nucleotide binding site, while the amino terminus contains a GTPase activating protein domain …

**Accessions** — [HGNC:660](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:660) · Entrez [373](https://www.ncbi.nlm.nih.gov/gene/373) · UniProt [P36406](https://www.uniprot.org/uniprotkb/P36406) · Ensembl [ENSG00000113595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113595)

## Data

Gene col 3480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3480); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3480]; `tensor/DDL_lfc|DDL_z.npy` [3480]; `embed/gene_vectors.npy` [3480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3480 or target_col == 3480). Every well: [[TRIM23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

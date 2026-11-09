---
symbol: "KLF5"
type: "gene"
col: 2256
ensembl_id: "ENSG00000102554"
name: "KLF transcription factor 5"
location: "13q22.1"
module: 31
arm: "+"
pooled_cpm: 181.13
n_lines_expressing: 32
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 43
direction_downstream: 61
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# KLF5

*KLF transcription factor 5* — 13q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.63× (z +31.5, q 0e+00, up in 25 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.648× (z -9.7, q 3e-19, down in 23 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.639× (z -5.4, q 2e-05, down in 19 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP3A5]] (+0.63, fdr 2e-05), [[SDR16C5]] (+0.61, fdr 2e-05), [[CD55]] (+0.61, fdr 1e-05); moves opposite to [[THOC5]] (-0.48, fdr 3e-05), [[IPO11]] (-0.46, fdr 3e-05), [[SEPHS1]] (-0.46, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[AQP3]] → it (grade B ⚠); 61 go from it, the strongest it → [[TCF7L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.63×** | +31.5 | 0e+00 | 25/30 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.79×** | +23.7 | 0e+00 | 26/30 (C32, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.82×** | +23.0 | 0e+00 | 27/30 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +14.1 | 5e-43 | 26/30 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +13.7 | 1e-40 | 24/30 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +12.4 | 2e-33 | 20/30 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +11.8 | 3e-30 | 20/30 (Panc 03.27, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +9.4 | 6e-19 | 26/31 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +9.2 | 3e-18 | 24/31 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +9.1 | 7e-18 | 24/30 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +8.6 | 3e-16 | 26/30 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +6.6 | 2e-09 | 11/30 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.29×** | +5.8 | 3e-07 | 14/30 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.6 | 7e-07 | 21/30 (SW1417, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +5.2 | 7e-06 | 10/30 (NCI-H2030, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.5 | 2e-04 | 12/30 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.002 | 3/30 (C-33 A, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -9.7 | 3e-19 | 23/29 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.639×** | -5.4 | 2e-05 | 19/30 (CFPAC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.650×** | -5.2 | 3e-05 | 19/30 (CFPAC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.823×** | -4.5 | 9e-04 | 22/31 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | 0.875× | -4.2 | 0.003 | 11/30 (HepG2/C3A, BT-474, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.844× | -3.9 | 0.007 | 14/30 (NCI-H2347, LoVo, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.845× | -3.9 | 0.007 | 15/30 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.746×** | -3.5 | 0.028 | 13/30 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.868× | -3.3 | 0.061 | 11/30 (BT-474, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.865× | -3.1 | 0.10 | 8/30 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.877× | -3.0 | 0.11 | 2/31 (J82, NCI-H2122) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.778× | -3.0 | 0.11 | 15/30 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 410 | 1 | 15 (11 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -33.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.395× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 383 | 10 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 58.3 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +20.8) | — |
| [[LS 180 (line)]] | wt | 636 | 2 | 9 (7 ⚠) | [[Harringtonine (drug)]] 5 µM 1.84× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.470× (z -12.4) |
| [[HT-29 (line)]] | alt | 525 | 2 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.550× (z -8.6) |
| [[SW48 (line)]] | wt | 595 | 2 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.66× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -21.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.332× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 158 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 60.0 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +20.7) | — |
| [[NCI-H2347 (line)]] | alt | 137 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -15.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 207 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +22.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 538 | 3 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -26.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 57.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.54× (z +25.6) | — |
| [[Hs 766T (line)]] | wt | 416 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 144 | 2 | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.97× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 62.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +20.3) | — |
| [[A-427 (line)]] | wt | 51.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +18.3) | — |
| [[A549 (line)]] | wt | 214 | 2 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.04× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 273 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.65× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -13.0) |
| [[J82 (line)]] | alt | 86.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.16× (z +25.1) | — |
| [[SW480 (line)]] | alt | 322 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -13.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 394 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.48× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -23.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 51.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +26.1) | — |
| [[LoVo (line)]] | wt | 612 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -27.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 280 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -13.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 115 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.314× (z -8.6) |
| [[COLO 205 (line)]] | alt | 513 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -14.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 71.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.0) | — |
| [[C-33 A (line)]] | alt | 63.8 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.79× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 51.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.02× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 41.4 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 43.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 31.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 35.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 30.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 37.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 44.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 31.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 44.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 27.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP3A5]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[SDR16C5]] | +0.61 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[CD55]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[FLRT3]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[TRIB1]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[EZR]] | +0.59 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[FOXO1]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TXNIP]] | +0.57 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[GPR37]] | +0.57 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[USP53]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[C11orf96]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[LIPH]] | +0.56 | +0.38 / +0.68 | both halves | 7e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC5]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[IPO11]] | -0.46 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SEPHS1]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SNRNP40]] | -0.46 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[LIG3]] | -0.46 | -0.38 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 27, C 16. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | B | AQP3 activity raises KLF5's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 4.68× lower at baseline in the lines without AQP3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[CYP3A5]] | B | CYP3A5 activity raises KLF5's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 4.44× lower at baseline in the lines without CYP3A5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[JUP]] | B | JUP activity raises KLF5's level | lines that do not express JUP (16) vs lines expressing it (34) | 4.07× lower at baseline in the lines without JUP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[CEACAM1]] | B | CEACAM1 activity raises KLF5's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 3.72× lower at baseline in the lines without CEACAM1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[PI3]] | B | PI3 activity raises KLF5's level | lines that do not express PI3 (27) vs lines expressing it (23) | 2.38× lower at baseline in the lines without PI3 | 0.007 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[LAMB3]] | B | LAMB3 activity raises KLF5's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 4.51× lower at baseline in the lines without LAMB3 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[TMC5]] | B | TMC5 activity raises KLF5's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 4.60× lower at baseline in the lines without TMC5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[IL2RG]] | B | IL2RG activity raises KLF5's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.85× lower at baseline in the lines without IL2RG | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[EFNB2]] | B | EFNB2 activity raises KLF5's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 3.12× lower at baseline in the lines without EFNB2 | 0.012 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[GSDMC]] | B | GSDMC activity raises KLF5's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 3.20× lower at baseline in the lines without GSDMC | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[C4BPB]] | B | C4BPB activity raises KLF5's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 5.19× lower at baseline in the lines without C4BPB | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[LMO7]] | B | LMO7 activity raises KLF5's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 3.39× lower at baseline in the lines without LMO7 | 0.019 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |

### Downstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 46, C 15. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF7L2]] | B | KLF5 activity raises TCF7L2's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without KLF5 | 0.001 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[JUP]] | B | KLF5 activity raises JUP's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 3.70× lower at baseline in the lines without KLF5 | 0.001 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[USP53]] | B | KLF5 activity raises USP53's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without KLF5 | 0.003 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[NEDD9]] | B | KLF5 activity raises NEDD9's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.79× lower at baseline in the lines without KLF5 | 0.005 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[THOC5]] | B | KLF5 activity lowers THOC5's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.27× higher at baseline in the lines without KLF5 | 0.006 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[TES]] | B | KLF5 activity raises TES's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 3.53× lower at baseline in the lines without KLF5 | 0.006 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[EPS8L1]] | B | KLF5 activity raises EPS8L1's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.52× lower at baseline in the lines without KLF5 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[S100A10]] | B | KLF5 activity raises S100A10's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.56× lower at baseline in the lines without KLF5 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[LMO7]] | B | KLF5 activity raises LMO7's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 3.12× lower at baseline in the lines without KLF5 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[EZR]] | B | KLF5 activity raises EZR's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.17× lower at baseline in the lines without KLF5 | 0.009 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[PTK6]] | B | KLF5 activity raises PTK6's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without KLF5 | 0.012 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[PARD6B]] | B | KLF5 activity raises PARD6B's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.81× lower at baseline in the lines without KLF5 | 0.014 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, 57.8); signed map (9.2, 31.3). **Vector** length 126, 36.9% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.1 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +23.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +12.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +23.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +4.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.7 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.5 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | +0.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.1 — chr13:73,054,976-73,077,541 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IKLF, CKLF; previously BTEB2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Hallmark sets | MYOGENESIS |
| Reactome | 3 pathways, smallest: Transcriptional regulation of granulopoiesis; Transcriptional regulation of white adipocyte differentiation; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13887](https://www.uniprot.org/uniprotkb/Q13887) (Krueppel-like factor 5):

> Transcription factor that binds to GC box promoter elements. Activates the transcription of these genes.

**Summary**, from NCBI Gene [688](https://www.ncbi.nlm.nih.gov/gene/688):

> This gene encodes a member of the Kruppel-like factor subfamily of zinc finger proteins. The encoded protein is a transcriptional activator that binds directly to a specific recognition motif in the promoters of target genes. This protein acts downstream of multiple different signaling pathways and is regulated by post-translational modification. It may participate in both promoting and suppressing cell proliferation. Expression of this gene may be changed in a variety of different cancers and …

**Accessions** — [HGNC:6349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6349) · Entrez [688](https://www.ncbi.nlm.nih.gov/gene/688) · UniProt [Q13887](https://www.uniprot.org/uniprotkb/Q13887) · Ensembl [ENSG00000102554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102554)

## Data

Gene col 2256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2256); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2256]; `tensor/DDL_lfc|DDL_z.npy` [2256]; `embed/gene_vectors.npy` [2256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2256 or target_col == 2256). Every well: [[KLF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

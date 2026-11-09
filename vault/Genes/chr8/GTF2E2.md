---
symbol: "GTF2E2"
type: "gene"
col: 12371
ensembl_id: "ENSG00000197265"
name: "general transcription factor IIE subunit 2"
location: "8p12"
module: 199
arm: "+"
pooled_cpm: 71.37
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# GTF2E2

*general transcription factor IIE subunit 2* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.56× (z +14.6, q 1e-45, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.748× (z -13.4, q 2e-38, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRFN3]] (+0.72, fdr 1e-05), [[PACC1]] (+0.69, fdr 1e-05), [[CTNNBL1]] (+0.67, fdr 1e-05); moves opposite to [[THAP2]] (-0.71, fdr 3e-05), [[SGO1-AS1]] (-0.70, fdr 1e-05), [[OXA1L-DT]] (-0.70, fdr 1e-04).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NEIL2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +14.6 | 1e-45 | 46/48 (AsPC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +14.4 | 8e-45 | 42/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +12.2 | 4e-32 | 40/48 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +9.1 | 2e-17 | 31/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +8.7 | 4e-16 | 31/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +8.4 | 4e-15 | 32/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +8.0 | 1e-13 | 26/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +7.0 | 2e-10 | 25/48 (LOX-IMVI, KATO III, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +5.7 | 9e-07 | 19/49 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.34×** | +5.0 | 3e-05 | 21/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.31×** | +4.7 | 2e-04 | 18/49 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **1.27×** | +4.1 | 0.002 | 17/45 (NCI-H1792, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.003 | 5/48 (NCI-H2030, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +3.9 | 0.003 | 19/48 (HOP62, KATO III, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.019 | 8/47 (CFPAC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Menadione (drug)]] 0.5 µM |  | 1.10× | +3.2 | 0.055 | 5/47 (SNU-423, A549, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.059 | 7/49 (MIA PaCa-2, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | 1.10× | +3.1 | 0.059 | 3/48 (HEC-1-A, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.748×** | -13.4 | 2e-38 | 30/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.724×** | -10.6 | 8e-24 | 30/48 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -10.4 | 5e-23 | 24/49 (A549, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.764×** | -8.5 | 3e-15 | 23/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -7.7 | 2e-12 | 25/48 (HS-578T, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.781×** | -7.5 | 5e-12 | 24/45 (RKO, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.827×** | -6.2 | 4e-08 | 23/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.854× | -5.2 | 1e-05 | 21/48 (AsPC-1, C-33 A, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.886× | -4.0 | 0.005 | 14/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.888× | -3.9 | 0.006 | 8/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.861× | -3.5 | 0.025 | 7/48 (CFPAC-1, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.863× | -3.5 | 0.025 | 12/47 (HCT15, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.905× | -3.3 | 0.047 | 6/48 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.906× | -3.2 | 0.047 | 8/48 (LoVo, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.903× | -3.2 | 0.047 | 18/43 (A-172, NCI-H1573, …) | all doses, flat | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.909× | -3.1 | 0.062 | 13/46 (NCI-H661, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 66.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -17.3) |
| [[RKO (line)]] | wt | 90.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.499× (z -12.7) |
| [[HS-578T (line)]] | alt | 106 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.462× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 123 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.467× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.640× (z -10.4) |
| [[A-427 (line)]] | wt | 98.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -15.2) |
| [[A498 (line)]] | wt | 81.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -14.3) |
| [[A549 (line)]] | wt | 84.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -16.2) |
| [[BT-474 (line)]] | alt | 64.4 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.362× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 66.1 | 1 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.79× (z +8.5) | [[Harringtonine (drug)]] 0.5 µM 0.453× (z -11.4) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.477× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 62.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.88× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -14.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 69.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -13.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 72.2 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 1.93× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 81.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -11.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -12.1) |
| [[SW480 (line)]] | alt | 75.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 73.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.7) |
| [[HOP62 (line)]] | alt | 42.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -10.1) |
| [[LoVo (line)]] | wt | 72.8 | 1 | 0 | [[Belinostat (drug)]] 5 µM 1.95× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 80.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 68.8 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.131× (z -13.8) |
| [[SNU-1 (line)]] | wt | 64.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.367× (z -8.7) |
| [[AN3 CA (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRFN3]] | +0.72 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PACC1]] | +0.69 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CTNNBL1]] | +0.67 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GFOD2]] | +0.67 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[TAF5L]] | +0.66 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[HERC2P9]] | +0.65 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ATG5]] | +0.65 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[SLC23A2]] | +0.64 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.64 | +0.65 / +0.24 | both halves | 5e-04 |  |
| [[GNA12]] | +0.63 | +0.64 / +0.39 | both halves | 6e-05 |  |
| [[NAPG]] | +0.62 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[WASF3]] | +0.62 | +0.59 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | -0.71 | -0.68 / -0.46 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.70 | -0.75 / -0.52 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | -0.70 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[FAM200B]] | -0.69 | -0.72 / -0.46 | both halves | 3e-05 |  |
| [[AK9]] | -0.68 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[MAILR]] | -0.68 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[TMEM202-AS1]] | -0.68 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[PCNX4-DT]] | -0.68 | -0.67 / -0.28 | both halves | 3e-04 |  |
| [[TSGA10]] | -0.67 | -0.71 / -0.31 | both halves | 2e-04 |  |
| [[N4BP2L1]] | -0.67 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[SRGAP3]] | -0.66 | -0.71 / -0.38 | both halves | 7e-05 |  |
| [[ZBTB1]] | -0.65 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEIL2]] | C | NEIL2 activity raises GTF2E2's level | lines that do not express NEIL2 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without NEIL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.2, 11.9); signed map (-40.8, -8.8). **Vector** length 104, 24.0% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.6 | +14.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +12.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +14.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +5.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.8 | -13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.2 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.5 | -10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -4.7 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -6.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIE subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:30,578,318-30,658,236 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIE-B, FE, TF2E2 |
| Gene groups (HGNC) | General transcription factor IIE complex subunits |
| Reactome | 13 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [P29084](https://www.uniprot.org/uniprotkb/P29084) (Transcription initiation factor IIE subunit beta):

> Recruits TFIIH to the initiation complex and stimulates the RNA polymerase II C-terminal domain kinase and DNA-dependent ATPase activities of TFIIH. Both TFIIH and TFIIE are required for promoter clearance by RNA polymerase.

**Summary**, from NCBI Gene [2961](https://www.ncbi.nlm.nih.gov/gene/2961):

> The general transcription factor IIE (TFIIE) is part of the RNA polymerase II transcription initiation complex, recruiting TFIIH and being essential for promoter clearance by RNA polymerase II. TFIIE is a heterodimer (and sometimes heterotetramer) of alpha and beta subunits. The protein encoded by this gene represents the beta subunit of TFIIE. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:4651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4651) · Entrez [2961](https://www.ncbi.nlm.nih.gov/gene/2961) · UniProt [P29084](https://www.uniprot.org/uniprotkb/P29084) · Ensembl [ENSG00000197265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197265)

## Data

Gene col 12371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12371); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12371]; `tensor/DDL_lfc|DDL_z.npy` [12371]; `embed/gene_vectors.npy` [12371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12371 or target_col == 12371). Every well: [[GTF2E2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2E2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "PLEKHA3"
type: "gene"
col: 3757
ensembl_id: "ENSG00000116095"
name: "pleckstrin homology domain containing A3"
location: "2q31.2"
module: 130
arm: "+"
pooled_cpm: 40.96
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# PLEKHA3

*pleckstrin homology domain containing A3* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +18.5, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.593× (z -14.5, q 3e-45, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.667× (z -5.9, q 4e-07, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAT2B]] (+0.69, fdr 7e-06), [[BROX]] (+0.64, fdr 9e-06), [[MTMR6]] (+0.59, fdr 1e-05); moves opposite to [[APRT]] (-0.53, fdr 1e-04), [[PI4KAP2]] (-0.53, fdr 2e-04), [[FASTKD1]] (-0.53, fdr 3e-05).
> It is in [[Module 130]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +18.5 | 0e+00 | 38/48 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +12.7 | 2e-34 | 42/49 (SW480, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +12.0 | 5e-31 | 32/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +9.9 | 5e-21 | 29/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +9.4 | 6e-19 | 24/41 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +8.2 | 1e-14 | 30/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +7.8 | 7e-13 | 27/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +7.4 | 7e-12 | 21/48 (SNU-423, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.23×** | +5.8 | 5e-07 | 20/47 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 1e-06 | 22/47 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +5.2 | 1e-05 | 22/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.21×** | +5.0 | 3e-05 | 21/44 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.5 | 3e-04 | 20/43 (NCI-H1792, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.2 | 1e-03 | 12/48 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +4.0 | 0.002 | 13/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +3.7 | 0.008 | 17/48 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.08× | +3.1 | 0.051 | 2/48 (hTERT-HPNE, SNU-1) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.051 | 2/48 (KATO III, C-33 A) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.062 | 8/48 (SW1417, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.082 | 8/48 (SW480, A-172, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 1.11× | +2.9 | 0.086 | 3/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.092 | 4/45 (HOP62, HCT15, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3757.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.593×** | -14.5 | 3e-45 | 31/48 (SW480, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.631×** | -12.8 | 5e-35 | 34/48 (SW480, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.740×** | -8.4 | 1e-14 | 27/48 (SW480, A549, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.758×** | -7.7 | 2e-12 | 28/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.800×** | -6.0 | 3e-07 | 22/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.667×** | -5.9 | 4e-07 | 24/48 (NCI-H2030, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.811×** | -5.8 | 5e-07 | 20/48 (PANC-1, SHP-77, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.820×** | -5.5 | 3e-06 | 19/48 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.694×** | -5.3 | 7e-06 | 19/48 (HT-29, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.765×** | -5.3 | 7e-06 | 21/48 (A498, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.887× | -4.7 | 1e-04 | 19/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | 0.847× | -4.6 | 2e-04 | 19/47 (BT-474, RPMI-7951, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.736×** | -4.5 | 4e-04 | 19/48 (Hs 766T, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.815×** | -4.1 | 0.002 | 13/48 (PANC-1, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.821×** | -3.9 | 0.004 | 11/48 (SHP-77, SW 1271, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bergenin (drug)]] 0.5 µM |  | 0.870× | -3.8 | 0.004 | 7/48 (J82, SW1417, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.777×** | -3.7 | 0.008 | 8/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.878× | -3.6 | 0.010 | 11/48 (A549, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.875× | -3.5 | 0.014 | 10/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.918× | -3.3 | 0.022 | 4/48 (SW 900, NCI-H2347, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.796×** | -3.3 | 0.023 | 8/46 (HepG2/C3A, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.921× | -3.2 | 0.032 | 8/48 (Hs 766T, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.2 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.237× (z -20.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.530× (z -8.9) |
| [[HOP62 (line)]] | alt | 35.4 | 2 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.2) | [[Belinostat (drug)]] 5 µM 0.387× (z -10.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 39.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -14.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 56.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 45.0 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.302× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 45.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.186× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 32.5 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 65.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -12.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 25.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 32.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 37.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.2) | — |
| [[A498 (line)]] | wt | 63.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.8) | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.101× (z -8.7) |
| [[H4 (line)]] | wt | 41.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.277× (z -8.9) |
| [[HS-578T (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.100× (z -12.4) ⚠ toxic |
| [[J82 (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.391× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 42.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 60.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.445× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 37.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SHP-77 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.246× (z -9.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAT2B]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[BROX]] | +0.64 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[MTMR6]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 | pathway: PI Metabolism |
| [[CREBL2]] | +0.58 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[AASDHPPT]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PEX1]] | +0.58 | +0.60 / +0.40 | both halves | 4e-05 |  |
| [[HINT3]] | +0.57 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[RBM7]] | +0.56 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[FBXO8]] | +0.56 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[COPS5]] | +0.56 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[COPS2]] | +0.56 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[CILK1]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APRT]] | -0.53 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[PI4KAP2]] | -0.53 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[FASTKD1]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[KYAT1]] | -0.51 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[CD320]] | -0.49 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[PI4KAP1]] | -0.49 | -0.55 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CCK]] | -0.49 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[PPP1R14B]] | -0.49 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[SLC25A5]] | -0.48 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[NOG]] | -0.48 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[DEPDC5]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SH3D21]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[B3GAT3]] | -0.47 | -0.54 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-20.1, 6.9); signed map (8.4, -27.6). **Vector** length 99.3, 22.2% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +18.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.3 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +12.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.1 | +8.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | -0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | -7.2 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.5 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.0 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.6 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:178,480,457-178,516,463 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAPP1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB20](https://www.uniprot.org/uniprotkb/Q9HB20) (Pleckstrin homology domain-containing family A member 3):

> Plays a role in regulation of vesicular cargo transport from the trans-Golgi network (TGN) to the plasma membrane. Regulates Golgi phosphatidylinositol 4-phosphate (PtdIns(4)P) levels and activates the PtdIns(4)P phosphatase activity of SACM1L when it binds PtdIns(4)P in 'trans' configuration. Binds preferentially to PtdIns(4)P. Negatively regulates APOB secretion from hepatocytes.

**Summary**, from NCBI Gene [65977](https://www.ncbi.nlm.nih.gov/gene/65977):

> Enables identical protein binding activity; molecular carrier activity; and phosphatidylinositol-4-phosphate binding activity. Predicted to be involved in endosome organization; receptor recycling; and retrograde transport, endosome to Golgi. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14338) · Entrez [65977](https://www.ncbi.nlm.nih.gov/gene/65977) · UniProt [Q9HB20](https://www.uniprot.org/uniprotkb/Q9HB20) · Ensembl [ENSG00000116095](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116095)

## Data

Gene col 3757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3757); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3757]; `tensor/DDL_lfc|DDL_z.npy` [3757]; `embed/gene_vectors.npy` [3757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3757 or target_col == 3757). Every well: [[PLEKHA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "KIF1C"
type: "gene"
col: 4960
ensembl_id: "ENSG00000129250"
name: "kinesin family member 1C"
location: "17p13.2"
module: 2
arm: "+"
pooled_cpm: 57.21
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 9
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# KIF1C

*kinesin family member 1C* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.31× (z +22.9, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.73× (z +10.5, q 2e-23, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.714× (z -9.1, q 3e-17, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42BPB]] (+0.63, fdr 7e-06), [[AKT1]] (+0.62, fdr 1e-05), [[CEP170B]] (+0.61, fdr 1e-05); moves opposite to [[SUGT1P3-1]] (-0.54, fdr 2e-05), [[TCEAL8]] (-0.52, fdr 3e-05), [[AASDH]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.31×** | +22.9 | 0e+00 | 47/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +22.0 | 0e+00 | 42/42 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +13.3 | 3e-38 | 39/45 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +10.5 | 2e-23 | 44/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +6.8 | 1e-09 | 32/47 (C32, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +6.4 | 2e-08 | 32/47 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +6.3 | 3e-08 | 34/47 (NCI-H460, C32, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +5.9 | 3e-07 | 26/49 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.8 | 5e-07 | 28/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 2e-06 | 30/48 (A-172, HT-29, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +5.4 | 3e-06 | 28/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 4e-06 | 27/48 (SNU-1, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.32×** | +5.2 | 1e-05 | 24/48 (NCI-H2030, A498, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +5.1 | 1e-05 | 29/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 5e-04 | 23/48 (NCI-H460, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +4.3 | 6e-04 | 22/47 (NCI-H460, C32, …) | all doses, flat | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +4.2 | 9e-04 | 20/48 (HS-578T, A498, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.002 | 17/48 (HEC-1-A, C32, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.003 | 20/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.003 | 19/48 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.003 | 21/48 (NCI-H460, HT-29, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.006 | 14/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.009 | 15/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.714×** | -9.1 | 3e-17 | 37/48 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.721×** | -8.9 | 2e-16 | 30/48 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -7.4 | 3e-11 | 27/48 (LOX-IMVI, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.686×** | -7.2 | 8e-11 | 34/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.783×** | -4.7 | 3e-04 | 27/48 (SW48, HS-578T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.853× | -4.3 | 0.002 | 21/48 (SNU-1, SW480, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.815×** | -3.8 | 0.013 | 21/48 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.015 | 22/48 (AN3 CA, A-427, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.716×** | -3.4 | 0.050 | 9/49 (HOP62, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.721×** | -3.3 | 0.058 | 16/48 (A-427, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.0 | 0.12 | 2/49 (COLO 205, SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 124 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.462× (z -9.1) |
| [[A-427 (line)]] | wt | 85.6 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -16.7) |
| [[LS 180 (line)]] | wt | 74.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 71.8 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.63× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.3) ⚠ cell-cycle shift, explains ~94% of this change |
| [[SW480 (line)]] | alt | 62.2 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.09× (z +10.3) | [[Selinexor (drug)]] 5 µM 0.635× (z -9.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HT-29 (line)]] | alt | 58.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +15.4) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 5 µM 0.550× (z -8.8) |
| [[LoVo (line)]] | wt | 49.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +17.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 55.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +14.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 53.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.38× (z +12.6) ⚠ toxic; transcription drop | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0929× (z -11.0) ⚠ toxic |
| [[KATO III (line)]] | alt | 60.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +18.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 98.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 72.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +14.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.287× (z -11.9) |
| [[PANC-1 (line)]] | alt | 39.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +18.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 81.4 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.378× (z -11.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.397× (z -10.9) |
| [[SNU-423 (line)]] | alt | 31.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +12.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 105 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -12.9) |
| [[A498 (line)]] | wt | 86.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +14.3) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 38.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +12.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 74.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 77.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +11.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 37.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.45× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 63.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 80.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 38.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.46× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 48.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 31.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 42.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 39.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +10.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 79.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 89.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.6) |
| [[SHP-77 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42BPB]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[AKT1]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CEP170B]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CAPN1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[STK25]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PACS2]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.60 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[PCBP4]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[STX2]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SBF1]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TCF3]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD52]] | +0.56 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P3-1]] | -0.54 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[TCEAL8]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[AASDH]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[LPAR6]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[KBTBD7]] | -0.50 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.50 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TRA2A]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[HHLA3]] | -0.48 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[SAP18]] | -0.48 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[MYNN]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[MED19]] | -0.48 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CNOT2]] | -0.48 | -0.29 / -0.32 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.0, -22.7); signed map (-46.5, -9.5). **Vector** length 112, 32.7% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.1 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +10.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.1 | +5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.5 | +5.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.1 | +6.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.0 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.4 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -8.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.2 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,997,950-5,028,401 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPAX2, SPG58; previously SAX2 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43896](https://www.uniprot.org/uniprotkb/O43896) (Kinesin-like protein KIF1C):

> Motor required for the retrograde transport of Golgi vesicles to the endoplasmic reticulum. Has a microtubule plus end-directed motility.

**Summary**, from NCBI Gene [10749](https://www.ncbi.nlm.nih.gov/gene/10749):

> The protein encoded by this gene is a member of the kinesin-like protein family. The family members are microtubule-dependent molecular motors that transport organelles within cells and move chromosomes during cell division. Mutations in this gene are a cause of spastic ataxia 2, autosomal recessive. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:6317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6317) · Entrez [10749](https://www.ncbi.nlm.nih.gov/gene/10749) · UniProt [O43896](https://www.uniprot.org/uniprotkb/O43896) · Ensembl [ENSG00000129250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129250)

## Data

Gene col 4960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4960); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4960]; `tensor/DDL_lfc|DDL_z.npy` [4960]; `embed/gene_vectors.npy` [4960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4960 or target_col == 4960). Every well: [[KIF1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

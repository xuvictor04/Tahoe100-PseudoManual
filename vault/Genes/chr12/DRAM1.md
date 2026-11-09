---
symbol: "DRAM1"
type: "gene"
col: 5805
ensembl_id: "ENSG00000136048"
name: "DNA damage regulated autophagy modulator 1"
location: "12q23.2"
module: 14
arm: "+"
pooled_cpm: 48.29
n_lines_expressing: 44
n_dd_up: 44
n_dd_down: 22
n_dd_up_clean: 36
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 6
direction_downstream: 15
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# DRAM1

*DNA damage regulated autophagy modulator 1* — 12q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.77× (z +31.4, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.344× (z -17.9, q 0e+00, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OGFRL1]] (+0.73, fdr 7e-06), [[RASGRP1]] (+0.69, fdr 7e-06), [[MR1]] (+0.69, fdr 1e-05); moves opposite to [[RNGTT]] (-0.61, fdr 2e-05), [[HPCAL1]] (-0.59, fdr 6e-05), [[ETV5]] (-0.57, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FAS]] → it (grade B ⚠); 15 go from it, the strongest it → [[BTG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.77×** | +31.4 | 0e+00 | 39/41 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.68×** | +16.5 | 0e+00 | 35/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.59×** | +15.3 | 0e+00 | 35/42 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.01×** | +14.1 | 4e-43 | 37/43 (NCI-H460, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.22×** | +13.4 | 7e-39 | 39/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +10.9 | 1e-25 | 31/41 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +8.6 | 7e-16 | 35/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +8.3 | 1e-14 | 26/42 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.0 | 6e-14 | 27/42 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +6.7 | 1e-09 | 24/41 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +6.6 | 2e-09 | 31/42 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +6.5 | 4e-09 | 24/42 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.45×** | +6.3 | 2e-08 | 29/42 (LOX-IMVI, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.44×** | +6.2 | 2e-08 | 28/42 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.29×** | +6.0 | 6e-08 | 25/42 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.0 | 6e-08 | 24/42 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.28×** | +5.9 | 1e-07 | 22/42 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.9 | 1e-07 | 21/42 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 5e-07 | 24/42 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.344×** | -17.9 | 0e+00 | 40/42 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.407×** | -15.1 | 0e+00 | 41/42 (SNU-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.452×** | -13.3 | 4e-38 | 36/42 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.679×** | -6.2 | 6e-08 | 19/36 (NCI-H1792, Panc 03.27, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -5.8 | 6e-07 | 25/42 (LoVo, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.749×** | -4.8 | 1e-04 | 22/42 (A-427, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.749×** | -4.8 | 1e-04 | 19/42 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.750×** | -4.8 | 1e-04 | 22/42 (A498, LoVo, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.785×** | -4.1 | 0.003 | 15/42 (J82, SNU-423, …) | top dose only |  |
| [[Naproxen (drug)]] 5 µM |  | **0.784×** | -3.9 | 0.005 | 14/42 (LOX-IMVI, HCT15, …) | all doses, flat |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.792×** | -3.9 | 0.005 | 15/41 (HCT15, NCI-H1573, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 5 µM |  | **0.794×** | -3.9 | 0.005 | 15/42 (LoVo, A498, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.795×** | -3.9 | 0.005 | 22/41 (SNU-1, HepG2/C3A, …) | rises with dose | composition shift |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.852× | -3.8 | 0.006 | 13/42 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Berbamine (dihydrochloride) (drug)]] 0.5 µM |  | **0.810×** | -3.5 | 0.015 | 5/42 (PANC-1, HCT15, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.671×** | -3.5 | 0.017 | 14/42 (J82, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -3.4 | 0.019 | 14/42 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.818×** | -3.4 | 0.024 | 15/42 (NCI-H1792, LoVo, …) | all doses, flat |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **0.820×** | -3.3 | 0.025 | 13/42 (H4, Panc 03.27, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 81.3 | 13 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +24.3) | [[Panobinostat (drug)]] 5 µM 0.321× (z -10.8) |
| [[LoVo (line)]] | wt | 52.0 | 7 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.187× (z -15.4) |
| [[A-172 (line)]] | wt | 107 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -11.0) |
| [[PANC-1 (line)]] | alt | 30.7 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +24.2) | [[Panobinostat (drug)]] 5 µM 0.452× (z -8.5) |
| [[A549 (line)]] | wt | 84.3 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.256× (z -12.4) |
| [[HOP62 (line)]] | alt | 29.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +23.4) | — |
| [[J82 (line)]] | alt | 191 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +28.4) | [[Panobinostat (drug)]] 5 µM 0.293× (z -13.4) |
| [[HS-578T (line)]] | alt | 36.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +18.8) | — |
| [[LOX-IMVI (line)]] | wt | 69.9 | 1 (1 ⚠) | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.53× (z +13.4) ⚠ cell-cycle shift, explains ~36% of this change | [[Panobinostat (drug)]] 5 µM 0.333× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 38.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +18.5) | — |
| [[SNU-423 (line)]] | alt | 57.9 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +24.2) | [[Panobinostat (drug)]] 5 µM 0.228× (z -11.7) |
| [[A498 (line)]] | wt | 117 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.339× (z -8.7) |
| [[BT-474 (line)]] | alt | 18.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +16.4) | — |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +22.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +24.3) | — |
| [[RKO (line)]] | wt | 53.2 | 2 (1 ⚠) | 2 | [[Selinexor (drug)]] 5 µM 2.63× (z +9.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.253× (z -10.0) |
| [[SNU-1 (line)]] | wt | 129 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -17.4) |
| [[A-427 (line)]] | wt | 40.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 21.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +18.1) | — |
| [[HepG2_C3A (line)]] | wt | 79.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.312× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 54.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.2) | — |
| [[NCI-H1792 (line)]] | alt | 72.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.336× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -10.4) |
| [[SW 900 (line)]] | alt | 27.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +16.4) | — |
| [[C32 (line)]] | wt | 37.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 85.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 39.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[RPMI-7951 (line)]] | alt | 21.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +12.2) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.174× (z -8.5) |
| [[SW48 (line)]] | wt | 48.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 35.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +17.4) | — |
| [[H4 (line)]] | wt | 44.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.9) ⚠ cell-cycle shift, explains ~95% of this change |
| [[SW1417 (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +11.8) | — |
| [[SW480 (line)]] | alt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.88 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.67 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OGFRL1]] | +0.73 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[RASGRP1]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MR1]] | +0.69 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[FAS]] | +0.69 | +0.62 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[SPATA18]] | +0.69 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[RAB32]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ACTA2]] | +0.67 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.66 | +0.64 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TBC1D22B]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PATL2]] | +0.66 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CXCL3]] | +0.66 | +0.63 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HPCAL1]] | -0.59 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[ETV5]] | -0.57 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[NAPG]] | -0.56 | -0.62 / -0.28 | both halves | 3e-04 |  |
| [[CAP1]] | -0.56 | -0.60 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAS]] | B | FAS activity raises DRAM1's level | lines that do not express FAS (8) vs lines expressing it (42) | 2.70× lower at baseline in the lines without FAS | 0.005 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[ACTA2]] | B | ACTA2 activity raises DRAM1's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 2.24× lower at baseline in the lines without ACTA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[ANKRD33B]] | B | ANKRD33B activity raises DRAM1's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.95× lower at baseline in the lines without ANKRD33B | 0.013 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[NKX3-1]] | B | NKX3-1 activity raises DRAM1's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.48× lower at baseline in the lines without NKX3-1 | 0.020 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[GLS2]] | B | GLS2 activity lowers DRAM1's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.86× higher at baseline in the lines without GLS2 | 0.064 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[PINCR]] | B | PINCR activity raises DRAM1's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without PINCR | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTG2]] | B | DRAM1 activity lowers BTG2's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.27× higher at baseline in the lines without DRAM1 | 0.008 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[ANKRD33B]] | B | DRAM1 activity raises ANKRD33B's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 5.36× lower at baseline in the lines without DRAM1 | 0.012 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[FAS]] | B | DRAM1 activity raises FAS's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 3.53× lower at baseline in the lines without DRAM1 | 0.018 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[FAM200B]] | B | DRAM1 activity raises FAM200B's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 1.39× lower at baseline in the lines without DRAM1 | 0.025 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[APLF]] | B | DRAM1 activity raises APLF's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without DRAM1 | 0.028 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[BTG3]] | B | DRAM1 activity raises BTG3's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without DRAM1 | 0.028 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[BTG2]] | B | DRAM1 activity strengthens BTG2's drug response | lines that do not express DRAM1 (6) vs lines expressing it (35) | the lines without DRAM1 respond 0.00× as strongly (z diff +3.10); strongest at Topotecan (hydrochloride) 5 µM: 0.32x vs 2.06x (z diff +8.1) | 0.033 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ACTA2]] | B | DRAM1 activity raises ACTA2's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.94× lower at baseline in the lines without DRAM1 | 0.034 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[ADORA2A]] | B | DRAM1 activity raises ADORA2A's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without DRAM1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[DCP1B]] | B | DRAM1 activity raises DCP1B's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without DRAM1 | 0.043 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[TMEM63B]] | B | DRAM1 activity raises TMEM63B's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without DRAM1 | 0.049 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[OGFRL1]] | B | DRAM1 activity raises OGFRL1's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 4.52× lower at baseline in the lines without DRAM1 | 0.049 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.1, 4.6); signed map (41.8, 8.6). **Vector** length 134, 42.8% of its response variance represented; |z| ≥ 3 in 1,419 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chemokine receptors bind chemokines* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +31.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.8 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +7.7 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +16.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.4 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.2 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.9 | +4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.8 | +4.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.6 | -17.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.6 | -15.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.3 | -13.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -5.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | DNA damage regulated autophagy modulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.2 — chr12:101,877,580-102,012,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11259, DRAM |
| Gene groups (HGNC) | DRAM autophagy modulator family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N682](https://www.uniprot.org/uniprotkb/Q8N682) (DNA damage-regulated autophagy modulator protein 1):

> Lysosomal modulator of autophagy that plays a central role in p53/TP53-mediated apoptosis. Not involved in p73/TP73-mediated autophagy.

**Summary**, from NCBI Gene [55332](https://www.ncbi.nlm.nih.gov/gene/55332):

> This gene is regulated as part of the p53 tumor suppressor pathway. The gene encodes a lysosomal membrane protein that is required for the induction of autophagy by the pathway. Decreased transcriptional expression of this gene is associated with various tumors. This gene has a pseudogene on chromosome 4. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25645) · Entrez [55332](https://www.ncbi.nlm.nih.gov/gene/55332) · UniProt [Q8N682](https://www.uniprot.org/uniprotkb/Q8N682) · Ensembl [ENSG00000136048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136048)

## Data

Gene col 5805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5805); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5805]; `tensor/DDL_lfc|DDL_z.npy` [5805]; `embed/gene_vectors.npy` [5805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5805 or target_col == 5805). Every well: [[DRAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DRAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

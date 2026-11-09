---
symbol: "ATP11C"
type: "gene"
col: 2197
ensembl_id: "ENSG00000101974"
name: "ATPase phospholipid transporting 11C (ATP11C blood group)"
location: "Xq27.1"
module: 17
arm: "-"
pooled_cpm: 88.77
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ATP11C

*ATPase phospholipid transporting 11C (ATP11C blood group)* — Xq27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +12.9, q 5e-35, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.425× (z -17.1, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JADE3]] (+0.69, fdr 7e-06), [[WNK1]] (+0.64, fdr 1e-05), [[PRDM2]] (+0.61, fdr 4e-05); moves opposite to [[ZNF45]] (-0.71, fdr 1e-05), [[GPATCH11]] (-0.67, fdr 1e-05), [[DDX19B]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +12.9 | 5e-35 | 36/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +8.2 | 9e-14 | 37/47 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.8 | 2e-09 | 35/49 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +3.7 | 0.035 | 19/46 (A-172, NCI-H1573, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.048 | 19/47 (Hs 766T, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.048 | 16/49 (NCI-H1573, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.098 | 17/47 (HOP62, SW1417, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.13 | 7/47 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.21× | +3.0 | 0.15 | 14/49 (NCI-H1573, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.425×** | -17.1 | 0e+00 | 45/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.429×** | -17.0 | 0e+00 | 46/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.489×** | -14.3 | 3e-44 | 46/47 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.684×** | -10.7 | 9e-25 | 33/47 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -10.2 | 2e-22 | 42/48 (A498, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -8.4 | 4e-15 | 35/46 (SW1417, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -8.4 | 4e-15 | 34/47 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -8.1 | 6e-14 | 35/47 (LoVo, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **0.743×** | -5.9 | 2e-07 | 31/47 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.757×** | -5.3 | 5e-06 | 23/47 (RKO, NCI-H2030, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.637×** | -4.7 | 1e-04 | 24/47 (LOX-IMVI, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.790×** | -4.7 | 1e-04 | 25/47 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.790×** | -4.7 | 1e-04 | 27/47 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -4.6 | 1e-04 | 19/47 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.802×** | -4.4 | 4e-04 | 23/48 (RKO, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.817×** | -4.1 | 0.002 | 22/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.681×** | -4.0 | 0.002 | 26/47 (NCI-H1573, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.829×** | -3.7 | 0.005 | 20/47 (SW480, SK-MEL-2, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.876× | -3.7 | 0.005 | 10/47 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.011 | 21/47 (H4, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.790×** | -3.3 | 0.021 | 18/47 (HCT15, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 54.1 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -14.4) |
| [[RKO (line)]] | wt | 93.8 | 3 | 5 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -15.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 61.1 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -19.9) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 82.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -20.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.372× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 114 | 3 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +16.7) | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -14.8) |
| [[SW480 (line)]] | alt | 105 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -16.8) |
| [[A549 (line)]] | wt | 97.7 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -11.7) |
| [[LoVo (line)]] | wt | 87.8 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.365× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 154 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -19.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.274× (z -16.7) |
| [[A498 (line)]] | wt | 110 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.513× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 72.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -11.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.371× (z -11.0) |
| [[PANC-1 (line)]] | alt | 179 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -13.9) |
| [[SNU-423 (line)]] | alt | 137 | 1 | 4 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.307× (z -13.2) |
| [[A-427 (line)]] | wt | 94.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -25.1) |
| [[MIA PaCa-2 (line)]] | alt | 49.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 78.4 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 138 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -14.7) |
| [[C32 (line)]] | wt | 65.7 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 55.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.415× (z -10.4) |
| [[Hs 766T (line)]] | wt | 113 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.400× (z -9.0) |
| [[HS-578T (line)]] | alt | 80.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -11.6) |
| [[J82 (line)]] | alt | 129 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -12.9) |
| [[KATO III (line)]] | alt | 88.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -10.3) |
| [[LS 180 (line)]] | wt | 64.9 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -8.5) |
| [[SW 1088 (line)]] | alt | 74.4 | 0 | 3 | — | [[Talc (drug)]] 5 µM 0.0659× (z -9.4) |
| [[A-172 (line)]] | wt | 50.5 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -8.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[BT-474 (line)]] | alt | 45.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -10.0) |
| [[H4 (line)]] | wt | 115 | 1 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.320× (z -9.9) |
| [[HOP62 (line)]] | alt | 99.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 67.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 80.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.364× (z -9.8) |
| [[SW 1271 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0960× (z -12.1) ⚠ transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.191× (z -8.6) |
| [[SW1417 (line)]] | alt | 84.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -11.4) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 70.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 41.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 26.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 70.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HepG2_C3A (line)]] | wt | 57.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 83.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.5) | — |
| [[SW48 (line)]] | wt | 89.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JADE3]] | +0.69 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[WNK1]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 | pathway: Ion channel transport |
| [[PRDM2]] | +0.61 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[DGKH]] | +0.61 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[RCC2]] | +0.59 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[MOB1A]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[HCFC1]] | +0.58 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ARSB]] | +0.58 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[ADSS2]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[NCOA2]] | +0.57 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[PRRC2B]] | +0.56 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[EPM2A]] | +0.56 | +0.45 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF45]] | -0.71 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[GPATCH11]] | -0.67 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[DDX19B]] | -0.66 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ZNF461]] | -0.65 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[PIGH]] | -0.65 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[POLM]] | -0.65 | -0.52 / -0.52 | both halves | 1e-05 | same gene group |
| [[INIP]] | -0.64 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[MSL3P1]] | -0.62 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[ZNF112]] | -0.61 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[ZNF559]] | -0.61 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MRPS31P4]] | -0.61 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[THOC1]] | -0.60 | -0.55 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP11C's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MCF2]] | C | MCF2 activity raises ATP11C's level | lines that do not express MCF2 (3) vs lines expressing it (47) | 2.59× lower at baseline in the lines without MCF2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SATB2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.9, -2.4); signed map (15.4, -7.5). **Vector** length 121, 35.9% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.1 | +12.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +8.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.0 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.7 | -17.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.0 | -10.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.7 | -17.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 11C (ATP11C blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq27.1 — chrX:139,726,346-139,945,276 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPIG, ATPIQ |
| Gene groups (HGNC) | Blood group antigens; ATPase phospholipid transporting; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NB49](https://www.uniprot.org/uniprotkb/Q8NB49) (Phospholipid-transporting ATPase IG):

> Catalytic component of a P4-ATPase flippase complex which catalyzes the hydrolysis of ATP coupled to the transport of aminophospholipids, phosphatidylserines (PS) and phosphatidylethanolamines (PE), from the outer to the inner leaflet of the plasma membrane. Major PS-flippase in immune cell subsets. In erythrocyte plasma membrane, it is required to maintain PS in the inner leaflet preventing its exposure on the surface. This asymmetric distribution is critical for the survival of erythrocytes …

**Summary**, from NCBI Gene [286410](https://www.ncbi.nlm.nih.gov/gene/286410):

> Enables phosphatidylethanolamine flippase activity and phosphatidylserine flippase activity. Involved in phospholipid translocation. Located in endoplasmic reticulum and plasma membrane. Part of phospholipid-translocating ATPase complex. Implicated in X-linked congenital hemolytic anemia. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13554) · Entrez [286410](https://www.ncbi.nlm.nih.gov/gene/286410) · UniProt [Q8NB49](https://www.uniprot.org/uniprotkb/Q8NB49) · Ensembl [ENSG00000101974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101974)

## Data

Gene col 2197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2197); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2197]; `tensor/DDL_lfc|DDL_z.npy` [2197]; `embed/gene_vectors.npy` [2197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2197 or target_col == 2197). Every well: [[ATP11C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP11C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

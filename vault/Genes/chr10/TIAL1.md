---
symbol: "TIAL1"
type: "gene"
col: 7581
ensembl_id: "ENSG00000151923"
name: "TIA1 cytotoxic granule associated RNA binding protein like 1"
location: "10q26.11"
module: 201
arm: "+"
pooled_cpm: 123.78
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# TIAL1

*TIA1 cytotoxic granule associated RNA binding protein like 1* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.01× (z +12.7, q 6e-34, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.504× (z -12.4, q 2e-32, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIAO2A]] (+0.66, fdr 1e-05), [[ZUP1]] (+0.65, fdr 1e-05), [[TMEM68]] (+0.65, fdr 1e-05); moves opposite to [[IER2]] (-0.60, fdr 1e-05), [[TNFRSF12A]] (-0.59, fdr 7e-06), [[JUNB]] (-0.57, fdr 3e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7581.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.01×** | +12.7 | 6e-34 | 45/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +10.0 | 5e-21 | 39/49 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +9.9 | 7e-21 | 44/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +8.3 | 1e-14 | 45/49 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +8.1 | 5e-14 | 43/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +7.4 | 1e-11 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +7.2 | 7e-11 | 38/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +7.0 | 2e-10 | 42/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.9 | 4e-10 | 37/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +6.4 | 1e-08 | 36/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.8 | 9e-05 | 34/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.26×** | +4.2 | 0.001 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.9 | 0.004 | 24/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.6 | 0.013 | 18/37 (Panc 03.27, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.013 | 27/48 (A498, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.026 | 28/49 (PANC-1, A498, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.504×** | -12.4 | 2e-32 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.538×** | -11.2 | 1e-26 | 47/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.574×** | -10.0 | 2e-21 | 45/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -6.2 | 7e-08 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.628×** | -4.4 | 0.001 | 35/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.794×** | -4.1 | 0.003 | 26/48 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.808×** | -3.8 | 0.011 | 23/49 (RKO, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.822×** | -3.4 | 0.045 | 22/44 (SNU-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -3.4 | 0.045 | 22/48 (NCI-H1792, A549, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.832×** | -3.3 | 0.054 | 19/48 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.833×** | -3.3 | 0.054 | 24/48 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.058 | 19/48 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.058 | 20/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.058 | 21/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.832×** | -3.2 | 0.058 | 20/47 (A-427, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.063 | 19/47 (SNU-423, A-427, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.886× | -3.1 | 0.068 | 6/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 175 | 7 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +16.7) | [[Panobinostat (drug)]] 0.5 µM 0.499× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 121 | 6 (3 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.455× (z -10.0) |
| [[SW480 (line)]] | alt | 137 | 5 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -14.2) |
| [[LoVo (line)]] | wt | 121 | 6 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +19.0) | [[Panobinostat (drug)]] 0.5 µM 0.524× (z -9.0) |
| [[KATO III (line)]] | alt | 102 | 3 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -12.5) |
| [[RKO (line)]] | wt | 149 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.1) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.59× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -12.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 105 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.362× (z -12.3) |
| [[A-427 (line)]] | wt | 117 | 3 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.9) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 116 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.492× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 98.6 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +12.7) | — |
| [[HCT15 (line)]] | alt | 183 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.427× (z -9.5) |
| [[HOP62 (line)]] | alt | 72.1 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -9.6) |
| [[LS 180 (line)]] | wt | 143 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +15.4) | [[Panobinostat (drug)]] 0.5 µM 0.460× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 106 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +11.7) | — |
| [[A549 (line)]] | wt | 118 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.7) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 123 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 74.9 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.99× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 152 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.475× (z -9.0) |
| [[SW48 (line)]] | wt | 146 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.02× (z +11.1) | — |
| [[A498 (line)]] | wt | 128 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.486× (z -8.8) |
| [[C-33 A (line)]] | alt | 130 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.0) | — |
| [[C32 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -10.9) |
| [[H4 (line)]] | wt | 133 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.392× (z -8.6) |
| [[Hs 766T (line)]] | wt | 121 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.6) | — |
| [[J82 (line)]] | alt | 82.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.491× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 153 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 114 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 127 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +8.7) | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.0713× (z -13.5) |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.198× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 135 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.460× (z -9.4) |
| [[SNU-1 (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0817× (z -21.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 115 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.153× (z -8.9) |
| [[A-172 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 228 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2A]] | +0.66 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ZUP1]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TMEM68]] | +0.65 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RAF1]] | +0.64 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[HOXB-AS3]] | +0.64 | +0.30 / +0.60 | both halves | 2e-04 |  |
| [[PDHX]] | +0.62 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[HOXB6]] | +0.62 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[HOXB7]] | +0.60 | +0.25 / +0.48 | both halves | 4e-04 |  |
| [[MED24]] | +0.60 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[HOXB4]] | +0.60 | +0.24 / +0.65 | both halves | 5e-04 |  |
| [[HOXB5]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[HOXB3]] | +0.60 | +0.37 / +0.57 | both halves | 8e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER2]] | -0.60 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.59 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[JUNB]] | -0.57 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[R3HDM4]] | -0.57 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[ACTG1]] | -0.55 | -0.41 / -0.37 | both halves | 8e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[CMIP]] | -0.55 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[EPPK1]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ADAMTSL5]] | -0.53 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[TAF1B]] | -0.53 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CSRP1]] | -0.53 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[EHD4]] | -0.52 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[RNF123]] | -0.52 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.3, 19.6); signed map (-30.1, -20.0). **Vector** length 101, 34.3% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.9 | +10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +10.6 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.9 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | -0.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -12.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -10.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -0.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | TIA1 cytotoxic granule associated RNA binding protein like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,571,802-119,597,029 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIAR |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: FGFR2 alternative splicing; Signaling by FGFR2; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01085](https://www.uniprot.org/uniprotkb/Q01085) (Nucleolysin TIAR):

> RNA-binding protein involved in alternative pre-RNA splicing and in cytoplasmic stress granules formation. Shows a preference for uridine-rich RNAs. Activates splicing of alternative exons with weak 5' splice sites followed by a U-rich stretch on its own pre-mRNA and on TIA1 mRNA (By similarity). Promotes the inclusion of TIA1 exon 5 to give rise to the long isoform (isoform a) of TIA1. Acts downstream of the stress-induced phosphorylation of EIF2S1/EIF2A to promote the recruitment of …

**Summary**, from NCBI Gene [7073](https://www.ncbi.nlm.nih.gov/gene/7073):

> The protein encoded by this gene is a member of a family of RNA-binding proteins, has three RNA recognition motifs (RRMs), and binds adenine and uridine-rich elements in mRNA and pre-mRNAs of a wide range of genes. It regulates various activities including translational control, splicing and apoptosis. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. The different isoforms have been show to function differently with respect to post-transcriptional …

**Accessions** — [HGNC:11804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11804) · Entrez [7073](https://www.ncbi.nlm.nih.gov/gene/7073) · UniProt [Q01085](https://www.uniprot.org/uniprotkb/Q01085) · Ensembl [ENSG00000151923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151923)

## Data

Gene col 7581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7581); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7581]; `tensor/DDL_lfc|DDL_z.npy` [7581]; `embed/gene_vectors.npy` [7581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7581 or target_col == 7581). Every well: [[TIAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

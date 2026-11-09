---
symbol: "AGL"
type: "gene"
col: 8561
ensembl_id: "ENSG00000162688"
name: "amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase"
location: "1p21.2"
module: 28
arm: "+"
pooled_cpm: 46.0
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# AGL

*amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.13× (z +14.6, q 1e-45, up in 43 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +12.2, q 5e-32, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.651× (z -7.9, q 2e-12, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF518A]] (+0.64, fdr 1e-05), [[ZMYM4]] (+0.64, fdr 1e-05), [[BMI1]] (+0.64, fdr 1e-05); moves opposite to [[GID4]] (-0.61, fdr 1e-05), [[RAD9A]] (-0.60, fdr 1e-05), [[MED31]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +14.6 | 1e-45 | 43/46 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +12.2 | 5e-32 | 38/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +11.8 | 6e-30 | 35/41 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +8.0 | 2e-13 | 30/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +7.9 | 4e-13 | 30/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +7.7 | 9e-13 | 28/44 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.6 | 3e-09 | 33/48 (A-427, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +5.3 | 7e-06 | 22/47 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.1 | 2e-05 | 20/48 (A-172, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.002 | 18/48 (A-427, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.24×** | +4.1 | 0.002 | 21/48 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.003 | 19/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.003 | 17/47 (NCI-H1792, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.7 | 0.010 | 14/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.012 | 16/47 (Hs 766T, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.015 | 10/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.027 | 16/48 (J82, H4, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.029 | 11/48 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.042 | 11/48 (SW48, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8561.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.651×** | -7.9 | 2e-12 | 33/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -7.0 | 7e-10 | 33/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.707×** | -6.7 | 3e-09 | 30/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -6.5 | 1e-08 | 30/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.729×** | -6.1 | 1e-07 | 24/47 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -6.0 | 2e-07 | 29/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.564×** | -5.8 | 5e-07 | 26/48 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.747×** | -5.6 | 1e-06 | 27/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.659×** | -4.2 | 0.002 | 19/43 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.806×** | -4.2 | 0.002 | 16/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.826×** | -3.7 | 0.011 | 22/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.705×** | -3.5 | 0.019 | 15/48 (hTERT-HPNE, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.840× | -3.4 | 0.030 | 15/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.840× | -3.4 | 0.030 | 19/48 (C-33 A, A-172, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.842× | -3.3 | 0.034 | 12/47 (SNU-1, RKO, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.857× | -3.0 | 0.092 | 12/47 (A-172, NCI-H460, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.898× | -3.0 | 0.096 | 14/48 (SW480, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.1 | 1 (1 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.31× (z +10.4) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.385× (z -12.2) |
| [[SW480 (line)]] | alt | 80.6 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.0) | [[Ixazomib citrate (drug)]] 5 µM 0.534× (z -9.0) |
| [[A-427 (line)]] | wt | 51.3 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +9.5) | [[PH-797804 (drug)]] 5 µM 0.110× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +8.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.287× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 80.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 58.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.7) | — |
| [[NCI-H23 (line)]] | alt | 47.4 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.331× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 24.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +15.0) | — |
| [[A498 (line)]] | wt | 31.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 54.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +10.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 51.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.3) | [[Docetaxel (drug)]] 0.05 µM 0.311× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 69.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.9) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~93% of this change |
| [[A-172 (line)]] | wt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 79.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 48.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 70.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 45.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.80× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.284× (z -8.8) |
| [[A549 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518A]] | +0.64 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[ZMYM4]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[BMI1]] | +0.64 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.64 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[RAD50]] | +0.63 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[TIA1]] | +0.62 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[ATP5PB]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ACADM]] | +0.62 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[GUF1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[DZIP3]] | +0.61 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[YTHDC2]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZNF280D]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GID4]] | -0.61 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[RAD9A]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[MED31]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[BET1L]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[WIPI1]] | -0.59 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CTDP1]] | -0.59 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[ZNRD2]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[TANGO2]] | -0.58 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.58 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[ZNF250]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SLC25A29]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TPST2]] | -0.57 | -0.64 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises AGL's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.2, 5.6); signed map (15.0, -34.0). **Vector** length 101, 25.7% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.5 | -6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.0 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -7.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.2 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:99,850,361-99,924,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GDE |
| Gene groups (HGNC) | Glycoside hydrolase family |
| Hallmark sets | MYOGENESIS, GLYCOLYSIS |
| Reactome | 5 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P35573](https://www.uniprot.org/uniprotkb/P35573) (Glycogen debranching enzyme):

> Multifunctional enzyme acting as 1,4-alpha-D-glucan:1,4-alpha-D-glucan 4-alpha-D-glycosyltransferase and amylo-1,6-glucosidase in glycogen degradation.

**Summary**, from NCBI Gene [178](https://www.ncbi.nlm.nih.gov/gene/178):

> This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs which may be due to tissue-specific alternative splicing. Alternatively spliced transcripts …

**Accessions** — [HGNC:321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:321) · Entrez [178](https://www.ncbi.nlm.nih.gov/gene/178) · UniProt [P35573](https://www.uniprot.org/uniprotkb/P35573) · Ensembl [ENSG00000162688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162688)

## Data

Gene col 8561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8561); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8561]; `tensor/DDL_lfc|DDL_z.npy` [8561]; `embed/gene_vectors.npy` [8561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8561 or target_col == 8561). Every well: [[AGL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

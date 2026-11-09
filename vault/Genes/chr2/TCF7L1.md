---
symbol: "TCF7L1"
type: "gene"
col: 7612
ensembl_id: "ENSG00000152284"
name: "transcription factor 7 like 1"
location: "2p11.2"
module: 128
arm: "+"
pooled_cpm: 51.97
n_lines_expressing: 38
n_dd_up: 2
n_dd_down: 38
n_dd_up_clean: 2
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 17
direction_downstream: 16
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# TCF7L1

*transcription factor 7 like 1* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +6.8, q 7e-09, up in 20 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (NCI-H1573 4.00×, NCI-H2347 2.97×); [[Tucidinostat (drug)]] 0.5 µM in 2 lines (NCI-H1573 4.14×, NCI-H2347 3.89×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 2.05×, NCI-H460 2.07×; ⚠ cell-cycle shift, explains ~50% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.23×).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.502× (z -18.4, q 0e+00, down in 29 of 36 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.479× (z -13.9, q 8e-42, down in 30 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPT]] (+0.63, fdr 7e-06), [[CACNA2D2]] (+0.61, fdr 4e-05), [[HIP1]] (+0.57, fdr 1e-05); moves opposite to [[ARMCX4]] (-0.46, fdr 3e-05), [[HECTD1]] (-0.44, fdr 7e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[PDZD4]] → it (grade B ⚠); 16 go from it, the strongest it → [[DENND5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7612.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (NCI-H1573 4.00×, NCI-H2347 2.97×); [[Tucidinostat (drug)]] 0.5 µM in 2 lines (NCI-H1573 4.14×, NCI-H2347 3.89×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 2.05×, NCI-H460 2.07×; ⚠ cell-cycle shift, explains ~50% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.23×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.8 | 7e-09 | 20/36 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.2 | 2e-07 | 25/36 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.20× | +3.4 | 0.13 | 11/36 (A498, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.14 | 9/36 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.14 | 8/36 (A-172, HS-578T, …) | rises with dose | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.17 | 8/36 (C-33 A, SNU-1, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.0 | 0.18 | 10/36 (PANC-1, NCI-H1792, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.502×** | -18.4 | 0e+00 | 29/36 (A-427, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.413×** | -16.7 | 0e+00 | 32/36 (hTERT-HPNE, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -16.1 | 0e+00 | 28/31 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.479×** | -13.9 | 8e-42 | 30/36 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.483×** | -13.2 | 6e-38 | 28/36 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.565×** | -10.8 | 3e-25 | 26/36 (A549, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.603×** | -9.5 | 1e-19 | 24/36 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.399×** | -9.1 | 9e-18 | 23/37 (A-427, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -8.9 | 3e-17 | 25/36 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.618×** | -8.4 | 3e-15 | 23/33 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.658×** | -7.9 | 1e-13 | 20/36 (NCI-H2030, LOX-IMVI, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.665×** | -7.7 | 6e-13 | 25/36 (MIA PaCa-2, A549, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.659×** | -7.6 | 2e-12 | 22/35 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -7.0 | 1e-10 | 21/36 (PANC-1, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.684×** | -6.9 | 2e-10 | 24/35 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -6.8 | 5e-10 | 20/36 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.705×** | -6.6 | 1e-09 | 29/36 (H4, A549, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.586×** | -5.3 | 3e-06 | 19/36 (Hs 766T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.608×** | -4.9 | 2e-05 | 19/36 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.621×** | -4.7 | 6e-05 | 15/36 (SW480, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.625×** | -4.6 | 8e-05 | 21/36 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.789×** | -4.3 | 4e-04 | 13/36 (NCI-H23, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.804×** | -4.1 | 8e-04 | 18/35 (NCI-H460, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 92.4 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.290× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 14 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 84.3 | 0 | 13 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -17.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.270× (z -12.3) |
| [[A549 (line)]] | wt | 116 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -29.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.237× (z -18.9) |
| [[LOX-IMVI (line)]] | wt | 38.1 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0739× (z -18.7) |
| [[C32 (line)]] | wt | 64.3 | 0 | 11 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0894× (z -17.1) |
| [[SNU-1 (line)]] | wt | 79.3 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.246× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 87.4 | 1 (1 ⚠) | 9 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +10.1) ⚠ cell-cycle shift, explains ~50% of this change | [[Dinaciclib (drug)]] 5 µM 0.154× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.364× (z -9.6) |
| [[A-172 (line)]] | wt | 77.7 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.298× (z -11.5) |
| [[HS-578T (line)]] | alt | 74.8 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.302× (z -10.7) |
| [[PANC-1 (line)]] | alt | 118 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -23.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -17.0) |
| [[A-427 (line)]] | wt | 114 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0436× (z -35.3) |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0592× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 20.8 | 3 (1 ⚠) | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.00× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.292× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 62.0 | 2 (1 ⚠) | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 3.23× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 237 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0721× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 56.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 32.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.425× (z -9.3) |
| [[BT-474 (line)]] | alt | 49.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0597× (z -23.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 58.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -10.3) |
| [[LoVo (line)]] | wt | 38.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.273× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 14.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.97× (z +10.1) | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 2 (1 ⚠) | — | [[Proglumide (drug)]] 0.05 µM 0.0778× (z -9.3) |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 1 | — | [[Baicalin (drug)]] 0.5 µM 0.0597× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.248× (z -9.7) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 97.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPT]] | +0.63 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CACNA2D2]] | +0.61 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[HIP1]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[KREMEN2]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 | pathway: Signaling by WNT |
| [[DPYSL5]] | +0.53 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[KCNQ2]] | +0.53 | +0.44 / +0.50 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[CECR2]] | +0.52 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CIB2]] | +0.52 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[PDZD4]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[JARID2]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.52 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[P4HA2]] | +0.51 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX4]] | -0.46 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[HECTD1]] | -0.44 | -0.37 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 8, C 9. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD4]] | B | PDZD4 activity raises TCF7L1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 3.99× lower at baseline in the lines without PDZD4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[KIF26A]] | B | KIF26A activity raises TCF7L1's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.82× lower at baseline in the lines without KIF26A | 0.008 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[ELFN1]] | B | ELFN1 activity strengthens TCF7L1's drug response | lines that do not express ELFN1 (15) vs lines expressing it (22) | the lines without ELFN1 respond 0.63× as strongly (z diff +2.70); strongest at Homoharringtonine 5 µM: 0.63x vs 0.41x (z diff +3.9) | 0.010 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; target measured in part of the lines; artifact flags |
| [[GPR155]] | B | GPR155 activity raises TCF7L1's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 5.52× lower at baseline in the lines without GPR155 | 0.031 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[LRRC4B]] | B | LRRC4B activity raises TCF7L1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.74× lower at baseline in the lines without LRRC4B | 0.040 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[APLP1]] | B | APLP1 activity raises TCF7L1's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 3.02× lower at baseline in the lines without APLP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[TSHZ3]] | B | TSHZ3 activity raises TCF7L1's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 2.96× lower at baseline in the lines without TSHZ3 | 0.070 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[RNF220]] | B | RNF220 activity raises TCF7L1's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 2.42× lower at baseline in the lines without RNF220 | 0.085 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[RAB6B]] | C | RAB6B activity raises TCF7L1's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 5.02× lower at baseline in the lines without RAB6B | 0.001 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |
| [[STOX2]] | C | STOX2 activity raises TCF7L1's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.98× lower at baseline in the lines without STOX2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[MAPT]] | C | MAPT activity raises TCF7L1's level | lines that do not express MAPT (10) vs lines expressing it (40) | 4.93× lower at baseline in the lines without MAPT | 0.011 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1; co-absent with the target |
| [[SYNGR1]] | C | SYNGR1 activity raises TCF7L1's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 5.49× lower at baseline in the lines without SYNGR1 | 0.017 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 11, C 5. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND5A]] | B | TCF7L1 activity raises DENND5A's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.50× lower at baseline in the lines without TCF7L1 | 0.032 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[GPR155]] | B | TCF7L1 activity raises GPR155's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.57× lower at baseline in the lines without TCF7L1 | 0.042 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[BCAS4]] | B | TCF7L1 activity raises BCAS4's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without TCF7L1 | 0.048 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[MAP3K15]] | B | TCF7L1 activity raises MAP3K15's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.55× lower at baseline in the lines without TCF7L1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[AZIN2]] | B | TCF7L1 activity raises AZIN2's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 1.61× lower at baseline in the lines without TCF7L1 | 0.075 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[RNF130]] | B | TCF7L1 activity raises RNF130's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 1.67× lower at baseline in the lines without TCF7L1 | 0.078 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[GLI2]] | B | TCF7L1 activity raises GLI2's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.20× lower at baseline in the lines without TCF7L1 | 0.080 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[HIP1]] | B | TCF7L1 activity raises HIP1's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.30× lower at baseline in the lines without TCF7L1 | 0.083 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[KIF26A]] | B | TCF7L1 activity raises KIF26A's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.05× lower at baseline in the lines without TCF7L1 | 0.084 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[SEPTIN6]] | B | TCF7L1 activity strengthens SEPTIN6's drug response | lines that do not express TCF7L1 (11) vs lines expressing it (36) | the lines without TCF7L1 respond 0.80× as strongly (z diff +0.98); strongest at Digitoxin 5 µM: 0.72x vs 0.45x (z diff +3.6) | 0.090 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A; target measured in part of the lines; artifact flags |
| [[KATNAL1]] | B | TCF7L1 activity raises KATNAL1's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 3.07× lower at baseline in the lines without TCF7L1 | 0.0995 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[STOX2]] | C | TCF7L1 activity raises STOX2's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 5.50× lower at baseline in the lines without TCF7L1 | 0.004 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.2, 38.2); signed map (26.5, 26.3). **Vector** length 103, 28.0% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.5 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | +3.3 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -13.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.4 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | -6.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor 7 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,133,392-85,310,387 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TCF3 |
| Gene groups (HGNC) | TCF/LEF transcription factor family; Wnt enhanceosome complex |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 21 pathways, smallest: RUNX3 regulates WNT signaling; Binding of TCF/LEF:CTNNB1 to target gene promoters; Specification of the neural plate border |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCS4](https://www.uniprot.org/uniprotkb/Q9HCS4) (Transcription factor 7-like 1):

> Participates in the Wnt signaling pathway. Binds to DNA and acts as a repressor in the absence of CTNNB1, and as an activator in its presence. Necessary for the terminal differentiation of epidermal cells, the formation of keratohyalin granules and the development of the barrier function of the epidermis (By similarity). Down-regulates NQO1, leading to increased mitomycin c resistance.

**Summary**, from NCBI Gene [83439](https://www.ncbi.nlm.nih.gov/gene/83439):

> This gene encodes a member of the T cell factor/lymphoid enhancer factor family of transcription factors. These transcription factors are activated by beta catenin, mediate the Wnt signaling pathway and are antagonized by the transforming growth factor beta signaling pathway. The encoded protein contains a high mobility group-box DNA binding domain and participates in the regulation of cell cycle genes and cellular senescence. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:11640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11640) · Entrez [83439](https://www.ncbi.nlm.nih.gov/gene/83439) · UniProt [Q9HCS4](https://www.uniprot.org/uniprotkb/Q9HCS4) · Ensembl [ENSG00000152284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152284)

## Data

Gene col 7612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7612); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7612]; `tensor/DDL_lfc|DDL_z.npy` [7612]; `embed/gene_vectors.npy` [7612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7612 or target_col == 7612). Every well: [[TCF7L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCF7L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "FASTKD2"
type: "gene"
col: 3974
ensembl_id: "ENSG00000118246"
name: "FASTK mitochondrial RNA regulator 2"
location: "2q33.3"
module: 1
arm: "+"
pooled_cpm: 37.03
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 17
n_dd_up_clean: 20
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FASTKD2

*FASTK mitochondrial RNA regulator 2* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +17.1, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.552× (z -12.2, q 2e-31, down in 37 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.643× (z -9.1, q 4e-17, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL11]] (+0.74, fdr 7e-06), [[WARS2]] (+0.71, fdr 7e-06), [[MRPS7]] (+0.71, fdr 7e-06); moves opposite to [[CAMTA1]] (-0.62, fdr 1e-05), [[NPTN]] (-0.58, fdr 3e-05), [[ADAM10]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ANKEF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +17.1 | 0e+00 | 41/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.85×** | +12.5 | 2e-33 | 42/48 (NCI-H1573, PANC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +12.4 | 9e-33 | 42/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +11.9 | 3e-30 | 40/48 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.82×** | +11.5 | 2e-28 | 42/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +10.1 | 6e-22 | 35/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +9.9 | 5e-21 | 39/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +9.3 | 1e-18 | 41/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +8.2 | 1e-14 | 1/48 (NCI-H661) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +8.2 | 1e-14 | 34/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +8.1 | 3e-14 | 35/48 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +7.7 | 7e-13 | 33/48 (A498, AsPC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +6.6 | 2e-09 | 29/48 (PANC-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.2 | 9e-06 | 19/48 (NCI-H2030, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.9 | 3e-05 | 21/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 2e-04 | 20/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 3e-04 | 15/48 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +4.3 | 5e-04 | 17/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3974.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.552×** | -12.2 | 2e-31 | 37/47 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.643×** | -9.1 | 4e-17 | 38/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.655×** | -8.7 | 8e-16 | 28/48 (SNU-423, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -7.6 | 6e-12 | 34/48 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -7.3 | 3e-11 | 27/48 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.703×** | -7.2 | 4e-11 | 32/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -7.2 | 6e-11 | 29/48 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.717×** | -6.8 | 7e-10 | 29/48 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.749×** | -5.9 | 2e-07 | 26/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -5.9 | 2e-07 | 25/39 (H4, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.775×** | -5.2 | 8e-06 | 23/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.810×** | -4.3 | 7e-04 | 21/48 (AN3 CA, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.799×** | -4.3 | 9e-04 | 19/44 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -4.0 | 0.003 | 21/48 (SK-MEL-2, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.767×** | -3.9 | 0.004 | 18/48 (LS 180, SW 1088, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.808×** | -3.1 | 0.058 | 14/48 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.059 | 9/48 (PANC-1, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.904× | -3.0 | 0.093 | 5/48 (CHP-212, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.6 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 31.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 49.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 33.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.13× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 38.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 48.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -10.8) |
| [[RKO (line)]] | wt | 58.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -12.7) |
| [[A-172 (line)]] | wt | 33.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 43.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 37.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 49.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.6) |
| [[A-427 (line)]] | wt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +11.5) | — |
| [[A549 (line)]] | wt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0876× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 45.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.2) | — |
| [[H4 (line)]] | wt | 54.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0907× (z -14.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -14.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.161× (z -12.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 36.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.8) | — |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -12.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 46.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -10.8) |
| [[SHP-77 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -13.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.9) |
| [[SNU-1 (line)]] | wt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 36.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.304× (z -9.6) |
| [[SW480 (line)]] | alt | 34.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.467× (z -9.3) |
| [[CHP-212 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL11]] | +0.74 | +0.64 / +0.77 | both halves | 7e-06 | pathway: rRNA processing; STRING 458 |
| [[WARS2]] | +0.71 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[MRPS7]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[MRPL38]] | +0.69 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[GATB]] | +0.69 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[UTP20]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 | pathway: rRNA processing |
| [[AFG1L]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TTC27]] | +0.66 | +0.58 / +0.63 | both halves | 7e-06 | same gene group |
| [[TRMT5]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 | STRING 474 |
| [[MRM3]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 | pathway: rRNA modification in the mitochondrion; STRING 692 |
| [[SMYD5]] | +0.65 | +0.47 / +0.71 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMTA1]] | -0.62 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[NPTN]] | -0.58 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ADAM10]] | -0.57 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKEF1]] | B | ANKEF1 activity lowers FASTKD2's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.31× higher at baseline in the lines without ANKEF1 | 0.034 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[TOP2A]] | B | TOP2A activity raises FASTKD2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.8, 11.4); signed map (10.9, -31.3). **Vector** length 99.0, 25.1% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.8 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +11.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +12.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.1 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -8.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -7.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -7.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | FASTK mitochondrial RNA regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:206,765,357-206,796,189 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0971 |
| Gene groups (HGNC) | FASTK mitochondrial RNA binding family; MicroRNA protein coding host genes |
| Reactome | 7 pathways, smallest: rRNA modification in the mitochondrion; FASTK family proteins regulate processing and stability of mitochondrial RNAs; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYY8](https://www.uniprot.org/uniprotkb/Q9NYY8) (FAST kinase domain-containing protein 2, mitochondrial):

> Plays an important role in assembly of the mitochondrial large ribosomal subunit. As a component of a functional protein-RNA module, consisting of RCC1L, NGRN, RPUSD3, RPUSD4, TRUB2, FASTKD2 and 16S mitochondrial ribosomal RNA (16S mt-rRNA), controls 16S mt-rRNA abundance and is required for intra-mitochondrial translation. May play a role in mitochondrial apoptosis.

**Summary**, from NCBI Gene [22868](https://www.ncbi.nlm.nih.gov/gene/22868):

> This gene encodes a protein that is localized in the mitochondrial inner compartment and that may play a role in mitochondrial apoptosis. Nonsense mutations have been reported to result in cytochrome c oxidase deficiency. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:29160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29160) · Entrez [22868](https://www.ncbi.nlm.nih.gov/gene/22868) · UniProt [Q9NYY8](https://www.uniprot.org/uniprotkb/Q9NYY8) · Ensembl [ENSG00000118246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118246)

## Data

Gene col 3974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3974); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3974]; `tensor/DDL_lfc|DDL_z.npy` [3974]; `embed/gene_vectors.npy` [3974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3974 or target_col == 3974). Every well: [[FASTKD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FASTKD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

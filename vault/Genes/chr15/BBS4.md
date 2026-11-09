---
symbol: "BBS4"
type: "gene"
col: 6412
ensembl_id: "ENSG00000140463"
name: "Bardet-Biedl syndrome 4"
location: "15q24.1"
module: 187
arm: "+"
pooled_cpm: 26.82
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# BBS4

*Bardet-Biedl syndrome 4* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +8.7, q 2e-15, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.552× (z -12.1, q 4e-31, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLYWCH1]] (+0.63, fdr 8e-06), [[CCS]] (+0.61, fdr 1e-05), [[ISCU]] (+0.60, fdr 3e-05); moves opposite to [[CHML]] (-0.57, fdr 1e-05), [[STAG1]] (-0.54, fdr 1e-05), [[LINC00342]] (-0.53, fdr 1e-05).
> It is in [[Module 187]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.7 | 2e-15 | 27/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +8.6 | 3e-15 | 33/48 (NCI-H1792, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +8.2 | 6e-14 | 31/48 (HOP62, COLO 205, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +8.0 | 1e-13 | 29/48 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.30×** | +5.3 | 1e-05 | 22/47 (COLO 205, HOP62, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +5.3 | 1e-05 | 17/47 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.20× | +5.2 | 1e-05 | 19/48 (LOX-IMVI, RKO, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +5.2 | 1e-05 | 18/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +4.3 | 8e-04 | 18/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 8e-04 | 14/48 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 8e-04 | 13/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.004 | 11/48 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.8 | 0.005 | 19/47 (LoVo, NCI-H1792, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.015 | 11/48 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.19× | +3.5 | 0.018 | 10/48 (A549, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.030 | 5/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.034 | 12/48 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.036 | 4/48 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.044 | 15/47 (SNU-423, BT-474, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.1 | 0.063 | 12/48 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +2.9 | 0.090 | 5/48 (HT-29, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6412.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.552×** | -12.1 | 4e-31 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.546×** | -11.9 | 4e-30 | 37/47 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.552×** | -11.2 | 8e-27 | 21/39 (AsPC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.580×** | -10.7 | 1e-24 | 37/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.625×** | -9.6 | 1e-19 | 32/44 (NCI-H460, HCT15, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -9.6 | 1e-19 | 33/47 (SW480, HCT15, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.640×** | -9.1 | 6e-18 | 32/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.651×** | -8.5 | 2e-15 | 29/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -7.4 | 7e-12 | 23/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.740×** | -5.9 | 2e-07 | 21/47 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.764×** | -5.5 | 2e-06 | 21/47 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -5.2 | 9e-06 | 18/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.626×** | -5.0 | 3e-05 | 17/47 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.777×** | -5.0 | 3e-05 | 18/34 (A549, SW 900, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.790×** | -4.8 | 6e-05 | 17/47 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.656×** | -4.5 | 2e-04 | 16/47 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.665×** | -4.4 | 4e-04 | 15/47 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.674×** | -4.2 | 7e-04 | 18/48 (NCI-H460, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.675×** | -4.2 | 7e-04 | 10/48 (NCI-H460, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.839× | -3.6 | 0.007 | 6/48 (A549, PANC-1, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.740×** | -3.2 | 0.025 | 8/47 (H4, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.2 | 2 (1 ⚠) | 8 (5 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -14.8) |
| [[A549 (line)]] | wt | 48.6 | 3 (3 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +11.5) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.0765× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[LoVo (line)]] | wt | 17.8 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +12.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -9.2) |
| [[SW480 (line)]] | alt | 31.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.219× (z -16.4) |
| [[KATO III (line)]] | alt | 20.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -10.2) |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -8.8) |
| [[A498 (line)]] | wt | 23.8 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +10.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[COLO 205 (line)]] | alt | 37.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -8.8) |
| [[HCT15 (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 49.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.369× (z -9.5) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.509× (z -9.5) |
| [[SHP-77 (line)]] | alt | 44.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -9.6) |
| [[SW48 (line)]] | wt | 18.4 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.0710× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0977× (z -12.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.338× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.216× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.189× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.458× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 36.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[A-172 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLYWCH1]] | +0.63 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[CCS]] | +0.61 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ISCU]] | +0.60 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[EAPP]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ZRSR2]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CCDC167]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[NKAP]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CDC37L1]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SPATA7]] | +0.57 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[AP3S2]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[EZH1]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHML]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[STAG1]] | -0.54 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[LINC00342]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[APPAT]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[TFDP1]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 | pathway: Cilium Assembly |
| [[EIF4G1]] | -0.50 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ACTB]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[PITPNB]] | -0.49 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TULP4]] | -0.48 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SFPQ]] | -0.48 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[EIF5A]] | -0.48 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RAB4A-AS1]] | -0.48 | -0.48 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.0, -50.6); signed map (-14.3, 4.9). **Vector** length 100, 23.8% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.4 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +4.8 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.8 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +3.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -11.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -11.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | Bardet-Biedl syndrome 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:72,686,179-72,738,475 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; BBSome; Centriolar satellite proteins |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RK4](https://www.uniprot.org/uniprotkb/Q96RK4) (BBSome complex member BBS4):

> The BBSome complex is thought to function as a coat complex required for sorting of specific membrane proteins to the primary cilia. The BBSome complex is required for ciliogenesis but is dispensable for centriolar satellite function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which localizes to the basal body and contacts the BBSome. Rab8(GTP) enters the primary cilium and promotes extension of the ciliary membrane. Firstly the BBSome associates with the …

**Summary**, from NCBI Gene [585](https://www.ncbi.nlm.nih.gov/gene/585):

> This gene is a member of the Bardet-Biedl syndrome (BBS) gene family. Bardet-Biedl syndrome is an autosomal recessive disorder characterized by severe pigmentary retinopathy, obesity, polydactyly, renal malformation and cognitive disability. The proteins encoded by BBS gene family members are structurally diverse. The similar phenotypes exhibited by mutations in BBS gene family members are likely due to the protein's shared roles in cilia formation and function. Many BBS proteins localize to …

**Accessions** — [HGNC:969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:969) · Entrez [585](https://www.ncbi.nlm.nih.gov/gene/585) · UniProt [Q96RK4](https://www.uniprot.org/uniprotkb/Q96RK4) · Ensembl [ENSG00000140463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140463)

## Data

Gene col 6412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6412); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6412]; `tensor/DDL_lfc|DDL_z.npy` [6412]; `embed/gene_vectors.npy` [6412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6412 or target_col == 6412). Every well: [[BBS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

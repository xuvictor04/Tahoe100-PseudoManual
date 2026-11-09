---
symbol: "MGAT5"
type: "gene"
col: 7593
ensembl_id: "ENSG00000152127"
name: "alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase"
location: "2q21.2-q21.3"
module: 134
arm: "+"
pooled_cpm: 348.22
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# MGAT5

*alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase* — 2q21.2-q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.36× (z +5.4, q 5e-05, up in 30 of 48 measured lines) ⚠ unreliable plate only. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.44×, NCI-H460 2.93×); [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 3.74×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 3.31×; ⚠ unreliable plate only); [[TAK-901 (drug)]] 0.05 µM in 1 line (C32 2.23×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.505× (z -16.9, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBA6]] (+0.57, fdr 1e-05), [[AGAP1]] (+0.57, fdr 1e-05), [[SLC2A1]] (+0.56, fdr 1e-05); moves opposite to [[RNF115]] (-0.57, fdr 1e-05), [[GIGYF1]] (-0.55, fdr 2e-05), [[KLF6]] (-0.52, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC2A1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7593.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.44×, NCI-H460 2.93×); [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 3.74×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 3.31×; ⚠ unreliable plate only); [[TAK-901 (drug)]] 0.05 µM in 1 line (C32 2.23×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.4 | 5e-05 | 30/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.28×** | +4.1 | 0.014 | 24/48 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.43× | +3.3 | 0.18 | 26/48 (SHP-77, SW 900, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.505×** | -16.9 | 0e+00 | 39/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.399×** | -16.1 | 0e+00 | 48/49 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.434×** | -14.1 | 1e-42 | 41/44 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.452×** | -13.9 | 1e-41 | 44/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.427×** | -13.8 | 6e-41 | 39/45 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.442×** | -13.7 | 8e-41 | 45/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.497×** | -11.8 | 5e-30 | 42/48 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -6.7 | 2e-09 | 34/48 (NCI-H1573, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -6.4 | 8e-09 | 38/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.706×** | -6.1 | 6e-08 | 27/48 (KATO III, CHP-212, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.733×** | -5.4 | 3e-06 | 32/48 (NCI-H1573, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.737×** | -5.3 | 5e-06 | 29/48 (SW1417, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -5.3 | 6e-06 | 23/49 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.759×** | -4.8 | 6e-05 | 35/48 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.768×** | -4.6 | 2e-04 | 30/48 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.860× | -3.7 | 0.007 | 20/48 (NCI-H1573, H4, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.819×** | -3.5 | 0.015 | 25/48 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -3.5 | 0.016 | 14/48 (SW480, SW48, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.024 | 22/48 (SW48, SW480, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.033 | 21/49 (H4, NCI-H1573, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.833×** | -3.2 | 0.033 | 21/48 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.881× | -3.1 | 0.038 | 2/49 (SW 1271, SW48) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 804 | 0 | 24 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -23.3) |
| [[NCI-H1573 (line)]] | alt | 343 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -27.8) |
| [[SW48 (line)]] | wt | 1,048 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -19.3) |
| [[SW1417 (line)]] | alt | 921 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.221× (z -16.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -15.9) |
| [[LOX-IMVI (line)]] | wt | 397 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -20.8) |
| [[J82 (line)]] | alt | 277 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -16.0) |
| [[LoVo (line)]] | wt | 502 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -25.7) |
| [[LS 180 (line)]] | wt | 529 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 305 | 2 (1 ⚠) | 6 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.31× (z +13.7) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 4.57× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -14.1) |
| [[C32 (line)]] | wt | 362 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.23× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.416× (z -10.9) |
| [[HS-578T (line)]] | alt | 319 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -22.2) |
| [[KATO III (line)]] | alt | 296 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 268 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -24.3) |
| [[NCI-H2030 (line)]] | alt | 402 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.305× (z -13.9) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.399× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 231 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -25.0) |
| [[SW 900 (line)]] | alt | 411 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.462× (z -13.1) |
| [[CHP-212 (line)]] | wt | 254 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -17.4) |
| [[HOP62 (line)]] | alt | 262 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 308 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 534 | 2 | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.93× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -17.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 237 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -18.4) |
| [[H4 (line)]] | wt | 421 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -15.2) |
| [[HT-29 (line)]] | alt | 396 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 399 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.386× (z -10.4) |
| [[A-172 (line)]] | wt | 202 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -12.1) |
| [[A549 (line)]] | wt | 201 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -20.0) |
| [[C-33 A (line)]] | alt | 252 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 224 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -12.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 719 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -14.3) |
| [[HCT15 (line)]] | alt | 311 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -18.0) |
| [[HEC-1-A (line)]] | alt | 251 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.512× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 273 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 180 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -17.8) |
| [[PANC-1 (line)]] | alt | 115 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.44× (z +17.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.459× (z -11.7) |
| [[A-427 (line)]] | wt | 148 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -13.1) |
| [[A498 (line)]] | wt | 313 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 235 | 1 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.61× (z +11.3) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 153 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.2) |
| [[SNU-423 (line)]] | alt | 194 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -15.7) |
| [[BT-474 (line)]] | alt | 177 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +19.8) | — |
| [[Hs 766T (line)]] | wt | 196 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 751 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 402 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 283 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 265 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[AGAP1]] | +0.57 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SLC2A1]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[PDE8A]] | +0.55 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[VDAC1]] | +0.55 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[GMDS]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation; STRING 410 |
| [[SNX25]] | +0.53 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[MALT1]] | +0.51 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[CHSY1]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[INPP5A]] | +0.50 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[SHB]] | +0.50 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[PTDSS1]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | -0.57 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[GIGYF1]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[KLF6]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[POLR3C]] | -0.52 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[UBXN2A]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ZNF383]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ZNF776]] | -0.51 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[ZNF181]] | -0.51 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[EHHADH]] | -0.50 | -0.57 / -0.41 | both halves | 4e-05 | same gene group |
| [[ZNF226]] | -0.50 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ZNF140]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[FBXL9P]] | -0.50 | -0.58 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A1]] | C | SLC2A1 activity raises MGAT5's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without SLC2A1 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.1, 14.5); signed map (-39.0, 28.6). **Vector** length 122, 42.8% of its response variance represented; |z| ≥ 3 in 1,608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.3 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +1.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -13.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.0 | -13.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.8 | -1.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -11.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.6 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.4 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.2-q21.3 — chr2:134,119,983-134,454,621 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GNT-V, MGAT5A |
| Gene groups (HGNC) | Mannosyl-glycoprotein N-acetylglucosaminyltransferases; MicroRNA protein coding host genes |
| Reactome | 10 pathways, smallest: N-Glycan antennae elongation; N-glycan antennae elongation in the medial/trans-Golgi; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q09328](https://www.uniprot.org/uniprotkb/Q09328) (Alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase A):

> Catalyzes the addition of N-acetylglucosamine (GlcNAc) in beta 1-6 linkage to the alpha-linked mannose of biantennary N-linked oligosaccharides. Catalyzes an important step in the biosynthesis of branched, complex-type N-glycans, such as those found on EGFR, TGFR (TGF-beta receptor) and CDH2. Via its role in the biosynthesis of complex N-glycans, plays an important role in the activation of cellular signaling pathways, reorganization of the actin cytoskeleton, cell-cell adhesion and cell …

**Summary**, from NCBI Gene [4249](https://www.ncbi.nlm.nih.gov/gene/4249):

> The protein encoded by this gene belongs to the glycosyltransferase family. It catalyzes the addition of beta-1,6-N-acetylglucosamine to the alpha-linked mannose of biantennary N-linked oligosaccharides present on the newly synthesized glycoproteins. It is one of the most important enzymes involved in the regulation of the biosynthesis of glycoprotein oligosaccharides. Alterations of the oligosaccharides on cell surface glycoproteins cause significant changes in the adhesive or migratory …

**Accessions** — [HGNC:7049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7049) · Entrez [4249](https://www.ncbi.nlm.nih.gov/gene/4249) · UniProt [Q09328](https://www.uniprot.org/uniprotkb/Q09328) · Ensembl [ENSG00000152127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152127)

## Data

Gene col 7593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7593); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7593]; `tensor/DDL_lfc|DDL_z.npy` [7593]; `embed/gene_vectors.npy` [7593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7593 or target_col == 7593). Every well: [[MGAT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGAT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

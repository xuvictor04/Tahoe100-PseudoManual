---
symbol: "LARGE1"
type: "gene"
col: 5448
ensembl_id: "ENSG00000133424"
name: "LARGE xylosyl- and glucuronyltransferase 1"
location: "22q12.3"
module: 17
arm: "-"
pooled_cpm: 104.72
n_lines_expressing: 41
n_dd_up: 29
n_dd_down: 9
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# LARGE1

*LARGE xylosyl- and glucuronyltransferase 1* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +29.8, q 0e+00, up in 33 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.532× (z -13.5, q 7e-39, down in 25 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.637× (z -4.8, q 2e-04, down in 19 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (HT-29 0.223×, LS 180 0.223×, SNU-423 0.228×, C32 0.311×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (RKO 0.105×, C-33 A 0.0873×, LoVo 0.221×, SW1417 0.277×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SK-MEL-2 0.0969×, KATO III 0.206×, SHP-77 0.185×, SNU-423 0.246×; ⚠ toxic; transcription drop); [[Budesonide (drug)]] 0.5 µM in 2 lines (A549 0.316×, NCI-H1573 0.376×); [[Dexamethasone (drug)]] 0.5 µM in 2 lines (A549 0.337×, NCI-H1573 0.391×); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (A549 0.281×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP21]] (+0.57, fdr 2e-04), [[GRIP1]] (+0.57, fdr 1e-05), [[MSX1]] (+0.55, fdr 2e-05); moves opposite to [[MRPS31P5-1]] (-0.60, fdr 2e-05), [[LRIG2]] (-0.57, fdr 1e-05), [[CNEP1R1]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZFAND3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +29.8 | 0e+00 | 33/39 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +19.7 | 0e+00 | 34/40 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +12.4 | 3e-33 | 30/39 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +11.6 | 1e-28 | 31/39 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +11.3 | 1e-27 | 32/39 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +11.3 | 1e-27 | 29/39 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +11.1 | 8e-27 | 32/39 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +11.1 | 2e-26 | 32/39 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +10.9 | 5e-26 | 34/39 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +10.9 | 6e-26 | 27/39 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +10.6 | 1e-24 | 27/39 (C32, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.58×** | +10.1 | 2e-22 | 29/39 (HOP62, H4, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +8.3 | 5e-15 | 26/39 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +8.2 | 1e-14 | 25/39 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +8.1 | 2e-14 | 28/41 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +5.9 | 1e-07 | 20/39 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5448.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (HT-29 0.223×, LS 180 0.223×, SNU-423 0.228×, C32 0.311×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (RKO 0.105×, C-33 A 0.0873×, LoVo 0.221×, SW1417 0.277×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SK-MEL-2 0.0969×, KATO III 0.206×, SHP-77 0.185×, SNU-423 0.246×; ⚠ toxic; transcription drop); [[Budesonide (drug)]] 0.5 µM in 2 lines (A549 0.316×, NCI-H1573 0.376×); [[Dexamethasone (drug)]] 0.5 µM in 2 lines (A549 0.337×, NCI-H1573 0.391×); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (A549 0.281×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -13.5 | 7e-39 | 25/35 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.589×** | -10.3 | 2e-22 | 24/40 (RKO, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.634×** | -9.7 | 4e-20 | 28/38 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.657×** | -8.6 | 7e-16 | 26/36 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **0.755×** | -6.3 | 4e-08 | 26/39 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.637×** | -4.8 | 2e-04 | 19/40 (KATO III, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.652×** | -4.5 | 5e-04 | 15/30 (HT-29, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.715×** | -3.6 | 0.026 | 15/38 (KATO III, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.729×** | -3.3 | 0.051 | 14/39 (LS 180, CHP-212, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.867× | -3.2 | 0.079 | 13/39 (A549, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 399 | 13 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +25.0) | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 184 | 0 | 16 (1 ⚠) | — | [[Budesonide (drug)]] 0.5 µM 0.316× (z -10.8) |
| [[SW480 (line)]] | alt | 93.3 | 15 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +23.1) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -10.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 32.4 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +24.7) | — |
| [[A498 (line)]] | wt | 34.2 | 11 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +27.8) | — |
| [[NCI-H460 (line)]] | wt | 32.2 | 11 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.37× (z +26.5) | — |
| [[NCI-H1573 (line)]] | alt | 143 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Budesonide (drug)]] 0.5 µM 0.376× (z -9.7) |
| [[SW1417 (line)]] | alt | 144 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 192 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -20.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 345 | 4 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -18.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 190 | 4 | 3 (3 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +17.9) | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -15.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 69.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +21.6) | — |
| [[H4 (line)]] | wt | 67.3 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +16.5) | — |
| [[Hs 766T (line)]] | wt | 43.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +19.4) | — |
| [[HT-29 (line)]] | alt | 211 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -16.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 93.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +23.7) | — |
| [[SK-MEL-2 (line)]] | alt | 132 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -26.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 36.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +14.3) | — |
| [[RKO (line)]] | wt | 340 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -25.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 141 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -19.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 74.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +21.6) | — |
| [[HEC-1-A (line)]] | alt | 29.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 53.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +16.2) | — |
| [[SNU-1 (line)]] | wt | 137 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 138 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -15.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 99.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -13.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 212 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -10.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 29.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +20.2) | — |
| [[SW 1088 (line)]] | alt | 135 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +11.2) | [[Bendamustine (drug)]] 5 µM 0.0970× (z -8.7) |
| [[AN3 CA (line)]] | alt | 215 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0873× (z -22.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +24.6) | — |
| [[CHP-212 (line)]] | wt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 149 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +17.4) | — |
| [[HS-578T (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.6) | — |
| [[SW48 (line)]] | wt | 237 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -9.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 60.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP21]] | +0.57 | +0.32 / +0.48 | both halves | 2e-04 |  |
| [[GRIP1]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MSX1]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[PRKCE]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.52 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[LITAF]] | +0.50 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[AHCYL2]] | +0.50 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[CASK]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ACVR1C]] | +0.50 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PGBD5]] | +0.49 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[FRYL]] | +0.49 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[MIB1]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P5-1]] | -0.60 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[LRIG2]] | -0.57 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[CNEP1R1]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[POT1]] | -0.55 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[MRPS31P4]] | -0.55 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[PRPF3]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ZNF17]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[EXD2]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ABHD10]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[DTWD1]] | -0.52 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[HEATR6]] | -0.51 | -0.58 / -0.41 | both halves | 4e-05 | same gene group |
| [[AARSD1]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LARGE1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFAND3]] | B | LARGE1 activity lowers ZFAND3's level | lines that do not express LARGE1 (9) vs lines expressing it (41) | 1.32× higher at baseline in the lines without LARGE1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000249141; maybe low, not absent |
| [[TSFM]] | B | LARGE1 activity lowers TSFM's level | lines that do not express LARGE1 (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without LARGE1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000249141; maybe low, not absent |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-3.8, -7.8); signed map (13.0, 20.9). **Vector** length 107, 29.6% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +10.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.5 | +10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.4 | +11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +11.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +4.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -9.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.0 | -0.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | LARGE xylosyl- and glucuronyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:33,162,226-33,922,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0609; previously LARGE |
| Gene groups (HGNC) | Glycosyltransferase family 8; MicroRNA protein coding host genes |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_LATE, HYPOXIA |
| Reactome | 6 pathways, smallest: Matriglycan biosynthesis on DAG1; DAG1 glycosylations; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O95461](https://www.uniprot.org/uniprotkb/O95461) (Xylosyl- and glucuronyltransferase LARGE1):

> Bifunctional glycosyltransferase with both alpha-1,3-xylosyltransferase and beta-1,3-glucuronyltransferase activities involved in the maturation of alpha-dystroglycan (DAG1) by glycosylation leading to DAG1 binding to laminin G-like domain-containing extracellular proteins with high affinity. Elongates the glucuronyl-beta-1,4-xylose-beta disaccharide primer structure initiated by B4GAT1 by adding repeating units [-3-Xylose-alpha-1,3-GlcA-beta-1-] to produce a heteropolysaccharide. Requires the …

**Summary**, from NCBI Gene [9215](https://www.ncbi.nlm.nih.gov/gene/9215):

> This gene encodes a member of the N-acetylglucosaminyltransferase gene family. It encodes a glycosyltransferase which participates in glycosylation of alpha-dystroglycan, and may carry out the synthesis of glycoprotein and glycosphingolipid sugar chains. It may also be involved in the addition of a repeated disaccharide unit. The protein encoded by this gene is the glycotransferase that adds the final xylose and glucuronic acid to alpha-dystroglycan and thereby allows alpha-dystroglycan to bind …

**Accessions** — [HGNC:6511](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6511) · Entrez [9215](https://www.ncbi.nlm.nih.gov/gene/9215) · UniProt [O95461](https://www.uniprot.org/uniprotkb/O95461) · Ensembl [ENSG00000133424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133424)

## Data

Gene col 5448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5448); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5448]; `tensor/DDL_lfc|DDL_z.npy` [5448]; `embed/gene_vectors.npy` [5448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5448 or target_col == 5448). Every well: [[LARGE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARGE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

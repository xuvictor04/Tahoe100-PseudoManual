---
symbol: "EXD3"
type: "gene"
col: 11929
ensembl_id: "ENSG00000187609"
name: "exonuclease 3'-5' domain containing 3"
location: "9q34.3"
module: 37
arm: "+"
pooled_cpm: 26.44
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# EXD3

*exonuclease 3'-5' domain containing 3* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.71× (z +10.2, q 7e-22, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 5 lines (SW480 3.32×, HEC-1-A 3.06×, NCI-H2347 4.91×, SW1417 2.88×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 4.79×, A498 2.44×); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 6.55×, AsPC-1 3.49×; ⚠ cell-cycle shift, explains ~57% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 2.84×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.636× (z -12.2, q 2e-31, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.351× (z -10.4, q 6e-23, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIPE-AS1]] (+0.64, fdr 7e-06), [[TPT1-AS1]] (+0.63, fdr 1e-05), [[L3MBTL1]] (+0.62, fdr 2e-05); moves opposite to [[MDH1]] (-0.64, fdr 7e-06), [[LANCL1]] (-0.57, fdr 3e-05), [[DLAT]] (-0.57, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11929.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 5 lines (SW480 3.32×, HEC-1-A 3.06×, NCI-H2347 4.91×, SW1417 2.88×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 4.79×, A498 2.44×); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 6.55×, AsPC-1 3.49×; ⚠ cell-cycle shift, explains ~57% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 2.84×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +10.2 | 7e-22 | 30/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +6.1 | 4e-07 | 23/47 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.20× | +3.2 | 0.15 | 9/47 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.15 | 11/47 (H4, NCI-H1573, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.18× | +3.2 | 0.15 | 11/47 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Arbutin (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.15 | 5/47 (RKO, LS 180, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.15 | 8/47 (A549, BT-474, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.15 | 7/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.12× | +3.0 | 0.15 | 3/48 (J82, BT-474, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.636×** | -12.2 | 2e-31 | 31/47 (A549, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.351×** | -10.4 | 6e-23 | 39/48 (HEC-1-A, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.434×** | -8.3 | 2e-14 | 31/45 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.633×** | -8.2 | 2e-14 | 31/45 (SNU-1, NCI-H23, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.658×** | -8.0 | 2e-13 | 25/47 (MIA PaCa-2, A-427, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.645×** | -7.9 | 3e-13 | 17/33 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.681×** | -6.9 | 3e-10 | 27/47 (A498, LS 180, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **0.722×** | -6.2 | 4e-08 | 24/44 (C-33 A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -6.0 | 1e-07 | 24/47 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.807×** | -5.8 | 5e-07 | 24/48 (KATO III, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.751×** | -5.4 | 3e-06 | 22/48 (SNU-1, LS 180, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.776×** | -4.8 | 7e-05 | 22/47 (HCT15, KATO III, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.678×** | -3.9 | 0.005 | 17/45 (SNU-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.007 | 13/47 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.822×** | -3.7 | 0.008 | 19/48 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.009 | 18/47 (SW480, SNU-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.720×** | -3.3 | 0.034 | 8/46 (SNU-423, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.890× | -3.1 | 0.054 | 3/48 (SW 900, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.747×** | -2.9 | 0.099 | 7/46 (KATO III, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 43.5 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.06× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -12.2) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.412× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -13.0) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.287× (z -11.0) |
| [[A-172 (line)]] | wt | 25.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-427 (line)]] | wt | 20.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.231× (z -10.5) |
| [[A498 (line)]] | wt | 16.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.186× (z -12.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[AsPC-1 (line)]] | alt | 23.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +16.1) | — |
| [[HT-29 (line)]] | alt | 36.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LS 180 (line)]] | wt | 47.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[NCI-H1573 (line)]] | alt | 21.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +28.3) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[RKO (line)]] | wt | 38.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -9.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0978× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 40.1 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.32× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[A549 (line)]] | wt | 25.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HCT15 (line)]] | alt | 39.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.73× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[Hs 766T (line)]] | wt | 32.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[J82 (line)]] | alt | 29.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[KATO III (line)]] | alt | 63.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.510× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 28.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 29.4 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.84× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 26.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.88× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SW48 (line)]] | wt | 42.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.218× (z -9.0) |
| [[BT-474 (line)]] | alt | 58.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -11.2) ⚠ cell-cycle shift, explains ~55% of this change |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[H4 (line)]] | wt | 14.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0972× (z -8.5) |
| [[LoVo (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0715× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 11.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.91× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIPE-AS1]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TPT1-AS1]] | +0.63 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[L3MBTL1]] | +0.62 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[ANKMY1]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SLC23A3]] | +0.58 | +0.38 / +0.65 | both halves | 7e-05 |  |
| [[LINC02646]] | +0.58 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[TPTEP2-CSNK1E]] | +0.58 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[DEAF1]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MAFG]] | +0.57 | +0.37 / +0.64 | both halves | 9e-05 |  |
| [[ADGRL1-AS1]] | +0.57 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[GATD1-DT]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[RENO1]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDH1]] | -0.64 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[LANCL1]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[DLAT]] | -0.57 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[AMACR]] | -0.56 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[THYN1]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[MDM1]] | -0.54 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[ECHS1]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CAND1]] | -0.52 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[COMMD8]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[DUSP19]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[DLD]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZMYM3]] | -0.52 | -0.40 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.490). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.8, -18.0); signed map (6.6, 10.1). **Vector** length 79.5, 14.9% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.8 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | -0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | +2.3 | -4.8 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.1 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.9 | +3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -10.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.5 | -5.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.4 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | +1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -1.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | exonuclease 3'-5' domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,306,896-137,423,211 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC54932, FLJ20433, mut-7, Nbr |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9H8](https://www.uniprot.org/uniprotkb/Q8N9H8) (Exonuclease mut-7 homolog):

> Possesses 3'-5' exoribonuclease activity. Required for 3'-end trimming of AGO1-bound miRNAs (By similarity).

**Summary**, from NCBI Gene [54932](https://www.ncbi.nlm.nih.gov/gene/54932):

> Predicted to enable 3'-5' exonuclease activity; metal ion binding activity; and nucleic acid binding activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26023) · Entrez [54932](https://www.ncbi.nlm.nih.gov/gene/54932) · UniProt [Q8N9H8](https://www.uniprot.org/uniprotkb/Q8N9H8) · Ensembl [ENSG00000187609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187609)

## Data

Gene col 11929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11929); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11929]; `tensor/DDL_lfc|DDL_z.npy` [11929]; `embed/gene_vectors.npy` [11929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11929 or target_col == 11929). Every well: [[EXD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

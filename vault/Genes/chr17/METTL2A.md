---
symbol: "METTL2A"
type: "gene"
col: 1516
ensembl_id: "ENSG00000087995"
name: "methyltransferase 2A, tRNA N3-cytidine"
location: "17q23.2"
module: 1
arm: "+"
pooled_cpm: 25.36
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# METTL2A

*methyltransferase 2A, tRNA N3-cytidine* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +17.0, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.617× (z -17.0, q 0e+00, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (RKO 0.227×, A498 0.337×, SW480 0.532×, SW1417 0.439×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.161×, HEC-1-A 0.365×, NCI-H23 0.266×, SHP-77 0.258×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.212×, C-33 A 0.269×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.115×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL2B]] (+0.69, fdr 7e-06), [[EIF2B3]] (+0.69, fdr 7e-06), [[RRP7A]] (+0.66, fdr 7e-06); moves opposite to [[GNAS]] (-0.67, fdr 7e-06), [[YPEL5]] (-0.63, fdr 2e-05), [[VAMP1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Pemigatinib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +17.0 | 0e+00 | 39/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +14.6 | 1e-45 | 38/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +13.1 | 4e-37 | 38/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.69×** | +13.1 | 8e-37 | 38/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +10.9 | 1e-25 | 32/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +10.6 | 3e-24 | 32/47 (SW480, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +9.3 | 1e-18 | 31/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +9.1 | 7e-18 | 31/46 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +8.8 | 6e-17 | 29/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +8.7 | 2e-16 | 30/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +8.2 | 2e-14 | 26/48 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.37×** | +7.8 | 2e-13 | 26/46 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +7.7 | 4e-13 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +7.5 | 3e-12 | 23/47 (SW480, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +7.2 | 3e-11 | 26/48 (NCI-H460, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +6.8 | 5e-10 | 23/47 (C-33 A, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.5 | 2e-09 | 19/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +5.9 | 1e-07 | 19/45 (KATO III, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.46×** | +4.9 | 2e-05 | 7/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1516.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (RKO 0.227×, A498 0.337×, SW480 0.532×, SW1417 0.439×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.161×, HEC-1-A 0.365×, NCI-H23 0.266×, SHP-77 0.258×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.212×, C-33 A 0.269×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -17.0 | 0e+00 | 41/48 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.791×** | -5.4 | 2e-05 | 18/40 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.813×** | -5.2 | 4e-05 | 18/44 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.840× | -4.2 | 0.003 | 12/35 (LoVo, C-33 A, …) | all doses, flat | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.877× | -4.2 | 0.003 | 10/48 (C32, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -3.6 | 0.034 | 13/46 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.882× | -3.4 | 0.061 | 8/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.884× | -3.1 | 0.14 | 8/46 (HepG2/C3A, A549, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.4 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -13.7) |
| [[A-427 (line)]] | wt | 31.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 24.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.9) |
| [[HOP62 (line)]] | alt | 17.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.0) |
| [[A498 (line)]] | wt | 20.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.7) |
| [[C-33 A (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 49.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.115× (z -9.7) |
| [[H4 (line)]] | wt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.3) |
| [[KATO III (line)]] | alt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[LoVo (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 31.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.5) |
| [[RKO (line)]] | wt | 31.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -15.7) |
| [[SHP-77 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 27.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.5) |
| [[SW48 (line)]] | wt | 25.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -10.2) |
| [[A-172 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL2B]] | +0.69 | +0.68 / +0.74 | both halves | 7e-06 | same gene group |
| [[EIF2B3]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[RRP7A]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.64 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[DDX55]] | +0.64 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[NSUN4]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 | same gene group |
| [[REXO4]] | +0.64 | +0.58 / +0.70 | both halves | 8e-06 |  |
| [[CIAO1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[MCAT]] | +0.63 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[KRI1]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.63 | +0.48 / +0.68 | both halves | 2e-05 | same gene group; STRING 484 |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.67 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[YPEL5]] | -0.63 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[VAMP1]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PRCP]] | -0.58 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[HIPK1]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[MMP2]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[UPK2]] | -0.55 | -0.17 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[PGRMC1]] | -0.54 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[ITM2B]] | -0.54 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[BTNL12P]] | -0.54 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[LAPTM4A]] | -0.54 | -0.53 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Pemigatinib (drug)]] 5 µM | C | METTL2A's natural level raises the cells' numbers under Pemigatinib 5 µM (protects the cells) | METTL2A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73 | 0.178 over the table, 0.005 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-41.5, -2.1); signed map (2.5, -45.7). **Vector** length 78.3, 14.7% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +6.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -17.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.8 | -5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.8 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 2A, tRNA N3-cytidine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:62,423,875-62,453,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12760, METTL2 |
| Gene groups (HGNC) | 7BS N3-cytosine RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IZ6](https://www.uniprot.org/uniprotkb/Q96IZ6) (tRNA N(3)-cytidine methyltransferase METTL2A):

> S-adenosyl-L-methionine-dependent methyltransferase that mediates N(3)-methylcytidine modification of residue 32 of the tRNA anticodon loop of tRNA(Thr)(UGU) and tRNA(Arg)(CCU). N(3)-methylcytidine methylation by METTL2A requires the N6-threonylcarbamoylation of tRNA (t6A37) by the EKC/KEOPS complex as prerequisite.

**Summary**, from NCBI Gene [339175](https://www.ncbi.nlm.nih.gov/gene/339175):

> Enables tRNA (cytidine-N3)-methyltransferase activity. Involved in tRNA methylation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25755) · Entrez [339175](https://www.ncbi.nlm.nih.gov/gene/339175) · UniProt [Q96IZ6](https://www.uniprot.org/uniprotkb/Q96IZ6) · Ensembl [ENSG00000087995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087995)

## Data

Gene col 1516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1516); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1516]; `tensor/DDL_lfc|DDL_z.npy` [1516]; `embed/gene_vectors.npy` [1516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1516 or target_col == 1516). Every well: [[METTL2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

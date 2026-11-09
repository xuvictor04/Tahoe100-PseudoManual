---
symbol: "SUDS3"
type: "gene"
col: 3266
ensembl_id: "ENSG00000111707"
name: "SIN3A corepressor complex component SDS3"
location: "12q24.23"
module: 25
arm: "+"
pooled_cpm: 62.66
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SUDS3

*SIN3A corepressor complex component SDS3* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.90× (z +16.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.735× (z -8.0, q 5e-13, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GFM2]] (+0.67, fdr 7e-06), [[GPN1]] (+0.66, fdr 7e-06), [[USP5]] (+0.66, fdr 7e-06); moves opposite to [[DMAC1]] (-0.57, fdr 4e-05), [[PPP1R14B-AS1]] (-0.56, fdr 3e-05), [[FOXA2]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.90×** | +16.7 | 0e+00 | 45/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.83×** | +15.7 | 0e+00 | 45/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +15.3 | 0e+00 | 42/49 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +13.1 | 7e-37 | 46/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +10.7 | 1e-24 | 38/43 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +10.0 | 1e-21 | 30/45 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +8.6 | 5e-16 | 33/48 (C32, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +6.9 | 4e-10 | 32/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +5.2 | 1e-05 | 24/48 (LS 180, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 2e-05 | 22/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.21×** | +5.0 | 3e-05 | 24/48 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.43×** | +4.8 | 7e-05 | 22/47 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.6 | 2e-04 | 19/44 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.12× | +4.1 | 0.002 | 16/48 (AsPC-1, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.9 | 0.004 | 12/48 (HEC-1-A, HT-29, …) | rises with dose | position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | 1.17× | +3.5 | 0.016 | 11/48 (COLO 205, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.023 | 13/49 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mozavaptan (drug)]] 0.5 µM |  | 1.12× | +2.9 | 0.097 | 8/48 (NCI-H460, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -8.0 | 5e-13 | 36/48 (LoVo, COLO 205, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -7.0 | 5e-10 | 33/48 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.759×** | -6.3 | 6e-08 | 26/48 (COLO 205, LoVo, …) | two highest doses | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -6.2 | 9e-08 | 18/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -5.5 | 4e-06 | 26/50 (Panc 03.27, SNU-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.870× | -5.2 | 2e-05 | 21/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.831×** | -4.8 | 1e-04 | 24/48 (CFPAC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -4.7 | 2e-04 | 18/49 (A498, SHP-77, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.834× | -4.2 | 0.002 | 20/47 (C-33 A, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | 0.861× | -3.9 | 0.005 | 22/48 (LS 180, SW480, …) | top dose only |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.865× | -3.8 | 0.007 | 7/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.865× | -3.8 | 0.007 | 10/49 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | 0.871× | -3.4 | 0.034 | 14/47 (NCI-H460, AN3 CA, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.881× | -3.3 | 0.034 | 5/48 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.886× | -3.2 | 0.052 | 15/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brimonidine (drug)]] 0.5 µM |  | 0.886× | -3.2 | 0.052 | 10/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.800×** | -3.1 | 0.075 | 10/48 (HT-29, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 50.0 | 6 (3 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.09× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.630× (z -8.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[PANC-1 (line)]] | alt | 69.7 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +16.9) | — |
| [[COLO 205 (line)]] | alt | 101 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -9.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HEC-1-A (line)]] | alt | 63.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.39× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.98× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 67.6 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.02× (z +10.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -10.9) |
| [[A-427 (line)]] | wt | 60.5 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.46× (z +10.2) | — |
| [[C32 (line)]] | wt | 50.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +9.3) | — |
| [[J82 (line)]] | alt | 53.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 60.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.85× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 51.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.14× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 57.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +10.3) | — |
| [[SW48 (line)]] | wt | 59.0 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.30× (z +9.2) | — |
| [[A-172 (line)]] | wt | 42.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 48.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -8.7) |
| [[LoVo (line)]] | wt | 78.4 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.96× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -10.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A498 (line)]] | wt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 60.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.297× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[CHP-212 (line)]] | wt | 59.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0791× (z -12.9) |
| [[H4 (line)]] | wt | 50.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 55.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 49.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[LS 180 (line)]] | wt | 62.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 50.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 54.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -8.7) |
| [[A549 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 75.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFM2]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GPN1]] | +0.66 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[USP5]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 | pathway: Deubiquitination |
| [[OPA1]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[RTF2]] | +0.64 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[EXOC3]] | +0.64 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[AGO1]] | +0.63 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[BABAM1]] | +0.63 | +0.74 / +0.57 | both halves | 9e-06 | pathway: Deubiquitination |
| [[APOOL]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[UBFD1]] | +0.62 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[AP3M1]] | +0.62 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[CRYZ]] | +0.61 | +0.56 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMAC1]] | -0.57 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[PPP1R14B-AS1]] | -0.56 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[FOXA2]] | -0.55 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[PFN1]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[S100A6]] | -0.54 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[CHKB-DT]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[POLR2L]] | -0.53 | -0.56 / -0.65 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[POLR1H]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 | pathway: Epigenetic regulation of gene expression |
| [[SERTAD1]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[GPX1]] | -0.53 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PHLDA2]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[RBX1]] | -0.52 | -0.39 / -0.49 | both halves | 6e-05 | pathway: Potential therapeutics for SARS |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.9, -13.1); signed map (-29.9, -28.4). **Vector** length 120, 31.0% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +12.1 | +16.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.2 | +15.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.8 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +8.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.9 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.5 | -6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | SIN3A corepressor complex component SDS3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:118,376,555-118,418,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDS3, FLJ00052, SAP45 |
| Gene groups (HGNC) | SIN3 histone deacetylase complex subunits |
| Reactome | 11 pathways, smallest: HDACs deacetylate histones; NoRC negatively regulates rRNA expression; Negative epigenetic regulation of rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7L9](https://www.uniprot.org/uniprotkb/Q9H7L9) (Sin3 histone deacetylase corepressor complex component SDS3):

> Regulatory protein which represses transcription and augments histone deacetylase activity of HDAC1. May have a potential role in tumor suppressor pathways through regulation of apoptosis. May function in the assembly and/or enzymatic activity of the mSin3A corepressor complex or in mediating interactions between the complex and other regulatory complexes.

**Summary**, from NCBI Gene [64426](https://www.ncbi.nlm.nih.gov/gene/64426):

> SDS3 is a subunit of the histone deacetylase (see HDAC1; MIM 601241)-dependent SIN3A (MIM 607776) corepressor complex (Fleischer et al., 2003 [PubMed 12724404]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29545) · Entrez [64426](https://www.ncbi.nlm.nih.gov/gene/64426) · UniProt [Q9H7L9](https://www.uniprot.org/uniprotkb/Q9H7L9) · Ensembl [ENSG00000111707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111707)

## Data

Gene col 3266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3266); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3266]; `tensor/DDL_lfc|DDL_z.npy` [3266]; `embed/gene_vectors.npy` [3266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3266 or target_col == 3266). Every well: [[SUDS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUDS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

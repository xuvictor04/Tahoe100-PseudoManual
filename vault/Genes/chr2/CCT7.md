---
symbol: "CCT7"
type: "gene"
col: 5732
ensembl_id: "ENSG00000135624"
name: "chaperonin containing TCP1 subunit 7"
location: "2p13.2"
module: 4
arm: "+"
pooled_cpm: 66.72
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CCT7

*chaperonin containing TCP1 subunit 7* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.89× (z +19.4, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.78× (z +8.2, q 2e-14, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.212×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.337×; ⚠ cell-cycle shift, explains ~40% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT5]] (+0.83, fdr 7e-06), [[CCT3]] (+0.75, fdr 7e-06), [[FKBP4]] (+0.75, fdr 7e-06); moves opposite to [[GABARAPL2]] (-0.72, fdr 7e-06), [[INAFM1]] (-0.71, fdr 7e-06), [[VEGFB]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TNNI3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.89×** | +19.4 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.78×** | +18.3 | 0e+00 | 42/43 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +12.2 | 4e-32 | 42/45 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +8.2 | 2e-14 | 41/48 (PANC-1, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.72×** | +7.7 | 1e-12 | 44/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +7.4 | 1e-11 | 43/48 (SW1417, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +7.1 | 9e-11 | 42/48 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +6.8 | 1e-09 | 44/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.56×** | +6.1 | 7e-08 | 31/48 (NCI-H1792, A549, …) | two highest doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +6.1 | 7e-08 | 30/48 (A-172, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.47×** | +5.5 | 2e-06 | 36/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.47×** | +5.3 | 5e-06 | 30/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +5.1 | 1e-05 | 31/48 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.8 | 6e-05 | 25/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.8 | 7e-05 | 30/48 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.3 | 5e-04 | 35/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +4.3 | 5e-04 | 34/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 8e-04 | 33/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.029 | 20/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.032 | 20/48 (NCI-H23, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Erdafitinib (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.032 | 16/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.059 | 18/48 (HS-578T, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.059 | 17/47 (HOP62, H4, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5732.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.212×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.337×; ⚠ cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 0.779× | -3.5 | 0.27 | 24/47 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.764× | -3.3 | 0.27 | 19/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.659× | -3.1 | 0.32 | 20/48 (NCI-H23, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 75.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 54.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 81.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 86.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.74× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 55.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 50.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 72.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 57.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 42.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.48× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 86.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 74.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 72.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-423 (line)]] | alt | 42.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.44× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 95.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 58.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 34.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 39.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[H4 (line)]] | wt | 61.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 83.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Hs 766T (line)]] | wt | 39.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HT-29 (line)]] | alt | 51.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 42.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +11.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 80.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 61.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 41.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 52.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 51.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SHP-77 (line)]] | alt | 76.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 68.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.39× (z +15.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 45.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -11.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HEC-1-A (line)]] | alt | 60.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 49.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 64.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -16.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 75.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 97.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | +0.83 | +0.83 / +0.81 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CCT3]] | +0.75 | +0.80 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[FKBP4]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[CCT6A]] | +0.72 | +0.80 / +0.61 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[PDAP1]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.71 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ATIC]] | +0.71 | +0.72 / +0.71 | both halves | 7e-06 | STRING 881 |
| [[DARS2]] | +0.71 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CCT2]] | +0.70 | +0.76 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSME3]] | +0.70 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[PTPN11]] | +0.69 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[PSMC5]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 | STRING 765 |

## Genes that move opposite

*45 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAPL2]] | -0.72 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.71 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[VEGFB]] | -0.70 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.69 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.69 | -0.67 / -0.70 | both halves | 7e-06 |  |
| [[SIRT2]] | -0.69 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[SNHG9]] | -0.68 | -0.56 / -0.72 | both halves | 1e-05 |  |
| [[MZT2B]] | -0.67 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[CDKN2D]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.66 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[BRI3]] | -0.65 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.64 | -0.59 / -0.69 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNNI3]] | B | TNNI3 activity raises CCT7's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without TNNI3 | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[AFAP1-AS1]] | B | AFAP1-AS1 activity lowers CCT7's level | lines that do not express AFAP1-AS1 (33) vs lines expressing it (17) | 1.26× higher at baseline in the lines without AFAP1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: AGR2, GABRP, LINC01610 |
| [[YPEL3]] | B | YPEL3 activity lowers CCT7's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.38× higher at baseline in the lines without YPEL3 | 0.092 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.7, -31.7); signed map (-12.3, -43.7). **Vector** length 94.9, 30.3% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +0.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.8 | -0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | +0.1 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.5 | +0.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.4 | +0.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:73,233,420-73,253,021 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ccth, Nip7-1 |
| Gene groups (HGNC) | Chaperonin containing TCP1 |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: Folding of actin by CCT/TriC; Formation of tubulin folding intermediates by CCT/TriC; RHOBTB1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99832](https://www.uniprot.org/uniprotkb/Q99832) (T-complex protein 1 subunit eta):

> Component of the chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of actin, tubulin and other proteins upon ATP hydrolysis. The TRiC complex mediates the folding of WRAP53/TCAB1, thereby regulating telomere maintenance.

**Summary**, from NCBI Gene [10574](https://www.ncbi.nlm.nih.gov/gene/10574):

> This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including actin and tubulin. Alternative splicing results in multiple transcript variants. Related pseudogenes …

**Accessions** — [HGNC:1622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1622) · Entrez [10574](https://www.ncbi.nlm.nih.gov/gene/10574) · UniProt [Q99832](https://www.uniprot.org/uniprotkb/Q99832) · Ensembl [ENSG00000135624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135624)

## Data

Gene col 5732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5732); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5732]; `tensor/DDL_lfc|DDL_z.npy` [5732]; `embed/gene_vectors.npy` [5732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5732 or target_col == 5732). Every well: [[CCT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

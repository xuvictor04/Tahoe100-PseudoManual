---
symbol: "KARS1"
type: "gene"
col: 786
ensembl_id: "ENSG00000065427"
name: "lysyl-tRNA synthetase 1"
location: "16q23.1"
module: 4
arm: "+"
pooled_cpm: 65.25
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# KARS1

*lysyl-tRNA synthetase 1* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +19.0, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +13.9, q 1e-41, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.350×, C-33 A 0.504×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCF2]] (+0.70, fdr 7e-06), [[CCT7]] (+0.68, fdr 7e-06), [[EIF2S1]] (+0.67, fdr 7e-06); moves opposite to [[GABARAPL2]] (-0.64, fdr 7e-06, ⚠ same locus), [[PHF1]] (-0.63, fdr 1e-05), [[C19orf81]] (-0.60, fdr 2e-05), [[IER5]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.75×** | +19.0 | 0e+00 | 48/49 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +16.9 | 0e+00 | 41/43 (NCI-H1792, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +13.9 | 1e-41 | 44/48 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +11.5 | 2e-28 | 40/45 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.8 | 5e-13 | 36/48 (HT-29, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.8 | 5e-13 | 37/48 (A-172, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.5 | 6e-12 | 38/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.3 | 2e-11 | 38/50 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +7.2 | 3e-11 | 39/49 (COLO 205, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +6.9 | 2e-10 | 41/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +5.9 | 2e-07 | 32/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.38×** | +5.8 | 3e-07 | 29/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.36×** | +5.8 | 3e-07 | 34/47 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.4 | 3e-06 | 29/48 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.32×** | +5.2 | 6e-06 | 26/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.9 | 3e-05 | 32/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.9 | 3e-05 | 25/48 (SW480, Hs 766T, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +4.7 | 8e-05 | 33/48 (NCI-H460, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +4.7 | 9e-05 | 31/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 2e-04 | 23/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.001 | 27/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.004 | 21/48 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 786.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.350×, C-33 A 0.504×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 5 µM |  | 0.884× | -3.4 | 0.29 | 12/48 (SW480, SW48, …) | rises with dose | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.886× | -3.3 | 0.29 | 13/48 (A-427, NCI-H2030, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 90.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 53.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 60.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 99.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 50.5 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.2) | — |
| [[A-172 (line)]] | wt | 52.2 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.86× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 56.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 58.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 69.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 43.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.8) | — |
| [[KATO III (line)]] | alt | 70.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-427 (line)]] | wt | 76.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 80.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 77.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[CFPAC-1 (line)]] | alt | 45.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +11.2) | — |
| [[J82 (line)]] | alt | 60.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.7) | — |
| [[LoVo (line)]] | wt | 57.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[LOX-IMVI (line)]] | wt | 65.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 56.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H2347 (line)]] | alt | 37.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 50.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[Panc 03.27 (line)]] | alt | 50.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 54.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SHP-77 (line)]] | alt | 88.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 70.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +10.3) | — |
| [[SW480 (line)]] | alt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[AN3 CA (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 42.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 79.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 52.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[LS 180 (line)]] | wt | 50.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H23 (line)]] | alt | 89.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +11.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 74.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SW 900 (line)]] | alt | 36.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[BT-474 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCF2]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 | STRING 425 |
| [[CCT7]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 581 |
| [[EIF2S1]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 605 |
| [[XRCC6]] | +0.66 | +0.59 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[MAPKAPK5]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[EIF3D]] | +0.63 | +0.70 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 776 |
| [[CCT8]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 | STRING 596 |
| [[POLDIP2]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SELENOF]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LRPPRC]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[ATIC]] | +0.61 | +0.69 / +0.57 | both halves | 1e-05 | STRING 506 |
| [[PAICS]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAPL2]] | -0.64 | -0.60 / -0.60 | both halves | 7e-06 | ⚠ same locus (49.6 kb: neighbours can correlate without regulation) |
| [[PHF1]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[C19orf81]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[IER5]] | -0.59 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[KRT10]] ⚠ | -0.58 | -0.42 / -0.59 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDKN2D]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[C4orf48]] | -0.58 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.57 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[SIGIRR]] | -0.57 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TMEM191A-1]] | -0.56 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[COX17]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SIRT2]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[INAFM1]] | -0.55 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[CDKN1C]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KARS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C19orf81]] | B | C19orf81 activity raises KARS1's level | lines that do not express C19orf81 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without C19orf81 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC02269, LMX1B, CRMP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.0, -32.1); signed map (-12.1, -43.4). **Vector** length 83.3, 21.7% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +13.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | -2.6 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.3 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | -2.3 | +2.8 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | -2.1 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -0.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.0 | -1.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | lysyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:75,627,474-75,648,643 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KARS2; previously DFNB89, KARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Hallmark sets | XENOBIOTIC_METABOLISM, MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: Mitochondrial tRNA aminoacylation; Cytosolic tRNA aminoacylation; tRNA Aminoacylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15046](https://www.uniprot.org/uniprotkb/Q15046) (Lysine--tRNA ligase):

> Catalyzes the specific attachment of an amino acid to its cognate tRNA in a 2 step reaction: the amino acid (AA) is first activated by ATP to form AA-AMP and then transferred to the acceptor end of the tRNA. When secreted, acts as a signaling molecule that induces immune response through the activation of monocyte/macrophages. Catalyzes the synthesis of the signaling molecule diadenosine tetraphosphate (Ap4A), and thereby mediates disruption of the complex between HINT1 and MITF and the …

**Summary**, from NCBI Gene [3735](https://www.ncbi.nlm.nih.gov/gene/3735):

> Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Lysyl-tRNA synthetase is a homodimer localized to the cytoplasm which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6215) · Entrez [3735](https://www.ncbi.nlm.nih.gov/gene/3735) · UniProt [Q15046](https://www.uniprot.org/uniprotkb/Q15046) · Ensembl [ENSG00000065427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065427)

## Data

Gene col 786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 786); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 786]; `tensor/DDL_lfc|DDL_z.npy` [786]; `embed/gene_vectors.npy` [786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 786 or target_col == 786). Every well: [[KARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

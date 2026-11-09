---
symbol: "NEDD8"
type: "gene"
col: 4987
ensembl_id: "ENSG00000129559"
name: "NEDD8 ubiquitin like modifier"
location: "14q12"
module: 48
arm: "+"
pooled_cpm: 48.09
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# NEDD8

*NEDD8 ubiquitin like modifier* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.89× (z +11.6, q 3e-28, up in 47 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +5.3, q 2e-05, up in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H460 5.34×, HOP62 5.40×, NCI-H1792 6.22×, SW480 4.37×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 5.29×, LOX-IMVI 5.98×, A549 5.10×, PANC-1 4.49×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.567× (z -6.0, q 1e-06, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (J82 0.326×, Panc 03.27 0.290×, AsPC-1 0.286×, BT-474 0.285×, …); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBL5]] (+0.83, fdr 7e-06), [[COX6C]] (+0.79, fdr 7e-06), [[ATP5PF]] (+0.78, fdr 7e-06); moves opposite to [[PEX1]] (-0.67, fdr 1e-05), [[SRSF3]] (-0.64, fdr 1e-05), [[NBN]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4987.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H460 5.34×, HOP62 5.40×, NCI-H1792 6.22×, SW480 4.37×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 5.29×, LOX-IMVI 5.98×, A549 5.10×, PANC-1 4.49×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.89×** | +11.6 | 3e-28 | 47/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.56×** | +10.4 | 8e-23 | 40/42 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.51×** | +7.2 | 8e-11 | 39/44 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.3 | 2e-05 | 42/48 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.70×** | +4.5 | 8e-04 | 37/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.60×** | +4.0 | 0.006 | 34/47 (PANC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.52×** | +3.4 | 0.048 | 28/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.2 | 0.091 | 27/47 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4987.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (J82 0.326×, Panc 03.27 0.290×, AsPC-1 0.286×, BT-474 0.285×, …); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.567×** | -6.0 | 1e-06 | 40/48 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -4.7 | 7e-04 | 39/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.667× | -3.5 | 0.10 | 38/48 (HOP62, A498, …) | all doses, flat | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.670× | -3.2 | 0.23 | 29/48 (LOX-IMVI, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 47.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.3) |
| [[A-172 (line)]] | wt | 39.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 44.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 45.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.0) |
| [[C32 (line)]] | wt | 26.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 69.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 41.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[J82 (line)]] | alt | 63.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.5) |
| [[LoVo (line)]] | wt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 42.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.98× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 37.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.22× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 66.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 38.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Panc 03.27 (line)]] | alt | 63.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.3) |
| [[PANC-1 (line)]] | alt | 40.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 38.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[BT-474 (line)]] | alt | 59.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.9) |
| [[COLO 205 (line)]] | alt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -8.6) |
| [[HCT15 (line)]] | alt | 51.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 87.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 52.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBL5]] | +0.83 | +0.76 / +0.83 | both halves | 7e-06 | STRING 943 |
| [[COX6C]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[ATP5PF]] | +0.78 | +0.69 / +0.82 | both halves | 7e-06 | STRING 483 |
| [[UQCRQ]] ⚠ | +0.77 | +0.71 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATOX1]] | +0.75 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.73 | +0.63 / +0.83 | both halves | 7e-06 |  |
| [[COX6A1]] | +0.72 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[SPCS1]] | +0.71 | +0.57 / +0.76 | both halves | 1e-05 |  |
| [[NDUFA4]] | +0.69 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[UQCRH]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[HSBP1]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[SSR4]] | +0.67 | +0.64 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX1]] | -0.67 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.64 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[NBN]] | -0.61 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SRSF6]] | -0.61 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[ZXDA]] | -0.59 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[C12orf29]] | -0.59 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.58 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ZXDB]] | -0.58 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ZNF181]] | -0.57 | -0.62 / -0.22 | both halves | 6e-04 |  |
| [[CCT6P3]] | -0.57 | -0.67 / -0.26 | both halves | 4e-04 |  |
| [[POGLUT1]] | -0.56 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ZNF606]] | -0.56 | -0.48 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.5, -22.5); signed map (-35.4, 9.8). **Vector** length 56.7, 16.8% of its response variance represented; |z| ≥ 3 in 561 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.56 to 31); *Respiratory electron transport* (reactome, mean cos +0.54 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.57 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +3.3 | +4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.0 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.8 | -0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.4 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.2 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.9 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.4 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | NEDD8 ubiquitin like modifier |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,216,857-24,232,367 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Nedd-8 |
| Reactome | 12 pathways, smallest: TGF-beta receptor signaling activates SMADs; Iron uptake and transport; UCH proteinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15843](https://www.uniprot.org/uniprotkb/Q15843) (Ubiquitin-like protein NEDD8):

> Ubiquitin-like protein which plays an important role in cell cycle control and embryogenesis via its conjugation to a limited number of cellular proteins, such as cullins or p53/TP53. Attachment of NEDD8 to cullins is critical for the recruitment of E2 to the cullin-RING-based E3 ubiquitin-protein ligase complex, thus facilitating polyubiquitination and proteasomal degradation of cyclins and other regulatory proteins. The E3 ubiquitin-protein ligase activity is regulated by the COP9 signalosome …

**Summary**, from NCBI Gene [4738](https://www.ncbi.nlm.nih.gov/gene/4738):

> Enables ubiquitin protein ligase binding activity. Acts upstream of or within protein neddylation. Located in nucleoplasm. Biomarker of Parkinson's disease; alcohol-associated liver disease; and malignant astrocytoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7732) · Entrez [4738](https://www.ncbi.nlm.nih.gov/gene/4738) · UniProt [Q15843](https://www.uniprot.org/uniprotkb/Q15843) · Ensembl [ENSG00000129559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129559)

## Data

Gene col 4987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4987); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4987]; `tensor/DDL_lfc|DDL_z.npy` [4987]; `embed/gene_vectors.npy` [4987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4987 or target_col == 4987). Every well: [[NEDD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEDD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

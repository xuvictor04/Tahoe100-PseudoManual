---
symbol: "RCN2"
type: "gene"
col: 3956
ensembl_id: "ENSG00000117906"
name: "reticulocalbin 2"
location: "15q24.3"
module: 11
arm: "-"
pooled_cpm: 40.48
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RCN2

*reticulocalbin 2* — 15q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.76× (z +18.2, q 0e+00, up in 45 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +10.3, q 1e-22, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.681× (z -5.3, q 5e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGS]] (+0.72, fdr 7e-06), [[SUMF2]] (+0.70, fdr 7e-06), [[RPA1]] (+0.68, fdr 7e-06); moves opposite to [[NSRP1]] (-0.73, fdr 7e-06), [[GLRX2]] (-0.69, fdr 7e-06), [[ZNF829]] (-0.68, fdr 7e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.76×** | +18.2 | 0e+00 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.36×** | +16.0 | 0e+00 | 40/41 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.55×** | +11.9 | 3e-30 | 41/45 (A-172, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +10.3 | 1e-22 | 39/48 (A549, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +7.6 | 3e-12 | 40/47 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.68×** | +7.1 | 9e-11 | 40/48 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.59×** | +6.4 | 1e-08 | 38/48 (LoVo, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.57×** | +6.2 | 4e-08 | 35/47 (KATO III, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.53×** | +5.9 | 3e-07 | 37/48 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.52×** | +5.7 | 6e-07 | 35/48 (KATO III, H4, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.46×** | +5.0 | 3e-05 | 28/48 (A-172, C32, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.3 | 7e-04 | 21/35 (A-172, C32, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.35×** | +4.1 | 0.002 | 30/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.36×** | +4.0 | 0.002 | 26/48 (SNU-423, A-172, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.013 | 23/48 (HT-29, HEC-1-A, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.084 | 18/47 (HCT15, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.681×** | -5.3 | 5e-05 | 29/48 (AN3 CA, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -4.8 | 5e-04 | 31/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.716×** | -4.6 | 7e-04 | 31/48 (SNU-1, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.771×** | -3.5 | 0.072 | 22/48 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.2 | 0.14 | 2/49 (CHP-212, SW 1088) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.728× | -3.1 | 0.17 | 14/48 (HOP62, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.1 | 0.18 | 15/48 (A-427, J82, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 32.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +11.8) | — |
| [[A-172 (line)]] | wt | 53.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.4) | — |
| [[A-427 (line)]] | wt | 42.4 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 31.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 59.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 36.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 42.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Harringtonine (drug)]] 0.5 µM 0.431× (z -8.6) |
| [[A549 (line)]] | wt | 43.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +12.1) | — |
| [[C32 (line)]] | wt | 40.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 39.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 58.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 31.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 50.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 45.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 49.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 33.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 26.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.2) | — |
| [[A498 (line)]] | wt | 21.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 57.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 43.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 32.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 42.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 46.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 69.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.2) |
| [[HCT15 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 45.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.120× (z -9.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-1 (line)]] | wt | 54.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.304× (z -9.2) |
| [[SW 1271 (line)]] | alt | 77.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0963× (z -9.6) |
| [[SW1417 (line)]] | alt | 51.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGS]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SUMF2]] | +0.70 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[RPA1]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[GINM1]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[TMED4]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[MLEC]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[LAPTM4A]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CD46]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 | STRING 433 |
| [[PCYOX1]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SETD3]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NUDT21]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | -0.73 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[GLRX2]] | -0.69 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[ZNF829]] | -0.68 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[DNTTIP2]] | -0.64 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[UTP3]] | -0.64 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SURF6]] | -0.63 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[RPL7L1]] | -0.62 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[ZNF286B]] | -0.62 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PDRG1]] | -0.61 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[FADD]] | -0.61 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[OSGIN1]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.8, -19.3); signed map (-50.1, -6.9). **Vector** length 90.2, 24.3% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.0 | +5.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.6 | +4.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.2 | +0.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.2 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -10.1 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.0 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.1 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | reticulocalbin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.3 — chr15:76,931,738-76,954,393 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERC-55, E6BP, ERC55, TCBP49 |
| Gene groups (HGNC) | CREC family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14257](https://www.uniprot.org/uniprotkb/Q14257) (Reticulocalbin-2):

> Not known. Binds calcium.

**Summary**, from NCBI Gene [5955](https://www.ncbi.nlm.nih.gov/gene/5955):

> The protein encoded by this gene is a calcium-binding protein located in the lumen of the ER. The protein contains six conserved regions with similarity to a high affinity Ca(+2)-binding motif, the EF-hand. This gene maps to the same region as type 4 Bardet-Biedl syndrome, suggesting a possible causative role for this gene in the disorder. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:9935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9935) · Entrez [5955](https://www.ncbi.nlm.nih.gov/gene/5955) · UniProt [Q14257](https://www.uniprot.org/uniprotkb/Q14257) · Ensembl [ENSG00000117906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117906)

## Data

Gene col 3956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3956); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3956]; `tensor/DDL_lfc|DDL_z.npy` [3956]; `embed/gene_vectors.npy` [3956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3956 or target_col == 3956). Every well: [[RCN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

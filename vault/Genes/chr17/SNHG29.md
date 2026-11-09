---
symbol: "SNHG29"
type: "gene"
col: 10555
ensembl_id: "ENSG00000175061"
name: "small nucleolar RNA host gene 29"
location: "17p11.2"
module: 43
arm: "+"
pooled_cpm: 137.58
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# SNHG29

*small nucleolar RNA host gene 29* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.88× (z +15.1, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +10.7, q 1e-24, up in 44 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.466×, SNU-1 0.468×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SNU-1 0.383×, A-427 0.429×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.276×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A6]] (+0.72, fdr 7e-06), [[RPL14]] (+0.71, fdr 7e-06), [[RPLP0]] (+0.70, fdr 7e-06); moves opposite to [[HMGB1P5]] (-0.51, fdr 3e-05, ⚠ HMGB1P5 in the vector space only through flagged drug-doses), [[DNMT1]] (-0.51, fdr 2e-05), [[EXOSC9]] (-0.51, fdr 4e-05), [[ABCF1]] (-0.50, fdr 7e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +15.1 | 0e+00 | 49/49 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +11.0 | 1e-25 | 40/44 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +10.7 | 1e-24 | 44/49 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +8.1 | 7e-14 | 42/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +7.9 | 3e-13 | 42/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +7.4 | 1e-11 | 41/50 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.9 | 3e-07 | 39/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.01×** | +5.2 | 1e-05 | 45/48 (KATO III, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.8 | 8e-05 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.7 | 2e-04 | 35/47 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 2e-04 | 36/48 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +4.5 | 3e-04 | 30/48 (KATO III, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +4.4 | 6e-04 | 31/48 (COLO 205, KATO III, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.3 | 8e-04 | 32/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.001 | 37/48 (A-172, SHP-77, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.002 | 36/48 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.009 | 33/48 (SW480, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.027 | 26/48 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.032 | 27/48 (NCI-H23, HS-578T, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.043 | 22/47 (A-427, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.046 | 27/49 (PANC-1, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.1 | 0.048 | 16/48 (A498, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10555.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.466×, SNU-1 0.468×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SNU-1 0.383×, A-427 0.429×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.276×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -3.0 | 0.51 | 21/48 (RKO, SNU-1, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.802× | -3.0 | 0.51 | 26/47 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.812× | -3.0 | 0.51 | 20/48 (COLO 205, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 68.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +11.6) | — |
| [[A-172 (line)]] | wt | 80.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 154 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.5) | — |
| [[KATO III (line)]] | alt | 143 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 2.17× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 71.8 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +16.2) | — |
| [[SNU-1 (line)]] | wt | 330 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -12.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 118 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +14.3) | — |
| [[C32 (line)]] | wt | 71.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 89.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 157 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 161 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.6) | — |
| [[LoVo (line)]] | wt | 351 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 44.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 67.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 274 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +12.0) | — |
| [[SW480 (line)]] | alt | 213 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.7) | — |
| [[A-427 (line)]] | wt | 129 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 154 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 62.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.9) | — |
| [[HCT15 (line)]] | alt | 144 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 123 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 176 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 87.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 237 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +12.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 132 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +9.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 126 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 93.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 87.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 69.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 218 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 178 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 97.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 98.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +11.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 77.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 277 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 215 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A6]] | +0.72 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[RPL14]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[RPLP0]] | +0.70 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[RPS4X]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[EEF1G]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[RPL27A]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[RPL39]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[EEF1B2]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[POLR1D]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[RACK1]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[PABPC1]] | +0.65 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[RPL29]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGB1P5]] ⚠ | -0.51 | -0.51 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DNMT1]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[EXOSC9]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ABCF1]] | -0.50 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[THSD8]] ⚠ | -0.49 | -0.34 / -0.43 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF107]] | -0.48 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[DDX52]] | -0.48 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[KIF20B]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[GMNN]] | -0.47 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[HMGN2P5]] | -0.46 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[SMC1A]] | -0.46 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[CEP295]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.4, -30.5); signed map (-61.1, -7.3). **Vector** length 105, 35.0% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.50 to 34).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +3.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.3 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | +0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.6 | +0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.6 | +0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +3.5 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.3 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.8 | +0.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.6 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 29 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p11.2 — chr17:16,438,767-16,480,249 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ACIL, MGC40157; previously C17orf45, NCRNA00188, C17orf76-AS1, FAM211A-AS1, LRRC75A-AS1 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [125144](https://www.ncbi.nlm.nih.gov/gene/125144):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28619) · Entrez [125144](https://www.ncbi.nlm.nih.gov/gene/125144) · Ensembl [ENSG00000175061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175061)

## Data

Gene col 10555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10555); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10555]; `tensor/DDL_lfc|DDL_z.npy` [10555]; `embed/gene_vectors.npy` [10555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10555 or target_col == 10555). Every well: [[SNHG29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

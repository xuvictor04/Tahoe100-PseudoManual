---
symbol: "SSRP1"
type: "gene"
col: 7343
ensembl_id: "ENSG00000149136"
name: "structure specific recognition protein 1"
location: "11q12.1"
module: 6
arm: "+"
pooled_cpm: 88.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SSRP1

*structure specific recognition protein 1* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.83× (z +19.3, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.41× (z +4.1, q 0.004, up in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (LoVo 7.56×, PANC-1 5.01×, NCI-H460 6.49×, Panc 03.27 5.72×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 7.02×, PANC-1 4.81×, J82 4.68×, LoVo 6.10×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.700× (z -6.2, q 4e-07, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (LS 180 0.280×, LoVo 0.397×, C32 0.378×, MIA PaCa-2 0.397×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HT-29 0.497×, NCI-H23 0.513×, A-427 0.535×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0857×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPR]] (+0.71, fdr 7e-06), [[TUBGCP3]] (+0.67, fdr 7e-06), [[CDCA7L]] (+0.66, fdr 1e-05); moves opposite to [[PCF11-AS1]] (-0.65, fdr 1e-05), [[ULBP2]] (-0.63, fdr 1e-05), [[CCDC142]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7343.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (LoVo 7.56×, PANC-1 5.01×, NCI-H460 6.49×, Panc 03.27 5.72×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 7.02×, PANC-1 4.81×, J82 4.68×, LoVo 6.10×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.83×** | +19.3 | 0e+00 | 49/49 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.74×** | +18.4 | 0e+00 | 43/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +12.3 | 1e-32 | 44/45 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.57×** | +5.5 | 4e-06 | 42/48 (HT-29, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.59×** | +5.5 | 4e-06 | 40/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.004 | 28/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.0 | 0.005 | 30/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 5 µM |  | 1.20× | +3.2 | 0.10 | 22/48 (HT-29, HCT15, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | 1.62× | +3.1 | 0.12 | 26/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.15 | 25/47 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7343.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (LS 180 0.280×, LoVo 0.397×, C32 0.378×, MIA PaCa-2 0.397×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HT-29 0.497×, NCI-H23 0.513×, A-427 0.535×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0857×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -6.2 | 4e-07 | 31/48 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.801×** | -3.8 | 0.037 | 27/48 (HT-29, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.771× | -3.2 | 0.19 | 29/48 (AsPC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.765× | -3.2 | 0.19 | 27/47 (HS-578T, A549, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.773× | -3.1 | 0.19 | 27/47 (A-172, SK-MEL-2, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 102 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +15.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +14.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.4) |
| [[C32 (line)]] | wt | 81.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +12.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.3) |
| [[Hs 766T (line)]] | wt | 68.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.05× (z +14.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -8.9) |
| [[KATO III (line)]] | alt | 88.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +15.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.5) |
| [[LoVo (line)]] | wt | 73.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +18.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.8) |
| [[LS 180 (line)]] | wt | 77.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +13.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 44.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 8.31× (z +15.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 57.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.02× (z +17.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.4) |
| [[SNU-423 (line)]] | alt | 83.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.56× (z +15.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 61.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +15.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 146 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -8.5) |
| [[A498 (line)]] | wt | 69.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +14.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 111 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.70× (z +14.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 117 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +11.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 80.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 103 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +16.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 78.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +15.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 88.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +14.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 126 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +16.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 107 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +14.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 91.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +16.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +17.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 76.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 79.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +11.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.275× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 52.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 131 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +16.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 110 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0857× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 32.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.32× (z +13.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 72.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +12.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 66.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +14.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +16.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 124 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 95.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 122 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +8.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.0) |
| [[SHP-77 (line)]] | alt | 74.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 116 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.82× (z +12.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 56.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +10.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPR]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[TUBGCP3]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CDCA7L]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PRKDC]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 583 |
| [[MTHFD1]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[RBM17]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers |
| [[NONO]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 | STRING 449 |
| [[CDK5RAP2]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ATP5F1A]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SSX2IP]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PDHA1]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[LMNB2]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCF11-AS1]] | -0.65 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ULBP2]] | -0.63 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[CCDC142]] | -0.62 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RNASEK]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[S100A13]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ORMDL2]] | -0.58 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[SELENOK]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[HIC2]] | -0.56 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[BBIP1]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[CLDN18]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[MAFG]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-28.9, -36.5); signed map (-18.5, -45.2). **Vector** length 83.4, 27.5% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.3 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.8 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | +1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.3 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | structure specific recognition protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,325,986-57,335,892 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FACT80 |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS |
| Reactome | 28 pathways, smallest: Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery; HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08945](https://www.uniprot.org/uniprotkb/Q08945) (FACT complex subunit SSRP1):

> Component of the FACT complex, a general chromatin factor that acts to reorganize nucleosomes. The FACT complex is involved in multiple processes that require DNA as a template such as mRNA elongation, DNA replication and DNA repair. During transcription elongation the FACT complex acts as a histone chaperone that both destabilizes and restores nucleosomal structure. It facilitates the passage of RNA polymerase II and transcription by promoting the dissociation of one histone H2A-H2B dimer from …

**Summary**, from NCBI Gene [6749](https://www.ncbi.nlm.nih.gov/gene/6749):

> The protein encoded by this gene is a subunit of a heterodimer that, along with SUPT16H, forms chromatin transcriptional elongation factor FACT. FACT interacts specifically with histones H2A/H2B to effect nucleosome disassembly and transcription elongation. FACT and cisplatin-damaged DNA may be crucial to the anticancer mechanism of cisplatin. This encoded protein contains a high mobility group box which most likely constitutes the structure recognition element for cisplatin-modified DNA. This …

**Accessions** — [HGNC:11327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11327) · Entrez [6749](https://www.ncbi.nlm.nih.gov/gene/6749) · UniProt [Q08945](https://www.uniprot.org/uniprotkb/Q08945) · Ensembl [ENSG00000149136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149136)

## Data

Gene col 7343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7343); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7343]; `tensor/DDL_lfc|DDL_z.npy` [7343]; `embed/gene_vectors.npy` [7343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7343 or target_col == 7343). Every well: [[SSRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

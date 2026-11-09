---
symbol: "GHITM"
type: "gene"
col: 9165
ensembl_id: "ENSG00000165678"
name: "growth hormone inducible transmembrane protein"
location: "10q23.1"
module: 133
arm: "+"
pooled_cpm: 104.9
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# GHITM

*growth hormone inducible transmembrane protein* — 10q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.30× (z +17.1, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.18× (z +11.2, q 9e-27, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.775× (z -4.8, q 0.001, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.270×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.397×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSDE1]] (+0.69, fdr 7e-06), [[NBR2]] (+0.68, fdr 1e-05), [[IDH1]] (+0.67, fdr 7e-06); moves opposite to [[KRI1]] (-0.64, fdr 1e-05), [[MTRES1]] (-0.61, fdr 3e-05), [[PPP1R35]] (-0.59, fdr 2e-05, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[TRAF2]] (-0.56, fdr 1e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.30×** | +17.1 | 0e+00 | 48/49 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +15.7 | 0e+00 | 44/44 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +11.6 | 9e-29 | 44/45 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.18×** | +11.2 | 9e-27 | 47/48 (LoVo, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +9.5 | 2e-19 | 46/49 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.86×** | +8.9 | 7e-17 | 45/48 (HT-29, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +8.5 | 1e-15 | 45/48 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +7.6 | 2e-12 | 43/48 (HT-29, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.8 | 4e-07 | 39/50 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.47×** | +5.5 | 2e-06 | 37/48 (C32, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.43×** | +5.1 | 2e-05 | 38/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.42×** | +4.9 | 5e-05 | 37/47 (COLO 205, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.7 | 1e-04 | 32/45 (A-172, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.3 | 6e-04 | 35/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.33×** | +4.1 | 0.001 | 30/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.031 | 25/49 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.034 | 28/48 (RKO, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.042 | 26/48 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +3.0 | 0.084 | 23/48 (PANC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9165.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.270×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.397×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -4.8 | 0.001 | 34/48 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.756×** | -4.0 | 0.019 | 34/49 (SW480, KATO III, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 91.4 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.00× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 89.4 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.79× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 143 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 161 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.81× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 119 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +16.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 115 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.6) | — |
| [[A549 (line)]] | wt | 81.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +17.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 71.6 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.56× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 103 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.71× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 78.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +11.0) | — |
| [[SW480 (line)]] | alt | 142 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +17.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.48× (z +11.1) | — |
| [[A498 (line)]] | wt | 106 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +15.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 70.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.48× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 92.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 144 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.05× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 140 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +13.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 122 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 72.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +12.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 62.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +11.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 156 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +10.9) | — |
| [[LoVo (line)]] | wt | 126 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.73× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 71.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +14.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 155 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 99.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.29× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 72.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 91.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 47.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 100.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +12.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 129 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.48× (z +8.9) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.270× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 80.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +11.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 85.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.14× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 79.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 66.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 93.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 176 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 68.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.30× (z +11.0) | — |
| [[H4 (line)]] | wt | 90.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 88.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +12.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 79.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 85.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[NBR2]] | +0.68 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[IDH1]] | +0.67 | +0.73 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[NFE2L1]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SERPINH1]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PAPOLA]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[METTL4]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[IARS1]] | +0.60 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ALDH2]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[SLC7A11]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[CANX]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRI1]] | -0.64 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[MTRES1]] | -0.61 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[PPP1R35]] ⚠ | -0.59 | -0.48 / -0.55 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAF2]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[POGZ]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[NTMT1]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[EXOC6]] | -0.53 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ABCF1]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[NBPF14]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[IER2]] | -0.51 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[RELB]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PIM3]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[TGIF2]] | -0.51 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GHITM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.4, 45.3); signed map (-14.7, 22.0). **Vector** length 96.3, 33.9% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.2 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +11.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.6 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.3 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | +0.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | growth hormone inducible transmembrane protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.1 — chr10:84,139,482-84,154,841 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC282, PTD010, DERP2, My021, TMBIM5, MICS1 |
| Gene groups (HGNC) | Transmembrane BAX inhibitor motif containing |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3K2](https://www.uniprot.org/uniprotkb/Q9H3K2) (Growth hormone-inducible transmembrane protein):

> Plays an important role in maintenance of mitochondrial morphology and in mediating either calcium or potassium/proton antiport. Mediates proton-dependent calcium efflux from mitochondrion. Also functions as an electroneutral mitochondrial proton/potassium exchanger. Required for the mitochondrial tubular network and cristae organization. Involved in apoptotic release of cytochrome c. Inhibits the proteolytic activity of AFG3L2, stimulating respiration and stabilizing respiratory enzymes in …

**Summary**, from NCBI Gene [27069](https://www.ncbi.nlm.nih.gov/gene/27069):

> Enables calcium:proton antiporter activity. Involved in calcium export from the mitochondrion; inner mitochondrial membrane organization; and negative regulation of release of cytochrome c from mitochondria. Located in endoplasmic reticulum membrane and mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17281) · Entrez [27069](https://www.ncbi.nlm.nih.gov/gene/27069) · UniProt [Q9H3K2](https://www.uniprot.org/uniprotkb/Q9H3K2) · Ensembl [ENSG00000165678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165678)

## Data

Gene col 9165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9165); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9165]; `tensor/DDL_lfc|DDL_z.npy` [9165]; `embed/gene_vectors.npy` [9165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9165 or target_col == 9165). Every well: [[GHITM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GHITM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

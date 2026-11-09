---
symbol: "CATSPERG"
type: "gene"
col: 1797
ensembl_id: "ENSG00000099338"
name: "catsper channel auxiliary subunit gamma"
location: "19q13.2"
module: 4
arm: "-"
pooled_cpm: 24.8
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CATSPERG

*catsper channel auxiliary subunit gamma* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.29× (z +22.2, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.488× (z -9.4, q 2e-18, down in 30 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.381× (z -6.6, q 6e-09, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00685]] (+0.66, fdr 7e-06), [[TPT1-AS1]] (+0.62, fdr 2e-05), [[SLC23A3]] (+0.61, fdr 7e-06); moves opposite to [[MRPL19]] (-0.70, fdr 7e-06), [[DLAT]] (-0.67, fdr 7e-06), [[PPP5C]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.29×** | +22.2 | 0e+00 | 45/47 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +12.4 | 1e-32 | 43/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.37×** | +11.3 | 2e-27 | 41/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +10.2 | 3e-22 | 36/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +8.9 | 1e-16 | 36/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +7.6 | 4e-12 | 35/46 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +6.6 | 3e-09 | 28/47 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.7 | 2e-04 | 23/47 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.002 | 20/48 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.37×** | +4.0 | 0.003 | 19/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.008 | 18/47 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.008 | 19/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.015 | 14/47 (KATO III, HT-29, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.030 | 11/47 (C-33 A, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.488×** | -9.4 | 2e-18 | 30/43 (Panc 03.27, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.496×** | -8.9 | 2e-16 | 20/31 (CFPAC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -6.6 | 6e-09 | 34/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.614×** | -6.4 | 2e-08 | 27/47 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.615×** | -6.4 | 2e-08 | 28/47 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.595×** | -6.3 | 2e-08 | 26/38 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -6.0 | 1e-07 | 26/45 (BT-474, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -5.5 | 2e-06 | 29/47 (PANC-1, H4, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.746×** | -5.5 | 3e-06 | 25/48 (A549, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.458×** | -5.4 | 4e-06 | 29/45 (PANC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.480×** | -5.0 | 2e-05 | 13/26 (HT-29, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.709×** | -4.4 | 6e-04 | 24/45 (A549, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.754×** | -3.7 | 0.008 | 20/46 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -3.7 | 0.008 | 18/43 (COLO 205, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.751×** | -3.6 | 0.014 | 22/47 (HT-29, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 65.6 | 1 | 10 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.212× (z -10.6) |
| [[HT-29 (line)]] | alt | 56.4 | 3 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 8.59 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +16.2) | — |
| [[H4 (line)]] | wt | 47.9 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0867× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[KATO III (line)]] | alt | 26.2 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 45.4 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0918× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 7.74 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +18.7) | — |
| [[PANC-1 (line)]] | alt | 45.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 22.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +16.7) | — |
| [[COLO 205 (line)]] | alt | 31.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +13.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -9.9) ⚠ toxic |
| [[HCT15 (line)]] | alt | 82.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0643× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 44.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 20.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +17.4) | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 10.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.171× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[AsPC-1 (line)]] | alt | 13.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.64× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 39.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.6) | [[TAK-901 (drug)]] 0.05 µM 0.169× (z -10.9) |
| [[C32 (line)]] | wt | 8.38 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 20.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.0562× (z -17.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 11.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.37× (z +14.7) | — |
| [[NCI-H23 (line)]] | alt | 30.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -9.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 52.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0450× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.6) | — |
| [[A-427 (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.236× (z -9.8) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 9.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.4) | — |
| [[J82 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +14.7) | — |
| [[NCI-H2347 (line)]] | alt | 9.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +8.7) | — |
| [[RKO (line)]] | wt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.66× (z +10.4) | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.108× (z -9.5) |
| [[A498 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00685]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TPT1-AS1]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[SLC23A3]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CD63]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[KPNB1-DT]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[LINC02018]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PPP1R13L]] | +0.60 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[SPATC1]] | +0.60 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[RABGEF1]] | +0.59 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[OTUD5]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[WNT9A]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL19]] | -0.70 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[DLAT]] | -0.67 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[PPP5C]] | -0.65 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[MRPL42]] | -0.64 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[XPO7]] | -0.64 | -0.73 / -0.54 | both halves | 1e-05 |  |
| [[FAM98B]] | -0.62 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[IPO8]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[GOT2]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[DLD]] | -0.62 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[SAAL1]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[SKP2]] | -0.60 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[TUBGCP3]] | -0.60 | -0.62 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CATSPERG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.1, -35.0); signed map (6.5, 11.4). **Vector** length 105, 27.8% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +22.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.2 | +2.3 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.0 | +2.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.8 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | catsper channel auxiliary subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,335,775-38,370,943 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434A1022, FLJ46353; previously C19orf15 |
| Gene groups (HGNC) | CatSpermasome complex |
| Reactome | 3 pathways, smallest: Sperm Motility And Taxes; Fertilization; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZRH7](https://www.uniprot.org/uniprotkb/Q6ZRH7) (Cation channel sperm-associated auxiliary subunit gamma):

> Auxiliary component of the CatSper complex, a complex involved in sperm cell hyperactivation. Sperm cell hyperactivation is needed for sperm motility which is essential late in the preparation of sperm for fertilization.

**Summary**, from NCBI Gene [57828](https://www.ncbi.nlm.nih.gov/gene/57828):

> CATSPERG is a subunit of the CATSPER (see CATSPER1; MIM 606389) sperm calcium channel, which is required for sperm hyperactivated motility and male fertility (Wang et al., 2009 [PubMed 19516020]).[supplied by OMIM, Jul 2010]

**Accessions** — [HGNC:25243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25243) · Entrez [57828](https://www.ncbi.nlm.nih.gov/gene/57828) · UniProt [Q6ZRH7](https://www.uniprot.org/uniprotkb/Q6ZRH7) · Ensembl [ENSG00000099338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099338)

## Data

Gene col 1797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1797); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1797]; `tensor/DDL_lfc|DDL_z.npy` [1797]; `embed/gene_vectors.npy` [1797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1797 or target_col == 1797). Every well: [[CATSPERG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CATSPERG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

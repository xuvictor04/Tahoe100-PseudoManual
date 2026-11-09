---
symbol: "ATG12"
type: "gene"
col: 7027
ensembl_id: "ENSG00000145782"
name: "autophagy related 12"
location: "5q22.3"
module: 18
arm: "-"
pooled_cpm: 98.67
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ATG12

*autophagy related 12* — 5q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +16.5, q 0e+00, up in 45 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.197×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.293×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOX4]] (+0.58, fdr 1e-05), [[MAP1LC3B]] (+0.56, fdr 3e-05), [[DYNLRB1]] (+0.53, fdr 2e-05); moves opposite to [[NUP93]] (-0.54, fdr 1e-05), [[SSRP1]] (-0.53, fdr 2e-05), [[LRRC45]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +16.5 | 0e+00 | 45/49 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +13.9 | 2e-41 | 43/49 (AsPC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +11.9 | 2e-30 | 43/48 (NCI-H1573, LS 180, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +11.7 | 3e-29 | 40/45 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +10.7 | 2e-24 | 30/48 (NCI-H1573, AsPC-1, …) | two highest doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +10.6 | 4e-24 | 43/48 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.48×** | +8.9 | 3e-17 | 29/44 (SK-MEL-2, H4, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +7.8 | 3e-13 | 33/47 (HT-29, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +7.7 | 8e-13 | 35/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.23×** | +4.9 | 4e-05 | 25/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.24×** | +4.8 | 7e-05 | 24/48 (NCI-H1573, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +4.8 | 9e-05 | 22/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.20×** | +4.1 | 0.002 | 21/50 (HS-578T, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 20/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.18× | +4.0 | 0.002 | 22/48 (AsPC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.004 | 22/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.011 | 17/48 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.015 | 19/47 (HS-578T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.015 | 13/48 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.030 | 17/47 (CFPAC-1, H4, …) | top dose only | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.073 | 12/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7027.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.197×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.293×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | 0.896× | -3.7 | 0.13 | 7/48 (KATO III, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.757× | -3.5 | 0.16 | 19/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 192 | 11 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +44.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.5× (z +30.0) | — |
| [[AsPC-1 (line)]] | alt | 279 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +34.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +13.5) | — |
| [[SW480 (line)]] | alt | 128 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.19× (z +17.4) | — |
| [[LoVo (line)]] | wt | 98.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +25.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +16.5) | — |
| [[NCI-H460 (line)]] | wt | 73.3 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +11.1) | — |
| [[A498 (line)]] | wt | 75.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +11.7) | — |
| [[A-427 (line)]] | wt | 183 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 95.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +14.9) | — |
| [[LOX-IMVI (line)]] | wt | 87.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 42.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +14.0) | — |
| [[A549 (line)]] | wt | 86.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 106 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.00× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 85.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 84.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.34× (z +17.6) | — |
| [[NCI-H23 (line)]] | alt | 72.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 93.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 81.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.8) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.293× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 131 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +24.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +14.0) | — |
| [[HS-578T (line)]] | alt | 101 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +12.4) | — |
| [[KATO III (line)]] | alt | 99.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +18.4) | — |
| [[NCI-H1792 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +14.3) | — |
| [[SNU-423 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 94.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +14.6) | — |
| [[SW48 (line)]] | wt | 71.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.11× (z +11.2) | — |
| [[H4 (line)]] | wt | 148 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HCT15 (line)]] | alt | 108 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 64.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 111 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +11.4) | — |
| [[J82 (line)]] | alt | 84.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 62.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.43× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW 900 (line)]] | alt | 54.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.5) | — |
| [[A-172 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 91.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOX4]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[MAP1LC3B]] | +0.56 | +0.45 / +0.61 | both halves | 3e-05 | same gene group; pathway: Autophagy; STRING 969 |
| [[DYNLRB1]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ATP6V1D]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[FCF1]] | +0.52 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[TXNL4B]] | +0.51 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[PCF11-AS1]] | +0.51 | +0.45 / +0.43 | both halves | 4e-05 |  |
| [[TPTE2P6]] | +0.50 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[TUT7]] | +0.50 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PAIP2]] | +0.50 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[PPP1R11]] | +0.49 | +0.37 / +0.49 | both halves | 9e-05 |  |
| [[ZNF490]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP93]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[SSRP1]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LRRC45]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SCAF4]] | -0.52 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[PTGES2]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[EIF4E]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[HEATR3]] | -0.51 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[CCDC88C]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[RANBP1]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[YBX2]] | -0.50 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[LSM12]] | -0.50 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[NDUFS6]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATG12's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **-** arm (projection on the module's main direction -0.353). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-16.7, -48.5); signed map (-12.1, 14.7). **Vector** length 92.4, 22.6% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.1 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +16.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.0 | +2.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.0 | +2.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.7 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | +0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.0 | +4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -2.7 | +1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.3 — chr5:115,828,200-115,841,837 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APG12; previously APG12L |
| Gene groups (HGNC) | Autophagy related; Atypical E3 ubiquitin ligases |
| Reactome | 9 pathways, smallest: Receptor Mediated Mitophagy; PINK1-PRKN Mediated Mitophagy; Negative regulators of DDX58/IFIH1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O94817](https://www.uniprot.org/uniprotkb/O94817) (Ubiquitin-like protein ATG12):

> Ubiquitin-like protein involved in autophagy vesicles formation. Conjugation with ATG5 through a ubiquitin-like conjugating system involving also ATG7 as an E1-like activating enzyme and ATG10 as an E2-like conjugating enzyme, is essential for its function. The ATG12-ATG5 conjugate acts as an E3-like enzyme which is required for lipidation of ATG8 family proteins and their association to the vesicle membranes. As part of the ATG8 conjugation system with ATG5 and ATG16L1, required for …

**Summary**, from NCBI Gene [9140](https://www.ncbi.nlm.nih.gov/gene/9140):

> Autophagy is a process of bulk protein degradation in which cytoplasmic components, including organelles, are enclosed in double-membrane structures called autophagosomes and delivered to lysosomes or vacuoles for degradation. ATG12 is the human homolog of a yeast protein involved in autophagy (Mizushima et al., 1998 [PubMed 9852036]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:588) · Entrez [9140](https://www.ncbi.nlm.nih.gov/gene/9140) · UniProt [O94817](https://www.uniprot.org/uniprotkb/O94817) · Ensembl [ENSG00000145782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145782)

## Data

Gene col 7027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7027); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7027]; `tensor/DDL_lfc|DDL_z.npy` [7027]; `embed/gene_vectors.npy` [7027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7027 or target_col == 7027). Every well: [[ATG12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

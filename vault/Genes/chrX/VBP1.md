---
symbol: "VBP1"
type: "gene"
col: 7932
ensembl_id: "ENSG00000155959"
name: "VHL binding protein 1"
location: "Xq28"
module: 85
arm: "-"
pooled_cpm: 54.54
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# VBP1

*VHL binding protein 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.32× (z +16.5, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.71× (z +6.3, q 3e-08, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.729× (z -3.8, q 0.093, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.238×; ⚠ cell-cycle shift, would explain all of this change); [[Menadione (drug)]] 0.05 µM in 1 line (SW 1271 0.0730×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.161×; ⚠ cell-cycle shift, explains ~45% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NNT]] (+0.62, fdr 2e-05), [[HFE]] (+0.59, fdr 9e-05), [[CPSF2]] (+0.59, fdr 3e-05); moves opposite to [[BAIAP3]] (-0.62, fdr 6e-05), [[FBXL16]] (-0.62, fdr 2e-05), [[KLHL26]] (-0.60, fdr 1e-04).
> It sits in the **-** arm of [[Module 085]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.32×** | +16.5 | 0e+00 | 48/48 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.65×** | +14.7 | 0e+00 | 42/42 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.48×** | +9.9 | 6e-21 | 43/45 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.87×** | +7.4 | 2e-11 | 45/47 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +6.3 | 3e-08 | 40/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +6.2 | 5e-08 | 40/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.64×** | +5.8 | 5e-07 | 43/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.52×** | +4.7 | 1e-04 | 36/48 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +4.7 | 1e-04 | 34/48 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.51×** | +4.7 | 2e-04 | 33/47 (A-172, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **1.46×** | +4.5 | 4e-04 | 32/47 (KATO III, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +4.5 | 4e-04 | 29/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.46×** | +4.3 | 7e-04 | 33/48 (A-172, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.43×** | +4.2 | 9e-04 | 31/48 (A549, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +4.2 | 0.001 | 25/48 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.001 | 30/48 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.004 | 30/48 (HT-29, C32, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.086 | 22/48 (HOP62, A549, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7932.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.238×; ⚠ cell-cycle shift, would explain all of this change); [[Menadione (drug)]] 0.05 µM in 1 line (SW 1271 0.0730×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.161×; ⚠ cell-cycle shift, explains ~45% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.729×** | -3.8 | 0.093 | 27/48 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.753× | -3.4 | 0.21 | 23/48 (A-427, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 67.1 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.94× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 95.2 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 46.0 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.68× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[SNU-423 (line)]] | alt | 57.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 75.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 57.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 47.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C32 (line)]] | wt | 26.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.44× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 44.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 53.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.37× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 66.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 25.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 52.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.55× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 44.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 56.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 57.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 48.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.87× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[H4 (line)]] | wt | 50.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.69× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 42.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 54.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 38.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 67.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 66.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 42.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.25× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 88.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 76.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 53.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 60.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[COLO 205 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 52.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 59.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 60.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW 1271 (line)]] | alt | 74.1 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0730× (z -9.3) |
| [[SW 900 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 66.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[BT-474 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | +0.62 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[HFE]] | +0.59 | +0.41 / +0.37 | both halves | 9e-05 |  |
| [[CPSF2]] | +0.59 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[AP5M1]] | +0.58 | +0.51 / +0.22 | both halves | 6e-04 |  |
| [[DECR1]] | +0.58 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[METTL4]] | +0.58 | +0.46 / +0.39 | both halves | 6e-05 |  |
| [[ARMT1]] | +0.58 | +0.56 / +0.37 | both halves | 7e-05 |  |
| [[ATP5PB]] | +0.57 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PSMC2]] | +0.57 | +0.56 / +0.35 | both halves | 1e-04 | STRING 435 |
| [[NDUFS1]] | +0.57 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[GPATCH2]] | +0.57 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[PAPOLA]] | +0.56 | +0.39 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAIAP3]] | -0.62 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[FBXL16]] | -0.62 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[KLHL26]] | -0.60 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[TMEM120B]] | -0.60 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[RALGDS]] | -0.59 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ATG4B]] | -0.59 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[GPR157]] | -0.59 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[SH3GL1]] | -0.58 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[NAT9]] | -0.58 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[DVL1]] | -0.57 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SLC66A2]] | -0.57 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ATG101]] | -0.57 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **-** arm (projection on the module's main direction -0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.7, 0.8); signed map (21.0, -26.1). **Vector** length 59.6, 14.8% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.8 | +6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.7 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | -1.3 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | +1.1 | -0.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | -2.2 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | +0.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.4 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | VHL binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:155,197,007-155,239,841 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PFD3, PFDN3 |
| Gene groups (HGNC) | Prefoldin subunits |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 4 pathways, smallest: Prefoldin mediated transfer of substrate  to CCT/TriC; Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding; Chaperonin-mediated protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [P61758](https://www.uniprot.org/uniprotkb/P61758) (Prefoldin subunit 3):

> Binds specifically to cytosolic chaperonin (c-CPN) and transfers target proteins to it. Binds to nascent polypeptide chain and promotes folding in an environment in which there are many competing pathways for nonnative proteins.

**Summary**, from NCBI Gene [7411](https://www.ncbi.nlm.nih.gov/gene/7411):

> The protein encoded by this gene interacts with the Von Hippel-Lindau protein to form an intracellular complex. The encoded protein functions as a chaperone protein, and may play a role in the transport of the Von Hippel-Lindau protein from the perinuclear granules to the nucleus or cytoplasm. Alternative splicing and the use of alternate transcription start sites results in multiple transcript variants encoding different protein isoforms. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:12662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12662) · Entrez [7411](https://www.ncbi.nlm.nih.gov/gene/7411) · UniProt [P61758](https://www.uniprot.org/uniprotkb/P61758) · Ensembl [ENSG00000155959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155959)

## Data

Gene col 7932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7932); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7932]; `tensor/DDL_lfc|DDL_z.npy` [7932]; `embed/gene_vectors.npy` [7932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7932 or target_col == 7932). Every well: [[VBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

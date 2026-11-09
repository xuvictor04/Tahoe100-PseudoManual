---
symbol: "COPS3"
type: "gene"
col: 6483
ensembl_id: "ENSG00000141030"
name: "COP9 signalosome subunit 3"
location: "17p11.2"
module: 24
arm: "-"
pooled_cpm: 37.17
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# COPS3

*COP9 signalosome subunit 3* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.92× (z +19.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.786× (z -6.2, q 3e-07, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.530×, NCI-H1792 0.284×, A-427 0.439×; ⚠ cell-cycle shift, explains ~87% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (HCT15 0.233×; ⚠ cell-cycle shift, explains ~59% of this change); [[AZD1390 (drug)]] 5 µM in 1 line (Hs 766T 0.0668×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERH]] (+0.68, fdr 7e-06), [[MLH1]] (+0.68, fdr 1e-05), [[FH]] (+0.66, fdr 1e-05); moves opposite to [[GABARAPL2]] (-0.65, fdr 7e-06), [[RPL36AL]] (-0.63, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[CDC34]] (-0.63, fdr 1e-05), [[COMMD6]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.92×** | +19.8 | 0e+00 | 47/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +14.5 | 4e-45 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.01×** | +12.8 | 4e-35 | 32/46 (A549, LoVo, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.61×** | +12.3 | 9e-33 | 43/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.73×** | +9.3 | 1e-18 | 34/42 (NCI-H460, KATO III, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.68×** | +9.2 | 3e-18 | 40/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +9.2 | 3e-18 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.57×** | +8.3 | 6e-15 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +7.8 | 4e-13 | 31/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.54×** | +7.7 | 1e-12 | 26/39 (PANC-1, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +7.1 | 7e-11 | 33/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.40×** | +5.9 | 1e-07 | 26/47 (LoVo, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +5.6 | 7e-07 | 26/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.5 | 1e-06 | 18/34 (A-172, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.23×** | +5.4 | 2e-06 | 25/48 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.2 | 7e-06 | 26/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.018 | 10/48 (NCI-H23, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.032 | 12/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6483.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.530×, NCI-H1792 0.284×, A-427 0.439×; ⚠ cell-cycle shift, explains ~87% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (HCT15 0.233×; ⚠ cell-cycle shift, explains ~59% of this change); [[AZD1390 (drug)]] 5 µM in 1 line (Hs 766T 0.0668×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.786×** | -6.2 | 3e-07 | 29/48 (A498, NCI-H661, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.729×** | -5.8 | 2e-06 | 27/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.753×** | -5.2 | 4e-05 | 24/48 (HCT15, SW48, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.3 | 0.002 | 0/48 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.865× | -3.7 | 0.019 | 22/48 (A498, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.816×** | -3.7 | 0.019 | 16/48 (SW 1088, PANC-1, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.824×** | -3.5 | 0.035 | 14/47 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.785× | -3.1 | 0.12 | 17/47 (J82, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.4 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +15.1) | — |
| [[NCI-H460 (line)]] | wt | 30.3 | 6 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.74× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +13.5) | — |
| [[A549 (line)]] | wt | 44.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 41.4 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.5 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 14.8× (z +10.7) | — |
| [[SW480 (line)]] | alt | 45.9 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.35× (z +13.1) | — |
| [[A-172 (line)]] | wt | 39.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[A-427 (line)]] | wt | 36.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[C32 (line)]] | wt | 25.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.4) | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0867× (z -8.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 23.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 33.5× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 38.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.70× (z +11.8) | — |
| [[KATO III (line)]] | alt | 36.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.74× (z +10.1) | — |
| [[LoVo (line)]] | wt | 27.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.1× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 27.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.26× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.284× (z -9.8) ⚠ cell-cycle shift, explains ~87% of this change |
| [[NCI-H23 (line)]] | alt | 47.1 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.24× (z +9.5) | — |
| [[A498 (line)]] | wt | 76.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.530× (z -10.4) ⚠ cell-cycle shift, explains ~87% of this change |
| [[BT-474 (line)]] | alt | 26.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 55.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.65× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.233× (z -9.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 1 | — | [[AZD1390 (drug)]] 5 µM 0.0668× (z -8.9) |
| [[HT-29 (line)]] | alt | 22.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.28× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 36.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.5× (z +10.3) | — |
| [[RKO (line)]] | wt | 38.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.42× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[AN3 CA (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERH]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[MLH1]] | +0.68 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[FH]] | +0.66 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[NCBP1]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[XRCC6]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TUBGCP3]] | +0.64 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[CENPH]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[NCAPH2]] | +0.62 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[CHEK1]] | +0.62 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[DYNC2I2]] | +0.62 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[FANCG]] | +0.61 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[PRPF8]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAPL2]] | -0.65 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | -0.63 | -0.56 / -0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDC34]] | -0.63 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.62 | -0.56 / -0.66 | both halves | 1e-05 | pathway: Neddylation; STRING 491 |
| [[RPL37A]] ⚠ | -0.62 | -0.59 / -0.62 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[DOCK6]] | -0.62 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[CLDN12]] | -0.61 | -0.40 / -0.71 | both halves | 5e-05 |  |
| [[EIF1B]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[BRI3]] | -0.60 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[C19orf81]] | -0.60 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[FAM182B]] | -0.59 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[RPL18]] ⚠ | -0.59 | -0.47 / -0.63 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.58 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[ARID3A]] | -0.58 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[ATP5MK]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.3, -32.5); signed map (-14.4, -43.6). **Vector** length 89.1, 21.8% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +5.8 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +5.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +5.2 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +12.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -4.9 | -3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.6 | +2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.1 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | COP9 signalosome subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,246,616-17,281,273 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SGN3, CSN3 |
| Gene groups (HGNC) | COP9 signalosome |
| Reactome | 11 pathways, smallest: DNA Damage Recognition in GG-NER; Formation of TC-NER Pre-Incision Complex; Transcription-Coupled Nucleotide Excision Repair (TC-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNS2](https://www.uniprot.org/uniprotkb/Q9UNS2) (COP9 signalosome complex subunit 3):

> Component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, IkappaBalpha/NFKBIA, ITPK1 and IRF8/ICSBP, possibly via its association with CK2 and …

**Summary**, from NCBI Gene [8533](https://www.ncbi.nlm.nih.gov/gene/8533):

> The protein encoded by this gene possesses kinase activity that phosphorylates regulators involved in signal transduction. It phosphorylates I kappa-Balpha, p105, and c-Jun. It acts as a docking site for complex-mediated phosphorylation. The gene is located within the Smith-Magenis syndrome region on chromosome 17. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2015]

**Accessions** — [HGNC:2239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2239) · Entrez [8533](https://www.ncbi.nlm.nih.gov/gene/8533) · UniProt [Q9UNS2](https://www.uniprot.org/uniprotkb/Q9UNS2) · Ensembl [ENSG00000141030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141030)

## Data

Gene col 6483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6483); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6483]; `tensor/DDL_lfc|DDL_z.npy` [6483]; `embed/gene_vectors.npy` [6483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6483 or target_col == 6483). Every well: [[COPS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

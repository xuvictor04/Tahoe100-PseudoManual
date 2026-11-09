---
symbol: "ATP6V0D1"
type: "gene"
col: 8273
ensembl_id: "ENSG00000159720"
name: "ATPase H+ transporting V0 subunit d1"
location: "16q22.1"
module: 59
arm: "+"
pooled_cpm: 28.32
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 3
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# ATP6V0D1

*ATPase H+ transporting V0 subunit d1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.53× (z +34.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.677× (z -6.3, q 2e-07, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.0943×, HT-29 0.153×, Panc 03.27 0.273×, SW 900 0.304×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.168×, SW1417 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.207×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW48 0.0886×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0942×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS18]] (+0.60, fdr 1e-05), [[NEU1]] (+0.60, fdr 2e-05), [[AMDHD2]] (+0.57, fdr 1e-05); moves opposite to [[NAE1]] (-0.56, fdr 3e-05), [[SORD]] (-0.47, fdr 5e-05), [[GLO1]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.53×** | +34.1 | 0e+00 | 47/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.62×** | +24.4 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.00×** | +21.1 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.60×** | +20.5 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.46×** | +19.8 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.71×** | +15.9 | 0e+00 | 42/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.60×** | +14.6 | 0e+00 | 44/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +14.2 | 5e-44 | 45/48 (SW480, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **5.15×** | +13.7 | 8e-41 | 44/48 (NCI-H460, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +12.8 | 1e-35 | 41/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +12.0 | 1e-31 | 39/48 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.17×** | +11.8 | 2e-30 | 40/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.99×** | +10.4 | 7e-24 | 42/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +9.8 | 7e-21 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +9.4 | 2e-19 | 41/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.87×** | +8.8 | 5e-17 | 34/48 (SW480, HOP62, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8273.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.0943×, HT-29 0.153×, Panc 03.27 0.273×, SW 900 0.304×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.168×, SW1417 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.207×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW48 0.0886×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0942×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.677×** | -6.3 | 2e-07 | 29/48 (SHP-77, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.814×** | -4.7 | 8e-04 | 19/48 (LoVo, SHP-77, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.795×** | -3.6 | 0.072 | 17/34 (AsPC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.809× | -3.2 | 0.23 | 17/47 (SW 900, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Busulfan (drug)]] 5 µM |  | 0.875× | -3.1 | 0.25 | 9/48 (NCI-H2030, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.6 | 15 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +31.3) | — |
| [[SW480 (line)]] | alt | 34.4 | 11 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.26× (z +21.4) | — |
| [[PANC-1 (line)]] | alt | 10.6 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.98× (z +16.6) | — |
| [[Hs 766T (line)]] | wt | 34.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +19.5) | — |
| [[HT-29 (line)]] | alt | 33.3 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -14.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 24.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +19.0) | — |
| [[NCI-H1573 (line)]] | alt | 41.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 59.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +18.3) | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +15.8) | [[AZD2858 (drug)]] 0.5 µM 0.0534× (z -10.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 26.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +14.4) | — |
| [[NCI-H23 (line)]] | alt | 17.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 37.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.88× (z +19.2) | — |
| [[SW1417 (line)]] | alt | 44.4 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 15.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +13.4) | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.41× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 17.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +15.6) | — |
| [[HS-578T (line)]] | alt | 18.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +15.2) | — |
| [[J82 (line)]] | alt | 35.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +21.1) | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +16.2) | — |
| [[NCI-H2347 (line)]] | alt | 23.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +20.0) | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 33.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +13.9) | — |
| [[A-172 (line)]] | wt | 14.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +18.3) | — |
| [[A-427 (line)]] | wt | 18.8 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.31× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 35.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.0943× (z -16.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 21.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +17.5) | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.60× (z +9.3) | — |
| [[LoVo (line)]] | wt | 23.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 20.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.35× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 41.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 48.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +17.1) | — |
| [[COLO 205 (line)]] | alt | 30.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +13.2) | — |
| [[SHP-77 (line)]] | alt | 25.4 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.71× (z +9.0) | [[Tucidinostat (drug)]] 0.5 µM 0.207× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +15.1) | — |
| [[C-33 A (line)]] | alt | 13.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.78× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0942× (z -8.6) |
| [[H4 (line)]] | wt | 8.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 19.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +8.7) | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0886× (z -8.8) |
| [[AN3 CA (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS18]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[NEU1]] | +0.60 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[AMDHD2]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CTNS]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[AP5Z1]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[TP53INP2]] | +0.55 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[NAPA]] | +0.54 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CTSA]] | +0.54 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ATP6V1D]] | +0.52 | +0.57 / +0.43 | both halves | 3e-05 | same gene group; pathway: Amino acids regulate mTORC1; STRING 999 |
| [[ZNF324]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ATP6V0C]] | +0.51 | +0.54 / +0.48 | both halves | 2e-05 | same gene group; pathway: Amino acids regulate mTORC1; STRING 999 |
| [[SPNS1]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAE1]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[SORD]] | -0.47 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[GLO1]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[FBXL4]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CARNMT1]] | -0.46 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[ANAPC1]] | -0.45 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[CLNS1A]] | -0.45 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[NUDT15]] | -0.45 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[EEF1E1]] | -0.45 | -0.49 / -0.43 | both halves | 3e-05 | pathway: MITF-M-regulated melanocyte development |
| [[DKC1]] | -0.44 | -0.46 / -0.42 | both halves | 4e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[ALG6]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[MTX2]] | -0.44 | -0.49 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.342). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.7, -47.1); signed map (-9.2, 7.4). **Vector** length 81.4, 21.0% of its response variance represented; |z| ≥ 3 in 1,275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +14.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +13.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.9 | +20.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.4 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.7 | -6.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.6 | -1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V0 subunit d1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,438,014-67,481,181 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATP6DV, VATX, VPATPD, P39, Vma6; previously ATP6D |
| Gene groups (HGNC) | V-type ATPase subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 19 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [P61421](https://www.uniprot.org/uniprotkb/P61421) (V-type proton ATPase subunit d 1):

> Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment. The V-ATPase complex also acts as an activator for mTORC1 on lysosomal …

**Summary**, from NCBI Gene [9114](https://www.ncbi.nlm.nih.gov/gene/9114):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A and three B subunits, two G …

**Accessions** — [HGNC:13724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13724) · Entrez [9114](https://www.ncbi.nlm.nih.gov/gene/9114) · UniProt [P61421](https://www.uniprot.org/uniprotkb/P61421) · Ensembl [ENSG00000159720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159720)

## Data

Gene col 8273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8273); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8273]; `tensor/DDL_lfc|DDL_z.npy` [8273]; `embed/gene_vectors.npy` [8273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8273 or target_col == 8273). Every well: [[ATP6V0D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

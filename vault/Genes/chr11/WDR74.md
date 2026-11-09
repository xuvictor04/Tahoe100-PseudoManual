---
symbol: "WDR74"
type: "gene"
col: 5440
ensembl_id: "ENSG00000133316"
name: "WD repeat domain 74"
location: "11q12.3"
module: 83
arm: "+"
pooled_cpm: 17.39
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# WDR74

*WD repeat domain 74* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.26× (z +18.7, q 0e+00, up in 40 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 3.03× (z +16.0, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.733× (z -4.5, q 0.003, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Aliskiren (drug)]] 0.5 µM in 1 line (CHP-212 0.0645×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QTRT1]] (+0.68, fdr 1e-05), [[PCBP1-AS1]] (+0.68, fdr 6e-05), [[VPS52]] (+0.67, fdr 1e-05); moves opposite to [[YIF1B]] (-0.64, fdr 1e-05), [[ANAPC11]] (-0.62, fdr 4e-05), [[C4orf48]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.26×** | +18.7 | 0e+00 | 40/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.58×** | +16.9 | 0e+00 | 30/31 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.03×** | +16.0 | 0e+00 | 41/47 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.98×** | +15.8 | 0e+00 | 45/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.05×** | +13.2 | 1e-37 | 36/36 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.66×** | +10.0 | 2e-21 | 44/46 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.70×** | +9.7 | 2e-20 | 41/47 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.26×** | +8.3 | 6e-15 | 41/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +7.9 | 2e-13 | 35/47 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +7.1 | 7e-11 | 32/43 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.00×** | +7.0 | 1e-10 | 38/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.3 | 1e-08 | 33/48 (HOP62, PANC-1, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.79×** | +5.9 | 1e-07 | 32/47 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.00×** | +5.9 | 2e-07 | 15/23 (LoVo, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.75×** | +5.7 | 4e-07 | 29/46 (LS 180, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +5.7 | 4e-07 | 33/47 (SW480, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.86×** | +5.6 | 7e-07 | 33/45 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.81×** | +5.5 | 1e-06 | 35/47 (LS 180, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.67×** | +5.2 | 6e-06 | 29/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +5.1 | 8e-06 | 30/47 (SW480, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.8 | 4e-05 | 24/48 (NCI-H2347, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.5 | 2e-04 | 24/46 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5440.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Aliskiren (drug)]] 0.5 µM in 1 line (CHP-212 0.0645×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -4.5 | 0.003 | 29/48 (A498, CHP-212, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | 0.524× | -3.5 | 0.15 | 17/48 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.714× | -3.3 | 0.16 | 20/46 (BT-474, C32, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 11.3 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.1× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.79× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 16.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.9× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.17× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +17.2) | — |
| [[HS-578T (line)]] | alt | 13.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 30.1× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 20.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +11.7) | — |
| [[C32 (line)]] | wt | 19.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +11.6) | — |
| [[KATO III (line)]] | alt | 14.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 30.8× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.20× (z +8.5) | — |
| [[LoVo (line)]] | wt | 15.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.55× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 26.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +15.4) | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 21.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +14.7) | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.0× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.54× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 13.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +12.8) | — |
| [[SW480 (line)]] | alt | 22.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 13.8 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.18× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.65× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.02× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 15.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.13× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +15.4) | — |
| [[SHP-77 (line)]] | alt | 22.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.84× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 28.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.3) | — |
| [[A-172 (line)]] | wt | 7.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +10.1) | — |
| [[A-427 (line)]] | wt | 36.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.75× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.0) | — |
| [[A549 (line)]] | wt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.12× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 1 | — | [[Aliskiren (drug)]] 0.5 µM 0.0645× (z -8.8) |
| [[COLO 205 (line)]] | alt | 7.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.35× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +12.3) | — |
| [[J82 (line)]] | alt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +8.5) | — |
| [[RKO (line)]] | wt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +11.1) | — |
| [[SW48 (line)]] | wt | 27.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QTRT1]] | +0.68 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | +0.68 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[VPS52]] | +0.67 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[DDX56]] | +0.66 | +0.57 / +0.58 | both halves | 1e-05 | STRING 975 |
| [[SNAPC5]] | +0.65 | +0.63 / +0.38 | both halves | 6e-05 |  |
| [[U2AF2]] | +0.64 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[DHX38]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[CROCC]] | +0.63 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[ZNF514]] | +0.61 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[POLDIP2]] | +0.61 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SLC5A6]] | +0.60 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[C8orf33]] | +0.60 | +0.55 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | -0.64 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ANAPC11]] | -0.62 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[C4orf48]] | -0.62 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.61 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PCMT1]] | -0.60 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[TMEM256]] | -0.60 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[TNFAIP8L1]] | -0.58 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[ATP5MJ]] | -0.58 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[BBLN]] | -0.58 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ZDHHC12]] | -0.57 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[LSM2]] | -0.56 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PAFAH1B3]] | -0.56 | -0.41 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers WDR74's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-10.0, 6.9); signed map (21.7, -22.9). **Vector** length 88.9, 23.3% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +18.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.2 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Afatinib (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 74 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,832,342-62,841,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10439, Nsa1 |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | MYC_TARGETS_V2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6RFH5](https://www.uniprot.org/uniprotkb/Q6RFH5) (WD repeat-containing protein 74):

> Regulatory protein of the MTREX-exosome complex involved in the synthesis of the 60S ribosomal subunit. Participates in an early cleavage of the pre-rRNA processing pathway in cooperation with NVL. Required for blastocyst formation, is necessary for RNA transcription, processing and/or stability during preimplantation development (By similarity).

**Summary**, from NCBI Gene [54663](https://www.ncbi.nlm.nih.gov/gene/54663):

> Involved in rRNA processing and ribosomal large subunit biogenesis. Located in nuclear exosome (RNase complex) and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25529) · Entrez [54663](https://www.ncbi.nlm.nih.gov/gene/54663) · UniProt [Q6RFH5](https://www.uniprot.org/uniprotkb/Q6RFH5) · Ensembl [ENSG00000133316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133316)

## Data

Gene col 5440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5440); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5440]; `tensor/DDL_lfc|DDL_z.npy` [5440]; `embed/gene_vectors.npy` [5440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5440 or target_col == 5440). Every well: [[WDR74 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR74.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "UBN1"
type: "gene"
col: 4025
ensembl_id: "ENSG00000118900"
name: "ubinuclein 1"
location: "16p13.3"
module: 20
arm: "-"
pooled_cpm: 83.38
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# UBN1

*ubinuclein 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.34× (z +28.7, q 0e+00, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW 900 0.133×, AsPC-1 0.409×, H4 0.238×, A549 0.411×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (SK-MEL-2 0.543×, AsPC-1 0.598×; ⚠ cell-cycle shift, explains ~94% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.201×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SW 1088 0.0837×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGNBP2]] (+0.63, fdr 1e-05), [[ING2]] (+0.63, fdr 1e-05), [[LIN7B]] (+0.63, fdr 3e-05); moves opposite to [[TMX1]] (-0.56, fdr 1e-05), [[MRPL42]] (-0.56, fdr 1e-05), [[MTHFD1]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +28.7 | 0e+00 | 45/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +14.5 | 1e-45 | 41/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +14.5 | 1e-45 | 43/48 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +14.2 | 8e-44 | 36/49 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +14.0 | 1e-42 | 41/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +12.9 | 3e-36 | 41/48 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.66×** | +12.1 | 5e-32 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.55×** | +10.1 | 6e-22 | 37/48 (AsPC-1, PANC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.52×** | +10.0 | 6e-22 | 35/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +6.7 | 9e-10 | 30/48 (COLO 205, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +6.6 | 3e-09 | 29/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +6.0 | 7e-08 | 31/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +5.8 | 4e-07 | 26/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **1.27×** | +5.5 | 1e-06 | 25/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +5.2 | 8e-06 | 23/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.9 | 3e-05 | 22/48 (AsPC-1, LS 180, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 2e-04 | 24/48 (SW480, COLO 205, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +4.5 | 2e-04 | 24/48 (Hs 766T, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 17/49 (HCT15, SW 1088, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.008 | 14/48 (RPMI-7951, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.019 | 21/49 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4025.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SW 900 0.133×, AsPC-1 0.409×, H4 0.238×, A549 0.411×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (SK-MEL-2 0.543×, AsPC-1 0.598×; ⚠ cell-cycle shift, explains ~94% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.201×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SW 1088 0.0837×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -5.5 | 3e-05 | 3/50 (NCI-H1792, SW 1088, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.838× | -4.2 | 0.008 | 22/49 (NCI-H1792, MIA PaCa-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.842× | -3.9 | 0.017 | 21/44 (SW 900, AsPC-1, …) | inconsistent across doses | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 0.850× | -3.8 | 0.017 | 20/48 (SK-MEL-2, AsPC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | 0.896× | -3.7 | 0.025 | 15/48 (SK-MEL-2, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.857× | -3.6 | 0.025 | 16/49 (AsPC-1, CFPAC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 69.3 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +26.7) | — |
| [[SW480 (line)]] | alt | 85.3 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 94.6 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 71.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +22.0) | — |
| [[KATO III (line)]] | alt | 93.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +18.8) | — |
| [[LS 180 (line)]] | wt | 60.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +17.5) | — |
| [[Hs 766T (line)]] | wt | 113 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +20.5) | — |
| [[LOX-IMVI (line)]] | wt | 65.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +20.4) | — |
| [[PANC-1 (line)]] | alt | 109 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +18.5) | — |
| [[BT-474 (line)]] | alt | 73.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +10.2) ⚠ cell-cycle shift, explains ~27% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.201× (z -15.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 59.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +18.9) | — |
| [[LoVo (line)]] | wt | 85.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 63.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +19.1) | — |
| [[Panc 03.27 (line)]] | alt | 52.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.2) | — |
| [[RKO (line)]] | wt | 76.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +15.5) | — |
| [[HEC-1-A (line)]] | alt | 62.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 105 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +24.5) | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 70.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 57.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 70.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 62.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 67.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.1) | — |
| [[HT-29 (line)]] | alt | 97.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +18.4) | — |
| [[hTERT-HPNE (line)]] | wt | 64.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +14.8) | — |
| [[J82 (line)]] | alt | 108 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 60.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 85.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 125 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.4) | — |
| [[A498 (line)]] | wt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +11.4) | — |
| [[C32 (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 66.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +17.5) | — |
| [[NCI-H1792 (line)]] | alt | 54.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.7) | — |
| [[NCI-H2030 (line)]] | alt | 73.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 52.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 81.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.3) | — |
| [[SHP-77 (line)]] | alt | 71.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 72.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 77.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 92.4 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0837× (z -9.7) |
| [[SW 1271 (line)]] | alt | 90.0 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.142× (z -9.0) ⚠ transcription drop; unreliable plate only |
| [[SW48 (line)]] | wt | 70.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.8) | — |
| [[A-172 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 94.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGNBP2]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ING2]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.63 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[PIAS4]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ZNF324]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ZMYM5]] | +0.58 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PMM1]] | +0.57 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[AKAP8L]] | +0.57 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[TRIM62]] | +0.56 | +0.27 / +0.64 | both halves | 3e-04 |  |
| [[TPRN]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[KLHL22]] | +0.54 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX1]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[MRPL42]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[VMA21]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[DHFR]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ATIC]] | -0.54 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[TMEM123]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[RPSA]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | -0.53 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[GNG12]] | -0.53 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[PFKM]] | -0.53 | -0.36 / -0.56 | both halves | 1e-04 | same gene group |
| [[PPP2R1B]] | -0.52 | -0.46 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.6, -28.4); signed map (-14.5, 0.2). **Vector** length 89.5, 22.6% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +28.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.3 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -7.5 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.9 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.3 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ubinuclein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,846,665-4,882,401 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; HIRA histone chaperone complex subunits |
| Reactome | 5 pathways, smallest: Formation of Senescence-Associated Heterochromatin Foci (SAHF); DNA Damage/Telomere Stress Induced Senescence; Cellular Senescence |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPG3](https://www.uniprot.org/uniprotkb/Q9NPG3) (Ubinuclein-1):

> Acts as a novel regulator of senescence. Involved in the formation of senescence-associated heterochromatin foci (SAHF), which represses expression of proliferation-promoting genes. Binds to proliferation-promoting genes. May be required for replication-independent chromatin assembly.

**Summary**, from NCBI Gene [29855](https://www.ncbi.nlm.nih.gov/gene/29855):

> Cellular senescence is a hallmark of tumor suppression and tissue aging. Senescent cells contain domains of heterochromatin, called senescence-associated heterochromatin foci (SAHF), that repress proliferation-promoting genes. The protein encoded by this gene binds to proliferation-promoting genes and is required for SAHF formation, enhancing methylation of histone H3. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:12506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12506) · Entrez [29855](https://www.ncbi.nlm.nih.gov/gene/29855) · UniProt [Q9NPG3](https://www.uniprot.org/uniprotkb/Q9NPG3) · Ensembl [ENSG00000118900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118900)

## Data

Gene col 4025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4025); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4025]; `tensor/DDL_lfc|DDL_z.npy` [4025]; `embed/gene_vectors.npy` [4025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4025 or target_col == 4025). Every well: [[UBN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

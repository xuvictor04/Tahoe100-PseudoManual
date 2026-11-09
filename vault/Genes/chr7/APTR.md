---
symbol: "APTR"
type: "gene"
col: 13194
ensembl_id: "ENSG00000214293"
name: "Alu-mediated CDKN1A/p21 transcriptional regulator"
location: "7q11.23"
module: 40
arm: "+"
pooled_cpm: 28.11
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# APTR

*Alu-mediated CDKN1A/p21 transcriptional regulator* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.18× (z +29.8, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.670× (z -5.9, q 2e-06, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.246×, MIA PaCa-2 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (RPMI-7951 0.146×, HT-29 0.308×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.307×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD8]] (+0.73, fdr 7e-06), [[HINFP]] (+0.69, fdr 7e-06), [[ECT2L]] (+0.68, fdr 7e-06); moves opposite to [[TMEM185B]] (-0.78, fdr 7e-06), [[CEP41]] (-0.73, fdr 1e-05), [[PSMG1]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.18×** | +29.8 | 0e+00 | 47/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.92×** | +15.8 | 0e+00 | 44/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.95×** | +15.3 | 0e+00 | 38/46 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.79×** | +15.1 | 0e+00 | 43/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.54×** | +13.7 | 1e-40 | 43/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +10.4 | 4e-23 | 39/48 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +9.0 | 2e-17 | 36/44 (AsPC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.8 | 4e-07 | 30/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.3 | 6e-06 | 25/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.2 | 9e-06 | 22/48 (SW1417, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 6e-05 | 24/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.5 | 3e-04 | 24/48 (KATO III, A-427, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 1e-03 | 21/48 (SW480, A549, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.1 | 0.002 | 19/47 (LoVo, PANC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +4.0 | 0.002 | 16/48 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.016 | 10/47 (PANC-1, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.18× | +3.4 | 0.020 | 14/48 (NCI-H1573, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13194.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.246×, MIA PaCa-2 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (RPMI-7951 0.146×, HT-29 0.308×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.307×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -5.9 | 2e-06 | 26/48 (NCI-H2347, A-427, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.634× | -3.5 | 0.10 | 18/47 (A-172, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.791× | -3.5 | 0.10 | 10/48 (LS 180, NCI-H23, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.796× | -3.4 | 0.11 | 13/48 (KATO III, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.3 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +20.0) | — |
| [[A498 (line)]] | wt | 29.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +19.7) | — |
| [[C32 (line)]] | wt | 20.9 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +13.6) | — |
| [[SW1417 (line)]] | alt | 28.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +23.1) | — |
| [[HS-578T (line)]] | alt | 22.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.33× (z +16.2) | — |
| [[A-172 (line)]] | wt | 24.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 37.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +18.6) | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[HT-29 (line)]] | alt | 66.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 20.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +14.6) | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +14.6) | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.96× (z +18.3) | — |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 20.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.72× (z +17.6) | — |
| [[CFPAC-1 (line)]] | alt | 20.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 20.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +14.7) | — |
| [[LoVo (line)]] | wt | 26.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H1792 (line)]] | alt | 32.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +14.8) | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 21.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +23.2) | — |
| [[RPMI-7951 (line)]] | alt | 23.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 18.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.78× (z +16.0) | — |
| [[A549 (line)]] | wt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +14.8) | — |
| [[BT-474 (line)]] | alt | 22.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +16.1) | — |
| [[C-33 A (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 23.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 25.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +9.1) | — |
| [[KATO III (line)]] | alt | 112 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 33.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.5) | — |
| [[RKO (line)]] | wt | 20.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +13.6) | — |
| [[SW48 (line)]] | wt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.88× (z +12.5) | — |
| [[A-427 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD8]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[HINFP]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ECT2L]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.68 | +0.46 / +0.74 | both halves | 2e-05 |  |
| [[RAB6A]] | +0.68 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[DENND10]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[MIR4458HG]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[TMEM165]] | +0.68 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.67 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[ABHD18]] | +0.66 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[GPBP1L1]] | +0.66 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[AAMDC]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | -0.78 | -0.64 / -0.76 | both halves | 7e-06 |  |
| [[CEP41]] | -0.73 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.66 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.66 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[PUF60]] | -0.65 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.65 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[TAF1B]] | -0.65 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[DDX10]] | -0.65 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[MGA]] | -0.64 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.64 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[NAA15]] | -0.63 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[RIF1]] | -0.63 | -0.55 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers APTR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SACS]] | B | SACS activity lowers APTR's level | lines that do not express SACS (5) vs lines expressing it (45) | 2.01× higher at baseline in the lines without SACS | 0.082 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-25.3, -36.9); signed map (-44.2, 13.6). **Vector** length 98.8, 24.9% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +29.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +15.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +10.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +9.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.4 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.1 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.6 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | Alu-mediated CDKN1A/p21 transcriptional regulator |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q11.23 — chr7:77,657,659-77,696,290 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously RSBN1L-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44173) · Entrez [100505854](https://www.ncbi.nlm.nih.gov/gene/100505854) · Ensembl [ENSG00000214293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214293)

## Data

Gene col 13194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13194); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13194]; `tensor/DDL_lfc|DDL_z.npy` [13194]; `embed/gene_vectors.npy` [13194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13194 or target_col == 13194). Every well: [[APTR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APTR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

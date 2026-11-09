---
symbol: "TRMT13"
type: "gene"
col: 4338
ensembl_id: "ENSG00000122435"
name: "tRNA methyltransferase 13"
location: "1p21.2"
module: 88
arm: "+"
pooled_cpm: 23.58
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# TRMT13

*tRNA methyltransferase 13* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +33.6, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.803× (z -5.2, q 1e-04, down in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (SNU-423 0.154×); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.134×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.240×; ⚠ toxic; transcription drop); [[GSK1059615 (drug)]] 0.5 µM in 1 line (COLO 205 0.0666×); [[PF-06260933 (drug)]] 5 µM in 1 line (HCT15 0.0584×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OCIAD1]] (+0.76, fdr 7e-06), [[RAD50]] (+0.75, fdr 7e-06), [[GTF2H1]] (+0.73, fdr 7e-06); moves opposite to [[SAP130]] (-0.72, fdr 7e-06), [[GNB2]] (-0.71, fdr 7e-06), [[IGSF8]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF606]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +33.6 | 0e+00 | 47/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.31×** | +29.0 | 0e+00 | 46/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.67×** | +22.9 | 0e+00 | 45/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +17.5 | 0e+00 | 32/41 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +15.8 | 0e+00 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +15.1 | 0e+00 | 28/37 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +11.5 | 1e-28 | 35/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +10.2 | 1e-22 | 26/44 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +9.3 | 8e-19 | 24/35 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +9.1 | 4e-18 | 27/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +6.6 | 3e-09 | 19/48 (RPMI-7951, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.7 | 1e-04 | 11/47 (NCI-H1573, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.20×** | +4.4 | 4e-04 | 18/48 (LS 180, NCI-H1573, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +4.2 | 0.001 | 14/48 (HS-578T, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.002 | 18/46 (HS-578T, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.7 | 0.007 | 14/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.6 | 0.010 | 14/48 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.011 | 14/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Afatinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.032 | 7/48 (C-33 A, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4338.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (SNU-423 0.154×); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.134×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.240×; ⚠ toxic; transcription drop); [[GSK1059615 (drug)]] 0.5 µM in 1 line (COLO 205 0.0666×); [[PF-06260933 (drug)]] 5 µM in 1 line (HCT15 0.0584×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.803×** | -5.2 | 1e-04 | 13/47 (SNU-423, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 0.05 µM |  | 0.842× | -3.9 | 0.028 | 12/47 (SW48, RKO, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.899× | -3.7 | 0.040 | 10/48 (LS 180, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.863× | -3.6 | 0.040 | 13/47 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 33.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 24.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +21.8) | — |
| [[PANC-1 (line)]] | alt | 24.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +16.9) | — |
| [[LoVo (line)]] | wt | 23.2 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.26× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 29.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.9) | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 24.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +17.3) | — |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +14.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 38.1 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +15.9) | — |
| [[A-172 (line)]] | wt | 20.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.7) | — |
| [[H4 (line)]] | wt | 27.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.11× (z +10.8) | [[Docetaxel (drug)]] 0.05 µM 0.134× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 30.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +12.0) | [[PF-06260933 (drug)]] 5 µM 0.0584× (z -8.9) |
| [[Hs 766T (line)]] | wt | 26.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.9) | — |
| [[KATO III (line)]] | alt | 30.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +14.2) | — |
| [[LS 180 (line)]] | wt | 26.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +16.8) | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.5) | — |
| [[A498 (line)]] | wt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +11.1) | — |
| [[A549 (line)]] | wt | 17.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 17.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 18.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +8.6) | [[GSK1059615 (drug)]] 0.5 µM 0.0666× (z -9.8) |
| [[HT-29 (line)]] | alt | 25.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +18.1) | — |
| [[NCI-H23 (line)]] | alt | 19.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 44.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.08× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 21.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 18.3 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.154× (z -12.1) |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCIAD1]] | +0.76 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[RAD50]] | +0.75 | +0.83 / +0.65 | both halves | 7e-06 |  |
| [[GTF2H1]] | +0.73 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[USP40]] | +0.73 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[LZIC]] | +0.73 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[AIMP1]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[METTL6]] | +0.72 | +0.79 / +0.48 | both halves | 2e-05 | same gene group |
| [[NEK9]] | +0.72 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.71 | +0.76 / +0.50 | both halves | 1e-05 | same gene group |
| [[DUS4L]] | +0.71 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[ZC3H7B]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP130]] | -0.72 | -0.71 / -0.64 | both halves | 7e-06 |  |
| [[GNB2]] | -0.71 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[IGSF8]] | -0.70 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[UBTD1]] | -0.68 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[CARHSP1]] | -0.68 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[ANKRD9]] | -0.67 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[UBE2G1]] | -0.67 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[PDXP]] | -0.66 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[RIMS3]] | -0.65 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[TPST2]] | -0.65 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[GRB2]] | -0.65 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[SRPK2]] | -0.64 | -0.65 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF606]] | B | ZNF606 activity raises TRMT13's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 1.08× lower at baseline in the lines without ZNF606 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises TRMT13's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.786). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-23.1, 7.6); signed map (11.2, -25.5). **Vector** length 97.9, 21.6% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.8 | +29.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +22.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +15.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +33.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.5 | +11.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,133,150-100,150,496 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10287, FLJ11219, hTrmt13; previously CCDC76 |
| Gene groups (HGNC) | 7BS 2'O-ribose DNA/RNA methyltransferases; Zinc fingers U11-48K-like CHHC-type; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUP7](https://www.uniprot.org/uniprotkb/Q9NUP7) (tRNA:m(4)X modification enzyme TRM13 homolog):

> tRNA methylase which 2'-O-methylates cytidine(4) in tRNA(Pro) and tRNA(Gly)(GCC), and adenosine(4) in tRNA(His).

**Summary**, from NCBI Gene [54482](https://www.ncbi.nlm.nih.gov/gene/54482):

> Predicted to enable tRNA methyltransferase activity. Predicted to be involved in tRNA methylation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25502) · Entrez [54482](https://www.ncbi.nlm.nih.gov/gene/54482) · UniProt [Q9NUP7](https://www.uniprot.org/uniprotkb/Q9NUP7) · Ensembl [ENSG00000122435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122435)

## Data

Gene col 4338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4338); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4338]; `tensor/DDL_lfc|DDL_z.npy` [4338]; `embed/gene_vectors.npy` [4338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4338 or target_col == 4338). Every well: [[TRMT13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

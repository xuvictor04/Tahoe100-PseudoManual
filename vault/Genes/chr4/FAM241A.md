---
symbol: "FAM241A"
type: "gene"
col: 10522
ensembl_id: "ENSG00000174749"
name: "family with sequence similarity 241 member A"
location: "4q25"
module: 233
arm: "+"
pooled_cpm: 31.38
n_lines_expressing: 43
n_dd_up: 46
n_dd_down: 0
n_dd_up_clean: 39
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/233"]
generated_by: "tahoemap"
---

# FAM241A

*family with sequence similarity 241 member A* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.36× (z +31.5, q 0e+00, up in 40 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 3 lines (LoVo 0.341×, A-172 0.205×, AsPC-1 0.375×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.0950×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.498×; ⚠ cell-cycle shift, explains ~0% of this change); [[OTS514 (drug)]] 5 µM in 1 line (SHP-77 0.0883×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.527×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM36]] (+0.52, fdr 1e-05), [[GPR63]] (+0.51, fdr 2e-05), [[KLHL29]] (+0.50, fdr 3e-05); moves opposite to [[XRCC6]] (-0.51, fdr 2e-05), [[PSMD13]] (-0.51, fdr 2e-05), [[ANAPC10]] (-0.49, fdr 6e-05).
> It is in [[Module 233]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WNT9A]] → it (grade B ⚠); 4 go from it, the strongest it → [[PSMA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.36×** | +31.5 | 0e+00 | 40/41 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.00×** | +20.2 | 0e+00 | 40/41 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.84×** | +19.2 | 0e+00 | 39/41 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.78×** | +18.8 | 0e+00 | 40/41 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.67×** | +18.1 | 0e+00 | 38/41 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +16.5 | 0e+00 | 40/41 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.37×** | +15.3 | 0e+00 | 39/41 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +14.1 | 3e-43 | 38/41 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.03×** | +13.0 | 1e-36 | 36/41 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +12.8 | 7e-36 | 36/41 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.95×** | +12.3 | 5e-33 | 36/41 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +11.8 | 1e-30 | 30/41 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +11.5 | 4e-29 | 35/41 (C32, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +9.5 | 9e-20 | 31/41 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +8.7 | 1e-16 | 30/41 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +8.5 | 7e-16 | 28/41 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.8 | 2e-13 | 30/40 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10522.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 3 lines (LoVo 0.341×, A-172 0.205×, AsPC-1 0.375×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.0950×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.498×; ⚠ cell-cycle shift, explains ~0% of this change); [[OTS514 (drug)]] 5 µM in 1 line (SHP-77 0.0883×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.527×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[IQ 1 (drug)]] 5 µM |  | 0.696× | -3.5 | 0.20 | 10/39 (NCI-H23, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.2 | 0.20 | 17/41 (RKO, KATO III, …) | top dose only | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.787× | -3.2 | 0.20 | 6/40 (C32, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.844× | -3.2 | 0.20 | 16/39 (RKO, A-427, …) | inconsistent across doses | composition shift |
| [[NG25 (drug)]] 5 µM |  | 0.724× | -3.1 | 0.20 | 11/40 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.7 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +16.8) | — |
| [[HOP62 (line)]] | alt | 12.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +18.5) | — |
| [[SW480 (line)]] | alt | 23.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +17.6) | — |
| [[A498 (line)]] | wt | 21.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +19.5) | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +16.9) | — |
| [[NCI-H1792 (line)]] | alt | 65.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +27.8) | — |
| [[NCI-H2347 (line)]] | alt | 35.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +21.2) | — |
| [[BT-474 (line)]] | alt | 59.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.5) | — |
| [[C32 (line)]] | wt | 16.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +17.8) | — |
| [[SW 900 (line)]] | alt | 33.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +16.3) | — |
| [[CFPAC-1 (line)]] | alt | 39.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +25.5) | — |
| [[Panc 03.27 (line)]] | alt | 37.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +17.4) | — |
| [[PANC-1 (line)]] | alt | 21.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.0) | — |
| [[RKO (line)]] | wt | 127 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0950× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.2) |
| [[A-427 (line)]] | wt | 19.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 65.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +17.6) | [[Harringtonine (drug)]] 0.05 µM 0.375× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 53.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.94× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 45.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +15.2) | — |
| [[NCI-H2030 (line)]] | alt | 40.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 9.14 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 32.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +8.8) | — |
| [[KATO III (line)]] | alt | 51.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.1) | — |
| [[LoVo (line)]] | wt | 55.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +18.4) | [[Harringtonine (drug)]] 0.05 µM 0.341× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 42.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +12.8) | — |
| [[A-172 (line)]] | wt | 17.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.205× (z -9.1) |
| [[A549 (line)]] | wt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 57.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +13.4) | — |
| [[H4 (line)]] | wt | 34.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 9.69 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.20× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +15.1) | — |
| [[J82 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 45.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 32.3 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0883× (z -9.3) |
| [[SNU-423 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +11.6) | — |
| [[SW48 (line)]] | wt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM36]] | +0.52 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[GPR63]] | +0.51 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[KLHL29]] | +0.50 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[USP25]] | +0.50 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[GNG5]] | +0.49 | +0.52 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[ELOVL7]] | +0.49 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[LONRF3]] | +0.49 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[RAPH1]] | +0.49 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[OSBPL6]] | +0.48 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[RRAS2]] | +0.46 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[USP53]] | +0.46 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[SH3GL2]] | +0.46 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[UCHL3]] | +0.44 | +0.36 / +0.44 | both halves | 1e-04 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC6]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PSMD13]] | -0.51 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[ANAPC10]] | -0.49 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[GTF2F1]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[USP5]] | -0.47 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[RTF2]] | -0.47 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[LRRC47]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[PSMC2]] | -0.46 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CDKAL1]] | -0.46 | -0.49 / -0.48 | both halves | 2e-05 | STRING 436 |
| [[SAMM50]] | -0.46 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[BAP1]] | -0.46 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SNRPC]] | -0.46 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT9A]] | B | WNT9A activity lowers FAM241A's level | lines that do not express WNT9A (11) vs lines expressing it (39) | 2.02× higher at baseline in the lines without WNT9A | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB6B, DZIP1L, MRAS |
| [[USP53]] | C | USP53 activity raises FAM241A's level | lines that do not express USP53 (4) vs lines expressing it (46) | 3.24× lower at baseline in the lines without USP53 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: MORC4, SVIP, PLEKHA5; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMA6]] | B | FAM241A activity lowers PSMA6's level | lines that do not express FAM241A (7) vs lines expressing it (43) | 1.30× higher at baseline in the lines without FAM241A | 0.012 | ⚠ within organs, on part of the lines; also absent: TES, TRIB1, LRRCC1; maybe low, not absent |
| [[CA13]] | B | FAM241A activity raises CA13's level | lines that do not express FAM241A (7) vs lines expressing it (43) | 2.60× lower at baseline in the lines without FAM241A | 0.045 | ⚠ within organs, on part of the lines; also absent: TES, TRIB1, LRRCC1; maybe low, not absent |
| [[PSMB2]] | B | FAM241A activity lowers PSMB2's level | lines that do not express FAM241A (7) vs lines expressing it (43) | 1.28× higher at baseline in the lines without FAM241A | 0.053 | ⚠ within organs, on part of the lines; also absent: TES, TRIB1, LRRCC1; maybe low, not absent |
| [[UCHL3]] | B | FAM241A activity raises UCHL3's level | lines that do not express FAM241A (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without FAM241A | 0.070 | ⚠ within organs, on part of the lines; also absent: TES, TRIB1, LRRCC1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 233]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.9, 32.5); signed map (10.9, 21.3). **Vector** length 85.3, 21.2% of its response variance represented; |z| ≥ 3 in 1,222 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +8.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.8 | +19.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +9.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.9 | +4.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 241 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:112,145,454-112,195,256 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39370; previously C4orf32 |
| Matched by | ensembl_id |

UniProt [Q8N8J7](https://www.uniprot.org/uniprotkb/Q8N8J7) carries no function annotation.

**Summary**, from NCBI Gene [132720](https://www.ncbi.nlm.nih.gov/gene/132720):

> Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26813) · Entrez [132720](https://www.ncbi.nlm.nih.gov/gene/132720) · UniProt [Q8N8J7](https://www.uniprot.org/uniprotkb/Q8N8J7) · Ensembl [ENSG00000174749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174749)

## Data

Gene col 10522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10522); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10522]; `tensor/DDL_lfc|DDL_z.npy` [10522]; `embed/gene_vectors.npy` [10522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10522 or target_col == 10522). Every well: [[FAM241A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM241A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

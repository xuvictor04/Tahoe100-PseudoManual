---
symbol: "CHP1"
type: "gene"
col: 11914
ensembl_id: "ENSG00000187446"
name: "calcineurin like EF-hand protein 1"
location: "15q15.1"
module: 1
arm: "-"
pooled_cpm: 81.4
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CHP1

*calcineurin like EF-hand protein 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.55× (z +20.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.829× (z -4.1, q 0.026, down in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[AZD2858 (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.210×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.393×; ⚠ toxic; transcription drop); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A498 0.493×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMC1]] (+0.61, fdr 2e-05), [[RHOA]] (+0.61, fdr 1e-04), [[MAGT1]] (+0.61, fdr 2e-05); moves opposite to [[PALB2]] (-0.60, fdr 4e-05), [[UMPS]] (-0.59, fdr 1e-05), [[MRTO4]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +20.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +19.3 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +19.3 | 0e+00 | 47/49 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +17.9 | 0e+00 | 40/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.18×** | +16.9 | 0e+00 | 46/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +15.6 | 0e+00 | 39/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +11.0 | 5e-26 | 33/45 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +10.7 | 9e-25 | 43/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +10.0 | 1e-21 | 45/48 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +8.3 | 8e-15 | 38/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.39×** | +7.2 | 3e-11 | 29/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +7.0 | 1e-10 | 43/49 (PANC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +6.6 | 2e-09 | 21/49 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +6.3 | 1e-08 | 33/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.34×** | +6.2 | 3e-08 | 30/47 (COLO 205, LS 180, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.28×** | +5.1 | 1e-05 | 26/47 (NCI-H2030, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 7e-05 | 30/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +4.4 | 3e-04 | 22/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 5 µM |  | 1.14× | +3.8 | 0.005 | 9/49 (A549, NCI-H23, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.13× | +3.6 | 0.007 | 8/49 (A498, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11914.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[AZD2858 (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.210×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.393×; ⚠ toxic; transcription drop); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A498 0.493×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.829×** | -4.1 | 0.026 | 21/48 (HS-578T, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.840× | -3.8 | 0.031 | 17/49 (NCI-H1792, COLO 205, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.841× | -3.8 | 0.031 | 22/48 (NCI-H1573, SW 1088, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.840× | -3.6 | 0.048 | 18/47 (Panc 03.27, HS-578T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.897× | -3.3 | 0.11 | 14/48 (A-427, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.861× | -3.2 | 0.11 | 16/48 (A498, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.6 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +19.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.2 | 9 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +18.1) | [[AZD2858 (drug)]] 0.5 µM 0.210× (z -9.3) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 74.8 | 10 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.54× (z +15.4) | — |
| [[LoVo (line)]] | wt | 134 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.17× (z +11.2) | — |
| [[C32 (line)]] | wt | 59.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +18.2) | — |
| [[A-172 (line)]] | wt | 54.9 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.69× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 64.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +17.1) | — |
| [[HOP62 (line)]] | alt | 55.2 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.87× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 60.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +19.9) | — |
| [[NCI-H1792 (line)]] | alt | 96.0 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.4) | — |
| [[RKO (line)]] | wt | 77.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 73.4 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.53× (z +11.8) | — |
| [[SW480 (line)]] | alt | 58.1 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.01× (z +14.4) | — |
| [[HCT15 (line)]] | alt | 66.9 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.24× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.81× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 69.8 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +11.7) | — |
| [[J82 (line)]] | alt | 52.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +14.5) | — |
| [[NCI-H2347 (line)]] | alt | 58.1 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.30× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 49.5 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 53.3 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.06× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 113 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.9) | — |
| [[KATO III (line)]] | alt | 103 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.37× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 67.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 116 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.7) | — |
| [[A549 (line)]] | wt | 102 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 2.12× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 138 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 125 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 105 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 56.6 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.24× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 53.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 65.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.5) | — |
| [[A-427 (line)]] | wt | 67.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.493× (z -8.5) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 66.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.95× (z +8.9) | — |
| [[H4 (line)]] | wt | 65.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 75.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.30× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 163 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 111 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMC1]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RHOA]] | +0.61 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[MAGT1]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[CAST]] | +0.58 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[ANO8]] | +0.57 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[DDAH2]] | +0.55 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[PITPNM1]] | +0.55 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[SPAG9]] | +0.55 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[GNAI2]] | +0.54 | +0.35 / +0.41 | both halves | 1e-04 |  |
| [[MAPK8IP1]] | +0.53 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[CLIC4]] | +0.52 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[CYB5R3]] | +0.52 | +0.20 / +0.50 | both halves | 7e-04 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALB2]] | -0.60 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[UMPS]] | -0.59 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MRTO4]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RPP25]] | -0.58 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[ANAPC1]] | -0.57 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[C1orf109]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[GEMIN6]] | -0.56 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[POLR2D]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[MLH3]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[MRM1]] | -0.56 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[MIEF1]] | -0.56 | -0.36 / -0.61 | both halves | 9e-05 |  |
| [[METTL13]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-52.7, -0.8); signed map (-10.8, 35.0). **Vector** length 104, 29.4% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +11.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.2 | +5.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +10.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.9 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +7.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.5 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -7.5 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.3 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.2 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | calcineurin like EF-hand protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,230,839-41,281,887 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Sid470p, CHP, SLC9A1BP, p22, p24 |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 4 pathways, smallest: Hyaluronan degradation; Hyaluronan metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99653](https://www.uniprot.org/uniprotkb/Q99653) (Calcineurin B homologous protein 1):

> Calcium-binding protein involved in different processes such as regulation of vesicular trafficking, plasma membrane Na(+)/H(+) exchanger and gene transcription. Involved in the constitutive exocytic membrane traffic. Mediates the association between microtubules and membrane-bound organelles of the endoplasmic reticulum and Golgi apparatus and is also required for the targeting and fusion of transcytotic vesicles (TCV) with the plasma membrane. Functions as an integral cofactor in cell pH …

**Summary**, from NCBI Gene [11261](https://www.ncbi.nlm.nih.gov/gene/11261):

> This gene encodes a phosphoprotein that binds to the Na+/H+ exchanger NHE1. This protein serves as an essential cofactor which supports the physiological activity of NHE family members and may play a role in the mitogenic regulation of NHE1. The protein shares similarity with calcineurin B and calmodulin and it is also known to be an endogenous inhibitor of calcineurin activity. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17433) · Entrez [11261](https://www.ncbi.nlm.nih.gov/gene/11261) · UniProt [Q99653](https://www.uniprot.org/uniprotkb/Q99653) · Ensembl [ENSG00000187446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187446)

## Data

Gene col 11914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11914); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11914]; `tensor/DDL_lfc|DDL_z.npy` [11914]; `embed/gene_vectors.npy` [11914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11914 or target_col == 11914). Every well: [[CHP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

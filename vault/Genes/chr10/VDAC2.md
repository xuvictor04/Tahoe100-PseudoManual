---
symbol: "VDAC2"
type: "gene"
col: 9155
ensembl_id: "ENSG00000165637"
name: "voltage dependent anion channel 2"
location: "10q22.2"
module: 20
arm: "+"
pooled_cpm: 66.13
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# VDAC2

*voltage dependent anion channel 2* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.31× (z +16.9, q 0e+00, up in 48 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.57× (z +14.5, q 4e-45, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.805× (z -5.6, q 1e-05, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AN3 CA 0.138×, LoVo 0.502×, LS 180 0.417×, SK-MEL-2 0.507×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.113×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.574×; ⚠ cell-cycle shift, explains ~28% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SHP-77 0.234×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRB2]] (+0.67, fdr 1e-05), [[ATP2C1]] (+0.64, fdr 1e-05), [[EFCAB14]] (+0.63, fdr 7e-06); moves opposite to [[ERVK3-1]] (-0.63, fdr 1e-05), [[LIPT1]] (-0.61, fdr 1e-05), [[CROCCP2-1]] (-0.59, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.31×** | +16.9 | 0e+00 | 48/50 (A498, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.57×** | +14.5 | 4e-45 | 48/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.24×** | +11.2 | 7e-27 | 39/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +8.5 | 3e-15 | 40/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +7.0 | 3e-10 | 38/48 (LoVo, LS 180, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +6.8 | 8e-10 | 36/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.6 | 4e-09 | 25/35 (NCI-H1573, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +6.4 | 1e-08 | 36/48 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.41×** | +6.2 | 4e-08 | 30/48 (A-427, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +6.0 | 1e-07 | 29/45 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +5.4 | 4e-06 | 29/48 (SW480, LoVo, …) | rises with dose |  |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.32×** | +5.0 | 2e-05 | 33/49 (A498, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.30×** | +4.7 | 1e-04 | 26/48 (KATO III, PANC-1, …) | inconsistent across doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +4.7 | 1e-04 | 27/48 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +4.4 | 4e-04 | 26/48 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 20/48 (SW480, NCI-H2030, …) | top dose only | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.001 | 26/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Lapatinib ditosylate (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.005 | 21/48 (A549, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.007 | 12/48 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.009 | 18/49 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.009 | 11/48 (HT-29, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.034 | 13/49 (SW480, HT-29, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9155.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (AN3 CA 0.138×, LoVo 0.502×, LS 180 0.417×, SK-MEL-2 0.507×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.113×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.574×; ⚠ cell-cycle shift, explains ~28% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SHP-77 0.234×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.805×** | -5.6 | 1e-05 | 25/48 (AN3 CA, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | 0.819× | -3.5 | 0.12 | 20/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.827× | -3.4 | 0.15 | 17/49 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.782× | -3.2 | 0.19 | 18/47 (SNU-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -3.0 | 0.25 | 12/48 (NCI-H1573, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 0.844× | -3.0 | 0.25 | 10/49 (BT-474, HEC-1-A, …) | rises with dose | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 61.8 | 6 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.19× (z +11.5) | — |
| [[LoVo (line)]] | wt | 94.8 | 3 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.23× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -12.5) |
| [[SW480 (line)]] | alt | 71.1 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 6.50× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 39.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.80× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 60.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.87× (z +9.3) | — |
| [[KATO III (line)]] | alt | 40.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +9.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.75× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 113 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.52× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -12.1) |
| [[SHP-77 (line)]] | alt | 30.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Thymol (drug)]] 0.5 µM 0.234× (z -10.0) |
| [[A-427 (line)]] | wt | 54.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[AN3 CA (line)]] | alt | 96.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -17.6) |
| [[CHP-212 (line)]] | wt | 67.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.113× (z -10.5) |
| [[HT-29 (line)]] | alt | 41.7 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.96× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 57.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.44× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 45.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.97× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 58.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.96× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 59.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -8.6) |
| [[A-172 (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 94.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRB2]] | +0.67 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[ATP2C1]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[EFCAB14]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[GDAP2]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ARHGEF7]] | +0.61 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[STRAP]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SNX3]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 | pathway: Deubiquitination |
| [[TCP1]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[STAM]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 | pathway: Deubiquitination |
| [[EIF3H]] | +0.60 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[DERL1]] | +0.59 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TMED7]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK3-1]] | -0.63 | -0.75 / -0.55 | both halves | 1e-05 |  |
| [[LIPT1]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.59 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[LRCH3]] | -0.58 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[YAF2]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[UNK]] | -0.57 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[RELB]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[DHRSX]] | -0.56 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZC3H7B]] | -0.56 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[SERTAD4]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[DCAF8]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[NFKBIB]] | -0.55 | -0.61 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.4, -12.8); signed map (-50.1, -4.6). **Vector** length 103, 27.3% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.50 to 8); *Viral mRNA Translation* (reactome, mean cos +0.50 to 8); *Eukaryotic Translation Termination* (reactome, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +14.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +6.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.1 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | voltage dependent anion channel 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:75,210,154-75,231,448 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Voltage dependent anion channels; Centriolar satellite proteins |
| Hallmark sets | APOPTOSIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Mitochondrial calcium ion transport; PINK1-PRKN Mediated Mitophagy; Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [P45880](https://www.uniprot.org/uniprotkb/P45880) (Non-selective voltage-gated ion channel VDAC2):

> Non-selective voltage-gated ion channel that mediates the transport of anions and cations through the mitochondrion outer membrane and plasma membrane. The channel adopts an open conformation at zero mV and a closed conformation at both positive and negative potentials. There are two populations of channels; the main that functions in a lower open-state conductance with lower ion selectivity, that switch, in a voltage-dependent manner, from the open to a low-conducting 'closed' state and the …

**Summary**, from NCBI Gene [7417](https://www.ncbi.nlm.nih.gov/gene/7417):

> This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes 1, 2, 12 and 21, and alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:12672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12672) · Entrez [7417](https://www.ncbi.nlm.nih.gov/gene/7417) · UniProt [P45880](https://www.uniprot.org/uniprotkb/P45880) · Ensembl [ENSG00000165637](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165637)

## Data

Gene col 9155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9155); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9155]; `tensor/DDL_lfc|DDL_z.npy` [9155]; `embed/gene_vectors.npy` [9155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9155 or target_col == 9155). Every well: [[VDAC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VDAC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

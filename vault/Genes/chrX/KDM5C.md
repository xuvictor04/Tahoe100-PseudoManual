---
symbol: "KDM5C"
type: "gene"
col: 4709
ensembl_id: "ENSG00000126012"
name: "lysine demethylase 5C"
location: "Xp11.22"
module: 145
arm: "+"
pooled_cpm: 116.5
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# KDM5C

*lysine demethylase 5C* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.13× (z +13.7, q 3e-40, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.730× (z -5.5, q 2e-05, down in 26 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 0.807× (z -3.5, q 0.024, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 0.410×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUPT6H]] (+0.58, fdr 3e-05), [[OTUD5]] (+0.58, fdr 1e-05), [[CYTH2]] (+0.56, fdr 1e-05); moves opposite to [[CLN6]] (-0.51, fdr 3e-05), [[MTX2]] (-0.49, fdr 5e-05), [[FAR1]] (-0.49, fdr 8e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4709.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.13×** | +13.7 | 3e-40 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +13.4 | 2e-38 | 41/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.73×** | +12.6 | 7e-34 | 46/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +11.5 | 2e-28 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.85×** | +11.2 | 6e-27 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.00×** | +10.5 | 1e-23 | 44/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +8.8 | 1e-16 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +7.1 | 1e-10 | 41/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 5e-09 | 37/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.39×** | +5.9 | 2e-07 | 32/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.26×** | +4.0 | 0.003 | 24/48 (A498, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.003 | 27/48 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +3.8 | 0.006 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +3.8 | 0.006 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.049 | 22/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.060 | 18/48 (NCI-H460, SW480, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.098 | 14/48 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 0.410×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.730×** | -5.5 | 2e-05 | 26/44 (NCI-H1792, SW48, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.778×** | -4.6 | 0.001 | 30/48 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.773×** | -4.5 | 0.001 | 32/47 (SW480, HCT15, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.795×** | -4.2 | 0.004 | 29/49 (HT-29, SHP-77, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.855× | -4.0 | 0.006 | 20/48 (SNU-423, CHP-212, …) | top dose only | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.803×** | -4.0 | 0.006 | 24/48 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.807×** | -3.9 | 0.007 | 24/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.810×** | -3.9 | 0.008 | 29/48 (RKO, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.807×** | -3.5 | 0.024 | 22/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.874× | -3.5 | 0.026 | 11/48 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.829×** | -3.4 | 0.031 | 23/49 (A-427, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.031 | 23/48 (SNU-423, AN3 CA, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.816×** | -3.4 | 0.034 | 24/48 (SNU-423, SW 900, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.830×** | -3.3 | 0.043 | 22/48 (H4, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 136 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.78× (z +21.1) | — |
| [[PANC-1 (line)]] | alt | 97.2 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +15.3) | — |
| [[SW480 (line)]] | alt | 153 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +16.0) | — |
| [[HT-29 (line)]] | alt | 133 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.9) | — |
| [[LoVo (line)]] | wt | 73.5 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 84.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 77.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +15.8) | — |
| [[COLO 205 (line)]] | alt | 105 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +15.0) | — |
| [[HS-578T (line)]] | alt | 84.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 108 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.0) | — |
| [[A498 (line)]] | wt | 82.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +20.7) | — |
| [[HOP62 (line)]] | alt | 186 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.32× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.27× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 115 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.32× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 65.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 92.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +13.5) | — |
| [[RPMI-7951 (line)]] | alt | 177 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 122 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +11.4) | — |
| [[SW48 (line)]] | wt | 179 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +11.8) | — |
| [[A549 (line)]] | wt | 122 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 163 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.04× (z +9.4) | — |
| [[KATO III (line)]] | alt | 126 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 191 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +10.6) | — |
| [[A-427 (line)]] | wt | 97.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[BT-474 (line)]] | alt | 132 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.73× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 154 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.58× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 89.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.26× (z +8.8) | — |
| [[RKO (line)]] | wt | 218 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.72× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 85.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 92.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.0) | — |
| [[A-172 (line)]] | wt | 94.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 193 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 185 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPT6H]] | +0.58 | +0.62 / +0.46 | both halves | 3e-05 | STRING 485 |
| [[OTUD5]] | +0.58 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[CYTH2]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[FER1L4]] | +0.55 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[WDR26]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 | same gene group |
| [[PAIP2]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[NR1H2]] | +0.53 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[LGALS8]] | +0.52 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[CLK3]] | +0.52 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[FBRS]] | +0.51 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ZNF546]] | +0.50 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[ROPN1L]] | +0.49 | +0.35 / +0.42 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN6]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[MTX2]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[FAR1]] | -0.49 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[PMS1]] | -0.47 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[VRK2]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[MAST2]] | -0.45 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[TMEM131L]] | -0.45 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[EEF1E1]] | -0.44 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[DUT]] | -0.44 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[CDCA7]] | -0.44 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[DCTPP1]] | -0.43 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.201). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.9, -40.6); signed map (6.2, 14.0). **Vector** length 76.4, 21.4% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +5.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +6.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.5 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.5 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 5C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:53,176,283-53,225,422 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DXS1272E, XE169; previously SMCX, JARID1C, MRX13 |
| Gene groups (HGNC) | PHD finger proteins; AT-rich interaction domain containing; MicroRNA protein coding host genes; Lysine demethylase 5 family |
| Reactome | 3 pathways, smallest: HDMs demethylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P41229](https://www.uniprot.org/uniprotkb/P41229) (Lysine-specific demethylase 5C):

> Histone demethylase that specifically demethylates 'Lys-4' of histone H3, thereby playing a central role in histone code. Does not demethylate histone H3 'Lys-9', H3 'Lys-27', H3 'Lys-36', H3 'Lys-79' or H4 'Lys-20'. Demethylates trimethylated and dimethylated but not monomethylated H3 'Lys-4'. Participates in transcriptional repression of neuronal genes by recruiting histone deacetylases and REST at neuron-restrictive silencer elements. Represses the CLOCK-BMAL1 heterodimer-mediated …

**Summary**, from NCBI Gene [8242](https://www.ncbi.nlm.nih.gov/gene/8242):

> This gene is a member of the SMCY homolog family and encodes a protein with one ARID domain, one JmjC domain, one JmjN domain and two PHD-type zinc fingers. The DNA-binding motifs suggest this protein is involved in the regulation of transcription and chromatin remodeling. Mutations in this gene have been associated with X-linked cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:11114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11114) · Entrez [8242](https://www.ncbi.nlm.nih.gov/gene/8242) · UniProt [P41229](https://www.uniprot.org/uniprotkb/P41229) · Ensembl [ENSG00000126012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126012)

## Data

Gene col 4709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4709); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4709]; `tensor/DDL_lfc|DDL_z.npy` [4709]; `embed/gene_vectors.npy` [4709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4709 or target_col == 4709). Every well: [[KDM5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

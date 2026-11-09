---
symbol: "TAF2"
type: "gene"
col: 744
ensembl_id: "ENSG00000064313"
name: "TATA-box binding protein associated factor 2"
location: "8q24.12"
module: 204
arm: "+"
pooled_cpm: 127.59
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# TAF2

*TATA-box binding protein associated factor 2* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +22.5, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.813× (z -5.2, q 1e-04, down in 27 of 47 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.264×, SNU-423 0.457×, SHP-77 0.514×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.223×, RKO 0.493×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.365×, KATO III 0.527×; ⚠ toxic); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW48 0.364×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED1]] (+0.77, fdr 7e-06), [[CDK12]] (+0.74, fdr 7e-06), [[DPP8]] (+0.70, fdr 7e-06); moves opposite to [[USP3]] (-0.73, fdr 7e-06), [[SEC61A2]] (-0.68, fdr 7e-06), [[PPP1R2]] (-0.65, fdr 1e-05).
> It is in [[Module 204]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +22.5 | 0e+00 | 45/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +16.2 | 0e+00 | 47/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +13.0 | 4e-36 | 43/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +11.1 | 2e-26 | 39/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +8.2 | 2e-14 | 34/48 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +7.1 | 8e-11 | 36/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +6.4 | 2e-08 | 33/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +6.3 | 2e-08 | 29/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +6.2 | 3e-08 | 32/48 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +6.2 | 4e-08 | 31/48 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.8 | 3e-07 | 33/48 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.25×** | +5.8 | 3e-07 | 28/48 (AsPC-1, SHP-77, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +5.6 | 1e-06 | 14/48 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +5.6 | 1e-06 | 29/48 (SW480, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 2e-06 | 32/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +5.1 | 1e-05 | 27/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +4.2 | 8e-04 | 19/47 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.057 | 10/47 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 744.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.264×, SNU-423 0.457×, SHP-77 0.514×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.223×, RKO 0.493×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.365×, KATO III 0.527×; ⚠ toxic); [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW48 0.364×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.813×** | -5.2 | 1e-04 | 27/47 (SNU-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.830×** | -4.9 | 3e-04 | 26/48 (RPMI-7951, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.916× | -3.3 | 0.20 | 4/48 (AsPC-1, A-427, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.884× | -3.1 | 0.26 | 12/49 (RPMI-7951, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 99.5 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +16.1) | — |
| [[RKO (line)]] | wt | 329 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 130 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 169 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 104 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.1) | — |
| [[PANC-1 (line)]] | alt | 123 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.3) | — |
| [[A498 (line)]] | wt | 156 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.9) | — |
| [[AsPC-1 (line)]] | alt | 133 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.8) | [[Docetaxel (drug)]] 0.05 µM 0.509× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~21% of this change |
| [[BT-474 (line)]] | alt | 133 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.6) | — |
| [[C32 (line)]] | wt | 132 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.10× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 109 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 153 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 134 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.6) | — |
| [[KATO III (line)]] | alt | 114 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +12.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.527× (z -9.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 93.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 132 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +24.6) | — |
| [[NCI-H2347 (line)]] | alt | 87.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 135 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.8) | [[Docetaxel (drug)]] 0.05 µM 0.476× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~21% of this change |
| [[SNU-1 (line)]] | wt | 125 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 113 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.4) | [[Canagliflozin (drug)]] 0.05 µM 0.364× (z -9.5) |
| [[A-172 (line)]] | wt | 78.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 119 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 299 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +17.4) | — |
| [[NCI-H2030 (line)]] | alt | 160 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +17.8) | — |
| [[NCI-H23 (line)]] | alt | 127 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +16.0) | — |
| [[NCI-H460 (line)]] | wt | 97.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +16.3) | — |
| [[SNU-423 (line)]] | alt | 86.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.457× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.5) | — |
| [[A549 (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 89.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.5) | — |
| [[H4 (line)]] | wt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.514× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 80.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.8) | — |
| [[A-427 (line)]] | wt | 87.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 98.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED1]] | +0.77 | +0.81 / +0.64 | both halves | 7e-06 | STRING 862 |
| [[CDK12]] | +0.74 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[DPP8]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[EPC2]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[ERCC6L2]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[RABL3]] | +0.68 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[FAF2]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[USP16]] | +0.66 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[MRPS7]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP3]] | -0.73 | -0.79 / -0.59 | both halves | 7e-06 |  |
| [[SEC61A2]] | -0.68 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[PPP1R2]] | -0.65 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[RHEBL1]] | -0.65 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[STK32C]] | -0.64 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[LRP5L]] | -0.64 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[SNX30]] | -0.64 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[GTF2IP4]] | -0.63 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[AGAP3]] | -0.63 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[SPOPL]] | -0.63 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[TBC1D12]] | -0.63 | -0.68 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction -0.835). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.1, 11.2); signed map (13.5, -29.9). **Vector** length 113, 32.3% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +13.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +16.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +1.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.2 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:119,730,774-119,832,863 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII150, CIF150; previously TAF2B |
| Gene groups (HGNC) | M1 metallopeptidases; General transcription factor IID complex subunits |
| Reactome | 19 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1X5](https://www.uniprot.org/uniprotkb/Q6P1X5) (Transcription initiation factor TFIID subunit 2):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. TAF2 forms a promoter DNA …

**Summary**, from NCBI Gene [6873](https://www.ncbi.nlm.nih.gov/gene/6873):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11536) · Entrez [6873](https://www.ncbi.nlm.nih.gov/gene/6873) · UniProt [Q6P1X5](https://www.uniprot.org/uniprotkb/Q6P1X5) · Ensembl [ENSG00000064313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064313)

## Data

Gene col 744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 744); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 744]; `tensor/DDL_lfc|DDL_z.npy` [744]; `embed/gene_vectors.npy` [744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 744 or target_col == 744). Every well: [[TAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

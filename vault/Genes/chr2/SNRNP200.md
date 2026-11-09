---
symbol: "SNRNP200"
type: "gene"
col: 6834
ensembl_id: "ENSG00000144028"
name: "small nuclear ribonucleoprotein U5 subunit 200"
location: "2q11.2"
module: 127
arm: "+"
pooled_cpm: 146.05
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# SNRNP200

*small nuclear ribonucleoprotein U5 subunit 200* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.72× (z +20.0, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.854× (z -4.9, q 5e-04, down in 23 of 49 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.380×, HEC-1-A 0.638×, AsPC-1 0.623×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.426×, AsPC-1 0.509×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.544×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF8]] (+0.90, fdr 7e-06), [[AGO1]] (+0.76, fdr 7e-06), [[BAP1]] (+0.70, fdr 7e-06); moves opposite to [[MSX1]] (-0.64, fdr 1e-05), [[ERVK3-1]] (-0.63, fdr 1e-05), [[EIF1B]] (-0.61, fdr 7e-06).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.72×** | +20.0 | 0e+00 | 48/49 (RKO, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.95×** | +15.8 | 0e+00 | 48/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +10.1 | 1e-21 | 38/49 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +9.7 | 5e-20 | 35/44 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +8.1 | 9e-14 | 37/48 (RKO, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +7.5 | 5e-12 | 35/45 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +6.7 | 2e-09 | 31/47 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +6.4 | 9e-09 | 34/48 (RKO, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[NG25 (drug)]] 5 µM |  | **1.70×** | +6.1 | 8e-08 | 43/47 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +5.0 | 4e-05 | 40/49 (Panc 03.27, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.4 | 6e-04 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.19× | +3.9 | 0.005 | 19/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.008 | 27/49 (SW1417, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.6 | 0.012 | 21/38 (SK-MEL-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.019 | 6/48 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.050 | 17/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.14× | +2.9 | 0.100 | 11/48 (SW1417, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6834.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.380×, HEC-1-A 0.638×, AsPC-1 0.623×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.426×, AsPC-1 0.509×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.544×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -4.9 | 5e-04 | 23/49 (LoVo, AsPC-1, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.804×** | -4.8 | 5e-04 | 39/49 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.827×** | -4.2 | 0.005 | 29/49 (A549, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.901× | -3.3 | 0.16 | 18/48 (A-427, HEC-1-A, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 110 | 6 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.80× (z +12.1) | — |
| [[A549 (line)]] | wt | 152 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 7.39× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 152 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.24× (z +13.2) | [[Harringtonine (drug)]] 5 µM 0.426× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 152 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.99× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 130 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.67× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 133 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.36× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 120 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.64× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 161 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.98× (z +17.4) | — |
| [[RKO (line)]] | wt | 139 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 14.0× (z +17.6) | — |
| [[SK-MEL-2 (line)]] | alt | 126 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.38× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 103 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.10× (z +9.7) | — |
| [[A-427 (line)]] | wt | 126 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.67× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 165 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.08× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.76× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 127 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.59× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.623× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 99.1 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.69× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 142 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.15× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 125 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.72× (z +15.3) | — |
| [[SNU-1 (line)]] | wt | 116 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -10.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 174 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.72× (z +13.8) | — |
| [[SW480 (line)]] | alt | 185 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.02× (z +16.4) | — |
| [[C-33 A (line)]] | alt | 165 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.53× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 115 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.14× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 145 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.17× (z +15.7) | — |
| [[Hs 766T (line)]] | wt | 84.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.5× (z +14.9) | — |
| [[HS-578T (line)]] | alt | 94.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.35× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.57× (z +9.2) | — |
| [[KATO III (line)]] | alt | 95.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.33× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 134 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.88× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 141 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.39× (z +15.4) | — |
| [[NCI-H2030 (line)]] | alt | 225 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.96× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 354 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.54× (z +15.9) | — |
| [[NCI-H2347 (line)]] | alt | 111 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.19× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 127 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.16× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 170 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.97× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 191 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.52× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 117 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.73× (z +13.0) | — |
| [[H4 (line)]] | wt | 148 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.25× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 189 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.72× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 146 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.85× (z +9.6) | — |
| [[J82 (line)]] | alt | 121 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.04× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 205 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.73× (z +9.4) | — |
| [[SW48 (line)]] | wt | 183 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.19× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 166 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF8]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[AGO1]] | +0.76 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[BAP1]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[TAF6]] | +0.70 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[RPSA]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[PRKCSH]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[DCTN1]] | +0.69 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[PRPF31]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 999 |
| [[GTF3C1]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[VTI1B]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.65 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[EMC1]] | +0.65 | +0.59 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSX1]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.63 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.61 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[FDX2]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[ZCCHC10]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[RBX1]] | -0.58 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[LRCH3]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[KIF9-AS1]] | -0.57 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[MAFG]] | -0.57 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.55 | -0.46 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.4, -23.2); signed map (-21.2, -36.7). **Vector** length 128, 38.9% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +10.0 | +20.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +9.8 | +15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.2 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +7.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +6.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.3 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein U5 subunit 200 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,274,338-96,321,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | U5-200KD, HELIC2, KIAA0788, Brr2; previously ASCC3L1, RP33 |
| Gene groups (HGNC) | U5 small nuclear ribonucleoprotein; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 8 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing - Major Pathway; mRNA Splicing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75643](https://www.uniprot.org/uniprotkb/O75643) (U5 small nuclear ribonucleoprotein 200 kDa helicase):

> Catalyzes the ATP-dependent unwinding of U4/U6 RNA duplices, an essential step in the assembly of a catalytically active spliceosome. Plays a role in pre-mRNA splicing as a core component of precatalytic, catalytic and postcatalytic spliceosomal complexes. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable). Involved in spliceosome assembly, activation and disassembly. Mediates changes in the dynamic network of RNA-RNA interactions in …

**Summary**, from NCBI Gene [23020](https://www.ncbi.nlm.nih.gov/gene/23020):

> Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This protein belongs to the DEXH-box family of putative RNA helicases. It is a core component of …

**Accessions** — [HGNC:30859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30859) · Entrez [23020](https://www.ncbi.nlm.nih.gov/gene/23020) · UniProt [O75643](https://www.uniprot.org/uniprotkb/O75643) · Ensembl [ENSG00000144028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144028)

## Data

Gene col 6834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6834); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6834]; `tensor/DDL_lfc|DDL_z.npy` [6834]; `embed/gene_vectors.npy` [6834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6834 or target_col == 6834). Every well: [[SNRNP200 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRNP200.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

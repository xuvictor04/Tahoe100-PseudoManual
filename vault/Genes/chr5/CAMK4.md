---
symbol: "CAMK4"
type: "gene"
col: 7636
ensembl_id: "ENSG00000152495"
name: "calcium/calmodulin dependent protein kinase IV"
location: "5q22.1"
module: 61
arm: "+"
pooled_cpm: 18.0
n_lines_expressing: 29
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 16
direction_downstream: 17
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# CAMK4

*calcium/calmodulin dependent protein kinase IV* — 5q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +14.1, q 1e-42, up in 15 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.888× (z -7.0, q 1e-09, down in 3 of 27 measured lines) ⚠ position not correctable. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.860× (z -3.7, q 0.062, down in 11 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.0948×, SK-MEL-2 0.286×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Docetaxel (drug)]] 0.05 µM in 2 lines (H4 0.0627×, RPMI-7951 0.216×; ⚠ transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW 1271 0.0711×, J82 0.291×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.346×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.367×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.324×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHRM3]] (+0.59, fdr 1e-05), [[ELAVL2]] (+0.58, fdr 3e-05), [[ONECUT2]] (+0.57, fdr 2e-04); moves opposite to [[VPS39]] (-0.47, fdr 3e-05), [[MKRN5P]] (-0.46, fdr 1e-04), [[NUDT16-DT]] (-0.46, fdr 5e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PPP4R4]] → it (grade B ⚠); 17 go from it, the strongest it → [[CDK14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +14.1 | 1e-42 | 15/26 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +13.9 | 2e-41 | 18/27 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +10.5 | 1e-23 | 7/26 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +9.8 | 1e-20 | 19/27 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.70×** | +8.5 | 2e-15 | 5/21 (LoVo, SNU-423, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +7.1 | 1e-10 | 14/26 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +6.9 | 5e-10 | 9/25 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.51×** | +6.8 | 5e-10 | 4/18 (SW480, A498, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +6.5 | 5e-09 | 19/26 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.45×** | +6.4 | 7e-09 | 15/26 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +6.4 | 8e-09 | 18/27 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **1.38×** | +5.6 | 1e-06 | 5/23 (NCI-H2030, LoVo, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +4.8 | 8e-05 | 11/27 (NCI-H2030, NCI-H460, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.29×** | +4.2 | 0.001 | 7/25 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +4.2 | 0.001 | 8/27 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.014 | 8/26 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.022 | 3/27 (SHP-77, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7636.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.0948×, SK-MEL-2 0.286×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Docetaxel (drug)]] 0.05 µM in 2 lines (H4 0.0627×, RPMI-7951 0.216×; ⚠ transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW 1271 0.0711×, J82 0.291×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.346×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.367×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.324×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.888× | -7.0 | 1e-09 | 3/27 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.860× | -3.7 | 0.062 | 11/27 (A-427, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.062 | 8/26 (SNU-423, C32, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.822×** | -3.4 | 0.100 | 11/26 (C32, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 0.825× | -3.3 | 0.10 | 14/26 (H4, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.829× | -3.2 | 0.12 | 10/26 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.832× | -3.2 | 0.12 | 5/26 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.840× | -3.0 | 0.18 | 4/27 (SW 900, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.07 | 5 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.44× (z +17.5) | — |
| [[LoVo (line)]] | wt | 7.73 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 6.51× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 54.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.5) |
| [[SNU-423 (line)]] | alt | 55.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.4) | [[Selinexor (drug)]] 5 µM 0.455× (z -9.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[C32 (line)]] | wt | 60.6 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.198× (z -10.9) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 35.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +17.6) | — |
| [[J82 (line)]] | alt | 34.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 12.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +11.7) | — |
| [[A-172 (line)]] | wt | 48.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.430× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[CHP-212 (line)]] | wt | 83.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +8.7) | — |
| [[H4 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0627× (z -16.0) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 38.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 4.75 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.09× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.216× (z -9.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2030 (line)]] | alt | 5.39 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.74× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.216× (z -10.4) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.225× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 1271 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0711× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRM3]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ELAVL2]] | +0.58 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ONECUT2]] | +0.57 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[SORCS2]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[DPY19L2P1]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[CDC42EP3]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ADRA1B]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[STK32B]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[OSBPL6]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[JAZF1]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[P2RY1]] | +0.53 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[GALNT18]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS39]] | -0.47 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[MKRN5P]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[NUDT16-DT]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[LURAP1L]] | -0.45 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 3, C 13. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP4R4]] | B | PPP4R4 activity raises CAMK4's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 4.47× lower at baseline in the lines without PPP4R4 | 0.069 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088 |
| [[FYN]] | B | FYN activity raises CAMK4's level | lines that do not express FYN (8) vs lines expressing it (42) | 3.32× lower at baseline in the lines without FYN | 0.077 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent |
| [[AKT3]] | B | AKT3 activity raises CAMK4's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 4.65× lower at baseline in the lines without AKT3 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises CAMK4's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 7.34× lower at baseline in the lines without HS3ST3A1 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[MME]] | C | MME activity raises CAMK4's level | lines that do not express MME (30) vs lines expressing it (20) | 6.67× lower at baseline in the lines without MME | 0.001 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[RGS7]] | C | RGS7 activity raises CAMK4's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 4.57× lower at baseline in the lines without RGS7 | 0.003 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent; co-absent with the target |
| [[TRIM9]] | C | TRIM9 activity raises CAMK4's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 5.66× lower at baseline in the lines without TRIM9 | 0.005 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |
| [[ATRNL1]] | C | ATRNL1 activity raises CAMK4's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 4.82× lower at baseline in the lines without ATRNL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[NEGR1]] | C | NEGR1 activity raises CAMK4's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 5.22× lower at baseline in the lines without NEGR1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[DTNA]] | C | DTNA activity raises CAMK4's level | lines that do not express DTNA (22) vs lines expressing it (28) | 5.64× lower at baseline in the lines without DTNA | 0.026 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553; co-absent with the target |
| [[MDGA2]] | C | MDGA2 activity raises CAMK4's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 4.81× lower at baseline in the lines without MDGA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[CFAP20DC]] | C | CFAP20DC activity raises CAMK4's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 3.33× lower at baseline in the lines without CFAP20DC | 0.052 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 4, C 13. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDK14]] | B | CAMK4 activity raises CDK14's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.32× lower at baseline in the lines without CAMK4 | 0.017 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12 |
| [[HLA-L-1]] | B | CAMK4 activity raises HLA-L-1's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 2.59× lower at baseline in the lines without CAMK4 | 0.050 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12 |
| [[PPP4R4]] | B | CAMK4 activity raises PPP4R4's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 2.63× lower at baseline in the lines without CAMK4 | 0.050 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12 |
| [[FYN]] | B | CAMK4 activity raises FYN's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without CAMK4 | 0.086 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12 |
| [[HS3ST3A1]] | C | CAMK4 activity raises HS3ST3A1's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 5.72× lower at baseline in the lines without CAMK4 | 0.015 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[ATRNL1]] | C | CAMK4 activity raises ATRNL1's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.48× lower at baseline in the lines without CAMK4 | 0.023 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[LHFPL6]] | C | CAMK4 activity raises LHFPL6's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.83× lower at baseline in the lines without CAMK4 | 0.024 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[RGS7]] | C | CAMK4 activity raises RGS7's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.25× lower at baseline in the lines without CAMK4 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[MME]] | C | CAMK4 activity raises MME's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 6.27× lower at baseline in the lines without CAMK4 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[NEGR1]] | C | CAMK4 activity raises NEGR1's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.70× lower at baseline in the lines without CAMK4 | 0.050 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[TRIM9]] | C | CAMK4 activity raises TRIM9's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 4.46× lower at baseline in the lines without CAMK4 | 0.050 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[FLT1]] | C | CAMK4 activity raises FLT1's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.09× lower at baseline in the lines without CAMK4 | 0.053 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.0, 32.1); signed map (26.8, 32.7). **Vector** length 72.8, 18.7% of its response variance represented; |z| ≥ 3 in 627 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +13.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | +4.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +14.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +4.0 | +6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.1 | -2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -7.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | -1.9 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent protein kinase IV |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.1 — chr5:111,223,653-111,494,886 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CaMK-GR, CaMKIV |
| Gene groups (HGNC) | CAMK1 family |
| Hallmark sets | SPERMATOGENESIS, PI3K_AKT_MTOR_SIGNALING |
| Reactome | 29 pathways, smallest: Loss of phosphorylation of MECP2 at T308; CREB1 phosphorylation through the activation of CaMKII/CaMKK/CaMKIV cascasde; CaMK IV-mediated phosphorylation of CREB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16566](https://www.uniprot.org/uniprotkb/Q16566) (Calcium/calmodulin-dependent protein kinase type IV):

> Calcium/calmodulin-dependent protein kinase that operates in the calcium-triggered CaMKK-CaMK4 signaling cascade and regulates, mainly by phosphorylation, the activity of several transcription activators, such as CREB1, MEF2D, JUN and RORA, which play pivotal roles in immune response, inflammation, and memory consolidation. In the thymus, regulates the CD4(+)/CD8(+) double positive thymocytes selection threshold during T-cell ontogeny. In CD4 memory T-cells, is required to link T-cell antigen …

**Summary**, from NCBI Gene [814](https://www.ncbi.nlm.nih.gov/gene/814):

> The product of this gene belongs to the serine/threonine protein kinase family, and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. This enzyme is a multifunctional serine/threonine protein kinase with limited tissue distribution, that has been implicated in transcriptional regulation in lymphocytes, neurons and male germ cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1464) · Entrez [814](https://www.ncbi.nlm.nih.gov/gene/814) · UniProt [Q16566](https://www.uniprot.org/uniprotkb/Q16566) · Ensembl [ENSG00000152495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152495)

## Data

Gene col 7636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7636); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7636]; `tensor/DDL_lfc|DDL_z.npy` [7636]; `embed/gene_vectors.npy` [7636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7636 or target_col == 7636). Every well: [[CAMK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

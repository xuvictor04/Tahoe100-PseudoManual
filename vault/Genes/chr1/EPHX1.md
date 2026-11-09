---
symbol: "EPHX1"
type: "gene"
col: 6811
ensembl_id: "ENSG00000143819"
name: "epoxide hydrolase 1"
location: "1q42.12"
module: 26
arm: "+"
pooled_cpm: 22.9
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# EPHX1

*epoxide hydrolase 1* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.28× (z +31.4, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0696×).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAS]] (+0.64, fdr 6e-05), [[LSMEM1]] (+0.63, fdr 5e-05), [[EMC1-AS1]] (+0.62, fdr 2e-05); moves opposite to [[EIF5B]] (-0.59, fdr 3e-04), [[BRD7]] (-0.58, fdr 1e-04), [[TECPR1]] (-0.56, fdr 6e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +31.4 | 0e+00 | 46/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +17.0 | 0e+00 | 40/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +14.7 | 0e+00 | 44/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +12.8 | 3e-35 | 30/40 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +11.8 | 6e-30 | 24/32 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +11.0 | 3e-26 | 26/47 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +8.6 | 7e-16 | 33/48 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +7.9 | 3e-13 | 27/48 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +7.6 | 2e-12 | 28/45 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +7.0 | 2e-10 | 24/46 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.8 | 7e-10 | 24/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +6.2 | 3e-08 | 25/48 (LS 180, LoVo, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.84×** | +6.0 | 1e-07 | 20/47 (PANC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.9 | 1e-07 | 24/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.8 | 3e-07 | 21/48 (J82, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.8 | 3e-07 | 18/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +5.3 | 4e-06 | 18/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +4.7 | 7e-05 | 12/48 (HOP62, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6811.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0696×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.837× | -3.3 | 0.29 | 13/46 (Panc 03.27, A498, …) | two highest doses |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.29 | 9/47 (C-33 A, H4, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.844× | -3.2 | 0.29 | 10/47 (SW1417, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 87.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.89× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 44.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +13.3) | — |
| [[A549 (line)]] | wt | 19.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +15.8) | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +11.8) | — |
| [[LoVo (line)]] | wt | 15.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +14.0) | — |
| [[LS 180 (line)]] | wt | 31.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 15.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +16.2) | — |
| [[SW480 (line)]] | alt | 16.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +13.8) | — |
| [[A-172 (line)]] | wt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.44× (z +17.1) | — |
| [[COLO 205 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.61× (z +8.7) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[HCT15 (line)]] | alt | 32.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 35.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +11.4) | — |
| [[J82 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.58× (z +13.5) | — |
| [[KATO III (line)]] | alt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 5.96 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0696× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.58× (z +17.3) | — |
| [[NCI-H2030 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 8.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 39.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +12.3) | — |
| [[SW48 (line)]] | wt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +9.3) | — |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | +0.64 | +0.39 / +0.42 | both halves | 6e-05 |  |
| [[LSMEM1]] | +0.63 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[EMC1-AS1]] | +0.62 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[GIPC2]] | +0.62 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[ITM2B]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ADCY10]] | +0.58 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[MAP7D2]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[KMT2E-AS1]] | +0.58 | +0.39 / +0.26 | both halves | 4e-04 |  |
| [[C5orf15]] | +0.57 | +0.49 / +0.21 | both halves | 7e-04 |  |
| [[EFCAB5]] | +0.57 | +0.53 / +0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ERAP1]] | +0.57 | +0.33 / +0.30 | both halves | 2e-04 |  |
| [[POLR2A]] | +0.57 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CD27-AS1]] | +0.57 | +0.49 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5B]] | -0.59 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[BRD7]] | -0.58 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[TECPR1]] | -0.56 | -0.44 / -0.21 | both halves | 6e-04 |  |
| [[MTMR9]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PPM1G]] | -0.56 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[WRAP73]] | -0.55 | -0.30 / -0.24 | both halves | 5e-04 | pathway: HALLMARK_P53_PATHWAY |
| [[COMMD2]] | -0.54 | -0.32 / -0.27 | both halves | 3e-04 |  |
| [[WDR70]] | -0.54 | -0.20 / -0.36 | both halves | 7e-04 |  |
| [[RBFA]] | -0.54 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[STUB1]] | -0.53 | -0.30 / -0.21 | both halves | 6e-04 |  |
| [[EIF2B3]] | -0.53 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[TMEM177]] | -0.53 | -0.28 / -0.34 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EPHX1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLRK1-AS1]] | B | KLRK1-AS1 activity raises EPHX1's level | lines that do not express KLRK1-AS1 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without KLRK1-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.474). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (26.1, -13.8); signed map (20.0, 1.2). **Vector** length 92.5, 19.8% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +31.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +14.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +17.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -0.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.3 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | epoxide hydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:225,810,124-225,845,563 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously EPHX |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Hallmark sets | FATTY_ACID_METABOLISM, UV_RESPONSE_UP, XENOBIOTIC_METABOLISM, P53_PATHWAY |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P07099](https://www.uniprot.org/uniprotkb/P07099) (Epoxide hydrolase 1):

> Biotransformation enzyme that catalyzes the hydrolysis of arene and aliphatic epoxides to less reactive and more water soluble dihydrodiols by the trans addition of water (By similarity). Plays a role in the metabolism of endogenous lipids such as epoxide-containing fatty acids. Metabolizes the abundant endocannabinoid 2-arachidonoylglycerol (2-AG) to free arachidonic acid (AA) and glycerol. Binds 20(S)-hydroxycholesterol (20(S)-OHC) (By similarity).

**Summary**, from NCBI Gene [2052](https://www.ncbi.nlm.nih.gov/gene/2052):

> Epoxide hydrolase is a critical biotransformation enzyme that converts epoxides from the degradation of aromatic compounds to trans-dihydrodiols which can be conjugated and excreted from the body. Epoxide hydrolase functions in both the activation and detoxification of epoxides. Mutations in this gene cause preeclampsia, epoxide hydrolase deficiency or increased epoxide hydrolase activity. Alternatively spliced transcript variants encoding the same protein have been found for this …

**Accessions** — [HGNC:3401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3401) · Entrez [2052](https://www.ncbi.nlm.nih.gov/gene/2052) · UniProt [P07099](https://www.uniprot.org/uniprotkb/P07099) · Ensembl [ENSG00000143819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143819)

## Data

Gene col 6811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6811); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6811]; `tensor/DDL_lfc|DDL_z.npy` [6811]; `embed/gene_vectors.npy` [6811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6811 or target_col == 6811). Every well: [[EPHX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

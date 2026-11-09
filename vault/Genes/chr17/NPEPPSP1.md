---
symbol: "NPEPPSP1"
type: "gene"
col: 15822
ensembl_id: "ENSG00000274487"
name: "NPEPPS pseudogene 1"
location: "17q12"
module: 20
arm: "+"
pooled_cpm: 9.55
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# NPEPPSP1

*NPEPPS pseudogene 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.59× (z +10.9, q 5e-25, up in 4 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.09× (z +5.2, q 2e-05, up in 20 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.845× (z -5.3, q 6e-05, down in 28 of 45 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.643× (z -3.9, q 0.018, down in 20 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.300×, HT-29 0.209×, KATO III 0.223×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CFPAC-1 0.263×, HT-29 0.141×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0592×, CFPAC-1 0.268×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0881×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUMO1]] (+0.64, fdr 7e-06), [[CTC1]] (+0.63, fdr 8e-06), [[SMG1P1]] (+0.59, fdr 1e-05); moves opposite to [[DDX50]] (-0.52, fdr 3e-05), [[ZNF335]] (-0.52, fdr 1e-05), [[ST3GAL3]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GABRP]] → it (grade B ⚠); 1 goes from it, the strongest it → [[B4GALT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.59×** | +10.9 | 5e-25 | 4/11 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +8.2 | 5e-14 | 10/17 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +7.1 | 2e-10 | 13/23 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.09×** | +5.2 | 2e-05 | 20/39 (BT-474, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +4.2 | 0.003 | 16/35 (BT-474, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.057 | 7/43 (RPMI-7951, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.070 | 9/43 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15822.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.300×, HT-29 0.209×, KATO III 0.223×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CFPAC-1 0.263×, HT-29 0.141×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0592×, CFPAC-1 0.268×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0881×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.845× | -5.3 | 6e-05 | 28/45 (COLO 205, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.620×** | -4.2 | 0.007 | 19/44 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.643×** | -3.9 | 0.018 | 20/41 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.740×** | -3.8 | 0.024 | 20/36 (CFPAC-1, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.693× | -3.2 | 0.14 | 17/42 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.704× | -3.1 | 0.18 | 10/42 (CFPAC-1, NCI-H2347, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 139 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -8.9) |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 8.40 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0592× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 4.59 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0881× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO1]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CTC1]] | +0.63 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[SMG1P1]] | +0.59 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MBD2]] | +0.59 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ANXA11]] | +0.56 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ZC3H3]] | +0.55 | +0.33 / +0.62 | both halves | 1e-04 |  |
| [[B4GALT5]] | +0.54 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[MAPK3]] | +0.54 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PABIR2]] | +0.53 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.53 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PPP1CB]] | +0.52 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[GABRP]] | +0.51 | +0.55 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX50]] | -0.52 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ZNF335]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ST3GAL3]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[METTL23]] | -0.51 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ZNF281]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[DUSP6]] | -0.49 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[AASDH]] | -0.49 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[USE1]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[CEBPZ]] | -0.48 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MAP7D3]] | -0.48 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[NIFK]] | -0.48 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRP]] | B | GABRP activity raises NPEPPSP1's level | lines that do not express GABRP (44) vs lines expressing it (6) | 3.23× lower at baseline in the lines without GABRP | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[MUC16]] | B | MUC16 activity raises NPEPPSP1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.09× lower at baseline in the lines without MUC16 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[MUC16]] | B | MUC16 activity weakens NPEPPSP1's drug response | lines that do not express MUC16 (36) vs lines expressing it (9) | the lines without MUC16 respond 1.03× as strongly (z diff -0.30); strongest at Dinaciclib 5 µM: 2.96x vs 0.61x (z diff -6.5) | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; target measured in part of the lines; both ways; artifact flags |
| [[MAL2]] | B | MAL2 activity raises NPEPPSP1's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 1.68× lower at baseline in the lines without MAL2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[ERBB3]] | B | ERBB3 activity strengthens NPEPPSP1's drug response | lines that do not express ERBB3 (25) vs lines expressing it (20) | the lines without ERBB3 respond 0.88× as strongly (z diff +0.10); rises at some drug-doses, falls at others (32% from rises): Idarubicin (hydrochloride) 5 µM: 0.71x vs 0.49x (z diff +2.7); Panobinostat 5 µM: 0.67x vs 0.55x (z diff +1.3); TAK-901 5 µM: 2.54x vs 3.45x (z diff +0.7) | 0.093 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[MAL2]] | B | MAL2 activity strengthens NPEPPSP1's drug response | lines that do not express MAL2 (29) vs lines expressing it (16) | the lines without MAL2 respond 0.79× as strongly (z diff +0.23); strongest at Idarubicin (hydrochloride) 5 µM: 0.72x vs 0.46x (z diff +3.0) | 0.098 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; target measured in part of the lines; both ways; artifact flags |
| [[SFTPA2]] | C | SFTPA2 activity raises NPEPPSP1's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 1.95× lower at baseline in the lines without SFTPA2 | 0.015 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALT5]] | C | NPEPPSP1 activity raises B4GALT5's level | lines that do not express NPEPPSP1 (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without NPEPPSP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NET1, BMP1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.414). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.2, -26.7); signed map (-26.4, -33.9). **Vector** length 65.1, 11.1% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.7 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.2 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.8 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -1.6 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | NPEPPS pseudogene 1 |
| Locus type | pseudogene |
| Location | 17q12 — chr17:38,195,872-38,257,152 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [440434](https://www.ncbi.nlm.nih.gov/gene/440434):

> Predicted to enable metalloaminopeptidase activity. Predicted to be involved in peptide catabolic process and proteolysis. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:44259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44259) · Entrez [440434](https://www.ncbi.nlm.nih.gov/gene/440434) · Ensembl [ENSG00000274487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274487)

## Data

Gene col 15822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15822); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15822]; `tensor/DDL_lfc|DDL_z.npy` [15822]; `embed/gene_vectors.npy` [15822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15822 or target_col == 15822). Every well: [[NPEPPSP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPEPPSP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

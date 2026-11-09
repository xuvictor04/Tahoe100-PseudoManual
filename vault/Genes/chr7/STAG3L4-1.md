---
symbol: "STAG3L4-1"
type: "gene"
col: 16611
ensembl_id: "ENSG00000291153"
name: ""
location: ""
module: 16
arm: "-"
pooled_cpm: 42.1
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# STAG3L4-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.80× (z +11.4, q 3e-27, up in 30 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +10.1, q 1e-21, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.794× (z -4.0, q 0.031, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.391×, PANC-1 0.558×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.367×; ⚠ cell-cycle shift, explains ~26% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.569×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A498 0.429×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB47-AS1]] (+0.59, fdr 2e-05), [[ECI1]] (+0.57, fdr 3e-05), [[ECT2L]] (+0.56, fdr 1e-05); moves opposite to [[GEMIN4]] (-0.58, fdr 4e-05), [[ERAL1]] (-0.54, fdr 1e-05), [[DCLRE1B]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF594-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +11.4 | 3e-27 | 30/40 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +10.2 | 5e-22 | 37/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +10.1 | 1e-21 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +9.6 | 1e-19 | 33/45 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +9.0 | 2e-17 | 28/42 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +7.6 | 2e-12 | 30/47 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +7.2 | 6e-11 | 34/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 3e-10 | 30/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +6.5 | 4e-09 | 27/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +5.8 | 3e-07 | 22/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +5.4 | 4e-06 | 22/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.4 | 4e-04 | 18/48 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 16/48 (A-172, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.0 | 0.002 | 20/47 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.4 | 0.027 | 20/48 (SW480, LoVo, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.040 | 14/48 (A-172, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.043 | 11/48 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16611.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.391×, PANC-1 0.558×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.367×; ⚠ cell-cycle shift, explains ~26% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.569×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (A498 0.429×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.794×** | -4.0 | 0.031 | 18/48 (A498, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.813×** | -3.9 | 0.031 | 16/47 (SW 900, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.881× | -3.6 | 0.058 | 6/48 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 52.0 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 41.9 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.35× (z +14.8) | — |
| [[A498 (line)]] | wt | 59.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.429× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 75.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.84× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 61.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 51.6 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.47× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.0) | — |
| [[A-172 (line)]] | wt | 52.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.26× (z +10.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 39.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.90× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 34.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +10.7) | — |
| [[A-427 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.340× (z -9.1) ⚠ cell-cycle shift, explains ~6% of this change |
| [[C-33 A (line)]] | alt | 49.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.29× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +9.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 34.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.94× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 27.7 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.83× (z +8.5) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[Panc 03.27 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +8.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB47-AS1]] | +0.59 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[ECI1]] | +0.57 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[ECT2L]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RRAGC-DT]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ADAT3]] | +0.55 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[USF2]] | +0.54 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[BNIPL]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[EMC10]] | +0.52 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[ZC3H3]] | +0.51 | +0.29 / +0.58 | both halves | 2e-04 |  |
| [[MAP3K12]] | +0.51 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[ZNF565]] | +0.51 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[FLJ40194]] | +0.51 | +0.45 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN4]] | -0.58 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ERAL1]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[DCLRE1B]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SLC35A4]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[MRPL35]] | -0.52 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[MGAT2]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[APEX2]] | -0.51 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ALDH1B1]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[EIF6]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TTPAL]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[DCLRE1A]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CCT7]] | -0.48 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594-DT]] | B | ZNF594-DT activity raises STAG3L4-1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without ZNF594-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.324). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.8, 0.5); signed map (2.4, 7.2). **Vector** length 98.7, 22.4% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.6 | +7.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.3 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.3 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -3.3 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -1.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[vincristine (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -1.4 |

## What is on record

> [!warning] No registry record
> STAG3L4-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16611); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16611]; `tensor/DDL_lfc|DDL_z.npy` [16611]; `embed/gene_vectors.npy` [16611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16611 or target_col == 16611). Every well: [[STAG3L4-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAG3L4-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

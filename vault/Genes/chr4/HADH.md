---
symbol: "HADH"
type: "gene"
col: 6243
ensembl_id: "ENSG00000138796"
name: "hydroxyacyl-CoA dehydrogenase"
location: "4q25"
module: 6
arm: "+"
pooled_cpm: 13.52
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# HADH

*hydroxyacyl-CoA dehydrogenase* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +15.1, q 0e+00, up in 33 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.51× (z +6.7, q 2e-09, up in 22 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.752× (z -4.5, q 0.004, down in 13 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBGCP3]] (+0.71, fdr 7e-06), [[NCAPD3]] (+0.70, fdr 1e-05), [[SHMT1]] (+0.70, fdr 1e-05); moves opposite to [[IER5]] (-0.57, fdr 4e-05), [[CATSPERG]] (-0.57, fdr 4e-05), [[MIR22HG]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[STXBP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.51×** | +15.1 | 0e+00 | 33/40 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.54×** | +14.7 | 0e+00 | 22/25 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.01×** | +11.4 | 8e-28 | 36/47 (A498, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.86×** | +10.1 | 5e-22 | 33/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.94×** | +10.0 | 2e-21 | 24/32 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.51×** | +6.8 | 1e-09 | 26/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +6.7 | 2e-09 | 22/45 (A498, C-33 A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +6.3 | 2e-08 | 22/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +5.7 | 6e-07 | 22/48 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +5.7 | 8e-07 | 17/48 (A498, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.32×** | +4.3 | 7e-04 | 19/42 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.28×** | +3.9 | 0.005 | 13/42 (NCI-H1573, SK-MEL-2, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.8 | 0.007 | 12/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.23×** | +3.4 | 0.023 | 10/47 (J82, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.16× | +3.4 | 0.023 | 15/46 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.046 | 7/46 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.068 | 6/44 (HT-29, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.081 | 5/48 (SW1417, LoVo, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.100 | 8/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.752×** | -4.5 | 0.004 | 13/47 (RKO, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.838× | -4.1 | 0.011 | 14/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.790×** | -3.9 | 0.017 | 10/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.792×** | -3.8 | 0.017 | 12/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.800×** | -3.4 | 0.078 | 13/44 (C-33 A, BT-474, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.871× | -3.2 | 0.11 | 5/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.701× | -3.1 | 0.18 | 11/46 (RKO, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 20.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -10.8) ⚠ cell-cycle shift, explains ~80% of this change |
| [[A498 (line)]] | wt | 14.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 16.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 13.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0803× (z -8.6) |
| [[H4 (line)]] | wt | 12.7 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0607× (z -10.6) |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0771× (z -11.5) |
| [[KATO III (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 8.05 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.70× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1792 (line)]] | alt | 7.88 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.78× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 6.17 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0744× (z -10.8) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBGCP3]] | +0.71 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.70 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[SHMT1]] | +0.70 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[CDCA7]] | +0.68 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[LMNB1]] | +0.67 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[ERLIN1]] | +0.67 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[HAUS1]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[GUSB]] | +0.66 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[MMS22L]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[SKP2]] | +0.66 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[MANEA]] | +0.64 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[MAD2L1]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | -0.57 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[CATSPERG]] | -0.57 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[MIR22HG]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[FAM32A]] | -0.56 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[ZNF432]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[KCTD5]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[ZBTB43]] | -0.55 | -0.60 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STXBP6]] | B | STXBP6 activity raises HADH's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.30× lower at baseline in the lines without STXBP6 | 0.070 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[PBK]] | C | PBK activity raises HADH's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without PBK | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises HADH's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without DSCC1 | 0.052 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[CENPM]], [[SKA3]] | C | CENPM, SKA3 activity raises HADH's level | lines that do not express CENPM, SKA3 (3) vs lines expressing them (47) | 2.07× lower at baseline in the lines without CENPM, SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MCM3]] | C | MCM3 activity raises HADH's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.0, -41.1); signed map (-33.0, -42.4). **Vector** length 70.3, 12.0% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Resolution of Abasic Sites (AP sites)* (reactome, mean cos +0.51 to 15); *Base Excision Repair* (reactome, mean cos +0.51 to 15); *Gap-filling DNA repair synthesis and ligation in GG-NER* (reactome, mean cos +0.51 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.3 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.7 | +14.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | +3.2 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +5.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.3 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.0 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | hydroxyacyl-CoA dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:107,989,714-108,035,241 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HADH1, SCHAD; previously HADHSC |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM, APICAL_JUNCTION, ADIPOGENESIS |
| Reactome | 10 pathways, smallest: Beta oxidation of butanoyl-CoA to acetyl-CoA; Beta oxidation of lauroyl-CoA to decanoyl-CoA-CoA; Beta oxidation of hexanoyl-CoA to butanoyl-CoA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16836](https://www.uniprot.org/uniprotkb/Q16836) (Hydroxyacyl-coenzyme A dehydrogenase, mitochondrial):

> Mitochondrial fatty acid beta-oxidation enzyme that catalyzes the third step of the beta-oxidation cycle for medium and short-chain 3-hydroxy fatty acyl-CoAs (C4 to C10). Plays a role in the control of insulin secretion by inhibiting the activation of glutamate dehydrogenase 1 (GLUD1), an enzyme that has an important role in regulating amino acid-induced insulin secretion (By similarity). Plays a role in the maintenance of normal spermatogenesis through the reduction of fatty acid accumulation …

**Summary**, from NCBI Gene [3033](https://www.ncbi.nlm.nih.gov/gene/3033):

> This gene is a member of the 3-hydroxyacyl-CoA dehydrogenase gene family. The encoded protein functions in the mitochondrial matrix to catalyze the oxidation of straight-chain 3-hydroxyacyl-CoAs as part of the beta-oxidation pathway. Its enzymatic activity is highest with medium-chain-length fatty acids. Mutations in this gene cause one form of familial hyperinsulinemic hypoglycemia. The human genome contains a related pseudogene of this gene on chromosome 15. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:4799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4799) · Entrez [3033](https://www.ncbi.nlm.nih.gov/gene/3033) · UniProt [Q16836](https://www.uniprot.org/uniprotkb/Q16836) · Ensembl [ENSG00000138796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138796)

## Data

Gene col 6243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6243); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6243]; `tensor/DDL_lfc|DDL_z.npy` [6243]; `embed/gene_vectors.npy` [6243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6243 or target_col == 6243). Every well: [[HADH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HADH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

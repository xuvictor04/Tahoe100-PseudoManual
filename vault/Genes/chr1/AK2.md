---
symbol: "AK2"
type: "gene"
col: 44
ensembl_id: "ENSG00000004455"
name: "adenylate kinase 2"
location: "1p35.1"
module: 105
arm: "+"
pooled_cpm: 87.07
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# AK2

*adenylate kinase 2* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.76× (z +10.2, q 1e-21, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.612× (z -13.6, q 2e-39, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POM121]] (+0.73, fdr 7e-06), [[CHSY1]] (+0.72, fdr 7e-06), [[FAM210A]] (+0.72, fdr 7e-06); moves opposite to [[CPLANE1]] (-0.60, fdr 8e-06), [[LARP7]] (-0.54, fdr 4e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 44.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.76×** | +10.2 | 1e-21 | 41/49 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.30×** | +7.2 | 2e-10 | 29/49 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +6.4 | 3e-08 | 37/48 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +5.4 | 7e-06 | 29/48 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.32×** | +5.3 | 2e-05 | 26/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.7 | 3e-04 | 29/48 (SHP-77, LoVo, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.6 | 4e-04 | 0/50 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.4 | 8e-04 | 23/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.003 | 26/48 (MIA PaCa-2, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.26×** | +4.1 | 0.003 | 21/45 (LoVo, NCI-H1573, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.21×** | +3.6 | 0.016 | 24/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.019 | 20/48 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.033 | 19/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.039 | 18/48 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.19× | +3.2 | 0.047 | 19/49 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 44.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.612×** | -13.6 | 2e-39 | 40/48 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.818×** | -5.6 | 5e-06 | 23/48 (J82, C32, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.761×** | -5.2 | 4e-05 | 28/48 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.791×** | -4.0 | 0.007 | 21/50 (SW480, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.816×** | -4.0 | 0.007 | 25/48 (LoVo, KATO III, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.818×** | -4.0 | 0.007 | 23/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.876× | -3.8 | 0.014 | 10/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.833×** | -3.6 | 0.020 | 18/49 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.710×** | -3.5 | 0.031 | 18/49 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.715×** | -3.4 | 0.037 | 19/50 (LoVo, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.038 | 16/49 (AN3 CA, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 44. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.7 | 5 (5 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +10.1) ⚠ cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -11.9) |
| [[C32 (line)]] | wt | 186 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -16.4) |
| [[HOP62 (line)]] | alt | 101 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +12.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.07× (z +9.9) | — |
| [[SW480 (line)]] | alt | 90.2 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.17× (z +10.0) ⚠ cell-cycle shift, explains ~65% of this change | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -11.4) |
| [[C-33 A (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0948× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.449× (z -10.4) |
| [[HS-578T (line)]] | alt | 98.7 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.51× (z +12.6) | — |
| [[J82 (line)]] | alt | 116 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.59× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 161 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 106 | 2 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.35× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -13.5) |
| [[PANC-1 (line)]] | alt | 112 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 3.67× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -18.7) |
| [[A-172 (line)]] | wt | 55.9 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.49× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -8.5) |
| [[LS 180 (line)]] | wt | 83.3 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +8.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H23 (line)]] | alt | 112 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.69× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.9) |
| [[RKO (line)]] | wt | 116 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.9) |
| [[SW 1088 (line)]] | alt | 92.3 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.0872× (z -9.8) |
| [[A-427 (line)]] | wt | 73.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.428× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 53.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 62.4 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.94× (z +8.7) | — |
| [[LoVo (line)]] | wt | 60.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +11.8) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[LOX-IMVI (line)]] | wt | 75.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 52.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.8) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[NCI-H2030 (line)]] | alt | 105 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.33× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 68.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +10.6) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[RPMI-7951 (line)]] | alt | 119 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.51× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SNU-423 (line)]] | alt | 85.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -11.2) |
| [[A549 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 78.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 44), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POM121]] | +0.73 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[CHSY1]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[BTAF1]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[PDK1]] | +0.69 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[PPFIA4]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[HERC3]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[DDX41]] | +0.68 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.68 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[HK2]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[DHRS13]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPLANE1]] | -0.60 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[LARP7]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises AK2's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Temsirolimus) | 50% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[SLC6A6]] | C | SLC6A6 activity raises AK2's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without SLC6A6 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.793). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.5, -19.4); signed map (-39.6, 24.6). **Vector** length 124, 37.6% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +5.7 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +10.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.1 | -13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.7 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -4.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -5.2 | -1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.6 | -5.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.7 | -3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:33,007,986-33,080,996 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Adenylate kinases |
| Hallmark sets | ADIPOGENESIS, E2F_TARGETS |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P54819](https://www.uniprot.org/uniprotkb/P54819) (Adenylate kinase 2, mitochondrial):

> Catalyzes the reversible transfer of the terminal phosphate group between ATP and AMP. Plays an important role in cellular energy homeostasis and in adenine nucleotide metabolism. Adenylate kinase activity is critical for regulation of the phosphate utilization and the AMP de novo biosynthesis pathways. Plays a key role in hematopoiesis.

**Summary**, from NCBI Gene [204](https://www.ncbi.nlm.nih.gov/gene/204):

> Adenylate kinases are involved in regulating the adenine nucleotide composition within a cell by catalyzing the reversible transfer of phosphate groups among adenine nucleotides. Three isozymes of adenylate kinase, namely 1, 2, and 3, have been identified in vertebrates; this gene encodes isozyme 2. Expression of these isozymes is tissue-specific and developmentally regulated. Isozyme 2 is localized in the mitochondrial intermembrane space and may play a role in apoptosis. Mutations in this …

**Accessions** — [HGNC:362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:362) · Entrez [204](https://www.ncbi.nlm.nih.gov/gene/204) · UniProt [P54819](https://www.uniprot.org/uniprotkb/P54819) · Ensembl [ENSG00000004455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004455)

## Data

Gene col 44: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 44); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 44, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 44]; `tensor/DDL_lfc|DDL_z.npy` [44]; `embed/gene_vectors.npy` [44]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 44 or target_col == 44). Every well: [[AK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

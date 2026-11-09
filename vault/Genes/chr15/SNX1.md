---
symbol: "SNX1"
type: "gene"
col: 386
ensembl_id: "ENSG00000028528"
name: "sorting nexin 1"
location: "15q22.31"
module: 45
arm: "+"
pooled_cpm: 93.3
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# SNX1

*sorting nexin 1* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.89× (z +14.5, q 4e-45, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.786× (z -5.5, q 3e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC11A]] (+0.81, fdr 7e-06), [[FOXJ3]] (+0.77, fdr 7e-06), [[UNC45A]] (+0.72, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.69, fdr 2e-05), [[CYREN]] (-0.68, fdr 1e-05), [[ST7L]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC2A9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +14.5 | 4e-45 | 47/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +13.9 | 3e-41 | 45/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +13.3 | 5e-38 | 46/48 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +10.7 | 2e-24 | 35/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +10.4 | 2e-23 | 44/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +8.5 | 2e-15 | 36/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +7.4 | 9e-12 | 32/48 (HEC-1-A, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +7.3 | 1e-11 | 32/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +6.6 | 4e-09 | 33/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +5.5 | 3e-06 | 32/48 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.4 | 3e-06 | 20/48 (HT-29, RKO, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.25×** | +5.1 | 2e-05 | 23/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.21×** | +4.3 | 9e-04 | 23/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.003 | 20/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.004 | 22/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.025 | 18/48 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.025 | 16/47 (SW48, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.068 | 11/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.099 | 8/49 (HOP62, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 386.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.786×** | -5.5 | 3e-05 | 29/48 (A-427, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.797×** | -5.2 | 7e-05 | 27/48 (COLO 205, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.813×** | -4.7 | 5e-04 | 27/48 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.893× | -3.6 | 0.040 | 5/48 (SNU-1, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.5 | 0.057 | 14/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.860× | -3.3 | 0.091 | 21/44 (NCI-H1573, SW 900, …) | rises with dose | composition shift |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.866× | -3.3 | 0.091 | 11/48 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.13 | 11/49 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.13 | 12/48 (LS 180, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 97.4 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +19.6) | — |
| [[PANC-1 (line)]] | alt | 78.2 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +12.5) | — |
| [[LoVo (line)]] | wt | 96.0 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +14.5) | — |
| [[NCI-H460 (line)]] | wt | 71.4 | 6 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.03× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +15.4) | — |
| [[LS 180 (line)]] | wt | 77.8 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +11.3) | — |
| [[J82 (line)]] | alt | 74.4 | 4 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.11× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 76.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 109 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.526× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 84.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.50× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 98.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 107 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.61× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.16× (z +8.7) | — |
| [[A-427 (line)]] | wt | 53.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 159 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 82.8 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.42× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 72.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 151 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.38× (z +9.9) | — |
| [[A-172 (line)]] | wt | 73.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.13× (z +9.0) | — |
| [[A549 (line)]] | wt | 114 | 1 | 0 | [[Belinostat (drug)]] 5 µM 1.89× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.221× (z -10.2) |
| [[H4 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.149× (z -8.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 104 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.95× (z +8.5) | — |
| [[KATO III (line)]] | alt | 92.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 104 | 1 | 0 | [[Belinostat (drug)]] 5 µM 1.92× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 64.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.15× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 94.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 95.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.07× (z +11.2) | — |
| [[A498 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC11A]] | +0.81 | +0.85 / +0.68 | both halves | 7e-06 |  |
| [[FOXJ3]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.72 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[MARCHF6]] | +0.70 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[MED23]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[SLC25A23]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[FBXO3]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[MED30]] | +0.69 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.68 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[MED17]] | +0.68 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.68 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[PMS2P3]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.69 | -0.74 / -0.48 | both halves | 2e-05 |  |
| [[CYREN]] | -0.68 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[ST7L]] | -0.67 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.66 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[SLC2A9]] | -0.66 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[FBXO30]] | -0.65 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.64 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.63 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.63 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[LZIC]] | -0.63 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[SSUH2]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[MED1]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A9]] | B | SLC2A9 activity raises SNX1's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.31× lower at baseline in the lines without SLC2A9 | 0.061 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-3.8, -13.4); signed map (-33.7, -9.5). **Vector** length 114, 33.8% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.5 | +14.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.0 | +13.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +13.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +0.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.1 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.6 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.8 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.1 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.1 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.8 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,094,123-64,146,090 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNX1A, MGC8664, HsT17379, Vps5 |
| Gene groups (HGNC) | Sorting nexins; PX-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13596](https://www.uniprot.org/uniprotkb/Q13596) (Sorting nexin-1):

> Involved in several stages of intracellular trafficking. Interacts with membranes containing phosphatidylinositol 3-phosphate (PtdIns(3P)) or phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2). Acts in part as component of the retromer membrane-deforming SNX-BAR subcomplex. The SNX-BAR retromer mediates retrograde transport of cargo proteins from endosomes to the trans-Golgi network (TGN) and is involved in endosome-to-plasma membrane transport for cargo protein recycling. The SNX-BAR …

**Summary**, from NCBI Gene [6642](https://www.ncbi.nlm.nih.gov/gene/6642):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This endosomal protein regulates the cell-surface expression of epidermal growth factor receptor. This protein also has a role in sorting protease-activated receptor-1 from early endosomes to lysosomes. This protein may form oligomeric complexes with family members. This gene results in three …

**Accessions** — [HGNC:11172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11172) · Entrez [6642](https://www.ncbi.nlm.nih.gov/gene/6642) · UniProt [Q13596](https://www.uniprot.org/uniprotkb/Q13596) · Ensembl [ENSG00000028528](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000028528)

## Data

Gene col 386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 386); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 386]; `tensor/DDL_lfc|DDL_z.npy` [386]; `embed/gene_vectors.npy` [386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 386 or target_col == 386). Every well: [[SNX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

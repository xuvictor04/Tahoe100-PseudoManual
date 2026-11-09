---
symbol: "ABHD15"
type: "gene"
col: 9700
ensembl_id: "ENSG00000168792"
name: "abhydrolase domain containing 15"
location: "17q11.2"
module: 7
arm: "+"
pooled_cpm: 2.56
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ABHD15

*abhydrolase domain containing 15* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.96× (z +15.4, q 0e+00, up in 29 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.376× (z -7.8, q 4e-12, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENDOG]] (+0.63, fdr 8e-05), [[ABHD14A]] (+0.59, fdr 6e-05), [[TRIM7]] (+0.59, fdr 1e-04); moves opposite to [[UFSP2]] (-0.51, fdr 7e-05), [[STAM2]] (-0.50, fdr 9e-05), [[HUS1]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TP53I13]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.96×** | +15.4 | 0e+00 | 29/31 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.61×** | +9.8 | 4e-20 | 22/27 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +8.4 | 8e-15 | 2/3 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +6.7 | 4e-09 | 21/32 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.6 | 6e-04 | 5/44 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +4.4 | 0.001 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.001 | 8/44 (C-33 A, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.76×** | +4.3 | 0.001 | 7/15 (LS 180, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +4.2 | 0.002 | 1/14 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +3.6 | 0.015 | 11/41 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.015 | 5/26 (KATO III, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.3 | 0.045 | 8/45 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Belumosudil (drug)]] 5 µM |  | 1.49× | +3.0 | 0.11 | 6/33 (COLO 205, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.376×** | -7.8 | 4e-12 | 30/46 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.459×** | -6.0 | 7e-07 | 20/39 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.523×** | -5.2 | 4e-05 | 20/41 (NCI-H2030, LS 180, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.639×** | -5.1 | 6e-05 | 19/32 (A-172, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -5.0 | 6e-05 | 15/28 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.546×** | -4.8 | 1e-04 | 14/38 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.573×** | -4.4 | 7e-04 | 17/42 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.586×** | -4.3 | 0.001 | 13/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -3.4 | 0.041 | 9/24 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.457×** | -3.3 | 0.063 | 10/28 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.474×** | -3.1 | 0.097 | 11/36 (NCI-H460, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.10 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +9.8) | [[Harringtonine (drug)]] 5 µM 0.0607× (z -10.3) |
| [[A-172 (line)]] | wt | 2.85 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0479× (z -12.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0443× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 4.32 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0595× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 3.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0985× (z -8.5) |
| [[HT-29 (line)]] | alt | 3.20 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0398× (z -9.2) |
| [[PANC-1 (line)]] | alt | 4.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 0.737 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.849 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 16 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENDOG]] | +0.63 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[ABHD14A]] | +0.59 | +0.39 / +0.61 | both halves | 6e-05 | same gene group; STRING 530 |
| [[TRIM7]] | +0.59 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[ALDH1A3-AS1]] | +0.59 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[GATD1-DT]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[OXLD1]] | +0.58 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[SLC12A9]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MRPL20-AS1]] | +0.57 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[ZNF48]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MLYCD]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MILIP]] | +0.54 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[POC1B-AS1]] | +0.54 | +0.39 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFSP2]] | -0.51 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[STAM2]] | -0.50 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[HUS1]] | -0.48 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[PTAR1]] | -0.48 | -0.21 / -0.62 | both halves | 6e-04 |  |
| [[GRIPAP1]] | -0.47 | -0.22 / -0.49 | both halves | 6e-04 |  |
| [[SAR1B]] | -0.47 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[KPNA5]] | -0.46 | -0.24 / -0.48 | both halves | 5e-04 |  |
| [[AAAS]] | -0.46 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[CCDC144BP]] | -0.46 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[ATM]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[MAP9]] | -0.45 | -0.03 / -0.39 | ⚠ not reproduced | 0.006 |  |
| [[RPAP3]] | -0.45 | -0.13 / -0.31 | ⚠ not reproduced | 0.002 |  |
| [[COPE]] | -0.44 | -0.49 / -0.21 | both halves | 7e-04 |  |
| [[MAP3K13]] | -0.44 | -0.33 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABHD15's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TP53I13]] | C | TP53I13 activity raises ABHD15's level | lines that do not express TP53I13 (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without TP53I13 | 0.008 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC25A37; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53I13]] | C | ABHD15's natural level strengthens TP53I13's drug response | ABHD15's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.34; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.229). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-3.6, 19.0); signed map (17.6, -6.7). **Vector** length 45.4, 5.64% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +15.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +9.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +6.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +0.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.8 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.0 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -7.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.9 | +0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:29,560,547-29,567,037 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXT9](https://www.uniprot.org/uniprotkb/Q6UXT9) (Protein ABHD15):

> May regulate adipocyte lipolysis and liver lipid accumulation.

**Summary**, from NCBI Gene [116236](https://www.ncbi.nlm.nih.gov/gene/116236):

> Predicted to enable monoacylglycerol lipase activity and short-chain carboxylesterase activity. Predicted to be involved in adipose tissue development and lipid catabolic process. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26971) · Entrez [116236](https://www.ncbi.nlm.nih.gov/gene/116236) · UniProt [Q6UXT9](https://www.uniprot.org/uniprotkb/Q6UXT9) · Ensembl [ENSG00000168792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168792)

## Data

Gene col 9700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9700); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9700]; `tensor/DDL_lfc|DDL_z.npy` [9700]; `embed/gene_vectors.npy` [9700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9700 or target_col == 9700). Every well: [[ABHD15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

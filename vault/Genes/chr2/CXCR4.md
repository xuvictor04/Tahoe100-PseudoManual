---
symbol: "CXCR4"
type: "gene"
col: 4311
ensembl_id: "ENSG00000121966"
name: "C-X-C motif chemokine receptor 4"
location: "2q22.1"
module: 1
arm: "-"
pooled_cpm: 6.6
n_lines_expressing: 28
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CXCR4

*C-X-C motif chemokine receptor 4* — 2q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.29× (z +21.2, q 0e+00, up in 22 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 0.743× (z -3.8, q 0.031, down in 6 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF122]] (+0.57, fdr 2e-05), [[TMEM51]] (+0.55, fdr 2e-05), [[NMB]] (+0.53, fdr 3e-05); moves opposite to [[TCERG1]] (-0.61, fdr 9e-06), [[ACSF3]] (-0.61, fdr 4e-05), [[YLPM1]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[NAA15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.29×** | +21.2 | 0e+00 | 22/25 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +10.0 | 6e-21 | 18/22 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +8.3 | 1e-14 | 12/21 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +8.3 | 2e-14 | 16/26 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.9 | 7e-10 | 9/26 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +6.0 | 2e-07 | 15/23 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.86×** | +5.6 | 2e-06 | 7/17 (J82, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +5.4 | 4e-06 | 0/9 | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.5 | 0.031 | 8/25 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.2 | 0.068 | 3/16 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.087 | 4/24 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.087 | 8/25 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.93×** | +3.1 | 0.087 | 9/24 (BT-474, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.091 | 5/25 (A498, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.091 | 7/25 (MIA PaCa-2, J82, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.031 | 6/26 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.660×** | -3.8 | 0.031 | 10/24 (A498, Hs 766T, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.660×** | -3.8 | 0.031 | 12/25 (NCI-H23, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.682×** | -3.5 | 0.058 | 13/22 (SHP-77, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.682×** | -3.5 | 0.058 | 6/24 (A498, NCI-H1792, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.716× | -3.0 | 0.22 | 6/24 (A498, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 54.8 | 0 | 14 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0600× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.148× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 16.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[HEC-1-A (line)]] | alt | 17.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 3.75 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.89× (z +10.2) | [[Menadione (drug)]] 0.05 µM 0.0670× (z -8.7) |
| [[SW480 (line)]] | alt | 7.54 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +11.5) | — |
| [[A-172 (line)]] | wt | 1.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.6× (z +10.2) | — |
| [[A549 (line)]] | wt | 3.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.6× (z +11.9) | — |
| [[J82 (line)]] | alt | 5.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +10.1) | — |
| [[LoVo (line)]] | wt | 3.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.62× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0966× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[SHP-77 (line)]] | alt | 9.80 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 8.76 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0938× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[SW 900 (line)]] | alt | 3.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.84× (z +8.7) | — |
| [[A-427 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.786 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF122]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TMEM51]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[NMB]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 | pathway: Class A/1 (Rhodopsin-like receptors) |
| [[SLC5A3]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[INTS6L]] | +0.52 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[OTUB2]] | +0.52 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[MRPS6]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[TNFRSF11A]] | +0.50 | +0.46 / +0.61 | both halves | 3e-05 | same gene group |
| [[IPMK]] | +0.50 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[HLA-A]] | +0.49 | +0.38 / +0.53 | both halves | 7e-05 | pathway: HIV Infection |
| [[GTF2B]] | +0.49 | +0.39 / +0.45 | both halves | 5e-05 | pathway: HIV Infection |
| [[TPI1]] | +0.49 | +0.47 / +0.40 | both halves | 5e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*63 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCERG1]] | -0.61 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[ACSF3]] | -0.61 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[YLPM1]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[FKTN]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[JPX]] | -0.54 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[RAD54L2]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[COMT]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[WDR70]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[YTHDC2]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[CCDC113]] | -0.52 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TSEN15]] | -0.52 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[FAN1]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CXCR4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAA15]] | B | CXCR4 activity lowers NAA15's level | lines that do not express CXCR4 (22) vs lines expressing it (28) | 1.28× higher at baseline in the lines without CXCR4 | 0.026 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, LMO2 |
| [[PLRG1]] | B | CXCR4 activity lowers PLRG1's level | lines that do not express CXCR4 (22) vs lines expressing it (28) | 1.19× higher at baseline in the lines without CXCR4 | 0.035 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, LMO2 |
| [[NMB]] | B | CXCR4 activity raises NMB's level | lines that do not express CXCR4 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without CXCR4 | 0.073 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, LMO2 |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.1, -40.6); signed map (-4.1, 49.9). **Vector** length 57.7, 12.0% of its response variance represented; |z| ≥ 3 in 647 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +21.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.8 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | -2.5 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.8 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | C-X-C motif chemokine receptor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.1 — chr2:136,114,349-136,119,177 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LESTR, NPY3R, HM89, NPYY3R, D2S201E, fusin, HSY3RR, NPYR |
| Gene groups (HGNC) | CD molecules; C-X-C motif chemokine receptors |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, KRAS_SIGNALING_UP, GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 19 pathways, smallest: Specification of primordial germ cells; Formation of definitive endoderm; Early Phase of HIV Life Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P61073](https://www.uniprot.org/uniprotkb/P61073) (C-X-C chemokine receptor type 4):

> Receptor for the C-X-C chemokine CXCL12/SDF-1 that transduces a signal by increasing intracellular calcium ion levels and enhancing MAPK1/MAPK3 activation. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. CXCR4 is coupled to G(i) G alpha proteins and mediates inhibition of adenylate cyclase. Involved in the AKT signaling cascade. Plays a role in …

**Summary**, from NCBI Gene [7852](https://www.ncbi.nlm.nih.gov/gene/7852):

> This gene encodes a CXC chemokine receptor specific for stromal cell-derived factor-1. The protein has 7 transmembrane regions and is located on the cell surface. It acts with the CD4 protein to support HIV entry into cells and is also highly expressed in breast cancer cells. Mutations in this gene have been associated with WHIM (warts, hypogammaglobulinemia, infections, and myelokathexis) syndrome. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. …

**Accessions** — [HGNC:2561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2561) · Entrez [7852](https://www.ncbi.nlm.nih.gov/gene/7852) · UniProt [P61073](https://www.uniprot.org/uniprotkb/P61073) · Ensembl [ENSG00000121966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121966)

## Data

Gene col 4311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4311); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4311]; `tensor/DDL_lfc|DDL_z.npy` [4311]; `embed/gene_vectors.npy` [4311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4311 or target_col == 4311). Every well: [[CXCR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXCR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

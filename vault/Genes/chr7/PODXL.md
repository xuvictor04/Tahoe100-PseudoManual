---
symbol: "PODXL"
type: "gene"
col: 4893
ensembl_id: "ENSG00000128567"
name: "podocalyxin like"
location: "7q32.3"
module: 78
arm: "+"
pooled_cpm: 129.21
n_lines_expressing: 26
n_dd_up: 15
n_dd_down: 26
n_dd_up_clean: 11
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# PODXL

*podocalyxin like* — 7q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +10.9, q 9e-25, up in 18 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.47× (z +9.1, q 2e-17, up in 9 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.538× (z -14.6, q 1e-45, down in 23 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFRP1]] (+0.67, fdr 1e-05), [[NMNAT2]] (+0.67, fdr 7e-06), [[KCNC4]] (+0.65, fdr 7e-06); moves opposite to [[COA6]] (-0.53, fdr 4e-05), [[NNMT]] (-0.52, fdr 3e-05), [[SPART-AS1]] (-0.52, fdr 5e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[HHIP]] → it (grade B ⚠); 7 go from it, the strongest it → [[GALNT12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +10.9 | 9e-25 | 18/25 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +10.5 | 1e-23 | 16/20 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +9.1 | 2e-17 | 9/24 (SW1417, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +7.2 | 8e-11 | 9/22 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 2e-06 | 7/24 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +5.6 | 2e-06 | 8/24 (SW1417, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 4e-05 | 6/24 (RPMI-7951, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 0.002 | 6/24 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Cyclosporin A (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.005 | 15/24 (SNU-423, RPMI-7951, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.26×** | +3.8 | 0.007 | 2/23 (AsPC-1, KATO III) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.014 | 6/24 (RPMI-7951, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ferulic acid (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.032 | 7/23 (SW1417, A-172, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.044 | 9/24 (PANC-1, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.056 | 3/24 (SW1417, Panc 03.27, …) | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.061 | 1/23 (RPMI-7951) | inconsistent across doses | position effect removed |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.061 | 7/23 (A-172, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -14.6 | 1e-45 | 23/25 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.724×** | -7.6 | 7e-12 | 17/24 (SK-MEL-2, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -6.5 | 2e-08 | 4/25 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -5.8 | 9e-07 | 14/24 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.794×** | -5.5 | 5e-06 | 19/24 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.731×** | -5.2 | 1e-05 | 16/24 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.740×** | -5.2 | 2e-05 | 14/26 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.767×** | -4.4 | 6e-04 | 15/24 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.756×** | -4.4 | 6e-04 | 14/24 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.769×** | -4.4 | 6e-04 | 16/24 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.786×** | -3.9 | 0.005 | 12/24 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.780×** | -3.8 | 0.006 | 9/24 (HOP62, J82, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.852× | -3.8 | 0.006 | 13/24 (A549, NCI-H1792, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.804×** | -3.6 | 0.011 | 13/24 (Hs 766T, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.800×** | -3.6 | 0.011 | 12/24 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.6 | 0.011 | 9/24 (Panc 03.27, SNU-423, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.808×** | -3.6 | 0.012 | 10/24 (A-172, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 180 | 0 | 18 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -19.8) |
| [[J82 (line)]] | alt | 528 | 0 | 17 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -22.4) |
| [[A-172 (line)]] | wt | 1,845 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0685× (z -35.2) |
| [[Hs 766T (line)]] | wt | 912 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -23.6) |
| [[SK-MEL-2 (line)]] | alt | 42.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 382 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -19.5) |
| [[RKO (line)]] | wt | 45.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.2) |
| [[A549 (line)]] | wt | 46.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -12.5) |
| [[HT-29 (line)]] | alt | 110 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -13.5) |
| [[LoVo (line)]] | wt | 73.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.338× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 96.5 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.467× (z -16.2) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.3) |
| [[NCI-H596 (line)]] | alt | 64.9 | 0 | 2 | — | [[Methylthiouracil (drug)]] 5 µM 0.176× (z -9.5) |
| [[PANC-1 (line)]] | alt | 37.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 45.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -9.9) |
| [[SW 1271 (line)]] | alt | 105 | 0 | 2 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0575× (z -9.4) |
| [[KATO III (line)]] | alt | 51.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -11.7) |
| [[SW1417 (line)]] | alt | 55.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -9.5) |
| [[SW48 (line)]] | wt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -10.4) |
| [[A-427 (line)]] | wt | 21.9 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 24.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 31.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 31.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 30.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 28.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.93 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 23.7 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 27.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 25.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFRP1]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[NMNAT2]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[KCNC4]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CSMD2]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PLXNA1]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[CD44]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[NES]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ITGA3]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 | STRING 429 |
| [[ECE1]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 | STRING 441 |
| [[GRK5]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[STMN3]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA6]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NNMT]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SPART-AS1]] | -0.52 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[GTF2IRD2B]] | -0.52 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[N4BP2L2]] | -0.51 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[ZCCHC8]] | -0.50 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[CNPY2]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HHIP]] | B | HHIP activity raises PODXL's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.12× lower at baseline in the lines without HHIP | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[RGS4]] | B | RGS4 activity raises PODXL's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.43× lower at baseline in the lines without RGS4 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[EMP1]] | B | EMP1 activity raises PODXL's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 2.68× lower at baseline in the lines without EMP1 | 0.085 | ⚠ within organs, on part of the lines |
| [[RASA3]] | B | RASA3 activity raises PODXL's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.99× lower at baseline in the lines without RASA3 | 0.087 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[LINC02813]] | B | LINC02813 activity raises PODXL's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without LINC02813 | 0.090 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[C13orf46]] | B | C13orf46 activity raises PODXL's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 2.85× lower at baseline in the lines without C13orf46 | 0.094 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[CMKLR2]] | B | CMKLR2 activity raises PODXL's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.10× lower at baseline in the lines without CMKLR2 | 0.097 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[PLP2]] | C | PLP2 activity raises PODXL's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 2.70× lower at baseline in the lines without PLP2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |
| [[KCNK3]] | C | KCNK3 activity raises PODXL's level | lines that do not express KCNK3 (30) vs lines expressing it (20) | 2.08× lower at baseline in the lines without KCNK3 | 0.099 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, IGFN1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT12]] | B | PODXL activity raises GALNT12's level | lines that do not express PODXL (24) vs lines expressing it (26) | 3.00× lower at baseline in the lines without PODXL | 0.002 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |
| [[ITPR3]] | B | PODXL activity raises ITPR3's level | lines that do not express PODXL (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without PODXL | 0.003 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |
| [[SLCO4A1]] | B | PODXL activity raises SLCO4A1's level | lines that do not express PODXL (24) vs lines expressing it (26) | 2.56× lower at baseline in the lines without PODXL | 0.007 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |
| [[CD44]] | B | PODXL activity raises CD44's level | lines that do not express PODXL (24) vs lines expressing it (26) | 2.92× lower at baseline in the lines without PODXL | 0.013 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |
| [[S100A16]] | B | PODXL activity raises S100A16's level | lines that do not express PODXL (24) vs lines expressing it (26) | 2.45× lower at baseline in the lines without PODXL | 0.056 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |
| [[FXYD5]] | B | PODXL activity raises FXYD5's level | lines that do not express PODXL (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without PODXL | 0.069 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |
| [[NT5E]] | B | PODXL activity raises NT5E's level | lines that do not express PODXL (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without PODXL | 0.085 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.7, 10.9); signed map (5.3, 47.2). **Vector** length 94.8, 27.6% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +9.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.7 | +1.7 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.3 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -14.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.9 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.8 | -7.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | podocalyxin like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.3 — chr7:131,500,262-131,558,217 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCLP, Gp200, PC, PODXL1, PDX, gp135 |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [O00592](https://www.uniprot.org/uniprotkb/O00592) (Podocalyxin):

> Involved in the regulation of both adhesion and cell morphology and cancer progression. Functions as an anti-adhesive molecule that maintains an open filtration pathway between neighboring foot processes in the podocyte by charge repulsion. Acts as a pro-adhesive molecule, enhancing the adherence of cells to immobilized ligands, increasing the rate of migration and cell-cell contacts in an integrin-dependent manner. Induces the formation of apical actin-dependent microvilli. Involved in the …

**Summary**, from NCBI Gene [5420](https://www.ncbi.nlm.nih.gov/gene/5420):

> This gene encodes a member of the sialomucin protein family. The encoded protein was originally identified as an important component of glomerular podocytes. Podocytes are highly differentiated epithelial cells with interdigitating foot processes covering the outer aspect of the glomerular basement membrane. Other biological activities of the encoded protein include: binding in a membrane protein complex with Na+/H+ exchanger regulatory factor to intracellular cytoskeletal elements, playing a …

**Accessions** — [HGNC:9171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9171) · Entrez [5420](https://www.ncbi.nlm.nih.gov/gene/5420) · UniProt [O00592](https://www.uniprot.org/uniprotkb/O00592) · Ensembl [ENSG00000128567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128567)

## Data

Gene col 4893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4893); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4893]; `tensor/DDL_lfc|DDL_z.npy` [4893]; `embed/gene_vectors.npy` [4893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4893 or target_col == 4893). Every well: [[PODXL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PODXL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

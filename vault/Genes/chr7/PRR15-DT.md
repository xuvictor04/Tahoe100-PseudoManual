---
symbol: "PRR15-DT"
type: "gene"
col: 13367
ensembl_id: "ENSG00000223813"
name: "PRR15 divergent transcript"
location: "7p14.3"
module: 44
arm: "+"
pooled_cpm: 8.07
n_lines_expressing: 25
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 49
direction_downstream: 44
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PRR15-DT

*PRR15 divergent transcript* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +13.8, q 7e-41, up in 13 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.300× (z -12.1, q 5e-31, down in 21 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR15]] (+0.78, fdr 7e-06, ⚠ same locus), [[PRR15L]] (+0.77, fdr 7e-06), [[UGT1A9]] (+0.74, fdr 7e-06), [[UGT1A8]] (+0.71, fdr 7e-06); moves opposite to [[ZNF471]] (-0.50, fdr 5e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 44 go from it, the strongest it → [[PRRG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +13.8 | 7e-41 | 13/20 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +6.9 | 2e-09 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.0 | 5e-07 | 2/15 (AsPC-1, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +5.8 | 1e-06 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.003 | 14/22 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.004 | 14/22 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.008 | 4/20 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.038 | 4/22 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.038 | 2/20 (SW480, SW1417) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.038 | 8/22 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.038 | 9/22 (AsPC-1, PANC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.081 | 4/20 (CFPAC-1, Panc 03.27, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13367.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.300×** | -12.1 | 5e-31 | 21/23 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.359×** | -10.3 | 1e-22 | 21/22 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.434×** | -8.4 | 7e-15 | 18/20 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -7.6 | 5e-12 | 19/21 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.498×** | -7.0 | 2e-10 | 19/22 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.531×** | -6.4 | 2e-08 | 14/23 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.665×** | -5.8 | 5e-07 | 15/20 (KATO III, COLO 205, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.573×** | -5.4 | 5e-06 | 14/23 (HT-29, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.588×** | -5.4 | 5e-06 | 14/23 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.640×** | -4.5 | 4e-04 | 14/22 (COLO 205, PANC-1, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.633×** | -4.4 | 5e-04 | 8/23 (Hs 766T, KATO III, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.642×** | -4.2 | 0.001 | 10/22 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.693×** | -3.7 | 0.010 | 13/22 (LoVo, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -3.7 | 0.010 | 10/20 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.698×** | -3.6 | 0.011 | 16/21 (SW1417, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.715×** | -3.4 | 0.026 | 16/22 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.734×** | -3.1 | 0.061 | 4/23 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.804×** | -3.1 | 0.063 | 11/22 (HT-29, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.737×** | -3.1 | 0.064 | 8/23 (HT-29, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -16.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0399× (z -15.9) |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 11 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0205× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0561× (z -16.0) |
| [[KATO III (line)]] | alt | 49.7 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -22.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -15.0) |
| [[LoVo (line)]] | wt | 44.6 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -17.3) |
| [[Hs 766T (line)]] | wt | 41.2 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0438× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0533× (z -13.2) |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -11.8) |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -16.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0911× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.100× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.174× (z -8.9) |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0709× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0941× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 3.15 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0540× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.0948× (z -8.8) |
| [[BT-474 (line)]] | alt | 9.53 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0318× (z -13.2) |
| [[A-172 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR15]] | +0.78 | +0.80 / +0.72 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[PRR15L]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[UGT1A9]] | +0.74 | +0.69 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A8]] | +0.71 | +0.65 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[CYP4F12]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[UGT1A1]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[HSD17B2]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[HNF1A-AS1]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[UGT1A6]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[PIP5K1B]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ABO]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TJP3]] | +0.65 | +0.71 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF471]] | -0.50 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 4, C 45. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers PRR15-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[PTPRB]] | B | PTPRB activity raises PRR15-DT's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without PTPRB | 0.039 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[RSPH1]] | B | RSPH1 activity raises PRR15-DT's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 2.53× lower at baseline in the lines without RSPH1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PRR15-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PRR15]] | C | PRR15 activity raises PRR15-DT's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 4.22× lower at baseline in the lines without PRR15 | 8e-04 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C; co-absent with the target |
| [[SORL1]] | C | SORL1 activity raises PRR15-DT's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 3.61× lower at baseline in the lines without SORL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3; co-absent with the target |
| [[PRR15L]] | C | PRR15L activity raises PRR15-DT's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 4.94× lower at baseline in the lines without PRR15L | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881; co-absent with the target |
| [[FXYD3]] | C | FXYD3 activity raises PRR15-DT's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 3.93× lower at baseline in the lines without FXYD3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2; co-absent with the target |
| [[ST8SIA6]] | C | ST8SIA6 activity raises PRR15-DT's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 3.06× lower at baseline in the lines without ST8SIA6 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2; co-absent with the target |
| [[CYP4F12]] | C | CYP4F12 activity raises PRR15-DT's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.50× lower at baseline in the lines without CYP4F12 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises PRR15-DT's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 5.30× lower at baseline in the lines without LGALS4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises PRR15-DT's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 4.01× lower at baseline in the lines without FAM3D | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 10, C 34. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRG2]] | B | PRR15-DT activity raises PRRG2's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without PRR15-DT | 0.009 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[MROH7]] | B | PRR15-DT activity raises MROH7's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 2.50× lower at baseline in the lines without PRR15-DT | 0.009 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[ZNF883]] | B | PRR15-DT activity lowers ZNF883's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 2.49× higher at baseline in the lines without PRR15-DT | 0.018 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[LINC02580]] | B | PRR15-DT activity raises LINC02580's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without PRR15-DT | 0.019 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[RSPH1]] | B | PRR15-DT activity raises RSPH1's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without PRR15-DT | 0.020 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[LINC01290]] | B | PRR15-DT activity raises LINC01290's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without PRR15-DT | 0.061 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[PRR16]] | B | PRR15-DT activity lowers PRR16's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 4.80× higher at baseline in the lines without PRR15-DT | 0.065 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| cells under [[Sodium Salicylate (drug)]] 0.5 µM | B | PRR15-DT activity raises the cells' numbers under Sodium Salicylate 0.5 µM (protects the cells) | lines that do not express PRR15-DT (25) vs lines expressing it (23) | the lines without PRR15-DT: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[PLAC8]] | B | PRR15-DT activity raises PLAC8's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 2.83× lower at baseline in the lines without PRR15-DT | 0.081 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[BCL2L15]] | B | PRR15-DT activity raises BCL2L15's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without PRR15-DT | 0.091 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[SORL1]] | C | PRR15-DT activity raises SORL1's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 7.44× lower at baseline in the lines without PRR15-DT | 3e-04 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[PRR15]] | C | PRR15-DT activity raises PRR15's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 4.05× lower at baseline in the lines without PRR15-DT | 0.001 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.3, 51.6); signed map (63.2, 4.3). **Vector** length 73.4, 21.9% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.70 to 4); *Aspirin ADME* (reactome, mean cos +0.70 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +13.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +5.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.3 | +2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +4.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.1 | +1.6 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -3.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | PRR15 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p14.3 — chr7:29,514,224-29,563,721 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AC007255.8 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55866) · Entrez [107986700](https://www.ncbi.nlm.nih.gov/gene/107986700) · Ensembl [ENSG00000223813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223813)

## Data

Gene col 13367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13367); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13367]; `tensor/DDL_lfc|DDL_z.npy` [13367]; `embed/gene_vectors.npy` [13367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13367 or target_col == 13367). Every well: [[PRR15-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR15-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

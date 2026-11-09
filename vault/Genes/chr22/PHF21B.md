---
symbol: "PHF21B"
type: "gene"
col: 637
ensembl_id: "ENSG00000056487"
name: "PHD finger protein 21B"
location: "22q13.31"
module: 102
arm: "+"
pooled_cpm: 15.67
n_lines_expressing: 29
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 15
direction_downstream: 16
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# PHF21B

*PHD finger protein 21B* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.77× (z +27.0, q 0e+00, up in 23 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.717× (z -6.3, q 2e-07, down in 16 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEGF11]] (+0.65, fdr 1e-05), [[MED12L]] (+0.64, fdr 7e-06), [[SDK2]] (+0.62, fdr 1e-05); moves opposite to [[TMEM254]] (-0.56, fdr 2e-05), [[SENP2]] (-0.48, fdr 3e-05), [[C6orf89]] (-0.47, fdr 3e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 16 go from it, the strongest it → [[ANKRD13B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +27.0 | 0e+00 | 23/26 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +15.0 | 0e+00 | 15/27 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +12.9 | 8e-36 | 13/25 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +11.6 | 1e-28 | 20/26 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +11.3 | 1e-27 | 15/24 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +8.6 | 9e-16 | 14/24 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +8.2 | 2e-14 | 16/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.5 | 4e-12 | 10/24 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +7.2 | 4e-11 | 15/26 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +6.2 | 4e-08 | 3/23 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.8 | 3e-07 | 8/27 (NCI-H460, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +5.8 | 3e-07 | 16/26 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.7 | 5e-07 | 10/26 (HOP62, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +5.7 | 6e-07 | 12/26 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +5.2 | 6e-06 | 11/26 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.006 | 5/26 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.010 | 2/25 (SNU-1, SW1417) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.015 | 3/25 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.055 | 3/24 (NCI-H1792, AN3 CA, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.717×** | -6.3 | 2e-07 | 16/26 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -5.7 | 4e-06 | 3/27 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.764×** | -5.1 | 7e-05 | 19/24 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.771×** | -4.9 | 1e-04 | 12/25 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.658×** | -4.1 | 0.004 | 9/24 (NCI-H661, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.813×** | -3.9 | 0.008 | 8/27 (NCI-H2030, BT-474, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.787×** | -3.8 | 0.011 | 12/24 (C32, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.829×** | -3.5 | 0.026 | 17/26 (NCI-H460, NCI-H23, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.830×** | -3.5 | 0.026 | 2/26 (AN3 CA, C32) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.831×** | -3.5 | 0.026 | 0/27 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.831×** | -3.2 | 0.063 | 3/26 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.070 | 0/26 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.892× | -3.1 | 0.093 | 10/26 (C32, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.853× | -3.0 | 0.11 | 12/26 (NCI-H23, BT-474, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.38 | 9 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.10× (z +18.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -12.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[C32 (line)]] | wt | 91.9 | 2 | 7 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H23 (line)]] | alt | 51.8 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.301× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 61.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -17.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 115 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0452× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0599× (z -14.7) |
| [[HOP62 (line)]] | alt | 4.56 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 28.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -16.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 28.2 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.3) | [[Docetaxel (drug)]] 0.05 µM 0.293× (z -12.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0334× (z -29.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.01 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 5.51× (z +10.1) | — |
| [[A549 (line)]] | wt | 23.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -10.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0819× (z -12.2) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 51.9 | 0 | 2 (1 ⚠) | — | [[venetoclax (drug)]] 5 µM 0.0769× (z -9.2) |
| [[A-427 (line)]] | wt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 73.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.325× (z -8.6) ⚠ cell-cycle shift, explains ~13% of this change |
| [[H4 (line)]] | wt | 19.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.00× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -8.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SW 900 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +10.5) | — |
| [[A-172 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEGF11]] | +0.65 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MED12L]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SDK2]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[RBPMS2]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[LINC00937]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[RASGEF1C]] | +0.56 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LHX2]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ADGRB1]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MSI1]] | +0.55 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[DOCK3]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ADCY1]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SYN2]] | +0.54 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM254]] | -0.56 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[SENP2]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[C6orf89]] | -0.47 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[SLC35B3]] | -0.44 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[THAP6]] | -0.44 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[TRIQK]] | -0.43 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 4, C 11. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PHF21B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC16A10]] | B | SLC16A10 activity raises PHF21B's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 2.91× lower at baseline in the lines without SLC16A10 | 0.042 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |
| [[BRSK2]] | B | BRSK2 activity raises PHF21B's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 3.33× lower at baseline in the lines without BRSK2 | 0.059 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[ADGRB1]] | B | ADGRB1 activity raises PHF21B's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 3.33× lower at baseline in the lines without ADGRB1 | 0.074 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[RET]] | C | RET activity raises PHF21B's level | lines that do not express RET (28) vs lines expressing it (22) | 4.39× lower at baseline in the lines without RET | 0.008 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[GNAO1]] | C | GNAO1 activity raises PHF21B's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 3.81× lower at baseline in the lines without GNAO1 | 0.009 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17; co-absent with the target |
| [[KIF26A]] | C | KIF26A activity raises PHF21B's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 3.86× lower at baseline in the lines without KIF26A | 0.012 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises PHF21B's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 3.96× lower at baseline in the lines without DPYSL5 | 0.015 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises PHF21B's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 4.26× lower at baseline in the lines without KIF1A | 0.016 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[LMX1B]] | C | LMX1B activity raises PHF21B's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 5.06× lower at baseline in the lines without LMX1B | 0.019 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |
| [[CECR2]] | C | CECR2 activity raises PHF21B's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 4.71× lower at baseline in the lines without CECR2 | 0.041 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent; co-absent with the target |
| [[KCNQ2]] | C | KCNQ2 activity raises PHF21B's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 3.13× lower at baseline in the lines without KCNQ2 | 0.044 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 5, C 11. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD13B]] | B | PHF21B activity raises ANKRD13B's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without PHF21B | 0.014 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |
| [[PACS1]] | B | PHF21B activity raises PACS1's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 1.22× lower at baseline in the lines without PHF21B | 0.037 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |
| [[MEX3A]] | B | PHF21B activity raises MEX3A's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 1.75× lower at baseline in the lines without PHF21B | 0.091 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |
| [[GLDC]] | B | PHF21B activity raises GLDC's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without PHF21B | 0.094 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |
| [[MFHAS1]] | B | PHF21B activity lowers MFHAS1's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 1.20× higher at baseline in the lines without PHF21B | 0.097 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |
| [[LMX1B]] | C | PHF21B activity raises LMX1B's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 3.14× lower at baseline in the lines without PHF21B | 0.008 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[PDZD4]] | C | PHF21B activity raises PDZD4's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 3.13× lower at baseline in the lines without PHF21B | 0.008 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[CECR2]] | C | PHF21B activity raises CECR2's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 3.83× lower at baseline in the lines without PHF21B | 0.025 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[RAB6B]] | C | PHF21B activity raises RAB6B's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 2.76× lower at baseline in the lines without PHF21B | 0.037 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[KIF26A]] | C | PHF21B activity raises KIF26A's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without PHF21B | 0.041 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[KIF1A]] | C | PHF21B activity raises KIF1A's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 4.93× lower at baseline in the lines without PHF21B | 0.044 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[MGAT5B]] | C | PHF21B activity raises MGAT5B's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 2.70× lower at baseline in the lines without PHF21B | 0.051 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.0, 36.9); signed map (27.9, 25.4). **Vector** length 67.6, 15.9% of its response variance represented; |z| ≥ 3 in 650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +27.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +12.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +3.9 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.3 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -3.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 21B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:44,881,162-45,010,005 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BHC80L, FLJ34161; previously PHF4 |
| Gene groups (HGNC) | PHD finger proteins |
| Matched by | ensembl_id |

UniProt [Q96EK2](https://www.uniprot.org/uniprotkb/Q96EK2) carries no function annotation.

**Summary**, from NCBI Gene [112885](https://www.ncbi.nlm.nih.gov/gene/112885):

> Predicted to enable zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25161) · Entrez [112885](https://www.ncbi.nlm.nih.gov/gene/112885) · UniProt [Q96EK2](https://www.uniprot.org/uniprotkb/Q96EK2) · Ensembl [ENSG00000056487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056487)

## Data

Gene col 637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 637); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 637]; `tensor/DDL_lfc|DDL_z.npy` [637]; `embed/gene_vectors.npy` [637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 637 or target_col == 637). Every well: [[PHF21B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF21B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

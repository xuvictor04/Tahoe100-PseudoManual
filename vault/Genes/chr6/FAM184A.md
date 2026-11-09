---
symbol: "FAM184A"
type: "gene"
col: 3299
ensembl_id: "ENSG00000111879"
name: "family with sequence similarity 184 member A"
location: "6q22.31"
module: 102
arm: "+"
pooled_cpm: 8.01
n_lines_expressing: 37
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 13
direction_downstream: 14
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# FAM184A

*family with sequence similarity 184 member A* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.40× (z +22.9, q 0e+00, up in 21 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.530× (z -8.4, q 1e-14, down in 20 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS3]] (+0.65, fdr 7e-06), [[MED12L]] (+0.62, fdr 1e-05), [[LINC00937]] (+0.61, fdr 2e-05); moves opposite to [[DNAJC16]] (-0.50, fdr 2e-04), [[EIF2B1]] (-0.48, fdr 3e-04), [[C6orf89]] (-0.48, fdr 3e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ANKS1B]] → it (grade B ⚠); 14 go from it, the strongest it → [[SUGCT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +22.9 | 0e+00 | 21/28 (A498, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.07×** | +21.0 | 0e+00 | 34/34 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.17×** | +15.3 | 0e+00 | 30/34 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.92×** | +14.2 | 2e-43 | 29/34 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.74×** | +13.3 | 2e-38 | 22/34 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +13.1 | 2e-37 | 19/29 (SHP-77, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +12.5 | 6e-34 | 18/28 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +12.4 | 2e-33 | 24/34 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.23×** | +10.6 | 2e-24 | 20/34 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +10.0 | 8e-22 | 18/29 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.30×** | +8.3 | 7e-15 | 20/32 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.74×** | +6.8 | 5e-10 | 5/15 (NCI-H2347, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.58×** | +6.1 | 6e-08 | 4/21 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +5.7 | 5e-07 | 15/29 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.55×** | +5.5 | 1e-06 | 5/12 (LoVo, CFPAC-1, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.46×** | +5.0 | 2e-05 | 9/34 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.9 | 3e-05 | 8/32 (SW480, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +4.8 | 6e-05 | 9/32 (LoVo, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3299.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.530×** | -8.4 | 1e-14 | 20/34 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.531×** | -8.4 | 1e-14 | 21/34 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -7.5 | 2e-11 | 20/33 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -7.3 | 4e-11 | 17/28 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.670×** | -5.3 | 1e-05 | 12/32 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.698×** | -4.8 | 2e-04 | 11/34 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.575×** | -3.8 | 0.010 | 7/27 (LoVo, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.759×** | -3.7 | 0.017 | 10/34 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.601×** | -3.5 | 0.026 | 13/32 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.784×** | -3.2 | 0.066 | 8/33 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.5 | 5 | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.23× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.117× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -16.6) |
| [[A-427 (line)]] | wt | 49.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -10.2) |
| [[C-33 A (line)]] | alt | 59.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0256× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0851× (z -11.3) |
| [[A498 (line)]] | wt | 8.26 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 2.28 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.92× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 4.38 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +10.5) | [[Digitoxin (drug)]] 0.5 µM 0.0638× (z -10.4) |
| [[SW480 (line)]] | alt | 2.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.08× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 9.70 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0801× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 4.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +10.5) | — |
| [[J82 (line)]] | alt | 9.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +8.5) | — |
| [[LoVo (line)]] | wt | 18.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.50× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 6.02 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0923× (z -8.8) |
| [[SHP-77 (line)]] | alt | 54.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 3.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.61× (z +8.5) | — |
| [[A-172 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.961 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS3]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[MED12L]] | +0.62 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.61 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[CDH23]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 | same gene group |
| [[KLHL13]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[DPYSL5]] | +0.59 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[GNAL]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[LRIG3-DT]] | +0.58 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[TEX15]] | +0.58 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[ASIC2]] | +0.58 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[NTRK3]] | +0.57 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[DPY19L2P1]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC16]] | -0.50 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[EIF2B1]] | -0.48 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[C6orf89]] | -0.48 | -0.31 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKS1B]] | B | ANKS1B activity raises FAM184A's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.86× lower at baseline in the lines without ANKS1B | 0.013 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[TOP2A]] | B | TOP2A activity lowers FAM184A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC6A17]] | B | SLC6A17 activity raises FAM184A's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 2.29× lower at baseline in the lines without SLC6A17 | 0.030 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT |
| [[ADAM22]] | B | ADAM22 activity raises FAM184A's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.01× lower at baseline in the lines without ADAM22 | 0.036 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[DOCK3]] | B | DOCK3 activity raises FAM184A's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without DOCK3 | 0.051 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[CHD5]] | B | CHD5 activity raises FAM184A's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.26× lower at baseline in the lines without CHD5 | 0.052 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[RIMS2]] | B | RIMS2 activity raises FAM184A's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 2.18× lower at baseline in the lines without RIMS2 | 0.056 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[KATNAL2]] | B | KATNAL2 activity raises FAM184A's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.55× lower at baseline in the lines without KATNAL2 | 0.060 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[SCN8A]] | B | SCN8A activity raises FAM184A's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without SCN8A | 0.071 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[MED12L]] | B | MED12L activity raises FAM184A's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.40× lower at baseline in the lines without MED12L | 0.073 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[CACNA1B]] | B | CACNA1B activity raises FAM184A's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without CACNA1B | 0.089 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[CTNNA2]] | B | CTNNA2 activity raises FAM184A's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.07× lower at baseline in the lines without CTNNA2 | 0.095 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUGCT]] | B | FAM184A activity raises SUGCT's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.63× lower at baseline in the lines without FAM184A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[RIMS2]] | B | FAM184A activity raises RIMS2's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 3.84× lower at baseline in the lines without FAM184A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[FAXC]] | B | FAM184A activity raises FAXC's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without FAM184A | 0.013 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[FAM171B]] | B | FAM184A activity raises FAM171B's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without FAM184A | 0.026 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[SCN8A]] | B | FAM184A activity raises SCN8A's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.90× lower at baseline in the lines without FAM184A | 0.035 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[B3GALT1]] | B | FAM184A activity raises B3GALT1's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without FAM184A | 0.046 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[DOCK3]] | B | FAM184A activity raises DOCK3's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.60× lower at baseline in the lines without FAM184A | 0.052 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[TLE2]] | B | FAM184A activity raises TLE2's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without FAM184A | 0.055 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[ATP6V1E2]] | B | FAM184A activity raises ATP6V1E2's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without FAM184A | 0.072 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[NEGR1]] | B | FAM184A activity raises NEGR1's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without FAM184A | 0.074 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[ADAM22]] | B | FAM184A activity raises ADAM22's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without FAM184A | 0.083 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[GPLD1]] | B | FAM184A activity raises GPLD1's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without FAM184A | 0.084 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.4, 34.7); signed map (28.4, 25.9). **Vector** length 55.7, 9.31% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +21.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +5.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.2 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +8.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -8.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.7 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -8.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | +0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 184 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:118,959,763-119,149,387 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13942; previously C6orf60 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q8NB25](https://www.uniprot.org/uniprotkb/Q8NB25) carries no function annotation.

**Summary**, from NCBI Gene [79632](https://www.ncbi.nlm.nih.gov/gene/79632):

> Located in P-body; centriolar satellite; and ciliary basal body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20991) · Entrez [79632](https://www.ncbi.nlm.nih.gov/gene/79632) · UniProt [Q8NB25](https://www.uniprot.org/uniprotkb/Q8NB25) · Ensembl [ENSG00000111879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111879)

## Data

Gene col 3299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3299); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3299]; `tensor/DDL_lfc|DDL_z.npy` [3299]; `embed/gene_vectors.npy` [3299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3299 or target_col == 3299). Every well: [[FAM184A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM184A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

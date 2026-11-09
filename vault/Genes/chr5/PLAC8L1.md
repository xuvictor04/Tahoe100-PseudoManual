---
symbol: "PLAC8L1"
type: "gene"
col: 10362
ensembl_id: "ENSG00000173261"
name: "PLAC8 like 1"
location: "5q32"
module: 39
arm: "+"
pooled_cpm: 4.8
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# PLAC8L1

*PLAC8 like 1* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +9.7, q 2e-19, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.338× (z -9.2, q 2e-17, down in 29 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.449× (z -6.8, q 2e-09, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKDD1B]] (+0.84, fdr 7e-06), [[SLC2A9]] (+0.83, fdr 7e-06), [[MSH4]] (+0.82, fdr 1e-05); moves opposite to [[HMGN3]] (-0.66, fdr 1e-04), [[FAM102B]] (-0.65, fdr 5e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DDR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +9.7 | 2e-19 | 36/41 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.92×** | +9.1 | 3e-17 | 36/45 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **2.57×** | +8.0 | 2e-13 | 36/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +7.2 | 8e-11 | 26/40 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +7.0 | 3e-10 | 2/5 (HOP62, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +6.5 | 5e-09 | 21/38 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.5 | 5e-09 | 14/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.7 | 7e-07 | 21/47 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.78×** | +4.6 | 2e-04 | 15/45 (A-427, Hs 766T, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.72×** | +4.6 | 2e-04 | 18/46 (LOX-IMVI, LS 180, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.6 | 3e-04 | 15/41 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +4.2 | 0.001 | 2/8 (HS-578T, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.001 | 17/41 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.58×** | +3.9 | 0.004 | 9/42 (HEC-1-A, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.006 | 13/45 (HS-578T, AN3 CA, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.007 | 12/47 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.025 | 8/46 (NCI-H1792, A498, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.48×** | +3.1 | 0.064 | 2/35 (MIA PaCa-2, KATO III) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10362.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.338×** | -9.2 | 2e-17 | 29/39 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.439×** | -7.0 | 7e-10 | 31/47 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.449×** | -6.8 | 2e-09 | 27/45 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -6.8 | 2e-09 | 29/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.542×** | -5.2 | 2e-05 | 19/40 (SK-MEL-2, A498, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.328×** | -5.0 | 7e-05 | 14/33 (RKO, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.690× | -3.0 | 0.19 | 19/45 (C-33 A, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 12.0 | 0 | 2 | — | [[Macitentan (drug)]] 0.05 µM 0.0679× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 6.61 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.108× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 5.26 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0385× (z -11.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0658× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 6.49 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0820× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Omeprazole (drug)]] 0.5 µM 0.0957× (z -8.5) |
| [[LoVo (line)]] | wt | 5.35 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0773× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 5.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0762× (z -11.3) |
| [[RKO (line)]] | wt | 11.0 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0796× (z -9.0) |
| [[A-172 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKDD1B]] | +0.84 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.83 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[MSH4]] | +0.82 | +0.87 / +0.57 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | +0.81 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[ARL9]] | +0.80 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.79 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.77 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.77 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.76 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.76 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[USP50]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN3]] | -0.66 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[FAM102B]] | -0.65 | -0.68 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDR2]] | B | DDR2 activity raises PLAC8L1's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without DDR2 | 0.009 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PLAC8L1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AOX1]] | B | AOX1 activity raises PLAC8L1's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.29× lower at baseline in the lines without AOX1 | 0.047 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ZNF382]] | B | ZNF382 activity raises PLAC8L1's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without ZNF382 | 0.060 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[PXMP4]] | B | PXMP4 activity lowers PLAC8L1's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without PXMP4 | 0.073 | ⚠ within organs, on part of the lines; also absent: ZNF532 |
| [[VWA1]] | B | VWA1 activity lowers PLAC8L1's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 1.31× higher at baseline in the lines without VWA1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[MPP4]] | C | MPP4 activity raises PLAC8L1's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.94× lower at baseline in the lines without MPP4 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.9, -12.8); signed map (16.9, 4.6). **Vector** length 82.4, 15.1% of its response variance represented; |z| ≥ 3 in 1,430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +9.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +8.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.7 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -9.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -2.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | PLAC8 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:146,084,313-146,105,577 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PLAC8 family |
| Matched by | ensembl_id |

UniProt [A1L4L8](https://www.uniprot.org/uniprotkb/A1L4L8) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31746) · Entrez [153770](https://www.ncbi.nlm.nih.gov/gene/153770) · UniProt [A1L4L8](https://www.uniprot.org/uniprotkb/A1L4L8) · Ensembl [ENSG00000173261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173261)

## Data

Gene col 10362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10362); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10362]; `tensor/DDL_lfc|DDL_z.npy` [10362]; `embed/gene_vectors.npy` [10362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10362 or target_col == 10362). Every well: [[PLAC8L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAC8L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

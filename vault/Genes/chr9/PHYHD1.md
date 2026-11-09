---
symbol: "PHYHD1"
type: "gene"
col: 10590
ensembl_id: "ENSG00000175287"
name: "phytanoyl-CoA dioxygenase domain containing 1"
location: "9q34.11"
module: 38
arm: "+"
pooled_cpm: 3.63
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PHYHD1

*phytanoyl-CoA dioxygenase domain containing 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.03× (z +23.9, q 0e+00, up in 33 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.440× (z -6.6, q 2e-08, down in 23 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00672]] (+0.79, fdr 7e-06), [[VWCE]] (+0.77, fdr 7e-06), [[FNDC7]] (+0.76, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.03×** | +23.9 | 0e+00 | 33/34 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.26×** | +11.3 | 4e-27 | 16/28 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.22×** | +9.1 | 2e-17 | 26/34 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +7.1 | 2e-10 | 0/5 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +6.5 | 7e-09 | 1/8 (HOP62) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +6.0 | 2e-07 | 9/19 (J82, A498, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.75×** | +4.5 | 5e-04 | 16/46 (Hs 766T, SW48, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +4.4 | 7e-04 | 8/36 (A-172, HEC-1-A, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.65×** | +4.1 | 0.002 | 8/23 (SW480, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.031 | 10/44 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.073 | 14/46 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.078 | 5/27 (KATO III, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 5 µM |  | 1.45× | +3.0 | 0.12 | 5/44 (SW48, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.440×** | -6.6 | 2e-08 | 23/40 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.557×** | -4.7 | 7e-04 | 20/46 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -4.3 | 0.004 | 15/30 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.387×** | -4.0 | 0.009 | 9/27 (KATO III, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.621×** | -3.6 | 0.043 | 7/44 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.647×** | -3.4 | 0.071 | 13/38 (Hs 766T, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.458×** | -3.3 | 0.079 | 5/21 (A498, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -3.3 | 0.079 | 8/45 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -3.2 | 0.100 | 13/42 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.762× | -3.1 | 0.12 | 11/42 (COLO 205, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.686× | -3.0 | 0.13 | 17/39 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0306× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.218× (z -8.9) |
| [[SW480 (line)]] | alt | 7.17 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0978× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 3.44 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.0883× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 6.02 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0641× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 1.46 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.4× (z +13.2) | — |
| [[A-172 (line)]] | wt | 2.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +10.9) | — |
| [[A498 (line)]] | wt | 2.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.84× (z +10.6) | — |
| [[A549 (line)]] | wt | 1.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.7× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 3.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +9.8) | — |
| [[C32 (line)]] | wt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +10.3) | — |
| [[J82 (line)]] | alt | 3.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.93× (z +9.7) | — |
| [[KATO III (line)]] | alt | 9.92 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.143× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 2.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 1.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.4× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 6.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 1.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.3× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +8.7) | — |
| [[A-427 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00672]] | +0.79 | +0.70 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[VWCE]] | +0.77 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[PYGM]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.74 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[TEX29]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.73 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.73 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[SLC22A13]] | +0.72 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[ADCY10P1]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.72 | +0.65 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PHYHD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LMO7DN]] | B | LMO7DN activity raises PHYHD1's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without LMO7DN | 0.044 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[SEMA4A]] | B | SEMA4A activity raises PHYHD1's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.74× lower at baseline in the lines without SEMA4A | 0.060 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[ADORA1]] | B | ADORA1 activity lowers PHYHD1's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.97× higher at baseline in the lines without ADORA1 | 0.063 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[TNNT2]] | B | TNNT2 activity raises PHYHD1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.49× lower at baseline in the lines without TNNT2 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[MLIP]] | B | MLIP activity raises PHYHD1's level | lines that do not express MLIP (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without MLIP | 0.085 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SCAT1]] | B | SCAT1 activity raises PHYHD1's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.46× lower at baseline in the lines without SCAT1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.814). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, -18.3); signed map (13.9, 12.2). **Vector** length 83.3, 15.8% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +23.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +4.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | phytanoyl-CoA dioxygenase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,920,966-128,942,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16638 |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SRE7](https://www.uniprot.org/uniprotkb/Q5SRE7) (Phytanoyl-CoA dioxygenase domain-containing protein 1):

> 2-oxoglutarate(2OG)-dependent dioxygenase that catalyzes the conversion of 2-oxoglutarate to succinate and CO(2) in an iron-dependent manner. However, does not couple 2OG turnover to the hydroxylation of acyl-coenzyme A derivatives, implying that it is not directly involved in phytanoyl coenzyme-A metabolism. Does not show detectable activity towards fatty acid CoA thioesters.; [Isoform 2]: Isoform 2 probably lacks enzyme activity.; [Isoform 3]: Isoform 3 probably lacks enzyme activity.

**Summary**, from NCBI Gene [254295](https://www.ncbi.nlm.nih.gov/gene/254295):

> Enables 2-oxoglutarate-dependent dioxygenase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23396) · Entrez [254295](https://www.ncbi.nlm.nih.gov/gene/254295) · UniProt [Q5SRE7](https://www.uniprot.org/uniprotkb/Q5SRE7) · Ensembl [ENSG00000175287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175287)

## Data

Gene col 10590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10590); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10590]; `tensor/DDL_lfc|DDL_z.npy` [10590]; `embed/gene_vectors.npy` [10590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10590 or target_col == 10590). Every well: [[PHYHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHYHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

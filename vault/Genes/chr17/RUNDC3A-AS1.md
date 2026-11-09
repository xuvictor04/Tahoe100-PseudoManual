---
symbol: "RUNDC3A-AS1"
type: "gene"
col: 15575
ensembl_id: "ENSG00000267750"
name: "RUNDC3A antisense RNA 1"
location: "17q21.31"
module: 53
arm: "+"
pooled_cpm: 3.86
n_lines_expressing: 45
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# RUNDC3A-AS1

*RUNDC3A antisense RNA 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.95× (z +26.7, q 0e+00, up in 27 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.653× (z -5.0, q 3e-04, down in 17 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AZU1]] (+0.66, fdr 7e-06), [[CDKL2]] (+0.66, fdr 7e-06), [[CELF5]] (+0.65, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FBXO27]] → it (grade B ⚠); 4 go from it, the strongest it → [[CHRNE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.95×** | +26.7 | 0e+00 | 27/30 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.14×** | +13.5 | 4e-39 | 28/40 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.66×** | +11.5 | 2e-28 | 24/39 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +9.8 | 2e-20 | 4/5 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +9.7 | 3e-20 | 12/22 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +8.1 | 4e-14 | 18/40 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +8.1 | 4e-14 | 21/41 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +7.9 | 3e-13 | 13/27 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +7.5 | 4e-12 | 16/35 (HEC-1-A, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.4 | 8e-09 | 18/39 (A498, HT-29, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +5.8 | 4e-07 | 1/6 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +5.3 | 4e-06 | 9/30 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +5.3 | 4e-06 | 12/31 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.3 | 4e-06 | 11/29 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.003 | 8/31 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.006 | 5/25 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Acetohexamide (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.006 | 3/33 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +3.5 | 0.011 | 4/36 (MIA PaCa-2, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -5.0 | 3e-04 | 17/37 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -4.8 | 5e-04 | 16/37 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.697×** | -4.3 | 0.003 | 14/42 (NCI-H23, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.698×** | -4.3 | 0.003 | 12/28 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ferulic acid (drug)]] 0.05 µM |  | **0.734×** | -3.4 | 0.080 | 8/32 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.610× | -3.1 | 0.21 | 2/25 (Panc 03.27, SW480) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.45 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.252× (z -8.6) |
| [[A-172 (line)]] | wt | 3.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.26× (z +9.3) | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.212× (z -8.6) |
| [[A498 (line)]] | wt | 3.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +10.4) | — |
| [[A549 (line)]] | wt | 3.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 8.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +8.9) | — |
| [[LoVo (line)]] | wt | 3.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.83× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0717× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 1.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +12.1) | — |
| [[SW480 (line)]] | alt | 3.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.972 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AZU1]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[CDKL2]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CELF5]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.64 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[MASP2]] | +0.62 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ELAVL3]] | +0.62 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[ADORA1]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CASKIN1]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[RSPH9]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[GRAMD2A]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[HYAL1]] | +0.58 | +0.47 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO27]] | B | FBXO27 activity raises RUNDC3A-AS1's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 2.07× lower at baseline in the lines without FBXO27 | 0.016 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2 |
| [[TOP2A]] | B | TOP2A activity lowers RUNDC3A-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRNE]] | B | RUNDC3A-AS1 activity raises CHRNE's level | lines that do not express RUNDC3A-AS1 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without RUNDC3A-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ERO1B, TEX14, TCTN1; maybe low, not absent; its own permutation p |
| [[MYO15A]] | B | RUNDC3A-AS1 activity raises MYO15A's level | lines that do not express RUNDC3A-AS1 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without RUNDC3A-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ERO1B, TEX14, TCTN1; maybe low, not absent; its own permutation p |
| [[PILRA]] | B | RUNDC3A-AS1 activity raises PILRA's level | lines that do not express RUNDC3A-AS1 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without RUNDC3A-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ERO1B, TEX14, TCTN1; maybe low, not absent |
| [[SYCE2]] | B | RUNDC3A-AS1 activity raises SYCE2's level | lines that do not express RUNDC3A-AS1 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without RUNDC3A-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ERO1B, TEX14, TCTN1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.2, -19.1); signed map (13.2, 16.4). **Vector** length 50.4, 6.58% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +26.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +7.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.2 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -2.2 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.0 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RUNDC3A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.31 — chr17:44,299,574-44,315,315 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [101926996](https://www.ncbi.nlm.nih.gov/gene/101926996):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:51344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51344) · Entrez [101926996](https://www.ncbi.nlm.nih.gov/gene/101926996) · Ensembl [ENSG00000267750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267750)

## Data

Gene col 15575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15575); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15575]; `tensor/DDL_lfc|DDL_z.npy` [15575]; `embed/gene_vectors.npy` [15575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15575 or target_col == 15575). Every well: [[RUNDC3A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUNDC3A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

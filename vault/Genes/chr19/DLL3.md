---
symbol: "DLL3"
type: "gene"
col: 1644
ensembl_id: "ENSG00000090932"
name: "delta like canonical Notch ligand 3"
location: "19q13.2"
module: 24
arm: "+"
pooled_cpm: 7.99
n_lines_expressing: 22
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# DLL3

*delta like canonical Notch ligand 3* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.00× (z +9.9, q 2e-20, up in 10 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 1.78× (z +3.7, q 0.018, up in 7 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.144×, NCI-H2347 0.175×, NCI-H661 0.166×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (PANC-1 0.168×, SHP-77 0.185×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0682×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.209×).
> Its strongest partners by |cos| (62 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 42 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PITPNA-AS1]] (+0.61, fdr 3e-05), [[DCTN6-DT]] (+0.58, fdr 6e-05), [[MNX1]] (+0.57, fdr 6e-05); moves opposite to [[ELK4]] (-0.49, fdr 4e-04), [[ALMS1]] (-0.47, fdr 1e-04), [[FLII]] (-0.47, fdr 3e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FHIP1A]] → it (grade B ⚠); 6 go from it, the strongest it → [[EID2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.00×** | +9.9 | 2e-20 | 10/11 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.16×** | +8.8 | 5e-16 | 4/6 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +5.3 | 2e-05 | 4/6 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +4.5 | 0.001 | 5/12 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.87×** | +4.0 | 0.007 | 4/13 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.78×** | +3.7 | 0.018 | 7/15 (SHP-77, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.018 | 6/15 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.77×** | +3.6 | 0.019 | 6/18 (PANC-1, HOP62, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.024 | 8/18 (PANC-1, SW480, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.055 | 5/17 (PANC-1, C32, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.144×, NCI-H2347 0.175×, NCI-H661 0.166×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (PANC-1 0.168×, SHP-77 0.185×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0682×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.209×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H661 (line)]] | alt | 48.7 | 0 | 2 (1 ⚠) | — | [[Thymol (drug)]] 0.5 µM 0.0682× (z -9.1) |
| [[PANC-1 (line)]] | alt | 89.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -10.2) |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 8.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 38 of them with an alert (⚠; 35 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNA-AS1]] | +0.61 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[DCTN6-DT]] | +0.58 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[MNX1]] | +0.57 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[ZNF232-AS1]] | +0.56 | +0.18 / +0.69 | ⚠ one half (not replicated) | 1e-03 |  |
| [[MINCR]] | +0.55 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[GAMT]] | +0.53 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[FLVCR1-DT]] | +0.53 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[PPP1R14A]] | +0.52 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[TNNI3]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[C19orf81]] | +0.52 | +0.13 / +0.58 | ⚠ one half (not replicated) | 0.002 |  |
| [[ANTKMT]] | +0.52 | +0.19 / +0.59 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TMEM160]] | +0.51 | +0.24 / +0.56 | both halves | 5e-04 |  |
| [[ADGRL3-AS1]] | +0.50 | +0.24 / +0.54 | both halves | 4e-04 |  |
| [[ZFAND2A-DT]] | +0.50 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[SRRM3]] | +0.49 | +0.31 / +0.55 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK4]] | -0.49 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[ALMS1]] | -0.47 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[FLII]] | -0.47 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[ZMPSTE24]] | -0.45 | -0.18 / -0.46 | ⚠ not reproduced | 9e-04 |  |
| [[CERS2]] | -0.45 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[PSMC3]] | -0.45 | -0.27 / -0.48 | both halves | 3e-04 | pathway: Formation of paraxial mesoderm |
| [[MSANTD7]] | -0.45 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[PSME3]] | -0.44 | -0.21 / -0.47 | both halves | 6e-04 | STRING 493 |
| [[ACADVL]] | -0.43 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[KLC2]] | -0.43 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[LIN7C]] | -0.43 | -0.13 / -0.50 | ⚠ one half (not replicated) | 0.002 |  |
| [[SF3B4]] | -0.43 | -0.17 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[PGRMC1]] | -0.43 | -0.26 / -0.42 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FHIP1A]] | B | FHIP1A activity lowers DLL3's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 3.17× higher at baseline in the lines without FHIP1A | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | DLL3 activity raises EID2B's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without DLL3 | 0.026 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |
| [[PTRHD1]] | B | DLL3 activity raises PTRHD1's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 1.32× lower at baseline in the lines without DLL3 | 0.039 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |
| [[TMEM150C]] | B | DLL3 activity raises TMEM150C's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without DLL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |
| [[FHIP1A]] | B | DLL3 activity lowers FHIP1A's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 2.01× higher at baseline in the lines without DLL3 | 0.063 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |
| [[FBXO33]] | B | DLL3 activity lowers FBXO33's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 1.04× higher at baseline in the lines without DLL3 | 0.084 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |
| [[FBXO27]] | C | DLL3 activity raises FBXO27's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 3.37× lower at baseline in the lines without DLL3 | 0.044 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA; co-absent with the target |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.9, -22.1); signed map (-29.5, 7.2). **Vector** length 28.1, 5.61% of its response variance represented; |z| ≥ 3 in 241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.8 | +1.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | +0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | delta like canonical Notch ligand 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,498,895-39,508,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCDO1 |
| Gene groups (HGNC) | Canonical Notch ligands |
| Reactome | 3 pathways, smallest: Somitogenesis; Formation of paraxial mesoderm; Gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYJ7](https://www.uniprot.org/uniprotkb/Q9NYJ7) (Delta-like protein 3):

> Inhibits primary neurogenesis. May be required to divert neurons along a specific differentiation pathway. Plays a role in the formation of somite boundaries during segmentation of the paraxial mesoderm (By similarity).

**Summary**, from NCBI Gene [10683](https://www.ncbi.nlm.nih.gov/gene/10683):

> This gene encodes a member of the delta protein ligand family. This family functions as Notch ligands that are characterized by a DSL domain, EGF repeats, and a transmembrane domain. Mutations in this gene cause autosomal recessive spondylocostal dysostosis 1. Two transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2909) · Entrez [10683](https://www.ncbi.nlm.nih.gov/gene/10683) · UniProt [Q9NYJ7](https://www.uniprot.org/uniprotkb/Q9NYJ7) · Ensembl [ENSG00000090932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090932)

## Data

Gene col 1644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1644); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1644]; `tensor/DDL_lfc|DDL_z.npy` [1644]; `embed/gene_vectors.npy` [1644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1644 or target_col == 1644). Every well: [[DLL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

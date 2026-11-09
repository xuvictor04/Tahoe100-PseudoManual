---
symbol: "MYLK-AS1"
type: "gene"
col: 14199
ensembl_id: "ENSG00000239523"
name: "MYLK antisense RNA 1"
location: "3q21.1"
module: 124
arm: "+"
pooled_cpm: 6.22
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 1
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# MYLK-AS1

*MYLK antisense RNA 1* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.41× (z +15.2, q 0e+00, up in 36 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.715× (z -4.0, q 0.039, down in 12 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.141×, C-33 A 0.0912×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.1000×; ⚠ toxic; cell-cycle shift, explains ~8% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.274×; ⚠ cell-cycle shift, explains ~26% of this change); [[Artesunate (drug)]] 0.5 µM in 1 line (COLO 205 0.0547×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SW1417 0.0917×).
> Its strongest partners by |cos| (43 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 57 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT7-DT]] (+0.73, fdr 4e-04), [[ADCK1]] (+0.69, fdr 7e-05), [[ANKRD18B]] (+0.68, fdr 4e-04); moves opposite to [[SLC27A1]] (-0.64, fdr 0.003, ⚠ one half only (not replicated)), [[BAIAP3]] (-0.60, fdr 5e-04), [[GNAI2]] (-0.60, fdr 0.008, ⚠ one half only (not replicated)), [[RALY]] (-0.58, fdr 3e-05), [[STAU1]] (-0.57, fdr 6e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +15.2 | 0e+00 | 36/42 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +11.3 | 3e-27 | 33/38 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +8.9 | 1e-16 | 19/29 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +8.0 | 1e-13 | 23/42 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +7.9 | 2e-13 | 31/43 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +7.5 | 5e-12 | 16/27 (Panc 03.27, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +7.3 | 3e-11 | 21/46 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.8 | 9e-10 | 8/11 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.62×** | +5.8 | 3e-07 | 18/47 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.7 | 7e-07 | 19/48 (SW1417, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +5.7 | 7e-07 | 19/46 (BT-474, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +5.3 | 5e-06 | 15/44 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.1 | 1e-05 | 17/45 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.9 | 4e-05 | 13/47 (HEC-1-A, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 5e-04 | 11/39 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +4.3 | 6e-04 | 14/45 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.003 | 10/47 (SW480, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +3.8 | 0.004 | 4/45 (SK-MEL-2, NCI-H460, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.011 | 4/46 (C-33 A, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14199.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.141×, C-33 A 0.0912×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.1000×; ⚠ toxic; cell-cycle shift, explains ~8% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.274×; ⚠ cell-cycle shift, explains ~26% of this change); [[Artesunate (drug)]] 0.5 µM in 1 line (COLO 205 0.0547×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SW1417 0.0917×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -4.0 | 0.039 | 12/46 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.763× | -3.4 | 0.22 | 5/47 (SW48, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.769× | -3.1 | 0.29 | 16/46 (HCT15, PANC-1, …) | two highest doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.754× | -3.1 | 0.29 | 7/46 (NCI-H661, KATO III, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.627× | -3.0 | 0.29 | 5/34 (SW480, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 5.35 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +9.1) | [[Cobimetinib (drug)]] 0.05 µM 0.0917× (z -8.5) |
| [[SW480 (line)]] | alt | 7.27 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.6) | — |
| [[A-427 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.1000× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0912× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 4.64 | 0 | 1 | — | [[Artesunate (drug)]] 0.5 µM 0.0547× (z -8.6) |
| [[RKO (line)]] | wt | 5.49 | 0 | 1 (1 ⚠) | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.0732× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 51 of them with an alert (⚠; 51 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT7-DT]] | +0.73 | +0.78 / +0.26 | both halves | 4e-04 |  |
| [[ADCK1]] | +0.69 | +0.73 / +0.38 | both halves | 7e-05 |  |
| [[ANKRD18B]] | +0.68 | +0.60 / +0.24 | both halves | 4e-04 |  |
| [[YARS2]] | +0.66 | +0.49 / +0.28 | both halves | 3e-04 |  |
| [[PLS3-AS1]] | +0.65 | +0.74 / +0.25 | both halves | 4e-04 | same gene group |
| [[OXA1L-DT]] | +0.65 | +0.66 / +0.25 | both halves | 4e-04 |  |
| [[EPM2A]] | +0.65 | +0.58 / +0.22 | both halves | 6e-04 |  |
| [[GABPB1-AS1]] | +0.64 | +0.64 / +0.18 | ⚠ one half (not replicated) | 0.001 | same gene group |
| [[DNAAF10]] | +0.64 | +0.68 / +0.34 | both halves | 1e-04 |  |
| [[CRPPA]] | +0.64 | +0.51 / +0.21 | both halves | 7e-04 |  |
| [[SPTY2D1OS]] | +0.64 | +0.71 / +0.25 | both halves | 4e-04 |  |
| [[DPH5-DT]] | +0.64 | +0.71 / +0.31 | both halves | 2e-04 |  |
| [[EFCAB5]] | +0.62 | +0.65 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | -0.64 | -0.62 / -0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[BAIAP3]] | -0.60 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[GNAI2]] | -0.60 | -0.57 / -0.01 | ⚠ one half (not replicated) | 0.008 |  |
| [[MAST3]] | -0.59 | -0.59 / +0.05 | ⚠ one half (not replicated) | 1.00 |  |
| [[ASL]] | -0.59 | -0.47 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[RALY]] | -0.58 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[HDAC11]] | -0.58 | -0.58 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[STAU1]] | -0.57 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[ASMTL]] | -0.57 | -0.33 / -0.23 | both halves | 5e-04 |  |
| [[NDFIP2]] | -0.57 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[ABTB1]] | -0.57 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[CEP131]] | -0.56 | -0.54 / -0.02 | ⚠ one half (not replicated) | 0.007 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYLK-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02057]] | B | LINC02057 activity lowers MYLK-AS1's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 1.39× higher at baseline in the lines without LINC02057 | 0.046 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[LINC00944]] | B | LINC00944 activity lowers MYLK-AS1's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.40× higher at baseline in the lines without LINC00944 | 0.089 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (5.0, 12.4); signed map (25.4, -12.3). **Vector** length 56.5, 7.78% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +15.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +3.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.1 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.5 | +4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | +4.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | +1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | MYLK antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q21.1 — chr3:123,585,143-123,644,568 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously MYLK-AS2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42440) · Entrez [100506826](https://www.ncbi.nlm.nih.gov/gene/100506826) · Ensembl [ENSG00000239523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239523)

## Data

Gene col 14199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14199); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14199]; `tensor/DDL_lfc|DDL_z.npy` [14199]; `embed/gene_vectors.npy` [14199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14199 or target_col == 14199). Every well: [[MYLK-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYLK-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

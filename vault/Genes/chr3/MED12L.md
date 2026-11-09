---
symbol: "MED12L"
type: "gene"
col: 6943
ensembl_id: "ENSG00000144893"
name: "mediator complex subunit 12L"
location: "3q25.1"
module: 102
arm: "+"
pooled_cpm: 22.55
n_lines_expressing: 32
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 21
direction_downstream: 22
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# MED12L

*mediator complex subunit 12L* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.79× (z +28.3, q 0e+00, up in 26 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.748× (z -4.2, q 0.015, down in 9 of 29 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.777× (z -3.6, q 0.058, down in 8 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00937]] (+0.67, fdr 7e-06), [[MEGF11]] (+0.67, fdr 7e-06), [[TEX15]] (+0.66, fdr 7e-06); moves opposite to [[LRRC27]] (-0.59, fdr 1e-05), [[RUFY1]] (-0.55, fdr 3e-05), [[TMEM254]] (-0.52, fdr 3e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 22 go from it, the strongest it → [[OLFM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.79×** | +28.3 | 0e+00 | 26/30 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.73×** | +23.3 | 0e+00 | 27/29 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.32×** | +22.0 | 0e+00 | 25/28 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +21.4 | 0e+00 | 23/29 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.57×** | +19.1 | 0e+00 | 20/29 (PANC-1, J82, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.40×** | +18.3 | 0e+00 | 21/29 (PANC-1, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.87×** | +15.8 | 0e+00 | 20/29 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.28×** | +12.3 | 4e-33 | 23/29 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.07×** | +11.0 | 2e-26 | 18/30 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +9.9 | 4e-21 | 18/28 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +7.2 | 3e-11 | 14/29 (HOP62, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.57×** | +6.5 | 4e-09 | 13/29 (A549, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +6.2 | 3e-08 | 13/22 (J82, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.47×** | +5.7 | 4e-07 | 13/29 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.0 | 2e-05 | 7/30 (A549, A-172, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 3e-04 | 5/29 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.006 | 3/29 (NCI-H2030, BT-474, …) | inconsistent across doses |  |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.008 | 4/30 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 1.17× | +3.4 | 0.016 | 3/30 (NCI-H23, A498, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.073 | 1/29 (HOP62) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6943.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.748×** | -4.2 | 0.015 | 9/29 (NCI-H2030, J82, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.842× | -3.7 | 0.058 | 5/30 (A549, H4, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.777×** | -3.6 | 0.058 | 8/29 (NCI-H23, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.790×** | -3.5 | 0.058 | 12/29 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.789×** | -3.4 | 0.088 | 8/29 (SW480, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.16 | 12/29 (NCI-H661, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.816× | -3.1 | 0.18 | 12/29 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 10.3 | 8 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.92× (z +12.3) | — |
| [[LoVo (line)]] | wt | 29.6 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -13.6) |
| [[J82 (line)]] | alt | 20.5 | 6 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.77× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 21.1 | 5 (3 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.54× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 24.3 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.71× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 8.96 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.24× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 5.85 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 7.68× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.36× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 80.9 | 0 | 4 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -15.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A-427 (line)]] | wt | 184 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 200 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 13.9 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.40× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.21× (z +11.6) | — |
| [[A-172 (line)]] | wt | 6.26 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.39× (z +8.6) | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0793× (z -9.1) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 284 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -9.7) |
| [[SNU-1 (line)]] | wt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[A498 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 17.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.66× (z +8.5) | — |
| [[C32 (line)]] | wt | 31.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.191× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 6.97 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.80× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 57.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 13.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.58× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00937]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MEGF11]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TEX15]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PHF21B]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SYN2]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[FAM184A]] | +0.62 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[ADCY1]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[SDK2]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GLDC]] | +0.60 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[MERTK]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[GNAO1]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[HS6ST2]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC27]] | -0.59 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[RUFY1]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[TMEM254]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[SPEF2]] | -0.50 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[DNAL4]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[BBOF1]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[FAM149B1]] | -0.49 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[WASHC3]] | -0.48 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[OGA]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[EXOC1]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[OSCP1]] | -0.47 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[PRMT2]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 8, C 13. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MED12L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC16A10]] | B | SLC16A10 activity raises MED12L's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without SLC16A10 | 0.039 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |
| [[OLFM2]] | B | OLFM2 activity raises MED12L's level | lines that do not express OLFM2 (14) vs lines expressing it (36) | 3.20× lower at baseline in the lines without OLFM2 | 0.056 | ⚠ within organs, on part of the lines; also absent: MGAT5B, JAM3, ANKS1B; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises MED12L's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.34× lower at baseline in the lines without MCOLN2 | 0.060 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[RHBDL3]] | B | RHBDL3 activity raises MED12L's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 3.77× lower at baseline in the lines without RHBDL3 | 0.071 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[ARHGAP44]] | B | ARHGAP44 activity raises MED12L's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.69× lower at baseline in the lines without ARHGAP44 | 0.078 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[GPC3]] | B | GPC3 activity raises MED12L's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 3.42× lower at baseline in the lines without GPC3 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2 |
| [[ENTREP2]] | B | ENTREP2 activity raises MED12L's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without ENTREP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[LHX2]] | C | LHX2 activity raises MED12L's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 3.91× lower at baseline in the lines without LHX2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR; co-absent with the target |
| [[GNAO1]] | C | GNAO1 activity raises MED12L's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 3.87× lower at baseline in the lines without GNAO1 | 0.018 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises MED12L's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 3.52× lower at baseline in the lines without DPYSL5 | 0.027 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[MSI1]] | C | MSI1 activity raises MED12L's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 3.08× lower at baseline in the lines without MSI1 | 0.030 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 11, C 11. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OLFM2]] | B | MED12L activity raises OLFM2's level | lines that do not express MED12L (18) vs lines expressing it (32) | 3.28× lower at baseline in the lines without MED12L | 0.004 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[RASGEF1C]] | B | MED12L activity raises RASGEF1C's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.20× lower at baseline in the lines without MED12L | 0.013 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[OTUD7A]] | B | MED12L activity raises OTUD7A's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.82× lower at baseline in the lines without MED12L | 0.013 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[MEGF11]] | B | MED12L activity raises MEGF11's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.18× lower at baseline in the lines without MED12L | 0.042 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[RHBDL3]] | B | MED12L activity raises RHBDL3's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without MED12L | 0.044 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[KCNQ2]] | B | MED12L activity raises KCNQ2's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without MED12L | 0.072 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[ENTREP2]] | B | MED12L activity raises ENTREP2's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.60× lower at baseline in the lines without MED12L | 0.072 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[FAM184A]] | B | MED12L activity raises FAM184A's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.40× lower at baseline in the lines without MED12L | 0.073 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[GNAL]] | B | MED12L activity raises GNAL's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.79× lower at baseline in the lines without MED12L | 0.091 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[LINC00937]] | B | MED12L activity raises LINC00937's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without MED12L | 0.093 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[RUFY1]] | B | MED12L activity raises RUFY1's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.22× lower at baseline in the lines without MED12L | 0.098 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[LHX2]] | C | MED12L activity raises LHX2's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without MED12L | 0.021 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.9, 37.1); signed map (28.0, 25.6). **Vector** length 81.7, 20.4% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +28.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.9 | +22.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.2 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | +7.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.8 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +11.0 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.1 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 12L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:151,085,286-151,437,072 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1635, TNRC11L, TRALPUSH, TRALP |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 2 pathways, smallest: M-decay: degradation of maternal mRNAs by maternally stored factors; Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YW9](https://www.uniprot.org/uniprotkb/Q86YW9) (Mediator of RNA polymerase II transcription subunit 12-like protein):

> May be a component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [116931](https://www.ncbi.nlm.nih.gov/gene/116931):

> The protein encoded by this gene is part of the Mediator complex, which is involved in transcriptional coactivation of nearly all RNA polymerase II-dependent genes. The Mediator complex links gene-specific transcriptional activators with the basal transcription machinery. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:16050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16050) · Entrez [116931](https://www.ncbi.nlm.nih.gov/gene/116931) · UniProt [Q86YW9](https://www.uniprot.org/uniprotkb/Q86YW9) · Ensembl [ENSG00000144893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144893)

## Data

Gene col 6943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6943); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6943]; `tensor/DDL_lfc|DDL_z.npy` [6943]; `embed/gene_vectors.npy` [6943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6943 or target_col == 6943). Every well: [[MED12L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED12L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

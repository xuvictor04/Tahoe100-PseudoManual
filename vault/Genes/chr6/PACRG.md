---
symbol: "PACRG"
type: "gene"
col: 3375
ensembl_id: "ENSG00000112530"
name: "parkin coregulated"
location: "6q26"
module: 35
arm: "+"
pooled_cpm: 3.95
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PACRG

*parkin coregulated* — 6q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.88× (z +25.7, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.651× (z -4.1, q 0.025, down in 14 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.136×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.0494×; ⚠ cell-cycle shift, explains ~91% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.103×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0788×); [[Canagliflozin (drug)]] 5 µM in 1 line (HOP62 0.0849×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01122]] (+0.69, fdr 7e-06), [[ARL14EP-DT]] (+0.66, fdr 7e-06), [[UPK2]] (+0.66, fdr 1e-05); moves opposite to [[ACSF3]] (-0.53, fdr 9e-05), [[CNOT10]] (-0.51, fdr 8e-05), [[MIS18A]] (-0.50, fdr 8e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.88×** | +25.7 | 0e+00 | 32/32 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.20×** | +11.0 | 2e-25 | 30/43 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +9.8 | 2e-20 | 24/31 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +8.7 | 7e-16 | 22/33 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +8.2 | 2e-14 | 6/15 (HS-578T, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +7.1 | 2e-10 | 22/45 (KATO III, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +6.8 | 1e-09 | 3/8 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +6.3 | 3e-08 | 17/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.96×** | +6.1 | 8e-08 | 14/30 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +6.0 | 1e-07 | 20/36 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.9 | 1e-07 | 13/46 (A498, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +5.7 | 6e-07 | 14/45 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +5.6 | 8e-07 | 1/5 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.51×** | +5.4 | 2e-06 | 13/45 (A-427, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +4.9 | 3e-05 | 17/45 (A-427, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +4.9 | 4e-05 | 16/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.002 | 14/45 (A498, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.005 | 9/37 (A-427, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.009 | 10/41 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3375.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.136×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.0494×; ⚠ cell-cycle shift, explains ~91% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.103×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0788×); [[Canagliflozin (drug)]] 5 µM in 1 line (HOP62 0.0849×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.651×** | -4.1 | 0.025 | 14/43 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.682×** | -3.6 | 0.077 | 14/41 (NCI-H23, A-427, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.528× | -3.2 | 0.23 | 9/29 (A-427, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.722× | -3.1 | 0.23 | 9/31 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.724× | -3.1 | 0.23 | 5/47 (NCI-H2030, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.69 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.44× (z +11.3) | [[Canagliflozin (drug)]] 5 µM 0.0849× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 16.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.89× (z +8.8) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0494× (z -12.0) ⚠ cell-cycle shift, explains ~91% of this change |
| [[A-427 (line)]] | wt | 10.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.103× (z -8.8) |
| [[A498 (line)]] | wt | 1.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +10.3) | — |
| [[LoVo (line)]] | wt | 1.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0788× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 2.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.40× (z +10.7) | — |
| [[SW480 (line)]] | alt | 1.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.28× (z +9.6) | — |
| [[A-172 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01122]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ARL14EP-DT]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[UPK2]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[LRRIQ3]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[LRIG2-DT]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[CHODL]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ID2-AS1]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ACKR2]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[GRID2]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MAP1LC3B2]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CCDC3]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[STX17-DT]] | +0.61 | +0.62 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSF3]] | -0.53 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[CNOT10]] | -0.51 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[MIS18A]] | -0.50 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[MTG1]] | -0.50 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[CTU2]] | -0.50 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[CEP192]] | -0.50 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[WRN]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PACRG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ID2-AS1]] | B | ID2-AS1 activity raises PACRG's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without ID2-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PACRG's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.7, 27.7); signed map (35.5, -2.0). **Vector** length 65.0, 10.5% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +25.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +6.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | parkin coregulated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q26 — chr6:162,727,132-163,315,500 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PARK2CRG, FLJ32724, Glup, HAK005771, BUG21, pf12 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M98](https://www.uniprot.org/uniprotkb/Q96M98) (Parkin coregulated gene protein):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating. Suppresses cell death induced by accumulation of unfolded Pael receptor (Pael-R, a substrate of Parkin). Facilitates the formation of inclusions consisting of Pael-R, molecular chaperones, protein degradation molecules and itself when proteasome is inhibited. May play an important role in the formation of Lewy bodies and protection of …

**Summary**, from NCBI Gene [135138](https://www.ncbi.nlm.nih.gov/gene/135138):

> This gene encodes a protein that is conserved across metazoans. In vertebrates, this gene is linked in a head-to-head arrangement with the adjacent parkin gene, which is associated with autosomal recessive juvenile Parkinson's disease. These genes are co-regulated in various tissues and they share a bi-directional promoter. Both genes are associated with susceptibility to leprosy. The parkin co-regulated gene protein forms a large molecular complex with chaperones, including heat shock proteins …

**Accessions** — [HGNC:19152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19152) · Entrez [135138](https://www.ncbi.nlm.nih.gov/gene/135138) · UniProt [Q96M98](https://www.uniprot.org/uniprotkb/Q96M98) · Ensembl [ENSG00000112530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112530)

## Data

Gene col 3375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3375); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3375]; `tensor/DDL_lfc|DDL_z.npy` [3375]; `embed/gene_vectors.npy` [3375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3375 or target_col == 3375). Every well: [[PACRG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PACRG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

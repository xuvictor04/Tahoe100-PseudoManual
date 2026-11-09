---
symbol: "GIN1"
type: "gene"
col: 7016
ensembl_id: "ENSG00000145723"
name: "gypsy retrotransposon integrase 1"
location: "5q21.1"
module: 28
arm: "+"
pooled_cpm: 5.67
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# GIN1

*gypsy retrotransposon integrase 1* — 5q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.08× (z +14.9, q 0e+00, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.504× (z -9.9, q 3e-20, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF585A]] (+0.76, fdr 1e-05), [[TMEM128]] (+0.75, fdr 1e-05), [[FAM200A]] (+0.73, fdr 1e-05); moves opposite to [[LMBR1]] (-0.60, fdr 3e-05), [[PLXND1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[THBS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +14.9 | 0e+00 | 33/41 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +12.8 | 7e-35 | 30/41 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +10.5 | 2e-23 | 24/41 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +8.2 | 3e-14 | 20/31 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +7.7 | 2e-12 | 23/45 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +7.2 | 6e-11 | 16/47 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.7 | 2e-04 | 9/46 (KATO III, A-427, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.3 | 0.001 | 15/44 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 0.002 | 7/47 (SW48, LoVo, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.004 | 11/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.005 | 4/46 (LoVo, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.009 | 1/46 (PANC-1) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.017 | 6/43 (A-427, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.5 | 0.017 | 2/48 (MIA PaCa-2, HOP62) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.4 | 0.026 | 0/14 | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.038 | 1/47 (LoVo) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.041 | 4/46 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.085 | 0/47 | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.504×** | -9.9 | 3e-20 | 24/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.532×** | -8.7 | 6e-16 | 27/36 (NCI-H1573, A-427, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.616×** | -7.0 | 6e-10 | 22/46 (BT-474, SW480, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.624×** | -6.8 | 2e-09 | 17/45 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -6.2 | 6e-08 | 19/41 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -4.7 | 2e-04 | 12/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.763×** | -3.9 | 0.008 | 12/47 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.21 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.193× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.281× (z -8.6) |
| [[A549 (line)]] | wt | 5.24 | 0 | 2 | — | [[Hesperidin (drug)]] 5 µM 0.0626× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -9.7) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 5.76 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0809× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -9.7) |
| [[A-172 (line)]] | wt | 4.82 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -8.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 7.69 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -9.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 5.89 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0933× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 6.65 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0552× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 5.63 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.129× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 5.67 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0870× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 7.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 5.67 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -11.4) |
| [[SHP-77 (line)]] | alt | 9.84 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -8.9) ⚠ toxic |
| [[A498 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF585A]] | +0.76 | +0.80 / +0.51 | both halves | 1e-05 |  |
| [[TMEM128]] | +0.75 | +0.85 / +0.51 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.73 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[RAD52]] | +0.71 | +0.80 / +0.47 | both halves | 2e-05 |  |
| [[ZBTB6]] | +0.71 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[KCTD18]] | +0.70 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[THAP6]] | +0.69 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[ARL14EP]] | +0.69 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.68 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[NAIF1]] | +0.68 | +0.72 / +0.47 | both halves | 2e-05 | STRING 407 |
| [[ZNF606]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ZXDA]] | +0.68 | +0.69 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1]] | -0.60 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[PLXND1]] | -0.59 | -0.58 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS4]] | B | THBS4 activity raises GIN1's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.31× lower at baseline in the lines without THBS4 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[ZNF675]] | B | ZNF675 activity raises GIN1's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without ZNF675 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[ZNF571]] | B | ZNF571 activity raises GIN1's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 1.27× lower at baseline in the lines without ZNF571 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[ZNF606]] | B | ZNF606 activity raises GIN1's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 1.11× lower at baseline in the lines without ZNF606 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.8, 6.4); signed map (6.6, -23.3). **Vector** length 61.8, 8.63% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +14.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +7.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.3 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | -0.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -8.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -6.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -7.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | gypsy retrotransposon integrase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.1 — chr5:103,086,000-103,120,138 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20125, GIN-1, TGIN1; previously ZH2C2 |
| Gene groups (HGNC) | Integrase like retrotransposon derived |
| Matched by | ensembl_id |

UniProt [Q9NXP7](https://www.uniprot.org/uniprotkb/Q9NXP7) carries no function annotation.

**Summary**, from NCBI Gene [54826](https://www.ncbi.nlm.nih.gov/gene/54826):

> Predicted to enable nucleic acid binding activity. Predicted to be involved in DNA integration. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25959) · Entrez [54826](https://www.ncbi.nlm.nih.gov/gene/54826) · UniProt [Q9NXP7](https://www.uniprot.org/uniprotkb/Q9NXP7) · Ensembl [ENSG00000145723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145723)

## Data

Gene col 7016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7016); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7016]; `tensor/DDL_lfc|DDL_z.npy` [7016]; `embed/gene_vectors.npy` [7016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7016 or target_col == 7016). Every well: [[GIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

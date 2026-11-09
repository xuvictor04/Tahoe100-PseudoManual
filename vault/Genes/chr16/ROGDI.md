---
symbol: "ROGDI"
type: "gene"
col: 871
ensembl_id: "ENSG00000067836"
name: "rogdi atypical leucine zipper"
location: "16p13.3"
module: 17
arm: "+"
pooled_cpm: 2.85
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ROGDI

*rogdi atypical leucine zipper* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.80× (z +11.4, q 2e-27, up in 13 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 3.78× (z +11.4, q 2e-27, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.510× (z -5.8, q 3e-06, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD17]] (+0.73, fdr 1e-05), [[PAFAH1B3]] (+0.65, fdr 3e-05), [[CDK5]] (+0.64, fdr 2e-05); moves opposite to [[GNG12-AS1]] (-0.60, fdr 8e-05), [[CSTF3]] (-0.58, fdr 3e-04), [[YARS2]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PRR36]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.80×** | +11.4 | 2e-27 | 13/16 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.78×** | +11.4 | 2e-27 | 42/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.49×** | +10.7 | 2e-24 | 35/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +10.4 | 5e-23 | 4/5 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.77×** | +8.7 | 4e-16 | 30/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +7.1 | 1e-10 | 5/5 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +5.2 | 1e-05 | 18/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +5.0 | 4e-05 | 7/18 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +4.6 | 3e-04 | 10/32 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +4.5 | 3e-04 | 8/43 (SW1417, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.7 | 0.010 | 6/18 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.82×** | +3.6 | 0.012 | 5/32 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.014 | 7/42 (NCI-H2030, A-427, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.80×** | +3.6 | 0.014 | 3/16 (HEC-1-A, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.75×** | +3.4 | 0.024 | 5/33 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.033 | 6/41 (PANC-1, A-427, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.040 | 9/43 (KATO III, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.11×** | +3.1 | 0.055 | 3/39 (KATO III, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.055 | 4/44 (NCI-H23, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.44×** | +3.1 | 0.055 | 5/44 (SW480, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.510×** | -5.8 | 3e-06 | 25/46 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.512×** | -5.7 | 3e-06 | 20/42 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -5.5 | 9e-06 | 15/26 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.620×** | -4.1 | 0.006 | 19/41 (SHP-77, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.666×** | -3.3 | 0.094 | 13/41 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -3.3 | 0.094 | 9/31 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.774× | -3.1 | 0.13 | 14/34 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.696× | -3.1 | 0.13 | 13/42 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.703× | -3.0 | 0.15 | 14/33 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.685× | -3.0 | 0.15 | 6/43 (BT-474, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0817× (z -8.6) |
| [[A-172 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD17]] | +0.73 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | +0.65 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CDK5]] | +0.64 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[BCAM]] | +0.64 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SCRN2]] | +0.63 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ARSA]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ALAD]] | +0.62 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[TMEM9]] | +0.62 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[VWA1]] | +0.61 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[TBCB]] | +0.61 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[ANO8]] | +0.60 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.59 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG12-AS1]] | -0.60 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[CSTF3]] | -0.58 | -0.29 / -0.37 | both halves | 3e-04 |  |
| [[YARS2]] | -0.58 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[KLRA1P]] | -0.58 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[DARS1-AS1]] | -0.56 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[GABPB1-AS1]] | -0.56 | -0.24 / -0.43 | both halves | 5e-04 |  |
| [[ACAD9]] | -0.55 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[MIRLET7IHG]] | -0.55 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[ZNF26]] | -0.54 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[PCBP1-AS1]] | -0.54 | -0.16 / -0.38 | ⚠ not reproduced | 0.001 |  |
| [[TAS2R4]] | -0.54 | -0.26 / -0.34 | both halves | 4e-04 |  |
| [[EEF1AKMT1]] | -0.53 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[MIATNB]] | -0.53 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR36]] | B | PRR36 activity raises ROGDI's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without PRR36 | 0.007 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[UCP2]] | B | UCP2 activity raises ROGDI's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.29× lower at baseline in the lines without UCP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: WNK2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (10.5, -5.2); signed map (-26.9, -2.2). **Vector** length 49.6, 6.48% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +11.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +7.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +3.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -3.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | rogdi atypical leucine zipper |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,796,968-4,802,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22386, ROGD1, RAV2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZN7](https://www.uniprot.org/uniprotkb/Q9GZN7) (Protein rogdi homolog):

> Probably involved in the regulation of intracellular pH. As part of the RAVE complex it may control the assembly of the proton-pumping V-ATPase complex and therefore regulate organelle acidification (Probable).

**Summary**, from NCBI Gene [79641](https://www.ncbi.nlm.nih.gov/gene/79641):

> Involved in brain development; neurogenesis; and odontogenesis of dentin-containing tooth. Located in nuclear envelope. Implicated in Kohlschutter-Tonz syndrome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29478) · Entrez [79641](https://www.ncbi.nlm.nih.gov/gene/79641) · UniProt [Q9GZN7](https://www.uniprot.org/uniprotkb/Q9GZN7) · Ensembl [ENSG00000067836](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067836)

## Data

Gene col 871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 871); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 871]; `tensor/DDL_lfc|DDL_z.npy` [871]; `embed/gene_vectors.npy` [871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 871 or target_col == 871). Every well: [[ROGDI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROGDI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

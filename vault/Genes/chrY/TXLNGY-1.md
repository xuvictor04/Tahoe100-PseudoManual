---
symbol: "TXLNGY-1"
type: "gene"
col: 16548
ensembl_id: "ENSG00000291033"
name: ""
location: ""
module: 1
arm: "+"
pooled_cpm: 5.72
n_lines_expressing: 20
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TXLNGY-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.67× (z +19.6, q 0e+00, up in 5 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +4.5, q 6e-04, up in 4 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.616× (z -5.3, q 7e-05, down in 0 of 17 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXLNGY]] (+0.92, fdr 7e-06, ⚠ same locus), [[MRPS25]] (+0.55, fdr 2e-05), [[WDR77]] (+0.55, fdr 2e-05), [[CCDC86]] (+0.55, fdr 2e-05); moves opposite to [[RNASE4]] (-0.55, fdr 4e-05), [[CARHSP1]] (-0.55, fdr 4e-05), [[TNNT1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[PYGO1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.67×** | +19.6 | 0e+00 | 5/8 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.16×** | +19.3 | 0e+00 | 4/13 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +12.4 | 9e-33 | 2/11 (SNU-423, A549) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.44×** | +5.5 | 6e-06 | 1/9 (A-172) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.91×** | +5.4 | 6e-06 | 1/14 (J82) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.6 | 4e-04 | 2/15 (A-427, A-172) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.5 | 6e-04 | 4/17 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +4.4 | 9e-04 | 1/16 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.003 | 2/16 (H4, COLO 205) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.7 | 0.010 | 0/16 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.6 | 0.014 | 0/17 | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.016 | 2/17 (A-172, SNU-1) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.023 | 8/18 (A-172, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.025 | 2/17 (HepG2/C3A, SNU-423) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.4 | 0.028 | 3/16 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.030 | 0/17 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.092 | 6/16 (SK-MEL-2, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.616×** | -5.3 | 7e-05 | 0/17 | inconsistent across doses | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -4.2 | 0.008 | 0/17 | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.598× | -3.2 | 0.23 | 10/17 (NCI-H460, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | 0.769× | -3.1 | 0.23 | 5/17 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.755× | -3.1 | 0.23 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.659 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.427 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXLNGY]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MRPS25]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[WDR77]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CCDC86]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[SLC5A6]] | +0.55 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[SNX5]] | +0.53 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[GNL3L]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[HS6ST2]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[EDNRB]] | +0.52 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[SLC35G1]] | +0.52 | +0.37 / +0.42 | both halves | 8e-05 |  |
| [[VARS1]] | +0.52 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[ATIC]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[BAGE2]] | +0.51 | +0.50 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASE4]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[CARHSP1]] | -0.55 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TNNT1]] | -0.52 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CASP9]] | -0.51 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[RRAS]] | -0.51 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[LGALS1]] | -0.50 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[WASF2]] | -0.50 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[SEZ6L2]] | -0.49 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[FAM89B]] | -0.49 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[PLA2G15]] | -0.48 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[ZER1]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ZCRB1]] | -0.48 | -0.39 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TXLNGY-1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TTTY10]] | C | TTTY10 activity raises TXLNGY-1's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 9.78× lower at baseline in the lines without TTTY10 | 9e-07 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYGO1]] | B | [[TXLNGY]], TXLNGY-1 activity raises PYGO1's level | lines that do not express TXLNGY, TXLNGY-1 (30) vs lines expressing them (20) | 2.28× lower at baseline in the lines without TXLNGY, TXLNGY-1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent genes |
| [[TTTY10]] | C | [[TXLNGY]], TXLNGY-1 activity raises TTTY10's level | lines that do not express TXLNGY, TXLNGY-1 (30) vs lines expressing them (20) | 5.93× lower at baseline in the lines without TXLNGY, TXLNGY-1 | 8e-06 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target; co-absent genes |
| [[EDNRB]] | C | [[TXLNGY]], TXLNGY-1 activity raises EDNRB's level | lines that do not express TXLNGY, TXLNGY-1 (30) vs lines expressing them (20) | 2.39× lower at baseline in the lines without TXLNGY, TXLNGY-1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.5, -42.5); signed map (2.9, -48.3). **Vector** length 29.1, 5.31% of its response variance represented; |z| ≥ 3 in 291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +19.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.6 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.9 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.9 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +3.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -3.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.7 | -2.2 |

## What is on record

> [!warning] No registry record
> TXLNGY-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16548); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16548]; `tensor/DDL_lfc|DDL_z.npy` [16548]; `embed/gene_vectors.npy` [16548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16548 or target_col == 16548). Every well: [[TXLNGY-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXLNGY-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

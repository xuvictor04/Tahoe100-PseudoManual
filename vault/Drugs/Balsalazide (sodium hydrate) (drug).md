---
drug: "Balsalazide (sodium hydrate)"
type: "drug"
salt_base: "Balsalazide"
targets: "IL6, STAT3"
moa_fine: "JAK/STAT inhibitor"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 9
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Balsalazide (sodium hydrate)

*JAK/STAT inhibitor (unclear) · targets: IL6, STAT3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 0 / 9; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.38 / 0.54.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G10 | 0 / 4 | — | -0.09 | -0.6/-0.4/-0.5 | — |
| 0.5 µM | [[Plate 05]]:G10 | 0 / 0 | — | +0.46 | +0.6/+0.4/-0.6 | — |
| 5 µM | [[Plate 14]]:G10 | 1 / 8 | 0.837 | +0.29 | +1.1/+0.5/-1.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (1 gene, none with an alert): [[ATP13A1]] 1.21× (z +3.1, 7/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[MUC17]] 0.618× (z -3.3, 0/4 lines), [[SLC22A14]] 0.700× (z -3.2, 10/46 lines), [[AOX1]] 0.752× (z -3.2, 4/29 lines), [[C6orf132]] 0.811× (z -3.0, 6/21 lines)

**5 µM** (8 genes, none with an alert): [[COLEC11]] 0.652× (z -4.5, 13/46 lines), [[MIR4300HG]] 0.744× (z -4.0, 9/45 lines), [[FTH1]] 0.760× (z -3.9, 41/44 lines), [[SYN3]] 0.800× (z -3.9, 11/48 lines), [[SBDS]] 0.822× (z -3.9, 25/48 lines), [[TRIM31]] 0.727× (z -3.7, 5/9 lines), [[LRRC75A]] 0.807× (z -3.6, 17/48 lines), [[GPR137]] 0.801× (z -3.3, 9/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 171]] (+2.2) | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 043]] (-2.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[SW1417 (line)]] (-3.6) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 9 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Oxaliplatin (drug)]] (+0.76, DNA synthesis/repair inhibitor, ⚠ only 7 significant genes); [[Pyridoxine (hydrochloride) (drug)]] (+0.76, unclear); [[Fusidic acid (drug)]] (+0.74, unclear); [[Folic acid (drug)]] (+0.73, unclear); [[Berberine (chloride hydrate) (drug)]] (+0.70, unclear); [[Clonidine (hydrochloride) (drug)]] (+0.70, Adrenoceptor agonist, ⚠ only 4 significant genes); [[Rutin (trihydrate) (drug)]] (+0.66, unclear); [[Volasertib (drug)]] (+0.66, unclear); [[Diphenhydramine (drug)]] (+0.65, unclear); [[Demeclocycline (drug)]] (+0.64, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 21 arrows, 21 of them with an alert ⚠; grade A 0, B 15, C 6. Shown: the 15 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PRR36]] | 5 µM | B | PRR36 activity lowers the cells' numbers under Balsalazide (sodium hydrate) 5 µM (makes them more sensitive) | lines that do not express PRR36 (19) vs lines expressing it (29) | the lines without PRR36: 1.10× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[MSRB3]] | 5 µM | B | MSRB3 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 0.91× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[WFDC2]] | 5 µM | B | WFDC2 activity lowers the cells' numbers under Balsalazide (sodium hydrate) 5 µM (makes them more sensitive) | lines that do not express WFDC2 (38) vs lines expressing it (10) | the lines without WFDC2: 1.12× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[SCUBE2]] | 5 µM | B | SCUBE2 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express SCUBE2 (7) vs lines expressing it (41) | the lines without SCUBE2: 0.87× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[EPCAM]] | 5 µM | B | EPCAM activity lowers the cells' numbers under Balsalazide (sodium hydrate) 5 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.10× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[MYH14]] | 5 µM | B | MYH14 activity lowers the cells' numbers under Balsalazide (sodium hydrate) 5 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.13× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[FAAH2]] | 5 µM | B | FAAH2 activity lowers the cells' numbers under Balsalazide (sodium hydrate) 5 µM (makes them more sensitive) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 1.12× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[ARHGEF6]] | 5 µM | B | ARHGEF6 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 0.90× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[DDR2]] | 5 µM | B | DDR2 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express DDR2 (9) vs lines expressing it (39) | the lines without DDR2: 0.89× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[TNFSF15]] | 5 µM | B | TNFSF15 activity lowers the cells' numbers under Balsalazide (sodium hydrate) 5 µM (makes them more sensitive) | lines that do not express TNFSF15 (31) vs lines expressing it (17) | the lines without TNFSF15: 1.13× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[AOX1]] | 5 µM | B | AOX1 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 0.90× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[RBMS3]] | 5 µM | B | RBMS3 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express RBMS3 (19) vs lines expressing it (29) | the lines without RBMS3: 0.89× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[KCNG1]] | 5 µM | B | KCNG1 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express KCNG1 (18) vs lines expressing it (30) | the lines without KCNG1: 0.90× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |
| [[COL17A1]] | 5 µM | B | COL17A1 activity lowers the cells' numbers under Balsalazide (sodium hydrate) 5 µM (makes them more sensitive) | lines that do not express COL17A1 (34) vs lines expressing it (14) | the lines without COL17A1: 1.11× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[GJA1]] | 5 µM | B | GJA1 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 0.89× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Balsalazide (sodium hydrate)"
- `tables/drugdoses.parquet` — dd in 141, 142, 143
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

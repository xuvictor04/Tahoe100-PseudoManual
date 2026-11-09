---
drug: "Rimonabant"
type: "drug"
salt_base: "Rimonabant"
targets: "CNR1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 7
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Rimonabant

*unclear (inhibitor/antagonist) · targets: CNR1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 1 / 7; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.40 / 0.35.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F9 | 1 / 0 | — | +0.42 | +0.6/-0.2/+0.5 | — |
| 0.5 µM | [[Plate 05]]:F9 | 0 / 1 | — | +0.43 | +0.1/-0.6/-0.1 | — |
| 5 µM | [[Plate 14]]:F9 | 5 / 2 | 0.828 | -0.09 | +1.0/-0.4/+1.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[STK40]] 1.21× (z +3.2, 11/49 lines)

**5 µM** (5 genes, none with an alert): [[ENSG00000277938]] 1.33× (z +3.6, 2/44 lines), [[CHTF18]] 1.28× (z +3.4, 5/46 lines), [[FERMT3]] 1.27× (z +3.4, 7/43 lines), [[OAS1]] 1.24× (z +3.1, 16/35 lines), [[CHADL]] 1.34× (z +2.9, 2/42 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[UGT1A6]] 0.740× (z -3.2, 0/13 lines)

**5 µM** (2 genes, none with an alert): [[MIR181A2HG]] 0.827× (z -3.9, 9/45 lines), [[CYP1B1-AS1]] 0.771× (z -3.3, 6/34 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[HEC-1-A (line)]] (-3.9) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 7 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Cinacalcet (drug)]] (+0.66, unclear, ⚠ only 8 significant genes); [[Esmolol (hydrochloride) (drug)]] (+0.66, unclear); [[Diphenhydramine (drug)]] (+0.66, unclear); [[Apalutamide (drug)]] (+0.65, Androgen receptor antagonist); [[Larotrectinib (drug)]] (+0.64, Other TK inhibitor); [[Mifepristone (drug)]] (+0.63, unclear); [[Tirabrutinib (drug)]] (+0.63, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.63, unclear); [[Estrone sulfate (potassium) (drug)]] (+0.60, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 34 arrows, 34 of them with an alert ⚠; grade A 0, B 28, C 6. Shown: the 15 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LINC02257]] | 5 µM | B | LINC02257 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express LINC02257 (15) vs lines expressing it (33) | the lines without LINC02257: 1.12× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[FOXQ1]] | 5 µM | B | FOXQ1 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express FOXQ1 (30) vs lines expressing it (18) | the lines without FOXQ1: 1.14× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[STEAP4]] | 5 µM | B | STEAP4 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express STEAP4 (38) vs lines expressing it (10) | the lines without STEAP4: 1.16× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[SLC5A1]] | 5 µM | B | SLC5A1 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express SLC5A1 (36) vs lines expressing it (12) | the lines without SLC5A1: 1.15× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[IL15]] | 5 µM | B | IL15 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.18× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[SERPINB5]] | 5 µM | B | SERPINB5 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express SERPINB5 (34) vs lines expressing it (14) | the lines without SERPINB5: 1.15× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[TMC4]] | 5 µM | B | TMC4 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express TMC4 (26) vs lines expressing it (22) | the lines without TMC4: 1.10× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[ADGRF1]] | 5 µM | B | ADGRF1 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express ADGRF1 (35) vs lines expressing it (13) | the lines without ADGRF1: 1.18× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[MAML2]] | 5 µM | B | MAML2 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2: 1.13× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[LGALS9]] | 5 µM | B | LGALS9 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express LGALS9 (13) vs lines expressing it (35) | the lines without LGALS9: 1.11× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[TTC22]] | 5 µM | B | TTC22 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express TTC22 (32) vs lines expressing it (16) | the lines without TTC22: 1.14× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[INAVA]], [[MROH3P]] | 5 µM | B | INAVA, MROH3P activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express INAVA, MROH3P (29) vs lines expressing them (19) | the lines without INAVA, MROH3P: 1.13× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[GALNT3]] | 5 µM | B | GALNT3 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express GALNT3 (30) vs lines expressing it (18) | the lines without GALNT3: 1.16× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[TMPRSS2]] | 5 µM | B | TMPRSS2 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express TMPRSS2 (35) vs lines expressing it (13) | the lines without TMPRSS2: 1.15× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ATP2C2]] | 5 µM | B | ATP2C2 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.16× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Rimonabant"
- `tables/drugdoses.parquet` — dd in 899, 900, 901
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

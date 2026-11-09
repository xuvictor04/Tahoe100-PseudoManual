---
drug: "Tranilast"
type: "drug"
salt_base: "Tranilast"
targets: "PLA2G2A, EGR1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 6
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tranilast

*unclear (inhibitor/antagonist) · targets: PLA2G2A, EGR1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 6 / 0; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.62 / 0.12.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:H2 | 3 / 1 | — | -0.00 | -0.4/-0.2/+1.1 | — |
| 0.5 µM | [[Plate 08]]:H2 | 6 / 0 | — | +0.14 | +0.0/+0.8/+1.4 | — |
| 5 µM | [[Plate 09]]:H2 | 0 / 0 | — | +0.39 | +0.5/+0.1/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[TPTE2P6]] 1.21× (z +3.2, 2/45 lines), [[ENSG00000283217]] 1.48× (z +3.0, 0/30 lines), [[HSPB8]] 1.30× (z +2.7, 3/46 lines)

**0.5 µM** (6 genes, none with an alert): [[MT-ATP6]] 1.58× (z +3.2, 39/48 lines), [[SLC15A1]] 1.46× (z +3.1, 0/7 lines), [[ARL9]] 1.52× (z +3.1, 6/45 lines), [[CCDC181]] 1.38× (z +3.0, 1/45 lines), [[KIF1A]] 1.26× (z +2.9, 0/14 lines), [[LINC01194]] 1.33× (z +2.9, 0/16 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000259539]] 0.757× (z -2.9, 7/41 lines)

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
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 6 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Docetaxel (Trihydrate) (drug)]] (+0.89, Microtubule inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.86, unclear); [[Methylprednisolone succinate (drug)]] (+0.84, Glucocorticoid receptor agonist); [[Darolutamide (drug)]] (+0.80, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Bendamustine (drug)]] (+0.80, DNA synthesis/repair inhibitor); [[Decitabine (drug)]] (+0.78, DNA methyltransferase inhibitor); [[Nimesulide (drug)]] (+0.77, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Azithromycin (hydrate) (drug)]] (+0.74, unclear); [[Almonertinib (hydrochloride) (drug)]] (+0.72, EGFR/ERBB inhibitor); [[Celecoxib (drug)]] (+0.70, Cyclooxygenase inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 24 arrows, 24 of them with an alert ⚠; grade A 0, B 7, C 17. Shown: the 15 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PIP5K1B]] | 0.5 µM | B | PIP5K1B activity lowers the cells' numbers under Tranilast 0.5 µM (makes them more sensitive) | lines that do not express PIP5K1B (33) vs lines expressing it (15) | the lines without PIP5K1B: 1.19× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[CGAS]] | 0.5 µM | B | CGAS activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express CGAS (17) vs lines expressing it (31) | the lines without CGAS: 0.83× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[ETS1]] | 0.5 µM | B | ETS1 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express ETS1 (11) vs lines expressing it (37) | the lines without ETS1: 0.79× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[SLFN5]] | 0.5 µM | B | SLFN5 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.81× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[ECHDC2]] | 0.5 µM | B | ECHDC2 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express ECHDC2 (12) vs lines expressing it (36) | the lines without ECHDC2: 0.85× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.5 µM | B | KLRC4-KLRK1, KLRK1 activity lowers the cells' numbers under Tranilast 0.5 µM (makes them more sensitive) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 1.16× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[KLHL5]] | 0.5 µM | B | KLHL5 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express KLHL5 (7) vs lines expressing it (41) | the lines without KLHL5: 0.84× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[PHF11]] | 0.5 µM | C | PHF11 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.72× the cells of the other lines | 0.011 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[ENSG00000285458]] | 0.5 µM | C | ENSG00000285458 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 0.78× the cells of the other lines | 0.023 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[RARG]] | 0.5 µM | C | RARG activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.74× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| [[ACCS]] | 0.5 µM | C | ACCS activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.77× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| [[FAM111A]] | 0.5 µM | C | FAM111A activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express FAM111A (3) vs lines expressing it (45) | the lines without FAM111A: 0.76× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |
| [[CEBPD]], [[GCA]] | 0.5 µM | C | CEBPD, GCA activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.74× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[PLS3]] | 0.5 µM | C | PLS3 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.77× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| [[SPAG16]] | 0.5 µM | C | SPAG16 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 0.81× the cells of the other lines | 0.051 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Tranilast"
- `tables/drugdoses.parquet` — dd in 1039, 1040, 1041
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

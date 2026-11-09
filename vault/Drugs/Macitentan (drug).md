---
drug: "Macitentan"
type: "drug"
salt_base: "Macitentan"
targets: "EDNRA, EDNRB"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 5
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Macitentan

*unclear (inhibitor/antagonist) · targets: EDNRA, EDNRB · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 0 / 5; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.31 / 0.36.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:H3 | 0 / 0 | — | +0.40 | -0.0/-0.2/+0.6 | — |
| 0.5 µM | [[Plate 08]]:H3 | 0 / 0 | — | +0.14 | -0.2/-0.6/+0.3 | — |
| 5 µM | [[Plate 09]]:H3 | 5 / 0 | — | -0.49 | -1.3/-1.6/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (5 genes, none with an alert): [[ENSG00000272297]] 1.42× (z +3.7, 1/17 lines), [[HYAL1]] 1.54× (z +3.2, 6/34 lines), [[ENSG00000291138]] 1.57× (z +3.1, 2/16 lines), [[PRMT5-DT]] 1.37× (z +3.1, 1/37 lines), [[MPND]] 1.29× (z +3.0, 2/42 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

No gene is significantly lowered at any dose.

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
| 5 µM | [[SW 900 (line)]] (-3.1) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 5 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Fulvestrant (drug)]] (+0.62, unclear, ⚠ only 8 significant genes); [[Imiquimod (hydrochloride) (drug)]] (+0.61, unclear, ⚠ vector dose flagged: toxic); [[Cysteamine (hydrochloride) (drug)]] (+0.61, unclear); [[AZD1390 (drug)]] (+0.60, unclear); [[Sunitinib (drug)]] (+0.58, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Saquinavir (drug)]] (+0.57, unclear); [[Lactate (calcium) (drug)]] (+0.56, unclear); [[Bestatin (drug)]] (+0.55, unclear, ⚠ only 3 significant genes); [[Lidocaine (hydrochloride) (drug)]] (+0.54, unclear); [[Methylprednisolone succinate (drug)]] (+0.53, Glucocorticoid receptor agonist); [[Canagliflozin (hemihydrate) (drug)]] (+0.53, Glucose transporter inhibitor); [[Hydroxyurea (drug)]] (+0.53, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 21 arrows, 21 of them with an alert ⚠; grade A 0, B 19, C 2. Shown: the 15 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.34× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.29× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[BMPER]] | 5 µM | B | BMPER activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.25× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under Macitentan 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.81× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[DCDC2]] | 5 µM | B | DCDC2 activity raises the cells' numbers under Macitentan 5 µM (protects the cells) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 0.88× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.30× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[CNRIP1]] | 5 µM | B | CNRIP1 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.21× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[SRPX]] | 5 µM | B | SRPX activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 1.20× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[AOX1]] | 5 µM | B | AOX1 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.25× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[RSPO3]] | 5 µM | B | RSPO3 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 1.26× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[C10orf90]] | 5 µM | B | C10orf90 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express C10orf90 (35) vs lines expressing it (13) | the lines without C10orf90: 1.27× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent |
| [[LINC01583]] | 5 µM | B | LINC01583 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express LINC01583 (28) vs lines expressing it (20) | the lines without LINC01583: 1.26× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2 |
| [[ADAM12]] | 5 µM | B | ADAM12 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 1.27× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[TEX41]] | 5 µM | B | TEX41 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express TEX41 (29) vs lines expressing it (19) | the lines without TEX41: 1.22× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[ENSG00000261273]] | 5 µM | B | ENSG00000261273 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express ENSG00000261273 (9) vs lines expressing it (39) | the lines without ENSG00000261273: 1.25× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SLFN5, BCAR3, ENSG00000284685; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Macitentan"
- `tables/drugdoses.parquet` — dd in 651, 652, 653
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

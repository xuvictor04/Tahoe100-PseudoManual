---
drug: "γ-Oryzanol"
type: "drug"
salt_base: "γ-Oryzanol"
targets: ""
moa_fine: "DNA methyltransferase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 1
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# γ-Oryzanol

*DNA methyltransferase inhibitor (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 1 / 0; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.27 / 0.43.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:F12 | 0 / 0 | — | +0.44 | +0.4/+0.6/-0.1 | — |
| 0.5 µM | [[Plate 11]]:F12 | 1 / 0 | — | -0.15 | +0.0/+0.3/+0.3 | — |
| 5 µM | [[Plate 12]]:F12 | 0 / 0 | — | -0.01 | +0.1/+0.5/+0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[ARHGAP4]] 1.26× (z +3.4, 6/45 lines)

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
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 1 significant gene. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Drospirenone (drug)]] (+0.58, unclear); [[Aliskiren (drug)]] (+0.57, unclear); [[Uridine (drug)]] (+0.55, unclear, ⚠ only 6 significant genes); [[Vemurafenib (drug)]] (+0.54, RAF inhibitor, ⚠ only 1 significant gene); [[Aspirin (drug)]] (+0.54, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.52, Glucose transporter inhibitor); [[Procainamide (hydrochloride) (drug)]] (+0.52, DNA methyltransferase inhibitor, ⚠ only 7 significant genes); [[Dorzolamide (hydrochloride) (drug)]] (+0.52, unclear); [[Bendamustine (drug)]] (+0.49, DNA synthesis/repair inhibitor); [[Silodosin (drug)]] (+0.47, unclear); [[Pimozide (drug)]] (+0.46, unclear); [[Capmatinib (drug)]] (+0.45, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.81× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[PAPPA]] | 0.05 µM | B | PAPPA activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[CD44]] | 0.05 µM | B | CD44 activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express CD44 (15) vs lines expressing it (33) | the lines without CD44: 0.84× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[DCDC2]] | 0.05 µM | B | DCDC2 activity lowers the cells' numbers under γ-Oryzanol 0.05 µM (makes them more sensitive) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 1.10× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[MYH14]] | 0.05 µM | B | MYH14 activity lowers the cells' numbers under γ-Oryzanol 0.05 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.20× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[SIRLNT]] | 0.05 µM | B | SIRLNT activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.81× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[SRGN]] | 0.05 µM | B | SRGN activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.81× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.83× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ENSG00000232949]] | 0.05 µM | B | ENSG00000232949 activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express ENSG00000232949 (29) vs lines expressing it (19) | the lines without ENSG00000232949: 0.83× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, IL6, IL7R |
| [[CCL3]] | 0.05 µM | B | CCL3 activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.82× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| [[CTSC]] | 0.05 µM | B | CTSC activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express CTSC (5) vs lines expressing it (43) | the lines without CTSC: 0.84× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ARHGAP22]] | 0.05 µM | B | ARHGAP22 activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express ARHGAP22 (21) vs lines expressing it (27) | the lines without ARHGAP22: 0.85× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[PRR36]] | 0.05 µM | B | PRR36 activity lowers the cells' numbers under γ-Oryzanol 0.05 µM (makes them more sensitive) | lines that do not express PRR36 (19) vs lines expressing it (29) | the lines without PRR36: 1.16× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[SCAMP5]] | 0.05 µM | C | SCAMP5 activity lowers the cells' numbers under γ-Oryzanol 0.05 µM (makes them more sensitive) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 1.33× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "\u03b3-Oryzanol"
- `tables/drugdoses.parquet` — dd in 1129, 1130, 1131
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Vemurafenib"
type: "drug"
salt_base: "Vemurafenib"
targets: "BRAF"
moa_fine: "RAF inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 1
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Vemurafenib

*RAF inhibitor (inhibitor/antagonist) · targets: BRAF · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 0 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.00 / 0.32.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B9 | 1 / 0 | — | +0.19 | -0.1/+0.1/-0.0 | — |
| 0.5 µM | [[Plate 02]]:B9 | 0 / 0 | — | +1.10 | -0.8/-0.2/-0.6 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B9 | 0 / 0 | — | +1.01 | -0.4/-0.4/-0.9 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[SYN2]] 1.37× (z +3.1, 2/23 lines)

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
| 5 µM | [[MIA PaCa-2 (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 1 significant gene. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Drospirenone (drug)]] (+0.76, unclear); [[Bimatoprost (drug)]] (+0.67, unclear); [[Dexmedetomidine (drug)]] (+0.65, Adrenoceptor agonist, ⚠ only 9 significant genes); [[Pyridoxine (drug)]] (+0.63, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.63, Glucose transporter inhibitor); [[Pimozide (drug)]] (+0.62, unclear); [[Docetaxel (Trihydrate) (drug)]] (+0.62, Microtubule inhibitor); [[Nimesulide (drug)]] (+0.61, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Oxaprozin (drug)]] (+0.58, Cyclooxygenase inhibitor); [[Bestatin (hydrochloride) (drug)]] (+0.57, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[C11orf91]] | 5 µM | B | C11orf91 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express C11orf91 (8) vs lines expressing it (40) | the lines without C11orf91: 0.80× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[IL32]] | 5 µM | B | IL32 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express IL32 (18) vs lines expressing it (30) | the lines without IL32: 0.84× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[KIF1A]] | 5 µM | B | KIF1A activity lowers the cells' numbers under Vemurafenib 5 µM (makes them more sensitive) | lines that do not express KIF1A (34) vs lines expressing it (14) | the lines without KIF1A: 1.19× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[CPA4]] | 5 µM | B | CPA4 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express CPA4 (26) vs lines expressing it (22) | the lines without CPA4: 0.85× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: GYPC, FLI1, IL6 |
| [[MMP1]] | 5 µM | B | MMP1 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express MMP1 (26) vs lines expressing it (22) | the lines without MMP1: 0.86× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[EVA1C]] | 5 µM | B | EVA1C activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express EVA1C (15) vs lines expressing it (33) | the lines without EVA1C: 0.86× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[HMGA2]] | 5 µM | B | HMGA2 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express HMGA2 (9) vs lines expressing it (39) | the lines without HMGA2: 0.88× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[CD59]] | 5 µM | B | CD59 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express CD59 (7) vs lines expressing it (41) | the lines without CD59: 0.79× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[FKBP7]] | 5 µM | B | FKBP7 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express FKBP7 (7) vs lines expressing it (41) | the lines without FKBP7: 0.84× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |
| [[PGM5P2-1]] | 5 µM | B | PGM5P2-1 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express PGM5P2-1 (12) vs lines expressing it (36) | the lines without PGM5P2-1: 0.85× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[ATAD1]], [[PTEN]] | 5 µM | C | ATAD1, PTEN activity lowers the cells' numbers under Vemurafenib 5 µM (makes them more sensitive) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 1.25× the cells of the other lines | 0.045 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| [[HOXA-AS2]] | 5 µM | C | HOXA-AS2 activity raises the cells' numbers under Vemurafenib 5 µM (protects the cells) | lines that do not express HOXA-AS2 (3) vs lines expressing it (45) | the lines without HOXA-AS2: 0.80× the cells of the other lines | 0.062 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |
| [[RAB11FIP1]] | 5 µM | C | RAB11FIP1 activity lowers the cells' numbers under Vemurafenib 5 µM (makes them more sensitive) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 1.27× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Vemurafenib"
- `tables/drugdoses.parquet` — dd in 1075, 1076, 1077
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

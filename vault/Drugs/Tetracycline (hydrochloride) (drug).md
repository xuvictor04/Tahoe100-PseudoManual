---
drug: "Tetracycline (hydrochloride)"
type: "drug"
salt_base: "Tetracycline"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 6
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Tetracycline (hydrochloride)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 6 / 2; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.11 / -0.27.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A3 | 2 / 2 | — | +0.30 | -0.1/+0.8/-0.3 | — |
| 0.5 µM | [[Plate 08]]:A3 | 0 / 6 | — | +0.09 | -0.0/+1.2/+0.8 | — |
| 5 µM | [[Plate 09]]:A3 | 1 / 1 | — | +1.03 | -0.8/-0.4/-2.1 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[MLIP]] 1.27× (z +3.0, 4/38 lines), [[ENSG00000286850]] 1.27× (z +3.0, 5/37 lines)

**5 µM** (1 gene, none with an alert): [[TOX2]] 1.23× (z +3.5, 6/30 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[DDIAS]] 0.745× (z -3.5, 10/46 lines), [[TREX2]] 0.804× (z -3.0, 5/45 lines)

**0.5 µM** (6 genes, none with an alert): [[FAM169A]] 0.818× (z -3.6, 4/35 lines), [[AARS2]] 0.806× (z -3.5, 9/47 lines), [[CSTF2T]] 0.748× (z -3.2, 11/45 lines), [[C17orf100]] 0.753× (z -3.2, 7/41 lines), [[MORN1]] 0.786× (z -3.0, 5/47 lines), [[SDC3]] 0.812× (z -2.9, 7/44 lines)

**5 µM** (1 gene, none with an alert): [[UBE2J2]] 0.807× (z -4.6, 13/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 170]] (+2.2) | — |

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

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Entecavir (monohydrate) (drug)]] (+0.77, unclear); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.75, unclear); [[Altretamine (drug)]] (+0.66, DNA synthesis/repair inhibitor, ⚠ only 1 significant gene); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.65, unclear); [[Silodosin (drug)]] (+0.64, unclear); [[Terfenadine (drug)]] (+0.63, unclear); [[Pasireotide (acetate) (drug)]] (+0.62, unclear); [[Fumaric acid (drug)]] (+0.58, unclear); [[Arbutin (drug)]] (+0.56, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 39 arrows, 39 of them with an alert ⚠; grade A 0, B 10, C 29. Shown: the 15 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PRDM5]] | 0.5 µM | B | PRDM5 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PRDM5 (13) vs lines expressing it (35) | the lines without PRDM5: 0.84× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[KLHL5]] | 0.5 µM | B | KLHL5 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLHL5 (7) vs lines expressing it (41) | the lines without KLHL5: 0.82× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[SLFN5]] | 0.5 µM | B | SLFN5 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.79× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[NLGN4X]] | 0.5 µM | B | NLGN4X activity lowers the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 1.06× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[RAB32]] | 0.5 µM | B | RAB32 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 0.82× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[EBI3]] | 0.5 µM | B | EBI3 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express EBI3 (12) vs lines expressing it (36) | the lines without EBI3: 0.82× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |
| [[SLC6A16]] | 0.5 µM | B | SLC6A16 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SLC6A16 (11) vs lines expressing it (37) | the lines without SLC6A16: 0.92× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, TEAD2, ZNF71; maybe low, not absent |
| [[DNAH11]] | 0.5 µM | B | DNAH11 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 0.83× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[FAS]] | 0.5 µM | B | FAS activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express FAS (8) vs lines expressing it (40) | the lines without FAS: 0.85× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[BASP1]] | 0.5 µM | B | BASP1 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express BASP1 (24) vs lines expressing it (24) | the lines without BASP1: 0.81× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| [[PHF11]] | 0.5 µM | C | PHF11 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.68× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[PSMB8]] | 0.5 µM | C | PSMB8 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.73× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[CEBPD]], [[GCA]] | 0.5 µM | C | CEBPD, GCA activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.67× the cells of the other lines | 0.006 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[PLS3]] | 0.5 µM | C | PLS3 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.74× the cells of the other lines | 0.019 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| [[LRRCC1]], [[OXR1]] | 0.5 µM | C | LRRCC1, OXR1 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.76× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Tetracycline (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 997, 998, 999
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

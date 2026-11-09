---
drug: "Procainamide (hydrochloride)"
type: "drug"
salt_base: "Procainamide"
targets: "DNMT1"
moa_fine: "DNA methyltransferase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 7
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Procainamide (hydrochloride)

*DNA methyltransferase inhibitor (inhibitor/antagonist) · targets: DNMT1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 1 / 7; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.23 / -0.06.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D11 | 2 / 0 | — | -0.31 | -0.2/-0.4/-0.4 | — |
| 0.5 µM | [[Plate 08]]:D11 | 1 / 0 | — | -0.52 | +0.3/+0.1/-0.5 | — |
| 5 µM | [[Plate 09]]:D11 | 5 / 2 | — | -0.18 | +1.7/+1.1/+0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ERFL]] 1.46× (z +3.3, 3/34 lines), [[ACBD4]] 1.32× (z +3.1, 2/42 lines)

**0.5 µM** (1 gene, none with an alert): [[CEP170B]] 1.31× (z +3.0, 10/47 lines)

**5 µM** (5 genes, none with an alert): [[TMEM266]] 1.46× (z +4.2, 3/38 lines), [[CFAP210]] 1.91× (z +3.4, 16/41 lines), [[ENSG00000159239]] 1.31× (z +3.3, 4/41 lines), [[ALPK2]] 1.34× (z +3.2, 0/16 lines), [[LAMA1]] 1.30× (z +3.0, 0/16 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (2 genes, none with an alert): [[ALG12]] 0.813× (z -3.6, 5/45 lines), [[PIGC]] 0.805× (z -2.9, 8/47 lines)

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
| 0.5 µM | [[A549 (line)]] (-3.5), [[HS-578T (line)]] (-3.0) | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 7 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Acetohexamide (drug)]] (+0.64, unclear); [[γ-Oryzanol (drug)]] (+0.52, DNA methyltransferase inhibitor, ⚠ only 1 significant gene); [[Mifepristone (drug)]] (+0.52, unclear); [[Brimonidine (drug)]] (+0.51, Adrenoceptor agonist); [[Norepinephrine (hydrochloride) (drug)]] (+0.50, Adrenoceptor agonist); [[Doxycycline (monohydrate) (drug)]] (+0.50, unclear); [[Proglumide (drug)]] (+0.48, unclear); [[Arbutin (drug)]] (+0.47, unclear); [[Bendamustine (drug)]] (+0.47, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 42 arrows, 42 of them with an alert ⚠; grade A 0, B 28, C 14. Shown: the 15 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.79× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[SIRLNT]] | 5 µM | B | SIRLNT activity raises the cells' numbers under Procainamide (hydrochloride) 5 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.79× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[SRPX]] | 0.5 µM | B | SRPX activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 1.20× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[PLA2G4A]] | 5 µM | B | PLA2G4A activity raises the cells' numbers under Procainamide (hydrochloride) 5 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.84× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[BNC2]] | 0.5 µM | B | BNC2 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.23× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[ZCCHC24]] | 0.5 µM | B | ZCCHC24 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ZCCHC24 (5) vs lines expressing it (43) | the lines without ZCCHC24: 1.26× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[SLC2A3]] | 0.5 µM | B | SLC2A3 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SLC2A3 (15) vs lines expressing it (33) | the lines without SLC2A3: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[PAPPA]] | 0.5 µM | B | PAPPA activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 1.25× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[KCNH8]] | 0.5 µM | B | KCNH8 activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 0.82× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[ENSG00000197813]] | 0.5 µM | B | ENSG00000197813 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000197813 (11) vs lines expressing it (37) | the lines without ENSG00000197813: 1.17× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC6A16, TEAD2, SLC2A3; maybe low, not absent |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.27× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[FAAH2]] | 0.5 µM | B | FAAH2 activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.79× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[FLI1]] | 5 µM | B | FLI1 activity raises the cells' numbers under Procainamide (hydrochloride) 5 µM (protects the cells) | lines that do not express FLI1 (31) vs lines expressing it (17) | the lines without FLI1: 0.82× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[ERBB3]] | 0.5 µM | B | ERBB3 activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.83× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Procainamide (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 842, 843, 844
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

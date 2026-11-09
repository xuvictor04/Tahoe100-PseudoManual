---
drug: "Methylprednisolone succinate"
type: "drug"
salt_base: "Methylprednisolone succinate"
targets: "NR3C1"
moa_fine: "Glucocorticoid receptor agonist"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 323
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Methylprednisolone succinate

*Glucocorticoid receptor agonist (unclear) · targets: NR3C1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 12 / 323 / 3; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.57 / 0.74.
> Flags by dose: unreliable plate only / low cells (technical?); noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.05 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:A10 | 2 / 10 | — | +0.19 | +0.4/-0.7/-1.6 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 02]]:G10 | 270 / 53 | — | -1.30 | -0.3/-0.2/+1.6 | low cells (technical?); noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G10 | 3 / 0 | — | -0.25 | +0.5/+0.5/+0.3 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, 2 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[LINC01934]] ⚠ 1.38× (z +3.1, 3/47 lines), [[ARHGAP4]] ⚠ 1.22× (z +2.9, 4/46 lines)

**0.5 µM** (270 genes, none with an alert; 12 shown): [[USP9Y]] 1.51× (z +4.9, 0/18 lines), [[FUT9]] 2.22× (z +4.5, 0/6 lines), [[LINC01967]] 1.98× (z +4.2, 0/8 lines), [[LINC00540]] 1.75× (z +4.2, 0/15 lines), [[ADGRV1]] 1.39× (z +4.1, 1/30 lines), [[VIPR1]] 1.86× (z +4.1, 1/18 lines), [[LINC02506]] 1.91× (z +4.0, 0/8 lines), [[LINC02476]] 1.70× (z +4.0, 0/8 lines), [[NLRP2]] 1.57× (z +3.9, 0/15 lines), [[UNC13A]] 1.55× (z +3.9, 3/18 lines), [[ZFY]] 1.48× (z +3.8, 0/19 lines), [[LSM7]] 2.04× (z +3.8, 31/47 lines)

**5 µM** (3 genes, none with an alert): [[TIPARP]] 1.58× (z +2.9, 18/47 lines), [[NFE2L2]] 1.22× (z +2.8, 15/48 lines), [[RMDN2-AS1]] 2.11× (z +2.8, 2/18 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, 10 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[LINC02474]] ⚠ 0.642× (z -3.7, 0/8 lines), [[C2CD4A]] ⚠ 0.518× (z -3.4, 1/9 lines), [[MAL2]] ⚠ 0.831× (z -3.3, 0/17 lines), [[ENSG00000251652]] ⚠ 0.715× (z -3.3, 0/11 lines), [[ENSG00000267284]] ⚠ 0.777× (z -3.3, 0/15 lines), [[USP9Y]] ⚠ 0.823× (z -3.2, 0/18 lines), [[SGPP2]] ⚠ 0.823× (z -3.2, 0/16 lines), [[HNF4A]] ⚠ 0.746× (z -3.1, 0/14 lines), [[MME]] ⚠ 0.797× (z -3.1, 0/18 lines), [[GRHL2]] ⚠ 0.826× (z -2.8, 0/14 lines)

**0.5 µM** (53 genes, none with an alert; 12 shown): [[MINPP1]] 0.679× (z -4.0, 18/45 lines), [[ZNF845]] 0.636× (z -4.0, 18/40 lines), [[TGFBRAP1]] 0.738× (z -4.0, 18/47 lines), [[SNX16]] 0.763× (z -3.8, 10/47 lines), [[MCUB]] 0.767× (z -3.8, 16/45 lines), [[GNS]] 0.722× (z -3.8, 21/48 lines), [[TMEM106B]] 0.752× (z -3.7, 19/48 lines), [[SACS]] 0.701× (z -3.6, 24/43 lines), [[GALNT4]] 0.671× (z -3.5, 14/47 lines), [[DOCK7]] 0.795× (z -3.4, 24/48 lines), [[DERA]] 0.765× (z -3.4, 18/48 lines), [[MBNL3]] 0.648× (z -3.4, 10/30 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 045]] (-2.1) |
| 0.5 µM | [[Module 048]] (+2.5), [[Module 024]] (+2.3), [[Module 003]] (+2.3) | [[Module 025]] (-2.6), [[Module 029]] (-2.5), [[Module 020]] (-2.2) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 1088 (line)]] (1.36), [[SW48 (line)]] (1.18), [[SW 1271 (line)]] (1.16), [[LOX-IMVI (line)]] (1.08) · weakest: [[NCI-H23 (line)]] (0.660), [[SW1417 (line)]] (0.666), [[SHP-77 (line)]] (0.675) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Celecoxib (drug)]] (+0.93, Cyclooxygenase inhibitor); [[Darolutamide (drug)]] (+0.87, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Ipatasertib (drug)]] (+0.87, PI3K/AKT inhibitor); [[Nimesulide (drug)]] (+0.85, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Tranilast (drug)]] (+0.84, unclear, ⚠ only 6 significant genes); [[Docetaxel (Trihydrate) (drug)]] (+0.84, Microtubule inhibitor); [[Bimatoprost (drug)]] (+0.82, unclear); [[Fingolimod (hydrochloride) (drug)]] (+0.81, unclear, ⚠ vector dose flagged: toxic); [[Erythromycin (drug)]] (+0.81, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.77, Glucose transporter inhibitor); [[Decitabine (drug)]] (+0.76, DNA methyltransferase inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.73, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 43 arrows, 43 of them with an alert ⚠; grade A 0, B 34, C 9. Shown: the 15 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[IL15]] | 0.5 µM | B | IL15 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.46× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[ATP1B1]] | 0.5 µM | B | ATP1B1 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 1.41× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[LGALS3BP]] | 0.5 µM | B | LGALS3BP activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.58× the cells of the other lines | 0.032 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity lowers the cells' numbers under Methylprednisolone succinate 5 µM (makes them more sensitive) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 1.28× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.37× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ENSG00000251537]] | 0.5 µM | B | ENSG00000251537 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 1.23× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[IGSF9]] | 0.5 µM | B | IGSF9 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express IGSF9 (16) vs lines expressing it (32) | the lines without IGSF9: 1.28× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[IL15]] | 5 µM | B | IL15 activity lowers the cells' numbers under Methylprednisolone succinate 5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.29× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[SPTLC3]] | 5 µM | B | SPTLC3 activity lowers the cells' numbers under Methylprednisolone succinate 5 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.25× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[PRKCA]] | 5 µM | B | PRKCA activity lowers the cells' numbers under Methylprednisolone succinate 5 µM (makes them more sensitive) | lines that do not express PRKCA (5) vs lines expressing it (43) | the lines without PRKCA: 1.35× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[TGFBR2]] | 0.5 µM | B | TGFBR2 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express TGFBR2 (7) vs lines expressing it (41) | the lines without TGFBR2: 1.50× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[AHR]] | 0.5 µM | B | AHR activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 1.39× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[AHR]] | 5 µM | B | AHR activity lowers the cells' numbers under Methylprednisolone succinate 5 µM (makes them more sensitive) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 1.29× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[SPTLC3]] | 0.5 µM | B | SPTLC3 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.32× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[MGST2]] | 0.5 µM | B | MGST2 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express MGST2 (10) vs lines expressing it (38) | the lines without MGST2: 1.39× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Methylprednisolone succinate"
- `tables/drugdoses.parquet` — dd in 678, 679, 680
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

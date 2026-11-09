---
drug: "AT7519"
type: "drug"
salt_base: "AT7519"
targets: "CDK2, CDK4, CDK5, CDK6, CDK9, CDK1, CDK7, GSK3B"
moa_fine: "CDK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 6
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# AT7519

*CDK inhibitor (inhibitor/antagonist) · targets: CDK2, CDK4, CDK5, CDK6, CDK9, CDK1, CDK7, GSK3B · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 0 / 6; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.05 / 0.28.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:H4 | 1 / 0 | — | +0.33 | +0.2/+0.7/+1.4 | — |
| 0.5 µM | [[Plate 02]]:H4 | 0 / 0 | — | +0.40 | -0.3/+0.3/-0.4 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:H4 | 2 / 4 | — | +0.49 | -0.5/-0.2/-0.1 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000232754]] 1.80× (z +6.4, 12/44 lines)

**5 µM** (2 genes, none with an alert): [[MSMO1]] 1.68× (z +2.9, 15/47 lines), [[TMEM184B]] 1.29× (z +2.9, 9/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (4 genes, none with an alert): [[PNPT1]] 0.713× (z -2.7, 8/47 lines), [[PARP9]] 0.663× (z -2.6, 11/41 lines), [[MX1]] 0.625× (z -2.6, 6/29 lines), [[HERC5]] 0.675× (z -2.6, 5/33 lines)

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
| 5 µM | [[COLO 205 (line)]] (-7.4), [[NCI-H1792 (line)]] (-6.7), [[SNU-1 (line)]] (-6.1), [[CHP-212 (line)]] (-5.4), [[H4 (line)]] (-5.3) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 6 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[APTO-253 (drug)]] (+0.72, unclear, ⚠ only 4 significant genes); [[ETC-206 (drug)]] (+0.70, Protein synthesis inhibitor, ⚠ only 0 significant genes); [[PF-06260933 (drug)]] (+0.64, Other MAPK inhibitor); [[Anastrozole (drug)]] (+0.62, unclear, ⚠ only 5 significant genes); [[SBI-0640756 (drug)]] (+0.60, Protein synthesis inhibitor); [[Fingolimod (hydrochloride) (drug)]] (+0.59, unclear, ⚠ vector dose flagged: toxic); [[Vilanterol (drug)]] (+0.59, Adrenoceptor agonist); [[Zileuton (drug)]] (+0.58, unclear, ⚠ only 4 significant genes); [[Naproxen (drug)]] (+0.53, Cyclooxygenase inhibitor); [[Erythromycin (drug)]] (+0.52, unclear); [[HI-TOPK-032 (drug)]] (+0.51, unclear); [[Methylprednisolone succinate (drug)]] (+0.50, Glucocorticoid receptor agonist); [[Bergenin (drug)]] (+0.50, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 20 arrows, 20 of them with an alert ⚠; grade A 0, B 4, C 16. Shown: the 15 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LINC01287]] | 5 µM | B | LINC01287 activity lowers the cells' numbers under AT7519 5 µM (makes them more sensitive) | lines that do not express LINC01287 (39) vs lines expressing it (9) | the lines without LINC01287: 1.42× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[CCND1]] | 5 µM | B | CCND1 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express CCND1 (7) vs lines expressing it (41) | the lines without CCND1: 0.60× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[SOX6]] | 5 µM | B | SOX6 activity lowers the cells' numbers under AT7519 5 µM (makes them more sensitive) | lines that do not express SOX6 (22) vs lines expressing it (26) | the lines without SOX6: 1.48× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[ENSG00000250137]] | 5 µM | B | ENSG00000250137 activity lowers the cells' numbers under AT7519 5 µM (makes them more sensitive) | lines that do not express ENSG00000250137 (31) vs lines expressing it (17) | the lines without ENSG00000250137: 1.14× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000232053, ENSG00000289600, AMPH; maybe low, not absent |
| [[ANG]], [[RNASE4]] | 5 µM | C | ANG, RNASE4 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.44× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| [[ENSG00000285458]] | 5 µM | C | ENSG00000285458 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 0.50× the cells of the other lines | 0.006 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[PHF11]] | 5 µM | C | PHF11 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.41× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[PLEKHN1]] | 5 µM | C | PLEKHN1 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.39× the cells of the other lines | 0.013 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| [[HES4]] | 5 µM | C | HES4 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.51× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| [[DDAH1]] | 5 µM | C | DDAH1 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express DDAH1 (3) vs lines expressing it (45) | the lines without DDAH1: 0.44× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| [[RARG]] | 5 µM | C | RARG activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.53× the cells of the other lines | 0.043 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| [[SDC3]] | 5 µM | C | SDC3 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.53× the cells of the other lines | 0.068 | ⚠ few lines (4 vs 46); across organs |
| [[RILP]] | 5 µM | C | RILP activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.48× the cells of the other lines | 0.085 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[LAMC1]] | 5 µM | C | LAMC1 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express LAMC1 (3) vs lines expressing it (45) | the lines without LAMC1: 0.54× the cells of the other lines | 0.086 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SLC36A4, CLTCL1, PALS2 |
| [[BCAP29]] | 5 µM | C | BCAP29's natural level raises the cells' numbers under AT7519 5 µM (protects the cells) | BCAP29's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.305 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "AT7519"
- `tables/drugdoses.parquet` — dd in 27, 28, 29
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

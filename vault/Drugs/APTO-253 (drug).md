---
drug: "APTO-253"
type: "drug"
salt_base: "APTO-253"
targets: "MYC, KLF4"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 4
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# APTO-253

*unclear (unclear) · targets: MYC, KLF4 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 0 / 4; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.04 / 0.37.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:H2 | 0 / 0 | — | +0.00 | -0.0/+0.3/-0.3 | — |
| 0.5 µM | [[Plate 02]]:H2 | 0 / 0 | — | +0.42 | +0.1/+1.0/+0.5 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:H2 | 0 / 4 | — | +0.33 | -0.8/-0.7/-0.3 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

No gene is significantly raised at any dose.

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (4 genes, none with an alert): [[TXNRD1]] 0.584× (z -4.6, 33/47 lines), [[NMRAL2P]] 0.439× (z -4.1, 11/28 lines), [[PIR]] 0.608× (z -3.6, 13/38 lines), [[UGT1A6]] 0.563× (z -3.2, 5/13 lines)

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

⚠ This drug's own vector: only 4 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[AT7519 (drug)]] (+0.72, CDK inhibitor, ⚠ only 6 significant genes); [[ETC-206 (drug)]] (+0.60, Protein synthesis inhibitor, ⚠ only 0 significant genes); [[Vilanterol (drug)]] (+0.59, Adrenoceptor agonist); [[PF-06260933 (drug)]] (+0.55, Other MAPK inhibitor); [[Anastrozole (drug)]] (+0.52, unclear, ⚠ only 5 significant genes); [[Fingolimod (hydrochloride) (drug)]] (+0.49, unclear, ⚠ vector dose flagged: toxic); [[Zileuton (drug)]] (+0.46, unclear, ⚠ only 4 significant genes); [[SBI-0640756 (drug)]] (+0.44, Protein synthesis inhibitor); [[Erythromycin (drug)]] (+0.42, unclear); [[Crizotinib (hydrochloride) (drug)]] (+0.41, Multi-TK inhibitor); [[ULK-101 (drug)]] (+0.41, unclear); [[Naproxen (drug)]] (+0.40, Cyclooxygenase inhibitor); [[Omeprazole (sodium) (drug)]] (+0.40, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 16 arrows, 16 of them with an alert ⚠; grade A 0, B 12, C 4. Shown: the 15 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AKT3]] | 5 µM | B | AKT3 activity raises the cells' numbers under APTO-253 5 µM (protects the cells) | lines that do not express AKT3 (16) vs lines expressing it (32) | the lines without AKT3: 0.86× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[MAML2]] | 0.05 µM | B | MAML2 activity lowers the cells' numbers under APTO-253 0.05 µM (makes them more sensitive) | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2: 1.24× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[CYP4F3]] | 5 µM | B | CYP4F3 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express CYP4F3 (29) vs lines expressing it (19) | the lines without CYP4F3: 1.21× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[ENSG00000285897]] | 5 µM | B | ENSG00000285897 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express ENSG00000285897 (27) vs lines expressing it (21) | the lines without ENSG00000285897: 1.16× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: RNF43, CRB3, KDF1 |
| [[EDN1]] | 5 µM | B | EDN1 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express EDN1 (27) vs lines expressing it (21) | the lines without EDN1: 1.21× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[LAMC2]] | 5 µM | B | LAMC2 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express LAMC2 (27) vs lines expressing it (21) | the lines without LAMC2: 1.18× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[S100A14]] | 5 µM | B | S100A14 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express S100A14 (33) vs lines expressing it (15) | the lines without S100A14: 1.20× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[LAMA3]] | 5 µM | B | LAMA3 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express LAMA3 (22) vs lines expressing it (26) | the lines without LAMA3: 1.20× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[NFATC2]] | 0.05 µM | B | NFATC2 activity lowers the cells' numbers under APTO-253 0.05 µM (makes them more sensitive) | lines that do not express NFATC2 (11) vs lines expressing it (37) | the lines without NFATC2: 1.19× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[PDE3B]] | 0.05 µM | B | PDE3B activity raises the cells' numbers under APTO-253 0.05 µM (protects the cells) | lines that do not express PDE3B (20) vs lines expressing it (28) | the lines without PDE3B: 0.88× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[ENSG00000225680]] | 5 µM | B | ENSG00000225680 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express ENSG00000225680 (33) vs lines expressing it (15) | the lines without ENSG00000225680: 1.13× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, EPS8L3, LINC02964 |
| [[GOLT1A]] | 5 µM | B | GOLT1A activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express GOLT1A (24) vs lines expressing it (24) | the lines without GOLT1A: 1.18× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[FZD6]] | 5 µM | C | FZD6 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 1.34× the cells of the other lines | 0.012 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| [[ENSG00000285458]] | 5 µM | C | ENSG00000285458 activity lowers the cells' numbers under APTO-253 5 µM (makes them more sensitive) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 1.29× the cells of the other lines | 0.040 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[PHF11]] | 0.05 µM | C | PHF11 activity lowers the cells' numbers under APTO-253 0.05 µM (makes them more sensitive) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 1.33× the cells of the other lines | 0.078 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "APTO-253"
- `tables/drugdoses.parquet` — dd in 24, 25, 26
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

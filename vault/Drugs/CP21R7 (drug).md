---
drug: "CP21R7"
type: "drug"
salt_base: "CP21R7"
targets: "GSK3B, PRKCA"
moa_fine: "GSK3 inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 1
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# CP21R7

*GSK3 inhibitor (inhibitor/antagonist) · targets: GSK3B, PRKCA · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 0 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.31 / 0.52.
> Flags by dose: - / plate-row cell shift; noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:E12 | 1 / 0 | — | -0.01 | +0.2/+0.6/+0.9 | — |
| 0.5 µM | [[Plate 02]]:E12 | 0 / 0 | — | -0.74 | +0.3/+0.2/+0.3 | plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:E12 | 0 / 0 | — | -0.40 | +1.2/+0.6/-0.0 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000232754]] 1.59× (z +5.0, 3/43 lines)

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
| 0.5 µM | [[NCI-H1573 (line)]] (-4.3) | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 1 significant gene. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Ornidazole (drug)]] (+0.68, unclear, ⚠ only 1 significant gene; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Omeprazole (sodium) (drug)]] (+0.68, unclear); [[Pimitespib (drug)]] (+0.66, unclear); [[Altretamine (drug)]] (+0.61, DNA synthesis/repair inhibitor, ⚠ only 1 significant gene); [[Voriconazole (drug)]] (+0.61, unclear, ⚠ only 6 significant genes); [[Arbutin (drug)]] (+0.56, unclear); [[Silodosin (drug)]] (+0.53, unclear); [[Tazarotene (drug)]] (+0.52, Retinoic receptor agonist); [[Minodronic acid (drug)]] (+0.50, unclear); [[Fluvoxamine (maleate) (drug)]] (+0.47, unclear); [[Sinomenine (drug)]] (+0.46, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 16 arrows, 16 of them with an alert ⚠; grade A 0, B 9, C 7. Shown: the 15 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AKT3]] | 0.5 µM | B | AKT3 activity raises the cells' numbers under CP21R7 0.5 µM (protects the cells) | lines that do not express AKT3 (16) vs lines expressing it (32) | the lines without AKT3: 0.87× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[SLC16A10]] | 0.5 µM | B | SLC16A10 activity raises the cells' numbers under CP21R7 0.5 µM (protects the cells) | lines that do not express SLC16A10 (15) vs lines expressing it (33) | the lines without SLC16A10: 0.85× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |
| [[MPZL3]] | 0.5 µM | B | MPZL3 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express MPZL3 (25) vs lines expressing it (23) | the lines without MPZL3: 1.27× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[ENSG00000225680]] | 0.5 µM | B | ENSG00000225680 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000225680 (33) vs lines expressing it (15) | the lines without ENSG00000225680: 1.19× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, EPS8L3, LINC02964 |
| [[IL15]] | 0.5 µM | B | IL15 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.33× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[RNF39]] | 0.5 µM | B | RNF39 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express RNF39 (30) vs lines expressing it (18) | the lines without RNF39: 1.22× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[TMC4]] | 0.5 µM | B | TMC4 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express TMC4 (26) vs lines expressing it (22) | the lines without TMC4: 1.19× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[CDH17]] | 0.5 µM | B | CDH17 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express CDH17 (40) vs lines expressing it (8) | the lines without CDH17: 1.29× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[ENSG00000232884]] | 0.5 µM | B | ENSG00000232884 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 1.33× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[PHF11]] | 0.5 µM | C | PHF11 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 1.46× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[PSMB8]] | 0.5 µM | C | PSMB8 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 1.37× the cells of the other lines | 0.046 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[LRRCC1]], [[OXR1]] | 0.5 µM | C | LRRCC1, OXR1 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 1.34× the cells of the other lines | 0.055 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| [[TBILA]] | 0.5 µM | C | TBILA activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.32× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[ENSG00000256029]] | 0.5 µM | C | ENSG00000256029 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000256029 (4) vs lines expressing it (44) | the lines without ENSG00000256029: 1.36× the cells of the other lines | 0.073 | ⚠ few lines (4 vs 46); across organs; also absent: ERRFI1, FXYD5, CAV2; maybe low, not absent |
| [[ISG20]] | 0.5 µM | C | ISG20 activity lowers the cells' numbers under CP21R7 0.5 µM (makes them more sensitive) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 1.34× the cells of the other lines | 0.076 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "CP21R7"
- `tables/drugdoses.parquet` — dd in 224, 225, 226
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

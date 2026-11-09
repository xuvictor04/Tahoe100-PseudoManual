---
drug: "Ritonavir"
type: "drug"
salt_base: "Ritonavir"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 37
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ritonavir

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 28 / 37; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.03 / 0.33.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D12 | 0 / 3 | — | -0.01 | +0.5/+0.4/+0.1 | — |
| 0.5 µM | [[Plate 05]]:D12 | 7 / 21 | — | -0.39 | +0.7/+0.6/+1.1 | — |
| 5 µM | [[Plate 14]]:D12 | 37 / 0 | 0.787 | -0.15 | +0.6/+0.8/+1.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (7 genes, none with an alert): [[ARL6]] 1.25× (z +3.4, 12/45 lines), [[PPT2]] 1.24× (z +3.3, 6/42 lines), [[AKT1]] 1.23× (z +3.3, 11/47 lines), [[GAD1]] 1.25× (z +3.2, 7/34 lines), [[PTCH1]] 1.23× (z +3.2, 9/46 lines), [[ULK3]] 1.27× (z +3.1, 6/44 lines), [[CD40]] 1.24× (z +3.0, 5/26 lines)

**5 µM** (37 genes, none with an alert; 12 shown): [[SCD]] 1.36× (z +6.2, 38/48 lines), [[FDFT1]] 1.31× (z +5.2, 36/47 lines), [[IDI1]] 1.31× (z +5.0, 35/48 lines), [[LDLR]] 1.26× (z +4.4, 25/46 lines), [[DHCR7]] 1.35× (z +4.3, 20/44 lines), [[OLMALINC]] 1.26× (z +4.2, 18/47 lines), [[HCN2]] 1.32× (z +4.2, 7/40 lines), [[ACAT2]] 1.22× (z +4.2, 14/48 lines), [[HMGCS1]] 1.27× (z +4.1, 26/47 lines), [[PNPLA3]] 1.21× (z +4.1, 8/45 lines), [[FDPS]] 1.26× (z +4.1, 26/48 lines), [[MVD]] 1.34× (z +4.0, 18/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[LINC01611]] 0.712× (z -3.5, 1/12 lines), [[MYOM3]] 0.685× (z -3.4, 4/18 lines), [[PDE4A]] 0.829× (z -3.0, 2/41 lines)

**0.5 µM** (21 genes, none with an alert; 12 shown): [[ENSG00000257735]] 0.587× (z -4.8, 11/35 lines), [[PEF1]] 0.768× (z -4.4, 18/44 lines), [[BTD]] 0.814× (z -4.3, 11/48 lines), [[BTN2A3P]] 0.695× (z -4.1, 10/38 lines), [[ENO4]] 0.725× (z -3.8, 12/43 lines), [[ZNF813]] 0.751× (z -3.7, 8/29 lines), [[ENSG00000258964]] 0.679× (z -3.7, 11/41 lines), [[CYRIA]] 0.735× (z -3.7, 2/23 lines), [[TEX22]] 0.712× (z -3.6, 17/44 lines), [[ENSG00000290832]] 0.764× (z -3.6, 10/43 lines), [[TRMO]] 0.766× (z -3.5, 11/45 lines), [[MMAA]] 0.781× (z -3.5, 6/42 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+2.8) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 900 (line)]] (1.86), [[Hs 766T (line)]] (1.72), [[LOX-IMVI (line)]] (1.71), [[hTERT-HPNE (line)]] (1.67) · weakest: [[NCI-H661 (line)]] (-0.435), [[NCI-H23 (line)]] (0.359), [[NCI-H2347 (line)]] (0.370) |
| 5 µM | — | [[LS 180 (line)]] (1.57), [[HCT15 (line)]] (1.40), [[COLO 205 (line)]] (1.39), [[SW 900 (line)]] (1.38) · weakest: [[SHP-77 (line)]] (0.254), [[CHP-212 (line)]] (0.346), [[AN3 CA (line)]] (0.375) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Celecoxib (drug)]] (+0.60, Cyclooxygenase inhibitor); [[Bimatoprost (drug)]] (+0.59, unclear); [[Tubulin inhibitor 6 (drug)]] (+0.59, Microtubule inhibitor, ⚠ only 2 significant genes); [[Bergenin (drug)]] (+0.55, unclear); [[Azithromycin (hydrate) (drug)]] (+0.54, unclear); [[Thymol (drug)]] (+0.52, unclear); [[Ipatasertib (drug)]] (+0.52, PI3K/AKT inhibitor); [[Methylprednisolone succinate (drug)]] (+0.52, Glucocorticoid receptor agonist); [[Drospirenone (drug)]] (+0.48, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[GALNT14]] | 0.5 µM | B | GALNT14 activity raises the cells' numbers under Ritonavir 0.5 µM (protects the cells) | lines that do not express GALNT14 (24) vs lines expressing it (24) | the lines without GALNT14: 0.90× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[SLC27A2]] | 0.5 µM | B | SLC27A2 activity raises the cells' numbers under Ritonavir 0.5 µM (protects the cells) | lines that do not express SLC27A2 (19) vs lines expressing it (29) | the lines without SLC27A2: 0.87× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[SEMA4G]] | 0.5 µM | C | SEMA4G activity raises the cells' numbers under Ritonavir 0.5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.82× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| [[CHCHD10]] | 0.5 µM | C | CHCHD10 activity raises the cells' numbers under Ritonavir 0.5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.83× the cells of the other lines | 0.086 | ⚠ tissue-confounded; across organs |
| [[ENSG00000288755]] | 0.5 µM | C | ENSG00000288755 activity raises the cells' numbers under Ritonavir 0.5 µM (protects the cells) | lines that do not express ENSG00000288755 (3) vs lines expressing it (45) | the lines without ENSG00000288755: 0.78× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); across organs; also absent: SLC25A45; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Ritonavir"
- `tables/drugdoses.parquet` — dd in 905, 906, 907
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

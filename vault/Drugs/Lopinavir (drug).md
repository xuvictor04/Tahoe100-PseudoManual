---
drug: "Lopinavir"
type: "drug"
salt_base: "Lopinavir"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 20
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Lopinavir

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 6 / 20; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.48 / 0.43.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D8 | 2 / 0 | — | -0.20 | +0.6/+0.3/+0.1 | — |
| 0.5 µM | [[Plate 11]]:D8 | 1 / 5 | — | +0.63 | +1.7/+1.0/+0.6 | — |
| 5 µM | [[Plate 12]]:D8 | 13 / 7 | — | -0.61 | +0.1/+0.2/+0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[MCOLN2]] 1.27× (z +3.2, 2/29 lines), [[GINS1]] 1.21× (z +2.8, 3/46 lines)

**0.5 µM** (1 gene, none with an alert): [[RPSA]] 1.25× (z +2.8, 15/48 lines)

**5 µM** (13 genes, none with an alert; 12 shown): [[FAM219B]] 1.38× (z +4.9, 16/47 lines), [[RPSA]] 1.35× (z +3.9, 20/47 lines), [[ETV4]] 1.25× (z +3.5, 9/45 lines), [[LRATD2]] 1.23× (z +3.4, 5/32 lines), [[ATIC]] 1.24× (z +3.4, 11/47 lines), [[PPT1]] 1.21× (z +3.3, 11/47 lines), [[DPAGT1]] 1.24× (z +3.3, 5/47 lines), [[CDK2]] 1.23× (z +3.3, 3/47 lines), [[RPS2P5]] 1.71× (z +3.3, 5/44 lines), [[P3H1]] 1.22× (z +3.2, 4/43 lines), [[GINS1]] 1.21× (z +2.9, 4/46 lines), [[HMGCR]] 1.22× (z +2.8, 10/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (5 genes, none with an alert): [[ANKDD1A]] 0.812× (z -3.5, 5/47 lines), [[PON3]] 0.743× (z -3.3, 0/25 lines), [[ENSG00000256417]] 0.751× (z -3.3, 1/20 lines), [[ENSG00000285868]] 0.728× (z -3.2, 5/41 lines), [[ACVR1C]] 0.792× (z -3.0, 11/42 lines)

**5 µM** (7 genes, none with an alert): [[ENSG00000289153]] 0.733× (z -3.4, 2/24 lines), [[ENSG00000283511]] 0.621× (z -3.3, 8/37 lines), [[LINC01031]] 0.779× (z -3.2, 7/46 lines), [[ENSG00000287306]] 0.772× (z -3.1, 6/30 lines), [[LINC02798]] 0.688× (z -3.1, 12/40 lines), [[MCF2]] 0.724× (z -3.0, 6/43 lines), [[ENSG00000240963]] 0.795× (z -2.9, 5/47 lines)

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
| 5 µM | [[SW 900 (line)]] (-4.1) | [[Panc 03.27 (line)]] (1.82), [[SW48 (line)]] (1.53), [[hTERT-HPNE (line)]] (1.49), [[J82 (line)]] (1.38) · weakest: [[H4 (line)]] (0.318), [[HepG2_C3A (line)]] (0.341), [[SW 1271 (line)]] (0.500) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Pemetrexed (drug)]] (+0.83, DNA synthesis/repair inhibitor); [[Mozavaptan (drug)]] (+0.73, unclear); [[Gallic acid (drug)]] (+0.69, Cyclooxygenase inhibitor); [[Fluvoxamine (drug)]] (+0.61, unclear); [[Asciminib (drug)]] (+0.59, Other TK inhibitor); [[Clonidine (hydrochloride) (drug)]] (+0.59, Adrenoceptor agonist, ⚠ only 4 significant genes); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.57, unclear); [[Temuterkib (drug)]] (+0.57, Other MAPK inhibitor, ⚠ only 3 significant genes); [[Adenine (drug)]] (+0.55, unclear); [[Tucatinib (drug)]] (+0.54, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under Lopinavir 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.19× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Lopinavir 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.15× the cells of the other lines | 0.066 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[ITPK1]] | 5 µM | C | ITPK1 activity raises the cells' numbers under Lopinavir 5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.80× the cells of the other lines | 0.067 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[PWWP2B]] | 5 µM | C | PWWP2B activity raises the cells' numbers under Lopinavir 5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.75× the cells of the other lines | 0.070 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Lopinavir 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.14× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[NR3C1]] | 5 µM | C | NR3C1 activity lowers the cells' numbers under Lopinavir 5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.16× the cells of the other lines | 0.096 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[SCAMP5]] | 5 µM | C | SCAMP5 activity raises the cells' numbers under Lopinavir 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.78× the cells of the other lines | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[ENSG00000286964]] | 5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Lopinavir 5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.17× the cells of the other lines | 0.099 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Lopinavir"
- `tables/drugdoses.parquet` — dd in 633, 634, 635
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Busulfan"
type: "drug"
salt_base: "Busulfan"
targets: ""
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 270
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Busulfan

*DNA synthesis/repair inhibitor (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 270 / 1 / 9; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.27 / 0.21.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E10 | 88 / 182 | — | +0.00 | +2.5/+1.7/-0.1 | — |
| 0.5 µM | [[Plate 05]]:E10 | 0 / 1 | — | +0.11 | -0.3/-0.8/-1.3 | — |
| 5 µM | [[Plate 14]]:E10 | 5 / 4 | 0.790 | -0.24 | +1.7/+1.4/-0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (88 genes, none with an alert; 12 shown): [[GALNT1]] 1.21× (z +4.9, 19/49 lines), [[TNC]] 1.51× (z +4.7, 12/26 lines), [[CD44]] 1.21× (z +3.9, 19/34 lines), [[LINC01776]] 1.55× (z +3.8, 5/18 lines), [[ENSG00000285016]] 1.40× (z +3.8, 24/48 lines), [[SAMD9]] 1.58× (z +3.8, 30/38 lines), [[NTN4]] 1.47× (z +3.8, 17/31 lines), [[SLC8A1]] 1.29× (z +3.7, 3/22 lines), [[SETBP1]] 1.36× (z +3.7, 12/30 lines), [[SEMA3A]] 1.28× (z +3.7, 12/30 lines), [[VCAN]] 1.27× (z +3.7, 6/21 lines), [[F2R]] 1.39× (z +3.7, 12/36 lines)

**5 µM** (5 genes, none with an alert): [[SORCS2]] 1.30× (z +4.6, 3/26 lines), [[ZNF681]] 1.29× (z +3.4, 3/29 lines), [[CSTF2T]] 1.23× (z +3.2, 7/46 lines), [[MAP1A]] 1.27× (z +2.9, 2/30 lines), [[HCG20]] 1.22× (z +2.9, 3/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (182 genes, none with an alert; 12 shown): [[TMEM185A]] 0.699× (z -5.2, 20/48 lines), [[RINT1]] 0.692× (z -5.2, 34/48 lines), [[AGAP3]] 0.715× (z -5.1, 25/48 lines), [[FBXO42]] 0.733× (z -4.7, 35/49 lines), [[DNAJC25]] 0.661× (z -4.7, 37/49 lines), [[SLC15A2]] 0.616× (z -4.7, 21/43 lines), [[PMS2CL]] 0.645× (z -4.5, 22/48 lines), [[ENSG00000284697]] 0.622× (z -4.5, 26/48 lines), [[ELP2]] 0.724× (z -4.4, 35/49 lines), [[GMCL1]] 0.761× (z -4.4, 29/49 lines), [[KLHL28]] 0.800× (z -4.3, 25/49 lines), [[PREPL]] 0.763× (z -4.3, 30/49 lines)

**0.5 µM** (1 gene, none with an alert): [[NSUN5P1]] 0.676× (z -3.8, 15/37 lines)

**5 µM** (4 genes, none with an alert): [[TBC1D17]] 0.825× (z -4.6, 19/48 lines), [[TRIB3]] 0.816× (z -3.8, 11/45 lines), [[ENTREP1]] 0.807× (z -3.1, 8/27 lines), [[SLC15A2]] 0.795× (z -2.8, 10/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 016]] (+2.6), [[Module 004]] (+2.6), [[Module 151]] (+2.1) | [[Module 179]] (-3.4), [[Module 207]] (-3.3), [[Module 041]] (-3.2) |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 179]] (-2.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[A-172 (line)]] (1.31), [[SW 1088 (line)]] (1.27), [[hTERT-HPNE (line)]] (1.27), [[H4 (line)]] (1.27) · weakest: [[BT-474 (line)]] (0.407), [[SHP-77 (line)]] (0.553), [[AN3 CA (line)]] (0.554) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[(R)-Verapamil (hydrochloride) (drug)]] (+0.94, unclear); [[Megestrol (drug)]] (+0.94, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Palmatine (chloride) (drug)]] (+0.94, unclear); [[Larotrectinib (drug)]] (+0.94, Other TK inhibitor); [[Retinoic acid (drug)]] (+0.90, Retinoic receptor agonist); [[Diphenhydramine (drug)]] (+0.87, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.86, unclear); [[Berbamine (drug)]] (+0.85, unclear); [[Diammonium Glycyrrhizinate (drug)]] (+0.82, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[IKZF3]] | 5 µM | B | IKZF3 activity lowers the cells' numbers under Busulfan 5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.09× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[SVIL]] | 5 µM | C | SVIL activity lowers the cells' numbers under Busulfan 5 µM (makes them more sensitive) | lines that do not express SVIL (3) vs lines expressing it (45) | the lines without SVIL: 1.30× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: DBN1, LAMC1, PLEC; maybe low, not absent |
| [[ATAD1]], [[PTEN]] | 5 µM | C | ATAD1, PTEN activity lowers the cells' numbers under Busulfan 5 µM (makes them more sensitive) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 1.18× the cells of the other lines | 0.094 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Busulfan"
- `tables/drugdoses.parquet` — dd in 221, 222, 223
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

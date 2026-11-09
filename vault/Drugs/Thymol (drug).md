---
drug: "Thymol"
type: "drug"
salt_base: "Thymol"
targets: "TRPA1"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 437
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Thymol

*unclear (activator/agonist) · targets: TRPA1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 12 / 437 / 120; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.08 / 0.29.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D6 | 5 / 7 | — | -0.75 | -0.3/-0.7/-0.4 | — |
| 0.5 µM | [[Plate 05]]:D6 | 385 / 52 | — | -0.85 | -1.5/-1.3/+0.0 | — |
| 5 µM | [[Plate 14]]:D6 | 73 / 47 | 0.912 | -0.33 | +3.1/+2.7/+1.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[NFATC4]] 1.49× (z +3.4, 3/28 lines), [[ANKRD7]] 1.29× (z +3.2, 2/32 lines), [[ILDR2]] 1.50× (z +3.1, 1/13 lines), [[POTEE]] 1.63× (z +3.0, 0/12 lines), [[BHLHE40-AS1]] 1.20× (z +3.0, 1/44 lines)

**0.5 µM** (385 genes, none with an alert; 12 shown): [[TMEM255B]] 1.87× (z +6.1, 14/26 lines), [[CCNYL2]] 1.61× (z +6.0, 1/12 lines), [[MIR4527HG]] 1.94× (z +5.9, 3/11 lines), [[TOM1]] 1.38× (z +5.4, 30/48 lines), [[SEMA6C]] 1.65× (z +5.2, 7/27 lines), [[KLRC4-KLRK1]] 1.81× (z +5.2, 5/13 lines), [[ZNF628]] 1.59× (z +5.2, 7/33 lines), [[ZFYVE19]] 1.46× (z +5.0, 17/43 lines), [[AKT1]] 1.36× (z +4.9, 25/44 lines), [[ZNF692]] 1.35× (z +4.8, 16/45 lines), [[TMEM120A]] 1.43× (z +4.7, 15/43 lines), [[SLC19A1]] 1.37× (z +4.6, 14/43 lines)

**5 µM** (73 genes, none with an alert; 12 shown): [[NCAPH]] 1.22× (z +4.4, 13/47 lines), [[SUPT16H]] 1.22× (z +4.3, 30/48 lines), [[ESCO2]] 1.33× (z +4.1, 13/47 lines), [[PHF23]] 1.24× (z +4.1, 5/48 lines), [[HMGB3]] 1.29× (z +4.0, 26/47 lines), [[CCT5]] 1.24× (z +3.9, 28/48 lines), [[HSPB8]] 1.28× (z +3.9, 8/47 lines), [[SIX1]] 1.34× (z +3.8, 11/39 lines), [[MKI67]] 1.27× (z +3.7, 35/48 lines), [[RRM1]] 1.21× (z +3.6, 17/47 lines), [[TUBA1A]] 1.27× (z +3.6, 15/38 lines), [[CENPF]] 1.23× (z +3.6, 23/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[PLBD2]] 0.804× (z -4.3, 10/48 lines), [[TARBP2]] 0.759× (z -3.8, 7/43 lines), [[MT-ND1]] 0.625× (z -3.8, 43/48 lines), [[ADORA2A]] 0.704× (z -3.6, 10/40 lines), [[FGFRL1]] 0.731× (z -3.4, 9/44 lines), [[TRIM3]] 0.778× (z -3.1, 14/47 lines), [[MT-ND4L]] 0.639× (z -3.1, 28/48 lines)

**0.5 µM** (52 genes, none with an alert; 12 shown): [[SLK]] 0.784× (z -6.3, 33/48 lines), [[BMS1]] 0.765× (z -5.7, 31/48 lines), [[ADSS2]] 0.793× (z -5.3, 27/48 lines), [[RAD21]] 0.753× (z -5.2, 39/48 lines), [[MIA3]] 0.825× (z -5.2, 25/48 lines), [[TOP2B]] 0.750× (z -5.0, 35/48 lines), [[ZMPSTE24]] 0.793× (z -4.9, 24/47 lines), [[DNAJC13]] 0.769× (z -4.8, 31/48 lines), [[SNX16]] 0.787× (z -4.8, 15/44 lines), [[BROX]] 0.825× (z -4.6, 22/48 lines), [[ZNF273]] 0.780× (z -4.5, 14/42 lines), [[BIRC3]] 0.772× (z -4.4, 26/43 lines)

**5 µM** (47 genes, none with an alert; 12 shown): [[MINDY3]] 0.826× (z -4.5, 21/48 lines), [[GTF2IP4]] 0.771× (z -4.2, 12/43 lines), [[PDE4DIPP2]] 0.800× (z -4.2, 14/40 lines), [[RRN3P1]] 0.723× (z -4.2, 15/37 lines), [[LRIG2]] 0.815× (z -4.2, 26/48 lines), [[CNNM2]] 0.806× (z -4.2, 29/48 lines), [[RINT1]] 0.805× (z -4.1, 27/48 lines), [[NISCH]] 0.828× (z -4.1, 21/48 lines), [[ARAP1]] 0.811× (z -4.0, 24/48 lines), [[EEF1AKMT3]] 0.802× (z -4.0, 11/46 lines), [[AADAT]] 0.812× (z -4.0, 10/40 lines), [[MIR29B2CHG]] 0.806× (z -4.0, 25/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 048]] (+2.6), [[Module 002]] (+2.2), [[Module 218]] (+2.2) | [[Module 025]] (-2.6), [[Module 029]] (-2.5) |
| 5 µM | [[Module 060]] (+2.8) | [[Module 179]] (-3.4), [[Module 207]] (-2.8), [[Module 171]] (-2.7) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[HCT15 (line)]] (-3.6), [[AsPC-1 (line)]] (-3.4) | [[SW 1088 (line)]] (1.85), [[SW 1271 (line)]] (1.63), [[NCI-H661 (line)]] (1.63), [[CHP-212 (line)]] (1.53) · weakest: [[A-427 (line)]] (0.425), [[NCI-H2347 (line)]] (0.499), [[HOP62 (line)]] (0.516) |
| 5 µM | — | [[SW 1088 (line)]] (1.50), [[H4 (line)]] (1.12), [[COLO 205 (line)]] (1.11), [[hTERT-HPNE (line)]] (1.10) · weakest: [[CHP-212 (line)]] (0.512), [[SW 1271 (line)]] (0.569), [[RPMI-7951 (line)]] (0.611) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Ipatasertib (drug)]] (+0.89, PI3K/AKT inhibitor); [[Hydroxyurea (drug)]] (+0.85, DNA synthesis/repair inhibitor); [[Nimesulide (drug)]] (+0.84, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[LY-2584702 (tosylate salt) (drug)]] (+0.81, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Celecoxib (drug)]] (+0.81, Cyclooxygenase inhibitor); [[9-ING-41 (drug)]] (+0.79, GSK3 inhibitor); [[Tubulin inhibitor 6 (drug)]] (+0.78, Microtubule inhibitor, ⚠ only 2 significant genes); [[Canagliflozin (drug)]] (+0.75, Glucose transporter inhibitor); [[Methylprednisolone succinate (drug)]] (+0.72, Glucocorticoid receptor agonist); [[Pyridoxine (drug)]] (+0.70, unclear); [[Bimatoprost (drug)]] (+0.70, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ZNF22]] | 0.5 µM | B | ZNF22 activity raises the cells' numbers under Thymol 0.5 µM (protects the cells) | lines that do not express ZNF22 (5) vs lines expressing it (43) | the lines without ZNF22: 0.74× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: DAB2IP, CAPN5 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Thymol"
- `tables/drugdoses.parquet` — dd in 1000, 1001, 1002
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Gallic acid (hydrate)"
type: "drug"
salt_base: "Gallic acid"
targets: ""
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 185
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Gallic acid (hydrate)

*Cyclooxygenase inhibitor (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 185 / 30 / 9; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.10 / -0.01.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B4 | 47 / 138 | — | +0.01 | +2.8/+2.8/+1.5 | — |
| 0.5 µM | [[Plate 05]]:B4 | 26 / 4 | — | -0.33 | -0.4/+0.3/-0.1 | — |
| 5 µM | [[Plate 14]]:B4 | 0 / 9 | 0.331 | -0.08 | -0.5/-0.1/-0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (47 genes, none with an alert; 12 shown): [[CENPE]] 1.26× (z +4.0, 18/48 lines), [[C21orf58]] 1.40× (z +3.7, 16/43 lines), [[SPDL1]] 1.36× (z +3.6, 23/45 lines), [[ENSG00000285816]] 1.32× (z +3.6, 6/45 lines), [[FERMT1]] 1.33× (z +3.6, 10/26 lines), [[ARHGEF39]] 1.40× (z +3.5, 4/44 lines), [[CIP2A]] 1.25× (z +3.5, 19/47 lines), [[GTSE1]] 1.36× (z +3.4, 19/47 lines), [[ZNF75A]] 1.35× (z +3.4, 14/47 lines), [[PRSS23]] 1.32× (z +3.4, 17/35 lines), [[KIF4A]] 1.21× (z +3.3, 13/47 lines), [[SPC24]] 1.32× (z +3.3, 15/48 lines)

**0.5 µM** (26 genes, none with an alert; 12 shown): [[PIM1]] 1.62× (z +5.0, 27/43 lines), [[EFEMP2]] 1.59× (z +4.5, 14/40 lines), [[PHF2]] 1.23× (z +4.4, 15/48 lines), [[A3GALT2]] 1.70× (z +4.0, 6/32 lines), [[PET100]] 1.64× (z +3.9, 7/41 lines), [[SIPA1]] 1.34× (z +3.8, 6/41 lines), [[FCHSD1]] 1.37× (z +3.7, 15/42 lines), [[RXRB]] 1.29× (z +3.6, 17/48 lines), [[DMWD]] 1.25× (z +3.6, 6/45 lines), [[KCTD15]] 1.29× (z +3.5, 4/38 lines), [[DTX3]] 1.36× (z +3.5, 4/29 lines), [[TEPSIN]] 1.36× (z +3.4, 6/39 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (138 genes, none with an alert; 12 shown): [[MIR3659HG]] 0.561× (z -4.9, 13/39 lines), [[ENSG00000257759]] 0.712× (z -4.8, 30/47 lines), [[EOLA2]] 0.511× (z -4.6, 29/46 lines), [[SLC15A2]] 0.620× (z -4.6, 18/44 lines), [[MT-RNR1]] 0.465× (z -4.5, 48/48 lines), [[TNKS1BP1]] 0.704× (z -4.5, 32/48 lines), [[MAX]] 0.770× (z -4.4, 33/48 lines), [[ENSG00000266931]] 0.618× (z -4.3, 18/44 lines), [[UBE2O]] 0.768× (z -4.2, 28/48 lines), [[CNNM2]] 0.760× (z -4.2, 30/48 lines), [[LNX2]] 0.780× (z -4.2, 23/48 lines), [[HK2]] 0.590× (z -4.2, 44/48 lines)

**0.5 µM** (4 genes, none with an alert): [[DDX56]] 0.782× (z -3.8, 14/47 lines), [[MAOA]] 0.780× (z -3.4, 2/30 lines), [[ATP6AP2]] 0.819× (z -3.4, 20/48 lines), [[ENSG00000290890]] 0.816× (z -3.1, 10/47 lines)

**5 µM** (9 genes, none with an alert): [[MT-RNR1]] 0.595× (z -4.3, 49/49 lines), [[KCNQ4]] 0.779× (z -4.2, 9/36 lines), [[TTYH3]] 0.832× (z -4.1, 12/47 lines), [[B4GALT7]] 0.810× (z -3.9, 13/47 lines), [[NSMF]] 0.803× (z -3.7, 20/46 lines), [[KMT2B]] 0.811× (z -3.6, 20/48 lines), [[SAMD10]] 0.787× (z -3.5, 10/36 lines), [[MT-CO1]] 0.823× (z -3.2, 33/49 lines), [[PSMB10]] 0.755× (z -3.0, 11/46 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 179]] (-3.3), [[Module 207]] (-2.9), [[Module 041]] (-2.5) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[HEC-1-A (line)]] (-3.1) | [[H4 (line)]] (1.33), [[LS 180 (line)]] (1.25), [[SW48 (line)]] (1.22), [[NCI-H1573 (line)]] (1.21) · weakest: [[AN3 CA (line)]] (0.558), [[BT-474 (line)]] (0.589), [[NCI-H2347 (line)]] (0.656) |
| 0.5 µM | — | [[SW 1271 (line)]] (2.08), [[SW 1088 (line)]] (1.90), [[BT-474 (line)]] (1.50), [[CHP-212 (line)]] (1.49) · weakest: [[SW1417 (line)]] (0.325), [[SW48 (line)]] (0.342), [[A549 (line)]] (0.474) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Diammonium Glycyrrhizinate (drug)]] (+0.87, unclear); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.85, unclear); [[Berbamine (drug)]] (+0.83, unclear); [[Palmatine (chloride) (drug)]] (+0.81, unclear); [[Larotrectinib (drug)]] (+0.79, Other TK inhibitor); [[Busulfan (drug)]] (+0.78, DNA synthesis/repair inhibitor); [[Megestrol (drug)]] (+0.78, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Retinoic acid (drug)]] (+0.74, Retinoic receptor agonist); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.73, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 23 arrows, 23 of them with an alert ⚠; grade A 0, B 15, C 8. Shown: the 15 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FOXQ1]] | 0.05 µM | B | FOXQ1 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express FOXQ1 (30) vs lines expressing it (18) | the lines without FOXQ1: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[SERPINB5]] | 0.05 µM | B | SERPINB5 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express SERPINB5 (34) vs lines expressing it (14) | the lines without SERPINB5: 1.20× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[INAVA]], [[MROH3P]] | 0.05 µM | B | INAVA, MROH3P activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express INAVA, MROH3P (29) vs lines expressing them (19) | the lines without INAVA, MROH3P: 1.21× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[IL1R2]] | 0.05 µM | B | IL1R2 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express IL1R2 (23) vs lines expressing it (25) | the lines without IL1R2: 1.18× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[TSPAN13]] | 0.05 µM | B | TSPAN13 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express TSPAN13 (13) vs lines expressing it (35) | the lines without TSPAN13: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| [[TRIM15]] | 0.05 µM | B | TRIM15 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express TRIM15 (34) vs lines expressing it (14) | the lines without TRIM15: 1.22× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[RNF39]] | 0.05 µM | B | RNF39 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express RNF39 (30) vs lines expressing it (18) | the lines without RNF39: 1.18× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[LYPD3]] | 0.05 µM | B | LYPD3 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express LYPD3 (15) vs lines expressing it (33) | the lines without LYPD3: 1.15× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[RGS4]] | 0.05 µM | B | RGS4 activity raises the cells' numbers under Gallic acid (hydrate) 0.05 µM (protects the cells) | lines that do not express RGS4 (35) vs lines expressing it (13) | the lines without RGS4: 0.87× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[KRT6A]] | 0.05 µM | B | KRT6A activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express KRT6A (41) vs lines expressing it (7) | the lines without KRT6A: 1.22× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[AQP3]] | 0.05 µM | B | AQP3 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 1.16× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[MPZL3]] | 0.05 µM | B | MPZL3 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express MPZL3 (25) vs lines expressing it (23) | the lines without MPZL3: 1.18× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[VWA2]] | 0.05 µM | B | VWA2 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express VWA2 (36) vs lines expressing it (12) | the lines without VWA2: 1.23× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| [[SLC44A3]] | 0.05 µM | B | SLC44A3 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express SLC44A3 (13) vs lines expressing it (35) | the lines without SLC44A3: 1.18× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[MT1G]] | 0.05 µM | B | MT1G activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express MT1G (31) vs lines expressing it (17) | the lines without MT1G: 1.15× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Gallic acid (hydrate)"
- `tables/drugdoses.parquet` — dd in 495, 496, 497
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

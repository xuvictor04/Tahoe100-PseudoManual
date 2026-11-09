---
drug: "Malotilate"
type: "drug"
salt_base: "Malotilate"
targets: "ALOX5"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 29
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Malotilate

*unclear (inhibitor/antagonist) · targets: ALOX5 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 29 / 24 / 11; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.26 / 0.43.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:E6 | 17 / 12 | — | +0.00 | +0.4/+0.2/-0.1 | — |
| 0.5 µM | [[Plate 11]]:E6 | 2 / 22 | — | +0.05 | +0.6/-0.0/+0.7 | — |
| 5 µM | [[Plate 12]]:E6 | 0 / 11 | — | +0.11 | +0.0/+0.0/-0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (17 genes, none with an alert; 12 shown): [[FN1]] 1.39× (z +4.0, 0/19 lines), [[MMP2]] 1.44× (z +3.9, 2/14 lines), [[ADAMTS1]] 1.34× (z +3.4, 2/21 lines), [[ADGRD1]] 1.52× (z +3.3, 0/10 lines), [[LOX]] 1.34× (z +3.3, 1/17 lines), [[RYR2]] 1.38× (z +3.2, 7/46 lines), [[DUSP10]] 1.29× (z +3.2, 14/37 lines), [[SLCO5A1]] 1.25× (z +3.2, 5/40 lines), [[TENM4]] 1.31× (z +3.2, 0/17 lines), [[FBN1]] 1.22× (z +3.1, 0/20 lines), [[MMP1]] 1.61× (z +3.1, 4/21 lines), [[RPL3]] 1.32× (z +3.1, 35/48 lines)

**0.5 µM** (2 genes, none with an alert): [[WNK2]] 1.22× (z +3.2, 1/32 lines), [[LINC00457]] 1.43× (z +3.0, 0/12 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (12 genes, none with an alert): [[TMEM80]] 0.701× (z -4.5, 5/43 lines), [[DTD2]] 0.774× (z -4.1, 10/46 lines), [[ENSG00000259066]] 0.681× (z -3.7, 4/43 lines), [[DMAC2L]] 0.809× (z -3.6, 9/47 lines), [[PYGO1]] 0.750× (z -3.5, 11/31 lines), [[CNN3-DT]] 0.702× (z -3.5, 5/31 lines), [[EPM2A]] 0.718× (z -3.4, 15/44 lines), [[BRPF3-AS1]] 0.691× (z -3.2, 10/44 lines), [[THBS4]] 0.690× (z -3.2, 11/39 lines), [[HESX1]] 0.769× (z -2.9, 9/40 lines), [[HGSNAT]] 0.814× (z -2.8, 17/47 lines), [[ARMC2]] 0.830× (z -2.7, 5/46 lines)

**0.5 µM** (22 genes, none with an alert; 12 shown): [[LANCL1-AS1]] 0.670× (z -4.2, 9/42 lines), [[SFTA3-1]] 0.583× (z -3.9, 3/11 lines), [[SLFN12]] 0.737× (z -3.7, 4/24 lines), [[ENSG00000291032]] 0.748× (z -3.6, 7/21 lines), [[RNF212]] 0.732× (z -3.5, 2/12 lines), [[FAR2P1]] 0.733× (z -3.5, 10/19 lines), [[SLC37A2]] 0.736× (z -3.4, 3/27 lines), [[TXLNGY]] 0.772× (z -3.4, 3/18 lines), [[SYTL1]] 0.716× (z -3.4, 6/27 lines), [[ENSG00000234139]] 0.697× (z -3.3, 8/30 lines), [[NPIPB2]] 0.756× (z -3.3, 11/43 lines), [[NEK5]] 0.764× (z -3.3, 11/41 lines)

**5 µM** (11 genes, none with an alert): [[ENSG00000251388]] 0.555× (z -3.8, 5/12 lines), [[GRM8]] 0.711× (z -3.8, 9/43 lines), [[BVES-AS1]] 0.680× (z -3.5, 5/27 lines), [[ENSG00000266573]] 0.590× (z -3.5, 2/8 lines), [[SLC66A1L]] 0.687× (z -3.5, 1/21 lines), [[MT-ND4L]] 0.603× (z -3.5, 41/48 lines), [[ENSG00000257062]] 0.776× (z -3.4, 3/19 lines), [[CSRNP3]] 0.694× (z -3.3, 3/23 lines), [[MAGOH]] 0.831× (z -3.3, 8/48 lines), [[LINC00648]] 0.660× (z -3.3, 6/12 lines), [[ASS1]] 0.831× (z -2.8, 2/34 lines)

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
| 0.05 µM | — | [[AN3 CA (line)]] (2.18), [[NCI-H661 (line)]] (1.83), [[RKO (line)]] (1.65), [[SW 1271 (line)]] (1.60) · weakest: [[SW 1088 (line)]] (0.273), [[NCI-H23 (line)]] (0.332), [[A-172 (line)]] (0.450) |
| 0.5 µM | — | [[CFPAC-1 (line)]] (2.04), [[RPMI-7951 (line)]] (1.76), [[Panc 03.27 (line)]] (1.76), [[HEC-1-A (line)]] (1.75) · weakest: [[AN3 CA (line)]] (-0.466), [[SW 1271 (line)]] (-0.229), [[CHP-212 (line)]] (-0.184) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Uridine (drug)]] (+0.79, unclear, ⚠ only 6 significant genes); [[Methylthiouracil (drug)]] (+0.73, unclear, ⚠ only 9 significant genes); [[Clopidogrel (drug)]] (+0.68, unclear); [[Cloxacillin (sodium) (drug)]] (+0.67, unclear); [[Artemether (drug)]] (+0.63, unclear, ⚠ only 7 significant genes); [[Allopurinol (drug)]] (+0.62, unclear); [[Methyl aminolevulinate (hydrochloride) (drug)]] (+0.59, unclear, ⚠ only 3 significant genes); [[Hesperidin (drug)]] (+0.57, unclear); [[Pentoxifylline (drug)]] (+0.56, unclear); [[Tazarotene (drug)]] (+0.54, Retinoic receptor agonist); [[Methotrexate (drug)]] (+0.51, DNA synthesis/repair inhibitor); [[Ranolazine (drug)]] (+0.43, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 15 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PRR36]] | 0.05 µM | B | PRR36 activity lowers the cells' numbers under Malotilate 0.05 µM (makes them more sensitive) | lines that do not express PRR36 (19) vs lines expressing it (29) | the lines without PRR36: 1.20× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[MYH14]] | 0.05 µM | B | MYH14 activity lowers the cells' numbers under Malotilate 0.05 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.23× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[PAPPA]] | 0.05 µM | B | PAPPA activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.79× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[TMC6]] | 0.05 µM | B | TMC6 activity lowers the cells' numbers under Malotilate 0.05 µM (makes them more sensitive) | lines that do not express TMC6 (12) vs lines expressing it (36) | the lines without TMC6: 1.26× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[HTRA3]] | 0.05 µM | B | HTRA3 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express HTRA3 (31) vs lines expressing it (17) | the lines without HTRA3: 0.81× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[C12orf75-AS1]] | 0.05 µM | B | C12orf75-AS1 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express C12orf75-AS1 (22) vs lines expressing it (26) | the lines without C12orf75-AS1: 0.82× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[GJA1]] | 0.05 µM | B | GJA1 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 0.82× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[MSRB3]] | 0.05 µM | B | MSRB3 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 0.84× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[PLA2G4A]] | 0.05 µM | B | PLA2G4A activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.87× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[HTRA1]] | 0.05 µM | B | HTRA1 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express HTRA1 (19) vs lines expressing it (29) | the lines without HTRA1: 0.83× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[SRPX]] | 0.05 µM | B | SRPX activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 0.87× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[SIRLNT]] | 0.05 µM | B | SIRLNT activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.80× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[ARHGEF6]] | 0.05 µM | B | ARHGEF6 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 0.84× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[ZNF469]] | 0.05 µM | B | ZNF469 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express ZNF469 (20) vs lines expressing it (28) | the lines without ZNF469: 0.82× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[RAB11FIP1]] | 0.05 µM | C | RAB11FIP1 activity lowers the cells' numbers under Malotilate 0.05 µM (makes them more sensitive) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 1.39× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Malotilate"
- `tables/drugdoses.parquet` — dd in 654, 655, 656
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

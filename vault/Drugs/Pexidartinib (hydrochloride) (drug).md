---
drug: "Pexidartinib (hydrochloride)"
type: "drug"
salt_base: "Pexidartinib"
targets: "CSF1R, KIT, FLT3"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 57
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pexidartinib (hydrochloride)

*Multi-TK inhibitor (inhibitor/antagonist) · targets: CSF1R, KIT, FLT3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 18 / 11 / 57; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.23 / 0.50.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C8 | 0 / 18 | — | +0.37 | -0.2/-0.3/-1.4 | — |
| 0.5 µM | [[Plate 08]]:C8 | 5 / 6 | — | +0.35 | +1.1/+0.0/-1.0 | — |
| 5 µM | [[Plate 09]]:C8 | 21 / 36 | — | +0.44 | -1.0/-0.5/-2.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (5 genes, none with an alert): [[WWOX]] 1.32× (z +3.4, 21/43 lines), [[TMEM45A]] 1.32× (z +3.4, 9/35 lines), [[MACROD2]] 1.27× (z +3.2, 17/38 lines), [[ENSG00000273149]] 1.51× (z +3.1, 5/45 lines), [[SLC35B4]] 1.22× (z +2.8, 3/47 lines)

**5 µM** (21 genes, none with an alert; 12 shown): [[ST3GAL1]] 1.28× (z +4.6, 19/37 lines), [[PLIN2]] 1.68× (z +4.3, 21/31 lines), [[CPT1A]] 1.25× (z +4.2, 18/46 lines), [[ETFDH]] 1.21× (z +3.9, 8/48 lines), [[ZNF7]] 1.24× (z +3.7, 11/47 lines), [[STK10]] 1.21× (z +3.6, 15/48 lines), [[KLF11]] 1.29× (z +3.6, 3/46 lines), [[P2RY11]] 1.34× (z +3.5, 10/47 lines), [[IFT140]] 1.23× (z +3.5, 12/48 lines), [[CPNE2]] 1.21× (z +3.4, 4/45 lines), [[EPAS1]] 1.24× (z +3.4, 17/39 lines), [[C6orf141]] 1.38× (z +3.4, 4/26 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (18 genes, none with an alert; 12 shown): [[TMEM30B]] 0.647× (z -4.1, 0/13 lines), [[EPB41L4A]] 0.779× (z -3.9, 1/22 lines), [[FOXG1]] 0.547× (z -3.9, 1/10 lines), [[PAX3]] 0.647× (z -3.8, 0/10 lines), [[ZNF730]] 0.669× (z -3.8, 0/18 lines), [[SLCO1B3]] 0.809× (z -3.6, 0/20 lines), [[OLFM1]] 0.660× (z -3.5, 3/18 lines), [[ENSG00000231317]] 0.548× (z -3.5, 2/11 lines), [[MED18]] 0.738× (z -3.5, 7/46 lines), [[ENSG00000256915]] 0.683× (z -3.4, 2/26 lines), [[LINC02474]] 0.606× (z -3.4, 0/8 lines), [[LINC02864]] 0.763× (z -3.2, 0/12 lines)

**0.5 µM** (6 genes, none with an alert): [[CYRIA]] 0.735× (z -3.7, 2/24 lines), [[ZNF732]] 0.533× (z -3.4, 0/7 lines), [[WHAMM]] 0.814× (z -3.2, 14/48 lines), [[PPTC7]] 0.809× (z -3.1, 12/48 lines), [[TGDS]] 0.815× (z -3.0, 6/48 lines), [[GALNT3]] 0.827× (z -3.0, 0/18 lines)

**5 µM** (36 genes, none with an alert; 12 shown): [[SYN2]] 0.545× (z -6.2, 13/23 lines), [[MXRA8]] 0.504× (z -4.8, 1/12 lines), [[RMEL3]] 0.479× (z -4.6, 4/13 lines), [[ZNF727]] 0.574× (z -4.4, 1/12 lines), [[TXLNGY-1]] 0.693× (z -4.2, 0/17 lines), [[C16orf87]] 0.717× (z -4.0, 18/48 lines), [[NAALADL2-AS2]] 0.504× (z -3.9, 1/11 lines), [[ATG3]] 0.776× (z -3.8, 22/48 lines), [[HOOK1]] 0.826× (z -3.8, 2/26 lines), [[TP53I11]] 0.730× (z -3.8, 7/41 lines), [[PEG10]] 0.755× (z -3.8, 9/31 lines), [[ENSG00000286046]] 0.601× (z -3.8, 4/39 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 048]] (-2.6), [[Module 059]] (-2.3), [[Module 024]] (-2.2) |
| 0.5 µM | — | — |
| 5 µM | [[Module 170]] (+2.9) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[HEC-1-A (line)]] (1.45), [[NCI-H1573 (line)]] (1.37), [[A-172 (line)]] (1.28), [[HT-29 (line)]] (1.26) · weakest: [[SNU-423 (line)]] (0.538), [[SHP-77 (line)]] (0.560), [[SW 1088 (line)]] (0.572) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Tirabrutinib (hydrochloride) (drug)]] (+0.50, Other TK inhibitor); [[4EGI-1 (drug)]] (+0.48, Protein synthesis inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Ivermectin (drug)]] (+0.46, unclear); [[Pentagastrin (drug)]] (+0.45, unclear, ⚠ only 9 significant genes); [[Rutin (trihydrate) (drug)]] (+0.44, unclear); [[Phenytoin (sodium) (drug)]] (+0.44, unclear, ⚠ only 7 significant genes); [[Lucanthone (drug)]] (+0.43, unclear); [[Delamanid (drug)]] (+0.43, unclear, ⚠ only 6 significant genes); [[Tirabrutinib (drug)]] (+0.42, Other TK inhibitor); [[Posaconazole (drug)]] (+0.41, unclear); [[(S)-Crizotinib (drug)]] (+0.41, unclear); [[Dabrafenib (drug)]] (+0.41, RAF inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| KIT | [[PKD1P6]] | moves it that way too | B | KIT activity lowers PKD1P6's level | compounds that target KIT: 3 of 4 raise it (Pexidartinib, Ponatinib, c-Kit-IN-1) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Pexidartinib (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 803, 804, 805
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

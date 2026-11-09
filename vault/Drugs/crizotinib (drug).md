---
drug: "crizotinib"
type: "drug"
salt_base: "crizotinib"
targets: "ALK, MET, ROS1"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 213
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# crizotinib

*Multi-TK inhibitor (inhibitor/antagonist) · targets: ALK, MET, ROS1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 1 / 213; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.29 / 0.23.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B2 | 1 / 0 | — | -0.19 | -0.3/-0.2/+0.3 | — |
| 0.5 µM | [[Plate 08]]:B2 | 1 / 0 | — | +0.13 | -0.1/+0.6/+0.6 | — |
| 5 µM | [[Plate 09]]:B2 | 44 / 169 | — | +0.21 | -2.2/+0.6/+0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[KCNN2]] 1.33× (z +2.9, 0/26 lines)

**0.5 µM** (1 gene, none with an alert): [[RNF212]] 1.42× (z +3.9, 0/12 lines)

**5 µM** (44 genes, none with an alert; 12 shown): [[LPIN1]] 1.28× (z +5.3, 23/48 lines), [[HP1BP3]] 1.21× (z +4.9, 25/48 lines), [[SCD]] 1.40× (z +4.6, 32/48 lines), [[GULP1]] 1.25× (z +4.5, 20/44 lines), [[ACSS2]] 1.35× (z +4.5, 22/47 lines), [[HNRNPM]] 1.25× (z +4.2, 29/48 lines), [[CASTOR2]] 1.30× (z +4.1, 11/47 lines), [[HMGCS1]] 1.41× (z +4.0, 27/47 lines), [[FASN]] 1.52× (z +4.0, 25/47 lines), [[DHCR24]] 1.36× (z +3.9, 15/44 lines), [[ACSL3]] 1.20× (z +3.9, 20/48 lines), [[B3GNT2]] 1.25× (z +3.8, 11/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (169 genes, none with an alert; 12 shown): [[SLIT1]] 0.685× (z -4.9, 8/38 lines), [[RBM43]] 0.652× (z -4.8, 15/44 lines), [[IFI44]] 0.668× (z -4.8, 23/36 lines), [[MT-ND4]] 0.620× (z -4.6, 44/48 lines), [[CASP4]] 0.780× (z -4.6, 19/43 lines), [[EIF2AK2]] 0.767× (z -4.5, 32/47 lines), [[TRIM5]] 0.765× (z -4.5, 23/47 lines), [[ENSG00000253100]] 0.608× (z -4.5, 13/35 lines), [[IFI44L]] 0.588× (z -4.5, 19/26 lines), [[IFI6]] 0.469× (z -4.4, 31/35 lines), [[ANKFN1]] 0.729× (z -4.3, 7/36 lines), [[OAS3]] 0.659× (z -4.3, 28/43 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+2.2) | [[Module 032]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H23 (line)]] (1.44), [[SNU-423 (line)]] (1.42), [[BT-474 (line)]] (1.37), [[A549 (line)]] (1.36) · weakest: [[NCI-H661 (line)]] (0.439), [[SW480 (line)]] (0.660), [[LS 180 (line)]] (0.694) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Crizotinib (hydrochloride) (drug)]] (+0.74, Multi-TK inhibitor); [[(S)-Crizotinib (drug)]] (+0.48, unclear); [[Ivermectin (drug)]] (+0.47, unclear); [[Dihydroartemisinin (drug)]] (+0.42, unclear); [[Pentamidine (isethionate) (drug)]] (+0.40, unclear); [[4EGI-1 (drug)]] (+0.39, Protein synthesis inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Phenytoin (sodium) (drug)]] (+0.39, unclear, ⚠ only 7 significant genes); [[8-Hydroxyquinoline (drug)]] (+0.39, unclear); [[Pentoxifylline (drug)]] (+0.38, unclear); [[BAY1125976 (drug)]] (+0.37, PI3K/AKT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity raises the cells' numbers under crizotinib 5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.84× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[IL15]] | 5 µM | B | IL15 activity raises the cells' numbers under crizotinib 5 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.86× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[IKZF3]] | 5 µM | B | IKZF3 activity lowers the cells' numbers under crizotinib 5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.16× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[TGFBR2]] | 5 µM | B | TGFBR2 activity raises the cells' numbers under crizotinib 5 µM (protects the cells) | lines that do not express TGFBR2 (7) vs lines expressing it (41) | the lines without TGFBR2: 0.84× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[TGFB2]] | 5 µM | B | TGFB2 activity raises the cells' numbers under crizotinib 5 µM (protects the cells) | lines that do not express TGFB2 (15) vs lines expressing it (33) | the lines without TGFB2: 0.90× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CTSF, EHD3, MAP9 |
| [[NSUN5P2-1]] | 5 µM | C | NSUN5P2-1's natural level raises the cells' numbers under crizotinib 5 µM (protects the cells) | NSUN5P2-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71 | 0.250 over the table, 0.021 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MET]] | [[TNFAIP1]] | moves it that way too | B | MET activity raises TNFAIP1's level | compounds that target MET: 3 of 4 lower it (Cabozantinib, Crizotinib / crizotinib, c-Kit-IN-1) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "crizotinib"
- `tables/drugdoses.parquet` — dd in 1114, 1115, 1116
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

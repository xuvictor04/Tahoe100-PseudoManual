---
drug: "Retinoic acid"
type: "drug"
salt_base: "Retinoic acid"
targets: "RARB, RARG, RARA, PPARD"
moa_fine: "Retinoic receptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 648
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Retinoic acid

*Retinoic receptor agonist (activator/agonist) · targets: RARB, RARG, RARA, PPARD · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 648 / 78 / 113; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.26 / 0.48.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A5 | 278 / 370 | — | +0.23 | +4.0/+3.0/+1.6 | — |
| 0.5 µM | [[Plate 05]]:A5 | 56 / 22 | — | -0.04 | -0.1/-0.5/+0.2 | — |
| 5 µM | [[Plate 14]]:A5 | 63 / 50 | 0.815 | +0.30 | -1.8/-0.6/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (278 genes, none with an alert; 12 shown): [[DHRS3]] 1.50× (z +6.7, 29/35 lines), [[NRP2]] 1.46× (z +5.8, 19/24 lines), [[SAMD9]] 1.90× (z +5.3, 34/37 lines), [[DIAPH3]] 1.26× (z +4.9, 24/45 lines), [[MAP1B]] 1.28× (z +4.8, 19/32 lines), [[TGM2]] 1.52× (z +4.7, 26/32 lines), [[GBP1]] 1.64× (z +4.6, 22/32 lines), [[NCAPG]] 1.34× (z +4.5, 23/47 lines), [[TRIM59]] 1.36× (z +4.5, 15/46 lines), [[ETV4]] 1.33× (z +4.4, 21/46 lines), [[SKA1]] 1.34× (z +4.4, 12/46 lines), [[CENPH]] 1.37× (z +4.4, 19/48 lines)

**0.5 µM** (56 genes, none with an alert; 12 shown): [[ACSL3]] 1.81× (z +12.9, 47/48 lines), [[ABCG1]] 2.92× (z +11.5, 28/33 lines), [[ABCA1]] 2.48× (z +10.8, 26/28 lines), [[DHRS3]] 1.71× (z +8.8, 35/35 lines), [[SCD]] 1.75× (z +7.9, 43/48 lines), [[RARB]] 1.63× (z +7.7, 16/20 lines), [[LPCAT3]] 1.48× (z +7.4, 30/48 lines), [[ACACA]] 1.47× (z +6.8, 33/47 lines), [[NRIP1]] 1.46× (z +6.1, 30/40 lines), [[STRA6]] 1.92× (z +5.9, 13/20 lines), [[ENSG00000235609]] 1.32× (z +5.2, 22/40 lines), [[OLMALINC]] 1.47× (z +5.1, 27/47 lines)

**5 µM** (63 genes, none with an alert; 12 shown): [[ACSL3]] 1.65× (z +15.3, 46/49 lines), [[ABCG1]] 2.56× (z +14.3, 29/34 lines), [[ABCA1]] 2.14× (z +12.8, 24/29 lines), [[LPCAT3]] 1.50× (z +10.9, 35/48 lines), [[SCD]] 1.72× (z +10.8, 45/49 lines), [[RARB]] 1.53× (z +9.5, 17/20 lines), [[DHRS3]] 1.46× (z +8.8, 32/36 lines), [[STRA6]] 1.78× (z +7.4, 16/21 lines), [[DLC1]] 1.21× (z +6.4, 16/35 lines), [[OLMALINC]] 1.41× (z +6.4, 29/47 lines), [[SREBF1]] 1.50× (z +6.1, 36/49 lines), [[TINAGL1]] 1.55× (z +6.1, 22/22 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (370 genes, none with an alert; 12 shown): [[ENSG00000273184]] 0.597× (z -6.4, 38/44 lines), [[ENSG00000284697]] 0.537× (z -5.8, 34/48 lines), [[SLC15A2]] 0.547× (z -5.8, 25/46 lines), [[TARS3]] 0.763× (z -5.8, 26/48 lines), [[FBXO42]] 0.693× (z -5.6, 40/48 lines), [[ENSG00000274322]] 0.651× (z -5.6, 31/48 lines), [[CNNM2]] 0.704× (z -5.4, 38/48 lines), [[AUH]] 0.727× (z -5.4, 38/48 lines), [[LINC00862]] 0.645× (z -5.4, 31/47 lines), [[SLC2A3]] 0.616× (z -5.4, 25/33 lines), [[PLAG1]] 0.744× (z -5.3, 25/39 lines), [[ENSG00000257759]] 0.685× (z -5.3, 28/47 lines)

**0.5 µM** (22 genes, none with an alert; 12 shown): [[ARID5B]] 0.781× (z -3.9, 20/42 lines), [[PRR16]] 0.735× (z -3.9, 11/24 lines), [[ADAMTS1]] 0.717× (z -3.9, 10/21 lines), [[TNC]] 0.712× (z -3.8, 14/25 lines), [[PPP1R3C]] 0.681× (z -3.6, 12/26 lines), [[ADGRF4]] 0.660× (z -3.4, 3/21 lines), [[RAB27B]] 0.796× (z -3.4, 9/33 lines), [[CD109]] 0.828× (z -3.3, 11/33 lines), [[SYT7]] 0.812× (z -3.2, 10/39 lines), [[NFATC4]] 0.698× (z -3.1, 7/28 lines), [[GALNT5]] 0.803× (z -3.0, 8/21 lines), [[HMGA2]] 0.773× (z -3.0, 17/39 lines)

**5 µM** (50 genes, none with an alert; 12 shown): [[SCG5]] 0.769× (z -6.0, 14/46 lines), [[LYPD6B]] 0.793× (z -5.1, 6/25 lines), [[ARID5B]] 0.811× (z -4.7, 21/43 lines), [[PRR16]] 0.771× (z -4.6, 17/25 lines), [[ENSG00000287023]] 0.721× (z -4.6, 9/23 lines), [[CUBN]] 0.805× (z -4.6, 10/27 lines), [[HMGA2]] 0.766× (z -4.4, 29/40 lines), [[FAT1]] 0.822× (z -4.3, 25/46 lines), [[PID1]] 0.816× (z -3.9, 9/27 lines), [[LINC02968]] 0.785× (z -3.9, 8/21 lines), [[SNED1]] 0.813× (z -3.9, 13/40 lines), [[SH3RF2]] 0.803× (z -3.8, 13/32 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 016]] (+2.8), [[Module 006]] (+2.7), [[Module 004]] (+2.6) | [[Module 207]] (-3.8), [[Module 179]] (-3.3), [[Module 041]] (-3.3) |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+2.2) | [[Module 194]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (1.42), [[NCI-H1573 (line)]] (1.38), [[A-172 (line)]] (1.32), [[HOP62 (line)]] (1.31) · weakest: [[AN3 CA (line)]] (0.360), [[BT-474 (line)]] (0.513), [[SHP-77 (line)]] (0.579) |
| 0.5 µM | — | [[NCI-H1792 (line)]] (1.58), [[LOX-IMVI (line)]] (1.36), [[COLO 205 (line)]] (1.33), [[A-172 (line)]] (1.32) · weakest: [[AN3 CA (line)]] (0.476), [[NCI-H661 (line)]] (0.497), [[A-427 (line)]] (0.560) |
| 5 µM | — | [[COLO 205 (line)]] (1.46), [[LOX-IMVI (line)]] (1.38), [[NCI-H1792 (line)]] (1.33), [[HT-29 (line)]] (1.31) · weakest: [[NCI-H2122 (line)]] (0.149), [[A-427 (line)]] (0.616), [[NCI-H1573 (line)]] (0.648) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Palmatine (chloride) (drug)]] (+0.94, unclear); [[Megestrol (drug)]] (+0.94, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Busulfan (drug)]] (+0.90, DNA synthesis/repair inhibitor); [[Berbamine (drug)]] (+0.90, unclear); [[Larotrectinib (drug)]] (+0.87, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.86, unclear); [[Diammonium Glycyrrhizinate (drug)]] (+0.78, unclear); [[Trifluridine (drug)]] (+0.75, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Pyridoxine (hydrochloride) (drug)]] (+0.75, unclear); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.74, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[RARA]], [[RARB]], [[RARG]] | [[NRP2]] | moves it that way too | B | RARA, RARB, RARG activity raises NRP2's level | compounds that target RARA, RARB, RARG: 2 of 2 raise it (Retinoic acid, Tazarotene) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

## Data

- `tables/drugs.parquet` — drug == "Retinoic acid"
- `tables/drugdoses.parquet` — dd in 887, 888, 889
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
